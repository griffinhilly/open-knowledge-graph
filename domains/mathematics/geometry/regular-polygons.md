---
id: regular-polygons
title: Regular Polygons
domain: mathematics
course: geometry
prerequisites:
  - id: polygon-angle-sums
    type: hard
builds-toward:
  - area-of-regular-polygons
tags: [polygons, regular-polygons, symmetry, interior-angles]
stage: abstract-reasoning
status: validated
---

# Regular Polygons

## Core Idea
A regular polygon has all sides congruent and all angles congruent. Each interior angle of a regular n-gon measures (n-2)(180)/n degrees. Each exterior angle measures 360/n degrees. Regular polygons have n lines of symmetry and rotational symmetry of order n. They tile the plane only for n = 3, 4, and 6 (equilateral triangles, squares, regular hexagons).

## How It's Best Learned
Compute interior angles for regular polygons with n = 3 through 10. Observe that as n increases, the interior angle approaches 180. Explore symmetry by folding and rotating. Connect to the inscribed polygon inside a circle. Discuss tilings and why only three regular polygons tile the plane.

## Common Misconceptions
- Assuming any equilateral polygon is regular (equilateral does not imply equiangular for polygons with more than 3 sides, e.g., a rhombus is equilateral but not regular).
- Confusing the interior angle formula with the angle sum formula.
- Thinking all regular polygons can tile the plane.

## Explainer

From your work on **polygon angle sums**, you know that an n-gon's interior angles sum to (n−2) × 180°. A **regular polygon** has one extra condition on top of that: all sides equal *and* all angles equal. Because all n interior angles are equal and they sum to (n−2) × 180°, each interior angle measures (n−2) × 180° / n. For a triangle (n = 3): (1 × 180°)/3 = 60°. For a square (n = 4): (2 × 180°)/4 = 90°. For a regular hexagon (n = 6): (4 × 180°)/6 = 120°. As n grows, the formula approaches 180°, which makes geometric sense — a polygon with very many sides looks like a circle, and its angles approach the "straight" 180°.

The **exterior angle** is the supplement of the interior angle: 180° − (n−2)×180°/n = 360°/n. This is simpler to remember and deeply intuitive: if you walk all the way around any convex polygon, you turn a total of 360°. For a regular polygon, every turn is equal, so each exterior angle is 360°/n. A regular pentagon has exterior angles of 72°; a regular octagon has 45°. This formula also shows why there's no regular polygon with fewer than 3 sides — you'd need to divide 360° into fewer than 3 parts and still have an interior angle that's positive.

Regular polygons have a rich **symmetry** structure. An n-gon has n lines of reflection symmetry (through each vertex and the midpoint of the opposite side for even n; through each vertex and opposite edge midpoint for odd n) and rotational symmetry of order n (it looks the same after rotations of 360°/n). This double symmetry — reflective and rotational — is what distinguishes regular polygons from merely equilateral or merely equiangular ones.

The question of which regular polygons **tile the plane** (cover it without gaps or overlaps using identical copies) comes down to whether the interior angle divides evenly into 360°. For tiles meeting at a vertex, the angles must sum to exactly 360°. The interior angles of equilateral triangles (60°), squares (90°), and regular hexagons (120°) all divide 360° evenly (6, 4, and 3 meeting at each vertex). For pentagons the interior angle is 108°, and 360/108 is not a whole number, so regular pentagons cannot tile the plane alone. This reasoning about angle divisibility is why exactly three regular polygons admit a regular tiling.
