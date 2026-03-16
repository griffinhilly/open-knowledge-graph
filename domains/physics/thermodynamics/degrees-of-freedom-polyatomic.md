---
id: degrees-of-freedom-polyatomic
title: Degrees of Freedom in Polyatomic Molecules
domain: physics
course: thermodynamics
prerequisites:
- id: kinetic-theory-of-gases
  type: hard
- id: equipartition-theorem
  type: soft
builds-toward:
- molar-heat-capacities
tags:
- kinetic-theory
- molecular-structure
- heat-capacity
stage: formal-systems
status: draft
---

# Degrees of Freedom in Polyatomic Molecules

## Core Idea
The equipartition theorem states that each quadratic degree of freedom contributes (1/2)R per mole to the heat capacity; translational motion contributes 3, rotation contributes 2 (linear) or 3 (nonlinear), and vibration contributes 2 per mode (1 kinetic + 1 potential). Polyatomic molecules have more degrees of freedom than diatomic ones, resulting in larger heat capacities; vibrational degrees of freedom only activate at high temperatures. Understanding degrees of freedom explains temperature dependence of heat capacities and the structure of molecules.

## How It's Best Learned
Count degrees of freedom for monatomic, diatomic, and polyatomic gases. Predict C_v using equipartition. Compare with measurements and explain discrepancies.

## Common Misconceptions
- Forgetting that vibrations contribute both kinetic and potential energy (2 each, not 1).
- Assuming all degrees of freedom are active at all temperatures (vibrational modes freeze out at low T).
- Confusing the number of atoms with the number of degrees of freedom.

## Explainer

From kinetic theory, you know that a monatomic ideal gas (like helium) has three translational degrees of freedom — one for motion along each spatial axis. Each contributes ½kT to the average energy via equipartition, giving a total average kinetic energy of (3/2)kT per molecule. The molar heat capacity at constant volume is C_v = (3/2)R. This matches experiment perfectly for noble gases. The question is: what changes for molecules with internal structure?

A molecule has **3N total degrees of freedom** (where N is the number of atoms), because each atom can move independently in three directions. But for the molecule as a rigid unit, three of those degrees of freedom describe **translation** of the center of mass — always. The remaining degrees of freedom are split between **rotation** and **vibration**. For a linear molecule (like CO₂, or diatomic N₂), rotation occurs about two axes perpendicular to the molecular axis — rotating about the bond axis itself contributes negligible energy because the moment of inertia along that axis is essentially zero. So a linear molecule has 2 rotational degrees of freedom. For a nonlinear molecule (like water, H₂O), all three rotational axes have significant moment of inertia, giving 3 rotational degrees of freedom. The remaining (3N − 3 − 2) or (3N − 3 − 3) degrees of freedom are **vibrations** — stretching and bending of bonds.

Each rotational degree of freedom contributes ½kT (one term in the energy, purely kinetic), just like translation. Each vibrational mode is a harmonic oscillator with both kinetic *and* potential energy terms; equipartition gives ½kT for each, so a single vibration contributes **kT** — double the rotational contribution. This is the crucial asymmetry: vibrations count double. For a diatomic gas like N₂: 3 translational + 2 rotational + 1 vibrational mode = total energy (3/2 + 1 + 1)kT = (7/2)kT per molecule, giving C_v = (7/2)R in the fully classical limit.

But experiment shows that at room temperature, C_v for nitrogen is only about (5/2)R — as if the vibrational mode weren't there. At very high temperatures (thousands of kelvin), it approaches (7/2)R. This is the quantum effect: **vibrational modes freeze out** below a characteristic temperature T_vib = ℏω/k (the vibrational quantum of energy). If kT ≪ ℏω, the mode cannot absorb a quantum of vibration and contributes nothing to the heat capacity. Rotational modes typically freeze out at much lower temperatures (T_rot ~ 10 K for most molecules), so at room temperature you always have full translational and rotational contributions, but vibrational contributions only partially activate. This temperature dependence of C_v — impossible to explain classically but explained naturally by quantum mechanics — was historically one of the key motivations for Planck's introduction of energy quantization.
