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
- id: quantum-harmonic-oscillator
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

## Questions

```yaml
- question: "A nonlinear molecule contains 4 atoms. How many vibrational normal modes does it have?"
  type: multiple-choice
  options:
    - "12"
    - "7"
    - "6"
    - "9"
  answer: 2
  explanation: "For a nonlinear molecule with N atoms, the number of vibrational modes is 3N − 6. With N = 4: 3(4) − 6 = 6. The 3N total degrees of freedom minus 3 translational and 3 rotational leaves 6 vibrational. (For a linear molecule it would be 3N − 5 = 7, since linear molecules have only 2 rotational degrees of freedom.)"

- question: "For a centrosymmetric molecule, the mutual exclusion rule states that no vibrational mode can be simultaneously IR-active and Raman-active."
  type: true-false
  answer: true
  explanation: "Centrosymmetric molecules (those with an inversion center, like CO₂ or C₂H₂) have modes that are either symmetric (gerade, 'g') or antisymmetric (ungerade, 'u') with respect to inversion. IR activity requires breaking inversion symmetry (u modes), while Raman activity requires preserving it (g modes). No mode can satisfy both simultaneously, so IR-active and Raman-active sets are mutually exclusive."

- question: "What physical criterion determines whether a vibrational normal mode is IR-active?"
  type: short-answer
  answer: "A mode is IR-active if the vibration produces a change in the molecular electric dipole moment (∂μ/∂Q ≠ 0, where Q is the normal coordinate). If the dipole moment does not change during the vibration, the mode cannot absorb infrared radiation."
  explanation: "Infrared absorption occurs when the oscillating electric field of IR radiation couples to an oscillating dipole in the molecule. If a vibration is symmetric and produces no dipole change (as in the symmetric stretch of CO₂), there is nothing for the IR field to couple to, and the mode is IR-inactive. This selection rule comes directly from time-dependent perturbation theory applied to the interaction between radiation and molecular dipoles."
```

## Explainer

When a molecule vibrates, all of its atoms move simultaneously in coordinated patterns. Rather than thinking of each bond as an independent spring, quantum mechanics shows that the natural modes of vibration — normal modes — are collective motions of the entire molecule. Each normal mode has all atoms moving with the same frequency and in phase, but with different amplitudes at different atomic positions. These are the eigenvectors of the mass-weighted Hessian (the matrix of second derivatives of the molecular potential energy surface), and they are the fundamental units of molecular vibration.

The count of normal modes follows directly from the degrees of freedom argument. A molecule of N atoms has 3N total degrees of freedom (three Cartesian coordinates per atom). Three of these describe the center-of-mass translation, and three describe rotation (two for a linear molecule, which cannot rotate about its own axis). The remaining degrees of freedom must be vibrational: 3N − 6 for nonlinear molecules, 3N − 5 for linear ones. This formula is worth internalizing — students frequently forget the linear-molecule exception, which leads to wrong mode counts for molecules like CO₂ and HCN.

Whether a given normal mode appears in an IR spectrum depends on the selection rule: the vibration must change the molecular dipole moment (∂μ/∂Q ≠ 0). Physically, an IR photon is absorbed when its oscillating electric field can couple to an oscillating dipole in the molecule. Symmetric stretches of centrosymmetric molecules — like the symmetric C=O stretch of CO₂ — do not alter the dipole moment and are therefore IR-inactive. Asymmetric stretches and bends that distort the charge distribution are IR-active. Raman spectroscopy uses a complementary selection rule: a mode is Raman-active if the vibration changes the molecular polarizability (∂α/∂Q ≠ 0). The two techniques are thus complementary detectors of different aspects of molecular geometry.

For centrosymmetric molecules, the mutual exclusion rule applies: no mode can be both IR-active and Raman-active simultaneously. This is a consequence of inversion symmetry — modes that are symmetric (gerade, g) with respect to inversion are Raman-active but IR-inactive, while antisymmetric (ungerade, u) modes are IR-active but Raman-inactive. CO₂ is the canonical example: its symmetric stretch is Raman-active and IR-inactive; its asymmetric stretch and bends are IR-active and Raman-inactive. This complementarity makes IR and Raman spectroscopy together more informative than either alone.

Real molecular vibrations deviate from the ideal harmonic oscillator in ways that show up in spectra. Anharmonicity — the departure of the true potential well from a perfect parabola — means vibrational energy levels are not perfectly equally spaced, and transitions with Δv = ±2 (overtones) and Δv = 0 for one mode combined with Δv = ±1 for another (combination bands) become weakly allowed. These extra features in an IR spectrum are often diagnostic but require the harmonic selection rules as a starting point to interpret.
