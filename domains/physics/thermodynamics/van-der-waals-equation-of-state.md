---
id: van-der-waals-equation-of-state
title: The van der Waals Equation of State
domain: physics
course: thermodynamics
prerequisites:
- id: real-gas-deviations
  type: hard
builds-toward:
- compressibility-factor-z
- critical-point-phenomena
tags:
- equations-of-state
- intermolecular-forces
- phase-transitions
stage: formal-systems
status: draft
---

# The van der Waals Equation of State

## Core Idea
The van der Waals equation (P + a(n/V)²)(V - nb) = nRT accounts for intermolecular attractions (a term) and molecular size (b term), providing better accuracy than the ideal gas law for real gases. The constants a and b are substance-specific, with a reflecting the strength of intermolecular forces and b representing the excluded volume per mole. The van der Waals equation predicts a critical point and qualitatively explains phase transitions, making it a useful model for intermediate pressures and temperatures.

## How It's Best Learned
Expand the van der Waals equation and recover the ideal gas law as a → 0, b → 0. Find the critical point by setting (∂P/∂V)_T = 0 and (∂²P/∂V²)_T = 0.

## Common Misconceptions
- Thinking the van der Waals equation predicts liquefaction exactly (it is qualitatively correct but quantitatively rough).
- Confusing the parameters a and b with measurable quantities (they are fitted constants).
- Assuming the van der Waals equation applies equally well at all pressures.

## Explainer

You already know from your study of real gas deviations that the ideal gas law breaks down under high pressure and low temperature. The ideal gas model treats molecules as point particles with no volume and no attraction to each other. Both assumptions fail in reality — molecules occupy space and pull on each other. The van der Waals equation fixes both flaws with just two extra constants, giving a much more realistic picture of gas behavior.

The **b term** (the "excluded volume" correction) addresses molecular size. In the ideal gas law, volume V is the total container volume. But molecules themselves take up space, so the free volume available for motion is not V but V − nb, where n is the number of moles and b is the volume excluded per mole. Think of it like having a room full of people: the space each person can move around in is the room volume minus the space the other people occupy. Subtracting nb from V corrects for this overcrowding effect, which becomes significant only when molecules are packed tightly — that is, at high pressures.

The **a term** (the "intermolecular attraction" correction) addresses the pull between molecules. In the bulk of the gas, a molecule is surrounded equally on all sides, so the attractions cancel out. But molecules near the container wall have fewer neighbors on the outward side, so they are tugged backward by the bulk. This reduces the force with which they strike the wall, meaning the actual pressure is slightly lower than the ideal formula predicts. The correction adds a/V²ₘ (or a(n/V)² in the full equation) back onto the measured pressure to recover what the pressure would be without intermolecular attraction. Substances with strong intermolecular forces have large a values; noble gases have small a values.

Putting it together: (P + a(n/V)²)(V − nb) = nRT. Notice that if a → 0 and b → 0, this collapses exactly to the ideal gas law PV = nRT — a good sanity check that the correction is additive, not a replacement. The equation also predicts a **critical point**, the temperature and pressure above which a gas cannot be liquefied no matter how much pressure is applied. At the critical point, the van der Waals isotherm has both its first and second derivatives equal to zero with respect to volume — a mathematical condition that lets you derive the critical temperature, pressure, and volume in terms of a and b. This is a remarkable prediction from a two-parameter model.

The honest limitation: the van der Waals equation is qualitatively excellent but quantitatively rough, especially near phase transitions. It predicts the S-shaped "van der Waals loop" in the pressure-volume diagram that signals a phase transition, but real condensation is sharper and the predicted liquid volumes are too large. For engineering calculations requiring precision, more elaborate equations of state are used. But van der Waals gives you the right physical intuition — that real gases behave ideally when molecules are far apart, and deviate most when they are crowded or cold enough that attractions matter.
