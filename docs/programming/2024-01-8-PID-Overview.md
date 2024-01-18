---
title: PID Overview
parent: Programming
notebook: programming
date: 2024-01-08
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
- "Thomas Reid"
nav_order: 3
has_children: false
---

# Introduction
{: .design}

Last season, I (Caleb) developed a PID feedback algorithm to control the speed of our robot.

## What is a PID?

PID stands for Proportional Integral Derivative. the last two are both named after their respective calculus concepts.

### **Proportional**

Proportional will affect velocity directly proportional to the error. The greater the error, the greater proportional is; The greater the error, the greater your velocity will be.

### **Integral**

The integral will affect the robot's velocity directly proportional to the accumulation of error. If you made a function of error vs time, the Integral would be the integral (area under the curve) of that function.

Integral will help if you have a very small error that proportional cannot take care of; over time (not very much time) this small error will accumulate into a larger error (integral). Eventually Integral will be large enough to overcome this small error, without the help of P.

### **Derivative**

The derivative will affect the velocity of a robot directly proportional to the rate of change of error. If you made a function of error vs time, Derivative would be the derivative (slope) of that function (at a certain point).

This means that as the error drops, the slope/derivative is negative; since velocity is affected directly proportional to the derivative, when the derivative is negative then velocity will be reduced by the derivative portion of a PID.

Essentially, the derivative will make sure that you don’t approach your target too fast.

{% raw %}

{: .design}
# Code & Code Review

## PID.h
```cpp
#pragma once
/**

  *    Module:       PID.h
  *    Author:       Team 98548J (Ace)
  *    Created:      7-14-2022
  *    Description:  Header file for PID class

  * @brief A class for tuneable PIDs
  * @param p Tune this value for proportional.
  * @param i Tune this value for integral.
  * @param d Tune this value for derivative.
  * @param r Tune this for the ramp-up speed.
  * @param integral_cap Sets a limit on the effect of integral (% of motor power).
  * @param speed_cap Sets a maximum output speed for the PID.
  * @param timeout The maximum amount of time the PID will run for.
  * @param not_done A pointer that will be set to false when the PID is done.
  * @param settle_time How many sec the PID will allow itself to 'settle' before stopping.
  
  */
class PID
{
public:

  // PID constants
  double P;
  double I;
  double D;
  double R;

  // PID constraint constants
  double IntegralProximity;
  double IntegralCap;
  double SpeedCap;

  // PID runtime variables
  double RampUp = 0;
  double Error = 0;
  double PreviousError = 0;
  double PIDSpeed;
  double SmartSpeed;
  double Integral = 0;
  double Derivative = 0;

  // PID logic control variables
  bool HasRampedUp = false;
  bool HasReachedEnd = false;
  double TimeReachedEnd = 0;
  double Timeout;
  double SettleTime;
  double Time = 0;
  bool RanOnce = false;
  bool *NotDone;

  PID(double p, double i, double d, double r, double integral_cap, double integral_proximity, double speed_cap, bool *not_done, double timeout, double settle_time);
    
  /**
 * @brief Updates the PID and related tasks.
 * @returns A value representing the output speed/power of the PID.
 * @param error Distance left to travel.
 * @param dt Time elapsed since last call (Delta time).
 */ 
  double Update(double error, double dt);

};
```

## PID.cpp
```cpp
/**
* 
*    Module:       PID.cpp
*    Author:       Team 98548J (Ace)
*    Created:      7-14-2022
*    Description:  Source file for PID class
*
*/

#include "vex.h"

// Function to get the sign of a number (returns -1 for negative, 1 for positive)
int GetSign(double number)
{
    return (number < 0) ? -1 : 1;
}

// Constructor for the PID class
PID::PID(double p, double i, double d, double r, double integral_cap, double integral_proximity, double speed_cap, bool *not_done, double timeout, double settle_time)
{
    // Assigning parameters to corresponding member variables
    P = p;
    I = i;
    D = d;
    R = r;

    IntegralProximity = integral_proximity;
    IntegralCap = integral_cap;
    SpeedCap = speed_cap;
    Timeout = timeout;
    SettleTime = settle_time;

    // Pointer to the "not_done" flag used for external control of the PID loop
    NotDone = not_done;
}

// Function to update the PID controller and compute the control output
double PID::Update(double error, double dt)
{   
    // Update the elapsed time
    Time += dt;

    // Store the previous error
    PreviousError = Error;

    // Update the current error
    Error = error;

    // Calculate the integral term if the error is within the proximity range
    if(std::abs(Error) < IntegralProximity) {
        Integral += error * dt;
    }

    // Calculate the derivative term
    Derivative = (Error - PreviousError) / dt;

    // Cap the integral term to prevent windup
    if(std::abs(Integral) * I > IntegralCap)
    {
        Integral = (IntegralCap * GetSign(Error)) / I;
    }

    // Compute the PID control output
    PIDSpeed = Error * P + Integral * I + Derivative * D;

    // Implement initial ramp-up for smoother control output
    if(!HasRampedUp)
    {
        RampUp += (R * dt) * GetSign(Error);
        if(std::abs(RampUp) < std::abs(PIDSpeed))
        {
            SmartSpeed = RampUp;
        }
        else
        {   
            HasRampedUp = true;
            SmartSpeed = PIDSpeed;
        }
    }
    else
    {
        SmartSpeed = PIDSpeed;
    }

    // Cap the control output to the specified speed limit
    if(std::abs(SmartSpeed) > SpeedCap)
    {
        SmartSpeed = SpeedCap * GetSign(SmartSpeed);
    }

    // Check for change in sign of error to signal reaching the target
    if(GetSign(Error) != GetSign(PreviousError) && RanOnce == true && HasReachedEnd == false)
    {
        HasReachedEnd = true;
        TimeReachedEnd = Time;
    }

    // Check if the system has reached the target and settled
    if(HasReachedEnd == true && Time - TimeReachedEnd > SettleTime)
    {
        *NotDone = false;
    }

    // Check if the specified timeout has been exceeded
    if(Time > Timeout)
    {
        *NotDone = false;
    }

    // Set the flag to indicate that the PID loop has executed at least once
    RanOnce = true;

    // Return the computed control output
    return SmartSpeed;
}

```
{% endraw %}