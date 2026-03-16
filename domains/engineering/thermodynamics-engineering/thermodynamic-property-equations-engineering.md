---
id: thermodynamic-property-equations-engineering
title: Equations of State and Thermodynamic Properties
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: state-functions-path-functions
  type: hard
- id: thermodynamic-properties-and-equations-of-state
  type: soft
builds-toward:
- ideal-real-gas-equations-state
- phase-equilibrium-clausius-clapeyron-detailed
- steam-tables-property-diagrams
tags:
- equations-of-state
- properties
- relations
- calculations
stage: advanced
status: draft
---

# Equations of State and Thermodynamic Properties

## Core Idea
Equations of state relate P, v, T and enable calculation of derived properties (h, s, u, g). The ideal gas law Pv = RT works for low pressures; real gases require corrections (virial expansion, van der Waals, empirical) especially near saturation and high pressure. Modern engineering relies on property tables, reference fluid equations, and software for accurate multicomponent calculations.

## Explainer

From your study of state functions and path functions, you know that thermodynamic properties like pressure P, specific volume v, temperature T, internal energy u, enthalpy h, and entropy s are state functions — their values depend only on the current state, not on how the system got there. An **equation of state** is simply the mathematical relationship that connects these state variables. The most important role of an equation of state is to allow you to calculate properties you cannot measure directly (like entropy or internal energy) from properties you can measure (pressure, temperature, and specific volume).

The **ideal gas law**, Pv = RT, is the foundational equation of state. It is derived from the assumptions that molecules occupy no volume and exert no intermolecular forces. These assumptions are excellent at low pressures and high temperatures — conditions where molecules are far apart. In that regime, Pv/RT ≈ 1 (the **compressibility factor** Z equals 1). The ideal gas law lets you use the simple relations du = cᵥ dT and dh = cₚ dT, which only hold for ideal gases. Most engineering gas calculations (combustion air, exhaust gases, refrigerants well above saturation) use the ideal gas assumption with tables of temperature-dependent specific heats for accuracy.

Real gases deviate from ideal behavior near saturation, at high pressures, or with strong intermolecular forces. The **van der Waals equation** (P + a/v²)(v - b) = RT corrects for molecular volume (b term) and intermolecular attraction (a/v² term). This two-parameter correction captures the qualitative behavior: the isotherm below the critical temperature develops a wiggle that predicts phase transitions. More accurate for engineering use are **virial equations** (power series in 1/v with empirically fit coefficients) and modern reference equations like those from NIST, which use dozens of fitted terms to reproduce measured properties of specific fluids (water, CO₂, refrigerants) to within experimental uncertainty. Steam tables, refrigerant tables, and natural gas property correlations are all encoded equations of state, pre-evaluated on a grid for convenience.

The derived properties h, s, u, and g are not independent of P, v, T — they are connected through the **fundamental thermodynamic relations**: dh = T ds + v dP, du = T ds - P dv. From these, exact partial derivative relationships follow (Maxwell relations), allowing entropy and energy changes to be computed from P-v-T data alone. This is how engineers extend an equation of state into a complete thermodynamic property package: given P(v, T), you can derive (∂u/∂v)_T = T(∂P/∂T)_v - P, and integrate to get internal energy changes without calorimetry. This machinery underpins the property calculations in every process simulator and refrigeration cycle design tool.

In practice, the engineering workflow is: identify the fluid and state, determine whether ideal gas behavior is adequate (check Z using reduced temperature and pressure), and if not, select the appropriate correlation or look up property tables. For water and steam, tables are effectively exact. For natural gas mixtures, equations of state like Peng-Robinson or BWRS are standard. For cryogenic fluids or refrigerants, NIST reference equations are the benchmark. The unifying conceptual thread — that all properties are functions of state variables related through an equation of state and the fundamental relations — is what lets you bridge between these different practical tools without treating each as a separate memorization task.

