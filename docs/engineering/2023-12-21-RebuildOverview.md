---
title: Rebuild Overview
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

