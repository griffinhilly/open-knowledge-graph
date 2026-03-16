---
id: vibrational-energy-levels-selection-rules
title: Vibrational Energy Levels and Selection Rules
domain: chemistry
course: physical-chemistry
prerequisites:
- id: harmonic-oscillator-molecular-vibrations
  type: hard
- id: vibrational-spectroscopy-theory
  type: hard
builds-toward:
- vibrational-frequency-force-constant
- infrared-spectroscopy-applications
tags:
- vibrational-spectroscopy
- selection-rules
- energy-levels
stage: advanced
status: draft
---

# Vibrational Energy Levels and Selection Rules

## Core Idea
Quantum vibrational states are quantized: E_v = ℏω(v + 1/2) where v = 0, 1, 2,... IR-active transitions require Δv = ±1 and a change in dipole moment along the vibration. Overtones (Δv = ±2, ±3,...) are typically forbidden or very weak. Hot bands from thermally populated excited states appear at lower frequency than fundamental transitions.

## How It's Best Learned
Measure IR spectrum of a diatomic or small polyatomic molecule; identify fundamental, overtone, and hot band transitions. Relate intensities to Franck-Condon factors and dipole moment derivatives.

## Explainer

From the harmonic oscillator model, you know that a vibrating diatomic molecule behaves approximately like a mass on a spring, with the potential energy rising parabolically as the bond stretches or compresses. Quantum mechanics tells us that such a system cannot vibrate with arbitrary energy — its energy is **quantized** into discrete levels given by E_v = ℏω(v + ½), where v is the vibrational quantum number (0, 1, 2, ...) and ω is the angular frequency determined by the bond's force constant and the reduced mass. The ½ in the formula means that even at v = 0, the molecule has **zero-point energy** — it never stops vibrating entirely, a direct consequence of the Heisenberg uncertainty principle.

The spacing between adjacent vibrational levels is uniform in the harmonic approximation: ΔE = ℏω regardless of which level you start from. This sets the stage for the **selection rule** Δv = ±1, which says that in a harmonic oscillator, only transitions between neighboring levels are allowed. The physical basis is that the transition dipole moment integral vanishes for Δv ≠ ±1 when the potential is exactly parabolic. The transition from v = 0 to v = 1 is the **fundamental**, and it dominates the IR spectrum.

But there is a second requirement: the vibration must cause a **change in dipole moment**. This is why homonuclear diatomics like N₂ and O₂ are IR-invisible — stretching the bond does not change the dipole moment (which is zero by symmetry at all bond lengths). Heteronuclear diatomics like HCl are IR-active because stretching the bond changes the charge separation. For polyatomic molecules, each normal mode is independently IR-active or inactive depending on whether that particular vibration modulates the molecular dipole.

Real molecules are not perfect harmonic oscillators. The true potential is **anharmonic** — it flattens out as the bond stretches toward dissociation and steepens at very short distances. Anharmonicity has two consequences: it makes the energy levels progressively closer together at higher v, and it relaxes the Δv = ±1 selection rule, allowing weak **overtone** transitions (Δv = ±2, ±3). Overtones appear in the spectrum at roughly twice, three times, etc., the fundamental frequency, but with rapidly decreasing intensity. **Hot bands** arise from transitions originating in thermally populated excited states (e.g., v = 1 → v = 2). Because anharmonicity compresses the spacing, hot bands appear at slightly lower frequency than the fundamental. Their intensity increases with temperature as more molecules occupy higher vibrational states, providing a direct spectroscopic thermometer for molecular vibration.
