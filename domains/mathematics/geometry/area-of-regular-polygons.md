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
  - id: area-of-triangles
    type: hard
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

## Questions

```yaml
- question: "A regular hexagon has side length 6 cm. The circumscribed radius (center to vertex) is also 6 cm. What is the apothem?"
  type: multiple-choice
  options:
    - "6 cm — the apothem equals the radius in a regular hexagon"
    - "12 cm — the apothem is the full diameter"
    - "Approximately 5.2 cm — the perpendicular distance from center to the midpoint of a side"
    - "3 cm — the apothem is half the side length"
  answer: 2
  explanation: "The apothem is the perpendicular distance from the center to the midpoint of a side — it is NOT the radius (center to vertex). For a regular hexagon with side length 6, the apothem = 6 × (√3/2) ≈ 5.196 cm, which is shorter than the radius of 6 cm. The apothem is always shorter than the radius because the perpendicular to the side is shorter than the line to the corner. Confusing them gives an incorrect area calculation."

- question: "A student calculates the area of a regular octagon using A = (1/2) × r × P, where r is the radius (center to vertex) instead of the apothem. How does her answer compare to the correct area?"
  type: multiple-choice
  options:
    - "Her answer is too small, because the radius is shorter than the apothem"
    - "Her answer is too large, because the radius is longer than the apothem"
    - "Her answer is correct — radius and apothem are equal for regular polygons"
    - "It depends on the number of sides — for some polygons they are equal"
  answer: 1
  explanation: "The radius (center to vertex) is always longer than the apothem (center to midpoint of side) for any regular polygon. Using the larger radius instead of the apothem inflates the height of each constituent triangle, producing an area that is too large. The apothem is specifically the perpendicular height of those triangles — using any other measurement (like the slant radius) overestimates that height."

- question: "The formula A = (1/2) × apothem × perimeter is a special rule unique to regular polygons, derived from principles unrelated to triangle area."
  type: true-false
  answer: false
  explanation: "The formula is derived directly from triangle area. Divide a regular n-gon into n congruent triangles by connecting the center to each vertex. Each triangle has base = side length s and height = apothem a. Area of one triangle = (1/2) × s × a. Multiply by n triangles: n × (1/2) × s × a = (1/2) × a × (n × s) = (1/2) × a × P. The polygon formula IS triangle area applied n times and consolidated — it is not a separate formula but a direct consequence of the triangular decomposition."

- question: "As the number of sides of a regular polygon increases without bound, the formula A = (1/2) × apothem × perimeter converges to the circle area formula πr²."
  type: true-false
  answer: true
  explanation: "As n → ∞, the apothem approaches the radius r (the perpendicular to the midpoint of an increasingly short side converges toward the vertex distance), and the perimeter approaches the circumference 2πr. Substituting into the polygon formula: (1/2) × r × 2πr = πr². The circle is the limiting case of a regular polygon, and the circle area formula emerges naturally from the polygon formula taken to its limit."

- question: "Explain why the apothem — not the radius — appears in the area formula for regular polygons, and describe the geometric role the apothem plays in the derivation."
  type: short-answer
  answer: "When a regular n-gon is divided into n congruent triangles (by connecting the center to each vertex), the apothem is the height of each triangle. Triangle area = (1/2) × base × height, where height is always the perpendicular distance from the apex to the base. The base of each triangle is one side of the polygon; the perpendicular from the center to the midpoint of that base is the apothem. The radius (center to vertex) is the slant side of each triangle, not its height — using the radius would not give the triangle's height and would overestimate the area. The apothem is the right measurement precisely because it is the perpendicular height."
  explanation: "A useful check: for a regular hexagon with side length s, the triangles are equilateral. The apothem is the altitude of an equilateral triangle = s√3/2. Using A = (1/2) × a × P = (1/2) × (s√3/2) × (6s) = (3s²√3)/2, which matches the known formula for a regular hexagon. The triangular decomposition is both the derivation and the verification."
```

## Explainer

You already know that a regular polygon has all sides equal and all angles equal. The key to finding its area is a beautifully simple dissection: slice the polygon into congruent triangles by drawing a line from the center to each vertex. A regular hexagon splits into 6 triangles, a square into 4, an octagon into 8. Each triangle has its tip at the center and its base as one side of the polygon. Because the polygon is regular, all these triangles are identical, so the total area is just (number of sides) × (area of one triangle).

Every triangle has base = side length s and height = **apothem** a, the perpendicular distance from the center to the midpoint of a side. Note carefully: the apothem goes to the *midpoint* of a side, not to a vertex — that distance would be the circumscribed radius r. The area of each triangle is (1/2) × s × a. Multiply by n triangles and collect terms: total area = n × (1/2) × s × a = (1/2) × (n × s) × a. But n × s is just the perimeter P, so the formula simplifies to **A = (1/2) × a × P**. The perimeter wraps around the outside; the apothem measures how "deep" the polygon is from outside to center.

When you know the side length but not the apothem, trigonometry fills the gap. The center-to-vertex line and the apothem together form a right triangle inside one of the n slices. The central angle of each slice is 360°/n, so the half-angle at the center is 180°/n. The apothem is the adjacent side of this right triangle, and half the side length (s/2) is the opposite side. That means tan(180°/n) = (s/2)/a, so a = (s/2)/tan(180°/n). For a regular hexagon with side 1, the central half-angle is 30°, tan(30°) = 1/√3, so a = (1/2)/(1/√3) = √3/2 — which you can verify directly since a regular hexagon is made of equilateral triangles.

This formula connects to the limiting case that is a circle: as n grows large, a regular n-gon approaches a circle. The apothem approaches the radius r, and the perimeter approaches the circumference 2πr. Substituting into the polygon formula gives (1/2)(r)(2πr) = πr² — the exact formula for circle area. The polygon formula is not just a useful calculation tool; it is the geometric reason the circle area formula is what it is.
