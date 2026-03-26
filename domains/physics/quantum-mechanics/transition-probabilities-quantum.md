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
stage: advanced
status: validated
---

# Transition Probabilities and Selection Rules

## Core Idea
Transition rates depend on ⟨f|H'|i⟩. Selection rules (e.g., Δl = ±1, Δj = 0, ±1 for electric dipole) determine allowed vs. forbidden transitions.

## Questions

```yaml
- question: "The electric dipole transition operator is proportional to the position vector r, which is odd under parity. What does this imply about which atomic transitions are allowed?"
  type: multiple-choice
  options:
    - "Only transitions between states of the same parity are allowed, because the integrand must be even to be nonzero"
    - "Only transitions between states of opposite parity are allowed, because the integrand must be even overall to be nonzero"
    - "All transitions are equally allowed, since parity has no effect on the integral value"
    - "Transitions are allowed only if both states have odd parity"
  answer: 1
  explanation: "For the matrix element ∫ ψ*_f r ψ_i dV to be nonzero, the integrand must not have a definite odd symmetry. Since r is odd under parity, the product ψ*_f r ψ_i must be even overall — which requires ψ*_f and ψ_i to have opposite parity (odd × odd × even = even, or even × odd × odd = even). States with the same parity give an odd integrand that integrates to zero. This is why Δl = ±1: changing l by an odd number changes the parity of the orbital wavefunction."

- question: "The 2s state of hydrogen has a lifetime of ~100 ms, roughly 10⁸ times longer than typical allowed transitions. What best explains this?"
  type: multiple-choice
  options:
    - "The 2s state has higher energy than 2p, making decay energetically unfavorable"
    - "The 2s → 1s electric dipole transition is selection-rule forbidden, so decay must occur via much weaker mechanisms"
    - "The selection rule Δn = ±1 prohibits 2s → 1s, since n changes by 1"
    - "The 2s state is the ground state of hydrogen and cannot decay further"
  answer: 1
  explanation: "The 2s → 1s transition violates the electric dipole selection rule Δl = ±1 because both states have l = 0 (s orbitals). The matrix element ⟨1s|r|2s⟩ vanishes by parity symmetry. The transition is 'forbidden' — meaning the electric dipole amplitude is zero, not that the transition is impossible. It eventually occurs via two-photon emission (a higher-order process), which is far slower, explaining the anomalously long lifetime. 'Forbidden' means the dominant mechanism is blocked, not that physics prevents the event."

- question: "A 'forbidden' transition in quantum mechanics is one that is prohibited by conservation of energy and therefore can rarely occur."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about selection rules. 'Forbidden' does not mean energetically impossible — it means the electric dipole matrix element ⟨f|H'|i⟩ vanishes due to symmetry, so the transition cannot occur via the electric dipole mechanism. The transition can still occur through weaker mechanisms: magnetic dipole, electric quadrupole, or higher-order processes. Each is suppressed by additional powers of the fine structure constant α ≈ 1/137. Forbidden transitions are slow, not impossible."

- question: "Selection rules for electric dipole transitions follow directly from the mathematical condition that the transition matrix element ⟨f|H'|i⟩ must be nonzero — they are not independently postulated constraints."
  type: true-false
  answer: true
  explanation: "This is the key insight about the origin of selection rules. They are not additional axioms of quantum mechanics; they are consequences of when the integral ∫ ψ*_f H' ψ_i dV is nonzero versus zero. The dipole operator H' ∝ r has specific symmetry properties; the vanishing of the integral for certain combinations of initial and final states follows from those symmetries. The Δl = ±1 rule, for example, falls out of the parity argument — it is the mathematical content of 'the integrand must be even to be nonzero.'"

- question: "Explain in physical terms why the selection rule Δl = ±1 holds for electric dipole transitions, rather than just stating the rule."
  type: short-answer
  answer: "The electric dipole perturbation H' is proportional to r, which is an odd function under parity inversion (r → −r). For the matrix element ⟨f|r|i⟩ to be nonzero, the full integrand ψ*_f r ψ_i must be even under parity. Since r is odd, ψ*_f and ψ_i must have opposite parity. The parity of a hydrogen orbital is (−1)^l, so initial and final states need l values that differ by an odd number — the minimal such difference is 1, giving Δl = ±1."
  explanation: "The rule is not memorized; it is derived from the symmetry of the integral. A student who just remembers 'Δl = ±1' without knowing why will struggle when confronted with other multipole transitions or other perturbation operators. The key is that the operator's symmetry under parity determines which combinations of states give a nonvanishing integral. This same logic extends to other selection rules (Δm_l = 0, ±1 from the angular part of the integral, etc.)."
```

## Explainer

From time-dependent perturbation theory, you know how to calculate the amplitude for a quantum system to transition from an initial state |i⟩ to a final state |f⟩ under a weak oscillating perturbation H'. The key result is that the transition probability grows with time according to the square of the **matrix element** ⟨f|H'|i⟩. Now we ask: when is this matrix element zero, and what does that imply for which transitions nature actually allows?

The matrix element ⟨f|H'|i⟩ = ∫ ψ*_f H' ψ_i dV is an integral over all space. The crucial insight is that this integral vanishes when the integrand has a definite odd symmetry — it oscillates symmetrically about zero and cancels. For electric dipole radiation (the dominant mechanism for atomic transitions), the perturbation H' is proportional to the position vector **r**, which is odd under parity. This means ⟨f|**r**|i⟩ vanishes unless the initial and final states have *opposite* parity, which translates into the rule **Δl = ±1**: the orbital angular momentum quantum number must change by exactly one. This is not an additional postulate — it falls directly out of the symmetry of the integral.

**Selection rules** are the full set of such constraints on which transitions are allowed. For atomic electric dipole transitions, the rules are: Δl = ±1, Δm_l = 0, ±1, and Δj = 0, ±1 (excluding j = 0 → j = 0). Transitions that satisfy these rules are **allowed**; those that violate them are **forbidden**. "Forbidden" does not mean impossible — it means the electric dipole matrix element vanishes. The transition can still occur via weaker mechanisms: magnetic dipole, electric quadrupole, or higher multipoles, each suppressed by additional factors of the fine structure constant α ≈ 1/137. A forbidden transition is simply slower by many orders of magnitude.

The practical payoff is enormous. Selection rules explain the structure of atomic spectra: which lines appear bright and which are absent. They explain the metastability of excited states (the famous 2s state of hydrogen cannot decay by electric dipole to the 1s ground state, so it lives ~100 ms instead of ~10⁻⁹ s). They underlie laser physics, where population inversions exploit the different lifetimes of allowed vs. forbidden transitions. Whenever you see a spectral line, selection rules are silently dictating what you can and cannot observe.
