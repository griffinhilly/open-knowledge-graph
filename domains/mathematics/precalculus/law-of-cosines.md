---
id: law-of-cosines
title: Law of Cosines
domain: mathematics
course: precalculus
prerequisites:
  - id: trigonometric-ratios-review
    type: hard
builds-toward:
  - dot-product
tags: [trigonometry, triangles, law-of-cosines]
stage: formal-systems
status: validated
---

# Law of Cosines

## Core Idea
The Law of Cosines states that c^2 = a^2 + b^2 - 2ab*cos(C), generalizing the Pythagorean theorem to non-right triangles (when C = 90, the formula reduces to c^2 = a^2 + b^2). It is used when you know two sides and the included angle (SAS) or all three sides (SSS). Combined with the Law of Sines, it allows you to solve any triangle.

## How It's Best Learned
Derive using coordinate geometry or the distance formula. Practice SAS cases (find the third side) and SSS cases (find an angle). Compare with the Pythagorean theorem to build intuition about the correction term -2ab*cos(C).

## Common Misconceptions
- Forgetting the negative sign in -2ab*cos(C), especially when the angle is obtuse (which makes cos(C) negative, so the term adds).
- Using the wrong angle in the formula (C must be the angle between sides a and b).
- Not recognizing when to use Law of Cosines vs. Law of Sines.
