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

## Questions

```yaml
- question: "A diatomic molecule has an excited electronic state with a significantly longer equilibrium bond length than the ground state. Starting from v''=0 in the ground state, which vibronic transition do you expect to be the most intense in the absorption spectrum?"
  type: multiple-choice
  options:
    - "The 0–0 transition, because it requires the minimum photon energy and is therefore most probable"
    - "The 0–0 transition, because ground-state vibrational wavefunctions always overlap most with v'=0 of the excited state"
    - "A transition to a high vibrational level v' > 0 of the excited state, because the vertical jump from v''=0 lands near the turning point of that level"
    - "The transition to the highest accessible vibrational level, because greater energy transfer maximizes photon absorption"
  answer: 2
  explanation: "The Franck-Condon principle says transitions are vertical: the nuclear geometry is frozen during the femtosecond-timescale electronic jump. When the excited state has a longer equilibrium bond length, its potential curve is displaced to the right. The v''=0 wavefunction (peaked near the ground-state equilibrium geometry) now overlaps most with a high vibrational level of the excited state, whose wavefunction has a turning-point maximum near that same geometry. Option A and B represent the common misconception that the 0–0 transition dominates regardless of geometry — this is only true when the two states have nearly identical equilibrium structures."

- question: "A molecule absorbs UV light and its fluorescence (emission) spectrum is measured. According to the Franck-Condon principle and Kasha's rule, the emission spectrum compared to the absorption spectrum should be:"
  type: multiple-choice
  options:
    - "Identical to the absorption spectrum, because the same FC overlap integrals govern both processes"
    - "A mirror image of the absorption spectrum, displaced to lower energy (redshifted)"
    - "A broad featureless band, because rapid vibrational relaxation destroys the vibrational structure before emission"
    - "Dominated by a single sharp 0–0 line, because emission always terminates at the lowest vibrational level of the ground state"
  answer: 1
  explanation: "After absorbing light, the molecule rapidly relaxes to v'=0 of the excited state (Kasha's rule) before emitting. Emission then proceeds as a vertical downward transition, and the same geometric displacement that shaped absorption also shapes emission — but now traversed in reverse. The FC factors are symmetric, producing the same progression envelope but shifted to lower energy (the 0–0 gap must be crossed before vibrational levels of the ground state are accessed). This mirror-image rule is diagnostic in spectroscopy: a clear mirror-image relationship between absorption and emission spectra confirms vibrational progressions governed by the same potential energy displacement."

- question: "When two electronic states have nearly identical equilibrium geometries and force constants, the 0–0 transition dominates the absorption spectrum and transitions to higher vibrational levels of the excited state are weak."
  type: true-false
  answer: true
  explanation: "If the two potential energy curves sit nearly directly above each other (no horizontal displacement), then a vertical transition from v''=0 lands near the bottom of the excited-state curve — precisely where v'=0 has its largest amplitude. The FC overlap integral |⟨χ_v'=0|χ_v''=0⟩|² is large, while overlaps with higher v' levels are small because their wavefunctions have low amplitude near the equilibrium geometry. The misconception to avoid is assuming this is always the case; strong vibrational progressions (e.g., in I₂) reveal significant geometry change between states."

- question: "A molecule initially in v''=0 of the ground electronic state can be excited to multiple different vibrational levels of the excited electronic state in a single absorption experiment, each with a different probability."
  type: true-false
  answer: true
  explanation: "This is the direct meaning of the vibrational progression in an absorption spectrum: each band corresponds to a distinct v''=0 → v' transition, and the intensity of each band reflects its Franck-Condon factor |⟨χ_v'|χ_v''=0⟩|². Absorption is not restricted to a single final state — it populates a distribution of vibrational levels, with the envelope shaped by the FC factors. This is why UV-Vis spectra of diatomics often show a series of regularly spaced bands rather than a single line."

- question: "Why does the 'vertical' nature of an electronic transition mean the 0–0 band is not always the most intense, even though it involves the smallest energy change?"
  type: short-answer
  answer: "Transition probability is governed by the Franck-Condon factor — the square of the overlap integral between the vibrational wavefunctions of the initial and final levels — not by the energy gap. A vertical transition preserves the nuclear geometry, so the molecule arrives at whatever point on the excited-state potential energy surface sits directly above its starting geometry. If the excited state has a different equilibrium bond length, this vertical landing point does not correspond to v'=0 (which sits at the new equilibrium) but to a higher vibrational level whose turning point is near the old equilibrium geometry. The 0–0 FC overlap is therefore small, and the most intense band shifts to higher v'."
  explanation: "This insight — that band intensities encode geometry changes between electronic states — makes FC analysis a powerful structural tool: the position and shape of the vibrational progression in an absorption spectrum directly reveals how much the equilibrium geometry changes upon electronic excitation. Long progressions (like I₂) signal large geometry changes; short progressions signal minimal changes. The principle connects quantum mechanical wavefunctions to observable spectral shapes."
```

## Explainer

From electronic spectroscopy, you know that molecules absorb light to jump between electronic states — from a ground-state potential energy curve to an excited-state curve. From vibrational spectroscopy, you know that nuclei within a molecule vibrate around their equilibrium positions, described by vibrational wavefunctions on those potential curves. The Franck-Condon principle connects these two ideas by explaining which vibrational levels of the excited state are reached most strongly during an electronic transition, and therefore why absorption bands have the shapes they do.

The key physical insight is a matter of timescales. An electronic transition happens in roughly 10⁻¹⁵ seconds (a femtosecond), while nuclear motion occurs on the timescale of 10⁻¹³ seconds (a vibrational period). The nuclei are essentially frozen during the electronic jump. On a potential energy diagram, this means the transition is **vertical** — the molecule goes straight up from its current nuclear geometry to whatever point on the excited-state curve sits directly above. The nuclei do not have time to relax to the new equilibrium geometry during the transition itself. This is why it is sometimes called the "vertical transition" approximation.

Quantum mechanically, the probability of landing in a particular vibrational level v' of the excited state (starting from v'' = 0 in the ground state, which is where most molecules sit at room temperature) is proportional to the **Franck-Condon factor**: the square of the overlap integral |⟨χ_v'|χ_v''⟩|². This integral measures how well the vibrational wavefunction of the target level overlaps spatially with the vibrational wavefunction of the starting level. If the two electronic states have nearly identical equilibrium bond lengths and force constants — their potential curves sit almost directly above each other — then the v'' = 0 wavefunction overlaps best with v' = 0, and the **0–0 transition** dominates. But if the excited state has a significantly longer or shorter equilibrium bond (the upper curve is displaced horizontally), then the v'' = 0 wavefunction overlaps best with a higher vibrational level of the excited state, and the most intense band shifts to a higher v' value.

This principle gives absorption spectra their characteristic shape: a series of bands forming a **vibrational progression**, with the intensity envelope peaking at the vibronic transition with the largest Franck-Condon factor. The classic example is I₂, whose visible absorption spectrum shows a long progression of evenly spaced bands because the excited state has a much longer bond than the ground state, so the vertical transition lands high up the vibrational ladder. The same logic applies in reverse to emission. After absorbing light and reaching a high v' level, the molecule quickly relaxes vibrationally to v' = 0 of the excited state (Kasha's rule), then emits by a vertical transition downward. The emission spectrum is therefore a mirror image of the absorption spectrum, displaced to lower energy — the **mirror image rule** — because the Franck-Condon factors for emission are governed by the same geometric displacement, just traversed in the opposite direction.
