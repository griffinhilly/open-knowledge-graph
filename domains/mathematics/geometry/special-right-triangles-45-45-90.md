---
id: special-right-triangles-45-45-90
title: 'Special Right Triangles: 45-45-90'
domain: mathematics
course: geometry
prerequisites:
- id: pythagorean-theorem
  type: hard
- id: isosceles-triangle-theorem
  type: soft
- id: sine-cosine-tangent-ratios
  type: soft
builds-toward:
- trigonometric-ratios-review
- unit-circle
tags:
- special-right-triangles
- 45-45-90
- exact-values
stage: abstract-reasoning
status: validated
---
# Special Right Triangles: 45-45-90

## Core Idea
A 45-45-90 triangle is an isosceles right triangle with sides in the ratio 1 : 1 : sqrt(2). The two legs are equal, and the hypotenuse is sqrt(2) times a leg. This triangle arises from cutting a square along its diagonal. It provides the exact values for sin(45), cos(45), and tan(45) = 1.

## How It's Best Learned
Derive by cutting a unit square diagonally and applying the Pythagorean theorem. Practice finding sides given one measurement. Compare with 30-60-90 to reinforce the distinct ratios. Apply to real-world problems involving diagonals of squares and 45-degree angles.

## Common Misconceptions
- Multiplying the leg by 2 instead of sqrt(2) to get the hypotenuse.
- Confusing 45-45-90 with 30-60-90 ratios.
- Rationalizing denominators incorrectly when the hypotenuse is given and legs must be found (divide by sqrt(2), which equals multiplying by sqrt(2)/2).

## Questions

```yaml
- question: "The legs of a 45-45-90 triangle are each 7 cm. What is the hypotenuse?"
  type: multiple-choice
  options:
    - "14 cm"
    - "7√3 cm"
    - "7√2 cm"
    - "7/√2 cm"
  answer: 2
  explanation: "In a 45-45-90 triangle, hypotenuse = leg × √2. So 7 × √2 = 7√2 cm. Option A (14 cm) is the most common error — students multiply the leg by 2 instead of √2, confusing this with doubling. Option B (7√3) comes from the 30-60-90 triangle, where the long leg = short leg × √3."

- question: "The hypotenuse of a 45-45-90 triangle is 10 cm. What is the length of each leg?"
  type: multiple-choice
  options:
    - "5 cm"
    - "10√2 cm"
    - "5√2 cm"
    - "10/√3 cm"
  answer: 2
  explanation: "When the hypotenuse is given, each leg = hypotenuse ÷ √2. Rationalizing: 10/√2 = 10√2/2 = 5√2 cm. Option A (5 cm) is wrong — it halves the hypotenuse instead of dividing by √2. Option B multiplies instead of divides. The key move is dividing by √2 and rationalizing, not halving."

- question: "In a 45-45-90 triangle, the hypotenuse is twice the length of each leg."
  type: true-false
  answer: false
  explanation: "The hypotenuse is √2 times the leg, not twice. Since √2 ≈ 1.414, the hypotenuse is about 41% longer than a leg — significantly less than double. This is one of the most persistent misconceptions. The factor of 2 applies to the *square* of the sides (1² + 1² = 2), not to the sides themselves."

- question: "A 45-45-90 triangle can be produced by cutting a square along its diagonal."
  type: true-false
  answer: true
  explanation: "Cutting a unit square diagonally produces two congruent triangles, each with two legs of length 1 (the square's sides) and angles of 45-45-90 (since the square's corners are 90° and the diagonal bisects each symmetrically). Applying the Pythagorean theorem gives the hypotenuse as √(1² + 1²) = √2. This is the cleanest derivation of the 1:1:√2 ratio."

- question: "Where does the √2 in the 45-45-90 side ratio come from? Explain the derivation."
  type: short-answer
  answer: "In an isosceles right triangle with legs of length 1, the Pythagorean theorem gives c² = 1² + 1² = 2, so c = √2. The √2 arises because both legs are equal, meaning you are squaring the same number twice and adding — which is equivalent to multiplying that square by 2, then taking the square root."
  explanation: "The derivation is pure Pythagorean theorem on equal legs. The key insight is that the hypotenuse is not simply the sum of the legs (which would give 2) but rather the square root of the sum of their squares (√2). This is why the ratio is 1:1:√2 and not 1:1:2 — a distinction that matters in every applied problem."
```

## Explainer

Start with something you already know: a square with side length 1. Draw its diagonal. You've just created two 45-45-90 triangles. Because the square is symmetric, both legs of each triangle are equal — they're just the sides of the square, length 1. Now apply the Pythagorean theorem, your hard prerequisite: the hypotenuse satisfies 1² + 1² = c², so c² = 2, giving c = √2. That's the entire derivation. The **45-45-90 ratio** is 1 : 1 : √2, and it comes directly from the geometry of a square.

The ratio scales to any 45-45-90 triangle. If the legs each have length s, the hypotenuse is s√2. If the hypotenuse is h, each leg is h/√2 — which you rationalize as h√2/2. The key mental shortcut is: **leg × √2 = hypotenuse**, and **hypotenuse ÷ √2 = leg**. Every 45-45-90 problem reduces to one of these two operations. You never need to re-derive from the Pythagorean theorem once you've internalized the ratio.

This triangle also gives you the exact trigonometric values at 45°. Since sin(θ) = opposite/hypotenuse in a right triangle, and both legs and the hypotenuse are in ratio 1:1:√2, sin(45°) = 1/√2 = √2/2. By symmetry (it's isosceles), cos(45°) = √2/2 as well. And tan(45°) = opposite/adjacent = 1/1 = 1. These are exact values — not decimal approximations — and they come directly from the geometry you just worked out. Knowing them cold is essential for trigonometry and the unit circle.

The 45-45-90 triangle appears constantly in practical geometry: the diagonal of any square, the cross-section of a square prism, the 45° angles in regular octagon constructions, and any "tilted square" problem. Whenever a problem involves a square, its diagonal, or a 45° angle, this triangle is almost certainly in play. When you later study the unit circle, you'll place this triangle at the 45° (π/4) position, and the coordinates there — (√2/2, √2/2) — are exactly the leg-to-hypotenuse ratios you derived here. The geometry and the trigonometry are the same thing, viewed from different angles.
