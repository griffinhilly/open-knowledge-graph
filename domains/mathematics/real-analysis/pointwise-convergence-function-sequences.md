---
id: pointwise-convergence-function-sequences
title: Pointwise Convergence of Function Sequences
domain: mathematics
course: real-analysis
prerequisites:
- id: epsilon-n-convergence
  type: hard
builds-toward:
- uniform-convergence
- interchange-limit-integral
tags:
- pointwise-convergence
- function-sequences
- limits
stage: advanced
status: draft
---

# Pointwise Convergence of Function Sequences

## Core Idea
A sequence of functions (fₙ) converges pointwise to f on a set S if for every x in S and every ε > 0, there exists N (depending on both ε and x) such that for all n > N, |fₙ(x) − f(x)| < ε. Pointwise convergence is the basic notion but can behave pathologically: limits of continuous functions need not be continuous.

## Questions

```yaml
- question: "Consider fₙ(x) = xⁿ on [0, 1]. The pointwise limit as n → ∞ is f(x) = 0 for x ∈ [0, 1) and f(1) = 1. What does this illustrate about pointwise convergence?"
  type: multiple-choice
  options:
    - "The convergence is uniform because all functions fₙ are continuous on [0,1]"
    - "The limit f is discontinuous even though every fₙ is continuous — pointwise convergence does not preserve continuity"
    - "The limit f must be wrong because a sequence of continuous functions always converges to a continuous function"
    - "Pointwise convergence cannot be defined on closed intervals since boundary behavior is ambiguous"
  answer: 1
  explanation: "Each fₙ(x) = xⁿ is continuous on [0, 1]. But the pointwise limit is f(x) = 0 for x < 1 and f(1) = 1 — a function with a jump discontinuity at x = 1. This is the canonical example of pointwise convergence's pathological behavior: the limit of continuous functions need not be continuous. The convergence is also not uniform — for any fixed n, points x close to 1 have xⁿ close to 1, so the sequence does not converge at a uniform rate across [0,1]."

- question: "In pointwise convergence of (fₙ) to f on S, the threshold N in the definition — the index beyond which |fₙ(x) − f(x)| < ε — may depend on:"
  type: multiple-choice
  options:
    - "Only ε — once a tolerance is fixed, the same N works for all x ∈ S simultaneously"
    - "Only x — different points converge at different speeds regardless of tolerance"
    - "Both ε and x — different points in S may require different N values even for the same ε"
    - "Neither ε nor x — N is determined solely by properties of the sequence (fₙ)"
  answer: 2
  explanation: "This is the defining characteristic of pointwise (as opposed to uniform) convergence. For each fixed x, you ask: how large must n be so that fₙ(x) is within ε of f(x)? The answer can vary across different points — some points may converge quickly, others slowly. In uniform convergence, a single N works for all x simultaneously (N depends only on ε, not on x). The logical structure captures the difference: pointwise says ∀x ∀ε ∃N (N chosen after x is fixed); uniform says ∀ε ∃N ∀x (a single N works everywhere)."

- question: "In the definition of pointwise convergence, the value of N (the index beyond which fₙ(x) is within ε of f(x)) is allowed to depend on the choice of x ∈ S."
  type: true-false
  answer: true
  explanation: "This is the defining feature that separates pointwise from uniform convergence. In pointwise convergence, for each x separately, you find an N that works for that particular x and ε. Different points may need very different N values — a slowly converging part of the domain requires a much larger N than a rapidly converging part. Uniform convergence is the stronger condition where a single N works simultaneously for all x."

- question: "If each function fₙ in a sequence is continuous on a closed interval [a, b] and fₙ converges pointwise to f, then f must also be continuous on [a, b]."
  type: true-false
  answer: false
  explanation: "This is false, and fₙ(x) = xⁿ on [0, 1] is the standard counterexample. Every xⁿ is continuous, but the pointwise limit has a jump discontinuity at x = 1. Continuity IS preserved under uniform convergence (a key theorem in analysis), which is one reason uniform convergence is considered the 'right' notion: it supports interchange of limits with continuity, integration, and differentiation in ways that pointwise convergence cannot guarantee."

- question: "Explain in your own words the key logical difference between pointwise and uniform convergence in terms of quantifier order."
  type: short-answer
  answer: "In pointwise convergence, N is chosen after x is fixed: for every x and every ε, there exists N (depending on both x and ε) such that n > N implies |fₙ(x) − f(x)| < ε. In uniform convergence, N is chosen before x: for every ε, there exists a single N such that for ALL x and all n > N, |fₙ(x) − f(x)| < ε. The key difference is that N cannot depend on x in the uniform case — the entire domain must converge at the same rate. This is not just a technicality: it determines which analytic properties (continuity, integrability, differentiability) pass to the limit."
  explanation: "The logical structure ∀x ∀ε ∃N(x,ε) versus ∀ε ∃N(ε) ∀x precisely captures whether convergence speed is allowed to vary with location. The inability to 'choose N after seeing x' is what makes uniform convergence powerful enough to preserve analytic structure."
```

