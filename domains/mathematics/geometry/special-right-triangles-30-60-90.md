---
id: special-right-triangles-30-60-90
title: 'Special Right Triangles: 30-60-90'
domain: mathematics
course: geometry
prerequisites:
- id: pythagorean-theorem
  type: hard
- id: sine-cosine-tangent-ratios
  type: soft
builds-toward:
- trigonometric-ratios-review
- unit-circle
tags:
- special-right-triangles
- 30-60-90
- exact-values
stage: abstract-reasoning
status: validated
---
# Special Right Triangles: 30-60-90

## Core Idea
A 30-60-90 triangle has sides in the ratio 1 : sqrt(3) : 2. The shortest side (opposite 30) is half the hypotenuse, and the longer leg (opposite 60) is sqrt(3) times the shorter leg. This triangle arises from bisecting an equilateral triangle. Knowing these ratios allows exact computation without a calculator and provides the exact values for sin/cos/tan of 30 and 60 degrees.

## How It's Best Learned
Derive the ratios by cutting an equilateral triangle in half and applying the Pythagorean theorem to find the altitude. Practice scaling: if the hypotenuse is 10, the short leg is 5 and the long leg is 5*sqrt(3). Work problems in both directions (given any one side, find the others).

## Common Misconceptions
- Putting sqrt(3) with the wrong side (it goes with the longer leg, opposite 60, not the shorter leg).
- Confusing 30-60-90 ratios with 45-45-90 ratios.
- Thinking the ratio 1:sqrt(3):2 means the sides are literally 1, sqrt(3), and 2 rather than being scalable by any factor.

## Questions

```yaml
- question: "A 30-60-90 triangle has a hypotenuse of 14. What is the length of the longer leg?"
  type: multiple-choice
  options:
    - "7"
    - "7√3"
    - "14√3"
    - "7√2"
  answer: 1
  explanation: "The scale factor is 7 (hypotenuse = 2 × scale factor, so 14 ÷ 2 = 7). The longer leg is opposite the 60° angle and equals √3 × scale factor = 7√3. Option D (7√2) is the error of applying 45-45-90 ratios; option C forgets to apply the scale factor correctly."

- question: "A student claims: 'In a 30-60-90 triangle with short leg 5, the side opposite 60° has length 5√2.' What is wrong?"
  type: multiple-choice
  options:
    - "Nothing — √2 applies when you double the short leg"
    - "The side opposite 60° is 5√3, not 5√2 — √2 belongs to the 45-45-90 triangle"
    - "The short leg should be 10 for this computation to work"
    - "The hypotenuse is 5√2, not the longer leg"
  answer: 1
  explanation: "The 30-60-90 ratios are 1 : √3 : 2. The longer leg (opposite 60°) is always √3 times the shorter leg — here, 5√3. The student confused this with the 45-45-90 triangle, whose ratio is 1 : 1 : √2. This is the single most common error on problems involving special right triangles."

- question: "In a 30-60-90 triangle, the hypotenuse is exactly twice the length of the shortest side."
  type: true-false
  answer: true
  explanation: "This follows directly from the 1 : √3 : 2 ratio. The shortest side (opposite 30°) corresponds to ratio 1, and the hypotenuse corresponds to ratio 2 — always double, regardless of the scale factor. Deriving this from the equilateral triangle construction makes it unforgettable: the short leg is half the original equilateral triangle's side, and the hypotenuse is the full side."

- question: "The ratio 1 : √3 : 2 in a 30-60-90 triangle means the sides is expected to measure exactly 1, √3, and 2 units."
  type: true-false
  answer: false
  explanation: "The ratio is scalable by any positive factor. A 30-60-90 triangle with hypotenuse 10 has sides 5, 5√3, and 10. The ratio describes the proportional relationship, not the literal measurements. Thinking the ratios are fixed values (not a scalable template) is one of the most common misconceptions with special right triangles."

- question: "How can you derive the 30-60-90 side ratios from scratch without memorizing them?"
  type: short-answer
  answer: "Start with an equilateral triangle with all sides of length 2. Cut it in half with an altitude from one vertex to the midpoint of the opposite side. Each half is a right triangle with hypotenuse 2 (one original side), short leg 1 (half the base), and a 30-60-90 degree angle arrangement. Apply the Pythagorean theorem to find the altitude: 1² + h² = 2², so h = √3. The ratio is therefore 1 : √3 : 2."
  explanation: "This derivation matters because it ties the ratios to geometry you already know, making them impossible to forget. It also reveals why √3 goes with the 60° angle — it is the altitude of the equilateral triangle — which prevents the common error of putting √3 on the wrong side."
```

## Explainer

You know the Pythagorean theorem: in a right triangle, a² + b² = c². The 30-60-90 triangle gives you a specific set of side ratios you can derive once and then use forever — no calculator required. Start with an equilateral triangle where every side has length 2 and every angle is 60°. Cut it straight down the middle from one vertex to the opposite side's midpoint. This produces two congruent right triangles. Each right triangle has a hypotenuse of 2 (one full side of the equilateral triangle), a short leg of 1 (half the base), and angles of 30°, 60°, and 90°. The long leg — the altitude you just cut along — can be found with the Pythagorean theorem: 1² + h² = 2², so h² = 3, and h = √3. The sides are in ratio 1 : √3 : 2.

The mnemonic for which side goes where: the **short leg** (length 1) is opposite the **30° angle**, the **long leg** (length √3) is opposite the **60° angle**, and the **hypotenuse** (length 2) is opposite the **90° angle**. Opposite the biggest angle is the longest side — that ordering is consistent with everything you know about triangles. The √3 always belongs to the 60° side; many mistakes come from accidentally swapping the two legs.

These ratios are scalable. If the hypotenuse is 10, multiply every ratio value by 5: short leg = 5, long leg = 5√3. If the short leg is 7, the hypotenuse is 14 and the long leg is 7√3. The scale factor is whatever you need to match the given side. The only rule: identify which side you're given and which position (short leg / long leg / hypotenuse) it occupies, then compute the scale factor from there.

The payoff extends into trigonometry. The sine, cosine, and tangent of 30° and 60° come directly from this triangle. sin(30°) = opposite/hypotenuse = 1/2; cos(30°) = adjacent/hypotenuse = √3/2; tan(30°) = 1/√3. For 60°, the roles of the legs swap: sin(60°) = √3/2; cos(60°) = 1/2; tan(60°) = √3. These are the exact values you'll use throughout trigonometry and precalculus — knowing their origin in the 30-60-90 triangle makes them impossible to forget and easy to re-derive when needed.
