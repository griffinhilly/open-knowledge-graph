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

## Explainer

From electronic spectroscopy, you know that molecules absorb light to jump between electronic states — from a ground-state potential energy curve to an excited-state curve. From vibrational spectroscopy, you know that nuclei within a molecule vibrate around their equilibrium positions, described by vibrational wavefunctions on those potential curves. The Franck-Condon principle connects these two ideas by explaining which vibrational levels of the excited state are reached most strongly during an electronic transition, and therefore why absorption bands have the shapes they do.

The key physical insight is a matter of timescales. An electronic transition happens in roughly 10⁻¹⁵ seconds (a femtosecond), while nuclear motion occurs on the timescale of 10⁻¹³ seconds (a vibrational period). The nuclei are essentially frozen during the electronic jump. On a potential energy diagram, this means the transition is **vertical** — the molecule goes straight up from its current nuclear geometry to whatever point on the excited-state curve sits directly above. The nuclei do not have time to relax to the new equilibrium geometry during the transition itself. This is why it is sometimes called the "vertical transition" approximation.

Quantum mechanically, the probability of landing in a particular vibrational level v' of the excited state (starting from v'' = 0 in the ground state, which is where most molecules sit at room temperature) is proportional to the **Franck-Condon factor**: the square of the overlap integral |⟨χ_v'|χ_v''⟩|². This integral measures how well the vibrational wavefunction of the target level overlaps spatially with the vibrational wavefunction of the starting level. If the two electronic states have nearly identical equilibrium bond lengths and force constants — their potential curves sit almost directly above each other — then the v'' = 0 wavefunction overlaps best with v' = 0, and the **0–0 transition** dominates. But if the excited state has a significantly longer or shorter equilibrium bond (the upper curve is displaced horizontally), then the v'' = 0 wavefunction overlaps best with a higher vibrational level of the excited state, and the most intense band shifts to a higher v' value.

This principle gives absorption spectra their characteristic shape: a series of bands forming a **vibrational progression**, with the intensity envelope peaking at the vibronic transition with the largest Franck-Condon factor. The classic example is I₂, whose visible absorption spectrum shows a long progression of evenly spaced bands because the excited state has a much longer bond than the ground state, so the vertical transition lands high up the vibrational ladder. The same logic applies in reverse to emission. After absorbing light and reaching a high v' level, the molecule quickly relaxes vibrationally to v' = 0 of the excited state (Kasha's rule), then emits by a vertical transition downward. The emission spectrum is therefore a mirror image of the absorption spectrum, displaced to lower energy — the **mirror image rule** — because the Franck-Condon factors for emission are governed by the same geometric displacement, just traversed in the opposite direction.
