---
title: Odometry Test Rig
parent: Engineering
notebook: engineering
date: 2023-06-05
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
- "Thomas Reid"
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

> ![placeholder CAD PICTURES](https://lh3.googleusercontent.com/pw/ABLVV87sQ1qCmYonFf_DNRXvcBo6nhtL00-W9Hz7QWCwxAXHflCbNpXxL8MyKgyyQ8DDSaM0llKjOIuZcuXbB3qcP51YvX217ix2htAQzpGfHHnPyK2b3hYANRWqSAgK8wajVAIxnEzJe8FN6pJZ3F5gJfqE=w1238-h1060-s-no-gm)![placeholder CAD PICTURES](https://lh3.googleusercontent.com/pw/ABLVV86F-N67J4c-SN62mn3t5IIQJCdyiEkOTYaAXj5qYLVCmmDL1QTKtukY4zwNByhm-bub8H174zIb8tdPBvXexdr0-SmseqqzlH-yCYaRBU5gHePrr6SMIOKQhSgbBUuKCs7CqN7VgL0_IWuRW0lSmOV6=w1406-h1060-s-no-gm)
> {: .image-pair}
> ![placeholder CAD PICTURES](https://lh3.googleusercontent.com/pw/ABLVV87b2oQokPFgFxFo7ZnwMx-ydKzGGxFAZJD4BOKjzn2CuJWh6AJWWudOyrY5fGGnf1mOIUrFQ5Dld2IOjqLeJdhfYGqthYF_8MlJB7rKhWTL6PvxBULXaWCsuuXY19OOsgvAfmEjXNT2_CP0eKNnZ9VU=w1922-h973-s-no-gm)![placeholder CAD PICTURES](https://lh3.googleusercontent.com/pw/ABLVV86Rf8upa9B7pu5_DweEtaPaMP0AuJfThITTWBUxJW4dhqYJUYjCXYhqiTPEIILPGVLBuCaN-Zmwsr5KYnb8bba_TxuMdNscqTRDMTzHCWRHefXWSaSTA6kL9DFgyDg4Us7Leny4a4yPpVaKx-PZ2anR=w1922-h973-s-no-gm)
> {: .image-pair}
{: .cad}

One thing to note is that we only inserted one tracking wheel into the CAD, this was to make sure we knew exactly what spacing to use to get the tracking wheel to make contact with the center of the robot. 

{: .design}
# Construct & Test

First, we put together the frame of the chassis. Then, we constructed the tracking wheels and attached all the motors and tracking wheels.

![placeholder ConstructionPictures](https://lh3.googleusercontent.com/pw/ABLVV86m1sEVYsd1vhCfcMJ3RW-BglcWRITxDJiN4KbIW0GfJg43ZpIVxs9Q9gu3NmSgMVGZW5qx_ZO5M1v--wZ0ih78kYYj9cbYy5pMwi21blmW85z0dpHFOW-aKW5bRMZ28RWcl30wDBq5TMcm9r0WWCqg=w795-h1060-s-no-gm)![placeholder ConstructionPictures](https://lh3.googleusercontent.com/pw/ABLVV8410Jy-AnhHCvgCNekpNdmjYFGOxFK69NrI490DH-LjDidrlwHFBoa-O7TlQ917XzB0uQvj_W7N8M_eX9zLDy7rlLuyv5oSgatT8pdzCzoC0SgTPsfPT5czPV1bQecK4-mCk9oxfADO8Sod3lmPzL8K=w795-h1060-s-no-gm)
{: .image-pair}
![placeholder ConstructionPictures](https://lh3.googleusercontent.com/pw/ABLVV86gc_yqmQwomT70bFtfNCTTBZhkfxbZTQlMuyx0YpgapdC3gS0l5YA6TBhhGyR4DYHYZSQvPO9OQhUCr74mxoPCwrrq9yPblpv2WQ0fFqYIQkki6qhrrNUXfp7G2dAGA9EIQc1FON2RpP5-BwZNP7w4=w795-h1060-s-no-gm){: width="48%"}

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

![placeholder ConstructionPictures](https://lh3.googleusercontent.com/pw/ABLVV84hWXQRs52oM9d_X637DMi83lNA-mUuMoaQzUyuGbwegqtueFyp-0NFINj_N2rm3ooAhCwpSPh-FfmHn3MYdgh7wrjjiqBhVBnnstYW7gpVoU_-IK7jjziomxxRHc1FSF_O5NMAdcLnisqexC8vQH3K=w1413-h1060-s-no-gm)![placeholder ConstructionPictures](https://lh3.googleusercontent.com/pw/ABLVV86_kWAQbLpbuazfpo_ADYLT4d8BMLEKvy3w9wTYSxkQRoHHwOVEFyhmXrT62aXaBUxw7I1oGloi-eiL5lngPunowilo6HQcUxsUnth2cC1pjBFvSxFRQ_lBX6f8KWZINUAghxUwT4-pQroWlBi7yokn=w1413-h1060-s-no-gm)
{: .image-pair}

The first step in testing our rig was to turn on the brain and verify that all of the motors and sensors are working -- they were. Next, we programmed the robot with a basic tank drive driver control program to see how well it drove.

The test rig was able to drive without any issues.

{: .design}
# Evaluate Solution

Now that we have a test rig, we will be able to begin researching and developing odometry for our robot.