---
id: bcs-theory-detailed
title: BCS Theory (Detailed)
domain: physics
course: condensed-matter-physics
prerequisites:
- id: superconductivity-phenomenology
  type: hard
- id: electron-phonon-interaction
  type: hard
- id: superconductivity-bcs-theory
  type: soft
- id: creation-annihilation-operators
  type: soft
tags:
- bcs-theory
- cooper-pair
- energy-gap
- superconductivity
stage: expert
status: validated
---

# BCS Theory (Detailed)

## Core Idea
BCS theory (Bardeen, Cooper, Schrieffer, 1957) explains superconductivity microscopically. Phonon-mediated attraction between electrons near the Fermi surface allows the formation of Cooper pairs — bound states of electrons with opposite momentum and spin (k↑, -k↓). The BCS ground state is a coherent superposition of pair-occupied and pair-empty states, described by the wavefunction |BCS> = product_k (u_k + v_k c†_{k↑} c†_{-k↓})|0>. The energy gap Delta(T) opens at E_F, with 2Delta(0) = 3.53 k_B T_c in weak coupling. The gap suppresses low-energy scattering and is responsible for zero resistance, the Meissner effect, and the exponential specific heat at low temperatures.

## Questions

```yaml
- question: "Cooper showed that two electrons above a filled Fermi sea with an arbitrarily weak attractive interaction form a bound state. Why does the Fermi sea play an essential role?"
  type: multiple-choice
  options:
    - "The Fermi sea provides a background potential that strengthens the attraction"
    - "The Fermi sea blocks the low-momentum states via the Pauli exclusion principle, restricting the pair to a thin shell near E_F where the density of states is high — this effective confinement to 2D in energy space allows a bound state for arbitrarily weak attraction, unlike the 3D free-space case which requires a minimum coupling strength"
    - "The Fermi sea contributes additional attractive interactions between the pair"
    - "Without the Fermi sea, the electrons would not have opposite momenta"
  answer: 1
  explanation: "In three-dimensional free space, a bound state requires the attractive potential to exceed a threshold. But at the Fermi surface, the Pauli exclusion principle confines the pair to a narrow energy shell of width ~ħω_D above E_F, effectively making the problem two-dimensional in energy. In 2D, any attractive potential — no matter how weak — supports a bound state. The Cooper pair binding energy is Δ ~ ħω_D exp(-1/N(0)V), which is nonzero for any V > 0 but exponentially small for weak coupling. This is why superconductivity is a weak-coupling instability of the Fermi sea."

- question: "The BCS ground state is not a state with a definite number of particles — it is a coherent superposition of states with different numbers of Cooper pairs. Why is this number uncertainty essential?"
  type: multiple-choice
  options:
    - "It is a mathematical convenience with no physical significance"
    - "The number-phase uncertainty relation (ΔN Δφ ≥ 1) means that a state with a well-defined macroscopic phase (needed for coherent supercurrent and the Josephson effect) must have uncertainty in particle number. The BCS state has a definite phase and indefinite particle number — this is the essence of off-diagonal long-range order and macroscopic quantum coherence"
    - "It accounts for electrons entering and leaving the superconductor"
    - "It corrects for the fact that electrons are indistinguishable"
  answer: 1
  explanation: "The BCS wavefunction |BCS> = Π_k(u_k + v_k c†_{k↑}c†_{-k↓})|0> is a product of terms, each of which is a superposition of pair-present (amplitude v_k) and pair-absent (amplitude u_k). This gives a definite phase relationship between different pair-number sectors. The macroscopic phase φ of the order parameter Δ = |Δ|e^{iφ} enables phenomena like the Josephson effect and flux quantization. A state with definite particle number would have completely uncertain phase and no supercurrent."

- question: "The BCS energy gap Δ(T) closes continuously at T_c and the transition is second-order. Below T_c, what physical quantity does Δ measure?"
  type: short-answer
  answer: "The energy gap Δ is the minimum energy required to break a Cooper pair into two individual quasiparticle excitations. It costs 2Δ to create a quasiparticle pair (one electron-like excitation above E_F and one hole-like excitation below). At T = 0, the gap is maximum: 2Δ(0) = 3.53 k_BT_c in weak-coupling BCS theory. As T → T_c, thermal fluctuations break pairs faster than they can form, Δ → 0, and the system transitions continuously to the normal state. The gap's existence is directly observable in tunneling experiments (sharp onset of current at voltage eV = Δ), infrared absorption (photons must exceed 2Δ to break pairs), and the exponential low-temperature specific heat C ∝ exp(-Δ/k_BT)."
  explanation: "The exponential specific heat is one of the clearest signatures of the gap: with no low-energy excitations available, the number of thermally excited quasiparticles drops exponentially as T → 0. This is qualitatively different from the linear-T specific heat of a normal metal."

- question: "Why do Cooper pairs form with zero total momentum (k↑, -k↓) rather than with finite center-of-mass momentum?"
  type: short-answer
  answer: "Zero total momentum maximizes the phase space for pairing. The phonon-mediated attraction operates between electrons in a thin shell of width ~ħω_D around the Fermi surface. For a pair with zero total momentum, both electrons sit on the Fermi surface, and ALL electrons in the shell can pair. If the pair had finite center-of-mass momentum Q, one electron would be at k and the other at -k+Q, and only electrons on the intersection of two displaced Fermi surface shells could pair — a much smaller phase space. Since the pairing energy depends exponentially on the available density of states, even a small reduction in phase space dramatically weakens pairing. This is why the BCS state strongly favors Q = 0 pairing."
  explanation: "The FFLO (Fulde-Ferrell-Larkin-Ovchinnikov) state is a rare exception where finite-Q pairing occurs under extreme conditions (large magnetic field with mismatched Fermi surfaces), but it requires very specific material properties and has been definitively observed in only a few systems."
```

