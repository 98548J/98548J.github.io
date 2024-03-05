---
title: Hang Elevation
parent: Engineering
notebook: engineering
date: 2024-01-15
signatures:
- "Ayla Clark"
- "Caleb Carlson"
- "Tucker Nielson"
- "Thomas Reid"
nav_order: 16
has_children: false
---

{: .design}
# Define Problem

When considering elevation in our strategy, we aimed for at least an A tier because it can quickly turn the game in our favor. We have witnessed numerous matches where teams have won by simply parking their robot. Additionally, having a reliable parking mechanism allows us to team up with a robot that has an opposite parking mechanism, enabling us to execute a double park on the elevation bar similar to the Tipping Point game from the previous year.

{: .problem}
We need an elevation mechanism to help us elevate in the end game of a match. 

{: .design}
# Generate Concepts

When building an elevation, there are three primary options to choose from. These options are clamping, hanging, and climbing. Clamping involves using a robot to grip the colored elevation bar and lift itself up to achieve a high tire elevation. However, this method requires a lot of space and can be quite heavy. Hanging is where a robot uses motorized or passive hooks to hang onto the colored horizontal bar elevation. While this can take up less space, if your robot doesn't have an elevated catapult, hanging can take up just as much space as a clamping mechanism. Climbing is where a robot drives up the elevation bar using a motor or PTO and two wheels to elevate. While this method can be very successful, it can be challenging to line up and can fall easily.

{: .decision} 
After some deliberation we decided to use a passive hook hang because we already have an elevated catapult and it would be just a small addition.  

{:.design}
# Construction

During construction, it was quite simple all we did was measure the diameter of the horizontal colored bar to find the perfect size to shave the Polly Carbonate. We used multiple layers so it could hold up to contacting the bar hard repeatedly over and over again. 

{:.design}
# Testing

We will conduct three sets of ten tests during the testing phase. After each set of ten tests, we will convert the results into a percentage to assess the overall performance of our robot. This will help us identify any major flaws in our design, which we can either adjust or eliminate based on the test results.

## Results 

| Hanging |
|:---|:---:|:---:|:---:|
| Test 1 | 90% |
| Test 2 | 60% | 
| Test 3 | 70% |

{:.design}
# Summary 

After testing, we observed that the robot's back end frequently got caught on the tile, causing our wheels to lose traction. This issue impeded our ability to swing properly, leading to several failures. To address this problem, we plan to add a piece of Lexan to the robot to prevent it from getting caught in the future. However, our first rendition of a hanging elevation was successful, and we plan to continue using it.