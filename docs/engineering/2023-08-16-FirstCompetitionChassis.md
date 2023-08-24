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
Define Problem

In our previous entry, we detailed how we designed, built, and tested 7 different drivetrains. The purpose of these tests was to figure out what the best wheel layout for our drivetrain would be. The results of our tests are shown in this entry.

{: .problem}
We need to decide exactly which wheel configuration we will use, the speed of the chassis, and the size footprint of our drivetrain.

{: .design}
Generate Concepts

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
Our Decision

## Wheel Configuration -

From our earlier testing, both concepts [#1]({{site.url}}/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20drivetrain%20with%206%204%E2%80%9D%20wheels.), and [#2]({{site.url}}/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20drivetrain%20with%204%204%E2%80%9D%20wheels%20and%20small%20flex%20wheels%20in%20the%20middle.) performed flawlessly during [our testing]({{site.url}}/docs/engineering/2023-06-08-ChassisPrototypeTests.html#:~:text=(This%20test%20includes%20all%207%20chassis%2C%20including%20the%20adjustable%20chassis)%3A). However, because 4" wheels are used for both of those concepts, we are limited in the gear ratio options we can use (the size of 4" wheels forces you to use larger gears). Additionally, 4" wheels take up a lot of space in a chassis, making future additions to the robot more difficult. 

Unlike the first two concepts, concept [#3]({{site.url}}/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20drivetrain%20with%204%203.25%E2%80%9D%20wheels%20and%20small%20flex%20wheels%20in%20the%20middle.) uses 3.25" wheels. These wheels will give us a lot more space to build future additions to our robot. One potential catch to using this idea is that, according to [our testing]({{site.url}}/docs/engineering/2023-06-08-ChassisPrototypeTests.html#:~:text=(Adjustable)%20Four%2D3.25%E2%80%9D%20%2B%20Two%20Flex), this style of drivetrain did **not** perform flawlessly; this style of chassis wasn't able to complete **one of ten** of the high-centered jump tests.

To mitigate this risk, we made one change to idea #3. This change was to attach a total of 4 flex wheels in between the main wheels (two flex wheels on each side). The idea behind this change is that the additional flex wheel on each side should give the drivetrain more purchase on the barrier as it goes over.

We predict that the addition of two flex wheels, as well as the compactness of the 3.25" wheels will make idea #3 the better option.

## Chassis Width & Length -

Our team immediately eliminated idea [#1]({{site.url}}/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20large%20chassis.%20(35%20holes%20in%20each%20dimension)) from consideration because a full-width chassis would limit our driver's maneuverability. Idea [#2]({{site.url}}/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20skinny%20chassis.%20(25%20holes%20wide%2C%2035%20holes%20long)) would provide us with a lot of maneuverability (especially while driving underneath an elevation bar), however, because of its width (or lack thereof), mechanisms that intake tri-balls and manipulate them will be severely limited in space. On the other hand, while idea [#3]({{site.url}}/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20wide%20chassis.%20(25%20holes%20long%2C%2028%20holes%20wide)) is slightly wider than the skinny chassis, it's still not too wide. Additionally, the added space for building in the front and back due to its length will make adding an intake easier.

## Chassis Speed -

As we have decided not to use 4" wheels, we don't have to consider idea [#1]({{site.url}}/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20very%20fast%20chassis%20(~62%20inches%20per%20second)). We know that speed is your friend during a timed competition. As such we decided to go with idea [#2]({{site.url}}/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20fast%20chassis%20(~61%20inches%20per%20second)) because it is the fastest gear ratio out of the remaining concepts.

{: .decision}
> Here is a summary of the decisions we made:
> * Idea [#3]({{site.url}}/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20drivetrain%20with%204%203.25%E2%80%9D%20wheels%20and%20small%20flex%20wheels%20in%20the%20middle.). A drivetrain with 4 3.25” wheels and small flex wheels in the middle.
> * Idea [#3]({{site.url}}/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20wide%20chassis.%20(25%20holes%20long%2C%2028%20holes%20wide)). A wide chassis. (25 holes long, 28 holes wide) 
> * Idea [#2]({{site.url}}/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=A%20fast%20chassis%20(~61%20inches%20per%20second)). A fast chassis ***(~61 inches per second)***

{: .design}
Develop Solution

Below you can see the layout of the gears and wheels we would use:

![FirstDrivetrainGears](/assets/engineering/FirstDrivetrainGears.png)

Rather than using a 6-motor drivetrain (66 watts), we want to make a 55-watt drivetrain. To do this, we would replace two of the regular V5 smart motors with some 5.5-watt motors.

To mount the 5.5-watt motors, we had to make a special mounting bracket. Below you can see the CAD used for the bracket:

![5.5-wattBracket](/assets/engineering/5.5WVerticalISO.png){: width="45%"} ![5.5-wattBracket](/assets/engineering/5.5WVerticalRight.png){: width="54%"}

And, here is our CAD with the addition of bearings, axles, motors, wheels, and other necessary components:

![FirstDrivetrainHalf](/assets/engineering/FirstDrivetrainHalf.png)

Once we had one half of the chassis in CAD, we simply mirrored the part, and jointed the two halves together with the rest of our robot's structure:

![FirstDrivetrainTop](/assets/engineering/FirstDrivetrainTop.png){: width="45%"}
![FirstDrivetrainTop](/assets/engineering/FirstDrivetrainISO.png){: width="54%"}
![FirstDrivetrainTop](/assets/engineering/FirstDrivetrainRight.png){: width="48%"}
![FirstDrivetrainTop](/assets/engineering/FirstDrivetrainFront.png){: width="48%"}

{: .design}
Construct & Test

Now that we have finished the CAD of our base chassis, we will build it according to the CAD. That way, there will be as few mistakes as possible, and because the CAD is so detailed, we won't need to figure out spacing when we build it. This method also keeps the chassis square and causes the least friction. Untimely leading to a more successful drive train.

With the help of the CAD, we were able to construct the chassis in only a few hours. The chassis is very smooth-running and has almost no friction. Using CAD allowed us to work out any problems with the chassis we had beforehand which saved so much time in the end. 

There was one thing that differed from the CAD on the chassis was instead of a screw joint on the wheel, we changed it to a regular axle so that it would move smoother. The screw joint was causing friction, and changing it eliminated all the friction. 

We plan to test the new chassis in our club scrimmage on Thursday. That way, we can compare our drive train to others and then reevaluate to see if there are any adjustments we can consider. However, with all the testing and CAD work we have done, I don't see much that we could adjust other than making a cover for the gears that contact the bar slightly. 

Along with the scrimmage, we ran the same tests on this chassis as we did on the previous test chassis. Below are the results of the scrimmage and tests we ran. 
