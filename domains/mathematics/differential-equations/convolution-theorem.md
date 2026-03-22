---
id: convolution-theorem
title: Convolution Theorem
domain: mathematics
course: differential-equations
prerequisites:
- id: solving-ivps-laplace-transform
  type: hard
- id: integration-by-parts
  type: soft
builds-toward:
- dirac-delta-function
tags:
- convolution
- product-rule
- inverse-transform
stage: formal-systems
status: draft
---

# Convolution Theorem

## Core Idea
The convolution of f and g is (f * g)(t) = ∫₀^t f(τ)g(t-τ)dτ. The convolution theorem states L[f * g] = F(s)G(s), so L^(-1)[F(s)G(s)] = (f * g)(t). This theorem is invaluable for solving non-homogeneous equations where the forcing function's transform is a product of simpler transforms, allowing you to decompose complex solutions into manageable parts.

## Questions

```yaml
- question: "You need to find ℒ⁻¹[1/(s(s+3))]. Recognizing F(s) = 1/s and G(s) = 1/(s+3), which approach correctly uses the convolution theorem?"
  type: multiple-choice
  options:
    - "Multiply the individual inverses: f(t)·g(t) = 1·e^{-3t} = e^{-3t}"
    - "Compute the convolution integral: ∫₀ᵗ e^{-3(t-τ)} dτ = (1 - e^{-3t})/3"
    - "Add the individual inverses: f(t) + g(t) = 1 + e^{-3t}"
    - "The theorem only applies when F(s) and G(s) have the same denominator"
  answer: 1
  explanation: "The convolution theorem states ℒ⁻¹[F(s)G(s)] = (f * g)(t) = ∫₀ᵗ f(τ)g(t-τ) dτ, not f(t)·g(t). With f(t) = 1 and g(t) = e^{-3t}, the convolution is ∫₀ᵗ 1·e^{-3(t-τ)} dτ = e^{-3t}∫₀ᵗ e^{3τ} dτ = e^{-3t}·[e^{3τ}/3]₀ᵗ = (1 - e^{-3t})/3. Option A is the most tempting error: the inverse Laplace transform distributes over addition but NOT over multiplication. You can verify the answer via partial fractions: 1/(s(s+3)) = (1/3)(1/s - 1/(s+3)), giving inverse (1 - e^{-3t})/3."

- question: "In the convolution integral y(t) = ∫₀ᵗ h(t-τ)g(τ) dτ describing a driven system, what is the physical meaning of h(t-τ)?"
  type: multiple-choice
  options:
    - "The current value of the forcing function at time t"
    - "The system's response to a unit impulse applied at time τ, evaluated at current time t"
    - "The transfer function evaluated at the frequency corresponding to time t"
    - "The average of the forcing function over the interval [0, t]"
  answer: 1
  explanation: "h(t-τ) is the impulse response of the system — how the system responds to a unit spike applied at time τ, observed at the current time t. The convolution integral accumulates these responses: each past input g(τ) contributes an impulse response h(t-τ) scaled by g(τ), and all contributions are summed. This reveals that the system's output at time t is a superposition of decaying responses to every past input — the system has 'memory' of all previous forcing."

- question: "If ℒ[f] = F(s) and ℒ[g] = G(s), then ℒ⁻¹[F(s)G(s)] = f(t)g(t)."
  type: true-false
  answer: false
  explanation: "This is the central misconception of the convolution theorem. The inverse Laplace transform distributes over addition: ℒ⁻¹[F(s) + G(s)] = f(t) + g(t). But it does NOT distribute over multiplication. The correct result is ℒ⁻¹[F(s)G(s)] = (f * g)(t) = ∫₀ᵗ f(τ)g(t-τ) dτ. Multiplication in the s-domain corresponds to convolution in the t-domain, not pointwise multiplication."

- question: "Convolution is commutative: (f * g)(t) = (g * f)(t) for all t ≥ 0."
  type: true-false
  answer: true
  explanation: "Since F(s)G(s) = G(s)F(s) in the s-domain, and the convolution theorem identifies ℒ⁻¹[F(s)G(s)] = (f * g)(t), commutativity follows from the commutativity of multiplication. It can also be verified directly by substituting u = t - τ in the integral: ∫₀ᵗ f(τ)g(t-τ) dτ = ∫₀ᵗ f(t-u)g(u) du = (g * f)(t)."

- question: "Explain why the convolution theorem is useful for inverting a Laplace transform of the form Y(s) = F(s)G(s), and what the alternative approach would be."
  type: short-answer
  answer: "When Y(s) factors as F(s)G(s) and both individual inverses f(t) and g(t) are known, the convolution theorem gives the inverse directly as the convolution integral ∫₀ᵗ f(τ)g(t-τ) dτ, without needing to algebraically combine F(s)G(s) into a form amenable to a table lookup. The alternative is partial fraction decomposition, which works when F(s)G(s) can be decomposed into simpler rational terms — but convolution is preferable when the forcing function is complicated or when the factored form already reveals physical structure (impulse response and input)."
  explanation: "Both approaches give the same answer, as the worked example in the Explainer confirms. The deeper value of convolution is conceptual: it shows that the output is a superposition of the system's impulse response over all past inputs, revealing causality and memory in the system's behavior. This interpretation is invisible when you just apply partial fractions and look up table entries."
```

## Explainer

From solving IVPs with the Laplace transform, you know the workflow: transform the ODE into an algebraic equation in s, solve for Y(s), then invert to find y(t). The bottleneck is often the inversion step. When Y(s) factors as a product F(s)·G(s) — two functions whose individual inverses you know — you might hope to recover y(t) by simply multiplying f(t)·g(t). This is wrong. The inverse Laplace transform does not distribute over multiplication the way it does over addition. The correct tool is **convolution**.

The **convolution** of two functions f and g is defined by (f * g)(t) = ∫₀ᵗ f(τ)g(t − τ) dτ. The variable τ slides across [0, t], with one function evaluated forward in time and the other evaluated backward. The integral accumulates how much f and g "overlap" as you shift one past the other. The **Convolution Theorem** says precisely: ℒ[f * g](s) = F(s)·G(s), or equivalently, ℒ⁻¹[F(s)·G(s)] = (f * g)(t). Multiplication in the s-domain corresponds to convolution in the t-domain.

As a concrete example, suppose you need ℒ⁻¹[1/(s(s + 2))]. You recognize F(s) = 1/s with f(t) = 1, and G(s) = 1/(s + 2) with g(t) = e^{−2t}. By the convolution theorem, the inverse is (f * g)(t) = ∫₀ᵗ 1 · e^{−2(t−τ)} dτ = e^{−2t} ∫₀ᵗ e^{2τ} dτ = e^{−2t} · [e^{2τ}/2]₀ᵗ = (1 − e^{−2t})/2. You can verify: partial fractions on 1/(s(s+2)) = ½(1/s − 1/(s+2)), so the inverse is (1 − e^{−2t})/2. Both routes agree.

The power of convolution becomes clear when the forcing function is complicated or unknown. The solution to y″ + p(t)y′ + q(t)y = g(t) can often be written as y(t) = ∫₀ᵗ h(t − τ)g(τ) dτ, where h is the **impulse response** (the solution when g is a unit spike at 0). Convolution says the response to an arbitrary forcing function g is a superposition of impulse responses weighted by g(τ) over all past times τ. This is the physical meaning: the system at time t "remembers" all past inputs, each decaying according to the system's own impulse response. The Dirac delta function, your next topic, makes the impulse response concept precise.


