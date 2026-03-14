---
id: area-of-regular-polygons
title: Area of Regular Polygons
domain: mathematics
course: geometry
prerequisites:
  - id: regular-polygons
    type: hard
  - id: sine-cosine-tangent-ratios
    type: soft
builds-toward:
  - surface-area-of-prisms
tags: [area, regular-polygons, apothem]
stage: abstract-reasoning
status: validated
---

# Area of Regular Polygons

## Core Idea
The area of a regular polygon is A = (1/2) * apothem * perimeter, where the apothem is the distance from the center to the midpoint of a side (the perpendicular distance from center to side). This formula works because a regular n-gon can be divided into n congruent isosceles triangles, each with base = side length and height = apothem. For polygons inscribed in a circle, the apothem can be found using trigonometry.

## How It's Best Learned
Divide a regular hexagon into 6 equilateral triangles and compute the area directly. Generalize to n-gons by dividing into n triangles. Define the apothem and show how to compute it using right triangle trigonometry (central angle = 360/n, half the central angle gives a right triangle). Practice with various n values.

## Common Misconceptions
- Confusing apothem with radius (the apothem goes to the midpoint of a side, the radius goes to a vertex).
- Forgetting the 1/2 in the formula.
- Not knowing how to find the apothem when only the side length is given (requires trigonometry).
