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
- id: angular-momentum
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
status: validated
---

# The Rigid Rotor Model of Molecular Rotation

## Core Idea
The rigid rotor treats a diatomic molecule as two masses connected by a fixed bond, rotating freely in space. Its quantum energy levels are E_J = ℏ²J(J+1)/(2I), where J = 0, 1, 2, … is the rotational quantum number and I is the moment of inertia. Each level has degeneracy 2J+1 from the magnetic quantum number M_J. The rotational constant B = ℏ/(4πcI) directly connects spectroscopic measurements to molecular bond lengths and masses. Polyatomic molecules require specifying up to three principal moments of inertia (symmetric, spherical, and asymmetric tops).

## How It's Best Learned
Derive the energy levels for a diatomic from first principles, then use them to predict the spacing of lines in a microwave spectrum. Extract bond length from B to solidify the connection between model and measurement.

## Common Misconceptions
- Assuming all rotational levels are equally spaced — they are not; spacing increases as 2B(J+1).
- Forgetting that I depends on reduced mass, not just bond length.

## Explainer

The rigid rotor model is the quantum-mechanical treatment of molecular rotation, and it connects directly to what you already know about angular momentum and moment of inertia from classical mechanics. Imagine a diatomic molecule like HCl as a dumbbell: two masses (the H and Cl atoms) connected by a rigid bond of fixed length. In classical mechanics, this system can rotate with any angular velocity and any kinetic energy. But quantum mechanics imposes a constraint you've seen before — just as the particle in a box can only have discrete energy levels, a rotating molecule can only spin at specific quantized energies.

The allowed rotational energy levels are E_J = ℏ²J(J+1)/(2I), where J is the **rotational quantum number** (J = 0, 1, 2, …) and I is the **moment of inertia**, equal to μr² for a diatomic (μ is the reduced mass, r is the bond length). Notice the energy depends on J(J+1), not J² — this means the spacing between adjacent levels is not constant. The gap between J and J+1 is proportional to 2B(J+1), where B = ℏ/(4πcI) is the **rotational constant** expressed in wavenumber units (cm⁻¹). So the higher you go in J, the larger the gaps between successive levels. This non-uniform spacing is the fingerprint of the rigid rotor and shows up directly in microwave spectra as a series of evenly spaced absorption lines (each separated by 2B), because the selection rule requires ΔJ = ±1.

Each energy level J has a **degeneracy** of 2J+1, arising from the magnetic quantum number M_J, which ranges from −J to +J. Physically, this means a molecule in state J = 2 can rotate with five different orientations of its angular momentum vector in space, all at the same energy (in the absence of an external field). This degeneracy matters enormously for spectroscopy: higher-J levels have more states, so more molecules can populate them, which affects the relative intensities of spectral lines.

The remarkable practical payoff of the rigid rotor model is that measuring a microwave spectrum directly gives you the bond length of a molecule. If you observe spectral lines spaced by 2B, you extract B, then compute I = ℏ/(4πcB), and finally solve for r = √(I/μ). For example, the rotational spectrum of ¹²C¹⁶O shows lines spaced by about 3.84 cm⁻¹, giving B ≈ 1.92 cm⁻¹ and a bond length of 1.128 Å — matching high-precision measurements. For polyatomic molecules, the model extends to **symmetric tops** (two equal moments of inertia, like NH₃), **spherical tops** (all three equal, like CH₄), and **asymmetric tops** (all three different, like H₂O), each with increasingly complex energy-level patterns but built on the same foundational physics.
