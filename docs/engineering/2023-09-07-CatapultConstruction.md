---
title: Catapult Construction  
parent: Engineering
notebook: engineering
date: 2023-09-7
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
nav_order: 7
has_children: false
---

{: .design}
# Define Problem

Now that we have a drivetrain, the next phase in designing our robot is to develop a way to score tri-balls during the [flood-the-zone]({{site.url}}/docs/game_analysis/2023-05-17-CriticalGameMoments.html#:~:text=consider%20them%20significant.-,Flood%20the%20zone%3A,-%E2%80%9CFlooding%20the%20zone) game phase.

{: .problem}
We need to decide what kind of mechanism we will use to launch tri-balls.

{: .design}
# Generate concepts 
Here are some ideas we came up with to launch the tri-balls:

1. **Flywheel**: By using a flywheel, we can launch tri-balls at incredibly high rates due to the ability to adjust the RPM of a flexible wheel. However, achieving consistency with a flywheel can be quite challenging.

2. **Catapult**: Using a catapult allows us to launch tri-balls with great accuracy, consistently placing them in the desired area. This strategy makes it easier for us to push the balls under the goal, resulting in a significant increase in our points per-second. However, it's important to note that the use of rubber bands is required, and over time, the rubber bands may wear out, potentially leading to decreased accuracy.

3. **Puncher**: Using a puncher allows tri-balls to be placed onto a stationary platform (as opposed to a moving catapult), which can make it much easier to match load quickly.

4. **Cata-Puncher** So-called "Cata-Punchers" are a hybrid between a regular catapult and a puncher. If a tri-ball is placed into the catapult of a "cata-puncher", the tri-ball is launched just as a normal catapult would. However, what sets a cata-puncher apart from the rest is a platform near the hinge of the catapult, where, if a tri-ball is placed on this platform, the catapult will *smack*, or *punch* the ball. One disadvantage of a "cata-puncher" is the extra space required to build the platform.

{: .design}
# Develop Solution

We had a small meeting to discuss which concept to use. We ultimately decided on a catapult due to its theorized accuracy and ability to score points quickly. Additionally, it should be a relatively simple mechanism to design and build.

{: .decision}
We will be designing and building a catapult.

{: .design}
# Develop Solution

To begin, we will CAD our design for our catapult, including the gear box and the head. After CAD, Caleb will be constructing and attaching the catapult to our chassis. 

{: .design}
# Construction 