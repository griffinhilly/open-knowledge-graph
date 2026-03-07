---
id: polar-coordinates
title: Polar Coordinates
domain: mathematics
course: precalculus
prerequisites:
  - id: trigonometric-ratios-review
    type: hard
  - id: unit-circle
    type: soft
builds-toward:
  - polar-graphs
  - polar-area
  - polar-arc-length
tags: [polar, coordinates, coordinate-systems]
stage: formal-systems
status: draft
---

# Polar Coordinates

## Core Idea
Polar coordinates represent a point by its distance from the origin (r) and the angle from the positive x-axis (theta), rather than by horizontal and vertical distances (x, y). The conversion formulas are x = r*cos(theta), y = r*sin(theta), r^2 = x^2 + y^2, tan(theta) = y/x. Polar coordinates are the natural choice for problems with circular or rotational symmetry.

## How It's Best Learned
Plot points in polar coordinates, including negative r values. Practice converting points and equations between rectangular and polar forms. Convert familiar curves (circles, lines) to polar form to build intuition.

## Common Misconceptions
- Forgetting that polar representations are not unique: (r, theta) and (r, theta + 2*pi) are the same point, and (-r, theta + pi) also represents the same point.
- Making errors when converting equations, especially with r^2 = x^2 + y^2 vs. r = sqrt(x^2 + y^2).
- Assuming theta must be between 0 and 2*pi.
