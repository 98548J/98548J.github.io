---
title: Rebuild Overview & Brainstorm
parent: Engineering
notebook: engineering
date: 2023-12-21
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
- "Thomas Reid"
nav_order: 11
has_children: false
---

{: .design}
# Define Problem

As mentioned in our [most recent team meeting]({{site.url}}/docs/TeamHistory/2023-12-21-RobotRebuild.html),  we would like to rebuild our robot. Below is an overview of what **issues** we have seen in our current design iteration, and *why we think that a complete redesign is necessary*.

## Issues -

* Our catapult shoots from a low position -- making it easy for our opponents to block our match loads.
* We cannot block teams who are match-loading.
* We have not found a reliable method of elevation, something ***absolutely critical*** in this year’s game since elevation can account for up to ***20 points*** of the match.

## Why does this mean we need to rebuild?

Even though we could mitigate the first issue by creating a catapult that can launch at a high arc -- oh wait, we [already did]({{site.url}}/docs/engineering/2023-09-22-CatapultRebuild.html)! -- teams with blockers will still be able to block us very easily. The only way to truly solve this first problem is to rebuild our tri-ball launching mechanism in such a way that it is hard for teams with blockers to block us.

As far as the second issue goes, we probably could design a deployable blocker for this robot. So this issue alone doesn't exactly force us to rebuild. Although, it would be easier to create a design for a robot that accounts for a blocker by design. (Our robot wasn't designed to have a deployable blocker on top of it.)

The third issue is much the same as the second; This issue could probably be solved without a rebuild, but it would be easier to solve it during a rebuild.

{: .problem}
>
> There are things our robot is bad at, or areas where our robot can improve, but the current layout / design of our robot makes it difficult to address these issues 

{: .design}
# Generate Concepts

# *Objective* -

Our current robot has been performing fairly well. It would be a shame if we rebuilt our robot only to find that we have not improved our situation. Because of this, this rebuild will be focused on creating a new robot that ***has the same capabilities as our old robot** as well as additional functionalities or improvements.

Here is an overview of our current robot: (with links to the appropriate notebook entries)

* [300rpm drivetrain](http://localhost:4000/docs/engineering/2023-08-30-SecondCompetitionChassis.html)
* [Two horizontally folding wings]()

## **Drivetrain**

 When rebuilding our robot, we want to make the most efficient use of our time. After careful consideration, we realized that we had already done extensive testing on our drivetrain and found it to be the best possible design for our robot. Therefore, we have decided to keep the drivetrain intact during the rebuild process. This will save us time, as our driver is already familiar with the drivetrain and will benefit from their existing skills.

## **Catapult**

We can make a catapult in one of three ways: the regular catapult, slapper, or kicker. The original catapult design works like a real one, where the tri-balls sit in a box or pocket and the catapult builds tension till it launches, flinging them across the field. The slapper hits the tri-balls from the side, which only contacts for a second and has a more predictable grouping. A kicker is similar to a slapper, but it hits from the underside and causes the tri-balls to follow a higher arc and make predictable grouping patterns. There are fixed and elevated catapults, but fixed catapults often face blocks that interfere with match loading, which is why elevated blockers are becoming more common.

{: .decision}
To overcome the robots that were obstructing our match loading, we decided to use an elevated catapult. This would allow us to get tri-balls over, regardless of robots trying to block us. Our catapult is different from others because it acts more like a kicker, hitting the tri-balls from underneath and creating a higher arc. This higher arc will result in better accuracy and fewer tri-balls rolling out of the field.

## **In-take*

When it comes to designing an intake mechanism, there are a few different options to choose from, including a single stage, double stage, and claw. A single-stage intake mechanism has one roller with rubber bands that helps to intake tri-balls. A double stage is similar but has an additional roller, making it bulkier and heavier, which can make it more challenging to use. On the other hand, a claw mechanism only clamps onto a single tri-ball to move it. While it is slower than the other two options, it cannot put tri-balls into a robot.

Considering these factors, we decided to create a new intake mechanism that would be more efficient and user-friendly. While our previous double-stage intake mechanism performed well, it was bulky and challenging to use. Therefore, we chose to design a new single-stage intake mechanism that would be less bulky and easier to operate. This new mechanism would allow us to intake objects quicker and more effectively into our elevated catapult than the previous one.

## **Wings** 

As we explore different designs for adding wings to our robot, we have identified three options: door hinge, drop-down, and flap. Door hinge wings function like a door hinge on the side of the robot and fold out from a horizontal position, but they do move tri-balls in the process. drop-down wings drop from a vertical position without moving any tri-balls, making deployment easier and consuming less air from the pneumatics. Flap wings are fixed together and can be flung down in front of the robot, allowing it to push a small group of tri-balls.

While designing the wings for our new robot, we decided against using the same fold-out wings from our previous robot. These wings were problematic as they kept pushing tri-balls in unintended directions. We opted instead for drop-down wings that would allow for smoother tri-ball release and deployment with reduced air usage from the pneumatics.

{:.design}
# Summary 

We have completed the process of generating concepts for our new robot and we are now ready to begin its creation. We are confident that the compilation we have chosen is the best fit for our specific robot. With this new robot, we are optimistic that we will not only excel in competitions but also in our upcoming signature event. also in our upcoming signature event.