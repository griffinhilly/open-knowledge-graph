---
id: harmonic-oscillator-molecular-vibrations
title: Quantum Harmonic Oscillator and Molecular Vibrations
domain: chemistry
course: physical-chemistry
prerequisites:
- id: quantum-chemistry-foundations
  type: hard
- id: particle-in-a-box
  type: soft
- id: simple-harmonic-motion
  type: soft
- id: spring-mass-system
  type: soft
- id: differential-equations-intro-separable
  type: soft
builds-toward:
- vibrational-spectroscopy-theory
- selection-rules-spectroscopy
- statistical-thermodynamics-applications
tags:
- harmonic-oscillator
- vibrations
- zero-point-energy
- ladder-operators
stage: advanced
status: validated
---

# Quantum Harmonic Oscillator and Molecular Vibrations

## Core Idea
The quantum harmonic oscillator (QHO) models molecular bond stretching and bending vibrations. Its energy levels are equally spaced: E_v = ℏω(v + 1/2), where v = 0, 1, 2, … The zero-point energy ℏω/2 persists even at absolute zero, reflecting the uncertainty principle. Wavefunctions are Hermite polynomials multiplied by a Gaussian envelope, and they extend into classically forbidden regions (tunneling). The anharmonic Morse potential is a more realistic model for real bonds, accounting for bond dissociation at high vibrational quantum numbers.

## How It's Best Learned
Verify the equally spaced energy levels first, then focus on the physical meaning of zero-point energy. Compare the QHO to the Morse oscillator to see how anharmonicity leads to overtone transitions in IR spectra.

## Common Misconceptions
- Forgetting zero-point energy — bonds always vibrate, even at 0 K.
- Assuming the harmonic model is exact; it is only valid for small displacements from equilibrium.

## Questions

```yaml
- question: "The ground-state energy of a quantum harmonic oscillator is E_0 = ℏω/2, not zero. Which principle most directly requires this non-zero ground state?"
  type: multiple-choice
  options:
    - "The Pauli exclusion principle, which prevents two particles from sharing the same quantum state."
    - "The Heisenberg uncertainty principle, which forbids a particle from simultaneously having zero position uncertainty (at equilibrium) and zero momentum."
    - "The Born-Oppenheimer approximation, which separates nuclear and electronic motion."
    - "Conservation of energy, which requires vibrational energy to be stored somewhere at all temperatures."
  answer: 1
  explanation: "If the oscillator had zero energy, it would sit motionless at the equilibrium position — its position and momentum would both be exactly zero, violating the uncertainty relation ΔxΔp ≥ ℏ/2. The zero-point energy ℏω/2 is the minimum energy consistent with this uncertainty. This is not a measurement artifact; it has physical consequences: even at 0 K, molecular bonds vibrate, which affects isotope effects, tunnel rates, and thermodynamic properties."

- question: "The quantum harmonic oscillator has equally spaced energy levels. This equal spacing means a real diatomic molecule's vibrational transitions should most appear at exactly the same frequency in an IR spectrum."
  type: true-false
  answer: false
  explanation: "Equal spacing holds only for the ideal harmonic potential. Real bonds follow an anharmonic potential (approximated by the Morse potential), where the restoring force weakens as the bond stretches toward dissociation. This causes the energy level spacing to decrease with increasing v. As a result, the fundamental (v=0→1) and overtones (v=0→2, 0→3) appear at slightly different frequencies, and at high enough energy the levels converge and the bond dissociates."

- question: "A quantum harmonic oscillator wavefunction has finite amplitude in regions where the total energy is less than the potential energy — classically forbidden zones. What is this phenomenon called, and what observable spectroscopic consequence does it have?"
  type: short-answer
  answer: "Quantum mechanical tunneling. Because wavefunctions decay exponentially rather than abruptly into classically forbidden regions, there is a non-zero probability of finding the bond stretched beyond its classical turning point. In spectroscopy, tunneling enables hydrogen-atom transfer reactions and contributes to the intensities of combination bands. It also underlies the fact that zero-point energy is non-zero: the particle cannot be localized at the potential minimum without kinetic energy."
  explanation: "In classical mechanics, a particle with energy E cannot penetrate a region where V > E. In quantum mechanics the wavefunction decays exponentially in such regions (evanescent behavior) but does not vanish, allowing tunneling through thin barriers. This is directly observable: reaction rates of proton-transfer reactions are much faster than predicted classically at low temperatures, due to tunneling through the activation barrier."
```

## Explainer

The classical harmonic oscillator — a mass on a spring — has a continuous range of energies depending on how far you stretch it. Its quantum counterpart has something fundamentally different: energy comes in discrete packages. The allowed vibrational energies are E_v = ℏω(v + 1/2), where v = 0, 1, 2, … is the vibrational quantum number and ω = √(k/μ) is the angular frequency set by the force constant k and reduced mass μ. The energy levels are equally spaced by ℏω, much like the equally spaced levels you saw in the particle-in-a-box, but now the potential is curved rather than flat.

The term v + 1/2 rather than v contains a crucial message: even the lowest state (v = 0) has energy ℏω/2, not zero. This zero-point energy is a direct consequence of the uncertainty principle. A particle confined to a potential well cannot be simultaneously at rest at the minimum — that would require ΔxΔp = 0. Instead it must have some residual kinetic energy, which is the zero-point energy. This is not a curiosity: zero-point energy is physically real. It keeps helium liquid at atmospheric pressure even at 0 K, it contributes to isotope effects in chemical reactions (heavier isotopes have lower ω and lower zero-point energy, changing reaction rates), and it means molecular bonds are always vibrating.

The wavefunctions of the QHO are Hermite polynomials multiplied by a Gaussian, ψ_v(x) = N_v · H_v(αx) · e^(−α²x²/2). For v = 0, this is a simple Gaussian centered at equilibrium — the particle is most likely found near the center. Higher v states show more nodes and larger spatial spread. Critically, the wavefunctions extend into the classically forbidden regions beyond the classical turning points. This quantum tunneling has real spectroscopic consequences: it is partly why proton-transfer reactions can proceed faster than a classical analysis predicts.

In connecting this to molecular spectroscopy, the force constant k corresponds to the curvature of the potential energy surface at the bond's equilibrium length. Stiff bonds (like C≡C) have large k and high ω, absorbing IR light at high wavenumber. Weak bonds (like H-bonds) absorb at low wavenumber. Because the reduced mass μ also enters ω, isotopic substitution (e.g., H → D) shifts vibrational frequencies predictably — this is isotopic labeling, a powerful tool in structural chemistry.

The harmonic model is an approximation, valid only for small displacements. For large v, the real potential — better described by the Morse potential V(r) = D_e(1 − e^(−a(r−r_e)))² — deviates significantly. The Morse levels converge and ultimately the bond dissociates. This anharmonicity relaxes the strict Δv = ±1 selection rule, allowing overtone transitions (Δv = ±2, ±3) to appear with weaker intensity in IR spectra. The quantum harmonic oscillator is thus not just a model — it is the first rung of a ladder that leads to quantitative prediction of every molecular vibration in an IR or Raman spectrum.
