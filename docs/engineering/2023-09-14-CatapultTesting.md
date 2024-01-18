---
title: Catapult Testing 
parent: Engineering
notebook: engineering
date: 2023-09-14
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
- "Thomas Reid"
nav_order: 8
has_children: false
---

{: .design}
# Introduction 

We have successfully built our first catapult and are now ready to begin testing it. 

In our [previous entry]({{site.url}}/docs/engineering/2023-09-07-CatapultConstruction.html#test), we tested our catapult's fire rate. We also wanted to test different basket configurations. The shape of our basket greatly affects where our tri-balls will land.

We plan to conduct multiple tests, including Rubber **Band Intensity** and **Standoff Length**, To determine the necessary amount of rubber bands and length of standoffs, we need to conduct tests. These tests will provide valuable information on whether we need to reconstruct the head of the catapult.

{: .design}
# Generate Concepts 

**Band Intensity:** We plan to conduct a series of tests to determine the optimal number of rubber bands required to launch the tri-ball to the desired distance, ensuring it lands in the offensive zone consistently. Initially, we will place an equal number of rubber bands on both sides of the catapult and then add one extra on the other side to achieve the precise tension needed for the catapult.

**Standoff Lengths:** To ensure optimal launch accuracy, we will first measure band intensity and then proceed to test the length of stand-offs. This is crucial in preventing the tri-balls from launching too early or hitting the ground. We will conduct tests with and without the middle stand-offs to determine if additional support is necessary, resulting in the best possible launch outcome.

{: .design}
# Testing

![TestSetup](/assets/engineering/Cata/Catapult%20Testing.png)

Initially, we began with the rubber band test and we did 14 tests each time we switched the rubber bands we latched the catapult ten times after launching them ten times we gave them a percentage from zero to one hundred and gave a color based on it. As is demonstrated in the graph below.

Each graph records the number of tests, the number of rubber bands on each side of the catapult, and the percentage of tri-balls that made it across.

| Right Side Rubber-Band | Left Side Rubber-Band | Score |
|:--:|:---:|:---:|
| 2 | 2 | 90% |
| 2 | 2 | 80% | 
| 3 | 3 | 100% |
| 3 | 3 | 80% |
| 2 | 3 | 100% |
| 3 | 2 | 100% |
| 3 | 2 | 100% |
| 3 | 4 | 100% |
| 3 | 4 | 100% |
| 3 | 3 | 100% |
| 4 | 3 | 90% |
| 4 | 3 | 100% |
| 4 | 4 | 100% |
| 4 | 4 | 100% |
{: .calendar}

After conducting the rubber band intensity test we moved on to stand-off lengths we did 4 different sizes of stand-offs with and without the central stand-off supporting in the launch. We did two versions of this test one with a four-band tensioned catapult and one with a six-band tensioned catapult as seen in the tables below. 

## 6 Rubber band

| Stand- Off length | With Middle Stand-Off | Without Middle Stand-Off |
|:--:|:---:|:---:|
| 1.5" | 90% | 60% |
| 2" | 90% | 70% | 
| 2.5" | 70% | 80% |
| 3" | 70% | 50% |
{: .calendar}

## 4 Rubber Band

| Stand- Off length | With Middle Stand-Off | Without Middle Stand-Off |
|:--:|:---:|:---:|
| 1.5" | 100% | 60% |
| 2" | 80% | 100% |
| 2.5" | 60% | 100% |
| 3" | 70% | 70% |
{: .calendar}

{: .design}
# Summary

After conducting tests, we have determined the optimal tension and length for the stand-offs which is two-inch stand-offs with 4 rubber bands. The result of this optimized test was a catapult that can reliably launch tri-balls across the bar.