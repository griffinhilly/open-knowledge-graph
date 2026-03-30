---
id: brownian-motion-stochastic
title: Brownian Motion and the Wiener Process
domain: mathematics
course: stochastic-processes
prerequisites:
- id: martingales-introduction
  type: hard
- id: measure-spaces
  type: hard
- id: random-variables-as-measurable-functions
  type: hard
- id: normal-distribution
  type: soft
tags:
- brownian-motion-stochastic
- wiener-process
- stochastic-processes
- continuous-time
stage: expert
status: validated
---

# Brownian Motion and the Wiener Process

## Core Idea
Brownian motion (the Wiener process) is a continuous-time stochastic process W(t) with W(0) = 0, independent increments, stationary Gaussian increments (W(t) - W(s) ~ N(0, t-s)), and almost surely continuous sample paths. It is the canonical building block of stochastic calculus and the continuous-time analogue of a symmetric random walk. The Wiener measure on the space of continuous functions C([0,∞)) provides the rigorous measure-theoretic foundation.

## Questions

```yaml
- question: "A symmetric random walk S_n with step size 1/√n is rescaled as X_n(t) = S_{⌊nt⌋}/√n. As n → ∞, what does X_n converge to in distribution?"
  type: multiple-choice
  options:
    - "A Poisson process with rate 1"
    - "Standard Brownian motion W(t), by Donsker's invariance principle (the functional central limit theorem)"
    - "A deterministic linear function of time"
    - "A Cauchy process, since the limiting distribution has heavy tails"
  answer: 1
  explanation: "Donsker's theorem (the functional CLT) states that the rescaled random walk converges in distribution to standard Brownian motion in the space C([0,1]) with the sup-norm topology. Each increment S_{k+1} - S_k has mean 0 and variance 1, so after rescaling by √n, the CLT applies at each fixed time. Donsker's theorem strengthens this from finite-dimensional convergence to convergence of the entire path. This is the deep justification for Brownian motion as the universal limit of random walks."

- question: "Brownian motion has independent increments: W(t₂) - W(t₁) and W(t₄) - W(t₃) are independent whenever the intervals [t₁,t₂] and [t₃,t₄] do not overlap."
  type: true-false
  answer: true
  explanation: "Independent increments over non-overlapping intervals is one of the defining properties of Brownian motion. Combined with the Gaussian distribution of each increment and continuity of paths, it fully characterizes the Wiener process. Note that overlapping increments like W(3) - W(1) and W(4) - W(2) are not independent because they share the contribution from [2,3]."

- question: "The sample paths of Brownian motion are almost surely continuous but almost surely nowhere differentiable. Explain why continuity does not imply differentiability in this context."
  type: short-answer
  answer: "Continuity means W(t+h) → W(t) as h → 0, but differentiability requires (W(t+h) - W(t))/h to converge. Since W(t+h) - W(t) ~ N(0,h), the increment is of order √h, so the difference quotient is of order 1/√h → ∞. The path is continuous because the increments shrink, but those increments don't shrink fast enough (relative to h) for a derivative to exist. This reflects the fractal, infinitely jagged nature of Brownian paths — they have Hausdorff dimension 3/2."
  explanation: "The nowhere-differentiability of Brownian motion is not an edge case — it holds with probability 1. The heuristic |W(t+h) - W(t)| ~ √h captures it: continuity needs increments to vanish (√h → 0), while differentiability needs them to vanish faster than h (√h/h = 1/√h → ∞). This gap between continuity and differentiability is why classical calculus fails for Brownian motion and why Itô calculus is necessary."

- question: "The covariance function of standard Brownian motion is Cov(W(s), W(t)) = ?"
  type: multiple-choice
  options:
    - "s·t"
    - "min(s, t)"
    - "|s - t|"
    - "e^{-|s-t|}"
  answer: 1
  explanation: "For s ≤ t, write W(t) = W(s) + (W(t) - W(s)). Then Cov(W(s), W(t)) = Cov(W(s), W(s)) + Cov(W(s), W(t) - W(s)) = Var(W(s)) + 0 = s = min(s,t). The zero cross-term follows from independent increments: W(s) depends only on the process up to time s, and W(t) - W(s) is independent of the process up to time s. The min(s,t) covariance uniquely identifies the Gaussian process that is Brownian motion."
```

## Explainer

**Brownian motion** is the foundational object of continuous-time probability. Physically, it models the erratic movement of a pollen grain suspended in water — the phenomenon Robert Brown observed in 1827 and Einstein explained in 1905. Mathematically, it is a stochastic process W(t) defined for t ≥ 0, characterized by four properties: W(0) = 0, independent increments over non-overlapping time intervals, Gaussian increments with W(t) - W(s) ~ N(0, t-s) for t > s, and continuous sample paths almost surely. Norbert Wiener gave the first rigorous construction (1923), which is why the process is also called the Wiener process.

The construction is non-trivial. You need to produce a probability measure on the infinite-dimensional space C([0,∞)) of continuous functions. One approach uses the Kolmogorov extension theorem: the finite-dimensional distributions are multivariate Gaussians (determined by the mean function μ(t) = 0 and covariance function K(s,t) = min(s,t)), and the extension theorem guarantees a consistent probability measure on infinite product spaces. Continuity of paths then follows from the Kolmogorov continuity criterion, using the fact that E[|W(t) - W(s)|⁴] = 3(t-s)² gives sufficient moment control.

From your study of martingales, Brownian motion provides a rich supply of continuous-time martingales. W(t) itself is a martingale (its expected future value given the present is the present value). W(t)² - t is also a martingale — the quadratic variation of Brownian motion grows linearly, and subtracting t compensates for this growth. More generally, exp(θW(t) - θ²t/2) is a martingale for any real θ (the exponential martingale). These martingale properties are the engine behind optional stopping arguments, change-of-measure techniques, and the entire apparatus of stochastic calculus.

The sample paths of Brownian motion are almost surely continuous but almost surely nowhere differentiable. The increments W(t+h) - W(t) have standard deviation √h, which goes to zero (continuity) but not fast enough relative to h for a derivative to exist (the ratio √h/h = 1/√h diverges). This pathological roughness — Brownian paths have Hausdorff dimension 3/2 — is precisely why Brownian motion cannot be analyzed using ordinary calculus and demands the development of Itô's stochastic integral, the next major topic in this course.
