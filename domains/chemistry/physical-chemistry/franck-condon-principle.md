---
id: franck-condon-principle
title: The Franck-Condon Principle and Vibronic Transitions
domain: chemistry
course: physical-chemistry
prerequisites:
- id: electronic-spectroscopy-theory
  type: hard
- id: vibrational-modes-and-symmetry
  type: hard
builds-toward: []
tags:
- Franck-Condon
- vertical-transitions
- vibrational-overlap
- vibronic
- absorption-band-shape
- potential-energy-curves
stage: advanced
status: draft
---

# The Franck-Condon Principle and Vibronic Transitions

## Core Idea
The Franck-Condon principle states that electronic transitions occur so rapidly (on the order of femtoseconds) that the nuclei have no time to move during the transition -- the transition is "vertical" on a potential energy surface diagram. The probability of a particular vibronic transition (from vibrational level v'' in the ground electronic state to v' in the excited state) is proportional to the square of the Franck-Condon factor: |<chi_v'|chi_v''>|^2, the overlap integral between the vibrational wavefunctions of the two electronic states. When the excited state has a significantly different equilibrium geometry (shifted potential energy curve), the maximum overlap -- and therefore the most intense absorption band -- occurs not at the 0-0 transition but at a higher vibrational level of the excited state. This principle explains the characteristic vibrational progressions seen in UV-Vis absorption and emission spectra.

## How It's Best Learned
Draw two displaced harmonic potential energy curves and sketch the vibrational wavefunctions on each. Identify which v''-to-v' overlaps are large by visual inspection (vertical transition from the v''=0 turning point), then compare to experimental absorption spectra of molecules like I2 or S2 that show clear vibronic progressions.

## Common Misconceptions
- Assuming the 0-0 transition is always the most intense; this is only true when the two electronic states have nearly identical equilibrium geometries and force constants.
- Forgetting that the Franck-Condon principle applies equally to emission; fluorescence spectra show a mirror-image vibrational progression governed by the same overlap integrals.
