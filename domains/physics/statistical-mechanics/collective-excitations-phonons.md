---
id: collective-excitations-phonons
title: Collective Excitations and Phonons
domain: physics
course: statistical-mechanics
prerequisites:
- id: goldstone-theorem
  type: hard
- id: long-range-order
  type: soft
builds-toward:
- bogoliubov-transformation
tags:
- excitations
- phonons
- collective
stage: advanced
status: draft
---

# Collective Excitations and Phonons

## Core Idea
Collective excitations are coherent modes in which many particles move in coordinated fashion. Phonons are quantized lattice vibrations in solids; magnons are spin waves. These elementary excitations emerge above an ordered ground state, can be treated as quasiparticles, and provide the dominant contribution to thermodynamic properties at low temperatures.

## Explainer

From the Goldstone theorem, you know that when a continuous symmetry is spontaneously broken, gapless (zero-frequency at k = 0) excitations must appear in the spectrum. A crystal breaks continuous translational symmetry down to discrete lattice translations, and the resulting Goldstone modes are **phonons** — quantized vibrations of the crystal lattice. The key insight is that instead of tracking 10²³ individual atomic positions, you can describe the entire set of small oscillations in terms of normal modes, each labeled by a wavevector k and a polarization branch.

Each normal mode of the lattice is a harmonic oscillator, and quantum mechanics tells you to quantize it: the mode of frequency ω_k can hold n_k = 0, 1, 2, ... energy quanta, each carrying energy ℏω_k. These quanta are **phonons**. A phonon is not a particle in the traditional sense — it has no conserved number, it can be created and absorbed freely — but it behaves like one for the purpose of thermodynamics and transport. You can scatter phonons off electrons, off other phonons, or off crystal defects, and the result is the thermal and electrical conductivity of real materials.

There are two types of phonons. **Acoustic** phonons correspond to all atoms in a unit cell moving in the same direction — these are sound waves quantized, and their dispersion is linear near k = 0: ω ≈ v_s |k|, with v_s the speed of sound. **Optical** phonons arise in crystals with more than one atom per unit cell; neighboring atoms move against each other, creating an oscillating dipole that can couple to light (hence the name). Optical phonons have a nonzero frequency at k = 0 and contribute a distinct bump to the density of states.

The thermodynamic importance of phonons is immediate: at low temperatures, acoustic phonons dominate the heat capacity and give the Debye T³ law (heat capacity ∝ T³). At higher temperatures, the Einstein model — treating all modes as having the same frequency — captures the saturation of heat capacity toward the classical Dulong-Petit value of 3k_B per atom. The same treatment applies to other broken-symmetry modes: **magnons** (spin waves in ferromagnets) follow analogous quantization and produce a T^(3/2) magnetic heat capacity at low temperatures. In each case, the strategy is the same — identify the soft modes above the ordered ground state, quantize them as independent harmonic oscillators, and compute thermodynamics using the appropriate Bose-Einstein or Planck-type distribution.
