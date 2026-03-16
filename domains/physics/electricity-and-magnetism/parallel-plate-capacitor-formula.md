---
id: parallel-plate-capacitor-formula
title: 'Parallel Plate Capacitor: Geometry and Formula'
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: capacitance-definition
  type: hard
- id: conductors-electrostatic-behavior
  type: hard
builds-toward:
- capacitor-circuits-series-parallel
- energy-density-electric-field
tags:
- parallel-plate
- geometry
- formula
stage: formal-systems
status: draft
---

# Parallel Plate Capacitor: Geometry and Formula

## Core Idea
A parallel plate capacitor with plate area A and separation d has capacitance C = ε₀A/d. The field between plates is uniform E = V/d, making this geometry ideal for theoretical analysis and practical applications.

## Explainer

From your prerequisites, you know that **capacitance** is defined as C = Q/V — the ratio of stored charge to voltage — and that conductors in electrostatic equilibrium have all charge on their surfaces and no field inside their bulk. The parallel plate capacitor translates these abstract ideas into a concrete, calculable geometry.

Consider two large, flat, parallel conducting plates separated by a small gap d. Place charge +Q on one plate and −Q on the other. From the behavior of conductors you already know, the positive charges spread uniformly across the inner surface of one plate and negative charges across the inner surface of the other (for an ideal infinite plate, all the charge faces inward). Each plate acts like a sheet of surface charge with density σ = Q/A. Applying Gauss's law — your new tool — to a flat pillbox straddling one plate shows that an infinite sheet of charge density σ produces a field E = σ/(2ε₀) on each side. Between the plates, the fields from both sheets point in the same direction and add: E = σ/ε₀ = Q/(ε₀A). Outside, they point in opposite directions and cancel to zero. This is why the field is uniform and confined between the plates.

With a uniform field E between the plates, the voltage difference is simply V = Ed (voltage equals field times distance for a uniform field). Combining: V = Qd/(ε₀A), so the capacitance is C = Q/V = ε₀A/d. The formula encodes three physical intuitions: (1) larger plate area A means more space to store charge at a given field strength, so C increases; (2) larger separation d means you need more voltage to produce the same field, so the same Q requires more V and C decreases; (3) the permittivity ε₀ sets the fundamental scale of how much charge a given electric field requires. When a dielectric material fills the gap, ε₀ is replaced by ε = κε₀, where κ > 1 is the dielectric constant — the material polarizes in response to the field, reducing the effective field and allowing more charge to be stored at the same voltage.

The parallel plate geometry is the workhorse of electrostatics precisely because the uniform field makes every calculation tractable. Energy stored in the capacitor is U = ½CV² = ε₀E²(Ad)/2, and the quantity ε₀E²/2 is recognized as the **energy density** of the electric field — a result that generalizes far beyond capacitors to any region of space containing an electric field.
