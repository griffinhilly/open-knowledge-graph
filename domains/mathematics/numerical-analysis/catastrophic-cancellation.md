---
id: catastrophic-cancellation
title: Catastrophic Cancellation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: rounding-errors
  type: hard
builds-toward:
- numerical-stability
tags:
- cancellation
- subtraction
- error-amplification
stage: formal-systems
status: draft
---

# Catastrophic Cancellation

## Core Idea
Catastrophic cancellation occurs when subtracting two nearly equal floating point numbers, losing most significant digits in the result. A relative error of 10⁻¹⁶ in the inputs can become an error of magnitude 1 in the output. Recognizing and avoiding this phenomenon through algebraic reformulation is critical for stable algorithms.

## How It's Best Learned
Compute examples like √(x²+1) - √(x²) for large x using direct and rationalized forms to see the difference in accuracy.

## Common Misconceptions
- Thinking all subtraction loses precision equally; only nearly-equal magnitudes cause catastrophic cancellation.
- Assuming higher precision (using doubles instead of floats) solves all cancellation problems; reformulation is often necessary.

## Explainer

From your study of **rounding errors**, you know that floating-point numbers are stored with a fixed number of significant digits — roughly 15–16 decimal digits for IEEE 754 double precision. Each number carries a tiny relative error: a stored value x̂ satisfies x̂ = x(1 + ε) where |ε| ≤ machine epsilon ≈ 10⁻¹⁶. This small relative error is usually harmless. Catastrophic cancellation is what happens when subtraction destroys this safety.

Consider computing a = 1.000000000000001 and b = 1.000000000000000 in double precision. Each is accurate to 15 significant digits. Their difference a − b should be 10⁻¹⁵, but in a 64-bit float both values may round to exactly the same stored representation, yielding a − b = 0 — a relative error of 100%. More generally, when two numbers agree to k significant digits, their difference has at most (15 − k) significant digits of accuracy. If they agree to 14 digits, the difference has only 1 significant digit. This is **catastrophic cancellation**: the leading significant digits cancel away, leaving a result dominated by rounding noise from both operands.

The classic example is the quadratic formula. For large c/a, the roots x = (−b ± √(b² − 4ac)) / (2a) involve adding and subtracting nearly equal quantities when b² ≫ 4ac. Concretely, take b = 10⁸ and b² − 4ac = 1: then √(b² − 4ac) ≈ 10⁸ as well, and computing −b + √(b² − 4ac) subtracts two numbers that agree to 8 digits, leaving only ~7 digits of accuracy in a result that should be close to zero. The fix: use the **rationalized form** x = −2c / (b + √(b² − 4ac)) for the small root, which avoids the cancellation entirely by multiplying and dividing rather than subtracting near-equal terms.

The general strategy is **algebraic reformulation**: rewrite expressions to avoid subtraction of near-equal quantities before evaluation. Common techniques include multiplying and dividing by the conjugate (for expressions like √(x + h) − √x), using Taylor expansions for quantities where direct subtraction is near zero (e.g., e^x − 1 near x = 0 should use the built-in `expm1` function), or using compensated summation algorithms like Kahan summation for summing many small terms. Switching from float to double helps by pushing the danger threshold further away, but it cannot fix a structurally cancellation-prone formula — only reformulation can.
