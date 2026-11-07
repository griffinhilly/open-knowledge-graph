---
id: geometric-brownian-motion
title: Geometric Brownian Motion
domain: mathematics
course: stochastic-processes
prerequisites:
- id: stochastic-differential-equations
  type: hard
- id: itos-formula
  type: hard
tags:
- geometric-brownian-motion
- lognormal
- black-scholes
- finance
stage: expert
status: validated
---

# Geometric Brownian Motion

## Core Idea
Geometric Brownian motion (GBM) solves dS = μS dt + σS dW, where both drift and diffusion are proportional to the current value S. Applying Itô's formula to ln(S) reveals that log-returns are normally distributed: ln(S(t)/S(0)) = (μ - σ²/2)t + σW(t), so S(t) = S(0)exp((μ - σ²/2)t + σW(t)). The solution is always positive, lognormally distributed, and is the standard model for stock prices in mathematical finance — the foundation of Black-Scholes theory.

## How It's Best Learned
Derive d(ln S) with Itô's formula once by hand, then test the result by simulation. Take μ = 0.04 and σ = 0.4, so μ - σ²/2 = -0.04. Simulate many paths from S(0) = 1 to T = 10 and compare the sample mean, near e^{0.4} ≈ 1.49, with the sample median, near e^{-0.4} ≈ 0.67. The mean rises while the typical path falls.

