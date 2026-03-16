---
id: transition-probabilities-quantum
title: Transition Probabilities and Selection Rules
domain: physics
course: quantum-mechanics
prerequisites:
- id: time-dependent-perturbation-theory
  type: hard
tags:
- transitions
- selection-rules
stage: formal-systems
status: draft
---

# Transition Probabilities and Selection Rules

## Core Idea
Transition rates depend on ⟨f|H'|i⟩. Selection rules (e.g., Δl = ±1, Δj = 0, ±1 for electric dipole) determine allowed vs. forbidden transitions.

## Explainer

From time-dependent perturbation theory, you know how to calculate the amplitude for a quantum system to transition from an initial state |i⟩ to a final state |f⟩ under a weak oscillating perturbation H'. The key result is that the transition probability grows with time according to the square of the **matrix element** ⟨f|H'|i⟩. Now we ask: when is this matrix element zero, and what does that imply for which transitions nature actually allows?

The matrix element ⟨f|H'|i⟩ = ∫ ψ*_f H' ψ_i dV is an integral over all space. The crucial insight is that this integral vanishes when the integrand has a definite odd symmetry — it oscillates symmetrically about zero and cancels. For electric dipole radiation (the dominant mechanism for atomic transitions), the perturbation H' is proportional to the position vector **r**, which is odd under parity. This means ⟨f|**r**|i⟩ vanishes unless the initial and final states have *opposite* parity, which translates into the rule **Δl = ±1**: the orbital angular momentum quantum number must change by exactly one. This is not an additional postulate — it falls directly out of the symmetry of the integral.

**Selection rules** are the full set of such constraints on which transitions are allowed. For atomic electric dipole transitions, the rules are: Δl = ±1, Δm_l = 0, ±1, and Δj = 0, ±1 (excluding j = 0 → j = 0). Transitions that satisfy these rules are **allowed**; those that violate them are **forbidden**. "Forbidden" does not mean impossible — it means the electric dipole matrix element vanishes. The transition can still occur via weaker mechanisms: magnetic dipole, electric quadrupole, or higher multipoles, each suppressed by additional factors of the fine structure constant α ≈ 1/137. A forbidden transition is simply slower by many orders of magnitude.

The practical payoff is enormous. Selection rules explain the structure of atomic spectra: which lines appear bright and which are absent. They explain the metastability of excited states (the famous 2s state of hydrogen cannot decay by electric dipole to the 1s ground state, so it lives ~100 ms instead of ~10⁻⁹ s). They underlie laser physics, where population inversions exploit the different lifetimes of allowed vs. forbidden transitions. Whenever you see a spectral line, selection rules are silently dictating what you can and cannot observe.
