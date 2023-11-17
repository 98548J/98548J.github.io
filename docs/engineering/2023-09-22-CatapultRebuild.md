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

{: .design}
# Develop Solution  

For our rebuild, we require a catapult that can be loaded in two ways: one for match loads and another with an intake. We plan to create a spot in front of the catapult for autonomous or early matches where we can load the tri-balls. This way, they will be hit by the catapult, almost like a punch, instead of sitting inside it. Then once the match is set in, we will use our intake to carry the tri-ball into the catapult itself, to launch it instead of punching it.

{: .design}
# Construction



