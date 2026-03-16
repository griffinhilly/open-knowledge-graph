---
id: pythagorean-theorem
title: Pythagorean Theorem
domain: mathematics
course: geometry
prerequisites:
  - id: segment-and-distance
    type: hard
  - id: triangle-angle-sum
    type: soft
  - id: square-roots-intro
    type: hard
builds-toward:
  - pythagorean-theorem-converse
  - right-triangle-trigonometry-intro
  - special-right-triangles-30-60-90
  - special-right-triangles-45-45-90
tags: [pythagorean-theorem, right-triangles, distance]
stage: abstract-reasoning
status: validated
---

# Pythagorean Theorem

## Core Idea
In a right triangle with legs a and b and hypotenuse c, a^2 + b^2 = c^2. This is arguably the most important theorem in geometry, connecting side lengths in right triangles and underlying the distance formula in coordinate geometry. There are hundreds of known proofs, from geometric (rearrangement of areas) to algebraic.

## How It's Best Learned
Start with a visual proof: arrange four copies of the right triangle around a square to show the area relationship. Practice finding the hypotenuse given two legs, and finding a leg given the hypotenuse and the other leg. Apply to coordinate geometry (deriving the distance formula). Introduce Pythagorean triples (3-4-5, 5-12-13, 8-15-17).

## Common Misconceptions
- Using a^2 + b^2 = c^2 with c as a leg instead of the hypotenuse.
- Forgetting to take the square root at the end.
- Thinking the theorem applies to non-right triangles (it does not, though the law of cosines generalizes it).
- Not simplifying radicals in exact answers.

## Questions

```yaml
- question: "A right triangle has legs of length 5 and 12. What is the length of the hypotenuse?"
  type: multiple-choice
  options: ["13", "17", "√119", "60"]
  answer: 0
  explanation: "Apply a² + b² = c²: 5² + 12² = 25 + 144 = 169 = 13². So c = 13. This is the classic 5-12-13 Pythagorean triple. Note that 17 is a common distractor (5 + 12), and 60 is the product — neither is correct."

- question: "The Pythagorean theorem states that for any triangle, a² + b² = c², where c is the longest side."
  type: true-false
  answer: false
  explanation: "The theorem applies only to right triangles, and c must specifically be the hypotenuse — the side opposite the right angle. For a non-right triangle with sides 4, 5, 6, the equation 4² + 5² = 6² gives 41 ≠ 36, which is false but does not contradict the theorem (it just confirms the triangle is not a right triangle). The generalization to arbitrary triangles requires the law of cosines."

- question: "How does the Pythagorean theorem lead directly to the distance formula between two points in the coordinate plane?"
  type: short-answer
  answer: "The horizontal and vertical distances between the two points form the legs of a right triangle, and the straight-line distance is the hypotenuse. Applying a² + b² = c² gives d = √((x₂ − x₁)² + (y₂ − y₁)²)."
  explanation: "This connection shows that the Pythagorean theorem is not just about triangles drawn on paper — it underlies the very definition of distance in the Cartesian plane. Every time you compute a distance in coordinate geometry, you are applying the Pythagorean theorem."
```

## Explainer

The Pythagorean theorem says that in any right triangle, if you label the two shorter sides (legs) as a and b and the longest side (hypotenuse) as c, then a² + b² = c². The hypotenuse is always the side opposite the right angle — identifying it correctly is the first step in every problem.

One of the most convincing proofs is purely visual. Take four identical right triangles and arrange them around a square so that their hypotenuses form the sides of the outer square (side length c) and their corners create a smaller inner square (side length a − b). The area of the outer square is c². The area of the four triangles is 4 · (½ab) = 2ab. The area of the inner square is (a − b)². Setting up the equation: c² = 2ab + (a − b)² = 2ab + a² − 2ab + b² = a² + b². The algebra confirms the picture. This proof requires nothing beyond area and algebra — and that is part of why the theorem has hundreds of known proofs spanning 2,500 years.

In practice, there are two kinds of problems: finding the hypotenuse given both legs (add the squares, then square root), and finding a leg given the hypotenuse and the other leg (subtract the squares, then square root). For the second type, students often make the mistake of adding instead of subtracting. If c = 13 and a = 5, then b² = c² − a² = 169 − 25 = 144, so b = 12 — not √(169 + 25).

Pythagorean triples — integer solutions like (3, 4, 5), (5, 12, 13), and (8, 15, 17) — are worth memorizing because they appear constantly and let you avoid messy radicals. When you see sides 3 and 4, you immediately know the hypotenuse is 5; you don't need to compute √(9 + 16).

The theorem's reach extends far beyond triangles drawn in isolation. In coordinate geometry, the distance between points (x₁, y₁) and (x₂, y₂) is exactly the hypotenuse of a right triangle with legs |x₂ − x₁| and |y₂ − y₁|, giving d = √((x₂ − x₁)² + (y₂ − y₁)²). This connection means the Pythagorean theorem is embedded in the very definition of distance — and by extension, in physics, engineering, and every branch of mathematics that uses coordinates.
