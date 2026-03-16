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

## Explainer

You already know that a regular polygon has all sides equal and all angles equal. The key to finding its area is a beautifully simple dissection: slice the polygon into congruent triangles by drawing a line from the center to each vertex. A regular hexagon splits into 6 triangles, a square into 4, an octagon into 8. Each triangle has its tip at the center and its base as one side of the polygon. Because the polygon is regular, all these triangles are identical, so the total area is just (number of sides) × (area of one triangle).

Every triangle has base = side length s and height = **apothem** a, the perpendicular distance from the center to the midpoint of a side. Note carefully: the apothem goes to the *midpoint* of a side, not to a vertex — that distance would be the circumscribed radius r. The area of each triangle is (1/2) × s × a. Multiply by n triangles and collect terms: total area = n × (1/2) × s × a = (1/2) × (n × s) × a. But n × s is just the perimeter P, so the formula simplifies to **A = (1/2) × a × P**. The perimeter wraps around the outside; the apothem measures how "deep" the polygon is from outside to center.

When you know the side length but not the apothem, trigonometry fills the gap. The center-to-vertex line and the apothem together form a right triangle inside one of the n slices. The central angle of each slice is 360°/n, so the half-angle at the center is 180°/n. The apothem is the adjacent side of this right triangle, and half the side length (s/2) is the opposite side. That means tan(180°/n) = (s/2)/a, so a = (s/2)/tan(180°/n). For a regular hexagon with side 1, the central half-angle is 30°, tan(30°) = 1/√3, so a = (1/2)/(1/√3) = √3/2 — which you can verify directly since a regular hexagon is made of equilateral triangles.

This formula connects to the limiting case that is a circle: as n grows large, a regular n-gon approaches a circle. The apothem approaches the radius r, and the perimeter approaches the circumference 2πr. Substituting into the polygon formula gives (1/2)(r)(2πr) = πr² — the exact formula for circle area. The polygon formula is not just a useful calculation tool; it is the geometric reason the circle area formula is what it is.
