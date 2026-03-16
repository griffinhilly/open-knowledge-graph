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

## Explainer

Your earlier work on right-triangle trigonometry introduced the idea that the shape of a right triangle is entirely determined by its angles — specifically, once you fix an acute angle, all right triangles with that angle are similar, and similar triangles have proportional sides. **Sine, cosine, and tangent** are simply names for three particular ratios that describe this shape. They transform an angle into a ratio, and that ratio tells you how the sides of the triangle relate.

Every ratio is defined relative to a chosen **acute angle A**. Label the three sides: the **hypotenuse** is always opposite the right angle and is the longest side; the **opposite** side is across from angle A; the **adjacent** side runs along angle A toward the right angle. With those labels in place: **sin(A) = opposite/hypotenuse**, **cos(A) = adjacent/hypotenuse**, and **tan(A) = opposite/adjacent**. The mnemonic **SOHCAHTOA** encodes these three definitions. The hypotenuse always appears in sine and cosine (as denominator) and never in tangent — tangent is purely the ratio of the two legs.

These ratios let you solve two types of problems. In the first type, you know an angle and one side, and you want a different side. You set up the ratio that links the known side to the unknown side, then solve algebraically. For example: angle A = 35°, hypotenuse = 10, find the opposite side. Since sin(35°) = opposite/10, the opposite side = 10 × sin(35°) ≈ 5.74. In the second type, you know two sides and want the angle. You compute the ratio, then apply an **inverse trig function**: if sin(A) = 0.574, then A = sin⁻¹(0.574) ≈ 35°. The inverse functions "undo" sine, cosine, and tangent, converting a ratio back into an angle.

The labels "opposite" and "adjacent" shift depending on which angle you call A. This is the most disorienting thing about the ratios, and the source of most errors. If you are given a triangle and you switch your focus from angle A to the other acute angle B, what was the "opposite" side for A becomes the "adjacent" side for B. Always start a problem by clearly marking which angle is your reference angle, and re-labeling the sides accordingly.

Trig ratios are the bridge between angles and distances. Surveyors use them to find heights of inaccessible objects. Engineers use them to resolve forces into components. Navigators use them to convert bearing and distance into north-south and east-west displacement. In every case, the logic is the same: a known angle and a known distance, combined through a trig ratio, yield an unknown distance or direction. Mastering the three ratios and knowing when to use each one equips you for special right triangles, the unit circle, and eventually the full sweep of trigonometric functions.
