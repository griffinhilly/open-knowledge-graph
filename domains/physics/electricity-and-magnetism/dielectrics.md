---
id: dielectrics
title: Dielectrics
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: capacitance
  type: hard
- id: electric-field
  type: soft
builds-toward:
- maxwells-equations-overview
tags:
- dielectric
- polarization
- permittivity
- capacitance
stage: formal-systems
status: validated
---

# Dielectrics

## Core Idea
A dielectric is an insulating material that, when placed in an electric field, becomes polarized — its molecules align or develop induced dipole moments that partially oppose the applied field. Inserting a dielectric with dielectric constant κ between capacitor plates increases capacitance to C = κε₀A/d and reduces the internal electric field by the factor κ. The permittivity of the material is ε = κε₀, replacing ε₀ in all electrostatic formulas for that medium.

## How It's Best Learned
Compare a capacitor charged to V₀ with battery connected vs. disconnected before dielectric insertion — two different physical scenarios with different outcomes. This sharpens understanding of when Q is fixed vs. V is fixed.

## Common Misconceptions
- Dielectrics do not conduct charge; they reduce E by polarization, not by charge redistribution.
- κ > 1 always for real materials, so inserting a dielectric always increases C.
- The dielectric constant is frequency-dependent in AC settings.
