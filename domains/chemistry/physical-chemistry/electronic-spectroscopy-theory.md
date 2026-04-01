---
id: electronic-spectroscopy-theory
title: Electronic Spectroscopy and the Franck-Condon Principle
domain: chemistry
course: physical-chemistry
prerequisites:
- id: molecular-orbital-theory-advanced
  type: hard
- id: selection-rules-spectroscopy
  type: hard
- id: harmonic-oscillator-molecular-vibrations
  type: soft
- id: emission-absorption-spectra
  type: soft
- id: electromagnetic-waves
  type: soft
- id: photon-model
  type: soft
- id: huckel-molecular-orbital-theory
  type: soft
- id: vibrational-modes-and-symmetry
  type: soft
- id: photon-concept-quanta
  type: soft
tags:
- UV-Vis
- Franck-Condon
- Born-Oppenheimer
- vibronic
- fluorescence
- phosphorescence
stage: advanced
status: validated
---
# Electronic Spectroscopy and the Franck-Condon Principle

## Core Idea
Electronic spectroscopy involves transitions between electronic states, typically in the UV-Visible range (200–800 nm). The Franck-Condon principle states that electronic transitions are so fast that nuclear positions and momenta are essentially unchanged: the transition is 'vertical' on the potential energy surface diagram. The intensity of each vibrational component (vibronic band) is proportional to the square of the Franck-Condon factor ⟨v'|v⟩², the overlap integral between vibrational wavefunctions of the two electronic states. Excited states can relax via fluorescence (spin-allowed) or phosphorescence (spin-forbidden), with rates governed by the Einstein A and B coefficients.

## How It's Best Learned
Draw potential energy curves for two electronic states with different equilibrium geometries. Identify which v=0→v' transition has maximum intensity from the Franck-Condon overlap, and use this to explain vibrational structure in UV absorption spectra.

## Common Misconceptions
- Confusing fluorescence (singlet→singlet) with phosphorescence (triplet→singlet); the latter is slow due to spin-forbidden nature.
- Assuming the most intense peak is always the 0→0 transition; this is only true if both states have identical geometries.

## Questions

```yaml
- question: "In a UV absorption spectrum, which transition has the greatest intensity according to the Franck-Condon principle?"
  type: multiple-choice
  options:
    - "Always the v=0 → v'=0 transition"
    - "The transition to the v' level whose wavefunction has the greatest overlap with the ground-state v=0 wavefunction"
    - "The transition to the highest vibrational level of the excited state"
    - "The transition with the largest energy gap"
  answer: 1
  explanation: "The Franck-Condon principle says intensity is proportional to |⟨v'|v⟩|². The most intense band corresponds to the excited-state vibrational level whose wavefunction overlaps most with the ground-state wavefunction. When excited and ground electronic states have the same equilibrium geometry, this IS the 0→0 transition — but when geometries differ (the common case), the maximum shifts to a higher v'."

- question: "Phosphorescence is slower than fluorescence because it involves a spin-forbidden transition from a triplet excited state back to the singlet ground state."
  type: true-false
  answer: true
  explanation: "Fluorescence is a singlet→singlet (S₁→S₀) radiative transition, which is spin-allowed and occurs on nanosecond timescales. Phosphorescence involves intersystem crossing from S₁ to the triplet state T₁, followed by a T₁→S₀ emission. Because this requires a spin flip, it violates the spin selection rule and is slow — occurring on microsecond to second timescales. This is why phosphorescent materials continue glowing after the excitation source is removed."

- question: "Why is the Franck-Condon transition described as 'vertical' on a potential energy diagram?"
  type: short-answer
  answer: "Because electronic transitions occur so rapidly (~10⁻¹⁵ s) that nuclei cannot move during the event — both nuclear positions and momenta are essentially frozen. On a potential energy vs. internuclear distance diagram, the transition appears as a vertical arrow from the ground-state vibrational wavefunction up to the excited-state potential curve at the same nuclear coordinate."
  explanation: "This follows from the Born-Oppenheimer approximation: electrons move on a timescale many orders of magnitude faster than nuclei. The electronic transition is complete before the nuclei have time to respond, so the nuclear geometry at the moment of absorption is the same as in the initial state. This verticality determines which vibrational levels of the excited state are populated."
```

## Explainer

Electronic spectroscopy probes transitions between different electronic states of a molecule — typically from the ground state (S₀) to an excited singlet state (S₁ or S₂) — using UV-Visible light. From your study of molecular orbital theory, you know that electrons occupy bonding, nonbonding, and antibonding MOs. Absorbing a photon in the 200–800 nm range promotes an electron to a higher MO, changing the molecule's electronic configuration entirely. The energy of that photon must match the energy gap between the two electronic states, which is why different chromophores absorb at characteristic wavelengths.

The key physics governing which vibrational bands appear in the spectrum is the Franck-Condon principle. Electronic transitions happen on the order of femtoseconds (10⁻¹⁵ s), while nuclear vibrations occur on picosecond timescales — roughly a thousand times slower. Because nuclei are essentially frozen during the transition, the molecule is instantaneously placed on the excited-state potential energy surface at the same nuclear geometry it had in the ground state. On a potential energy diagram, this appears as a vertical arrow. The excited-state vibrational level that gets populated most is the one whose wavefunction has the greatest spatial overlap with the ground-state v=0 wavefunction — this overlap is quantified by the Franck-Condon factor ⟨v'|v⟩². If the equilibrium bond length is longer in the excited state (common when an antibonding MO is populated), the potential energy minimum shifts outward, and vertical transitions land partway up the excited-state well, producing a vibrational progression with maximum intensity at a higher v'.

After absorption, the excited molecule has several decay pathways. It can emit a photon in the reverse process — fluorescence — returning from S₁ to S₀. This is spin-allowed (singlet→singlet) and fast, typically occurring within nanoseconds. Alternatively, the molecule can undergo intersystem crossing to the lowest triplet state T₁, a spin-state change that is slow but becomes relevant when heavy atoms or extended conjugation enhance spin-orbit coupling. Emission from T₁→S₀ is phosphorescence. Because it requires a spin flip (spin-forbidden), it is much slower — persisting for microseconds to seconds — which is why phosphorescent materials glow in the dark long after the light is removed.

A common error is assuming the 0→0 transition is always the most intense peak. This is only true when the ground and excited states have nearly identical geometries. In practice, the equilibrium geometry often changes upon electronic excitation — bond lengths, angles, or even the overall molecular shape shifts — and the Franck-Condon maximum moves to higher v'. Recognizing this lets you read a UV-Vis spectrum to infer geometric changes: a long vibrational progression with maximum intensity far from 0→0 implies a large geometry change upon excitation.
