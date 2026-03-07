---
id: inverse-trigonometric-functions
title: Inverse Trigonometric Functions
domain: mathematics
course: precalculus
prerequisites:
  - id: inverse-functions-review
    type: hard
  - id: unit-circle
    type: hard
builds-toward:
  - solving-trigonometric-equations
  - implicit-differentiation
  - trigonometric-substitution
tags: [trigonometry, inverse-functions, arcsin, arccos, arctan]
stage: formal-systems
status: draft
---

# Inverse Trigonometric Functions

## Core Idea
Since trig functions are periodic (not one-to-one), we restrict their domains to create invertible versions: arcsin on [-pi/2, pi/2], arccos on [0, pi], arctan on (-pi/2, pi/2). These inverse trig functions answer the question "what angle has this trig value?" Understanding their restricted ranges is critical for getting correct answers in equations and for the derivative formulas in calculus.

## How It's Best Learned
Start with why restriction is necessary (horizontal line test fails on unrestricted trig). Graph each inverse function as a reflection of the restricted parent. Practice evaluating arcsin(1/2), arccos(-sqrt(2)/2), etc. by thinking about the unit circle within the restricted range.

## Common Misconceptions
- Confusing sin^(-1)(x) with 1/sin(x).
- Ignoring the restricted range and giving multiple answers when only one is correct.
- Evaluating arcsin(sin(5*pi/4)) as 5*pi/4 instead of adjusting to the range [-pi/2, pi/2].
