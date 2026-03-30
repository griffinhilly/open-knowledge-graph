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
stage: advanced
status: validated
---
# Machine Epsilon and Unit Roundoff

## Core Idea
Machine epsilon is the smallest positive number such that 1 + ε ≠ 1 in floating point arithmetic, quantifying the relative precision of a computer's number system. It determines the accuracy threshold for all numerical computations. For double-precision arithmetic, machine epsilon is approximately 2.22 × 10⁻¹⁶.

## Questions

```yaml
- question: "A programmer computes 1.0 + 1e-20 in double-precision floating point. What result does the computer return?"
  type: multiple-choice
  options:
    - "1.00000000000000000001 — the addition is stored exactly"
    - "1.0 — the added value is smaller than machine epsilon and is lost to rounding"
    - "A runtime overflow error — the result exceeds representable range"
    - "An indeterminate value — floating-point addition is non-deterministic"
  answer: 1
  explanation: "Machine epsilon (~2.22×10⁻¹⁶ for double precision) is the smallest ε such that 1+ε ≠ 1. Because 1e-20 is far smaller than ε, the floating-point representation of 1+1e-20 rounds back to exactly 1.0 — the tiny value is absorbed into the rounding of the significand. This is precisely what the definition of machine epsilon captures."

- question: "Double-precision machine epsilon is approximately 2.22×10⁻¹⁶. A stored number x has true value 10¹². What is the worst-case absolute rounding error when x is stored?"
  type: multiple-choice
  options:
    - "About 2.22×10⁻¹⁶ — machine epsilon is the absolute error bound"
    - "About 1.11×10⁻⁴ — the relative error bound ε/2 applied to the magnitude of x"
    - "Zero — large numbers are stored exactly in floating point"
    - "Unbounded — machine epsilon only applies near the value 1"
  answer: 1
  explanation: "Machine epsilon is a RELATIVE error bound, not absolute. The unit roundoff u = ε_mach/2 ≈ 1.11×10⁻¹⁶ means |fl(x) − x|/|x| ≤ u, so the absolute error for x ≈ 10¹² is at most u × 10¹² ≈ 1.11×10⁻⁴. A number like 10¹² is accurate to about 15 significant digits but the absolute error is much larger than ε_mach itself. Option A is the classic confusion: treating the relative bound as an absolute one."

- question: "Machine epsilon tells us that any real number stored in floating point differs from its true value by at most ε_mach in absolute terms."
  type: true-false
  answer: false
  explanation: "Machine epsilon is a RELATIVE error bound, not an absolute one. The guarantee is |fl(x) − x|/|x| ≤ ε_mach/2 — the error is proportional to the magnitude of x. For a very large number like 10¹⁵, the absolute rounding error can be on the order of 10⁻¹ (a tenth!), far larger than ε_mach ≈ 2.22×10⁻¹⁶. Confusing relative and absolute bounds leads to badly wrong estimates of numerical error."

- question: "In IEEE 754 double precision, the gap between 1.0 and the next representable floating-point number equals machine epsilon."
  type: true-false
  answer: true
  explanation: "This is the operational definition of machine epsilon: it is the spacing between 1.0 and the next representable double, which equals 2⁻⁵² ≈ 2.22×10⁻¹⁶. The significance of defining ε_mach near 1 (rather than near some other number) is that spacing between consecutive floating-point numbers scales with the magnitude of those numbers — near 1, the spacing equals ε_mach; near 2, the spacing is 2ε_mach; near 0.5, the spacing is ε_mach/2."

- question: "Why is machine epsilon described as a relative error bound rather than an absolute one, and why does this distinction matter for numerical computations involving very large or very small numbers?"
  type: short-answer
  answer: "Machine epsilon bounds the error as a fraction of the number's magnitude: |fl(x) − x|/|x| ≤ ε_mach/2. This means large numbers incur large absolute errors (though still tiny relative to their size), while small numbers incur tiny absolute errors. The distinction matters because: for x ≈ 10¹², the absolute error can be ~10⁻⁴, which is large in many applications; for x ≈ 10⁻¹², the absolute error is ~10⁻²⁸, negligible. Algorithms that subtract two nearly equal large numbers can suffer catastrophic cancellation — the relative error of the difference explodes even though each operand was stored accurately."
  explanation: "The relative nature of floating-point error is not just a technical detail — it fundamentally shapes which algorithms are trustworthy. Subtraction of nearly equal numbers (catastrophic cancellation) is dangerous precisely because the relative error on the individual numbers is fine but the relative error on their small difference is enormous. Understanding that ε_mach is a relative bound is the foundation for diagnosing numerical instability."
```

## Explainer

From your study of floating-point representation, you know that real numbers are stored in a finite binary format — a sign bit, an exponent, and a significand (mantissa). Because the significand has a fixed number of bits, there is a finite gap between any floating-point number and its nearest neighbors. **Machine epsilon** (often written ε_mach or u for **unit roundoff**) is a precise way to characterize this gap near the number 1.

The definition is operational: ε_mach is the smallest positive floating-point number ε such that the computer evaluates 1 + ε as strictly greater than 1. In IEEE 754 double precision (64-bit), the significand has 52 explicit bits plus one implicit leading bit, giving 53 bits of precision. The spacing between 1.0 and the next representable double is exactly 2⁻⁵² ≈ 2.22 × 10⁻¹⁶. This is machine epsilon. For single precision (32-bit, 24-bit significand), it is 2⁻²³ ≈ 1.19 × 10⁻⁷.

The practical meaning is a bound on **relative rounding error**. When you round any real number x to the nearest floating-point number fl(x), the relative error satisfies |fl(x) − x|/|x| ≤ u, where u = ε_mach/2 is the unit roundoff. This means every stored number is accurate to about 15–16 significant decimal digits in double precision. It does not mean absolute error is small — for a number like 10¹⁵, the absolute rounding error can be as large as 0.1. The relative nature of machine epsilon is the key point: precision degrades for very large or very small magnitudes only through accumulated operations, not from a single rounding.

Why does this matter for numerical algorithms? Because errors compound. If a computation requires many arithmetic steps, rounding errors accumulate, and machine epsilon sets the floor on what accuracy you can expect. An algorithm that amplifies rounding errors dramatically — one that is **numerically unstable** — can lose all significant digits even when machine epsilon is tiny. Conversely, a **backward-stable** algorithm guarantees that the computed result is the exact answer to a slightly perturbed problem, with the perturbation bounded in terms of machine epsilon. Understanding ε_mach is therefore the foundation for analyzing whether an algorithm should be trusted: it tells you not just the precision of individual numbers, but the scale of the errors you need to track through every operation.
