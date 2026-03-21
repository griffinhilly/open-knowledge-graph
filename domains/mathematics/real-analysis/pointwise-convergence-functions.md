---
id: pointwise-convergence-functions
title: Pointwise Convergence of Function Sequences
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
- id: function-notation-review
  type: soft
builds-toward:
- uniform-convergence-functions
- uniform-convergence-preserves-continuity
tags:
- function-sequences
- pointwise
- convergence
stage: advanced
status: draft
---

# Pointwise Convergence of Function Sequences

## Core Idea
A sequence of functions (fₙ) converges pointwise to f if for every x and every ε > 0, there exists N (depending on both x and ε) such that n > N implies |fₙ(x) - f(x)| < ε. This is the weakest notion of convergence for functions. Pointwise limits can have surprising properties: a sequence of continuous functions can converge pointwise to a discontinuous function.

## Questions

```yaml
- question: "Consider the sequence fₙ(x) = xⁿ on the interval [0,1]. What is the pointwise limit?"
  type: multiple-choice
  options:
    - "f(x) = 1 for all x ∈ [0,1], because each xⁿ is bounded by 1"
    - "f(x) = 0 for all x ∈ [0,1], because powers of numbers less than 1 go to 0"
    - "f(x) = 0 for x ∈ [0,1) and f(1) = 1 — a discontinuous function"
    - "The sequence does not converge pointwise because the functions are not monotone"
  answer: 2
  explanation: "For any fixed x ∈ [0,1), we have |x| < 1 so xⁿ → 0 as n → ∞. But at x = 1, fₙ(1) = 1ⁿ = 1 for every n, so the limit is 1. The pointwise limit is therefore 0 on [0,1) and 1 at x = 1 — a discontinuous function, even though every fₙ is continuous. This is the canonical example showing that pointwise convergence does not preserve continuity."

- question: "In the definition of pointwise convergence, the threshold N such that n > N implies |fₙ(x) − f(x)| < ε:"
  type: multiple-choice
  options:
    - "Must be the same for every x in the domain — otherwise the convergence is not well-defined"
    - "Can depend on both x and ε"
    - "Can depend on ε but must be chosen independently of x"
    - "Must be chosen before specifying which x we are testing"
  answer: 1
  explanation: "Pointwise convergence allows N to depend on both x and ε. This is the critical distinction from uniform convergence, where N must work for all x simultaneously (N depends only on ε). In the xⁿ example, for x = 0.99 and ε = 0.01 you need a much larger N than for x = 0.5 — the convergence is slow near 1, fast away from it. Requiring a single N for all x would be the stronger uniform convergence condition."

- question: "A sequence of continuous functions can converge pointwise to a function that is not continuous."
  type: true-false
  answer: true
  explanation: "True. The sequence fₙ(x) = xⁿ on [0,1] is a clean example: every fₙ is continuous, but the pointwise limit is 0 on [0,1) and 1 at x = 1, which is discontinuous. This is why pointwise convergence is called the 'weakest' notion — it gives very little control over the properties of the limit function. Uniform convergence, by contrast, does preserve continuity."

- question: "If fₙ → f pointwise and each fₙ is continuous, then f must also be continuous."
  type: true-false
  answer: false
  explanation: "False. As the xⁿ example on [0,1] shows, the pointwise limit of continuous functions can be discontinuous. Continuity of the limit is preserved by uniform convergence, not pointwise convergence. Intuitively, pointwise convergence only requires that at each individual x the approximation eventually works — it places no constraint on how fast convergence happens across different x values, and that lack of uniformity allows the limit to 'jump' at a boundary point."

- question: "Explain why the N in the definition of pointwise convergence is allowed to depend on x, and what goes wrong if we instead require N to be independent of x."
  type: short-answer
  answer: "Pointwise convergence asks, for each fixed x, whether fₙ(x) → f(x) as a sequence of real numbers. Since each x is treated independently, the rate of convergence can vary across x, so we need an N that is large enough for that particular x. Requiring N to be independent of x — to work simultaneously for all x — is exactly the definition of uniform convergence, a strictly stronger condition. In the xⁿ example, near x = 1 the sequence converges very slowly (you need a huge N to get xⁿ below any fixed ε), while near x = 0 it converges immediately. No single N can handle all x values at once, so the convergence is pointwise but not uniform."
  explanation: "The philosophical point: pointwise convergence is a statement about infinitely many sequences of numbers (one sequence per x), each converging in its own time. Uniform convergence is a statement about a single sequence of functions converging as a whole object. The gap between them is where continuity, integrability, and differentiability can break: operations that commute with limits for sequences of numbers may fail when functions converge only pointwise."
```
