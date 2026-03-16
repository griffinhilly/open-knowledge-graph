---
id: degrees-of-freedom-and-heat-capacity
title: Degrees of Freedom and Heat Capacity
domain: physics
course: thermodynamics
prerequisites:
- id: internal-energy-microscopic-view
  type: hard
- id: equipartition-theorem
  type: soft
builds-toward:
- heat-capacity-of-gases
tags:
- molecular-structure
- kinetic-theory
- heat-capacity
stage: formal-systems
status: draft
---

# Degrees of Freedom and Heat Capacity

## Core Idea
Molecular degrees of freedom include translational (3), rotational (2 for linear, 3 for nonlinear), and vibrational (2 per mode). The equipartition theorem states each quadratic degree of freedom contributes (1/2)kT to average energy. This predicts heat capacity: Cv = (f/2)R for f degrees of freedom.

## Explainer

From your study of internal energy, you know that temperature measures the average kinetic energy of molecular motion. From equipartition, you know that every independent quadratic term in the energy — every **degree of freedom** — contributes exactly ½kT to the average energy. The question is: how many degrees of freedom does a molecule actually have? The answer depends on molecular structure, and getting it right is the key to predicting heat capacities.

For a **monatomic ideal gas** (He, Ne, Ar), the only motion is translation in three directions: E = p_x²/2m + p_y²/2m + p_z²/2m. That is 3 quadratic terms, so ⟨E⟩ = (3/2)kT per molecule, U = (3/2)NkT for N molecules, and C_V = (3/2)R per mole. This is the simplest case and matches experiment beautifully.

For a **diatomic molecule** (N₂, O₂, HCl), the molecule can also rotate. A dumbbell-shaped molecule has 2 independent rotation axes (perpendicular to the bond) — rotation about the bond axis has negligible moment of inertia and is quantum mechanically frozen out at ordinary temperatures. Each rotation contributes ½kT (rotational kinetic energy only, no potential term), adding 2 × ½kT. So at moderate temperatures, C_V = (3/2 + 2/2)R = **(5/2)R**. At high temperatures, the two atoms also vibrate along the bond. A vibration has both kinetic energy (½μẋ²) and potential energy (½kx²), contributing 2 × ½kT — so each vibrational mode adds a full kT. With vibration active, C_V = (5/2 + 2/2)R = **(7/2)R**.

The crucial experimental observation is that **degrees of freedom freeze out** at low temperatures. This is a quantum effect: if kT ≪ ℏω for a given mode (where ω is the mode's characteristic frequency), the mode stays in its quantum ground state and contributes nothing to the heat capacity. Vibrational modes have the highest frequencies (ℏω_vib ~ 0.1–0.5 eV), so they freeze out first — room temperature N₂ has C_V ≈ (5/2)R, not (7/2)R, because 300 K is too cold to excite vibrations. Rotational modes freeze out at much lower temperatures (ℏω_rot ~ 10⁻³ eV), so they are always active for diatomic gases above ~100 K. This stepwise activation of degrees of freedom, seen as a staircase in C_V vs. temperature plots, was a puzzle for classical physics and required quantum mechanics to explain.
