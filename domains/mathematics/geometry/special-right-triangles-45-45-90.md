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

## Explainer

Start with something you already know: a square with side length 1. Draw its diagonal. You've just created two 45-45-90 triangles. Because the square is symmetric, both legs of each triangle are equal — they're just the sides of the square, length 1. Now apply the Pythagorean theorem, your hard prerequisite: the hypotenuse satisfies 1² + 1² = c², so c² = 2, giving c = √2. That's the entire derivation. The **45-45-90 ratio** is 1 : 1 : √2, and it comes directly from the geometry of a square.

The ratio scales to any 45-45-90 triangle. If the legs each have length s, the hypotenuse is s√2. If the hypotenuse is h, each leg is h/√2 — which you rationalize as h√2/2. The key mental shortcut is: **leg × √2 = hypotenuse**, and **hypotenuse ÷ √2 = leg**. Every 45-45-90 problem reduces to one of these two operations. You never need to re-derive from the Pythagorean theorem once you've internalized the ratio.

This triangle also gives you the exact trigonometric values at 45°. Since sin(θ) = opposite/hypotenuse in a right triangle, and both legs and the hypotenuse are in ratio 1:1:√2, sin(45°) = 1/√2 = √2/2. By symmetry (it's isosceles), cos(45°) = √2/2 as well. And tan(45°) = opposite/adjacent = 1/1 = 1. These are exact values — not decimal approximations — and they come directly from the geometry you just worked out. Knowing them cold is essential for trigonometry and the unit circle.

The 45-45-90 triangle appears constantly in practical geometry: the diagonal of any square, the cross-section of a square prism, the 45° angles in regular octagon constructions, and any "tilted square" problem. Whenever a problem involves a square, its diagonal, or a 45° angle, this triangle is almost certainly in play. When you later study the unit circle, you'll place this triangle at the 45° (π/4) position, and the coordinates there — (√2/2, √2/2) — are exactly the leg-to-hypotenuse ratios you derived here. The geometry and the trigonometry are the same thing, viewed from different angles.
