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
status: validated
---

# Pointwise Convergence of Function Sequences

## Core Idea
A sequence of functions (fₙ) converges pointwise to f on a set S if for every x in S and every ε > 0, there exists N (depending on both ε and x) such that for all n > N, |fₙ(x) − f(x)| < ε. Pointwise convergence is the basic notion but can behave pathologically: limits of continuous functions need not be continuous.

## How It's Best Learned
Compute the threshold N(x, ε) for fₙ(x) = xⁿ with ε = 0.01. You need xⁿ < 0.01, so n > ln(0.01)/ln(x). That gives n ≥ 7 at x = 0.5, n ≥ 44 at x = 0.9, and n ≥ 459 at x = 0.99. Seeing N grow without bound as x → 1 is the whole content of "N depends on x." Compare with fₙ(x) = x/n, where N = 100 works at every point of [0, 1].

## Common Misconceptions
- A pointwise limit of continuous functions is continuous. (fₙ(x) = xⁿ on [0, 1] has a limit that jumps from 0 to 1 at x = 1.)
- If fₙ → 0 pointwise, the graphs eventually lie close to the x-axis everywhere at once. (The bump fₙ = 1 on [n, n + 1] and 0 elsewhere tends to 0 at every x, yet every graph has a bump of height 1.)
- Pointwise convergence makes the largest error sup |fₙ(x) − f(x)| shrink to 0. (For xⁿ on [0, 1), that supremum equals 1 for every n; shrinking sup error is uniform convergence.)

## Questions

```yaml
- question: Consider fₙ(x) = xⁿ on [0, 1]. The pointwise limit as n → ∞ is f(x) = 0 for x ∈ [0, 1) and f(1) = 1. What does this illustrate about pointwise convergence?
  type: multiple-choice
  options:
  - The convergence is uniform because all functions fₙ are continuous on [0,1]
  - The limit f is discontinuous even though every fₙ is continuous — pointwise convergence does not preserve continuity
  - The limit f must be wrong because a sequence of continuous functions always converges to a continuous function
  - Pointwise convergence cannot be defined on closed intervals since boundary behavior is ambiguous
  answer: 1
  explanation: 'Each fₙ(x) = xⁿ is continuous on [0, 1]. But the pointwise limit is f(x) = 0 for x < 1 and f(1) = 1 — a function with a jump discontinuity at x = 1. This is the canonical example of pointwise convergence''s pathological behavior: the limit of continuous functions need not be continuous. The convergence is also not uniform — for any fixed n, points x close to 1 have xⁿ close to 1, so the sequence does not converge at a uniform rate across [0,1].'

- question: 'In pointwise convergence of (fₙ) to f on S, the threshold N in the definition — the index beyond which |fₙ(x) − f(x)| < ε — may depend on:'
  type: multiple-choice
  options:
  - Only ε — once a tolerance is fixed, the same N works for all x ∈ S simultaneously
  - Only x — different points converge at different speeds regardless of tolerance
  - Both ε and x — different points in S may require different N values even for the same ε
  - Neither ε nor x — N is determined solely by properties of the sequence (fₙ)
  answer: 2
  explanation: 'This is the defining characteristic of pointwise (as opposed to uniform) convergence. For each fixed x, you ask: how large must n be so that fₙ(x) is within ε of f(x)? The answer can vary across different points — some points may converge quickly, others slowly. In uniform convergence, a single N works for all x simultaneously (N depends only on ε, not on x). The logical structure captures the difference: pointwise says ∀x ∀ε ∃N (N chosen after x is fixed); uniform says ∀ε ∃N ∀x (a single N works everywhere).'

- question: In the definition of pointwise convergence, the value of N (the index beyond which fₙ(x) is within ε of f(x)) is allowed to depend on the choice of x ∈ S.
  type: true-false
  answer: true
  explanation: This is the defining feature that separates pointwise from uniform convergence. In pointwise convergence, for each x separately, you find an N that works for that particular x and ε. Different points may need very different N values — a slowly converging part of the domain requires a much larger N than a rapidly converging part. Uniform convergence is the stronger condition where a single N works simultaneously for all x.

- question: If each function fₙ in a sequence is continuous on a closed interval [a, b] and fₙ converges pointwise to f, then f is expected to also be continuous on [a, b].
  type: true-false
  answer: false
  explanation: 'This is false, and fₙ(x) = xⁿ on [0, 1] is the standard counterexample. Every xⁿ is continuous, but the pointwise limit has a jump discontinuity at x = 1. Continuity IS preserved under uniform convergence (a key theorem in analysis), which is one reason uniform convergence is considered the ''right'' notion: it supports interchange of limits with continuity, integration, and differentiation in ways that pointwise convergence cannot guarantee.'

- question: Explain in your own words the key logical difference between pointwise and uniform convergence in terms of quantifier order.
  type: short-answer
  answer: 'In pointwise convergence, N is chosen after x is fixed: for every x and every ε, there exists N (depending on both x and ε) such that n > N implies |fₙ(x) − f(x)| < ε. In uniform convergence, N is chosen before x: for every ε, there exists a single N such that for ALL x and all n > N, |fₙ(x) − f(x)| < ε. The key difference is that N cannot depend on x in the uniform case — the entire domain must converge at the same rate. This is not just a technicality: it determines which analytic properties (continuity, integrability, differentiability) pass to the limit.'
  explanation: The logical structure ∀x ∀ε ∃N(x,ε) versus ∀ε ∃N(ε) ∀x precisely captures whether convergence speed is allowed to vary with location. The inability to 'choose N after seeing x' is what makes uniform convergence powerful enough to preserve analytic structure.
```

