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
stage: advanced
status: validated
---

# Catastrophic Cancellation

## Core Idea
Catastrophic cancellation occurs when subtracting two nearly equal floating point numbers, losing most significant digits in the result. A relative error of 10⁻¹⁶ in the inputs can become an error of magnitude 1 in the output. Recognizing and avoiding this phenomenon through algebraic reformulation is critical for stable algorithms.

## How It's Best Learned
Compute examples like √(x²+1) - √(x²) for large x using direct and rationalized forms to see the difference in accuracy.

## Common Misconceptions
- Thinking all subtraction loses precision equally; only nearly-equal magnitudes cause catastrophic cancellation.
- Assuming higher precision (using doubles instead of floats) solves all cancellation problems; reformulation is often necessary.

## Questions

```yaml
- question: "Two floating-point numbers agree to their first 13 significant digits. You subtract them using a 15-significant-digit system. Approximately how many significant digits of accuracy does the result have?"
  type: multiple-choice
  options:
    - "15 digits — subtraction does not affect the precision of either operand"
    - "13 digits — precision is preserved because both inputs were accurate to 13 digits"
    - "About 2 digits — the 13 shared leading digits cancel, leaving only the residual accuracy"
    - "Zero digits — the result is always exactly zero when numbers agree to this many digits"
  answer: 2
  explanation: "When two numbers agree to k significant digits, their difference has at most (15 − k) significant digits. Agreeing to 13 digits leaves only about 2 significant digits in the result. The leading 13 digits cancel away; what remains is dominated by rounding noise in both operands. Option D overstates the case — the numbers agree to 13 digits but not all 15, so the result is small but nonzero, just nearly all noise."

- question: "You need to compute √(x² + 1) − √(x²) for x = 10⁷. The direct formula gives a result with almost no significant digits. What is the better approach?"
  type: multiple-choice
  options:
    - "Use 128-bit floats to get more significant digits in the inputs"
    - "Multiply and divide by the conjugate, rewriting as 1 / (√(x²+1) + √(x²))"
    - "Round both square roots to fewer digits before subtracting to reduce cancellation"
    - "Compute the two square roots separately and store them in distinct variables before subtracting"
  answer: 1
  explanation: "The conjugate reformulation avoids subtracting nearly-equal quantities entirely. The algebraically equivalent form 1 / (√(x²+1) + √(x²)) involves only addition in the denominator, which is numerically stable. Option A (higher precision) only shifts the danger threshold — for x = 10⁷, the operands agree to 7 digits, well within even double precision's range of cancellation. Options C and D change nothing about the structural cancellation problem."

- question: "Catastrophic cancellation can be eliminated by switching from 32-bit (single) to 64-bit (double) precision arithmetic."
  type: true-false
  answer: false
  explanation: "Higher precision reduces the relative error in each operand but cannot prevent those errors from dominating when the correct answer is much smaller than either operand. For the quadratic formula with b = 10⁸, cancellation occurs because operands agree to 8 digits — well within double precision's 15-digit range. Only algebraic reformulation changes the structure of the computation; higher precision only postpones the problem."

- question: "Catastrophic cancellation can occur when two nearly equal floating-point numbers are added if they have opposite signs."
  type: true-false
  answer: true
  explanation: "Adding numbers of opposite sign is equivalent to subtraction. If x = 1.000000000001 and y = −1.000000000000, then x + y involves the same near-cancellation as computing x − (−y) explicitly. The relevant criterion is whether the operands are nearly equal in magnitude and opposite in sign, not whether the operation is syntactically addition or subtraction. The sign and the magnitude together determine whether catastrophic cancellation occurs."

- question: "Why does algebraic reformulation fix catastrophic cancellation when simply using higher precision does not?"
  type: short-answer
  answer: "Higher precision reduces the relative error in each operand but cannot prevent those errors from dominating the result when the correct answer is orders of magnitude smaller than either operand. Reformulation restructures the computation so the cancellation-prone subtraction never occurs — you compute the same mathematical value via a different arithmetic path that avoids subtracting nearly-equal quantities. The problem is structural (the formula's shape and condition number), not representational (how many digits are used)."
  explanation: "The quadratic formula example makes this concrete: using the conjugate form x = −2c / (b + √(b²−4ac)) for the small root avoids the cancellation regardless of precision, because the denominator involves addition rather than subtraction of nearly-equal terms. No amount of extra precision fixes a formula that is structurally ill-conditioned; only reformulation changes the condition number of the computation itself."
```

## Explainer

From your study of **rounding errors**, you know that floating-point numbers are stored with a fixed number of significant digits — roughly 15–16 decimal digits for IEEE 754 double precision. Each number carries a tiny relative error: a stored value x̂ satisfies x̂ = x(1 + ε) where |ε| ≤ machine epsilon ≈ 10⁻¹⁶. This small relative error is usually harmless. Catastrophic cancellation is what happens when subtraction destroys this safety.

Consider computing a = 1.000000000000001 and b = 1.000000000000000 in double precision. Each is accurate to 15 significant digits. Their difference a − b should be 10⁻¹⁵, but in a 64-bit float both values may round to exactly the same stored representation, yielding a − b = 0 — a relative error of 100%. More generally, when two numbers agree to k significant digits, their difference has at most (15 − k) significant digits of accuracy. If they agree to 14 digits, the difference has only 1 significant digit. This is **catastrophic cancellation**: the leading significant digits cancel away, leaving a result dominated by rounding noise from both operands.

The classic example is the quadratic formula. For large c/a, the roots x = (−b ± √(b² − 4ac)) / (2a) involve adding and subtracting nearly equal quantities when b² ≫ 4ac. Concretely, take b = 10⁸ and b² − 4ac = 1: then √(b² − 4ac) ≈ 10⁸ as well, and computing −b + √(b² − 4ac) subtracts two numbers that agree to 8 digits, leaving only ~7 digits of accuracy in a result that should be close to zero. The fix: use the **rationalized form** x = −2c / (b + √(b² − 4ac)) for the small root, which avoids the cancellation entirely by multiplying and dividing rather than subtracting near-equal terms.

The general strategy is **algebraic reformulation**: rewrite expressions to avoid subtraction of near-equal quantities before evaluation. Common techniques include multiplying and dividing by the conjugate (for expressions like √(x + h) − √x), using Taylor expansions for quantities where direct subtraction is near zero (e.g., e^x − 1 near x = 0 should use the built-in `expm1` function), or using compensated summation algorithms like Kahan summation for summing many small terms. Switching from float to double helps by pushing the danger threshold further away, but it cannot fix a structurally cancellation-prone formula — only reformulation can.
