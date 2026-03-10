---
id: molecular-partition-functions
title: Molecular Partition Functions
domain: chemistry
course: physical-chemistry
prerequisites:
- id: statistical-mechanics-foundations
  type: hard
- id: harmonic-oscillator-molecular-vibrations
  type: soft
- id: rigid-rotor-model
  type: soft
builds-toward:
- statistical-thermodynamics-applications
tags:
- partition-function
- translational
- rotational
- vibrational
- electronic
- factorization
stage: advanced
status: draft
---

# Molecular Partition Functions

## Core Idea
The molecular partition function q is the sum of Boltzmann factors over all molecular energy levels. For an ideal gas, the total partition function factorizes into independent contributions: q = q_trans · q_rot · q_vib · q_elec, because translational, rotational, vibrational, and electronic degrees of freedom are (approximately) independent. Each contribution has a characteristic form: q_trans ∝ V(2πmkT/h²)^(3/2); q_rot depends on the rotational constants; q_vib = ∏[1−exp(−hν_i/kT)]^(−1) for harmonic oscillators; q_elec is usually just the ground-state degeneracy unless excited states are thermally accessible. Thermodynamic properties are then obtained as derivatives of ln q.

## How It's Best Learned
Evaluate each partition function contribution for a simple diatomic like N₂ at 298 K and 1000 K. Observe how q_trans is enormous (many translational states accessible), q_rot is moderate, and q_vib is close to 1 (vibrational states barely excited at room temperature).

## Common Misconceptions
- Confusing q (single-molecule partition function) with Q = q^N/N! (N-molecule system partition function); the N! accounts for indistinguishability.
- Thinking all degrees of freedom contribute equally to heat capacity; only those with kT ≳ level spacing are 'activated'.
