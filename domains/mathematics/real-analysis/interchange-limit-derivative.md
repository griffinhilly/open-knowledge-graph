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

## Explainer

You know from uniform convergence that swapping limit operations requires work: uniform convergence lets you exchange a limit with an integral and preserves continuity, but neither of these facts is obvious from pointwise convergence alone. The question here is harder still: if fₙ → f, can you conclude that fₙ' → f'? That is, can you differentiate through a limit?

The naive hope fails dramatically. Consider fₙ(x) = sin(nx)/√n. These functions converge uniformly to 0 (the amplitudes 1/√n → 0), so the limit function is f = 0 and f' = 0. But differentiating gives fₙ'(x) = √n cos(nx), whose amplitude grows without bound — these derivatives do not converge at all. The functions become flat in the limit, but they oscillate wildly and increasingly rapidly along the way. So even **uniform convergence of the functions** is not enough to control the derivatives.

The correct theorem requires a different trade: you need **uniform convergence of the derivatives** fₙ', plus pointwise convergence of the functions at at least one point. If both hold, then two conclusions follow: the functions themselves converge uniformly to some limit f, and the derivatives converge uniformly to f'. You can exchange the limit and derivative: lim (d/dx fₙ) = d/dx (lim fₙ). The intuition is that uniform convergence of fₙ' controls how fast the functions change across all x simultaneously — preventing the oscillation disaster in the earlier example.

This theorem is the engine behind **term-by-term differentiation of power series**. A power series Σaₙxⁿ converges on an interval to some function f. You want to differentiate it by differentiating each term: (Σaₙxⁿ)' = Σnaₙxⁿ⁻¹. The interchange theorem — with the Weierstrass M-test establishing uniform convergence of the derivative series inside any compact subinterval — justifies this operation rigorously. The result is that a power series is infinitely differentiable inside its radius of convergence, and each derivative is computed term by term. This connects uniform convergence to the rich theory of analytic functions.
