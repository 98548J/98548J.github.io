---
title: Wing Construction
parent: Engineering
notebook: engineering
date: 2023-11-04
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
- "Thomas Reid"
nav_order: 11
has_children: false
---

 {: .design}
# Define problem 

During competitions, we observed that many robots had a mechanism to score balls without holding more than one. These robots were able to score points at a very high rate. We were impressed by this and wanted to incorporate a similar mechanism into our robot. This would allow us to potentially turn the tide of the match during competitions.

{: .problem}
We need something to be able to score a mass amount of tri-balls without possessing them.

{: .design}
# Generate Concepts

The mechanism these people are using is called wings, and there are two main types that we have seen people use. These two types are door hinge wings and drop wings. Door hinge wings work like a door with pneumatics pistons. They come out from each side of the robot, creating a wall that can push a large number of tri-balls into the goal. Drop wings are similar, they start standing straight up and pistons push them down to create a wall that can push a mass amount of tri-balls into the goal as well.

{: .design}
# Our Decision

After analyzing two different types, we have concluded that door hinge wings would be more advantageous for our robot. When the wings are flipped out, we can make them thinner to easily de-score the alliance tri-ball. This increases our chances of achieving win-point. Although we may consider drop wings in the future, we believe that door hinge wings are perfect for our current robot's requirements.

{: .decision}
We have chosen to build door-hinge wings for our robot.

{: .design}
# Develop Solution

Before we start constructing our wings, we need to think about the design. We plan to use pistons angled far enough to deploy them. High-strength axles will be used as the ends of our wings, and we will attach them using c-channel to create a hinge that will allow them to pivot freely. Although we want our wings to be flexible, we also want them to be strong enough to withstand the impact of another robot. To prevent them from bending or breaking, we plan to create a locking mechanism that will make a strong truss. This will make it difficult to bend the wings.

{: .design}
# Construction

When we were constructing the wings, we realized that they required some assistance in opening. Due to the piston's acute angle, it was difficult for it to push out. As a solution, we decided to use the new mini pistons to act as a boost for opening and closing. The mini pistons would push the wings out so that the other pistons could carry them. When it was time to retract the wings, the mini pistons would disengage the lock.

{: .design}
# Testing

To test this design, we will see how our wing performs in three different scenarios. Each test will be ran 3 times.

1. De-scoring alliance tri-ball.
1. Front goal push.
1. Central barrier push.

For the two push tests, we will line up ten tri-balls and see how many go in or over. For the alliance tri-ball test, we will line up the Alliance tri-ball ten times for each test.

## Results 

| | Ali Tri-ball | Goal push | Over central |
|:---|:---:|:---:|:---:|
| Test 1 | 100% | 100% | 20% |
| Test 2 | 90% | 70% | 0% |
| Test 3 | 90% | 90% | 10% |

{: .design}
# Evaluate

These wings did a great job at pushing tri-balls into the goal and removing an alliance tri-ball from the match load zone. ***However***, these wings are absolutely terrible at pushing tri-balls over the central barrier. For now, these wings will work, but in the future we will need to re-design these wings.