## Questions

```yaml
- question: "Consider fₙ(x) = xⁿ on [0, 1]. The pointwise limit is f(x) = 0 for x ∈ [0,1) and f(1) = 1. What does this example illustrate?"
  type: multiple-choice
  options:
    - "The convergence is uniform because all functions fₙ are continuous on [0,1]"
    - "The pointwise limit f is discontinuous even though every fₙ is continuous — pointwise convergence does not preserve continuity"
    - "The limit must be wrong because a sequence of continuous functions always converges to a continuous function"
    - "Pointwise convergence cannot be defined on closed intervals"
  answer: 1
  explanation: "Each xⁿ is continuous on [0,1], but the pointwise limit has a jump discontinuity at x = 1 (it equals 0 just to the left and 1 at x = 1). This is the canonical example of pointwise convergence's pathological behavior: the limit of a sequence of continuous functions need not be continuous. The convergence is also not uniform — for any fixed n, points x close to 1 satisfy xⁿ close to 1, not close to 0, so no single N makes the approximation uniformly good near x = 1."

- question: "In the definition of pointwise convergence of (fₙ) to f on S, the threshold N such that |fₙ(x) − f(x)| < ε for all n > N depends on:"
  type: multiple-choice
  options:
    - "Only ε — once you fix a tolerance, the same N works for all x ∈ S"
    - "Only x — different points converge at different speeds regardless of tolerance"
    - "Both ε and x — the N needed to get within ε of the limit can vary across different points in S"
    - "Neither ε nor x — N is determined by the sequence alone"
  answer: 2
  explanation: "This is the defining characteristic of pointwise (as opposed to uniform) convergence. For each fixed x, you ask how large n must be so that fₙ(x) is within ε of f(x) — and the answer can vary across different points. Some parts of the domain may converge quickly, others slowly. The logical quantifier order is: ∀x ∀ε ∃N(x,ε), where N is chosen after x is fixed. Uniform convergence flips this: ∀ε ∃N ∀x, so a single N works everywhere simultaneously."

- question: "In the definition of pointwise convergence, the value of N is allowed to depend on the particular point x ∈ S being considered."
  type: true-false
  answer: true
  explanation: "This is the defining feature that separates pointwise from uniform convergence. In pointwise convergence, for each x separately, you find an N that works for that specific x and ε — different points may need different N values. A slowly converging part of the domain can require a much larger N than a rapidly converging part. Uniform convergence is the stronger condition where a single N works simultaneously for all x, meaning the sequence converges at a rate that does not depend on location."

- question: "If each function fₙ in a sequence is continuous on [a, b] and fₙ converges pointwise to f, then f must be continuous on [a, b]."
  type: true-false
  answer: false
  explanation: "False — fₙ(x) = xⁿ on [0,1] is the standard counterexample. Every xⁿ is continuous, but the pointwise limit is 0 on [0,1) and 1 at x = 1, which is discontinuous at x = 1. Continuity IS preserved under uniform convergence (a key theorem of real analysis), which is one reason uniform convergence is the analytically 'right' notion: it supports the interchange of limits and continuous operations that pointwise convergence cannot guarantee."

- question: "Explain the key difference between pointwise and uniform convergence in terms of the logical structure of their definitions."
  type: short-answer
  answer: "In pointwise convergence, the required index N depends on both the tolerance ε and the specific point x: for each x, you independently find how large n must be to get within ε of the limit at that point. The logical structure is: ∀x ∀ε ∃N(x,ε) such that n > N implies |fₙ(x) − f(x)| < ε. In uniform convergence, N is found before x is chosen: ∀ε ∃N ∀x such that n > N implies |fₙ(x) − f(x)| < ε for all x simultaneously. Uniform convergence requires the sequence to converge at a rate that works uniformly across the entire domain."
  explanation: "The quantifier order — whether N is chosen before or after x — is the precise mathematical statement of this difference. It is not a technicality: it determines which analytic properties (continuity, integrability, differentiability) are preserved by the limit. Pointwise convergence is too weak to guarantee any of these interchanges; uniform convergence is exactly strong enough."
```
