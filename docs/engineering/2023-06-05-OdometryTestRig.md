---
title: Odometry Test Rig
parent: Engineering
notebook: engineering
date: 2023-06-05
signatures:
- "Ayla Clark"
- "Caleb Carlson"
nav_order: 2
has_children: false
---

{: .design}
# Define Problem

We currently have no experience with odometry. One thing I (Caleb) want to do this year is use odometry to program our autonomous routines. However, we need a robot to start programming odometry with.

{: .problem}
We need a robot to begin developing our odometry.

{: .design}
# Generate Concepts

Here are some potential solutions we came up with for this ‘testbed’:

* Integrate it into our competition robot.
* Build a simple testbed robot separately.

{: .design}
# Our Decision

Since we have not finished our game analysis yet, it wouldn’t make sense to integrate odometry into our competition robot. 

{: .decision}
As such, we decided to design a simple robot with odometry tracking wheels instead.

{: .design}
# Develop Solution

To speed up the process of building our designs, we use CAD software before we build. The CAD software we use is Autodesk Fusion 360. One convenient thing about Fusion 360 is that it stores all of your files online, this way each team member can almost seamlessly work on the same file, from different computers.

Below you can see the CAD we will build our design from:

> ![placeholder CAD PICTURES](/assets/engineering/TestRigTop.png)![placeholder CAD PICTURES](/assets/engineering/TestRig.png)
> {: .image-pair}
> ![placeholder CAD PICTURES](/assets/engineering/TestRigRight.png)![placeholder CAD PICTURES](/assets/engineering/TestRigFront.png)
> {: .image-pair}
{: .cad}

One thing to note is that we only inserted one tracking wheel into the CAD, this was to make sure we knew exactly what spacing to use to get the tracking wheel to make contact with the center of the robot. 

{: .design}
# Construct & Test

First, we put together the frame of the chassis. Then, we constructed the tracking wheels and attached all the motors and tracking wheels.

![placeholder ConstructionPictures](/assets/engineering/TestRigConstructionFrame.jpg)![placeholder ConstructionPictures](/assets/engineering/TestRigConstructionTrackingWheel.jpg)
{: .image-pair}
![placeholder ConstructionPictures](/assets/engineering/TestRigConstruction.jpg){: width="48%"}

However, by this point, we realized something was wrong. The issue was, that the V5 brain would not support the use of the 393 motors we were intending on using. The 393 motors draw around **4.6 Amps** when under maximum load (stalling), but the 3-wire ports on the V5 brain only support **2 Amps** together.

If we tried to run this robot, we would risk damaging our brain.

{: .design}
# Define Problem

To summarize, our original plan was to use the old 393 motors for the testbed; we discovered that this would not be feasible with the V5 brain.

{: .problem}
We need a new way of powering the drivetrain of our test-rig, without the risk of damaging our robot's brain.

{: .design}
# Generate Concepts

Here are some potential solutions we came up with to solve the problem:

* Use only 2 393 motors and limit the voltage output.
* Use 2 motors from a V5 smart port 3-wire expander (not as limited as the 3-wire ports; supports up to 20 watts)
* Use 4 V5 11-watt motors, but flip them so they are on the outside of the robot.
* Use 4 V5 5.5-watt motors, but flip them so they are on the outside of the robot.

{: .design}
# Our Decision

The first two potential solutions involve a level of risk that we don’t want to take. (A V5 brain costs > $350!) Out of the other two potential solutions, while we don’t necessarily need the power of the 11-Watt motors, because the 5.5-Watt motors are essentially rare commodities at the moment in our robotics program, it wouldn’t be wise to use 4 of them. 

{: .decision}
Using the process of elimination, we decided to simply use 4 of the 11-watt motors.

{: .design}
# Develop Solution

Normally, having motors on the outside of your robot, exposed, would be a very bad idea. The reason this would be a bad idea is that during a competition match, an opposing robot could accidentally ram into you and damage any exposed elements of your robot -- in this case, your motors.

Since we are not using this test rig for competition purposes, this is not an issue.

Aside from any questions of whether this should be done, the switch should be very easy:

1. Remove 393 motors and block bearings.
2. Attach “1-Post Hex Nut Retainer w/ Bearing Flat” in place of where block bearings used to be.
3. Attach the V5 11-watt smart motors.
4. Attach wheels.
5. Wire the robot and perform cable management.
6. Attach Brain, Battery, and Radio.

…And that’s it!

{: .design}
# Construct & Test

Below you can see the test rig with the motors attached, and then wired:

![placeholder ConstructionPictures](/assets/engineering/TestRigConstruction2Unwired.jpg)![placeholder ConstructionPictures](/assets/engineering/TestRigConstruction2Wired.jpg)
{: .image-pair}

The first step in testing our rig was to turn on the brain and verify that all of the motors and sensors are working -- they were. Next, we programmed the robot with a basic tank drive driver control program to see how well it drove.

The test rig was able to drive without any issues.

{: .design}
# Evaluate Solution

Now that we have a test rig, we will be able to begin researching and developing odometry for our robot.