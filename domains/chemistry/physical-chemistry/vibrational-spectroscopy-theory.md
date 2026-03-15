---
id: vibrational-spectroscopy-theory
title: 'Vibrational Spectroscopy: Theory and Normal Modes'
domain: chemistry
course: physical-chemistry
prerequisites:
- id: harmonic-oscillator-molecular-vibrations
  type: hard
- id: selection-rules-spectroscopy
  type: hard
- id: ir-spectroscopy-basics
  type: soft
- id: simple-harmonic-motion
  type: soft
- id: wave-properties-intro
  type: soft
- id: electromagnetic-spectrum
  type: soft
- id: born-oppenheimer-approximation
  type: soft
- id: rotational-spectroscopy
  type: soft
- id: harmonic-oscillator-quantum
  type: soft
builds-toward:
- raman-spectroscopy-theory
- vibrational-modes-and-symmetry
tags:
- normal-modes
- IR-active
- Raman-active
- anharmonicity
- overtones
- combination-bands
stage: advanced
status: validated
---
# Vibrational Spectroscopy: Theory and Normal Modes

## Core Idea
A nonlinear molecule with N atoms has 3N−6 vibrational degrees of freedom, each described as a normal mode — a collective, synchronized motion of all atoms. Normal modes are found by diagonalizing the mass-weighted Hessian (second derivative of potential energy). A mode is IR-active if it changes the molecular dipole moment (selection rule: ∂μ/∂Q ≠ 0) and Raman-active if it changes the polarizability (∂α/∂Q ≠ 0). The mutual exclusion rule states that for centrosymmetric molecules, no mode can be both IR and Raman active. Anharmonicity introduces overtones (Δv = ±2) and combination bands in observed spectra.

## How It's Best Learned
Work through the normal mode analysis of CO₂ and H₂O to see how symmetry governs activity. Apply the mutual exclusion rule to CO₂, then use group theory to categorize modes of larger molecules.

## Common Misconceptions
- Thinking each peak in an IR spectrum corresponds to one bond stretching — complex molecules show normal modes where many bonds move together.
- Forgetting linear molecules have 3N−5 modes, not 3N−6.
