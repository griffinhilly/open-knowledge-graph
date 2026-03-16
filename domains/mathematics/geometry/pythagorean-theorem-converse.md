---
id: pythagorean-theorem-converse
title: Pythagorean Theorem Converse
domain: mathematics
course: geometry
prerequisites:
  - id: pythagorean-theorem
    type: hard
builds-toward:
  - coordinate-geometry-proofs
tags: [pythagorean-theorem, converse, triangle-classification]
stage: abstract-reasoning
status: validated
---

# Pythagorean Theorem Converse

## Core Idea
The converse of the Pythagorean Theorem states: if a^2 + b^2 = c^2 for the sides of a triangle (where c is the longest side), then the triangle is a right triangle. Moreover, if a^2 + b^2 > c^2, the triangle is acute, and if a^2 + b^2 < c^2, the triangle is obtuse. This allows us to classify triangles by angle type using only side lengths.

## How It's Best Learned
Give students sets of three side lengths and have them classify the triangle as right, acute, or obtuse using the Pythagorean inequality. Emphasize that c must be the longest side. Connect to the original theorem: the converse goes from sides to angle classification, while the original goes from a right angle to a side relationship.

## Common Misconceptions
- Not assigning c to the longest side before checking the equation.
- Confusing the direction of the inequality (a^2 + b^2 > c^2 is acute, not obtuse).
- Thinking the converse is trivially true because the theorem is true; converses must be proven separately.

## Explainer

The Pythagorean Theorem you already know runs in one direction: *if* a triangle has a right angle, *then* the square of the hypotenuse equals the sum of the squares of the other two sides (a² + b² = c²). The **converse** reverses this: *if* the sides of a triangle satisfy a² + b² = c² (with c as the longest side), *then* the triangle must have a right angle. These are different logical claims, and a theorem being true does not automatically make its converse true — converses require their own proofs.

The standard proof constructs a companion triangle. Given a triangle with sides a, b, c satisfying a² + b² = c², build a *second* triangle with legs a and b and a right angle between them. By the Pythagorean Theorem, that second triangle has hypotenuse √(a² + b²) = √(c²) = c. So both triangles have the same three side lengths. By the SSS (side-side-side) congruence rule you know from geometry, the two triangles are congruent — meaning the original triangle has a right angle too, in exactly the same position as the constructed one.

The full classification extends this logic to all triangles. Imagine inflating or deflating the angle opposite the longest side c. When the angle is exactly 90°, we have a² + b² = c². If you *increase* that angle past 90° to make an **obtuse** triangle, the opposite side c grows longer, so a² + b² < c². If you *decrease* the angle below 90° for an **acute** triangle, c shrinks, so a² + b² > c². The inequality direction can feel counterintuitive — remember the rule as: **acute means the sum is too big** (the sides are "more than enough" for a right angle), while **obtuse means the sum is too small** (the sides "fall short").

This theorem is a practical classification tool: given any three side lengths, assign the longest to c, compute a² + b² and c², compare, and immediately know the triangle type without measuring any angles. For example, sides 5, 12, 13: 5² + 12² = 25 + 144 = 169 = 13². Right triangle. Sides 5, 12, 14: 169 < 196, so obtuse. Sides 5, 12, 12: 169 > 144, so acute. The converse transforms a purely numerical test into a geometric conclusion — a powerful bridge between algebra and shape.
