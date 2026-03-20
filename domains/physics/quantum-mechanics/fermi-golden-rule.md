---
id: fermi-golden-rule
title: The Fermi Golden Rule
domain: physics
course: quantum-mechanics
prerequisites:
- id: time-dependent-perturbation-theory
  type: hard
tags:
- fermi-golden-rule
- transition-rates
stage: advanced
status: draft
---

# The Fermi Golden Rule

## Core Idea
Transition rate to continuum: Γ_{i→f} = (2π/ℏ) |⟨f|H'|i⟩|² ρ(E_f), where ρ(E_f) is the density of final states. Predicts absorption, emission, decay, and scattering rates.

## Explainer

From time-dependent perturbation theory, you learned how to compute the probability that a perturbation H' drives a quantum system from an initial state |i⟩ to a specific final state |f⟩. The result at first order is P_{i→f}(t) = (1/ℏ²)|⟨f|H'|i⟩|² × [sin(Δωt/2)/(Δω/2)]², where Δω = (E_f − E_i)/ℏ. For transitions between two discrete levels, this oscillates — the system tunnels back and forth. But in many physical situations, the final state is not a single discrete level; it is a continuum of states (photons in free space, scattered particles at various angles, electrons in a conduction band). The Fermi Golden Rule handles this case.

When final states form a continuum, we sum P_{i→f}(t) over all final states within an energy window and ask: how does total transition probability grow with time? The key mathematical step is recognizing that as t → ∞, the factor [sin(Δωt/2)/(Δω/2)]² becomes sharply peaked around Δω = 0 and approaches 2πt δ(E_f − E_i). The delta function enforces **energy conservation** — only final states at exactly the initial energy can be reached. Dividing by time gives a constant **transition rate**:

**Γ_{i→f} = (2π/ℏ) |⟨f|H'|i⟩|² ρ(E_f)**

where ρ(E_f) is the **density of final states** — the number of states per unit energy available at the transition energy E_f = E_i.

The formula has two factors, each with clear physical meaning. The **matrix element** |⟨f|H'|i⟩|² measures how strongly the perturbation couples the initial and final states — a transition that H' cannot drive has zero matrix element and zero rate. The **density of states** ρ(E_f) measures how many final states are available — even a strong coupling produces a slow rate if final states are scarce. Both factors must be large for a fast transition. This structure explains why an atom in free space emits photons at a rate that depends on both the atomic dipole moment (matrix element) and the photon density of states (which goes as ω²), giving the familiar ω³ dependence of spontaneous emission. It also underlies scattering cross sections in nuclear and particle physics through the Born approximation, and governs electron-phonon scattering rates that determine electrical resistivity in metals.
