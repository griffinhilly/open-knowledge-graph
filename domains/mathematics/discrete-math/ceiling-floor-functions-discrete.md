---
id: ceiling-floor-functions-discrete
title: Ceiling and Floor Functions
domain: mathematics
course: discrete-math
prerequisites:
- id: absolute-value
  type: soft
builds-toward:
- counting-principles
tags:
- discrete-math
- functions
- notation
stage: formal-systems
status: draft
---

# Ceiling and Floor Functions

## Core Idea
The floor function ⌊x⌋ returns the greatest integer ≤ x, while the ceiling function ⌈x⌉ returns the least integer ≥ x. These functions are essential in discrete mathematics for rounding, analyzing algorithms, and counting problems where integer solutions are required.

## Explainer

The real number line is continuous — there are infinitely many values between any two integers. But discrete mathematics lives in the world of whole numbers. The **floor function** ⌊x⌋ and **ceiling function** ⌈x⌉ are the bridge between these two worlds: they take any real number and snap it to the nearest integer in a well-defined direction.

Think of floor as "round down, always." ⌊3.7⌋ = 3, ⌊−1.2⌋ = −2 (because −2 is the greatest integer *less than or equal to* −1.2 — note that for negative numbers, rounding down means going further from zero). Ceiling is "round up, always": ⌈3.2⌉ = 4, ⌈−1.7⌉ = −1. When x is exactly an integer, both functions return x itself: ⌊5⌋ = ⌈5⌉ = 5. This is important to internalize before working with them algebraically.

You already know **absolute value** snaps a number onto the non-negative half of the real line. Floor and ceiling are a different kind of snapping: they project onto the integers. Their power shows up in counting arguments. Suppose you have n items and want to divide them into groups of k — the number of complete groups is ⌊n/k⌋, and the number of groups needed if you can't split items is ⌈n/k⌉. This distinction is ubiquitous in algorithm analysis: if you're dividing an array of 100 elements in half repeatedly, after log₂(100) ≈ 6.64 steps you need ⌈log₂(100)⌉ = 7 actual levels.

Two useful identities to internalize: ⌊x⌋ ≤ x < ⌊x⌋ + 1, and ⌈x⌉ − 1 < x ≤ ⌈x⌉. These bounds let you convert floor/ceiling expressions into inequalities, which is how they appear in proofs. Also note that ⌈x⌉ = ⌊x⌋ + 1 when x is not an integer, and ⌈x⌉ = ⌊x⌋ when x is an integer. The relationship between the two is: ⌈x⌉ = −⌊−x⌋. This symmetry can simplify problems that initially seem to require separate cases for floor and ceiling.
