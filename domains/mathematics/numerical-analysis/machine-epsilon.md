---
id: machine-epsilon
title: Machine Epsilon and Unit Roundoff
domain: mathematics
course: numerical-analysis
prerequisites:
- id: floating-point-representation
  type: hard
builds-toward:
- rounding-errors
- numerical-stability
tags:
- machine-epsilon
- precision
- floating-point
stage: formal-systems
status: draft
---

# Machine Epsilon and Unit Roundoff

## Core Idea
Machine epsilon is the smallest positive number such that 1 + ε ≠ 1 in floating point arithmetic, quantifying the relative precision of a computer's number system. It determines the accuracy threshold for all numerical computations. For double-precision arithmetic, machine epsilon is approximately 2.22 × 10⁻¹⁶.

## Explainer

From your study of floating-point representation, you know that real numbers are stored in a finite binary format — a sign bit, an exponent, and a significand (mantissa). Because the significand has a fixed number of bits, there is a finite gap between any floating-point number and its nearest neighbors. **Machine epsilon** (often written ε_mach or u for **unit roundoff**) is a precise way to characterize this gap near the number 1.

The definition is operational: ε_mach is the smallest positive floating-point number ε such that the computer evaluates 1 + ε as strictly greater than 1. In IEEE 754 double precision (64-bit), the significand has 52 explicit bits plus one implicit leading bit, giving 53 bits of precision. The spacing between 1.0 and the next representable double is exactly 2⁻⁵² ≈ 2.22 × 10⁻¹⁶. This is machine epsilon. For single precision (32-bit, 24-bit significand), it is 2⁻²³ ≈ 1.19 × 10⁻⁷.

The practical meaning is a bound on **relative rounding error**. When you round any real number x to the nearest floating-point number fl(x), the relative error satisfies |fl(x) − x|/|x| ≤ u, where u = ε_mach/2 is the unit roundoff. This means every stored number is accurate to about 15–16 significant decimal digits in double precision. It does not mean absolute error is small — for a number like 10¹⁵, the absolute rounding error can be as large as 0.1. The relative nature of machine epsilon is the key point: precision degrades for very large or very small magnitudes only through accumulated operations, not from a single rounding.

Why does this matter for numerical algorithms? Because errors compound. If a computation requires many arithmetic steps, rounding errors accumulate, and machine epsilon sets the floor on what accuracy you can expect. An algorithm that amplifies rounding errors dramatically — one that is **numerically unstable** — can lose all significant digits even when machine epsilon is tiny. Conversely, a **backward-stable** algorithm guarantees that the computed result is the exact answer to a slightly perturbed problem, with the perturbation bounded in terms of machine epsilon. Understanding ε_mach is therefore the foundation for analyzing whether an algorithm should be trusted: it tells you not just the precision of individual numbers, but the scale of the errors you need to track through every operation.
