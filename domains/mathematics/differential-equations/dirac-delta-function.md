---
id: dirac-delta-function
title: Dirac Delta Function and Impulse Response
domain: mathematics
course: differential-equations
prerequisites:
- id: convolution-theorem
  type: hard
builds-toward:
- systems-first-order-linear-odes
tags:
- delta-function
- impulse
- distribution
stage: advanced
status: draft
---

# Dirac Delta Function and Impulse Response

## Core Idea
The Dirac delta δ(t) models an instantaneous impulse: zero everywhere except at t = 0, with ∫_{-∞}^∞ δ(t)dt = 1. Its Laplace transform is L[δ(t)] = 1. The impulse response of a system is the solution when forced by δ(t), and convolution with the impulse response gives the response to any input. Deltas are essential for modeling sudden shocks and discontinuous inputs.

## Explainer

Your prerequisite on the convolution theorem gave you a tool for combining two functions: (f * g)(t) = ∫₀ᵗ f(τ)g(t − τ)dτ. You also learned that the Laplace transform converts convolution into multiplication: L[f * g] = L[f] · L[g]. This is powerful for solving differential equations, but it raises a natural question: what acts as the "identity element" for convolution? That is, what function h has the property that f * h = f for every f? The answer is the **Dirac delta**, δ(t). It is the convolution identity, and that role alone justifies its importance.

The delta function δ(t) is not a function in the ordinary sense — it cannot be defined by assigning a value at each point. Instead, it is a **distribution**: a mathematical object defined by how it behaves inside integrals. Its defining property is the **sifting property**: for any continuous function f, ∫_{-∞}^∞ f(t) δ(t − a) dt = f(a). The delta "sifts out" the value of f at the single point t = a. Think of it as an infinitely tall, infinitely narrow spike located at a, with total area 1. No actual function has this shape, but the integral behavior is well-defined and consistent.

The Laplace transform makes δ(t) easy to work with in practice. Since L[δ(t)] = 1 (the transform of the delta at t = 0 is simply 1), a differential equation forced by δ(t) becomes, after transforming, an algebraic equation with a right-hand side of 1. Solving gives you the **transfer function** or **impulse response** H(s) in the s-domain. Inverting gives h(t) — the solution when the system is hit by an instantaneous unit impulse at t = 0. This impulse response is a fingerprint of the system: once you know h(t), the convolution theorem tells you the response to *any* input f(t) is simply (h * f)(t). You do not need to re-solve the ODE for each new input.

Physically, δ(t) models forces or signals that deliver energy instantaneously: a hammer blow, an electrical spike, or a sudden injection at a specific time. For a spring-mass system, hitting the mass with a sharp impulse at t = 0 sets it into free oscillation. The resulting position x(t) is exactly the impulse response h(t). For a shifted impulse δ(t − a), the effect is the same but delayed to time t = a. This ability to model concentrated inputs at precise moments — and then superpose them via convolution to handle distributed inputs — makes the Dirac delta indispensable for systems analysis, signal processing, and any engineering context where inputs can be sudden or discontinuous.
