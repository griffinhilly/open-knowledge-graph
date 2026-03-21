---
id: interchange-limit-derivative
title: Interchange of Limit and Derivative
domain: mathematics
course: real-analysis
prerequisites:
- id: uniform-convergence-functions
  type: hard
- id: rigorous-derivative-definition
  type: hard
builds-toward:
- uniform-convergence-power-series
tags:
- limit-derivative
- interchange
- convergence
stage: advanced
status: draft
---

# Interchange of Limit and Derivative

## Core Idea
If (fₙ) is a sequence of differentiable functions such that (fₙ') converges uniformly and (fₙ) converges pointwise, then (fₙ) converges uniformly to f, and lim fₙ' = f'. This is a deep result: passing limits through derivatives requires uniform convergence of derivatives, not just the original functions. It enables term-by-term differentiation of power series.

## Questions

```yaml
- question: "Consider fₙ(x) = sin(nx)/√n. These functions converge uniformly to 0. Can you conclude that lim fₙ'(x) = (lim fₙ)'(x) = 0?"
  type: multiple-choice
  options:
    - "Yes — uniform convergence of the functions is sufficient to interchange limit and derivative"
    - "No — fₙ'(x) = √n cos(nx), whose amplitude grows without bound, so the derivatives do not converge"
    - "Yes — because the limit function f = 0 is differentiable, the interchange is always valid"
    - "No — the interchange requires only pointwise convergence, not uniform convergence"
  answer: 1
  explanation: "fₙ'(x) = √n cos(nx) has amplitude √n → ∞, so the derivatives diverge everywhere. This is the canonical counterexample showing that uniform convergence of fₙ is not sufficient to interchange limit and derivative. The functions become flat (amplitudes 1/√n → 0) but oscillate faster and faster — the derivative tracks oscillation speed, not amplitude, so it blows up even as the functions themselves vanish."

- question: "Which conditions are jointly sufficient to justify d/dx(lim fₙ) = lim(d/dx fₙ)?"
  type: multiple-choice
  options:
    - "Pointwise convergence of fₙ and pointwise convergence of fₙ'"
    - "Uniform convergence of fₙ and continuity of fₙ'"
    - "Uniform convergence of fₙ' and pointwise convergence of fₙ at at least one point"
    - "Uniform convergence of both fₙ and fₙ' must be assumed separately"
  answer: 2
  explanation: "The interchange theorem requires: (1) uniform convergence of the derivatives fₙ', and (2) pointwise convergence of fₙ at at least one point. Option D sounds stronger but is actually redundant — uniform convergence of fₙ is a conclusion of the theorem given these hypotheses, not an additional assumption. The key is that uniform control on derivatives (not on functions) is what prevents pathological oscillation."

- question: "If fₙ' converges uniformly to some function g, and fₙ converges pointwise to f at one point, then fₙ converges to f uniformly on the entire domain."
  type: true-false
  answer: true
  explanation: "This is part of the interchange theorem's conclusion. Uniform convergence of fₙ is guaranteed by uniform convergence of fₙ' plus pointwise convergence of fₙ anywhere — you don't need to assume it. The pointwise convergence at one point 'anchors' the family; the uniform control on the derivatives then forces uniform convergence of the functions themselves."

- question: "If a sequence of differentiable functions fₙ converges uniformly to f, then the sequence of derivatives fₙ' converges uniformly to f'."
  type: true-false
  answer: false
  explanation: "False — fₙ(x) = sin(nx)/√n is a direct counterexample. These functions converge uniformly to 0, yet fₙ'(x) = √n cos(nx) diverges. Uniform convergence controls the values of fₙ across x, but says nothing about how fast the functions change. The derivative measures rate of change, which can be wild even when the functions themselves are uniformly small."

- question: "Why is uniform convergence of the derivatives — rather than uniform convergence of the functions — the key condition needed to interchange limit and derivative?"
  type: short-answer
  answer: "The derivative measures rate of change, not magnitude. A sequence of functions can be uniformly small (converging to zero) while oscillating increasingly rapidly — producing arbitrarily large derivatives. Uniform convergence of the derivatives prevents this: it says the rates of change of fₙ are uniformly controlled across all x, which is exactly what is needed to ensure that the limiting function's rate of change equals the limit of the rates of change."
  explanation: "The counterexample sin(nx)/√n makes this vivid: the amplitude goes to zero (uniform convergence of functions) but the frequency grows without bound (derivatives diverge). Requiring uniform convergence of fₙ' ensures that oscillation speed is uniformly bounded, ruling out the rapid-oscillation pathology that destroys the interchange."
```

## Explainer

You know from uniform convergence that swapping limit operations requires work: uniform convergence lets you exchange a limit with an integral and preserves continuity, but neither of these facts is obvious from pointwise convergence alone. The question here is harder still: if fₙ → f, can you conclude that fₙ' → f'? That is, can you differentiate through a limit?

The naive hope fails dramatically. Consider fₙ(x) = sin(nx)/√n. These functions converge uniformly to 0 (the amplitudes 1/√n → 0), so the limit function is f = 0 and f' = 0. But differentiating gives fₙ'(x) = √n cos(nx), whose amplitude grows without bound — these derivatives do not converge at all. The functions become flat in the limit, but they oscillate wildly and increasingly rapidly along the way. So even **uniform convergence of the functions** is not enough to control the derivatives.

The correct theorem requires a different trade: you need **uniform convergence of the derivatives** fₙ', plus pointwise convergence of the functions at at least one point. If both hold, then two conclusions follow: the functions themselves converge uniformly to some limit f, and the derivatives converge uniformly to f'. You can exchange the limit and derivative: lim (d/dx fₙ) = d/dx (lim fₙ). The intuition is that uniform convergence of fₙ' controls how fast the functions change across all x simultaneously — preventing the oscillation disaster in the earlier example.

This theorem is the engine behind **term-by-term differentiation of power series**. A power series Σaₙxⁿ converges on an interval to some function f. You want to differentiate it by differentiating each term: (Σaₙxⁿ)' = Σnaₙxⁿ⁻¹. The interchange theorem — with the Weierstrass M-test establishing uniform convergence of the derivative series inside any compact subinterval — justifies this operation rigorously. The result is that a power series is infinitely differentiable inside its radius of convergence, and each derivative is computed term by term. This connects uniform convergence to the rich theory of analytic functions.
