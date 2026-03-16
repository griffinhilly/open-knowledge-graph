---
id: right-triangle-trigonometry-intro
title: Right Triangle Trigonometry Introduction
domain: mathematics
course: geometry
prerequisites:
- id: similar-triangles-aa
  type: hard
- id: pythagorean-theorem
  type: hard
- id: proportions-in-similar-triangles
  type: soft
builds-toward:
- sine-cosine-tangent-ratios
tags:
- trigonometry
- right-triangles
- ratios
- introduction
stage: abstract-reasoning
status: validated
---
# Right Triangle Trigonometry Introduction

## Core Idea
Right triangle trigonometry connects angle measures to side ratios. Because all right triangles with the same acute angle are similar (by AA), the ratios of their sides depend only on the angle, not the triangle's size. This insight motivates defining the trigonometric ratios. For any acute angle in a right triangle, the ratios opposite/hypotenuse, adjacent/hypotenuse, and opposite/adjacent are constant across all similar triangles.

## How It's Best Learned
Start by having students measure sides of several right triangles with the same acute angle and compute ratios, observing they are constant. Connect this to AA similarity. Then name the ratios (sine, cosine, tangent). Use SOHCAHTOA as a mnemonic only after the concept is understood.

## Common Misconceptions
- Thinking trigonometric ratios depend on the size of the triangle rather than just the angle.
- Not understanding which side is "opposite" and which is "adjacent" (these change depending on which acute angle you are considering).
- Trying to apply right triangle trigonometry to non-right triangles.

## Questions

```yaml
- question: "If two right triangles both contain a 40° angle, what can you say about the ratio (opposite side) / hypotenuse in each triangle?"
  type: multiple-choice
  options:
    - "The ratio is larger in the bigger triangle"
    - "The ratio is the same in both triangles"
    - "The ratio depends on the length of the hypotenuse"
    - "The ratio is the same only if the triangles are congruent"
  answer: 1
  explanation: "All right triangles with the same acute angle are similar by AA similarity (they share the right angle and the given acute angle). Similar triangles have proportional sides, so the ratio of any two corresponding sides is constant — it depends only on the angle, not the size of the triangle. This is the foundational insight that makes trigonometry possible."

- question: "In a right triangle, the labels 'opposite' and 'adjacent' refer to fixed sides of the triangle that do not change regardless of which angle you focus on."
  type: true-false
  answer: false
  explanation: "The labels 'opposite' and 'adjacent' are relative to a specific acute angle. The side opposite angle A is adjacent to angle B, and vice versa. When you switch which angle you are considering, the opposite and adjacent sides swap. Only the hypotenuse (opposite the right angle) stays fixed. This confusion is one of the most common errors in setting up trig ratios."

- question: "Why do trigonometric ratios like sin(θ) depend only on the angle θ and not on the size of the right triangle?"
  type: short-answer
  answer: "Any two right triangles with the same acute angle θ are similar by AA similarity. Because similar triangles have proportional sides, the ratio of any two specified sides (like opposite to hypotenuse) is the same in both triangles. The size cancels out, leaving a ratio that depends only on θ."
  explanation: "This is the key conceptual leap of the topic. Trigonometry would be useless if the ratios varied with triangle size — you would need a different table for every triangle. AA similarity guarantees they don't, which is why a single value of sin(30°) = 0.5 works for every right triangle with a 30° angle, regardless of scale."
```

## Explainer

The central question of this topic is: what can an angle tell you about the shape of a right triangle? You already know from similar triangles that two right triangles with the same acute angle must be similar — they have the same shape, just different sizes. And from your work with proportions in similar triangles, you know that when two triangles are similar, their corresponding side ratios are equal. These two facts together produce something remarkable: if you fix an acute angle, the ratio of any two sides of the right triangle is completely determined by that angle alone, regardless of how large or small the triangle is.

This is the insight that motivates defining the trigonometric ratios. For a given acute angle θ in a right triangle, we define three ratios based on which sides we compare. The side directly across from θ is called the **opposite** side. The side touching θ (that is not the hypotenuse) is called the **adjacent** side. The hypotenuse is always opposite the right angle. With these labels, sine is opposite over hypotenuse, cosine is adjacent over hypotenuse, and tangent is opposite over adjacent. The mnemonic SOHCAHTOA encodes all three.

A crucial subtlety: the labels "opposite" and "adjacent" are not fixed properties of the triangle's sides — they depend on which angle you are looking at. In a triangle with angles A, B, and the right angle, the side that is opposite A is adjacent to B. When you set up a trig ratio, always identify the reference angle first, then label the sides relative to it.

To build intuition, try this: draw three right triangles of different sizes, each with a 30° angle. Measure the hypotenuse and opposite side of each. Divide opposite by hypotenuse for each triangle. You will find the ratio is consistently about 0.5 — and that ratio is sin(30°). The calculator is not doing magic; it is storing the ratio that remains constant across all right triangles with that angle.

Right triangle trigonometry applies only when you have a right angle in your triangle. For triangles without a right angle, you will later need the law of sines and the law of cosines. For now, the right-angle constraint is essential — it is what allows you to define a unique hypotenuse and ensures the AA similarity argument holds.
