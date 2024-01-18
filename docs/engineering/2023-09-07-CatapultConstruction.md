---
title: Catapult Construction  
parent: Engineering
notebook: engineering
date: 2023-09-7
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
- "Thomas Reid"
nav_order: 7
has_children: false
---
{: .design}
# Define Problem

Now that we have a drivetrain, the next phase in designing our robot is to develop a way to score tri-balls during the [flood-the-zone](/docs/game_analysis/2023-05-17-CriticalGameMoments.html#:~:text=consider%20them%20significant.-,Flood%20the%20zone%3A,-%E2%80%9CFlooding%20the%20zone) game phase.

{: .problem}
We need to decide what kind of mechanism we will use to launch tri-balls.

{: .design}
# Generate concepts

Here are some ideas we came up with to launch the tri-balls:

1. **Flywheel**: By using a flywheel, we can launch tri-balls at incredibly high rates due to the ability to adjust the RPM of a flexible wheel. However, achieving consistency with a flywheel can be quite challenging.
2. **Catapult**: Using a catapult allows us to launch tri-balls with great accuracy, consistently placing them in the desired area. This strategy makes it easier for us to push the balls under the goal, resulting in a significant increase in our points per second. However, it's important to note that the use of rubber bands is required, and over time, the rubber bands may wear out, potentially leading to decreased accuracy.
3. **Puncher**: Using a puncher allows tri-balls to be placed onto a stationary platform (as opposed to a moving catapult), which can make it much easier to match load quickly.
4. **Cata-Puncher** So-called "Cata-Punchers" are a hybrid between a regular catapult and a puncher. If a tri-ball is placed into the catapult of a "cata-puncher", the tri-ball is launched just as a normal catapult would. However, what sets a cata-puncher apart from the rest is a platform near the hinge of the catapult, where, if a tri-ball is placed on this platform, the catapult will *smack*, or *punch* the ball. One disadvantage of a "cata-puncher" is the extra space required to build the platform.

{: .design}
# Our Decision

We had a small meeting to discuss which concept to use. We ultimately decided on a catapult due to its theorized accuracy and ability to score points quickly. Additionally, it should be a relatively simple mechanism to design and build.

{: .decision}
We will be designing and building a catapult.

{: .design}
# Develop Solution

Now that we know which concept we will be building, we need to decide exactly how to build it. One team we took inspiration from was 229V, you can see the research entry we did on them [here]({{site.url}}/docs/research/2023-09-07-229V-ACE.html).

To begin, we will CAD our design for the catapult gearbox. After CADing is complete, Caleb will construct and attach the catapult to our chassis.

Below you can see our first attempt at a CAD for our catapult:

![Cata33](/assets/engineering/SecondRobot/Cata33ISO2.png)
{: .cad}

There is an intermediary slip-gear which will have 3 sections of teeth cut out of it. These sections of teeth will allow the catapult to fire after storing up enough energy.

{: .design}
# Construction

Below you can see our gearbox frame as it is being assembled, and the gearbox attached to our robot:

![PartialGearbox](/assets/engineering/Cata/PartialGearbox.png)![Gearbox](/assets/engineering/Cata/Gearbox-Braces.png)
{: .image-pair}

During construction, we also added two 7.5" braces. These braces will help counteract any torque impulses that would otherwise bend our rear C-channel into oblivion.
To attach rubber bands to our catapult, we added four standoffs; two on our catapult basket and two on our chassis frame:

![TopBand](/assets/engineering/Cata/TopBandLabeled.png)![LowerBand](/assets/engineering/Cata/LowerBandLabeled.png)
{: .image-pair}

{: .design}
# Test

After attaching the gearbox to our robot, we made a simple basket for the catapult and tested the fire rate of our catapult. To test the fire rate, we simply took a video of the catapult and reviewed the footage afterward:

<div class="center">
<iframe class="center" width="560rem" height="315rem" src="https://www.youtube.com/embed/IMFXdegquXM?rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

This test is useful because we can compare our ***actual*** fire rate to our ***theoretical*** fire rate to determine the efficiency of our mechanism. Our fire rate ended up being around **98.4** launches per minute. When we compare this to the ideal fire rate of our catapult, **99.0** launches per minute, we can quantitatively see that it is very close to this. (about a 0.6% away from the ideal)

## Testing Issues

As we were testing our catapult, we noticed a ***big*** problem.

{: .problem}
> Our catapult will occasionally seize up; as the gear attached to our catapult re-engages the drive gear (a slip-gear), it occasionally fails in any of the following ways:
>
> * The gear will re-engage *too early*, causing the catapult to **crash** into our drivetrain.
> * The gear will re-engage poorly by **grinding** teeth together and/or skipping teeth.

We isolated the source of the problem to the *settling time of the catapult*. By settling time, we mean how long it takes for the catapult to stop moving/bouncing after being released. Without significantly modifying our catapult, the only thing we can do to avoid this problem is to slow down the fire rate of our catapult.

{:  .design}
# Evaluate

After testing our fire rate, we know that our catapult has potential, but until we can fix the seizing issue, we will have to run our catapult at a lower fire rate. Overall, things are looking good for our catapult; the potential of 98.4 tri-balls per minute is promising. 