---
id: ito-integral
title: The Itô Integral
domain: mathematics
course: stochastic-processes
prerequisites:
- id: properties-of-brownian-motion
  type: hard
- id: martingales-introduction
  type: hard
- id: lp-spaces
  type: soft
tags:
- ito-integral
- stochastic-calculus
- stochastic-integration
stage: expert
status: validated
---

# The Itô Integral

## Core Idea
The Itô integral ∫₀ᵀ H(t) dW(t) extends integration to allow Brownian motion as the integrator. Because Brownian paths have infinite variation, Riemann-Stieltjes integration fails, and the integral must be constructed as an L² limit of integrals of simple (step) processes. The key choice is evaluating the integrand at the left endpoint of each subinterval, which produces an integral that is a martingale with zero expectation and the Itô isometry E[(∫H dW)²] = E[∫H² dt].

## Questions

```yaml
- question: "Why can't the Itô integral ∫₀ᵀ H(t) dW(t) be defined as a pathwise Riemann-Stieltjes integral?"
  type: multiple-choice
  options:
    - "Because W(t) is not measurable with respect to the Borel sigma-algebra"
    - "Because the Riemann-Stieltjes integral ∫f dg requires g to have bounded variation, but Brownian paths have infinite variation on every interval"
    - "Because H(t) may be negative, and Riemann-Stieltjes integration only works for positive integrands"
    - "Because Brownian motion is not continuous, and Riemann-Stieltjes requires continuity of the integrator"
  answer: 1
  explanation: "The Riemann-Stieltjes integral ∫f dg is well-defined when g has bounded (finite) variation. Brownian paths are almost surely of infinite variation on every interval, so the classical construction breaks down — the approximating sums don't converge. Itô's construction bypasses this by defining the integral as an L² limit: first for simple (step function) integrands where the integral is just a finite sum, then extending by density to the closure in L². The resulting integral is fundamentally a probabilistic object, not a pathwise one."

- question: "The Itô integral ∫₀ᵀ W(t) dW(t) equals (1/2)W(T)² − (1/2)T, not (1/2)W(T)² as ordinary calculus would suggest. The extra −(1/2)T term arises because:"
  type: multiple-choice
  options:
    - "The Itô integral uses left-endpoint evaluation, which introduces a systematic bias equal to half the quadratic variation"
    - "Brownian motion has negative drift that accumulates over time"
    - "The integral is computed incorrectly; the true answer is (1/2)W(T)²"
    - "The factor −(1/2)T is a normalization constant required to make the integral a martingale"
  answer: 0
  explanation: "Left-endpoint evaluation means the integrand is evaluated at tᵢ₋₁, not at the midpoint or right endpoint. In the Riemann sum Σ W(tᵢ₋₁)(W(tᵢ) - W(tᵢ₋₁)), expanding W(tᵢ) = W(tᵢ₋₁) + ΔWᵢ and using the fact that Σ(ΔWᵢ)² → T (quadratic variation) produces the correction term −T/2. If we used midpoint evaluation (Stratonovich convention), the correction disappears and we get (1/2)W(T)². The Itô choice is preferred in probability because it makes the integral a martingale — E[∫₀ᵀ W dW] = 0 — which is essential for stochastic analysis."

- question: "The Itô isometry states that E[(∫₀ᵀ H(t) dW(t))²] = E[∫₀ᵀ H(t)² dt]. In your own words, explain why this is the fundamental computational tool for Itô integrals."
  type: short-answer
  answer: "The Itô isometry converts a question about the variance of a stochastic integral (an L² norm in probability space) into an ordinary Lebesgue integral of H² over time. This means you can compute second moments of Itô integrals without working with the Brownian integrator directly — you just integrate the square of the integrand against dt. It also shows that the Itô integral is an isometry from L²(Ω × [0,T]) to L²(Ω), which is what allows the extension from simple processes to general adapted processes by L² approximation. Without it, the construction of the integral would not close."
  explanation: "The isometry E[(∫H dW)²] = E[∫H² dt] is a direct consequence of independent increments: cross-terms E[H(tᵢ)ΔWᵢ · H(tⱼ)ΔWⱼ] vanish for i ≠ j because ΔWⱼ is independent of everything up to time tⱼ₋₁. Only the diagonal terms survive, giving Σ E[H(tᵢ)²] · (tᵢ₊₁ - tᵢ), which in the limit is E[∫H² dt]. This structural feature — that the L² norm of the stochastic integral depends only on the integrand — is the foundation of everything that follows."

- question: "Every Itô integral ∫₀ᵗ H(s) dW(s), where H is adapted and square-integrable, is a martingale."
  type: true-false
  answer: true
  explanation: "The martingale property of Itô integrals follows from left-endpoint evaluation: H(s) is adapted (known at time s), and dW(s) is independent of the filtration up to time s. This means E[H(s)dW(s) | ℱₛ] = H(s)E[dW(s)] = 0, so the integral has zero expected increment at every time. The martingale property is one of the main reasons the Itô convention is preferred over the Stratonovich convention in probability theory — it preserves the 'fair game' structure that makes martingale techniques available."
```

