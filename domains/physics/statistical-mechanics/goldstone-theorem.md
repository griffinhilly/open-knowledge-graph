---
id: goldstone-theorem
title: Goldstone's Theorem and Gapless Modes
domain: physics
course: statistical-mechanics
prerequisites:
- id: symmetry-breaking-phase-transitions
  type: hard
builds-toward:
- collective-excitations-phonons
tags:
- symmetry
- excitations
- gapless
stage: advanced
status: draft
---

# Goldstone's Theorem and Gapless Modes

## Core Idea
Goldstone's theorem states that every continuously broken symmetry produces a gapless (zero-energy) excitation mode. Breaking translational symmetry yields phonons; breaking spin symmetry yields magnons. These Goldstone bosons are the long-wavelength fluctuations of the broken order parameter and appear at all temperatures below the transition.

## Explainer

From your study of symmetry breaking, you know that a phase transition can lower the symmetry of a ground state below the symmetry of the Hamiltonian. A ferromagnet provides the clearest example: the Hamiltonian is rotationally symmetric, but below T_c the spins align in some specific direction — the ground state picks a direction that the Hamiltonian did not prefer. The order parameter (the magnetization) points somewhere, breaking the continuous rotational symmetry. Goldstone's theorem tells you that this is not free: every continuously broken symmetry must produce a specific type of low-energy excitation.

The intuition comes from thinking about the symmetry the ground state broke. If rotational symmetry is broken by alignment along the z-axis, you can ask: what happens if you slowly rotate the magnetization? A uniform global rotation costs no energy — it just moves you to a different but equally valid ground state. But a **spatially varying** rotation — where spins gradually tilt from one direction to another over a long wavelength — costs only a little energy, and that cost vanishes as the wavelength goes to infinity. These long-wavelength, low-energy "twists" of the order parameter are the **Goldstone modes** (for magnets, they are called magnons or spin waves). The key is that the energy cost of a Goldstone mode goes to zero as its wavevector k → 0: they are **gapless**, meaning no minimum energy is required to excite them.

Contrast this with a discrete symmetry breaking, such as an Ising magnet where spins are either up or down. There, the broken symmetry is discrete — you cannot continuously rotate between the two ground states. No Goldstone theorem applies, and excitations typically have an energy gap. The theorem is specifically about **continuous** symmetries because only there can you continuously interpolate between ground states, generating the smooth long-wavelength deformations that become gapless modes.

**Phonons** are the canonical example in a crystal. A crystal breaks continuous translational symmetry: the atoms settle into a lattice that picks specific positions. Long-wavelength sound waves — coherent slow displacements of the lattice — are the corresponding Goldstone modes. Their dispersion relation ω ∝ k vanishes as k → 0, confirming the gapless character. In general, the number of Goldstone bosons equals the number of broken continuous symmetry generators, a counting rule that gives a powerful handle on the low-energy physics of any ordered phase without solving the full microscopic problem.
