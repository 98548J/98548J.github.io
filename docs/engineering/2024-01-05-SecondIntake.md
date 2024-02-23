---
title: Second Intake
parent: Engineering
notebook: engineering
date: 2023-01-05
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
- "Thomas Reid"
nav_order: 14
has_children: false
---

{: .design}
# Define Problem

We require an intake mechanism that can easily pick up the tri-balls from the ground and transfer them to the catapult, without taking up too much space like our previous robots. Additionally, the intake mechanism should be able to grip the tri-balls firmly without exerting excessive force on the motor. 

{: .problem}
We need to choose a catapult that can elevate to avoid robots with blockers and fire at a high rate.

{: .design}
# Generate Concepts

 We already generated some concepts in the rebuilding entry so here is a summary of the concepts. When it comes to designing an intake mechanism, there are a few different options to choose from, including a single stage, double stage, and claw. A single-stage intake mechanism has one roller with rubber bands that helps to intake tri-balls. A double stage is similar but has an additional roller, making it bulkier and heavier, which can make it more challenging to use. On the other hand, a claw mechanism only clamps onto a single tri-ball to move it. While it is slower than the other two options, it cannot put tri-balls into a robot.

Considering these factors, we decided to create a new intake mechanism that would be more efficient and user-friendly. While our previous double-stage intake mechanism performed well, it was bulky and challenging to use. Therefore, we chose to design a new single-stage intake mechanism that would be less bulky and easier to operate. This new mechanism would allow us to intake objects quicker and more effectively into our elevated catapult than the previous one.

{: .decision} 
After some deliberation we decided that we would use a kicker as our form of launching tri-balls this would also be very easy to make it elevate.

{:.design}
# Construction

When we were constructing the intake, we decided to use two pieces of c-channel arms pivoting on screws. This allows the intake to move up and down freely as we encounter the goal or other robots. To provide the best grip on the tri-balls, we kept the rubber bands. We used sprockets to hold the rubber bands in the grooves to keep them evenly spaced and prevent them from moving around. As well as Instead of using two 5.5-watt motors, we chose to use one single-watt motor to save space and ensure a clean operation. We also made polycarbonate ramps for the intake to slide up the goal so we don't go inside it.

{:.design}
# Testing
Once we finished constructing our intake, we planned to perform a series of tests. These included in-taking tri-balls from a corner, in-taking them from the central bar, and out-taking them while a tri-ball was inside the robot. During these tests, we will randomly position the tri-balls to ensure the accuracy of our results.

## Results 

| | Corner Intake| Central Bar Intake | Inside Robot |
|:---|:---:|:---:|:---:|
| Corner down | 100% | 100% | 100% |
|  Flat side on the ground  | 100% | 100% | 100% |
| Thrown/ Random | 100% | 100% | 100% |

{:.design}
# Summary 

Based on the test results, the intake has performed well and it fulfills all the requirements we were looking for. The new intake has a reduced bulk, while still providing the same grip and range as the old one. In addition, it is stronger and can withstand contact with robots and the field exceptionally well.