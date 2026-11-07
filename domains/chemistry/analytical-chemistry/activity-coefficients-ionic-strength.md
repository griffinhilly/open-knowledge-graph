---
id: activity-coefficients-ionic-strength
title: Activity, Ionic Strength, and the Debye–Hückel Equation
domain: chemistry
course: analytical-chemistry
prerequisites:
- id: chemical-equilibrium
  type: hard
- id: equilibrium-expression-kc-kp-constants
  type: hard
- id: solubility-product-constant-ksp
  type: soft
- id: concentration-units
  type: soft
builds-toward:
- systematic-treatment-of-equilibrium
- potentiometry
- ion-selective-electrodes
- solution-thermodynamics-activity-models
tags:
- activity
- activity coefficient
- ionic strength
- Debye-Hückel
- salt effect
stage: advanced
status: validated
---

# Activity, Ionic Strength, and the Debye–Hückel Equation

## Core Idea
In real solutions, ions are surrounded by a cloud of oppositely charged ions that partly screens their charge, so they behave as if they were less concentrated. The effective concentration is the activity, a = γc, where γ is the activity coefficient. The ionic strength, I = ½Σcᵢzᵢ², measures how crowded with charge a solution is, and the Debye–Hückel equation predicts how γ falls as I rises. Exact equilibrium constants are written with activities, which explains why adding an unrelated salt can change solubility and pH.

## How It's Best Learned
Calculate ionic strength for several solutions, noticing how the z² term makes a 2+ or 3+ ion count heavily. Then use the Debye–Hückel limiting law to estimate γ for ions of charge 1, 2 and 3 at the same ionic strength. Finish by redoing a Ksp calculation with activities and comparing the solubility with the concentration-only answer.

## Common Misconceptions
- Ionic strength is just the total molar concentration of ions. (Each ion is weighted by the square of its charge, so 0.010 M MgSO₄ contains 0.020 M of ions but has I = 0.040 M.)
- Adding a salt with no common ion cannot change the solubility of a precipitate. (Raising ionic strength lowers the activity coefficients of the dissolved ions, so more solid dissolves; this is the salt effect.)
- Activity coefficients are always close to 1 and can be ignored. (They approach 1 only in very dilute solutions; at an ionic strength of 0.1 M, γ for a 2+ ion is well below 1.)

## Questions

```yaml
- question: "What is the ionic strength of 0.010 M MgCl₂?"
  type: multiple-choice
  options: ["0.010 M", "0.020 M", "0.030 M", "0.040 M"]
  answer: 2
  explanation: "I = ½[(0.010)(2²) + (0.020)(1²)] = ½(0.040 + 0.020) = 0.030 M. The Mg²⁺ ion counts four times per mole because of the z² term."
- question: "Adding NaNO₃ to a saturated AgCl solution lowers the solubility of AgCl."
  type: true-false
  answer: false
  explanation: "NaNO₃ shares no ion with AgCl, so there is no common-ion effect. It raises the ionic strength, which lowers the activity coefficients of Ag⁺ and Cl⁻, so more AgCl must dissolve to satisfy Ksp written in activities."
- question: "At the same ionic strength, which ion has the smallest activity coefficient?"
  type: multiple-choice
  options: ["Na⁺", "Cl⁻", "Ca²⁺", "Al³⁺"]
  answer: 3
  explanation: "In the Debye–Hückel equation, log γ is proportional to z². A 3+ ion is affected nine times as strongly as a 1+ ion, so Al³⁺ has the lowest γ."
- question: "Use the Debye–Hückel limiting law, log γ = −0.51z²√I (water, 25 °C), to estimate γ for a singly charged ion at I = 0.010 M."
  type: short-answer
  answer: "About 0.89"
  explanation: "log γ = −0.51 × 1 × √0.010 = −0.51 × 0.10 = −0.051, so γ = 10^(−0.051) ≈ 0.89. Even at this low ionic strength, the ion behaves as if it were about 11% less concentrated."
```

## Explainer

In introductory equilibrium problems you write Ksp, Ka and other constants with molar concentrations. That works well for very dilute solutions. In more concentrated ionic solutions, it starts to fail, and careful analytical work has to correct for it.

The reason is electrostatic. Each ion in solution attracts ions of opposite charge and repels ions of the same charge. On average, a cation sits in a slight excess of anions, called its ionic atmosphere. This atmosphere partly cancels the cation's charge, so the ion interacts less strongly than its concentration suggests. Chemists account for this with the activity, a = γc. The activity coefficient γ equals 1 in the limit of infinite dilution and falls below 1 as the solution becomes more crowded with charge.

The measure of crowding is the ionic strength:

I = ½ Σ cᵢzᵢ²

where cᵢ is the molar concentration of each ion and zᵢ its charge. Squaring the charge makes highly charged ions dominate. A 0.010 M NaCl solution has I = 0.010 M, but a 0.010 M MgCl₂ solution has I = 0.030 M.

Peter Debye and Erich Hückel derived how γ depends on I in 1923. For water at 25 °C, their limiting law is

log γ = −0.51 z² √I

It is accurate only at low ionic strength, roughly up to 0.01 M. An extended form adds a term for ion size and works to about 0.1 M. Two patterns follow from the equation. γ falls as ionic strength rises, and it falls much faster for ions of higher charge.

Activities matter because true equilibrium constants are written with them. For a sparingly soluble salt, Ksp = a(Ag⁺) × a(Cl⁻) = γ₊[Ag⁺] × γ₋[Cl⁻]. If you add an inert salt such as KNO₃, the γ values fall. To keep the product of activities fixed, the concentrations must rise, so more AgCl dissolves. This is the salt effect, and it acts in the opposite direction from the common-ion effect.

Activities also define measurements. The pH is formally −log a(H⁺), and a pH electrode responds to activity, not concentration. Ion-selective electrodes behave the same way, which is why analysts add an ionic-strength adjustment buffer so samples and standards share the same γ.
