---
title: Second Competition Chassis
parent: Engineering
notebook: engineering
date: 2023-08-30
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
- "Thomas Reid"
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

The wheel configuration of our [previous chassis](/docs/engineering/2023-08-16-FirstCompetitionChassis.html#develop-solution) worked very well and was able to complete all the tasks we threw at it. As such, we will keep our current wheel configuration.

## Chassis Width & Length -

Again, we thought that the size of our [previous chassis](/docs/engineering/2023-08-16-FirstCompetitionChassis.html#:~:text=%233.-,A%20wide%20chassis.%20(25%20holes%20long%2C%2028%20holes%20wide),-Idea%20%232.%20A) (25 holes long, 28 holes wide) was good. As such, we will keep our current chassis width and length.

## Chassis Speed -

As we have decided not to use 4" wheels, we don't have to consider idea [#1](/docs/engineering/2023-08-28-SecondCompetitionChassis.html#:~:text=A%20very%20fast%20chassis%20(~62%20inches%20per%20second)). We previously acted under the assumption that ***"The faster your robot is the better!"***, however, we now realize that this is **not the case**. We still want to have a decent-speed chassis, but we don't want to be too fast. idea [#4](/docs/engineering/2023-08-28-SecondCompetitionChassis.html#:~:text=A%20slower%20chassis%20(~51%20inches%20per%20second)) fits this description; while it is the slowest chassis speed we brainstormed, it is still fairly fast (compared to, say, 4" wheels at 200 Rpm).

{: .decision}
> Here is a summary of the decisions we made:
> * Idea [#3](/docs/engineering/2023-08-28-SecondCompetitionChassis.html#:~:text=A%20drivetrain%20with%204%203.25%E2%80%9D%20wheels%20and%20small%20flex%20wheels%20in%20the%20middle.). A drivetrain with 4 3.25” wheels and small flex wheels in the middle.
> * Idea [#3](/docs/engineering/2023-08-28-SecondCompetitionChassis.html#:~:text=A%20wide%20chassis.%20(25%20holes%20long%2C%2028%20holes%20wide)). A wide chassis. (25 holes long, 28 holes wide) 
> * Idea [#2](/docs/engineering/2023-08-28-SecondCompetitionChassis.html#:~:text=A%20fast%20chassis%20(~61%20inches%20per%20second)). A slower chassis ***(~51 inches per second)***

{: .design}
# Develop Solution

Now that we know what we are going to build for our chassis, we can start to figure out exactly **how** we are going to build it. To do this we use CAD.

The first step was to make a CAD of the gear layout for our drivetrain. Below you can see the initial layout we made:

![FirstGearLayout](https://lh3.googleusercontent.com/pw/ABLVV865TAKnnvmD8fUQngNREaohrkXnOaAohBRcNSSEPbxq5fV5qssA8zdpF9oyb6nSF3PX4gVkSp0vzM9FQF0pLzjW0rG79NhhS4T8JDWtne6XhFkHGcbhKumjt3u5XJE732pxpafC5qIPgHQZ0jFSQpD0=w1800-h500-s-no-gm)
![FirstGearAndWheelLayout](https://lh3.googleusercontent.com/pw/ABLVV87hCQDSr5tZN8sYY9ZbG2KdHYztdBeUU50PnCghi7_sXsbcBNQvJptNNkUqizHHKUsF_ZgBu9geGEoXEN3gqDJIqX4MMi76ZhyCMfkcNbSAEwjGUrb_N59c5ZlpnWBOu9pmctnBCp_5SMbP8171ekd2=w1850-h600-s-no-gm)
{: .cad}

However, at this point, we noticed a problem with our current CAD.

{: .design}
# Define Problem

There are large gaps between the flex wheels and omni wheels. These gaps will make it much more difficult for us to drive over the barrier:

![FirstGearAndWheelLayoutProblem](https://lh3.googleusercontent.com/pw/ABLVV848yDNiyLW_rRcZBmQM3spsK-LPaQ_2HpWf4mPC0OgSwUa1HbxCSmJFDOpTT4FBX2VJ5_3E45pWsIbQvx-_D7KF-9_DKC_KldN5reSe5juV2eKvlfEm9DPQ1h3ko8Vx87oT7CcSBzwg1PYyZBI6MsZc=w1850-h725-s-no-gm)
{: .cad}

{: .problem}
> The problem is this:
> * Our current CAD design will likely become stuck on the barrier.

{: .design}
# Generate Concepts

Here are a few options we came up with to fix our problem:

1. Research to find a different gear ratio that would allow us to reduce the gaps in our drivetrain.
2. Move the gears (not attached to the c-channel) vertically down, below the axles of our wheels.
3. Move everything vertically down relative to the obstructive c-channel.


{: .design}
# Our Decision

We discussed each potential solution as a team to identify which one would work best for us.

Concept [#1](/docs/engineering/2023-08-30-SecondCompetitionChassis.html#:~:text=Research%20to%20find%20a%20different%20gear%20ratio%20which%20would%20allow%20us%20to%20reduce%20the%20gaps%20in%20our%20drivetrain.) would likely work; however, we feel like there should be a way to modify the ***layout*** of our current gear ratio to achieve the same effect.

Concept [#3]({site.url}/docs/engineering/2023-08-30-SecondCompetitionChassis.html#:~:text=Move%20everything%20vertically%20down%20relative%20to%20the%20obstructive%20c%2Dchannel.) would also likely work; however, this would force us to attach our motors horizontally instead of vertically. This is a problem because the motors would then be taking up space where we may build an intake for our robot in the future.

This leaves concept [#2](/docs/engineering/2023-08-30-SecondCompetitionChassis.html#:~:text=Move%20the%20gears%20(not%20attatched%20to%20the%20c%2Dchannel)%20vertically%20down%2C%20below%20the%20axles%20of%20our%20wheels.) as our last remaining option.

{: .decision}
>We will use idea [#2](/docs/engineering/2023-08-30-SecondCompetitionChassis.html#:~:text=Move%20the%20gears%20(not%20attatched%20to%20the%20c%2Dchannel)%20vertically%20down%2C%20below%20the%20axles%20of%20our%20wheels.): 
> * Move the gears (not attached to the c-channel) vertically down, below the axles of our wheels.

{: .design}
# Develop Solution

Below you can see a CAD screenshot of the gears after we moved them down. Specifically, we moved the inner gears between the large outer gears down exactly 0.5 inches. Additionally, you can see the supporting framework structure of the drivetrain in the second picture.

![SecondGearLayout](https://lh3.googleusercontent.com/pw/ABLVV86gnJhKKBEOS-RnWhhV8qUZJUjIqHft9eqAfRML3lDKQzvHkt_0XQMv82Oww0qABk1bsxASJU0RSk3lwrsEygA7GfKfPm3Wb0Cj7vi10ZZ6M95EjYOakJTboQexN5qlF8XE1StPoNCR_fHIofjqx-KI=w1922-h576-s-no-gm)
![SecondGearLayoutWithSupports](https://lh3.googleusercontent.com/pw/ABLVV858hP0sLZ1W6pfWc6Xr92kmOaha2DHaUFCbFPRh74OjbLaeKlnSvT35W10i8CE5gURt6Id-GxGvJz2WQOdWztZ64Znv1FdTv2w0Vl1DvBT8XFFQrQirUqX4bauBPPNDkEejQ8nc037Fgo4xwdgZbLC6=w1922-h769-s-no-gm)
{: .cad}

Once we had one half of the chassis in CAD, we simply mirrored the part, and joined the two halves together with the rest of our robot's structure:

![FirstDrivetrainTop](https://lh3.googleusercontent.com/pw/ABLVV86Na92QFy-gZpbshMx1147LoxfxbT5r0RVtNK1NobN-FyvVgVrkqaRSw0ZtootBq8juRrHGlzJQ4S0AAYTRF-GRZzd6EyWQWjECW4Wj40snbYff4QapfbmwAR_H-SvRu2JKucghfGFextWS75E7bN3E=w990-h931-s-no-gm){: width="45%"}
![FirstDrivetrainTop](https://lh3.googleusercontent.com/pw/ABLVV87lN3899YNxWvXD1zvnK7bQPj-9MRtCktInr5TnH1ns_kQsq3aXnQm8ROp915IIzMELIsldBQddefgSZSeXg84_Dzzu6iBeXU2kToEnuNOP_UJ1mYrn_nRAvLJB8wNfMPw_mAxV28yM7oKl0yjTpx4S=w1201-h770-s-no-gm){: width="54%"}
![FirstDrivetrainTop](https://lh3.googleusercontent.com/pw/ABLVV87ubRj2cl3iQ_MU_UgbbeZ9z5YfQhWsGiTy0NPOx88SmMO6-5O2Cs1XE9_RXcHzGLBoyhqgqlOEsadL-enXGhY0HTETk1Zo8D1gtoJn34J8B8sXK00-xM5si78edRt1QOoh0adRjbjx5r6skm_b5No8=w1886-h430-s-no-gm){: width="48%"}
![FirstDrivetrainTop](https://lh3.googleusercontent.com/pw/ABLVV84mvHN-twj9WVtUiWjeSNG9wAF7JPM9-_PXxnxuBvwvtACrw1XLIvZIzIK_HoBOpscnJsxrkmUwq0DwSfocLAeHMffUTZC_KKxYD1Yj6lg_jYVfTaFbxoxpDowrTBTXUnHKO6r0Hew-eTIIsGqfQqNw=w1832-h440-s-no-gm){: width="48%"}
 {: .cad}

{: .design}
# Construct

Now that we have a CAD of our robot, we should be able to construct each half of our drivetrain easily.

One thing that we emphasize a lot during our builds is ensuring we have as little friction as possible in our builds. Below you can see a video showing the amount of resistance in our drivetrain:

<div class="center">
<iframe class="center" width="560" height="315" src="https://www.youtube.com/embed/V5yFDuwT_t4?rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

After we had constructed each half of our drivetrain, we connected them:

![Second Competition Chassis Top View](https://lh3.googleusercontent.com/pw/ABLVV86iIt3wQRVR2HPLytsSN-j_7n_UMKCZmGd7VMIJDDHZlhj7dFqD42kt5oe23mF7c9Qc3-2-g5VjNUbkhBWUsMGT2SphRTY-E9oEDjOb-ITbTzgDaj8OPIcwsIS3KKZvK4MFOgIBWS5J9IhhMiCToseG=w1413-h1060-s-no-gm)

{: .design}
# Test

To test this chassis, we ran the same tests as we did for our [drivetrain prototypes](/docs/engineering/2023-06-08-ChassisPrototypeTests.html#:~:text=(This%20test%20includes%20all%207%20chassis%2C%20including%20the%20adjustable%20chassis)%3A); each test was run 10 times, and the results were recorded as a percentage. Below, you can see our results:

| Momentum Jump | Contact Jump | High-Centered Jump|
|:---:|:---:|:---:|
| 100% | 100% | 100% |

From this testing data, we can see that these [conclusions](/docs/engineering/2023-06-08-ChassisPrototypeTests.html#evaluate-solution) we had drawn from our test drivetrain prototype testing previously have proven accurate. The use of flex wheels in between the drivetrain's main wheels allows the chassis to drive over the barrier much easier.

{: .design}
# Evaluate Solution

According to our testing, this drivetrain should be a great starting point for our robot; by using more watts of power in our drivetrain (66W compared to 55W) and less speed, we should not have to worry about overheating.

