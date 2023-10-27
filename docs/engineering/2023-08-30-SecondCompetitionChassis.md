---
title: Second Competition Chassis
parent: Engineering
notebook: engineering
date: 2023-08-30
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
nav_order: 5
has_children: false
---

{: .design}
# Define Problem

In the previous entry, we described how we designed, built, and tested our first competition chassis. However, after testing the chassis we made there was one small problem:

{: .problem}
Our current chassis is too fast; it has too little torque to accelerate and decelerate as needed. Prolonged use of our current chassis will cause the motors to heat up, and thermal throttle.

{: .design}
# Generate Concepts

We had already come up with a decent list of potential drivetrain configurations in the previous entry. Here is that list:

## Wheel Configurations -

1. A drivetrain with 6 4” wheels.
2. A drivetrain with 4 4” wheels and small flex wheels in the middle.
3. A drivetrain with 4 3.25” wheels and small flex wheels in the middle.

## Chassis Widths & Lengths -

1. A large chassis. (35 holes in each dimension)
2. A skinny chassis. (25 holes wide, 35 holes long)
3. A wide chassis. (25 holes long, 28 holes wide) 

## Chassis Speeds -

1. A very fast chassis ***(~62 inches per second)***
   * 200 Rpm Motors -> 72 Tooth Gear -> 48** Tooth Gear -> 4.0" Wheels
2. A fast chassis ***(~61 inches per second)***
   * 600 Rpm Motors -> 36 Tooth Gear -> 60 Tooth Gear -> 3.25" Wheels
3. An average speed chassis ***(~56 inches per second)***
   * 200 Rpm Motors -> 60 Tooth Gear -> 36 Tooth Gear -> 3.25" Wheels
4. A slower chassis ***(~51 inches per second)***
   * 600 Rpm Motors -> 36 Tooth Gear -> 72 Tooth Gear -> 3.25"

{: .design}
# Our Decision

## Wheel Configuration -

The wheel configuration of our [previous chassis]({{site.url}}/docs/engineering/2023-08-16-FirstCompetitionChassis.html#develop-solution) worked very well and was able to complete all the tasks we threw at it. As such, we will keep our current wheel configuration.

## Chassis Width & Length -

Again, we thought that the size of our [previous chassis]({{site.url}}/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=%233.-,A%20wide%20chassis.%20(25%20holes%20long%2C%2028%20holes%20wide),-Idea%20%232.%20A) (25 holes long, 28 holes wide) was good. As such, we will keep our current chassis width and length.

## Chassis Speed -

As we have decided not to use 4" wheels, we don't have to consider idea [#1]({{site.url}}/docs/engineering/2023-08-28-SecondCompetitionChassis.html#:~:text=A%20very%20fast%20chassis%20(~62%20inches%20per%20second)). We previously acted under the assumption that ***"The faster your robot is the better!"***, however, we now realize that this is **not the case**. We still want to have a decent-speed chassis, but we don't want to be too fast. idea [#4]({{site.url}}/docs/engineering/2023-08-28-SecondCompetitionChassis.html#:~:text=A%20slower%20chassis%20(~51%20inches%20per%20second)) fits this description; while it is the slowest chassis speed we brainstormed, it is still fairly fast (compared to, say, 4" wheels at 200 Rpm).

{: .decision}
> Here is a summary of the decisions we made:
> * Idea [#3]({{site.url}}/docs/engineering/2023-08-28-SecondCompetitionChassis.html#:~:text=A%20drivetrain%20with%204%203.25%E2%80%9D%20wheels%20and%20small%20flex%20wheels%20in%20the%20middle.). A drivetrain with 4 3.25” wheels and small flex wheels in the middle.
> * Idea [#3]({{site.url}}/docs/engineering/2023-08-28-SecondCompetitionChassis.html#:~:text=A%20wide%20chassis.%20(25%20holes%20long%2C%2028%20holes%20wide)). A wide chassis. (25 holes long, 28 holes wide) 
> * Idea [#2]({{site.url}}/docs/engineering/2023-08-28-SecondCompetitionChassis.html#:~:text=A%20fast%20chassis%20(~61%20inches%20per%20second)). A slower chassis ***(~51 inches per second)***

{: .design}
# Develop Solution

Now that we know what we are going to build for our chassis, we can start to figure out exactly **how** we are going to build it. To do this we use CAD.

The first step was to make a CAD of the gear layout for our drivetrain. Below you can see the initial layout we made:

![FirstGearLayout](/assets/engineering/SecondRobot/FirstChassisGears.png)
![FirstGearAndWheelLayout](/assets/engineering/SecondRobot/ChassisFirst1.png)
{: .cad}

However, at this point, we noticed a problem with our current CAD.

{: .design}
# Define Problem

There are large gaps between the flex wheels and omni wheels. These gaps will make it much more difficult for us to drive over the barrier:

![FirstGearAndWheelLayoutProblem](/assets/engineering/SecondRobot/ChassisFirst.png)
{: .cad}

{: .problem}
> The problem is this:
> * Our current CAD design will likely become stuck on the barrier.

{: .design}
# Generate Concepts

Here are a few options we came up with to fix our problem:

1. Research to find a different gear ratio which would allow us to reduce the gaps in our drivetrain.
2. Move the gears (not attatched to the c-channel) vertically down, below the axles of our wheels.
3. Move everything vertically down relative to the obstructive c-channel.


{: .design}
# Our Decision

We discussed each potential solution as a team to identify which one would work best for us.

Concept [#1]({{site.url}}/docs/engineering/2023-08-30-SecondCompetitionChassis.html#:~:text=Research%20to%20find%20a%20different%20gear%20ratio%20which%20would%20allow%20us%20to%20reduce%20the%20gaps%20in%20our%20drivetrain.) would likely work; however, we feel like there should be a way to modify the ***layout*** of our current gear ratio to achieve the same effect.

Concept [#3]({site.url}/docs/engineering/2023-08-30-SecondCompetitionChassis.html#:~:text=Move%20everything%20vertically%20down%20relative%20to%20the%20obstructive%20c%2Dchannel.) would also likely work; however, this would force us to attach our motors horizontally instead of vertically. This is a problem because the motors would then be taking up space where we may build an intake for our robot in the future.

This leaves concept [#2]({{site.url}}/docs/engineering/2023-08-30-SecondCompetitionChassis.html#:~:text=Move%20the%20gears%20(not%20attatched%20to%20the%20c%2Dchannel)%20vertically%20down%2C%20below%20the%20axles%20of%20our%20wheels.) as our last remaining option.

{: .decision}
>We will use idea [#2]({{site.url}}/docs/engineering/2023-08-30-SecondCompetitionChassis.html#:~:text=Move%20the%20gears%20(not%20attatched%20to%20the%20c%2Dchannel)%20vertically%20down%2C%20below%20the%20axles%20of%20our%20wheels.): 
> * Move the gears (not attatched to the c-channel) vertically down, below the axles of our wheels.

{: .design}
# Develop Solution

Below you can see a CAD screenshot of the gears after we moved them down. Specifically, we moved the inner gears between the large outer gears down exactly 0.5 inches. Additionally, you can see the supporting framework structure of the drivetrain in the second picture.

![SecondGearLayout](/assets/engineering/SecondRobot/SecondChassisGears.png)
![SecondGearLayoutWithSupports](/assets/engineering/SecondRobot/SecondChassisFlexDisplay.png)
{: .cad}

{: .design}
# Evaluate Solution

