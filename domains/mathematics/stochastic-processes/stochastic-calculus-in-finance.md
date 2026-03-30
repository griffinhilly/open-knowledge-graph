---
id: stochastic-calculus-in-finance
title: Stochastic Calculus Applications in Finance
domain: mathematics
course: stochastic-processes
prerequisites:
- id: geometric-brownian-motion
  type: hard
- id: girsanov-theorem
  type: hard
- id: martingale-representation-theorem
  type: hard
- id: feynman-kac-formula
  type: soft
tags:
- mathematical-finance
- black-scholes
- option-pricing
- risk-neutral-pricing
stage: expert
status: validated
---

# Stochastic Calculus Applications in Finance

## Core Idea
Mathematical finance applies stochastic calculus to price and hedge financial derivatives. The fundamental theorem of asset pricing connects arbitrage-freeness to the existence of an equivalent martingale measure, and market completeness to its uniqueness. Under the Black-Scholes model, Girsanov's theorem constructs the risk-neutral measure, the martingale representation theorem provides the hedging strategy, and the Feynman-Kac formula connects risk-neutral expectations to the Black-Scholes PDE.

## Questions

```yaml
- question: "The first fundamental theorem of asset pricing states that a market is arbitrage-free if and only if:"
  type: multiple-choice
  options:
    - "The stock price follows geometric Brownian motion"
    - "There exists an equivalent probability measure Q under which all discounted asset prices are martingales"
    - "The expected return of every asset equals the risk-free rate"
    - "The market contains at least as many tradeable assets as sources of randomness"
  answer: 1
  explanation: "The first FTAP (Harrison-Pliska theorem) establishes a deep equivalence: no-arbitrage is equivalent to the existence of an equivalent martingale measure (EMM) Q. Under Q, discounted asset prices are martingales — their expected returns equal the risk-free rate. Option C is a consequence of Q existing (under Q, expected returns are r), not the theorem itself. Option D relates to the second FTAP (completeness). The theorem is remarkable because it translates an economic condition (no free lunch) into a mathematical condition (existence of a measure)."

- question: "In the Black-Scholes model, a European call option with strike K and maturity T has price C = S₀Φ(d₁) − Ke^{-rT}Φ(d₂). The term Φ(d₂) represents:"
  type: multiple-choice
  options:
    - "The probability that the option expires in the money under the risk-neutral measure Q"
    - "The probability that the stock price exceeds K at maturity under the physical measure P"
    - "The delta of the option (number of shares in the replicating portfolio)"
    - "The expected payoff of the option, discounted at the risk-free rate"
  answer: 0
  explanation: "Under Q, ln(S_T) ~ N(ln S₀ + (r-σ²/2)T, σ²T), so Q(S_T > K) = Φ(d₂) where d₂ = (ln(S₀/K) + (r-σ²/2)T)/(σ√T). The term Ke^{-rT}Φ(d₂) is the present value of the strike times the exercise probability. The term S₀Φ(d₁) involves d₁ = d₂ + σ√T and represents E_Q[S_T · 1_{S_T>K}] discounted — the delta Φ(d₁) is the number of shares in the replicating portfolio (option C is close but refers to d₁, not d₂)."

- question: "Explain why the Black-Scholes option price does not depend on the stock's expected return μ."
  type: short-answer
  answer: "The option price is an expectation under the risk-neutral measure Q, not the physical measure P. Girsanov's theorem removes the physical drift μ and replaces it with the risk-free rate r. Under Q, dS = rS dt + σS dW̃ — the stock grows at rate r regardless of its real-world expected return. The reason μ drops out is the no-arbitrage argument: the option can be perfectly replicated by delta-hedging, and the hedging strategy's cost depends only on σ (which determines the hedging adjustments) and r (the financing cost), not on where the stock is expected to go. Two stocks with the same σ but different μ have the same option price."
  explanation: "This is one of the deepest insights of Black-Scholes theory. Risk preferences are irrelevant for derivative pricing (risk-neutral valuation) — you price options as if everyone were risk-neutral, even though they aren't. The physical drift μ affects the stock's expected return but not the cost of replicating the option, because the replicating portfolio is continuously adjusted to be instantaneously riskless."

- question: "The Black-Scholes model assumes constant volatility σ. In practice, implied volatilities vary across strikes and maturities (the 'volatility smile'). This empirical fact:"
  type: true-false
  answer: true
  explanation: "The volatility smile/skew is one of the most well-documented departures from Black-Scholes. If the model were correct, all options on the same stock would produce the same implied volatility when inverted through the Black-Scholes formula. Instead, out-of-the-money puts typically have higher implied volatility than at-the-money options (the 'skew'), reflecting the market's pricing of tail risk and jump risk that GBM cannot capture. This motivates extensions: local volatility (Dupire), stochastic volatility (Heston), and jump-diffusion (Merton) models."
```

## Explainer

**Mathematical finance** is the most prominent application of stochastic calculus. The central problem is pricing and hedging derivatives — financial contracts whose value depends on the evolution of an underlying asset. The Black-Scholes framework, built on geometric Brownian motion and Itô calculus, provides the theoretical foundation. The key insight is that in a complete market, every derivative can be replicated by dynamically trading the underlying asset and a risk-free bond, and the replication cost determines the derivative's price.

The **fundamental theorems of asset pricing** are the theoretical pillars. The first FTAP states that a market is arbitrage-free if and only if there exists an equivalent martingale measure (EMM) Q under which all discounted asset prices are martingales. The second FTAP states that the market is complete (every contingent claim is attainable) if and only if the EMM is unique. In the Black-Scholes model (one stock, one Brownian motion), Girsanov's theorem constructs the unique EMM by setting θ = (μ-r)/σ and defining Q via the Girsanov density. Under Q, the stock satisfies dS = rS dt + σS dW̃ — the physical drift μ is replaced by the risk-free rate r.

The **Black-Scholes formula** C = S₀Φ(d₁) - Ke^{-rT}Φ(d₂) for a European call with strike K and maturity T follows from computing E_Q[e^{-rT}max(S_T - K, 0)]. Since S_T is lognormally distributed under Q (from GBM with drift r), this is a direct calculation. The same result can be derived via the **Black-Scholes PDE** ∂V/∂t + rS(∂V/∂S) + (1/2)σ²S²(∂²V/∂S²) = rV, which is obtained by constructing the delta-hedging portfolio and eliminating risk. The Feynman-Kac formula provides the bridge: the PDE solution equals the risk-neutral expectation.

The **replicating portfolio** is constructed via the martingale representation theorem. The discounted option price V(t)e^{-rt} is a Q-martingale adapted to the Brownian filtration, so by the MRT, V(t)e^{-rt} = V(0) + ∫₀ᵗ H(s) dW̃(s). Converting to the stock numeraire: hold Δ(t) = ∂V/∂S shares of stock and invest the remainder in bonds. This delta-hedging strategy replicates the option payoff exactly — it is self-financing, and at maturity the portfolio value equals max(S_T - K, 0). The strategy's existence (guaranteed by the MRT) is what justifies using the risk-neutral expectation as the price. Without a replication argument, the expectation under Q would be just one possible price among many.
