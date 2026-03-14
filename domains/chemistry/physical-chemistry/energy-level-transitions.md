---
id: energy-level-transitions
title: Quantized Energy Levels and Spectroscopic Transitions
domain: chemistry
course: physical-chemistry
prerequisites:
- id: quantum-chemistry-foundations
  type: hard
builds-toward:
- fluorescence-and-phosphorescence-theory
tags:
- energy-levels
- absorption
- emission
- Boltzmann-population
- line-spectra
- quantization
stage: advanced
status: draft
---

# Quantized Energy Levels and Spectroscopic Transitions

## Core Idea
Quantum mechanics restricts atoms and molecules to discrete energy levels, and transitions between these levels occur by absorption or emission of photons with energy exactly matching the level spacing: Delta-E = h*nu. The Boltzmann distribution governs the population of each level at thermal equilibrium: N_i/N_0 = (g_i/g_0)*exp(-Delta-E_i/k_BT), where g_i is the degeneracy. This population distribution determines which transitions are observable -- absorption requires significant ground-state population, while emission requires population inversion or thermal excitation. Line spectra arise because the allowed energies are discrete; the pattern of lines encodes the energy-level structure and therefore the identity and bonding of the species.

## How It's Best Learned
Calculate energy-level spacings and Boltzmann populations for a simple system (e.g., rotational levels of CO or electronic levels of hydrogen) at different temperatures. Then connect these populations to the relative intensities of spectral lines, seeing how temperature controls which transitions dominate.

## Common Misconceptions
- Assuming all energy levels are equally populated; Boltzmann weighting means higher levels are exponentially less populated unless the spacing is much smaller than k_BT.
- Believing every possible transition is observed; selection rules (Delta-J, Delta-l, spin conservation) restrict which transitions actually occur with appreciable probability.
