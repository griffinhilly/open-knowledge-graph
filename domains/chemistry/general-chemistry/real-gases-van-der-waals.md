---
id: real-gases-van-der-waals
title: Real Gases and the van der Waals Equation
domain: chemistry
course: general-chemistry
prerequisites:
- id: gas-laws
  type: hard
- id: intermolecular-forces
  type: hard
builds-toward:
- phase-changes-and-diagrams
tags:
- van-der-Waals
- real-gas
- compressibility-factor
- non-ideal-gas
- intermolecular-attraction
- molecular-volume
stage: advanced
status: draft
---
# Real Gases and the van der Waals Equation

## Core Idea
Real gases deviate from ideal behavior because molecules occupy finite volume and experience intermolecular attractions. The van der Waals equation, (P + a(n/V)²)(V − nb) = nRT, corrects for these two effects: the 'a' term accounts for attractive forces (which reduce pressure below the ideal prediction), and the 'b' term accounts for the excluded volume of the molecules themselves. Deviations from ideality are greatest at high pressures (molecules crowded together) and low temperatures (kinetic energy insufficient to overcome attractions). The compressibility factor Z = PV/nRT quantifies deviation: Z = 1 for an ideal gas, Z < 1 when attractions dominate, Z > 1 when volume exclusion dominates.

## How It's Best Learned
Compare PV/nRT plots for real gases (N₂, CO₂, H₂O) against the ideal value of 1. Identify which correction (a or b) dominates under different conditions. Practice converting between the ideal gas law and van der Waals equation to see how each correction term shifts the result.

## Common Misconceptions
- The van der Waals constants a and b are not universal — they are specific to each gas and reflect its particular molecular properties (polarizability, size).
- A gas does not become 'non-ideal' suddenly at some threshold. All gases are real; the ideal gas law is simply a closer approximation under certain conditions (low P, high T).

## Explainer

The ideal gas law treats molecules as point particles that never attract or repel each other — and for many everyday conditions, that simplification works remarkably well. But you already know from studying intermolecular forces that real molecules do attract one another (through London dispersion, dipole-dipole, or hydrogen bonding), and from the gas laws that pressure, volume, and temperature are all interrelated. Real-gas behavior is what happens when those two pieces of knowledge collide: the simplifying assumptions break down, and we need a better model.

Consider what happens when you compress a gas into a small volume. The molecules are now close enough that their **intermolecular attractions** become significant. Each molecule heading toward the container wall gets tugged backward slightly by its neighbors, so it hits the wall with less force than an ideal gas molecule would. The measured pressure is therefore *lower* than PV = nRT predicts. The van der Waals equation fixes this with the **a correction**: it adds a term a(n/V)² to the measured pressure, where *a* is a constant specific to each gas that reflects how strongly its molecules attract each other. Gases like water vapor and ammonia, with strong hydrogen bonding, have large *a* values; helium and neon, with only weak London forces, have tiny ones.

The second correction addresses **molecular volume**. The ideal gas law assumes molecules take up no space, so the entire container volume is available for motion. In reality, each molecule excludes a small region around itself that no other molecule can occupy. The **b correction** subtracts nb from the total volume, where *b* reflects the effective size of one mole of molecules. Together, the corrected equation becomes (P + a(n/V)²)(V − nb) = nRT. At low pressures and high temperatures — where molecules are far apart and moving fast — both corrections shrink toward zero and the equation collapses back to PV = nRT, exactly as you would expect.

The **compressibility factor** Z = PV/nRT gives you a single number to diagnose which correction matters more. For an ideal gas, Z equals exactly 1. When attractions dominate (moderate pressures, molecules fairly close), Z dips below 1 because intermolecular pulling reduces the effective pressure. When volume exclusion dominates (very high pressures, molecules nearly touching), Z climbs above 1 because the finite molecular size forces the gas to occupy more volume than the ideal law predicts. Plotting Z versus pressure for different gases reveals a characteristic dip-then-rise curve, and the depth of the dip correlates directly with the strength of intermolecular forces — connecting this topic right back to the trends you learned earlier.
