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
stage: formal-systems
status: draft
---

# Machine Epsilon and Rounding Errors

## Core Idea
Machine epsilon is the smallest positive number ε such that 1 + ε ≠ 1 in floating point arithmetic, quantifying the relative error in number representation. It characterizes the precision limit of the floating point system and allows us to estimate rounding errors in arithmetic operations. Understanding machine epsilon enables prediction and control of accumulated errors in numerical computations.

## Questions

```yaml
- question: "In IEEE 754 double precision, you compute (1.0 + 1e-20) − 1.0. What is the result?"
  type: multiple-choice
  options:
    - "1e-20, because the subtraction recovers the small value"
    - "0.0, because 1e-20 is smaller than machine epsilon so 1.0 + 1e-20 rounds to 1.0"
    - "machine epsilon (≈ 2.22 × 10⁻¹⁶), the smallest detectable difference from 1"
    - "A negative value due to underflow"
  answer: 1
  explanation: "Machine epsilon (≈ 2.22 × 10⁻¹⁶) is the smallest ε such that 1 + ε ≠ 1 in double precision. Since 1e-20 < machine epsilon, the addition 1.0 + 1e-20 rounds back to 1.0, and the subtraction gives exactly 0.0. This is the essence of machine epsilon as a precision floor: values below it are invisible when added to 1."

- question: "What does machine epsilon bound for a floating-point number x?"
  type: multiple-choice
  options:
    - "The absolute error |fl(x) − x| in representing x"
    - "The relative error |fl(x) − x| / |x| in representing x"
    - "The error introduced by a single arithmetic operation"
    - "The gap to the nearest representable number below x"
  answer: 1
  explanation: "Machine epsilon bounds the *relative* rounding error: |fl(x) − x| / |x| ≤ εₘ/2. This is what makes floating-point precision scale-invariant — you get roughly the same number of significant digits for very large and very small numbers alike. Absolute error would be scale-dependent and therefore uninformative across orders of magnitude."

- question: "A real number x is stored in double precision. The relative rounding error |fl(x) − x| / |x| is bounded by machine epsilon regardless of the magnitude of x."
  type: true-false
  answer: true
  explanation: "This is the key property of floating-point representation: |fl(x) − x| / |x| ≤ εₘ/2, where εₘ ≈ 2.22 × 10⁻¹⁶ for double precision. The relative error bound holds for any nonzero x, which is why floating-point is useful across wildly different scales — the precision (in significant digits) is approximately constant."

- question: "Catastrophic cancellation occurs when subtracting two large numbers, and machine epsilon gives no warning that the result may be inaccurate."
  type: true-false
  answer: false
  explanation: "Catastrophic cancellation happens when subtracting two *nearly equal* numbers, not necessarily large ones. Machine epsilon does give a precise warning: if the result of a subtraction is much smaller in magnitude than the operands, relative error amplification is occurring. The result may have few or no correct significant digits. Machine epsilon defines exactly where this danger zone begins — it is the tool that lets you recognize when reformulation is necessary."

- question: "Why is relative rounding error the appropriate measure for floating-point precision rather than absolute error?"
  type: short-answer
  answer: "Relative error measures how many significant digits are correct, independent of the number's scale. Since floating-point represents numbers as mantissa × 2^exponent, the same number of significant bits applies whether computing 0.000001 or 10^20. Absolute error would be scale-dependent: a number like 10^10 with absolute error 10^{-6} has 16 correct figures, while 10^{-10} with the same absolute error has none."
  explanation: "The design goal of floating-point is uniform precision across scales: roughly 15–16 significant decimal digits in double precision regardless of magnitude. Only relative error captures this goal. Absolute error is meaningless as a universal bound because it depends on the number's size. Machine epsilon formalizes this by bounding relative error, making it the natural unit of floating-point precision."
```

## Explainer

From your study of floating-point representation, you know that a number like 0.1 cannot be stored exactly in binary — it becomes a nearest representable value. **Machine epsilon** (εₘ) makes this imprecision precise: it is the gap between 1 and the next representable floating-point number above 1, or equivalently, the smallest ε such that the computer distinguishes 1 + ε from 1. For IEEE 754 double precision (64-bit), εₘ ≈ 2.22 × 10⁻¹⁶. For single precision (32-bit), εₘ ≈ 1.19 × 10⁻⁷.

The key property of εₘ is that it bounds **relative rounding error**: when you round a real number x to the nearest floating-point value fl(x), you have |fl(x) − x| / |x| ≤ εₘ/2. This says the relative error in representing any number is at most half a machine epsilon — no matter how large or small x is. This is what makes floating-point arithmetic useful: the precision scales with the magnitude of the number, so you get roughly the same number of significant digits everywhere. Absolute error, by contrast, would be uninformative since it depends on scale.

The danger comes when you combine operations. Each arithmetic step introduces a new rounding error of at most εₘ/2 in relative terms, and errors **accumulate** as you perform many operations in sequence. If you sum n numbers naively, the accumulated error can be O(n · εₘ) times the result. This is usually fine for small n, but in algorithms that perform millions of floating-point operations (like large matrix factorizations or iterative solvers), error budgets must be tracked carefully. Understanding εₘ lets you reason about whether accumulated errors are acceptable for your application's precision requirements.

A particularly important failure mode is **catastrophic cancellation**: when you subtract two nearly equal floating-point numbers, the result may have very few correct significant digits. For example, if x = 1.000000000000001 and y = 1.000000000000000, both representable to 16 digits, their difference x − y should be 10⁻¹⁵ but in practice will be dominated by rounding error. Machine epsilon tells you exactly where this danger zone begins — whenever your computation produces a result much smaller than the inputs, relative error amplification occurs. Recognizing this allows you to reformulate the computation (completing the square, using Taylor expansions near zero, etc.) to avoid the cancellation entirely.
