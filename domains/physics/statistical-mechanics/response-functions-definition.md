---
id: response-functions-definition
title: Response Functions and Linear Response
domain: physics
course: statistical-mechanics
prerequisites:
- id: time-correlation-functions
  type: hard
- id: linear-response-theory-statmech
  type: hard
builds-toward:
- green-kubo-formula
tags:
- response
- perturbation
- dynamics
stage: advanced
status: draft
---

# Response Functions and Linear Response

## Core Idea
Response functions describe how a system deviates from equilibrium when subjected to small external perturbations. Linear response theory states that observables respond linearly to weak driving forces, with the response function related to equilibrium fluctuations through the fluctuation-dissipation theorem.

## Explainer

A **response function** answers the question: if I poke a system with a small external perturbation, how does it respond? The word "small" is key — small enough that the response is proportional to the perturbation, so that the relationship between cause and effect is linear. This linearity is not an approximation of last resort; it is the regime where equilibrium statistical mechanics makes clean, exact predictions. In the linear regime, the full response is encoded in equilibrium correlation functions that you can compute without ever applying the perturbation.

Concretely, suppose you apply a time-dependent field h(t) that couples to observable B in the Hamiltonian (i.e., H' = −h(t)B). The response of a different observable A is given by the linear response formula: ⟨δA(t)⟩ = ∫ χ_{AB}(t − t') h(t') dt', where χ_{AB}(t − t') is the **generalized susceptibility** or response function. The convolution structure reflects causality and time-translation invariance. The response at time t depends on the field at all past times t' < t, weighted by χ. In Fourier space this convolution becomes a simple product: δÃ(ω) = χ̃_{AB}(ω) h̃(ω), making frequency-domain analysis natural for periodic driving.

The deep result — due to Kubo — is that χ_{AB}(t) is entirely determined by **equilibrium time-correlation functions**. Specifically, χ_{AB}(t) = (i/ℏ) θ(t) ⟨[A(t), B(0)]⟩₀, where the expectation value is taken over the unperturbed equilibrium ensemble and θ(t) is the step function enforcing causality. This is the **Kubo formula**. It says you do not need to drive the system to measure its response — you can infer the entire linear response from fluctuations that spontaneously occur in thermal equilibrium. This is profound: the same thermal fluctuations that look like noise carry complete information about how the system will respond to external drives.

The imaginary part of the frequency-domain susceptibility χ''(ω) measures **dissipation** — how much energy the system absorbs from the driving field. The real part χ'(ω) measures the in-phase reactive response. The **fluctuation-dissipation theorem**, which you studied as a prerequisite, connects these: χ''(ω) is proportional to the power spectrum of equilibrium fluctuations S(ω) via χ''(ω) = (ω/2k_BT) S_{AB}(ω). Dissipation and fluctuations are two faces of the same microscopic dynamics. Familiar response functions — magnetic susceptibility, dielectric function, thermal conductivity, viscosity — are all special cases of this framework, and the Kubo formula provides the microscopic foundation for computing them all from equilibrium molecular dynamics.
