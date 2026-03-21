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

## Questions

```yaml
- question: "Nitrogen gas (N₂) at room temperature has a measured molar heat capacity at constant volume of approximately (5/2)R, not the (7/2)R you might expect for a diatomic molecule. What is the best explanation?"
  type: multiple-choice
  options:
    - "N₂ has fewer than 5 degrees of freedom at room temperature because it is a simple molecule"
    - "The vibrational modes are quantum mechanically frozen out at room temperature because kT is much smaller than the vibrational energy quantum"
    - "Rotational degrees of freedom do not contribute to heat capacity in diatomic gases"
    - "The equipartition theorem does not apply to diatomic gases"
  answer: 1
  explanation: "N₂ has 3 translational + 2 rotational + 2 vibrational (kinetic + potential) = 7 degrees of freedom in principle, predicting C_V = (7/2)R. But the vibrational mode's energy quantum ℏω_vib is roughly 0.1–0.5 eV, far exceeding kT ≈ 0.026 eV at 300 K. Quantum mechanics keeps the vibration locked in its ground state, contributing nothing to heat capacity. Rotational modes are active (ℏω_rot ≪ kT), so we get C_V ≈ (5/2)R. This is a quantum effect classical physics cannot explain."

- question: "A monatomic ideal gas and a diatomic ideal gas (at a temperature where only translational and rotational modes are active) are each given the same amount of heat. Which gas experiences the larger temperature rise?"
  type: multiple-choice
  options:
    - "The monatomic gas, because it has fewer degrees of freedom to absorb the energy"
    - "The diatomic gas, because more degrees of freedom means each one absorbs more heat"
    - "Both experience the same temperature rise because they obey the ideal gas law"
    - "The diatomic gas, because its higher heat capacity means it stores more energy per degree"
  answer: 0
  explanation: "Heat capacity C_V = (f/2)R, where f is the number of active degrees of freedom. A monatomic gas has f = 3, so C_V = (3/2)R. A diatomic gas with active translation and rotation has f = 5, so C_V = (5/2)R. Since the diatomic gas requires more energy per mole per degree of temperature rise, the same amount of heat produces a smaller temperature increase in the diatomic gas. The monatomic gas, with fewer modes to distribute energy into, heats up faster."

- question: "According to the equipartition theorem, a diatomic gas at very high temperature (where vibrational modes are fully active) should have C_V = (7/2)R at all temperatures."
  type: true-false
  answer: false
  explanation: "C_V = (7/2)R only when all 7 degrees of freedom (3 translational, 2 rotational, 2 vibrational) are active. But degrees of freedom freeze out at low temperatures — a quantum effect. At room temperature, vibrational modes are frozen (kT ≪ ℏω_vib), giving C_V ≈ (5/2)R. Only at high temperatures where kT ≫ ℏω_vib does the full (7/2)R emerge. Classical physics predicts (7/2)R at all temperatures; the observed staircase in C_V vs. T requires quantum mechanics."

- question: "Each translational degree of freedom of a molecule contributes (1/2)kT to its average thermal energy, according to the equipartition theorem."
  type: true-false
  answer: true
  explanation: "This is precisely the equipartition theorem: every independent quadratic term in the energy — each degree of freedom — contributes exactly (1/2)kT to the average energy per molecule, where k is Boltzmann's constant and T is temperature. For three translational modes, the total translational kinetic energy is (3/2)kT per molecule, giving the average kinetic energy for a monatomic ideal gas."

- question: "Why does the heat capacity of a diatomic gas increase as temperature rises, rather than remaining constant?"
  type: short-answer
  answer: "At low temperatures, only translational degrees of freedom are active; rotational modes activate at intermediate temperatures; vibrational modes activate at high temperatures. Each activation adds to the heat capacity in steps."
  explanation: "Each mode has a characteristic quantum energy ℏω. A mode only contributes to heat capacity when kT is comparable to or exceeds ℏω. Rotational modes have low ℏω_rot (activate below ~100 K for most diatomics), so they are always on at practical temperatures. Vibrational modes have high ℏω_vib (~0.1–0.5 eV), so they only activate at hundreds to thousands of kelvin. The result is a staircase: C_V ≈ (3/2)R (translation only) → (5/2)R (+ rotation) → (7/2)R (+ vibration) as temperature rises. This step structure was inexplicable classically and was one of the early confirmations of quantum mechanics."
```

## Explainer

From your study of internal energy, you know that temperature measures the average kinetic energy of molecular motion. From equipartition, you know that every independent quadratic term in the energy — every **degree of freedom** — contributes exactly ½kT to the average energy. The question is: how many degrees of freedom does a molecule actually have? The answer depends on molecular structure, and getting it right is the key to predicting heat capacities.

For a **monatomic ideal gas** (He, Ne, Ar), the only motion is translation in three directions: E = p_x²/2m + p_y²/2m + p_z²/2m. That is 3 quadratic terms, so ⟨E⟩ = (3/2)kT per molecule, U = (3/2)NkT for N molecules, and C_V = (3/2)R per mole. This is the simplest case and matches experiment beautifully.

For a **diatomic molecule** (N₂, O₂, HCl), the molecule can also rotate. A dumbbell-shaped molecule has 2 independent rotation axes (perpendicular to the bond) — rotation about the bond axis has negligible moment of inertia and is quantum mechanically frozen out at ordinary temperatures. Each rotation contributes ½kT (rotational kinetic energy only, no potential term), adding 2 × ½kT. So at moderate temperatures, C_V = (3/2 + 2/2)R = **(5/2)R**. At high temperatures, the two atoms also vibrate along the bond. A vibration has both kinetic energy (½μẋ²) and potential energy (½kx²), contributing 2 × ½kT — so each vibrational mode adds a full kT. With vibration active, C_V = (5/2 + 2/2)R = **(7/2)R**.

The crucial experimental observation is that **degrees of freedom freeze out** at low temperatures. This is a quantum effect: if kT ≪ ℏω for a given mode (where ω is the mode's characteristic frequency), the mode stays in its quantum ground state and contributes nothing to the heat capacity. Vibrational modes have the highest frequencies (ℏω_vib ~ 0.1–0.5 eV), so they freeze out first — room temperature N₂ has C_V ≈ (5/2)R, not (7/2)R, because 300 K is too cold to excite vibrations. Rotational modes freeze out at much lower temperatures (ℏω_rot ~ 10⁻³ eV), so they are always active for diatomic gases above ~100 K. This stepwise activation of degrees of freedom, seen as a staircase in C_V vs. temperature plots, was a puzzle for classical physics and required quantum mechanics to explain.
