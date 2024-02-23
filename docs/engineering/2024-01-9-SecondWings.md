---
title: Second Wings
parent: Engineering
notebook: engineering
date: 2023-01-09
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
- "Thomas Reid"
nav_order: 15
has_children: false
---

{: .design}
# Define Problem

From our first robot, we faced several issues with its wings. They would frequently push tri-balls while extending out and get stuck while retracting because they folded out from the side instead of dropping down like other robots we have observed. To prevent unwanted movement of tri-balls, the wings need to be positioned vertically. Additionally, the robot must be capable of pushing tri-balls into the goal and over the bars.


{: .problem}
We need wings that fold down vertically and that can push tri-balls out of the corners and over the central bar. 

{: .design}
# Generate Concepts

We have already generated concepts for this in our rebuild entry here is a summary of the section. As we explore different designs for adding wings to our robot, we have identified three options: door hinge, drop-down, and flap. Door hinge wings function like a door hinge on the side of the robot and fold out from a horizontal position, but they do move tri-balls in the process. drop-down wings drop from a vertical position without moving any tri-balls, making deployment easier and consuming less air from the pneumatics. Flap wings are fixed together and can be flung down in front of the robot, allowing it to push a small group of tri-balls.

While designing the wings for our new robot, we decided against using the same fold-out wings from our previous robot. These wings were problematic as they kept pushing tri-balls in unintended directions. We opted instead for drop-down wings that would allow for smoother tri-ball release and deployment with reduced air usage from the pneumatics.

{:.design}
# Construction



{:.design}
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

{:.design}
# Summary 