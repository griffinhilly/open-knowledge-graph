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

## Explainer

From solving IVPs with the Laplace transform, you know the workflow: transform the ODE into an algebraic equation in s, solve for Y(s), then invert to find y(t). The bottleneck is often the inversion step. When Y(s) factors as a product F(s)·G(s) — two functions whose individual inverses you know — you might hope to recover y(t) by simply multiplying f(t)·g(t). This is wrong. The inverse Laplace transform does not distribute over multiplication the way it does over addition. The correct tool is **convolution**.

The **convolution** of two functions f and g is defined by (f * g)(t) = ∫₀ᵗ f(τ)g(t − τ) dτ. The variable τ slides across [0, t], with one function evaluated forward in time and the other evaluated backward. The integral accumulates how much f and g "overlap" as you shift one past the other. The **Convolution Theorem** says precisely: ℒ[f * g](s) = F(s)·G(s), or equivalently, ℒ⁻¹[F(s)·G(s)] = (f * g)(t). Multiplication in the s-domain corresponds to convolution in the t-domain.

As a concrete example, suppose you need ℒ⁻¹[1/(s(s + 2))]. You recognize F(s) = 1/s with f(t) = 1, and G(s) = 1/(s + 2) with g(t) = e^{−2t}. By the convolution theorem, the inverse is (f * g)(t) = ∫₀ᵗ 1 · e^{−2(t−τ)} dτ = e^{−2t} ∫₀ᵗ e^{2τ} dτ = e^{−2t} · [e^{2τ}/2]₀ᵗ = (1 − e^{−2t})/2. You can verify: partial fractions on 1/(s(s+2)) = ½(1/s − 1/(s+2)), so the inverse is (1 − e^{−2t})/2. Both routes agree.

The power of convolution becomes clear when the forcing function is complicated or unknown. The solution to y″ + p(t)y′ + q(t)y = g(t) can often be written as y(t) = ∫₀ᵗ h(t − τ)g(τ) dτ, where h is the **impulse response** (the solution when g is a unit spike at 0). Convolution says the response to an arbitrary forcing function g is a superposition of impulse responses weighted by g(τ) over all past times τ. This is the physical meaning: the system at time t "remembers" all past inputs, each decaying according to the system's own impulse response. The Dirac delta function, your next topic, makes the impulse response concept precise.