## Explainer

Classical integration theory — whether Riemann or Lebesgue — integrates functions against smooth or bounded-variation integrators. Brownian motion has infinite variation on every interval, so these tools fail. The **Itô integral** resolves this by constructing ∫₀ᵀ H(t) dW(t) as an L² limit rather than a pathwise limit. The construction proceeds in three steps: define the integral for simple (step function) processes as a finite sum Σ Hᵢ(W(tᵢ₊₁) - W(tᵢ)), prove the Itô isometry for these simple integrals, then extend to general adapted square-integrable processes by approximation in L².

The critical design choice is **left-endpoint evaluation**: the integrand H is evaluated at the left endpoint tᵢ of each subinterval [tᵢ, tᵢ₊₁], not at the midpoint or right endpoint. This is not arbitrary — it ensures that H(tᵢ) is known (adapted to ℱ_{tᵢ}) before the increment W(tᵢ₊₁) - W(tᵢ) is realized. The consequence is that the Itô integral is a **martingale**: E[∫₀ᵗ H dW | ℱₛ] = ∫₀ˢ H dW for s ≤ t. The integrand is "decided" before the randomness arrives, so no information about the future leaks in. The Stratonovich convention (midpoint evaluation) produces a different integral that satisfies the ordinary chain rule but is not a martingale — the Itô convention sacrifices the classical chain rule to gain the martingale property, a trade that turns out to be enormously profitable.

The **Itô isometry** E[(∫₀ᵀ H dW)²] = E[∫₀ᵀ H² dt] is the engine of the construction. It says the L² norm of the stochastic integral equals the L² norm of the integrand computed against ordinary Lebesgue measure. The proof is elegant: expand the square of the Riemann sum and observe that cross-terms vanish by independence of increments, leaving only diagonal terms. This isometry makes the map H ↦ ∫H dW a bounded linear operator from L²(Ω × [0,T]) to L²(Ω), and bounded linear operators on Hilbert spaces extend uniquely and continuously to the closure — completing the construction.

The price of left-endpoint evaluation appears immediately in the simplest example. Computing ∫₀ᵀ W(t) dW(t) from the Riemann sum Σ W(tᵢ)(W(tᵢ₊₁) - W(tᵢ)) and using the identity ab = (1/2)((a+b)² - a² - b²) yields (1/2)W(T)² - (1/2)Σ(ΔWᵢ)². The sum of squared increments converges to T (the quadratic variation), giving ∫₀ᵀ W dW = (1/2)W(T)² - (1/2)T. The "-T/2" correction is the signature of Itô calculus — it is absent in Stratonovich calculus and absent in ordinary calculus. This correction generalizes to Itô's formula, the chain rule of stochastic calculus, which is the next topic.
