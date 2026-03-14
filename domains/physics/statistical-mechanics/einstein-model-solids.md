---
id: einstein-model-solids
title: The Einstein Model of Solids
domain: physics
course: statistical-mechanics
prerequisites:
- id: quantum-harmonic-oscillator
  type: hard
- id: planck-distribution-blackbody
  type: soft
builds-toward:
- debye-model-lattice-dynamics
tags:
- einstein-model
- harmonic-oscillator
- specific-heat
stage: advanced
status: draft
---

# The Einstein Model of Solids

## Core Idea
Einstein modeled a crystal as 3N independent quantum harmonic oscillators (one per atom). Each oscillator has energy levels E_n = ℏω(n + 1/2). At high T, this recovers the Dulong-Petit law C_V = 3Nk. At low T, the exponential Boltzmann suppression of excited states gives C_V ∝ exp(-ℏω/kT), predicting very soft specific heat that overshoots the observed T³ behavior.
