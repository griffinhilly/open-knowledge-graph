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

## Questions

```yaml
- question: "A quantum particle is prepared in an energy eigenstate with energy E. Over time, according to the TDSE, what happens to the probability distribution |ψ(r, t)|²?"
  type: multiple-choice
  options:
    - "It spreads out over time because quantum mechanics requires all localized states to delocalize"
    - "It oscillates periodically with frequency E/h, changing shape over time"
    - "It remains unchanged — the time evolution is a pure phase factor e^{−iEt/ℏ} that does not affect |ψ|²"
    - "It decays exponentially unless the particle is in the ground state"
  answer: 2
  explanation: "For an energy eigenstate, the TDSE gives ψ(r, t) = ψ(r, 0) e^{−iEt/ℏ}. The probability density is |ψ(r, t)|² = |ψ(r, 0)|² · |e^{−iEt/ℏ}|² = |ψ(r, 0)|², since |e^{iθ}| = 1 for any real θ. The phase factor rotates in the complex plane but has unit magnitude, so it cancels completely in the probability density. This is why energy eigenstates are called 'stationary states' — all measurable probabilities are time-independent, even though the wavefunction itself is changing."

- question: "A wavepacket — a spatially localized quantum particle — is a superposition of energy eigenstates, each oscillating at its own frequency E/ℏ. What happens to the wavepacket over time?"
  type: multiple-choice
  options:
    - "Nothing — superpositions of stationary states are themselves stationary, since each component is unchanged"
    - "The wavepacket oscillates but maintains its shape, since energy eigenstates are the natural modes of the system"
    - "The wavepacket spreads and can move, because components with different energies acquire different phases over time, altering their interference pattern"
    - "The wavepacket immediately collapses to one of the energy eigenstates it contains"
  answer: 2
  explanation: "Each energy eigenstate in the superposition acquires its own phase e^{−iEt/ℏ}. Since components with different energies evolve at different rates, the relative phases between components change over time. This changes the interference pattern among the components, which determines the shape of |ψ|². The result: the wavepacket spreads and moves. The term 'stationary' applies only to individual energy eigenstates, not to superpositions. Option A is the key misconception — stationarity of each component does not make the superposition stationary."

- question: "For a particle in an energy eigenstate with energy E, the probability distribution |ψ(r, t)|² is independent of time, even though the wavefunction ψ(r, t) itself changes."
  type: true-false
  answer: true
  explanation: "The time evolution of an energy eigenstate is ψ(r, t) = ψ(r, 0) e^{−iEt/ℏ}. The wavefunction changes (its complex phase rotates), but |ψ(r, t)|² = |ψ(r, 0)|² · |e^{−iEt/ℏ}|² = |ψ(r, 0)|² since |e^{iθ}| = 1. All measurable probabilities and expectation values of time-independent observables are constant. The global phase rotation of the wavefunction is unobservable — no measurement can detect it."

- question: "A quantum state that is a superposition of two energy eigenstates is itself a stationary state, since it is composed entirely of stationary-state wavefunctions."
  type: true-false
  answer: false
  explanation: "A superposition of energy eigenstates is not stationary. Consider ψ = c₁ψ₁ e^{−iE₁t/ℏ} + c₂ψ₂ e^{−iE₂t/ℏ}. The probability density |ψ|² contains a cross-term proportional to e^{−i(E₁−E₂)t/ℏ}, which oscillates at frequency (E₁ − E₂)/h. This oscillating interference term causes the probability distribution to change in time — the state is emphatically not stationary. Stationarity of individual components does not sum to stationarity of the superposition."

- question: "In what sense is the time-dependent Schrödinger equation iℏ ∂ψ/∂t = Ĥψ the quantum analog of Newton's second law, and why does this analogy matter for understanding quantum dynamics?"
  type: short-answer
  answer: "Newton's second law F = ma is a dynamical equation: given the forces acting on a system (encoded by F) and the initial state (position and momentum), it determines how the state evolves in time. The TDSE plays exactly the same role: given the Hamiltonian Ĥ (which encodes the system's kinetic and potential energy) and the initial wavefunction ψ(r, 0), it determines ψ(r, t) for all future times. The analogy matters because it establishes the TDSE as the complete and fundamental law of quantum dynamics — not a special-case tool but the equation governing all quantum evolution, from simple two-state systems to complex many-body dynamics."
  explanation: "The analogy also highlights what is different: Newton's law is deterministic in phase space (position and momentum); the TDSE governs a complex-valued field whose squared magnitude gives probabilities. The 'state' in quantum mechanics is the wavefunction — far richer than a phase-space point — and its evolution is governed by a linear partial differential equation, which is why superposition and interference are possible."
```

## Explainer

The time-dependent Schrödinger equation is the quantum analog of Newton's second law — it tells you how a quantum state changes over time. Where Newton's law says "force determines acceleration," the TDSE says "the Hamiltonian determines the rate of change of the wavefunction." From your study of the time-independent Schrödinger equation, you already know how to find energy eigenstates — solutions where the energy is definite. The time-dependent equation reveals what happens beyond those special cases: it governs *all* quantum evolution, including states that are superpositions of energy eigenstates.

The equation iℏ ∂ψ/∂t = Ĥψ has a remarkable structure. The left side involves a partial derivative in time (which you know means the rate of change with t, holding spatial coordinates fixed) and the imaginary unit i, meaning the wavefunction is complex-valued. The right side applies the **Hamiltonian operator**, which encodes kinetic energy (−ℏ²/2m ∇²) plus potential energy V(r). So the equation literally says: the imaginary unit times ℏ times the time rate-of-change of ψ equals the total energy operator acting on ψ. The complex-number structure ensures that probability is conserved: |ψ|² integrates to 1 at all times.

For energy eigenstates — states where Ĥψ = Eψ — the time-dependent equation has a clean solution: ψ(r,t) = ψ(r,0) e^{−iEt/ℏ}. This **phase factor** e^{−iEt/ℏ} oscillates in time but never changes the probability distribution |ψ|², since |e^{−iEt/ℏ}| = 1. This is why energy eigenstates are called **stationary states** — their measurable properties don't evolve. The frequency of oscillation is f = E/h, connecting quantum energy to the Einstein relation E = hf you know from photons.

The real power of the time-dependent equation appears for superposition states. A **wavepacket** — a localized quantum particle — is built from a continuous distribution of energy eigenstates, each oscillating at its own frequency E/ℏ. As these components interfere constructively and destructively over time, the packet spreads and moves. This spreading is not a flaw but the quantum prediction: a particle with momentum spread Δp will develop position spread Δx ≥ ℏ/(2Δp) over time, consistent with the uncertainty principle. The TDSE governs all of this evolution exactly, from the simplest two-state oscillation to the complex dynamics of many-body systems.
