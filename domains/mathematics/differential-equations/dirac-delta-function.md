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
stage: formal-systems
status: validated
---

# Dirac Delta Function and Impulse Response

## Core Idea
The Dirac delta δ(t) models an instantaneous impulse: zero everywhere except at t = 0, with ∫_{-∞}^∞ δ(t)dt = 1. Its Laplace transform is L[δ(t)] = 1. The impulse response of a system is the solution when forced by δ(t), and convolution with the impulse response gives the response to any input. Deltas are essential for modeling sudden shocks and discontinuous inputs.

## Questions

```yaml
- question: "Why is the Dirac delta function called a 'distribution' rather than a function?"
  type: multiple-choice
  options:
    - "Because it distributes its value evenly across an interval rather than concentrating it at a single point"
    - "Because it is defined by its behavior inside integrals (the sifting property) rather than by assigning a value at each point"
    - "Because it is used in probability distributions to model rare events"
    - "Because Dirac originally derived it from probability theory using the normal distribution as a limit"
  answer: 1
  explanation: "An ordinary function is defined by assigning a value to each point in its domain. The Dirac delta cannot be defined this way — it would need to be zero everywhere except at one point, yet integrate to 1, which is impossible for any standard function. Instead, δ(t) is defined by its sifting property: ∫f(t)δ(t−a)dt = f(a) for any continuous f. It is defined by what it does inside integrals, not by pointwise values. This is the definition of a distribution — a functional that maps test functions to numbers. The 'infinitely tall, infinitely narrow spike' description is a useful intuition, but the formal definition is the integral behavior."

- question: "A linear system has impulse response h(t) = e^{−2t}u(t). An engineer needs to find the output when the input is f(t) = sin(t)·u(t). What is the most efficient approach?"
  type: multiple-choice
  options:
    - "Re-solve the differential equation from scratch with f(t) = sin(t) on the right-hand side"
    - "Approximate sin(t) as a sum of delta functions and solve for each one separately"
    - "Compute the convolution (h * f)(t) — since h(t) is the impulse response, convolving it with any input gives the system output"
    - "Take the Laplace transform of sin(t) and substitute it into the original ODE in the s-domain without using h(t)"
  answer: 2
  explanation: "The impulse response h(t) is a complete fingerprint of the system's linear dynamics. The convolution theorem guarantees that the output for any input f(t) is simply (h * f)(t) — no need to re-solve the ODE. This is the central payoff of impulse response theory: solve the system once (with δ(t) as input), and you have the tool to handle any input through convolution. The Laplace domain version is equally elegant: Y(s) = H(s)·F(s), where H(s) = L[h(t)] is the transfer function. The impulse response and the ODE are equivalent characterizations of the system."

- question: "The Dirac delta function δ(t) has the property that ∫_{-∞}^∞ δ(t) dt = 0, because it is zero almost everywhere."
  type: true-false
  answer: false
  explanation: "This is a common and important misconception. The integral of δ(t) over all of ℝ is 1, not 0. This is one of its defining properties. The intuition is that δ(t) concentrates a total 'mass' of 1 at a single point — like an infinitely tall, infinitely narrow spike with unit area. Although it is zero everywhere except at t = 0, the integral captures the total 'mass,' which is 1. This is precisely what makes it the identity element for convolution: f * δ = f. If the integral were 0, the delta would have no effect when convolved with any function."

- question: "In the Laplace domain, L[δ(t)] = 1, which means that the transfer function H(s) of a system equals the Laplace transform of its impulse response."
  type: true-false
  answer: true
  explanation: "This is correct and fundamental. Since L[δ(t)] = 1, the Laplace transform of the ODE forced by δ(t) has right-hand side 1. Solving gives the transfer function H(s) in the s-domain. Inverting yields h(t), the impulse response. The relationship L[h(t)] = H(s) means the system's frequency-domain behavior and its time-domain response to a unit impulse are Laplace transform pairs. Once you have H(s), the response to any input F(s) is Y(s) = H(s)·F(s) — multiplication in the s-domain corresponds to convolution in the time domain."

- question: "Explain why the impulse response h(t) is described as a 'fingerprint' of a linear system, and how it is used to find the response to an arbitrary input."
  type: short-answer
  answer: "The impulse response h(t) completely characterizes a linear time-invariant system because it encodes how the system responds to the most elementary possible input — an instantaneous unit impulse. Any other input f(t) can be thought of as a superposition of scaled, shifted delta functions. By linearity and time-invariance, the system's response to each shifted delta δ(t−τ) is a shifted copy h(t−τ), scaled by f(τ). Integrating over all τ gives the total response: y(t) = ∫f(τ)h(t−τ)dτ = (f * h)(t). So knowing h(t) means never needing to re-solve the ODE for a new input — convolution with h gives the answer directly."
  explanation: "The delta function makes this possible because L[δ(t)] = 1: forcing the system with δ(t) in the Laplace domain gives Y(s) = H(s)·1 = H(s), so the impulse response IS the transfer function (under inverse Laplace). This is why solving the system once with δ(t) as input captures all information about the system's dynamics. The convolution theorem then provides the mechanism: the time-domain convolution (h * f)(t) corresponds to the product H(s)·F(s) in the s-domain, making computation tractable. The impulse response bridges delta-function theory, the convolution theorem, and practical systems analysis."
```

## Explainer

Your prerequisite on the convolution theorem gave you a tool for combining two functions: (f * g)(t) = ∫₀ᵗ f(τ)g(t − τ)dτ. You also learned that the Laplace transform converts convolution into multiplication: L[f * g] = L[f] · L[g]. This is powerful for solving differential equations, but it raises a natural question: what acts as the "identity element" for convolution? That is, what function h has the property that f * h = f for every f? The answer is the **Dirac delta**, δ(t). It is the convolution identity, and that role alone justifies its importance.

The delta function δ(t) is not a function in the ordinary sense — it cannot be defined by assigning a value at each point. Instead, it is a **distribution**: a mathematical object defined by how it behaves inside integrals. Its defining property is the **sifting property**: for any continuous function f, ∫_{-∞}^∞ f(t) δ(t − a) dt = f(a). The delta "sifts out" the value of f at the single point t = a. Think of it as an infinitely tall, infinitely narrow spike located at a, with total area 1. No actual function has this shape, but the integral behavior is well-defined and consistent.

The Laplace transform makes δ(t) easy to work with in practice. Since L[δ(t)] = 1 (the transform of the delta at t = 0 is simply 1), a differential equation forced by δ(t) becomes, after transforming, an algebraic equation with a right-hand side of 1. Solving gives you the **transfer function** or **impulse response** H(s) in the s-domain. Inverting gives h(t) — the solution when the system is hit by an instantaneous unit impulse at t = 0. This impulse response is a fingerprint of the system: once you know h(t), the convolution theorem tells you the response to *any* input f(t) is simply (h * f)(t). You do not need to re-solve the ODE for each new input.

Physically, δ(t) models forces or signals that deliver energy instantaneously: a hammer blow, an electrical spike, or a sudden injection at a specific time. For a spring-mass system, hitting the mass with a sharp impulse at t = 0 sets it into free oscillation. The resulting position x(t) is exactly the impulse response h(t). For a shifted impulse δ(t − a), the effect is the same but delayed to time t = a. This ability to model concentrated inputs at precise moments — and then superpose them via convolution to handle distributed inputs — makes the Dirac delta indispensable for systems analysis, signal processing, and any engineering context where inputs can be sudden or discontinuous.