## Explainer

From your study of ε-N convergence for sequences of real numbers, you know what it means for a sequence aₙ to converge to a limit L: for every ε > 0, there exists N such that n > N implies |aₙ − L| < ε. **Pointwise convergence of function sequences** applies this same idea at each point of the domain independently. Given a sequence of functions f₁, f₂, f₃, ... defined on a set S, for each fixed x ∈ S the values f₁(x), f₂(x), f₃(x), ... form an ordinary sequence of real numbers. If that numerical sequence converges for every x ∈ S, we say fₙ converges pointwise to the limit function f, where f(x) = lim_{n→∞} fₙ(x).

The formal definition makes the structure explicit: for every x ∈ S and every ε > 0, there exists N (depending on both ε and x) such that n > N implies |fₙ(x) − f(x)| < ε. The dependence of N on x is the defining feature. At some points, convergence may be fast (small N suffices); at others, it may be agonizingly slow (enormous N required). The definition places no constraint on how N varies across x — each point converges at its own pace.

The canonical example is fₙ(x) = xⁿ on [0, 1]. For any fixed x ∈ [0, 1), since |x| < 1, xⁿ → 0 as n → ∞. At x = 1, however, 1ⁿ = 1 for all n. The pointwise limit is therefore f(x) = 0 for x ∈ [0, 1) and f(1) = 1 — a discontinuous function, even though every fₙ is continuous. This is the central warning about pointwise convergence: **the limit of a sequence of continuous functions need not be continuous**. The convergence at points near x = 1 is extremely slow (for x = 0.999, you need n on the order of thousands for xⁿ to be small), and this non-uniform rate of convergence allows the limit to develop a discontinuity.

This pathological behavior is what motivates **uniform convergence**, the stronger notion where a single N works for all x simultaneously (N depends only on ε, not on x). Uniform convergence preserves continuity, commutes with integration, and under appropriate hypotheses commutes with differentiation — none of which pointwise convergence guarantees. The passage from pointwise to uniform convergence is one of the key conceptual advances of real analysis: it identifies exactly how much control over convergence speed is needed to ensure that the limit inherits the analytic properties of the approximating functions.
