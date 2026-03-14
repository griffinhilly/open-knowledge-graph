---
id: arc-length
title: Arc Length
domain: mathematics
course: calculus-2
prerequisites:
- id: fundamental-theorem-of-calculus-part-2
  type: hard
- id: u-substitution
  type: hard
- id: trigonometric-substitution
  type: soft
- id: central-angles-and-arcs
  type: soft
- id: circumference
  type: soft
builds-toward:
- arc-length-parametric
- surface-area-of-revolution
tags:
- integration
- applications
- arc-length
stage: formal-systems
status: validated
---
# Arc Length

## Core Idea
The length of a curve y = f(x) from x = a to x = b is L = integral from a to b of sqrt(1 + (f'(x))^2) dx. This formula comes from summing infinitesimal hypotenuses (sqrt(dx^2 + dy^2)) along the curve. Arc length integrals are often difficult or impossible to evaluate in closed form, making them good candidates for numerical methods.

## How It's Best Learned
Derive the formula from the Pythagorean theorem applied to infinitesimal segments. Compute arc length for functions where the integral simplifies nicely (e.g., y = x^(3/2), y = (x^2)/2 - ln(x)/4). Emphasize that most arc length integrals do not have neat answers.

## Common Misconceptions
- Forgetting the square root or the 1 inside it.
- Confusing arc length with the integral of |f(x)| (which gives area, not length).
- Expecting all arc length integrals to have closed-form solutions.
