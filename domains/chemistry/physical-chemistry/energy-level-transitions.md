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

## Explainer

Quantum mechanics tells you that atoms and molecules cannot have just any amount of energy — they are restricted to specific, discrete **energy levels**, like rungs on a ladder rather than points on a ramp. This is a direct consequence of the wave nature of particles: just as a guitar string can only vibrate at certain frequencies (its harmonics), an electron bound in an atom can only occupy certain energy states. The spacing between these levels depends on the system: electronic levels in atoms are typically separated by electron-volts (visible and UV light), vibrational levels in molecules by tenths of electron-volts (infrared), and rotational levels by thousandths of electron-volts (microwave).

A transition between two levels occurs when the system absorbs or emits a photon whose energy exactly matches the gap: **ΔE = hν**, where h is Planck's constant and ν is the photon frequency. This is why atomic spectra consist of sharp lines rather than continuous bands — each line corresponds to one specific transition between two specific levels. The pattern of lines is a fingerprint of the atom or molecule, encoding its entire energy-level structure. Hydrogen's Balmer series, the sodium doublet, and the rotational spectrum of carbon monoxide are all direct readouts of quantum-mechanical energy ladders.

Not all transitions are equally likely, and some are essentially forbidden. **Selection rules** — derived from the mathematical requirement that the transition dipole moment integral be nonzero — dictate which transitions produce strong spectral lines. For example, in a one-electron atom, the orbital angular momentum quantum number must change by exactly ±1 (Δl = ±1), and spin must be conserved. These rules explain why some gaps in the energy ladder never produce observable lines, even though the energy levels exist. The intensity of an allowed transition depends on two factors: the intrinsic probability of the transition (the transition dipole moment) and how many molecules are in the initial state.

This is where the **Boltzmann distribution** enters. At thermal equilibrium, the population of each energy level follows N_i ∝ g_i·exp(−E_i/k_BT), where g_i is the degeneracy (number of states at that energy) and k_BT sets the thermal energy scale. At room temperature, k_BT ≈ 0.025 eV, which means electronic excited states (gaps of several eV) are essentially unpopulated — you only see absorption from the ground state. Rotational levels, with spacings much smaller than k_BT, are thermally populated across many levels, producing rich spectra with many lines whose intensities rise, peak, and fall as the Boltzmann factor and degeneracy compete. Understanding these population effects lets you predict not just which lines appear, but their relative strengths — connecting quantum mechanics directly to what you observe in the spectrometer.
