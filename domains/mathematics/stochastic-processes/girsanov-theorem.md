---
id: girsanov-theorem
title: Girsanov Theorem
domain: mathematics
course: stochastic-processes
prerequisites:
- id: stochastic-differential-equations
  type: hard
- id: martingales-introduction
  type: hard
- id: radon-nikodym-theorem
  type: soft
tags:
- girsanov
- change-of-measure
- risk-neutral
- equivalent-measures
stage: expert
status: validated
---

# Girsanov Theorem

## Core Idea
Girsanov's theorem describes how Brownian motion transforms under a change of probability measure. If W is a Brownian motion under P and we define a new measure Q via the Radon-Nikodym derivative dQ/dP = exp(-∫θ dW - (1/2)∫θ² dt), then W̃(t) = W(t) + ∫₀ᵗ θ(s) ds is a Brownian motion under Q. This allows removing or adding drift: a process with drift under one measure becomes driftless under another. It is the mathematical foundation of risk-neutral pricing in finance.

## Questions

```yaml
- question: "Under measure P, the process X(t) satisfies dX = μ dt + σ dW where W is a P-Brownian motion. Using Girsanov's theorem with θ = μ/σ, under the new measure Q:"
  type: multiple-choice
  options:
    - "X(t) satisfies dX = 2μ dt + σ dW̃ — the drift doubles"
    - "X(t) satisfies dX = σ dW̃ — the drift is absorbed into the new Brownian motion W̃"
    - "X(t) satisfies dX = μ dt + σ dW̃ — only the Brownian motion changes, not the drift"
    - "X(t) becomes deterministic under Q"
  answer: 1
  explanation: "With θ = μ/σ, Girsanov's theorem says W̃(t) = W(t) + (μ/σ)t is a Q-Brownian motion. Rewriting: W(t) = W̃(t) - (μ/σ)t. Substituting into dX: dX = μ dt + σ(dW̃ - (μ/σ)dt) = μ dt + σ dW̃ - μ dt = σ dW̃. The drift μ dt has been completely absorbed. Under Q, X is a driftless diffusion — a scaled Brownian motion. This is the core mechanism of risk-neutral pricing: the real-world drift μ of a stock becomes the risk-free rate r after the appropriate change of measure."

- question: "The Novikov condition E_P[exp((1/2)∫₀ᵀ θ²(t) dt)] < ∞ is a sufficient condition for:"
  type: multiple-choice
  options:
    - "The SDE dX = θX dt + dW to have a unique solution"
    - "The exponential local martingale Z(t) = exp(-∫₀ᵗ θ dW - (1/2)∫₀ᵗ θ² ds) to be a true martingale, ensuring the Girsanov change of measure is valid"
    - "The process W̃(t) to have independent increments under P"
    - "The drift θ(t) to be bounded almost surely"
  answer: 1
  explanation: "The Girsanov density Z(t) = exp(-∫θ dW - (1/2)∫θ² ds) is always a non-negative local martingale, hence a supermartingale with E[Z(t)] ≤ 1. For Girsanov's theorem to work, Z must be a true martingale (E[Z(T)] = 1), so that dQ = Z(T) dP defines a genuine probability measure. Novikov's condition provides the sufficient integrability to upgrade the local martingale to a true martingale. Without it, the 'measure' Q might have total mass less than 1 and fail to be a probability measure."

- question: "Explain why Girsanov's theorem does not allow you to change a Brownian motion into a deterministic process, even though it can remove drift."
  type: short-answer
  answer: "Girsanov's theorem changes the drift of a process but not its diffusion coefficient. Under any equivalent measure Q, the quadratic variation of the process is unchanged ([X,X]_t is the same under P and Q), so the noise σ dW̃ persists — only its distribution relative to the new Brownian motion W̃ is reinterpreted. Removing drift converts X from 'Brownian motion plus drift' to 'Brownian motion,' not to a constant. To make the process deterministic, you would need to eliminate the diffusion coefficient σ, which no absolutely continuous change of measure can do — singular measures (with dQ/dP = 0 on some events) would be required."
  explanation: "This reflects a deep principle: equivalent probability measures (P ~ Q with dQ/dP > 0 a.s.) agree on which events have probability zero. A Brownian path is almost surely non-differentiable under P, and this remains true under any equivalent Q. You can change what looks like drift but not the fundamental roughness of the paths."
```

## Explainer

**Girsanov's theorem** answers a remarkable question: if you change the probability measure on a probability space, what happens to the Brownian motion? The answer is that it acquires (or loses) a drift. Specifically, if W is a standard Brownian motion under probability measure P, and we define a new measure Q by the Radon-Nikodym derivative dQ/dP = Z(T), where Z(t) = exp(-∫₀ᵗ θ(s) dW(s) - (1/2)∫₀ᵗ θ(s)² ds) is the exponential martingale, then the process W̃(t) = W(t) + ∫₀ᵗ θ(s) ds is a standard Brownian motion under Q.

The exponential Z(t) is called the **Girsanov density** or **likelihood ratio process**. Your prerequisite on the Radon-Nikodym theorem ensures you understand what dQ/dP means: it is a non-negative measurable function that converts P-expectations to Q-expectations via E_Q[X] = E_P[Z·X]. The Novikov condition E_P[exp((1/2)∫₀ᵀ θ² dt)] < ∞ is the standard sufficient condition ensuring Z is a true martingale (E_P[Z(T)] = 1), so that Q is a genuine probability measure equivalent to P. Without this condition, Z could be a strict supermartingale with E[Z(T)] < 1, and Q would assign total mass less than 1 — a defective measure.

The practical power of Girsanov's theorem is **drift removal**. If under P we have dX = μ(t)dt + σ(t)dW, we can choose θ = μ/σ and switch to a measure Q under which dX = σ dW̃ — the drift has been absorbed into the new Brownian motion. This is the mathematical content of **risk-neutral pricing** in finance: under the real-world measure P, a stock has drift μ (its expected return). Under the risk-neutral measure Q (constructed via Girsanov with θ = (μ-r)/σ, where r is the risk-free rate), the stock has drift r. Option prices are expectations under Q, not P — Girsanov's theorem is the bridge between the physical and risk-neutral worlds.

A critical limitation: Girsanov's theorem changes drift but **not volatility**. The quadratic variation [X,X]_t is the same under both P and Q because equivalent measures agree on null sets, and quadratic variation is determined pathwise. This means the "roughness" of sample paths is an absolute property — no change of measure can smooth Brownian motion or eliminate diffusion. Drift is a statistical property (it determines which direction the process tends to go), while volatility is a pathwise property (it determines how rough the paths are). Girsanov lets you manipulate the former while the latter remains invariant.
