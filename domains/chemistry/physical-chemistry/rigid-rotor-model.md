---
id: rigid-rotor-model
title: The Rigid Rotor Model of Molecular Rotation
domain: chemistry
course: physical-chemistry
prerequisites:
- id: quantum-chemistry-foundations
  type: hard
- id: rotational-kinematics
  type: soft
- id: moment-of-inertia
  type: soft
builds-toward:
- rotational-spectroscopy
- selection-rules-spectroscopy
tags:
- rotation
- rigid-rotor
- moment-of-inertia
- rotational-energy
stage: advanced
status: draft
---

# The Rigid Rotor Model of Molecular Rotation

## Core Idea
The rigid rotor treats a diatomic molecule as two masses connected by a fixed bond, rotating freely in space. Its quantum energy levels are E_J = ℏ²J(J+1)/(2I), where J = 0, 1, 2, … is the rotational quantum number and I is the moment of inertia. Each level has degeneracy 2J+1 from the magnetic quantum number M_J. The rotational constant B = ℏ/(4πcI) directly connects spectroscopic measurements to molecular bond lengths and masses. Polyatomic molecules require specifying up to three principal moments of inertia (symmetric, spherical, and asymmetric tops).

## How It's Best Learned
Derive the energy levels for a diatomic from first principles, then use them to predict the spacing of lines in a microwave spectrum. Extract bond length from B to solidify the connection between model and measurement.

## Common Misconceptions
- Assuming all rotational levels are equally spaced — they are not; spacing increases as 2B(J+1).
- Forgetting that I depends on reduced mass, not just bond length.