## Common Misconceptions
- A positive drift μ means a typical path grows. (The median grows at rate μ - σ²/2, which is negative whenever σ² > 2μ, even though E[S(t)] = S(0)e^{μt} rises.)
- The logarithm of S has drift μ. (Itô's formula gives d(ln S) = (μ - σ²/2)dt + σ dW; the -σ²/2 comes from the second-order term.)
- Under GBM the simple return S(t)/S(0) - 1 is normally distributed. (The log-return is normal; the simple return is a shifted lognormal, skewed to the right and bounded below by -1.)

## Questions

```yaml
- question: "In the GBM solution S(t) = S(0)exp((μ - σ²/2)t + σW(t)), the drift of ln(S) is μ - σ²/2, not μ. Where does the -σ²/2 come from?"
  type: multiple-choice
  options:
    - "It is a discretization error from converting continuous to discrete time"
    - "It is the Itô correction: applying Itô's formula to ln(S) with dS = μS dt + σS dW produces d(ln S) = (μ - σ²/2)dt + σ dW"
    - "It compensates for the fact that geometric means are smaller than arithmetic means"
    - "It ensures the process remains positive"
  answer: 1
  explanation: "Apply Itô's formula to f(S) = ln(S) with f'(S) = 1/S and f''(S) = -1/S². Then d(ln S) = (1/S)(μS dt + σS dW) + (1/2)(-1/S²)(σS)² dt = (μ - σ²/2)dt + σ dW. The -σ²/2 is the Itô correction term (1/2)f''(S)(σS)² dt = -σ²/2 dt. While option C is heuristically related (Jensen's inequality for the concave log function), the precise source is Itô's formula."

- question: "S(t) follows GBM with μ = 0.10 and σ = 0.30. The expected value E[S(t)] grows at rate:"
  type: multiple-choice
  options:
    - "μ - σ²/2 = 0.055, the drift of ln(S)"
    - "μ = 0.10, because E[S(t)] = S(0)e^{μt} regardless of σ"
    - "μ + σ²/2 = 0.145, because volatility increases the expected level"
    - "σ² = 0.09, because in GBM the variance dominates the growth"
  answer: 1
  explanation: "E[S(t)] = S(0)E[exp((μ-σ²/2)t + σW(t))] = S(0)exp(μt), using the moment generating function of the normal distribution: E[e^{aW(t)}] = e^{a²t/2}. The (μ-σ²/2) in the exponent is the growth rate of the median (and the geometric mean), but the expected value grows at rate μ because the lognormal distribution's right tail contributes extra. This distinction between median growth (μ-σ²/2) and mean growth (μ) is a consequence of Jensen's inequality applied to the convex exponential function."

- question: "Geometric Brownian motion can take negative values if the initial condition S(0) > 0, provided σ is large enough and enough time passes."
  type: true-false
  answer: false
  explanation: "S(t) = S(0)exp((μ-σ²/2)t + σW(t)) is the exponential of a real number, which is always strictly positive. If S(0) > 0, then S(t) > 0 for all t almost surely, regardless of μ or σ. This positivity is a key property that makes GBM suitable for modeling quantities like stock prices or populations that cannot go negative. The process can get arbitrarily close to zero but never reaches or crosses it."

- question: "Explain why geometric Brownian motion, despite its widespread use, is a flawed model for real stock prices."
  type: short-answer
  answer: "GBM assumes constant volatility σ and drift μ, producing returns that are i.i.d. normal. Real stock returns exhibit volatility clustering (periods of high and low volatility), heavy tails (extreme moves more frequent than the normal distribution predicts), mean reversion in volatility, and leverage effects (negative correlation between returns and volatility changes). GBM also cannot produce jumps — sudden large price moves observed in real markets. More realistic models include stochastic volatility (Heston), jump-diffusion (Merton), and local volatility models."
  explanation: "GBM is the 'spherical cow' of finance — an idealization that captures the essential features (positivity, multiplicative growth, randomness) while missing second-order effects. Its value is as a tractable baseline that admits closed-form solutions (Black-Scholes), not as a precise description of reality."
```

## Explainer

**Geometric Brownian motion** is the multiplicative analogue of Brownian motion. Where Brownian motion adds random increments (dX = σ dW), GBM multiplies by random factors (dS/S = μ dt + σ dW, or equivalently dS = μS dt + σS dW). The proportionality of both drift and diffusion to the current level S means that percentage changes, not absolute changes, are the natural unit — a 1% move when S = 100 is a 1% move when S = 1000. This multiplicative structure is why GBM is the default model for prices, populations, and other quantities that grow proportionally.

Solving the SDE requires Itô's formula. Apply f(x) = ln(x) to S: d(ln S) = (1/S)dS + (1/2)(-1/S²)(dS)² = (μ - σ²/2)dt + σ dW. The Itô correction subtracts σ²/2 from the drift — a critical detail. Integrating: ln(S(t)) - ln(S(0)) = (μ - σ²/2)t + σW(t), so S(t) = S(0)exp((μ - σ²/2)t + σW(t)). Since W(t) ~ N(0,t), the log-return ln(S(t)/S(0)) is normally distributed, and S(t) itself is **lognormally distributed** with E[S(t)] = S(0)e^{μt} and Var(S(t)) = S(0)²e^{2μt}(e^{σ²t} - 1).

A subtle but important distinction: the **median** of S(t) is S(0)exp((μ - σ²/2)t), growing at rate μ - σ²/2, while the **mean** E[S(t)] = S(0)e^{μt} grows at the faster rate μ. The gap σ²/2 is a Jensen's inequality effect — the convexity of the exponential function means the average of e^X exceeds e^{average of X}. When σ is large, the median can decrease even as the mean increases. This has practical implications: a "typical" sample path of GBM grows slower than the expected value suggests, because the mean is pulled up by rare but extreme positive outcomes.

In mathematical finance, GBM is the foundation of the **Black-Scholes model**. Under the risk-neutral measure (obtained via Girsanov's theorem), the stock price follows dS = rS dt + σS dW̃ where r is the risk-free rate. The explicit lognormal distribution of S(T) allows closed-form pricing of European options: the Black-Scholes formula is a direct consequence of computing E[max(S(T) - K, 0)] under this lognormal distribution. While GBM's assumptions (constant μ, σ, no jumps, normal log-returns) are violated by real market data, its tractability and the intuitions it provides make it the essential starting point for all of quantitative finance.
