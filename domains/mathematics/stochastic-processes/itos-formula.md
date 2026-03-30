---
id: itos-formula
title: "Itô's Formula (Itô's Lemma)"
domain: mathematics
course: stochastic-processes
prerequisites:
- id: ito-integral
  type: hard
- id: properties-of-brownian-motion
  type: hard
tags:
- ito-formula
- ito-lemma
- stochastic-calculus
- chain-rule
stage: expert
status: validated
---

# Itô's Formula (Itô's Lemma)

## Core Idea
Itô's formula is the chain rule of stochastic calculus: for a C² function f and a process X(t) = X(0) + ∫μ ds + ∫σ dW, we have df(X) = f'(X)dX + (1/2)f''(X)σ²dt. The extra second-order term (1/2)f''σ²dt arises because (dW)² = dt — the non-zero quadratic variation of Brownian motion prevents the second-order Taylor term from vanishing as it does in classical calculus. This formula is the single most used tool in stochastic calculus.

## Questions

```yaml
- question: "Apply Itô's formula to f(x) = x² with X(t) = W(t) (standard Brownian motion). What is d(W²)?"
  type: multiple-choice
  options:
    - "2W(t) dW(t), exactly as the classical chain rule gives"
    - "2W(t) dW(t) + dt, because the Itô correction term (1/2)f''(W)(dW)² = (1/2)(2)(dt) = dt"
    - "W²(t) dt + 2W(t) dW(t)"
    - "2W(t) dW(t) − dt"
  answer: 1
  explanation: "With f(x) = x², we have f'(x) = 2x and f''(x) = 2. Itô's formula gives df(W) = f'(W)dW + (1/2)f''(W)(dW)² = 2W dW + (1/2)(2)(dt) = 2W dW + dt. Integrating both sides recovers the earlier result: W(T)² = 2∫₀ᵀ W dW + T, or equivalently ∫₀ᵀ W dW = (W(T)² - T)/2. The +dt correction is the hallmark of Itô calculus — it is absent from the classical chain rule because smooth functions have zero quadratic variation."

- question: "Itô's formula applied to f(x) = eˣ with dX = μ dt + σ dW gives d(eˣ) = eˣ(μ + σ²/2)dt + eˣσ dW. The μ + σ²/2 drift — larger than the naive μ — is sometimes called:"
  type: multiple-choice
  options:
    - "The Girsanov correction"
    - "The convexity adjustment (or Jensen's inequality effect), reflecting that the exponential's curvature amplifies volatility into drift"
    - "The risk-neutral drift"
    - "The martingale compensation"
  answer: 1
  explanation: "For a convex function like eˣ, the average of the function exceeds the function of the average (Jensen's inequality). In continuous time, this manifests as the (1/2)f''σ² = (1/2)eˣσ² term in Itô's formula. The exponential curves upward, so random fluctuations (volatility) systematically push the expected value of eˣ above what you'd predict from the drift μ alone. This σ²/2 'convexity adjustment' appears throughout mathematical finance — it is why the drift of geometric Brownian motion differs from what naive application of the chain rule would suggest."

- question: "A student claims that Itô's formula is just the ordinary chain rule with an error term added. Explain why this framing is misleading."
  type: short-answer
  answer: "Itô's formula is not an approximation to the classical chain rule with a correction — it is the exact chain rule for processes driven by Brownian motion. The 'extra' (1/2)f''σ²dt term arises naturally and necessarily from the Taylor expansion when (dW)² = dt rather than 0. In classical calculus, (dx)² = 0 because smooth paths have zero quadratic variation, so the second-order Taylor term vanishes. For Brownian motion, (dW)² = dt is a first-order quantity that contributes to the expansion at the same order as dW and dt. The formula is exact and complete — there is no error."
  explanation: "Calling the (1/2)f''σ²dt an 'error term' suggests it is small or negligible. It is neither — it is often the dominant effect. In geometric Brownian motion, the convexity adjustment σ²/2 determines whether the stock price grows faster or slower than the deterministic case. The correct framing is that the classical chain rule is the special case of Itô's formula when σ = 0 (no noise), not that Itô's formula is the classical rule plus noise."

- question: "Itô's formula requires the function f to be twice continuously differentiable (C²). This regularity condition cannot be relaxed."
  type: true-false
  answer: false
  explanation: "The C² condition is sufficient but not necessary. The Tanaka formula extends Itô's formula to the non-smooth function f(x) = |x|, which has a kink at x = 0 and no second derivative there. The result involves a local time term that captures the singular behavior at the non-differentiable point: d|W| = sgn(W)dW + dL₀(t), where L₀ is the local time at zero. More generally, Itô-Tanaka-Meyer formulas extend to convex functions and functions of bounded variation. The C² assumption is a clean starting point, but the theory extends well beyond it."
```

## Explainer

**Itô's formula** is to stochastic calculus what the chain rule is to ordinary calculus — it tells you how to compute df(X) when X is a stochastic process. But unlike the classical chain rule, the stochastic version has an extra term. If X(t) satisfies dX = μ(t)dt + σ(t)dW and f is C², then df(X) = f'(X)μ dt + f'(X)σ dW + (1/2)f''(X)σ² dt. The third term, (1/2)f''σ²dt, is the **Itô correction** — it is absent from classical calculus and arises entirely from the non-zero quadratic variation of Brownian motion.

The derivation follows from a second-order Taylor expansion: f(X + dX) ≈ f(X) + f'(X)dX + (1/2)f''(X)(dX)². In classical calculus, (dX)² is second-order infinitesimal and vanishes. But for stochastic processes, (dX)² = (μ dt + σ dW)² = σ²(dW)² + 2μσ(dt)(dW) + μ²(dt)². Using the multiplication rules dt·dt = 0, dt·dW = 0, and dW·dW = dt (the quadratic variation), only the σ²dt term survives. This is a rigorous consequence of the quadratic variation computation you studied in the previous topic: Σ(ΔWᵢ)² → T in L², so squared Brownian increments behave like dt at the infinitesimal level.

The formula's power lies in its ability to transform one stochastic differential equation into another. To analyze a complicated process Y(t) = f(X(t)), apply Itô's formula to find the SDE for Y directly. For example, if S follows geometric Brownian motion dS = μS dt + σS dW, then applying Itô's formula to f(S) = ln(S) gives d(ln S) = (μ - σ²/2)dt + σ dW. The logarithm converts the multiplicative SDE into an additive one with constant coefficients — immediately showing that ln S(T) is normally distributed and S(T) is lognormally distributed. This single computation underlies the Black-Scholes option pricing model.

The multidimensional version handles functions of several Itô processes simultaneously. If X₁, ..., Xₙ are Itô processes driven by possibly correlated Brownian motions, then for f(X₁, ..., Xₙ) the formula includes all partial derivatives ∂f/∂xᵢ (first order), all cross terms (1/2)∂²f/∂xᵢ∂xⱼ times the quadratic covariation d[Xᵢ, Xⱼ] (second order), and the time derivative ∂f/∂t if f depends explicitly on t. The structure is always the same: classical chain rule plus second-order corrections from quadratic (co)variation. Mastering this formula is the single most important skill in stochastic calculus.
