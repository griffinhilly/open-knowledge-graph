---
id: richardson-extrapolation
title: Richardson Extrapolation
domain: mathematics
course: numerical-analysis
prerequisites:
- id: numerical-differentiation
  type: hard
builds-toward:
- romberg-integration
tags:
- extrapolation
- acceleration
- richardson
stage: advanced
status: validated
---
# Richardson Extrapolation

## Core Idea
Richardson extrapolation combines numerical estimates at different step sizes to cancel leading-order error terms. If an estimate has error c₁h + c₂h² + ..., combining results at h and h/2 eliminates the O(h) term. This acceleration technique generalizes to any problem with known asymptotic error expansions and is the foundation for Romberg integration.

## Questions

```yaml
- question: "A numerical method produces estimates A(h) = I + c₁h + c₂h² + ··· You compute A(h) and A(h/2). What does the Richardson extrapolation formula 2A(h/2) − A(h) produce, and why?"
  type: multiple-choice
  options:
    - "An average of the two estimates, which reduces random numerical noise"
    - "An estimate with error starting at O(h²) instead of O(h), because the O(h) terms cancel exactly"
    - "The exact value I, because combining two estimates eliminates all error"
    - "An estimate with error starting at O(h/2), because we used the smaller step size"
  answer: 1
  explanation: "Richardson extrapolation cancels the leading error term algebraically. A(h/2) = I + (c₁/2)h + (c₂/4)h² + ···. Multiply by 2: 2A(h/2) = 2I + c₁h + (c₂/2)h² + ···. Subtract A(h) = I + c₁h + c₂h² + ···: result = I + 0·h + (c₂/2 − c₂)h² + ··· = I − (c₂/2)h² + ···. The O(h) term cancels exactly; accuracy improves by a full order. This is not averaging — different coefficients are required, and averaging (weighting both estimates by 1/2) would not cancel the linear term."

- question: "For Richardson extrapolation to dramatically improve accuracy, what must be known about the method being used?"
  type: multiple-choice
  options:
    - "The exact value of the true answer I, so that errors can be measured and corrected"
    - "The structure of the error expansion — specifically, that it takes the form c₁h^p + c₂h^q + ··· with known exponents"
    - "The values of the error coefficients c₁, c₂, … so the cancellation formula can be derived"
    - "That the step size h is already below machine epsilon, ensuring floating-point arithmetic is exact"
  answer: 1
  explanation: "You need to know the *form* of the error expansion — the powers of h that appear — not the coefficients themselves. For a method with error c₁h + c₂h² + ···, the cancellation weights (2 and −1 in 2A(h/2) − A(h)) are determined entirely by the exponent p = 1. For centered differences with error c₂h² + c₄h⁴ + ··· (only even powers), different weights cancel the O(h²) term. If the error expansion is unknown or irregular (e.g., due to singularities), Richardson extrapolation cannot be applied reliably — the unknown powers mean you don't know which linear combination to form."

- question: "Richardson extrapolation improves accuracy by using results already computed at two step sizes, requiring no additional function evaluations beyond those two estimates."
  type: true-false
  answer: true
  explanation: "This is the key practical advantage: Richardson extrapolation is 'free' in the sense that once you have A(h) and A(h/2), the improved estimate 2A(h/2) − A(h) requires only arithmetic, no new function evaluations. Compare this to the naive approach of simply using a smaller step size h/2 — that achieves the same O(h²) error but at the cost of recomputing the estimate from scratch. Richardson extrapolation recycles existing work and extracts higher accuracy from it."

- question: "Richardson extrapolation works by averaging two numerical estimates, giving each estimate equal weight of 1/2."
  type: true-false
  answer: false
  explanation: "Richardson extrapolation uses deliberately unequal weights chosen to cancel the leading error term, not to average. For a method with O(h) error, the formula is 2A(h/2) − 1·A(h): weights +2 and −1. Simple averaging would give (A(h) + A(h/2))/2 = I + (3c₁/4)h + ···, which does not cancel the O(h) term at all. The specific weights are derived algebraically from the requirement that the coefficient of h in the combined estimate equals zero. Different error structures require different weights."

- question: "Why does Richardson extrapolation fail or behave unpredictably when applied to a method whose error expansion contains a logarithmic term (e.g., error ~ c₁h ln h + c₂h²) rather than a pure power series in h?"
  type: short-answer
  answer: "Richardson extrapolation is designed to cancel specific powers of h. The standard formula 2A(h/2) − A(h) is derived assuming error terms proportional to h^p for integer p. If the error contains h ln h, replacing h with h/2 gives (h/2)ln(h/2) = (h/2)(ln h − ln 2), which does not scale simply as a half-integer power of h. The resulting combination 2A(h/2) − A(h) no longer cancels the leading error — the logarithmic term survives in modified form. Richardson extrapolation requires a clean polynomial error expansion in h to work; irregular or logarithmic error structures break the algebraic cancellation."
  explanation: "The deeper point: Richardson extrapolation exploits the *structure* of errors, not just their magnitude. When you know errors are pure powers of h, you can engineer their cancellation. When error structure is complicated by logs, fractional powers, or singularities, the method's assumptions fail and you may actually worsen accuracy by combining estimates with the wrong weights."
```

## Explainer

From numerical differentiation, you know that approximations like the centered difference (f(x+h) - f(x-h))/(2h) have errors that shrink with h. But taking h smaller has a cost: when h is very small, floating-point cancellation makes the numerator inaccurate. Richardson extrapolation offers a smarter route: compute two estimates at different step sizes and combine them algebraically to cancel the dominant error term — improving accuracy without pushing h toward machine precision.

Here is the key insight. Suppose your method produces an estimate A(h) with asymptotic error expansion A(h) = I + c₁h + c₂h² + ···, where I is the true value and c₁, c₂ are unknown constants. Now compute A(h/2) = I + c₁(h/2) + c₂(h/2)² + ··· = I + (c₁/2)h + (c₂/4)h² + ···. Multiply this equation by 2 and subtract the first: 2A(h/2) - A(h) = I + (terms in h² and higher). The O(h) term **cancels exactly**, producing a new estimate with error starting at O(h²). You have gained a full order of accuracy using only two evaluations already in hand — no new function calls required.

The technique applies repeatedly. If the original method has error c₂h² + c₄h⁴ + ··· (as with centered differences, which only have even powers in the expansion), a single Richardson step produces error O(h⁴). Apply the same combination to two O(h⁴) estimates at different spacings to get O(h⁶), and so on. This bootstrapping produces what is called a **Richardson table**: a triangular array where each column is one application of the cancellation formula applied to the previous column. The diagonal entries converge very rapidly.

This is the foundation of **Romberg integration**. Start with the trapezoidal rule for ∫f(x)dx, which has an error expansion in even powers of h (a result called the Euler-Maclaurin formula). Compute the trapezoidal sum at step sizes h, h/2, h/4, ···, then build the Richardson table column by column. The bottom-right entry of the table is an extremely accurate estimate of the integral — often matching hundreds of trapezoidal evaluations with just a handful. The prerequisite that makes this work is knowing the structure of the error expansion. Problems with clean polynomial error expansions respond dramatically to Richardson; problems with singularities or irregular error behavior respond less predictably.
