---
id: linear-response-theory
title: Linear Response Theory
domain: physics
course: statistical-mechanics
prerequisites:
- id: fluctuation-dissipation-theorem
  type: hard
- id: canonical-ensemble
  type: soft
builds-toward:
- response-functions-susceptibilities
tags:
- response-function
- perturbation
- equilibrium
stage: advanced
status: draft
---

# Linear Response Theory

## Core Idea
Linear response theory gives the response ⟨δA⟩ = χ_{AB} δB of an observable A to a small external perturbation δB as ⟨δA(t)⟩ = ∫ χ_{AB}(t−t') δB(t') dt'. The response function χ is given by the Kubo formula involving the equilibrium correlation of fluctuations, directly connecting the fluctuation-dissipation theorem to dynamics.

## Explainer

From the fluctuation-dissipation theorem, you know that the dissipative response of a system — how it absorbs energy from an external drive — is directly related to the spectrum of its equilibrium fluctuations. The same thermal noise that jiggles a resistor also determines its electrical resistance. Linear response theory provides the precise dynamical framework behind this statement: for any *small* perturbation, the system's full response — not just its steady-state value but its entire time history — is completely determined by equilibrium properties, computed once and reused for any perturbation.

The setup: the equilibrium Hamiltonian is H₀. A small time-dependent field δB(t) couples to observable B̂, adding −δB(t)B̂ to the Hamiltonian. First-order time-dependent perturbation theory gives ⟨δA(t)⟩ = ∫_{−∞}^{t} χ_{AB}(t − t') δB(t') dt'. This is a **convolution**: the current response depends on the entire history of the perturbation, weighted by the **response function** χ_{AB}(τ), which measures how strongly the system at time τ ago influences the present. The upper limit t (not +∞) enforces **causality**: χ_{AB}(τ) = 0 for τ < 0, meaning the response cannot precede its cause. In frequency space, causality imposes the **Kramers-Kronig relations**, linking the real (dispersive) and imaginary (absorptive) parts of the complex susceptibility χ(ω).

The **Kubo formula** is the central result: χ_{AB}(t) = −(i/ℏ)θ(t)⟨[Â(t), B̂(0)]⟩₀, where the expectation value is taken in the *unperturbed* equilibrium state and θ(t) is the Heaviside function enforcing causality. This means you never need to solve the driven problem: compute the commutator expectation in equilibrium, and you have the complete linear response to any small perturbation. The imaginary part of χ(ω) in frequency space gives the **dissipation spectrum** — how strongly the system absorbs at each frequency. The fluctuation-dissipation theorem then identifies Im[χ(ω)] ∝ S(ω), the **spectral density** of equilibrium fluctuations of Â. A mode that fluctuates strongly in equilibrium also absorbs strongly when driven — the same microscopic processes responsible for thermal noise also carry driven dissipation.

Linear response theory unifies an enormous range of transport phenomena. Electrical conductivity (the response of current density to an applied electric field), magnetic susceptibility (response of magnetization to an applied magnetic field), thermal conductivity (response of heat current to a temperature gradient), and the diffusion coefficient all take the form of Kubo formulas — integrals of equilibrium time-correlation functions. This is the foundation of modern non-equilibrium statistical mechanics: instead of solving complicated driven problems case by case, you extract all linear transport coefficients from a single equilibrium simulation or calculation. The framework breaks down when the perturbation is large enough to push the system into genuinely nonlinear territory, but for small fields it is exact.