## Explainer

BCS theory, published in 1957, is one of the great triumphs of many-body quantum mechanics. It explains superconductivity from first principles in three conceptual steps: the Cooper instability, the BCS ground state, and the energy gap.

**Step 1: Cooper pairs.** Leon Cooper showed in 1956 that two electrons above a filled Fermi sea, interacting via even an arbitrarily weak attractive potential (provided by phonon exchange), form a bound state. This is impossible in free space in 3D — you need a minimum coupling strength for binding. But the Fermi sea, by blocking all states below E_F, effectively confines the pair to a thin shell where the problem becomes 2D-like, and any attraction produces binding. The bound state has zero total momentum (k up, -k down) and a binding energy Delta ~ hbar omega_D exp(-1/N(0)V), which is small but nonzero for any V > 0.

**Step 2: The BCS ground state.** Cooper's result shows that the normal Fermi sea is unstable to pairing, but a single pair does not describe superconductivity — all electrons near E_F participate. The BCS ground state is a coherent superposition: |BCS> = product_k (u_k + v_k c^dagger_{k up} c^dagger_{-k down}) |0>, where u_k and v_k are variational parameters determined by minimizing the energy. The probability |v_k|^2 that the pair (k, -k) is occupied transitions smoothly from 1 below E_F to 0 above, with the transition width set by Delta. This is a fundamentally new state of matter: it has a definite macroscopic phase (enabling supercurrents) but indefinite particle number, embodying macroscopic quantum coherence.

**Step 3: The energy gap.** The BCS state has a gap Delta in the quasiparticle excitation spectrum: it costs at least 2Delta to break a Cooper pair. This gap is the reason for zero resistance — there are no low-energy excitations to scatter into. The gap equation is 1/V = integral [1/(2 sqrt(xi^2 + Delta^2))] tanh(sqrt(xi^2 + Delta^2)/(2k_BT)) dxi, which determines Delta(T) self-consistently. At T = 0, the weak-coupling result is 2Delta(0) = 3.53 k_BT_c. The gap closes continuously at T_c (second-order transition) with the mean-field behavior Delta(T) proportional to (T_c - T)^{1/2} near T_c.

BCS theory quantitatively predicts the critical temperature, the specific heat jump at T_c (Delta C/gamma T_c = 1.43), the coherence length xi_0 = hbar v_F / (pi Delta), the penetration depth, and the nuclear spin relaxation rate (Hebel-Slichter peak). Its success established the phonon mechanism for conventional superconductors and earned Bardeen, Cooper, and Schrieffer the 1972 Nobel Prize. The theory's limitations — it applies to weak-coupling, s-wave pairing in clean materials — are precisely what makes the study of unconventional superconductors (cuprates, iron-based, heavy-fermion) so challenging and interesting.
