---
id: stationary-processes
title: Stationary Processes
domain: mathematics
course: stochastic-processes
prerequisites:
- id: brownian-motion
  type: hard
- id: conditional-expectation
  type: hard
- id: characteristic-functions
  type: soft
tags:
- stationarity
- autocovariance
- spectral-density
- wide-sense-stationarity
stage: expert
status: validated
---

# Stationary Processes

## Core Idea
A process X(t) is strictly stationary if its finite-dimensional distributions are invariant under time shifts: (X(t₁+h), ..., X(tₙ+h)) has the same joint distribution as (X(t₁), ..., X(tₙ)) for all h. Wide-sense (weak) stationarity requires only constant mean and a covariance function R(τ) = Cov(X(t), X(t+τ)) that depends only on the lag τ. The spectral representation theorem connects stationary processes to their power spectral density via the Fourier transform of the autocovariance.

## Questions

```yaml
- question: "Brownian motion W(t) has stationary increments (W(t+h) - W(s+h) has the same distribution as W(t) - W(s)). Is Brownian motion itself a stationary process?"
  type: multiple-choice
  options:
    - "Yes — stationary increments implies stationarity"
    - "No — Var(W(t)) = t grows with time, so the distribution of W(t) depends on t, violating stationarity"
    - "Yes, but only in the wide-sense (second-order) meaning"
    - "It depends on the initial condition W(0)"
  answer: 1
  explanation: "Stationarity requires the marginal distribution of X(t) to be time-invariant. Since W(t) ~ N(0,t), the variance grows linearly — the distribution at time 2 is N(0,2), different from the distribution at time 1 which is N(0,1). Brownian motion has stationary increments but is not itself stationary. The Ornstein-Uhlenbeck process, which adds mean reversion, is the canonical modification that produces a stationary Gaussian process."

- question: "A wide-sense stationary process has autocovariance R(τ). The power spectral density S(ω) is defined as the Fourier transform of R(τ). If R(τ) = σ²e^{-α|τ|} (as in the Ornstein-Uhlenbeck process), what is S(ω)?"
  type: multiple-choice
  options:
    - "S(ω) = σ²/(α² + ω²) · (2α), a Lorentzian (Cauchy) spectral density"
    - "S(ω) = σ²e^{-ω²/(2α²)}, a Gaussian spectral density"
    - "S(ω) = σ²δ(ω), concentrated at frequency zero"
    - "S(ω) = σ²/(2π) for all ω, flat (white noise)"
  answer: 0
  explanation: "The Fourier transform of e^{-α|τ|} is 2α/(α² + ω²). Multiplying by σ² gives S(ω) = 2ασ²/(α² + ω²), a Lorentzian. This decays as 1/ω² for large |ω|, meaning the OU process has less power at high frequencies — it is 'smoother' than white noise (which has flat S(ω)) but 'rougher' than processes with Gaussian spectral density. The parameter α determines the cutoff frequency: below α, the spectrum is approximately flat; above α, it decays. This characterizes the OU process as colored noise with a specific bandwidth."

- question: "Strict stationarity implies wide-sense stationarity whenever the first two moments exist."
  type: true-false
  answer: true
  explanation: "Strict stationarity means all finite-dimensional distributions are time-invariant. If the first two moments exist, this implies E[X(t)] is constant and Cov(X(t), X(t+τ)) depends only on τ — which is exactly wide-sense stationarity. The converse is false: a Gaussian process that is wide-sense stationary is also strictly stationary (because Gaussian distributions are determined by their first two moments), but for non-Gaussian processes, wide-sense stationarity is strictly weaker."

- question: "Explain why white noise (a process with R(τ) = σ²δ(τ)) cannot be a well-defined stochastic process with continuous sample paths."
  type: short-answer
  answer: "White noise has autocovariance R(τ) = σ²δ(τ), meaning the process is uncorrelated at every pair of distinct times — Cov(X(t), X(s)) = 0 for t ≠ s. For a continuous process, X(t) → X(s) as t → s, which would force Cov(X(t), X(s)) → Var(X(s)) = σ² as t → s. But R(τ) jumps from 0 to σ² at τ = 0, so the covariance is discontinuous — incompatible with path continuity. White noise exists as a generalized process (a distribution-valued process) or as the formal derivative of Brownian motion dW/dt, but not as a pointwise-defined continuous process."
  explanation: "This is why SDEs are written dX = σ dW rather than dX/dt = σ · (white noise). White noise ξ(t) = dW/dt doesn't exist as a function but does exist as a measure or distribution. The Itô integral ∫f dW is the rigorous substitute for ∫f(t)ξ(t)dt."
```

## Explainer

**Stationarity** captures the idea that a process's statistical character doesn't change over time. The strong form — strict stationarity — requires that time-shifting the entire process leaves all finite-dimensional distributions unchanged. The weaker but more practical form — wide-sense (or second-order) stationarity — requires only that the mean E[X(t)] = μ is constant and the autocovariance Cov(X(t), X(t+τ)) = R(τ) depends only on the time lag τ, not on the absolute time t. For Gaussian processes, the two notions coincide because Gaussian distributions are determined by their first two moments.

The **autocovariance function** R(τ) encodes the memory structure of a stationary process. It must be even (R(-τ) = R(τ)), positive semi-definite, and achieves its maximum at τ = 0 (R(0) = Var(X(t))). The rate at which R(τ) decays determines how quickly the process "forgets" its past: exponential decay R(τ) = σ²e^{-α|τ|} (the OU process) indicates a specific memory timescale 1/α, while power-law decay R(τ) ~ |τ|^{-β} indicates long-range dependence with no characteristic timescale. Brownian motion is not stationary (its variance grows), but its increment process X(t) = W(t+1) - W(t) is stationary with R(τ) that vanishes for |τ| > 1.

The **spectral representation** connects the time domain to the frequency domain. The Wiener-Khinchin theorem states that the power spectral density S(ω) = ∫R(τ)e^{-iωτ}dτ is the Fourier transform of the autocovariance, and conversely R(τ) = (1/2π)∫S(ω)e^{iωτ}dω. The spectral density S(ω) ≥ 0 describes how the process's variance is distributed across frequencies. White noise has flat S(ω) = σ² (equal power at all frequencies); the OU process has Lorentzian S(ω) = 2ασ²/(α² + ω²) (low-pass filtered); a periodic process has S(ω) concentrated at its fundamental frequency and harmonics.

Stationarity is both a modeling assumption and a mathematical prerequisite. In time series analysis and signal processing, stationarity is typically assumed so that the autocovariance and spectrum are well-defined and estimable from data. In stochastic process theory, stationarity is a property that diffusions achieve in the long run — the Ornstein-Uhlenbeck process converges to its stationary distribution regardless of initial conditions. Understanding stationarity is essential for ergodic theory (time averages of stationary ergodic processes converge to ensemble averages) and for the spectral theory of stochastic processes.
