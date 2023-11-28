---
title: Catapult Rebuild 
parent: Engineering
notebook: engineering
date: 2023-09-22
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
nav_order: 9
has_children: false
---

{: .design}
# Define problem 

After constructing and testing our first catapult, we realized that it needed to be significantly faster to be effective in matches and skills. Therefore, we will be rebuilding the catapult to launch 99 tri-balls per minute. This will allow us to quickly launch all 44 match loads during skills, enabling us to perform other game actions without delay.

{: .problem}
We need a better catapult that can fire at a faster rate without jamming up.

{: .design}
# Generate Concepts

We have limited options as our first competition is in two weeks and we need to not only program but let our driver. Here are our current ideas for the short amount of time we have.

* leaving the catapult as it is. This will allow us to focus on other mechanisms and programming, as well as give our driver more practice time. However, it is important to keep in mind that this may leave us with less time to rebuild the catapult before our next competition after our first. Additionally, using an inefficient catapult may affect our driver's performance as he got used to the old one.

* Rebuilding our robot may result in less time for our driver to operate it and less time for other mechanisms. However, this decision will only reduce the time for elevation. We will still have ample time to work on the intake mechanism, which is a crucial part of the robot. Additionally, our driver will have the opportunity to get accustomed to a more efficient catapult.

{: .design}
# Our Decision

We recently held a meeting to discuss whether or not we should rebuild our catapult. After much deliberation, we ultimately decided to move forward with the rebuild. Our primary goal is to improve our skills score and give our driver a chance to become accustomed to a more efficient catapult. Additionally, this decision will allow us more time to focus on other areas between our next competition.

{: .decision}
Rebuilding the catapult is the most beneficial in the long run.

### Objective --

For our rebuild, we require a catapult that can be loaded in two ways: one for match loads and another with an intake. We plan to create a spot in front of the catapult for autonomous or early matches where we can load the tri-balls. This way, they will be hit by the catapult, almost like a punch, instead of sitting inside it. Then once the match begins, we will use our intake to carry the tri-ball into the catapult itself, to launch it instead of punching it.

{: .design}
# Develop Solution 

### Addressing the jamming problem --

We have worked around this problem in the past by *slowing down* our motor speed. Thinking critically now, In terms of the actual mechanism, by **slowing it down**, we are giving the catapult **more time** to launch. So, if we want to keep the same catapult head, any modifications we make simply need to give our catapult more time to launch... yet simultaneously allow us to use our maximum fire rate of 99 tri-balls per minute.

One of our sister teams has a catapult with the same maximum fire rate as us, but they do not have a jamming problem. We compared our designs to see the difference. The biggest difference we noticed was the size of slip gear we each used:

![Slip Gear Comparison](/assets/engineering/Cata/gear%20example2.png)

***Both of these gear configurations are identical*** on paper:

* 12-tooth, single-stage, slip-gear spinning at 200 rpm driving a 36 tooth gear... **99 tri-balls per minute**
* 36-tooth, triple-stage, slip-gear spinning at 66.6 rpm driving a 36 tooth gear... **99 tri-balls per minute**

And yet, when you look at the geometry of the gears, it is easy to see that they do behave slightly different; because of the slightly bigger window with the 12-tooth gear -- literally a bit of extra **"wiggle room"** -- our catapult would have **more time** to launch.

For our construction, we will be using the 12-tooth gear in our gearbox as a slip-gear instead.

### Addressing the layout issue --

We need more space above, and behind our catapult to put a platform to match load from. 

One way we can get more space for match loading above is by moving our catapult downwards. We will start building these modifications before we make any other changes.

{: .design}
# Construction

Below you can see pictures showing the platform we made.

![PLATFORM](/assets/engineering/Cata/Platform.jpg)![BallOnPlatform](/assets/engineering/Cata/BallOnPlatform.jpg)
{: .image-pair}

We used two linear rails attached to the back of our catapult to support a backstop for the catapult. Additionally we added two passive standoffs which will not stop the catapult from launching, but will serve as a support for the tri-balls when match loading.

{: .design}
# Testing

To test if this modification worked, we shot tri-balls over the mid bar from the match load bar. The match loading platform worked very well. All of the tri-balls we attempted to launch went over.

{: .design}
# Evaluate

We are confident in our modification. With the ability to match load, and the ability to run our catapult at full speed we will be much more competitive.