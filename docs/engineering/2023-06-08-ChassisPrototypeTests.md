---
title: Chassis Prototype Tests
parent: Engineering
notebook: engineering
date: 2023-06-08
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
nav_order: 3
has_children: false
---

{: .design}
# Define Problem

This season presents our robots with a unique challenge; there is a (non-trivially tall) barrier spanning the field:

![barrier](/assets/engineering/Barrier.png)

Because our team has never encountered such a (literal) obstacle before, we don't know what the most effective method of traversing such an obstacle would be.

{: .problem}
We need to find out what features make a good chassis for this season.

{: .design}
# Generate Concepts

Here are some potential ways we could solve our problem:

1. Design, build, and test multiple chassis, each with unique characteristics.
2. Look on VEX forum and YouTube for any robots already built that perform well.
3. Make our best educated-guesses about what kind of characteristics will perform the best on a chassis, and start building.

{: .design}
# Our Decision

We are all in agreement that the last concept (#3) is a poor choice. And while option #2 would probably work, we wouldn't know **why** the chassis we built is good.

{: .decision}
The option that would allow us to learn the most, is option #1. (Also, this solution would adhere to the design process).

{: .design}
# Develop Solution

First, we will install Fusion 360 on our personal computers and create a shared folder for easy access to all team members. However, the robotics room will be closed from June 16 to August 1, which means that we will have to halt production of the robot until we can meet as a team again. In the meantime, we will focus on completing the chassis so that we can have a quick start when we resume working together.

Ayla and Caleb are experienced with Fusion and will handle most of the CAD work. They'll use a downloadable parts file library to avoid fabricating every piece used on the robot; instead of spending time creating CAD files for individual parts, we can create assemblies using pre-made CAD files. During the break, Ayla also plans to start CAD work on other subsystems of the robot after the chassis has been completed.

Once we are done designing a chassis in CAD, we will build and test it.

{: .note}
For our seven different chassis designs, we first made a CAD model of **a single small robot** with four 4” wheels, over time we realized that it would be **much easier** to make **a modular chassis** that could be easily adapted for other test modes by switching out wheels. The adjustable chassis was designed with 6 modes in mind. See the below images:

| First Chassis: | Adjustable Chassis: |
|:---:|:---:|
|![first chassis](/assets/engineering/4 inch 4 wheel HOME.png) | ![adjustable](/assets/engineering/HOME.png) |

## Configurations:

![adjustable](/assets/engineering/4 inch 4 wheel RIGHT.png){: width="32.5%"}
![adjustable](/assets/engineering/4 inch 4 wheel 2 flex RIGHT.png){: width="32.5%"}
![adjustable](/assets/engineering/4 inch 6 wheel RIGHT.png){: width="32.5%"}
![adjustable](/assets/engineering/3.75 inch 4 wheel RIGHT.png){: width="32.5%"}
![adjustable](/assets/engineering/3.75 inch 4 wheel 2 flex RIGHT.png){: width="32.5%"}
![adjustable](/assets/engineering/3.75 inch 6 wheel RIGHT.png){: width="32.5%"}
 {: .cad}

The images depicted above show the seven chassis that we will be testing. We plan to gather data on both designs and incorporate the best features into another CAD model.

{: .design}
# Construct

We aim to first build, and test each chassis, determining their strengths and weaknesses through our testing. This will help us identify the features that work well and those that don't.

Our testing procedure involves multiple runs over the center bar to determine its success rate. We will document each instance of success and failure, along with the reason for any failures.

After completing construction, we will move on to testing the functionality of each drivetrain to evaluate how well it performs during game tasks. Here are some pictures showing the first drivetrain, and the first test mode of the adjustable chassis:

![smallerChassis](/assets/engineering/MinniChassis2.jpg)![adjustableChassis](/assets/engineering/AdjustableChassisSide.jpg)
{: .image-pair}

{: .design}
# Test

To become familiar with the smallest robot, our driver, Tucker, ran some driver skills. He completed a total of six runs and the following scores were obtained. The average skills score obtained was **6.5**:

| Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Run 6 |
|:---:|:---:|:---:|:---:|:---:|:---:|
|2|7|4|12|6|8|

We then conducted a series of tests involving the central bar:

1. Start driving at the bar early, building up momentum before driving over the bar.
2. Start driving where the robot is contacting the bar, then drive over.
3. Manually high center the robot on the bar, and see if it can drive off of it.

| First Test - Distance | Second Test - Contacting | Third Test - High Centered |
|:---:|:---:|:---:|
|![Distance](/assets/engineering/Distance.jpg) | ![Contact](/assets/engineering/Contact.jpg) | ![HighCentered](/assets/engineering/HighCentered.jpg) |

Below you can see the results of our barrier tests, each trial had 10 tests, and the result of those 10 tests is shown in percentage as a success rate; higher is better.

(This test includes all 7 chassis, including the adjustable chassis):

| | Momentum Jump | Contact Jump | High-Centered Jump|
|:---|:---:|:---:|:---:|
| (Small) Four-4” | 100% | 100% | 100% |
| (Adjustable) Six-4”  | 100% | 100% | 100% |
| (Adjustable) Four-4” + Two Flex | 100% | 100% | 100% |
| (Adjustable) Four-4” | 100% | 100% | 30% |
| (Adjustable) Six-3.25” | 40% | 80% | 80% |
| (Adjustable) Four-3.25” + Two Flex | 100% | 100% | 90% |
| (Adjustable) Four-3.25” | 0% | 1% | 0% |

{: .design}
# Evaluate Solution

During the testing phase, we discovered the advantages and disadvantages of each drivetrain configuration. As a result, we now have the necessary information to construct a high-performing chassis for our competition robot. Here is a list of things we have learned about what did and didn't work, as well as ideas we want to incorporate into our competition robot:

## Advantages

* Having larger wheels makes jumping over the bar easier.
* Using flex wheels in the middle adds traction when going over the center bar; in many cases preventing the chassis from getting high-centered.
* Using flex wheels in the middle protects the gears and motors of the drivetrain from being hit by the barrier.
* Having smaller wheels in the center helps the drive train to drive over the bar smoother and faster compared to larger diameter center wheels.

## Disadvantages

* Large distances between wheels; increase the chance of becoming high-centered.
* Motor placement too close to the front (exposed motors) can potentially damage the motor from repeated violent contact with the barrier.
* Without a guard or wheel in the middle, the gears hit the barrier while going over.
* Having wheels in the center of the chassis that are too big makes driving over the barrier a rough, and slow ride.