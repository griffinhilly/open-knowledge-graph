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

## Questions

```yaml
- question: "A triangle has sides 6, 8, and 11. What type of triangle is it?"
  type: multiple-choice
  options:
    - "Right — 6² + 8² = 100 is close enough to 11² = 121"
    - "Acute — because the two shorter sides together exceed the longest side"
    - "Obtuse — because 6² + 8² = 100 < 11² = 121"
    - "Cannot be classified using side lengths alone"
  answer: 2
  explanation: "Assign the longest side to c: c = 11. Compute a² + b² = 36 + 64 = 100, and c² = 121. Since 100 < 121, we have a² + b² < c², which means the triangle is obtuse. The common error is reversing the inequalities — students often think 'the sum falls short, so it must be acute,' but the logic runs the other way: an obtuse angle makes the opposite side grow, so c² grows larger than a² + b²."

- question: "Which set of side lengths forms a right triangle?"
  type: multiple-choice
  options:
    - "5, 12, 14"
    - "7, 24, 25"
    - "3, 4, 6"
    - "8, 15, 18"
  answer: 1
  explanation: "Test each by assigning the largest side to c and checking a² + b² = c². For 7, 24, 25: 7² + 24² = 49 + 576 = 625 = 25². ✓ For 5, 12, 14: 25 + 144 = 169 ≠ 196. For 3, 4, 6: 9 + 16 = 25 ≠ 36. For 8, 15, 18: 64 + 225 = 289 ≠ 324. Only 7-24-25 satisfies the equation — this is a well-known Pythagorean triple."

- question: "If a triangle's sides satisfy a² + b² > c² (where c is the longest side), the triangle is obtuse."
  type: true-false
  answer: false
  explanation: "This is the most common inequality mix-up. When a² + b² > c², the triangle is ACUTE. The logic: an obtuse angle causes the opposite side to grow longer, making c² exceed a² + b². Conversely, if a² + b² is MORE than c², the angle opposite c is less than 90° — the triangle is acute. Memory aid: 'acute means the sum is too big' (the sides are more than needed for a right angle)."

- question: "The converse of the Pythagorean Theorem requires its own separate proof because a theorem being true does not guarantee its converse is also true."
  type: true-false
  answer: true
  explanation: "This is a fundamental point in logic: the converse of a true statement is not automatically true. The standard proof of the converse constructs a companion right triangle with the same leg lengths, then uses SSS congruence to conclude that the original triangle must also have a right angle. Without this proof, we couldn't legitimately reverse the theorem's direction."

- question: "Why must c be assigned to the longest side before applying the Pythagorean converse? What goes wrong if you don't?"
  type: short-answer
  answer: "c must be the longest side because the inequality test is built around the relationship between the largest angle and its opposite side. The Pythagorean theorem says the hypotenuse (longest side, opposite the largest angle) satisfies a² + b² = c². If you assign c to a shorter side, a² + b² will almost always exceed c² — giving a misleading 'acute' result — even for right or obtuse triangles. The test only works correctly when c is the candidate for the role of hypotenuse."
  explanation: "Example: for sides 3, 4, 5, if you mistakenly set c = 3, you get 4² + 5² = 41 > 9, suggesting 'acute' — but the triangle is actually right. The converse test classifies the angle opposite the longest side; only the longest side has any chance of being the hypotenuse."
```

## Explainer

The Pythagorean Theorem you already know runs in one direction: *if* a triangle has a right angle, *then* the square of the hypotenuse equals the sum of the squares of the other two sides (a² + b² = c²). The **converse** reverses this: *if* the sides of a triangle satisfy a² + b² = c² (with c as the longest side), *then* the triangle must have a right angle. These are different logical claims, and a theorem being true does not automatically make its converse true — converses require their own proofs.

The standard proof constructs a companion triangle. Given a triangle with sides a, b, c satisfying a² + b² = c², build a *second* triangle with legs a and b and a right angle between them. By the Pythagorean Theorem, that second triangle has hypotenuse √(a² + b²) = √(c²) = c. So both triangles have the same three side lengths. By the SSS (side-side-side) congruence rule you know from geometry, the two triangles are congruent — meaning the original triangle has a right angle too, in exactly the same position as the constructed one.

The full classification extends this logic to all triangles. Imagine inflating or deflating the angle opposite the longest side c. When the angle is exactly 90°, we have a² + b² = c². If you *increase* that angle past 90° to make an **obtuse** triangle, the opposite side c grows longer, so a² + b² < c². If you *decrease* the angle below 90° for an **acute** triangle, c shrinks, so a² + b² > c². The inequality direction can feel counterintuitive — remember the rule as: **acute means the sum is too big** (the sides are "more than enough" for a right angle), while **obtuse means the sum is too small** (the sides "fall short").

This theorem is a practical classification tool: given any three side lengths, assign the longest to c, compute a² + b² and c², compare, and immediately know the triangle type without measuring any angles. For example, sides 5, 12, 13: 5² + 12² = 25 + 144 = 169 = 13². Right triangle. Sides 5, 12, 14: 169 < 196, so obtuse. Sides 5, 12, 12: 169 > 144, so acute. The converse transforms a purely numerical test into a geometric conclusion — a powerful bridge between algebra and shape.
