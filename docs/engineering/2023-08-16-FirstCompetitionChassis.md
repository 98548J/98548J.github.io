---
title: First Competition Chassis
parent: Engineering
notebook: engineering
date: 2023-08-16
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
nav_order: 4
has_children: false
---

{: .design}
# Define Problem

In our previous entry, we detailed how we designed, built, and tested 7 different drivetrain's. The purpose of these tests was to figure out what the best wheel layout for our drivetrain would be. The results of our tests are shown in this entry.

{: .problem}
We need to decide exactly which wheel configuration we will use, the speed of the chassis, and the size footprint of our drivetrain.

{: .design}
# Generate Concepts

Here are some potential solutions we came up with, all of these concepts were based on our testing data.

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

From our earlier testing, both concepts [#1](/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20drivetrain%20with%206%204%E2%80%9D%20wheels.), and [#2](/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20drivetrain%20with%204%204%E2%80%9D%20wheels%20and%20small%20flex%20wheels%20in%20the%20middle.) performed flawlessly during [our testing](/docs/engineering/2023-06-08-ChassisPrototypeTests.html#:~:text=(This%20test%20includes%20all%207%20chassis%2C%20including%20the%20adjustable%20chassis)%3A). However, because 4" wheels are used for both of those concepts, we are limited in the gear ratio options we can use (the size of 4" wheels forces you to use larger gears). Additionally, 4" wheels take up a lot of space in a chassis, making future additions to the robot more difficult. 

Unlike the first two concepts, concept [#3](/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20drivetrain%20with%204%203.25%E2%80%9D%20wheels%20and%20small%20flex%20wheels%20in%20the%20middle.) uses 3.25" wheels. These wheels will give us a lot more space to build future additions to our robot. One potential catch to using this idea is that, according to [our testing](/docs/engineering/2023-06-08-ChassisPrototypeTests.html#:~:text=(Adjustable)%20Four%2D3.25%E2%80%9D%20%2B%20Two%20Flex), this style of drivetrain did **not** perform flawlessly; this style of chassis wasn't able to complete **one of ten** of the high-centered jump tests.

To mitigate this risk, we made one change to idea #3. This change was to attach a total of 4 flex wheels in between the main wheels (two flex wheels on each side). The idea behind this change is that the additional flex wheel on each side should give the drivetrain more purchase on the barrier as it goes over.

We predict that the addition of two flex wheels, as well as the compactness of the 3.25" wheels will make idea #3 the better option.

## Chassis Width & Length -

Our team immediately eliminated idea [#1](/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20large%20chassis.%20(35%20holes%20in%20each%20dimension)) from consideration because a full-width chassis would limit our driver's maneuverability. Idea [#2](/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20skinny%20chassis.%20(25%20holes%20wide%2C%2035%20holes%20long)) would provide us with a lot of maneuverability (especially while driving underneath an elevation bar), however, because of its width (or lack thereof), mechanisms that intake tri-balls and manipulate them will be severely limited in space. On the other hand, while idea [#3](/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20wide%20chassis.%20(25%20holes%20long%2C%2028%20holes%20wide)) is slightly wider than the skinny chassis, it's still not too wide. Additionally, the added space for building in the front and back due to its length will make adding an intake easier.

## Chassis Speed -

As we have decided not to use 4" wheels, we don't have to consider idea [#1](/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20very%20fast%20chassis%20(~62%20inches%20per%20second)). We know that speed is your friend during a timed competition. As such we decided to go with idea [#2](/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20fast%20chassis%20(~61%20inches%20per%20second)) because it is the fastest gear ratio out of the remaining concepts.

{: .decision}
> Here is a summary of the decisions we made:
> * Idea [#3](/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20drivetrain%20with%204%203.25%E2%80%9D%20wheels%20and%20small%20flex%20wheels%20in%20the%20middle.). A drivetrain with 4 3.25” wheels and small flex wheels in the middle.
> * Idea [#3](/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20wide%20chassis.%20(25%20holes%20long%2C%2028%20holes%20wide)). A wide chassis. (25 holes long, 28 holes wide) 
> * Idea [#2](/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20fast%20chassis%20(~61%20inches%20per%20second)). A fast chassis ***(~61 inches per second)***

{: .design}
# Develop Solution

Below you can see the layout of the gears and wheels we would use:

![FirstDrivetrainGears](/assets/engineering/FirstDrivetrainGears.png)
{: .cad}

Rather than using a 6-motor drivetrain (66 watts), we want to make a 55-watt drivetrain. To do this, we would replace two of the regular V5 smart motors with some 5.5-watt motors.

To mount the 5.5-watt motors, we had to make a special mounting bracket. Below you can see the CAD used for the bracket:

![5.5-wattBracket](/assets/engineering/5.5WVerticalISO.png){: width="45%"}![5.5-wattBracket](/assets/engineering/5.5WVerticalRight.png){: width="54%"}
{: .image-pair}
{: .cad}


And, here is our CAD with the addition of bearings, axles, motors, wheels, and other necessary components:

![FirstDrivetrainHalf](/assets/engineering/FirstDrivetrainHalf.png)
{: .cad}

Once we had one half of the chassis in CAD, we simply mirrored the part, and joined the two halves together with the rest of our robot's structure:

![FirstDrivetrainTop](/assets/engineering/FirstDrivetrainTop.png){: width="45%"}
![FirstDrivetrainTop](/assets/engineering/FirstDrivetrainISO.png){: width="54%"}
![FirstDrivetrainTop](/assets/engineering/FirstDrivetrainRight.png){: width="48%"}
![FirstDrivetrainTop](/assets/engineering/FirstDrivetrainFront.png){: width="48%"}
 {: .cad}

{: .design}
# Construct

Now that we have finished the CAD of our base chassis, we will build it according to the CAD. That way, there will be as few mistakes as possible, and because the CAD is so detailed, we won't need to figure out spacing when we build it. This method also keeps the chassis square and causes the least friction. Untimely leading to a more successful drive train.

Below you can see some pictures showing one side of the drivetrain as it is being constructed:

![FirstDrivetrainPartiallyConstructedHalf](/assets/engineering/FirstDrivetrainPartiallyConstructedHalf.jpg){: width="48%"}
![FirstDrivetrainHalf](/assets/engineering/FirstDrivetrainHalf.jpg){: width="48%"}

Below is one 5.5-watt motor vertical mounting bracket constructed:

![5.5wattmount](/assets/engineering/5.5wattmount.jpg){: width="48%"}
![5.5wattmountfront](/assets/engineering/5.5wattmountfront.jpg){: width="48%"}

Below is the completed chassis with both halves attached, and to the right is a render of our CAD for reference:

![CompletedFirstDrivetrain](/assets/engineering/CompletedFirstDrivetrainPIC3.jpg){: width="45%"}
![CompletedFirstDrivetrainCAD](/assets/engineering/CompletedFirstDrivetrainCAD3.png){: width="54%"}
{: .cad}

With the help of the CAD, we were able to construct the chassis in only a few hours. The chassis is very smooth-running and has almost no friction.

We plan to test this new chassis in our scrimmage on Thursday. That way, we can compare our drivetrain to others and then reevaluate to see if there are any adjustments we can consider. Along with the scrimmage, we ran the same tests on this chassis as we did on the previous test chassis. Below are the results of the scrimmage and tests:

{: .design}
# Test

To test this chassis, we ran the same tests as we did for our [drivetrain prototypes](/docs/engineering/2023-06-08-ChassisPrototypeTests.html#:~:text=(This%20test%20includes%20all%207%20chassis%2C%20including%20the%20adjustable%20chassis)%3A); each test was run 10 times, and the results were recorded as a percentage. Below, you can see our results:

| Momentum Jump | Contact Jump | High-Centered Jump|
|:---:|:---:|:---:|
| 100% | 100% | 100% |

From this testing data, we can see that the [conclusions](/docs/engineering/2023-06-08-ChassisPrototypeTests.html#evaluate-solution) we had drawn from our drivetrain prototype testing previously have proven accurate. The use of flex wheels in between the drivetrain's main wheels allows the chassis to drive over the barrier much easier.

## Scrimmage -

During the scrimmage, we won all of our matches. This shows that this chassis performs well. **However**, although we won all of our matches, throughout the scrimmage, **our robot's motors would very quickly heat up**; this is a problem because when a V5 smart motor gets too hot, it will limit the amount of voltage that can be applied to the motor. The effect of this thermal throttling is that our robot will accelerate slower, have a lower top speed, and also have a very low torque. Sometimes, when the motors are thermal throttling, the chassis is unable to go over the barrier.

{: .design}
# Evaluate Solution

In summary, here is what we have learned from this chassis:

* Our chassis is too fast; it overheats too quickly.
* Using two flex wheels per drivetrain side is an effective way to assist in driving over the barrier.

Now that we are aware of these advantages and disadvantages, we will be able to make a much better chassis in the future.