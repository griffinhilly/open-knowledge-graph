---
id: real-gas-deviations
title: Deviations of Real Gases from Ideal Behavior
domain: physics
course: thermodynamics
prerequisites:
- id: ideal-gas-law
  type: hard
builds-toward:
- van-der-waals-equation-of-state
- compressibility-factor-z
- joule-thomson-expansion-effect
tags:
- equations-of-state
- intermolecular-forces
- high-pressure
stage: formal-systems
status: draft
---

# Deviations of Real Gases from Ideal Behavior

## Core Idea
Real gases deviate from ideal behavior because molecules have finite size (excluded volume) and experience intermolecular attractive forces, particularly at high pressures and low temperatures. The compressibility factor Z = PV/nRT quantifies deviations from ideality (Z = 1 for ideal gas, Z < 1 for attractive forces, Z > 1 for repulsive forces). Understanding real gas deviations is essential for accurate calculations in refrigeration, liquefaction, and high-pressure applications.

## How It's Best Learned
Plot Z versus pressure or reduced pressure for various gases. Identify regions where attractive forces (Z < 1) and repulsive forces (Z > 1) dominate.

## Common Misconceptions
- Thinking the ideal gas law works everywhere (it fails at high P and low T).
- Confusing molecular size effects (repulsive, Z > 1) with attractive forces (Z < 1).
- Assuming deviations are always small (they can be huge near the critical point).

## Explainer

The ideal gas law PV = nRT rests on two simplifying assumptions: molecules have negligible volume, and they exert no forces on each other between collisions. From your study of the ideal gas law, you know it works well for dilute gases at high temperatures — conditions where molecules are far apart and moving fast. Real gases deviate because both assumptions fail as pressure rises or temperature falls, and the **compressibility factor** Z = PV/nRT provides a single dimensionless measure of the deviation (Z = 1 for ideal, Z ≠ 1 for real).

Consider **attractive intermolecular forces** first. At moderate pressures, molecules are close enough to exert van der Waals attraction on each other. A molecule approaching the container wall feels a net inward pull from its neighbors — it arrives at the wall with slightly less momentum than it would in isolation. The result is that the gas exerts *less* pressure than the ideal model predicts: Z < 1. This is why gases can condense into liquids at all — attractive forces can overwhelm thermal kinetic energy, causing molecules to cluster and reducing the pressure. Carbon dioxide near its critical point (31°C, 73 atm) shows Z dramatically less than 1 because intermolecular attractions are near their strongest relative to the particles' kinetic energy.

At **high pressures**, the finite physical size of molecules becomes dominant. Molecules cannot occupy the same space — they have a hard repulsive core — so the volume actually available to any one molecule is less than the total container volume. The gas is harder to compress than the ideal model assumes: Z > 1. Think of compressing a jar of marbles: below some minimum volume they simply cannot pack any tighter, regardless of applied pressure. For gases like helium and hydrogen at room temperature, which have very weak attractive forces, this repulsive-core effect dominates even at moderate pressures and Z > 1 throughout.

The competition between these two effects produces the characteristic Z-vs-P curve: at low pressure, Z dips below 1 (attraction dominates), reaches a minimum, then rises above 1 at high pressure (repulsion dominates). The **Boyle temperature** — where B₂(T) = 0 in the virial expansion — is the temperature at which Z ≈ 1 across a range of pressures because attractive and repulsive effects cancel. Different gases cross the Boyle temperature at different values because their intermolecular potentials differ in depth and range. All of this behavior is captured quantitatively by the van der Waals equation (P + an²/V²)(V − nb) = nRT, where the constant a measures the strength of attractions and b measures the excluded volume — translating molecular-scale physics directly into macroscopic equations of state.
