---
id: properties-of-brownian-motion
title: Properties of Brownian Motion
domain: mathematics
course: stochastic-processes
prerequisites:
- id: brownian-motion
  type: hard
- id: lebesgue-integral
  type: soft
tags:
- brownian-motion-stochastic
- quadratic-variation
- scaling
- reflection-principle
stage: expert
status: validated
---

# Properties of Brownian Motion

## Core Idea
Brownian motion exhibits remarkable structural properties beyond its definition. It is self-similar (scaling invariance: cW(t/c²) is again a Brownian motion), has unbounded variation but finite quadratic variation equal to t, satisfies the strong Markov property, and obeys a reflection principle. The quadratic variation [W,W]_t = t is the single most consequential property for stochastic calculus — it is the reason Itô's formula has an extra term compared to the classical chain rule.

## Questions

```yaml
- question: "The total variation of Brownian motion on any interval [0,T] is:"
  type: multiple-choice
  options:
    - "Equal to T, matching the quadratic variation"
    - "Finite but random, depending on the particular sample path"
    - "Almost surely infinite"
    - "Zero, because the expected value of each increment is zero"
  answer: 2
  explanation: "Brownian paths are so rough that their total variation (sum of absolute increments) is infinite on every interval. Over a partition of [0,T] into n subintervals, the sum of |ΔW_i| is approximately Σ|N(0,T/n)| ~ n · √(T/n) · √(2/π) = √(2Tn/π) → ∞ as n → ∞. This infinite first variation but finite quadratic variation (equal to T) places Brownian motion in a regularity class between differentiable functions (finite first variation) and truly wild paths. It is the finite quadratic variation that makes stochastic calculus work."

- question: "If W(t) is a standard Brownian motion, is the time-reversed process X(t) = tW(1/t) (with X(0) = 0) also a standard Brownian motion?"
  type: true-false
  answer: true
  explanation: "This is the time-inversion property. X(t) = tW(1/t) has Gaussian finite-dimensional distributions with E[X(t)] = 0 and Cov(X(s), X(t)) = st · Cov(W(1/s), W(1/t)) = st · min(1/s, 1/t) = st · (1/max(s,t)) = min(s,t). Since X has the correct mean, covariance, and Gaussian distributions, and its continuity at 0 follows from the law of the iterated logarithm, X is a standard Brownian motion. This is one of several non-obvious symmetries of the Wiener process."

- question: "Why does the quadratic variation of Brownian motion being equal to t (rather than zero) fundamentally change the rules of calculus for stochastic integrals?"
  type: short-answer
  answer: "In ordinary calculus, smooth functions have zero quadratic variation, and (df)² terms vanish in Taylor expansions. Brownian motion's quadratic variation [W,W]_t = t means (dW)² ≈ dt is a first-order term that cannot be discarded. When expanding f(W(t)) via Taylor series, the second-order term (1/2)f''(W)(dW)² contributes (1/2)f''(W)dt — a non-zero drift term. This produces the extra (1/2)σ²f'' correction in Itô's formula compared to the classical chain rule. The quadratic variation is finite and deterministic, which is what makes the resulting calculus consistent."
  explanation: "The heuristic dW² = dt captures the essential point: Brownian motion is rough enough that second-order terms in Taylor expansions survive. For any process with zero quadratic variation (all smooth deterministic functions), the classical chain rule suffices. The non-zero quadratic variation of Brownian motion is the single structural fact that necessitates Itô calculus."

- question: "The scaling property states that for any c > 0, the process Y(t) = (1/√c)W(ct) is also a standard Brownian motion."
  type: true-false
  answer: true
  explanation: "Check: Y(0) = 0, Y has Gaussian increments with Y(t) - Y(s) = (1/√c)(W(ct) - W(cs)) ~ N(0, (ct-cs)/c) = N(0, t-s), and Y inherits independence of increments and path continuity from W. The process Y is therefore a standard Brownian motion. This self-similarity means Brownian motion looks statistically the same at all scales — zooming in on a Brownian path yields another Brownian path, which is characteristic of fractal objects."
```

## Explainer

Beyond its four defining properties, Brownian motion possesses a constellation of structural features that make it uniquely tractable and deeply connected to analysis. The most important of these is **quadratic variation**. For a partition 0 = t₀ < t₁ < ... < tₙ = T of [0,T], the quadratic variation is the limit of Σ(W(tᵢ) - W(tᵢ₋₁))² as the mesh goes to zero. Each squared increment (W(tᵢ) - W(tᵢ₋₁))² has mean tᵢ - tᵢ₋₁ and variance 2(tᵢ - tᵢ₋₁)², so the sum has mean T and variance that goes to zero — it converges in L² to T. This deterministic quadratic variation [W,W]_T = T, summarized as the heuristic (dW)² = dt, is the engine of Itô calculus.

**Self-similarity** (scaling invariance) states that (1/√c)W(ct) is again a standard Brownian motion for any c > 0. Brownian motion looks statistically identical at every timescale — zoom into a small segment and rescale, and you see the same statistical object. This fractal character is reflected in the Hausdorff dimension of 3/2 for the graph of t ↦ W(t). Related symmetries include time inversion (tW(1/t) is a Brownian motion) and the reflection principle (|W(t)| or W reflected at its maximum relate the distribution of the running maximum to the process itself). The reflection principle yields the distribution of the maximum: P(max_{s≤t} W(s) ≥ a) = 2P(W(t) ≥ a) for a > 0.

The **strong Markov property** extends the ordinary Markov property from deterministic times to stopping times: given the process at a stopping time τ, the future process W(τ + t) - W(τ) is an independent Brownian motion. This is essential for analyzing first-passage times and boundary problems. Combined with the reflection principle, it implies that the first hitting time T_a = inf{t : W(t) = a} has an inverse Gaussian distribution with E[T_a] = ∞ — Brownian motion will eventually hit any level, but the expected time to do so is infinite.

The contrast between **total variation** (infinite) and **quadratic variation** (finite) determines the entire character of stochastic calculus. Smooth functions have finite total variation and zero quadratic variation; Brownian motion has infinite total variation but deterministic quadratic variation equal to t. This places Brownian paths in a precise regularity class: too rough for ordinary calculus (which assumes zero quadratic variation), but regular enough for the Itô integral (which requires finite quadratic variation). Every major result in stochastic calculus — Itô's formula, the Girsanov theorem, the martingale representation theorem — traces back to this fundamental property.
