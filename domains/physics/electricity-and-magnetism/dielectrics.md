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

## Explainer

From your study of capacitance, you know that a capacitor stores energy in the electric field between its plates, with C = ε₀A/d for a parallel-plate geometry in vacuum. A **dielectric** is an insulating material that, when inserted between the plates, increases the capacitance by a factor κ — the **dielectric constant** (also called relative permittivity). The reason is microscopic: the material's molecules respond to the applied field by becoming polarized.

**Polarization** happens in two ways. In polar molecules (like water), permanent electric dipoles rotate to partially align with the external field. In nonpolar molecules, the applied field distorts the electron cloud slightly, inducing a temporary dipole. In both cases, the aligned dipoles create their own electric field inside the material that points opposite to the applied field. This internal "opposition field" partially cancels the applied field, reducing the net E inside the dielectric by the factor κ. Crucially, no charge flows — the material remains an insulator. The dipoles just rearrange internally, which is fundamentally different from a conductor's response.

Now consider the consequences for a capacitor. If you charge the capacitor to voltage V₀ with the battery connected and then insert a dielectric, the battery maintains V = V₀ while κ increases C from C₀ to κC₀. More charge flows from the battery to the plates — Q increases by the factor κ. If instead you charge the capacitor, disconnect the battery (so Q is fixed), and then insert the dielectric, the reduced internal field means lower voltage: V = V₀/κ. The energy stored also drops by κ (the dielectric has done work pulling itself between the plates). These two scenarios — **constant voltage** vs. **constant charge** — give different physics, and distinguishing them is essential for any dielectric problem.

The **permittivity** of the medium is defined as ε = κε₀. Every electrostatic formula valid in vacuum — Coulomb's law, the capacitance formula, the energy density u = ½ε₀E² — still holds inside a uniform dielectric if you replace ε₀ with ε = κε₀. This is why κ appears in Gauss's law and Maxwell's equations as a material property: it describes how much the medium reduces the electric field (and thus how much it enhances charge storage) compared to free space. For engineering purposes, high-κ dielectrics are valuable precisely because they allow large capacitance in compact devices.
