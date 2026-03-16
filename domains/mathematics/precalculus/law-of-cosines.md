---
id: law-of-cosines
title: Law of Cosines
domain: mathematics
course: precalculus
prerequisites:
  - id: trigonometric-ratios-review
    type: hard
builds-toward:
  - dot-product
tags: [trigonometry, triangles, law-of-cosines]
stage: formal-systems
status: validated
---

# Law of Cosines

## Core Idea
The Law of Cosines states that c^2 = a^2 + b^2 - 2ab*cos(C), generalizing the Pythagorean theorem to non-right triangles (when C = 90, the formula reduces to c^2 = a^2 + b^2). It is used when you know two sides and the included angle (SAS) or all three sides (SSS). Combined with the Law of Sines, it allows you to solve any triangle.

## How It's Best Learned
Derive using coordinate geometry or the distance formula. Practice SAS cases (find the third side) and SSS cases (find an angle). Compare with the Pythagorean theorem to build intuition about the correction term -2ab*cos(C).

## Common Misconceptions
- Forgetting the negative sign in -2ab*cos(C), especially when the angle is obtuse (which makes cos(C) negative, so the term adds).
- Using the wrong angle in the formula (C must be the angle between sides a and b).
- Not recognizing when to use Law of Cosines vs. Law of Sines.

## Explainer

The **Law of Cosines** is a generalization of the Pythagorean theorem you've relied on for right triangles. The Pythagorean theorem says c² = a² + b² when angle C is exactly 90°. But most triangles don't have a right angle. The Law of Cosines corrects for the deviation: c² = a² + b² − 2ab·cos(C), where C is the angle opposite side c and between sides a and b. When C = 90°, cos(90°) = 0, so the correction term vanishes and you're back to the Pythagorean theorem. The law works for any angle in any triangle.

The intuition for the correction term comes from how the angle C pushes the opposite side c longer or shorter. When C is acute (less than 90°), cos(C) is positive, so −2ab·cos(C) is negative — the correction shrinks c² below a² + b². Think of it this way: a narrow angle brings two sides close together, making the opposite side shorter than the Pythagorean guess. When C is obtuse (greater than 90°), cos(C) is negative, so −2ab·cos(C) becomes positive — the correction stretches c² above a² + b². An obtuse angle splays the sides apart, making the opposite side longer than the right-angle case would suggest. This is why the formula makes geometric sense even when you can't visualize it directly.

You use the Law of Cosines in two situations based on what information you have. In the **SAS case** (two sides and the included angle), you know a, b, and C, and you compute c directly. In the **SSS case** (all three sides), you know a, b, and c, and you solve for the angle: cos(C) = (a² + b² − c²) / (2ab). Rearranging to find angles from sides is exactly backward from finding sides from angles — just divide through by 2ab and apply arccosine. When you need to find a remaining angle after using SAS to find the third side, you can either apply the Law of Cosines again or switch to the Law of Sines, whichever is more convenient.

The connection to the **dot product** you'll encounter later is not coincidental. The dot product of two vectors **a** and **b** is defined as |**a**||**b**|cos(θ), where θ is the angle between them. The Law of Cosines is essentially the statement that |**a** − **b**|² = |**a**|² + |**b**|² − 2**a**·**b**. In other words, the Law of Cosines is the dot product identity written in terms of side lengths and angles. This connection reveals why cosine appears naturally in triangle geometry — it measures the geometric projection of one side onto another.
