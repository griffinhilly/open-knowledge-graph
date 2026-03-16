---
id: expectation-values-quantum
title: Expectation Values and Quantum Averages
domain: physics
course: modern-physics
prerequisites:
- id: quantum-superposition-states
  type: hard
- id: quantum-operators-observables
  type: hard
builds-toward:
- canonical-commutation-relations
tags:
- quantum
- observables
- measurement
stage: abstract-reasoning
status: draft
---

# Expectation Values and Quantum Averages

## Core Idea
The expectation value of an observable is ⟨A⟩ = ∫ψ* Â ψ dx, giving the average result of many measurements on identically prepared systems. For an eigenstate of Â, the expectation value equals the eigenvalue. Expectation values obey classical equations of motion (Ehrenfest theorem), bridging quantum and classical mechanics.

## Explainer

In classical mechanics, a particle has a definite position, momentum, and energy at every moment. In quantum mechanics, a particle in a superposition state has no definite value for an observable — until measurement, the system is genuinely in multiple states simultaneously. What you *can* compute is the **expectation value**: the average outcome you would obtain if you prepared many identical copies of the system and measured each one. This is not a statement about uncertainty in preparation — the state is precisely known — it is a statement about the irreducibly probabilistic nature of quantum measurement.

The formula **⟨A⟩ = ∫ψ* Â ψ dx** computes this average using the operator Â corresponding to observable A. The structure ψ* Â ψ is a weighted average: Â ψ applies the operator to the wavefunction, and then ψ* "samples" the result with the probability amplitude at each point. For position, Â = x, and ⟨x⟩ = ∫ψ* x ψ dx = ∫x|ψ|² dx — literally the average of position weighted by the probability density |ψ|². For momentum, Â = −iℏ∂/∂x, and the integral picks up the average momentum encoded in how rapidly the wavefunction oscillates.

A special case clarifies the structure. If ψ is an **eigenstate** of Â with eigenvalue a — meaning Âψ = aψ — then ⟨A⟩ = ∫ψ* (aψ) dx = a ∫|ψ|² dx = a. Every measurement gives exactly a; the expectation value equals the eigenvalue and there is no spread. By contrast, in a superposition ψ = c₁ψ₁ + c₂ψ₂ where Âψ₁ = a₁ψ₁ and Âψ₂ = a₂ψ₂, you get ⟨A⟩ = |c₁|²a₁ + |c₂|²a₂ — a weighted average of eigenvalues, weighted by the squared amplitudes, exactly like a classical probability-weighted average.

The **Ehrenfest theorem** shows that expectation values obey classical equations of motion: d⟨x⟩/dt = ⟨p⟩/m and d⟨p⟩/dt = −⟨∂V/∂x⟩. These are Newton's laws for averages. When the quantum state is a narrow wave packet (well-localized in space), ⟨∂V/∂x⟩ ≈ ∂V/∂x evaluated at ⟨x⟩, and the expectation values trace out the classical trajectory. This is why large objects behave classically — their wave packets are so narrow that the expectation values and the eigenvalues are indistinguishable. Ehrenfest's theorem is not a coincidence; it is the mathematical explanation of why quantum mechanics reduces to classical mechanics in the appropriate limit.
