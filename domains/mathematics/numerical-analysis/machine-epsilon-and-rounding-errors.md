---
id: machine-epsilon-and-rounding-errors
title: Machine Epsilon and Rounding Errors
domain: mathematics
course: numerical-analysis
prerequisites:
- id: floating-point-representation
  type: hard
builds-toward:
- catastrophic-cancellation
- numerical-stability-and-conditioning
tags:
- machine-epsilon
- rounding
- error-analysis
stage: advanced
status: draft
---

# Machine Epsilon and Rounding Errors

## Core Idea
Machine epsilon is the smallest positive number ε such that 1 + ε ≠ 1 in floating point arithmetic, quantifying the relative error in number representation. It characterizes the precision limit of the floating point system and allows us to estimate rounding errors in arithmetic operations. Understanding machine epsilon enables prediction and control of accumulated errors in numerical computations.

## Explainer

From your study of floating-point representation, you know that a number like 0.1 cannot be stored exactly in binary — it becomes a nearest representable value. **Machine epsilon** (εₘ) makes this imprecision precise: it is the gap between 1 and the next representable floating-point number above 1, or equivalently, the smallest ε such that the computer distinguishes 1 + ε from 1. For IEEE 754 double precision (64-bit), εₘ ≈ 2.22 × 10⁻¹⁶. For single precision (32-bit), εₘ ≈ 1.19 × 10⁻⁷.

The key property of εₘ is that it bounds **relative rounding error**: when you round a real number x to the nearest floating-point value fl(x), you have |fl(x) − x| / |x| ≤ εₘ/2. This says the relative error in representing any number is at most half a machine epsilon — no matter how large or small x is. This is what makes floating-point arithmetic useful: the precision scales with the magnitude of the number, so you get roughly the same number of significant digits everywhere. Absolute error, by contrast, would be uninformative since it depends on scale.

The danger comes when you combine operations. Each arithmetic step introduces a new rounding error of at most εₘ/2 in relative terms, and errors **accumulate** as you perform many operations in sequence. If you sum n numbers naively, the accumulated error can be O(n · εₘ) times the result. This is usually fine for small n, but in algorithms that perform millions of floating-point operations (like large matrix factorizations or iterative solvers), error budgets must be tracked carefully. Understanding εₘ lets you reason about whether accumulated errors are acceptable for your application's precision requirements.

A particularly important failure mode is **catastrophic cancellation**: when you subtract two nearly equal floating-point numbers, the result may have very few correct significant digits. For example, if x = 1.000000000000001 and y = 1.000000000000000, both representable to 16 digits, their difference x − y should be 10⁻¹⁵ but in practice will be dominated by rounding error. Machine epsilon tells you exactly where this danger zone begins — whenever your computation produces a result much smaller than the inputs, relative error amplification occurs. Recognizing this allows you to reformulate the computation (completing the square, using Taylor expansions near zero, etc.) to avoid the cancellation entirely.
