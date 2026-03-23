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
status: validated
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

## Questions

```yaml
- question: "A diatomic gas like N₂ has a measured molar heat capacity at constant volume of approximately (5/2)R at room temperature. If this same gas is heated to 5000 K, what would you expect C_v to approach?"
  type: multiple-choice
  options:
    - "(5/2)R — the value stays constant because the molecular structure doesn't change"
    - "(7/2)R — vibrational modes become thermally accessible at very high temperatures"
    - "(3/2)R — only translational modes matter at high temperatures"
    - "(9/2)R — all degrees of freedom double their contribution at high temperature"
  answer: 1
  explanation: "At room temperature, N₂'s vibrational mode is frozen out (kT ≪ ℏω), so only 3 translational + 2 rotational degrees of freedom contribute: C_v = (5/2)R. At 5000 K, kT becomes comparable to the vibrational quantum, and the one vibrational mode (contributing R, not (1/2)R, because it has both KE and PE) begins to fully activate, pushing C_v toward (5/2 + 1)R = (7/2)R. Option A is the classic misconception: molecular structure is unchanged, but which degrees of freedom are thermally accessible changes with temperature."

- question: "A nonlinear triatomic molecule (3 atoms) like H₂O has how many vibrational modes, and how much does each mode contribute to C_v per mole at high temperature?"
  type: multiple-choice
  options:
    - "3 modes, each contributing (1/2)R — same as a rotational degree of freedom"
    - "3 modes, each contributing R — because each vibrational mode has both kinetic and potential energy"
    - "2 modes, each contributing (1/2)R — linear and nonlinear molecules have the same vibrational count"
    - "4 modes, each contributing R — nonlinear molecules gain an extra mode compared to linear"
  answer: 1
  explanation: "A nonlinear molecule with N atoms has 3N − 6 vibrational modes: 3(3) − 6 = 3 modes for H₂O. Each vibrational mode is a harmonic oscillator with both a kinetic energy term and a potential energy term, each averaging (1/2)kT per molecule by equipartition. Together that's kT per molecule, or R per mole — double what a rotational degree of freedom (only kinetic) contributes. This is the crucial asymmetry: vibrations count double."

- question: "A linear triatomic molecule (like CO₂) has more vibrational modes than a nonlinear triatomic molecule (like H₂O) with the same number of atoms."
  type: true-false
  answer: true
  explanation: "Linear molecules have 3N − 5 vibrational modes; nonlinear molecules have 3N − 6. For N = 3: a linear molecule has 4 vibrational modes, a nonlinear molecule has 3. Linear molecules lose one rotational degree of freedom (rotation about the bond axis contributes negligible energy), so that degree of freedom 'becomes' an additional vibrational mode instead."

- question: "At room temperature, a diatomic ideal gas has the same molar heat capacity at constant volume as it would at 5000 K, because its molecular structure is unchanged."
  type: true-false
  answer: false
  explanation: "Molecular structure is unchanged, but which degrees of freedom are thermally accessible depends on temperature. Vibrational modes freeze out when kT ≪ ℏω (the vibrational quantum). At room temperature for most diatomic gases, this condition holds and C_v ≈ (5/2)R. At 5000 K, vibrational modes become active and C_v approaches (7/2)R. This temperature dependence of heat capacity is a quantum mechanical effect that classical equipartition alone cannot explain."

- question: "Why does each vibrational mode contribute twice as much energy per mole to a gas's heat capacity as each rotational degree of freedom?"
  type: short-answer
  answer: "Each rotational degree of freedom has only kinetic energy, which by equipartition averages (1/2)kT per molecule, contributing (1/2)R per mole. A vibrational mode is a harmonic oscillator with both a kinetic energy term and a potential energy term — each averaging (1/2)kT — for a total of kT per molecule and R per mole. The asymmetry arises because vibration stores energy in two quadratic terms, not one."
  explanation: "The equipartition theorem assigns (1/2)kT to each independent quadratic term in the energy. Rotation contributes one quadratic term (kinetic). Vibration contributes two: (1/2)mv² for kinetic and (1/2)kx² for potential. This is why the fully classical heat capacity of a diatomic gas — if all modes were active — would be (3/2 + 1 + 1)R = (7/2)R, not (5/2)R."
```

## Explainer

From kinetic theory, you know that a monatomic ideal gas (like helium) has three translational degrees of freedom — one for motion along each spatial axis. Each contributes ½kT to the average energy via equipartition, giving a total average kinetic energy of (3/2)kT per molecule. The molar heat capacity at constant volume is C_v = (3/2)R. This matches experiment perfectly for noble gases. The question is: what changes for molecules with internal structure?

A molecule has **3N total degrees of freedom** (where N is the number of atoms), because each atom can move independently in three directions. But for the molecule as a rigid unit, three of those degrees of freedom describe **translation** of the center of mass — always. The remaining degrees of freedom are split between **rotation** and **vibration**. For a linear molecule (like CO₂, or diatomic N₂), rotation occurs about two axes perpendicular to the molecular axis — rotating about the bond axis itself contributes negligible energy because the moment of inertia along that axis is essentially zero. So a linear molecule has 2 rotational degrees of freedom. For a nonlinear molecule (like water, H₂O), all three rotational axes have significant moment of inertia, giving 3 rotational degrees of freedom. The remaining (3N − 3 − 2) or (3N − 3 − 3) degrees of freedom are **vibrations** — stretching and bending of bonds.

Each rotational degree of freedom contributes ½kT (one term in the energy, purely kinetic), just like translation. Each vibrational mode is a harmonic oscillator with both kinetic *and* potential energy terms; equipartition gives ½kT for each, so a single vibration contributes **kT** — double the rotational contribution. This is the crucial asymmetry: vibrations count double. For a diatomic gas like N₂: 3 translational + 2 rotational + 1 vibrational mode = total energy (3/2 + 1 + 1)kT = (7/2)kT per molecule, giving C_v = (7/2)R in the fully classical limit.

But experiment shows that at room temperature, C_v for nitrogen is only about (5/2)R — as if the vibrational mode weren't there. At very high temperatures (thousands of kelvin), it approaches (7/2)R. This is the quantum effect: **vibrational modes freeze out** below a characteristic temperature T_vib = ℏω/k (the vibrational quantum of energy). If kT ≪ ℏω, the mode cannot absorb a quantum of vibration and contributes nothing to the heat capacity. Rotational modes typically freeze out at much lower temperatures (T_rot ~ 10 K for most molecules), so at room temperature you always have full translational and rotational contributions, but vibrational contributions only partially activate. This temperature dependence of C_v — impossible to explain classically but explained naturally by quantum mechanics — was historically one of the key motivations for Planck's introduction of energy quantization.
