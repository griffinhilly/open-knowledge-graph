---
id: arc-length-circles
title: Arc Length of Circles
domain: mathematics
course: geometry
prerequisites:
  - id: central-angles-and-arcs
    type: hard
  - id: proportions
    type: hard
builds-toward:
  - sector-area
  - radian-measure
tags: [circles, arc-length, circumference, proportionality]
stage: abstract-reasoning
status: validated
---

# Arc Length

## Core Idea
Arc length is the linear distance along a portion of a circle's circumference. Since the circumference of a circle is 2*pi*r, an arc of measure theta degrees has length (theta/360) * 2*pi*r. Arc length is proportional to the central angle. This formula bridges angular measurement and linear measurement, laying groundwork for radian measure in later courses.

## How It's Best Learned
Derive the formula from proportional reasoning: the arc is the same fraction of the circumference as the central angle is of 360 degrees. Practice computing arc lengths for various angles and radii. Give problems where students must find the angle given the arc length, or the radius given both.

## Common Misconceptions
- Confusing arc length (a linear measurement in units like cm) with arc measure (in degrees).
- Forgetting to use the radius in the formula (using diameter instead, or omitting it).
- Not including pi in exact answers.

## Explainer

The circumference of a circle is the total distance around it: C = 2πr. An **arc** is simply a piece of that circumference — a curved segment cut off by a central angle. Arc length answers the question: if you walked along the curve instead of through the center, how far would you travel?

The key insight comes from **proportional reasoning**, which you already know. A central angle of 360° sweeps the entire circle, giving the full circumference. A central angle of 180° sweeps exactly half the circle, giving half the circumference. By the same logic, a central angle of θ degrees sweeps a fraction θ/360 of the circle. Arc length is just that fraction of the full circumference: **arc length = (θ/360) × 2πr**. The formula is not something to memorize blindly — it is proportional reasoning applied to a circle. If you understand that, you can reconstruct it from scratch.

Notice what the two variables control independently. The **angle** (θ) determines what fraction of the circle you're traveling along. The **radius** (r) scales the size of the circle itself. A 90° arc on a small circle (r = 1) has length π/2 ≈ 1.57 units. The same 90° arc on a circle ten times larger (r = 10) has length 5π ≈ 15.7 units — ten times as long. The angle alone doesn't determine length; you need the radius too.

The most important conceptual distinction is **arc measure versus arc length**. Arc measure is the degree of the central angle — a pure number between 0° and 360°, with no units of distance. Arc length is a linear distance — measured in centimeters, inches, or whatever unit the radius uses. Two arcs can have the same degree measure (say, 60°) but different lengths if their circles have different radii. Keeping these two quantities separate prevents the most common errors in circle problems.

This topic is a stepping stone to **radian measure**, which you'll encounter in later courses. Radians redefine angle measurement so that the arc length formula becomes arc length = rθ (with no 360 conversion factor), because one radian is defined as the angle for which arc length equals the radius. When you see that definition, the connection back to this formula will be immediate: radians are just the natural unit that makes the proportion come out cleanly.
