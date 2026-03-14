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
