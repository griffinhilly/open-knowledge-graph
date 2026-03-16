---
id: schrodinger-equation-time-dependent
title: 'Schrödinger Equation: Time-Dependent Form'
domain: physics
course: modern-physics
prerequisites:
- id: schrodinger-equation-intro
  type: hard
- id: partial-derivatives
  type: hard
- id: complex-numbers-intro
  type: hard
builds-toward:
- wavefunctions-boundary-conditions
- classical-limit-correspondence
tags:
- quantum-mechanics
- schrödinger
stage: advanced
status: draft
---

# Schrödinger Equation: Time-Dependent Form

## Core Idea
The time-dependent Schrödinger equation, iℏ ∂ψ/∂t = Ĥψ, describes how a quantum state evolves in time. The Hamiltonian operator Ĥ contains the kinetic and potential energy of the system. Solutions are wavefunctions ψ(r,t) whose squared magnitude |ψ|² gives the probability density for finding the particle at position r at time t.

## Explainer

The time-dependent Schrödinger equation is the quantum analog of Newton's second law — it tells you how a quantum state changes over time. Where Newton's law says "force determines acceleration," the TDSE says "the Hamiltonian determines the rate of change of the wavefunction." From your study of the time-independent Schrödinger equation, you already know how to find energy eigenstates — solutions where the energy is definite. The time-dependent equation reveals what happens beyond those special cases: it governs *all* quantum evolution, including states that are superpositions of energy eigenstates.

The equation iℏ ∂ψ/∂t = Ĥψ has a remarkable structure. The left side involves a partial derivative in time (which you know means the rate of change with t, holding spatial coordinates fixed) and the imaginary unit i, meaning the wavefunction is complex-valued. The right side applies the **Hamiltonian operator**, which encodes kinetic energy (−ℏ²/2m ∇²) plus potential energy V(r). So the equation literally says: the imaginary unit times ℏ times the time rate-of-change of ψ equals the total energy operator acting on ψ. The complex-number structure ensures that probability is conserved: |ψ|² integrates to 1 at all times.

For energy eigenstates — states where Ĥψ = Eψ — the time-dependent equation has a clean solution: ψ(r,t) = ψ(r,0) e^{−iEt/ℏ}. This **phase factor** e^{−iEt/ℏ} oscillates in time but never changes the probability distribution |ψ|², since |e^{−iEt/ℏ}| = 1. This is why energy eigenstates are called **stationary states** — their measurable properties don't evolve. The frequency of oscillation is f = E/h, connecting quantum energy to the Einstein relation E = hf you know from photons.

The real power of the time-dependent equation appears for superposition states. A **wavepacket** — a localized quantum particle — is built from a continuous distribution of energy eigenstates, each oscillating at its own frequency E/ℏ. As these components interfere constructively and destructively over time, the packet spreads and moves. This spreading is not a flaw but the quantum prediction: a particle with momentum spread Δp will develop position spread Δx ≥ ℏ/(2Δp) over time, consistent with the uncertainty principle. The TDSE governs all of this evolution exactly, from the simplest two-state oscillation to the complex dynamics of many-body systems.
