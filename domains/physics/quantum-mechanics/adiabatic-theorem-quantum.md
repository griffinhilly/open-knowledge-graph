---
id: adiabatic-theorem-quantum
title: The Adiabatic Theorem and Berry's Phase
domain: physics
course: quantum-mechanics
prerequisites:
- id: schrodinger-equation-time-dependent
  type: hard
- id: eigenvalues-eigenstates-quantum
  type: hard
- id: particle-in-a-box
  type: soft
- id: time-dependent-perturbation-theory
  type: soft
builds-toward:
- berry-phase-topological-invariants
tags:
- time-evolution
- adiabatic-approximation
- geometric-phase
- berry-phase
stage: advanced
status: validated
---

# The Adiabatic Theorem and Berry's Phase

## Core Idea
The adiabatic theorem says that if a Hamiltonian changes slowly enough, a system that starts in its nth eigenstate stays in the nth eigenstate of the changing Hamiltonian, provided that level stays separated from its neighbours. "Slowly" means slow compared with ħ divided by the energy gap. Along the way the state picks up two phases: a dynamic phase from the energy, −(1/ħ)∫E_n dt, and a geometric phase that depends only on the path taken through parameter space. When the parameters return to their starting values, the geometric phase is Berry's phase, which can be measured.

## How It's Best Learned
Contrast two ways of widening an infinite square well: slowly, so the particle stays in the ground state of each new width, and suddenly, so the wavefunction is left unchanged and becomes a mixture of new eigenstates. Then write the state as a sum over instantaneous eigenstates and show which terms are suppressed when the change is slow. Work out Berry's phase for a spin-½ particle following a magnetic field that sweeps out a cone. Note that "adiabatic" here means slow, not "without heat flow."

## Common Misconceptions
- Adiabatic in quantum mechanics means no heat is exchanged, as in thermodynamics. (Here it means the Hamiltonian changes slowly compared with the system's internal time scale ħ/ΔE; the two uses are related but distinct.)
- Any change that looks slow to a human is adiabatic. (Slowness is measured against ħ/ΔE; a small energy gap makes the condition very hard to meet.)
- The only phase a slowly evolving state acquires is the dynamic phase from its energy. (There is also a geometric phase, and around a closed loop it can be observed, for example in interference experiments.)

## Questions

```yaml
- question: "A particle sits in the ground state of an infinite square well. The well's width is slowly doubled. What is the final state?"
  type: multiple-choice
  options: ["The ground state of the wide well, with one quarter of the original energy", "The original wavefunction, unchanged", "An equal mixture of all states of the wide well", "The first excited state of the wide well"]
  answer: 0
  explanation: "By the adiabatic theorem the particle stays in the ground state of the changing well. Since E₁ ∝ 1/L², doubling L cuts the energy to one quarter. A sudden change would instead leave the wavefunction unchanged."
- question: "For a closed loop in parameter space traversed adiabatically, Berry's phase depends on the geometry of the loop and not on how fast the loop is traversed."
  type: true-false
  answer: true
  explanation: "The geometric phase γ = i∮⟨n|∇_R n⟩·dR depends only on the path. The dynamic phase depends on the time taken; the geometric phase does not."
- question: "What condition must hold for the adiabatic approximation to apply?"
  type: multiple-choice
  options: ["The Hamiltonian must be time-independent", "The time over which H changes must be long compared with ħ/ΔE, where ΔE is the gap to neighbouring levels", "The temperature must be zero", "The energy must be conserved"]
  answer: 1
  explanation: "Transitions to other levels are suppressed when the change is slow compared with the internal time scale ħ/ΔE. A level crossing, where ΔE goes to zero, breaks the approximation."
- question: "A spin-½ particle with spin aligned along a magnetic field follows the field as its direction slowly traces out a closed cone that subtends solid angle Ω. What is the Berry phase?"
  type: short-answer
  answer: "γ = −Ω/2"
  explanation: "The Berry phase for the aligned spin-½ state equals minus one half of the solid angle traced out by the field direction. The anti-aligned state has +Ω/2."
```

## Explainer
Suppose a Hamiltonian H(t) depends on parameters that change in time, such as the width of a well or the direction of a magnetic field. At each instant H(t) has its own eigenstates |n(t)⟩ and energies E_n(t), found by solving the time-independent problem with the parameters frozen. The adiabatic theorem, proved by Max Born and Vladimir Fock in 1928, says that if the change is slow enough, a system that starts in |n(0)⟩ ends in |n(t)⟩. It follows the nth level continuously and does not jump to others.

What counts as slow? Expand the state in instantaneous eigenstates and substitute into the Schrödinger equation. The coupling to another level m involves the rate of change of H divided by (E_m − E_n). When H changes over a time T much longer than ħ/|E_m − E_n|, these couplings average out and the transitions are suppressed. The condition fails near a level crossing, where the gap closes.

The opposite limit is the sudden approximation. If a change happens much faster than ħ/ΔE, the wavefunction has no time to respond and stays as it was. The infinite well shows the contrast. Double the width slowly and the particle stays in the ground state, with energy reduced by a factor of four. Double it suddenly and the old ground-state wavefunction becomes a superposition of many new eigenstates.

The adiabatic state is |n(t)⟩ times a phase. Part of the phase is the dynamic phase, θ_n = −(1/ħ)∫E_n(t′)dt′, which a stationary state would collect anyway. Michael Berry showed in 1984 that there is a second part, the geometric phase

γ_n = i∫⟨n|∇_R n⟩·dR,

where R stands for the changing parameters. For an open path this phase can be changed by redefining the phases of the eigenstates. For a closed loop that returns the parameters to their start, it cannot, and it becomes a physical, measurable quantity. For a spin-½ particle aligned with a field whose direction traces a closed cone, Berry's phase is −Ω/2, where Ω is the solid angle of the cone.

Geometric phases appear across physics. The Aharonov-Bohm effect can be read as a Berry phase. In crystals, Berry phases of electron bands underlie topological insulators and the quantized Hall effect. The adiabatic theorem also supports adiabatic quantum computing, which prepares a hard problem's answer by slowly deforming a simple Hamiltonian into a complicated one.
