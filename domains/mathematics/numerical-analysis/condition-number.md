---
id: condition-number
title: Condition Number of a Problem
domain: mathematics
course: numerical-analysis
prerequisites:
- id: numerical-stability
  type: hard
- id: mean-value-theorem
  type: soft
builds-toward:
- condition-number-of-a-matrix
tags:
- condition-number
- conditioning
- sensitivity
stage: formal-systems
status: validated
---

# Condition Number of a Problem

## Core Idea
The condition number measures how much the solution changes relative to changes in input data. A large condition number indicates an ill-conditioned problem where small input perturbations cause large output changes. The relative condition number κ(x) = |x f'(x) / f(x)| quantifies this sensitivity for a general function f.

## Questions

```yaml
- question: "A numerical analyst uses a well-tested, numerically stable algorithm to compute ln(x) for x = 1.0001 and gets wildly inaccurate results. The most likely explanation is:"
  type: multiple-choice
  options:
    - "The algorithm has a bug in its floating-point arithmetic"
    - "The problem itself is ill-conditioned near x = 1: small relative errors in x cause enormous relative errors in ln(x)"
    - "The computer lacks sufficient floating-point precision for any logarithm computation"
    - "The algorithm should switch to double precision instead of single precision"
  answer: 1
  explanation: "Near x = 1, the condition number κ(x) = 1/|ln(x)| → ∞ as x → 1. This is a property of the mathematical problem, not the algorithm. Any algorithm — no matter how stable — must work with floating-point inputs that carry small relative errors, and the condition number tells you those errors will be amplified enormously. Switching precision or fixing the algorithm cannot rescue an ill-conditioned problem; the mathematics itself is sensitive."

- question: "For f(x) = √x at x = 4, the relative condition number is κ = |x·f′(x)/f(x)| = |4·(1/4)/2| = 0.5. What does this mean?"
  type: multiple-choice
  options:
    - "A 1% relative error in x produces approximately 0.5% relative error in √x — the problem is well-conditioned"
    - "The algorithm for √x amplifies errors by a factor of 0.5 at this point"
    - "√x is ill-conditioned at x = 4 because the condition number is less than 1"
    - "A 1% relative error in x produces approximately 2% relative error in √x"
  answer: 0
  explanation: "The condition number is an amplification factor for relative errors. κ = 0.5 means a relative input error of ε produces a relative output error of at most 0.5ε — errors actually shrink. This is a well-conditioned problem. Option D inverts the factor; option B misattributes conditioning to the algorithm rather than the problem."

- question: "Using a more numerically stable algorithm cannot reduce the output error below what the condition number predicts, given the precision of the input data."
  type: true-false
  answer: true
  explanation: "The condition number sets the fundamental lower bound on achievable accuracy for a given input precision. A stable algorithm approaches this bound — it doesn't introduce unnecessary extra error — but cannot beat it. Conditioning is a problem property; stability is an algorithm property. The best possible outcome from any algorithm is output error ≈ κ × (input error)."

- question: "An ill-conditioned problem means the algorithm used to solve it is numerically unstable."
  type: true-false
  answer: false
  explanation: "Conditioning describes the problem; stability describes the algorithm. They are independent properties. An ill-conditioned problem (large κ) will produce inaccurate results from any algorithm because tiny unavoidable floating-point input errors get amplified by κ — this has nothing to do with how the algorithm handles rounding internally. Conversely, a stable algorithm can solve a well-conditioned problem accurately, but no algorithm can fix an inherently ill-conditioned one."

- question: "Why can a more numerically stable algorithm not 'fix' an ill-conditioned problem, even in principle?"
  type: short-answer
  answer: "Because conditioning is a property of the mathematical problem, not the algorithm. The condition number quantifies how much relative error in the output is inherent for any given relative error in the input — it's a statement about the underlying mathematics. Floating-point inputs always carry small rounding errors, and the condition number says those errors will be amplified by a factor of κ regardless of how carefully the algorithm processes them. Stability only ensures an algorithm doesn't add *extra* amplification beyond what conditioning dictates; it cannot subtract the amplification the problem itself imposes."
  explanation: "The key conceptual move is separating problem sensitivity (conditioning) from algorithmic error propagation (stability). Once you accept that floating-point numbers always have small relative errors baked in, the condition number is the unavoidable tax those errors pay at the output. No computation can produce output more accurate than (input error) × κ for a problem with condition number κ."
```

## Explainer

From your study of numerical stability, you learned to distinguish between problems that are inherently sensitive and algorithms that introduce unnecessary error. The condition number makes the inherent sensitivity of a problem precise and quantitative. It answers: "If my input has a tiny relative error ε, how large a relative error should I expect in the output — before I've even chosen an algorithm?"

The formula κ(x) = |x f′(x) / f(x)| has a clear structure. The numerator |x f′(x)| captures how fast the output changes (via the derivative, connecting to the Mean Value Theorem you know), scaled by the size of the input x. The denominator |f(x)| normalizes by the output size. The result is dimensionless: a condition number of 100 means a relative input error of 0.01% can produce a relative output error of up to 1%. You can think of κ as an amplification factor for relative errors.

Concrete examples sharpen the intuition. Consider f(x) = √x near x = 1. Here κ(1) = |1 · (1/2) / 1| = 0.5 — well-conditioned; relative errors shrink by half. Now consider f(x) = ln(x) near x ≈ 1. Here f′(x) = 1/x, so κ(x) = |x · (1/x) / ln(x)| = 1/|ln(x)|. As x → 1, ln(x) → 0, so κ → ∞. Taking the logarithm of a number close to 1 is **ill-conditioned**: tiny relative errors in x produce enormous relative errors in ln(x). This is a property of the mathematical problem, not the algorithm.

A critical conceptual move: conditioning is a **problem property**, stability is an **algorithm property**. An ill-conditioned problem will give inaccurate answers no matter how careful you are — the underlying mathematics is sensitive, and floating-point inputs always carry small errors. A well-conditioned problem, however, can still be ruined by an unstable algorithm. The condition number sets the ceiling on achievable accuracy; stable algorithms approach that ceiling. When numerical results look wrong, diagnosing which of these two issues you have — is the problem ill-conditioned, or is the algorithm unstable? — determines whether better arithmetic or a better algorithm is the solution.
