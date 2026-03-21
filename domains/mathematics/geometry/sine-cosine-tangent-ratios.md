---
id: sine-cosine-tangent-ratios
title: Sine, Cosine, and Tangent Ratios
domain: mathematics
course: geometry
prerequisites:
- id: right-triangle-trigonometry-intro
  type: hard
builds-toward:
- special-right-triangles-30-60-90
- special-right-triangles-45-45-90
- trigonometric-ratios-review
tags:
- trigonometry
- sine
- cosine
- tangent
- SOHCAHTOA
stage: abstract-reasoning
status: validated
---
# Sine, Cosine, and Tangent Ratios

## Core Idea
For an acute angle A in a right triangle: sin(A) = opposite/hypotenuse, cos(A) = adjacent/hypotenuse, tan(A) = opposite/adjacent. These three ratios allow us to find unknown sides given an angle, or unknown angles given sides (using inverse trig). The mnemonic SOHCAHTOA encodes these definitions. Trig ratios are the bridge between angle measurement and distance measurement.

## How It's Best Learned
Define each ratio with clear labeled diagrams. Practice identifying opposite, adjacent, and hypotenuse relative to a specified angle. Solve for unknown sides (given an angle and one side) and unknown angles (given two sides, using inverse trig on a calculator). Mix problem types so students must decide which ratio to use.

## Common Misconceptions
- Swapping opposite and adjacent sides.
- Using the wrong ratio for the given information (e.g., using sine when tangent is appropriate).
- Forgetting that the hypotenuse is always the longest side and is opposite the right angle, never "opposite" or "adjacent" to an acute angle in the ratio sense.
- Confusing sin^(-1) (inverse sine, for finding angles) with 1/sin (cosecant).

## Questions

```yaml
- question: "In a right triangle with angle A = 40° and hypotenuse = 15 cm, which calculation correctly finds the side adjacent to angle A?"
  type: multiple-choice
  options:
    - "15 × sin(40°)"
    - "15 × cos(40°)"
    - "15 × tan(40°)"
    - "15 / tan(40°)"
  answer: 1
  explanation: "cos(A) = adjacent/hypotenuse, so adjacent = hypotenuse × cos(A) = 15 × cos(40°). Option A uses sine, which gives the opposite side (sin = opposite/hyp). Option C uses tangent (opposite/adjacent), which requires knowing a leg rather than the hypotenuse. Matching the ratio to the sides you know and want is the core skill."

- question: "In a right triangle, the side labeled 'opposite' when working from acute angle A becomes which of the following when working from the other acute angle B?"
  type: multiple-choice
  options:
    - "The hypotenuse"
    - "Still the opposite side — the label doesn't change"
    - "The adjacent side"
    - "It becomes undefined — you can only designate one reference angle at a time"
  answer: 2
  explanation: "The labels 'opposite' and 'adjacent' are not fixed properties of the sides — they shift depending on which angle is the reference. The side facing angle A is its 'opposite'; that same side runs along angle B toward the right angle, making it 'adjacent' for B. This is the most disorienting aspect of trig ratios and the source of most labeling errors. Always re-label after switching reference angles."

- question: "The hypotenuse appears as the denominator in both sine and cosine — regardless of which acute angle you choose as the reference angle."
  type: true-false
  answer: true
  explanation: "The hypotenuse is always opposite the right angle and is always the longest side. sin(A) = opposite/hypotenuse and cos(A) = adjacent/hypotenuse — both use the hypotenuse as the denominator. Tangent (opposite/adjacent) is the only ratio that never involves the hypotenuse. This is consistent no matter which acute angle you designate as A."

- question: "sin⁻¹(0.6) means the same thing as 1/sin(0.6)."
  type: true-false
  answer: false
  explanation: "sin⁻¹ is the inverse sine function — it takes a ratio and returns the angle whose sine equals that ratio. It does NOT mean the reciprocal. The reciprocal of sine is cosecant (csc). The superscript −1 denotes function inversion, not arithmetic reciprocal. Confusing these is a common mistake: sin⁻¹(0.6) ≈ 36.9°, while 1/sin(0.6) ≈ 1.77 (radians context) — completely different values."

- question: "In a right triangle where you know two sides but not the angle, describe the process for finding the missing angle using a trig ratio."
  type: short-answer
  answer: "Identify the two known sides relative to the desired angle, labeling them (opposite, adjacent, or hypotenuse). Compute the appropriate ratio: sin if you have opposite and hypotenuse, cos if adjacent and hypotenuse, tan if opposite and adjacent. Then apply the corresponding inverse function: angle = sin⁻¹(ratio), cos⁻¹(ratio), or tan⁻¹(ratio)."
  explanation: "The inverse function 'undoes' the trig ratio, converting a ratio back into an angle. For example, if opposite = 5 and hypotenuse = 10, then sin(A) = 0.5, so A = sin⁻¹(0.5) = 30°. The key is choosing which ratio links your two known sides — that determines which inverse function to apply."
```

## Explainer

Your earlier work on right-triangle trigonometry introduced the idea that the shape of a right triangle is entirely determined by its angles — specifically, once you fix an acute angle, all right triangles with that angle are similar, and similar triangles have proportional sides. **Sine, cosine, and tangent** are simply names for three particular ratios that describe this shape. They transform an angle into a ratio, and that ratio tells you how the sides of the triangle relate.

Every ratio is defined relative to a chosen **acute angle A**. Label the three sides: the **hypotenuse** is always opposite the right angle and is the longest side; the **opposite** side is across from angle A; the **adjacent** side runs along angle A toward the right angle. With those labels in place: **sin(A) = opposite/hypotenuse**, **cos(A) = adjacent/hypotenuse**, and **tan(A) = opposite/adjacent**. The mnemonic **SOHCAHTOA** encodes these three definitions. The hypotenuse always appears in sine and cosine (as denominator) and never in tangent — tangent is purely the ratio of the two legs.

These ratios let you solve two types of problems. In the first type, you know an angle and one side, and you want a different side. You set up the ratio that links the known side to the unknown side, then solve algebraically. For example: angle A = 35°, hypotenuse = 10, find the opposite side. Since sin(35°) = opposite/10, the opposite side = 10 × sin(35°) ≈ 5.74. In the second type, you know two sides and want the angle. You compute the ratio, then apply an **inverse trig function**: if sin(A) = 0.574, then A = sin⁻¹(0.574) ≈ 35°. The inverse functions "undo" sine, cosine, and tangent, converting a ratio back into an angle.

The labels "opposite" and "adjacent" shift depending on which angle you call A. This is the most disorienting thing about the ratios, and the source of most errors. If you are given a triangle and you switch your focus from angle A to the other acute angle B, what was the "opposite" side for A becomes the "adjacent" side for B. Always start a problem by clearly marking which angle is your reference angle, and re-labeling the sides accordingly.

Trig ratios are the bridge between angles and distances. Surveyors use them to find heights of inaccessible objects. Engineers use them to resolve forces into components. Navigators use them to convert bearing and distance into north-south and east-west displacement. In every case, the logic is the same: a known angle and a known distance, combined through a trig ratio, yield an unknown distance or direction. Mastering the three ratios and knowing when to use each one equips you for special right triangles, the unit circle, and eventually the full sweep of trigonometric functions.
