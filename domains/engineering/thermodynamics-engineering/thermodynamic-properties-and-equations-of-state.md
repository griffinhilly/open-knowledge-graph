---
id: thermodynamic-properties-and-equations-of-state
title: Thermodynamic Properties and Equations of State
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: entropy-intro
  type: hard
builds-toward:
- pure-substance-phase-diagrams
tags:
- properties
- state
- equations-of-state
stage: advanced
status: draft
---

# Thermodynamic Properties and Equations of State

## Core Idea
Thermodynamic properties (P, T, V, u, h, s) describe the state of matter; intensive properties are independent of mass while extensive properties depend on system size. An equation of state (like PV=RT for ideal gases) relates properties and reduces the number of independent variables needed to specify a system's state. Engineering systems often use simplified equations of state or property tables rather than exact molecular equations.

## How It's Best Learned
For ideal gases, memorize the equation PV=nRT and practice converting between specific and molar forms. For real fluids, learn to navigate property tables (steam tables, refrigerant tables) and understand when ideal gas assumption is reasonable. Recognize that specifying two independent intensive properties (usually T and P or T and v) fully determines all other properties.

## Common Misconceptions
- All six properties (P, T, V, u, h, s) are independent; only two are independent for a pure substance.
- Enthalpy h is only relevant to open systems; it is equally important for understanding closed systems.
- The ideal gas law is always accurate; it fails near saturation and at high pressures.

## Explainer

From your study of entropy, you've already encountered several thermodynamic properties: temperature T, pressure P, internal energy u, and entropy s. The organizing principle that connects all of them is the **state postulate**: for a pure, simple compressible substance (no electrical, magnetic, or surface effects), specifying two independent intensive properties completely determines the thermodynamic state. Every other property is then fixed. This is not obvious — it is a result, rooted in the structure of the fundamental thermodynamic relations — but it is the rule that makes property calculations tractable.

**Intensive properties** are independent of system size: temperature, pressure, specific volume v (volume per unit mass), specific internal energy u, specific enthalpy h = u + Pv, and specific entropy s. **Extensive properties** scale with mass: total volume V, total internal energy U, total enthalpy H. In engineering calculations, you almost always work with specific (per unit mass) intensive properties and multiply by mass to get totals. This distinction matters practically: if you double the mass of steam in a vessel while keeping T and P the same, h (per unit mass) is unchanged but H (total) doubles.

An **equation of state** is the mathematical relationship that ties the state variables together and reduces the number of independent variables. The ideal gas equation Pv = RT is the simplest: given any two of P, T, and v, the third is determined. This equation derives from treating gas molecules as non-interacting point masses — a model that works well for most gases far from saturation and at moderate pressures. It fails predictably near phase transitions and at high pressures where molecular volume and intermolecular attractions become significant. The van der Waals equation and the Peng-Robinson equation are more accurate for real gases in those regimes.

For water and many refrigerants, no simple equation of state is accurate enough for engineering design. Instead, **property tables** (steam tables, refrigerant tables) provide tabulated values of u, h, s, and v as functions of T and P across subcooled liquid, saturated, and superheated vapor regions. The practical skill is navigation: first identify the phase by comparing the given temperature or pressure to saturation values, then read the appropriate table region, then interpolate between entries if needed. Specifying two independent properties locates a point in the table; the remaining properties are read from that row. The state postulate is why two inputs always suffice — and why memorizing which two properties are given (rather than which six might be listed) is the key to solving any thermodynamic problem efficiently.
