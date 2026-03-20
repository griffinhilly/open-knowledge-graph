---
id: critical-point-and-supercritical-fluids
title: Critical Point and Supercritical Fluids
domain: physics
course: thermodynamics
prerequisites:
- id: clausius-clapeyron-phase-boundary
  type: hard
- id: phase-diagrams
  type: soft
tags:
- critical-point
- phase-diagram
- supercritical
stage: advanced
status: draft
---

# Critical Point and Supercritical Fluids

## Core Idea
The critical point is the endpoint of the liquid-vapor boundary on a phase diagram (T_c, P_c). Above the critical temperature, liquid and gas become indistinguishable (supercritical fluid). The critical point is characterized by (∂P/∂V)_T = 0 and (∂²P/∂V²)_T = 0.

## Explainer

From phase diagrams and the Clausius-Clapeyron equation, you know that the liquid-vapor boundary is a curve in the P-T plane along which both phases coexist in equilibrium. If you follow this boundary upward — increasing both temperature and pressure — what happens? The density of the vapor increases (it becomes more compressed), while the density of the liquid decreases (thermal expansion). At some point, the two densities must converge. The **critical point** (T_c, P_c) is exactly where they meet: above this temperature, there is no longer a meaningful distinction between liquid and gas.

The mathematical signature of the critical point is that the P-V isotherm develops an inflection point with zero slope: (∂P/∂V)_T = 0 and (∂²P/∂V²)_T = 0 simultaneously. On the van der Waals equation, these two conditions uniquely determine T_c = 8a/27Rb and P_c = a/27b², giving the critical point in terms of the intermolecular interaction parameters a and b. Below T_c, isotherms have a "swaybacked" region where the van der Waals equation predicts (∂P/∂V)_T > 0 — a mechanically unstable region that resolves into the coexisting liquid and vapor phases via the Maxwell construction. Above T_c, isotherms are monotonically decreasing and no phase separation occurs.

A **supercritical fluid** exists above T_c and P_c. Because liquid and gas become indistinguishable at the critical point, you can continuously transform liquid into gas above T_c without ever crossing a phase boundary — by going around the critical point. A supercritical fluid shares properties of both phases: it has the density of a liquid but the diffusivity and viscosity of a gas, making it an excellent solvent and transport medium. Supercritical CO₂ (T_c = 304 K, P_c = 73 atm) is industrially important for decaffeination, pharmaceutical extraction, and dry cleaning precisely because it has liquid-like solvating power with gas-like penetration into porous materials.

Near the critical point, something physically dramatic occurs: **critical opalescence**. Density fluctuations grow over length scales comparable to the wavelength of visible light, scattering it strongly and making the fluid appear milky. This is a signature that the system has no preferred length scale — fluctuations occur at all scales simultaneously. The compressibility (∂V/∂P)_T diverges as T → T_c because the usual resistance to compression vanishes: at the critical point, it costs almost no energy to rearrange matter between liquid-like and gas-like density. These diverging fluctuations near the critical point are the entry point to the much deeper subject of critical phenomena and universal scaling.
