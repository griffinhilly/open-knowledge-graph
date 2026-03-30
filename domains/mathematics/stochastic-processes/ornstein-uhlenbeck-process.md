---
id: ornstein-uhlenbeck-process
title: The Ornstein-Uhlenbeck Process
domain: mathematics
course: stochastic-processes
prerequisites:
- id: stochastic-differential-equations
  type: hard
- id: itos-formula
  type: hard
tags:
- ornstein-uhlenbeck
- mean-reversion
- stationary-process
- gaussian-process
stage: expert
status: validated
---

# The Ornstein-Uhlenbeck Process

## Core Idea
The Ornstein-Uhlenbeck (OU) process solves dX = -θX dt + σ dW, where θ > 0 controls the rate of mean reversion. Its explicit solution X(t) = X(0)e^{-θt} + σ∫₀ᵗ e^{-θ(t-s)} dW(s) is Gaussian with mean X(0)e^{-θt} and variance (σ²/2θ)(1 - e^{-2θt}). As t → ∞, the process converges to a stationary Gaussian distribution N(0, σ²/2θ). The OU process is the prototypical mean-reverting diffusion and the only stationary Gaussian Markov process.

## Questions

```yaml
- question: "The Ornstein-Uhlenbeck process dX = -θX dt + σ dW is solved using the integrating factor e^{θt}. What is the explicit solution?"
  type: multiple-choice
  options:
    - "X(t) = X(0)e^{θt} + σ∫₀ᵗ e^{θ(t-s)} dW(s)"
    - "X(t) = X(0)e^{-θt} + σ∫₀ᵗ e^{-θ(t-s)} dW(s)"
    - "X(t) = X(0) + σW(t) - θ∫₀ᵗ X(s)ds"
    - "X(t) = X(0)e^{-θt} + σW(t)"
  answer: 1
  explanation: "Apply Itô's formula to Y(t) = X(t)e^{θt}: dY = e^{θt}(dX + θX dt) = e^{θt}(σ dW) = σe^{θt} dW. Integrating: Y(t) = Y(0) + σ∫₀ᵗ e^{θs} dW(s), so X(t) = e^{-θt}Y(t) = X(0)e^{-θt} + σ∫₀ᵗ e^{-θ(t-s)} dW(s). The exponential decay e^{-θt} on the initial condition shows mean reversion; the integral term is a weighted average of past noise with exponentially decaying weights — recent noise matters more than distant noise."

- question: "The stationary variance of the OU process is σ²/(2θ). If θ is doubled (faster mean reversion) while σ stays constant, the stationary variance:"
  type: multiple-choice
  options:
    - "Doubles — faster mean reversion increases fluctuations"
    - "Halves — faster mean reversion pulls the process back more quickly, reducing the spread"
    - "Stays the same — variance depends only on σ"
    - "Quadruples — variance is proportional to θ²"
  answer: 1
  explanation: "The stationary variance σ²/(2θ) is inversely proportional to θ. Stronger mean reversion (larger θ) gives the process less time to wander before being pulled back, reducing the equilibrium variance. This matches physical intuition: a stiffer spring (larger θ) produces smaller oscillations for the same noise level (σ). The balance between noise injection (σ) and restoring force (θ) determines the equilibrium spread."

- question: "Explain why the Ornstein-Uhlenbeck process is the unique stationary Gaussian Markov process (up to affine transformation)."
  type: short-answer
  answer: "A stationary Gaussian Markov process must have an exponentially decaying autocorrelation R(τ) = ce^{-θ|τ|} — Markov demands that the autocorrelation satisfy R(s+t) = R(s)R(t)/R(0) (the Chapman-Kolmogorov condition for Gaussians), and the only continuous solution is exponential. A Gaussian process is fully determined by its mean and covariance, so the stationary distribution and the exponential autocorrelation uniquely determine the process as the OU process. No other diffusion has all three properties simultaneously: Gaussian marginals, the Markov property, and stationarity."
  explanation: "Brownian motion is Gaussian and Markov but not stationary (its variance grows with time). A stationary Gaussian process with non-exponential autocorrelation (like a squared-exponential kernel) loses the Markov property. The OU process sits at the unique intersection of these three properties, making it the natural continuous-time analogue of an AR(1) process."
```

## Explainer

The **Ornstein-Uhlenbeck process** is the simplest non-trivial SDE with an explicit solution and a non-degenerate stationary distribution. It satisfies dX = -θX dt + σ dW, where the drift -θX acts as a restoring force pulling the process toward zero. When X is positive, the drift is negative (pushing down); when X is negative, the drift is positive (pushing up). This is mean reversion — the continuous-time analogue of a discrete-time AR(1) process with coefficient e^{-θ}.

The solution technique uses an integrating factor, paralleling the method for linear ODEs. Define Y(t) = X(t)e^{θt}. By Itô's formula, dY = e^{θt}(dX + θX dt) = e^{θt}σ dW. This is a pure Itô integral with no drift, so Y(t) = X(0) + σ∫₀ᵗ e^{θs} dW(s). Multiplying by e^{-θt} gives the explicit solution: X(t) = X(0)e^{-θt} + σ∫₀ᵗ e^{-θ(t-s)} dW(s). Since this is a deterministic function of Gaussian random variables (the Itô integral of a deterministic function is Gaussian), X(t) is Gaussian with mean E[X(t)] = X(0)e^{-θt} and variance Var(X(t)) = σ²∫₀ᵗ e^{-2θ(t-s)} ds = (σ²/2θ)(1 - e^{-2θt}).

As t → ∞, the mean decays to zero and the variance converges to σ²/(2θ). The process forgets its initial condition exponentially fast (at rate θ) and settles into a stationary Gaussian distribution N(0, σ²/(2θ)). The autocorrelation of the stationary process is R(τ) = (σ²/2θ)e^{-θ|τ|} — exponentially decaying with correlation time 1/θ. This is a fundamental model in physics (velocity of a Brownian particle under friction, by Uhlenbeck and Ornstein's original 1930 paper), finance (the Vasicek interest rate model), and biology (fluctuations around a homeostatic set point).

The OU process occupies a special place in the taxonomy of stochastic processes: it is the **unique** continuous-time process that is simultaneously Gaussian, Markov, and stationary. Brownian motion is Gaussian and Markov but not stationary (variance grows). A stationary Gaussian process with a non-exponential covariance function loses the Markov property. The exponential covariance is the only one compatible with all three properties, and this pins down the OU process uniquely (up to location and scale parameters). This characterization theorem explains why the OU process appears as the natural building block in so many contexts.
