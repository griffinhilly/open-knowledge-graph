---
id: critical-point-behavior-substances
title: Critical Point and Supercritical Fluid Behavior
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: van-der-waals-derivation
  type: soft
tags:
- critical-point
- supercritical
- phase-transitions
stage: advanced
status: draft
---

# Critical Point and Supercritical Fluid Behavior

## Core Idea
At the critical point, the distinction between liquid and gas phases disappears; above this point no amount of pressure can liquefy a gas. Critical temperature, pressure, and density are substance-specific properties that mark the limit of two-phase coexistence. Understanding critical behavior is important for high-pressure systems and near-critical fluids used in advanced thermodynamic cycles and extraction processes.

## Explainer

Start with the phase diagram you know: pressure on the vertical axis, temperature on the horizontal, with a vapor pressure curve separating the liquid and gas regions. This curve represents conditions where liquid and gas coexist in equilibrium. Move up that curve — increasing both pressure and temperature — and something remarkable happens at the **critical point** (Tc, Pc): the distinction between liquid and gas disappears entirely. The density of the liquid phase decreases and the density of the gas phase increases as you approach the critical point, until they converge to the same value — the **critical density** ρ_c. At and above the critical point, there is only one fluid phase.

The van der Waals equation you've studied is the simplest model that captures this. The critical point occurs where the pressure-volume isotherm has an inflection point — both (∂P/∂V)_T = 0 and (∂²P/∂V²)_T = 0 simultaneously. These two conditions, applied to the van der Waals equation, yield T_c = 8a/(27Rb), P_c = a/(27b²), and V_c = 3nb — explicit expressions for the critical properties in terms of the molecular interaction parameters a (attraction) and b (excluded volume). The critical point is the temperature and pressure at which the attractive and repulsive contributions exactly balance at the inflection. Below T_c, the P-V isotherm has an S-curve with a physical two-phase region (the Maxwell equal-area construction gives the actual phase boundary). Above T_c, the isotherm is monotonically decreasing — a single fluid phase at all pressures.

Above the critical point is the **supercritical fluid** region. A supercritical fluid has no meniscus (the liquid-gas interface that you see when boiling), and you cannot liquefy it by applying pressure alone — no matter how high you raise the pressure, it remains a single phase. Its properties are intermediate: liquid-like densities (which give high solvating power) combined with gas-like viscosities and diffusivities (which give rapid mass transfer). Supercritical CO₂ (T_c = 31°C, P_c = 73 atm) is the industrial workhorse: coffee decaffeination, pharmaceutical extraction, polymer processing, and dry cleaning all exploit its tunability. By adjusting pressure and temperature, you can dial the density — and therefore the solubility of target compounds — with precision not available in either a pure liquid or a pure gas.

Near the critical point, large density fluctuations develop because the restoring force against compression nearly vanishes. Light scattering from these fluctuations produces **critical opalescence** — an otherwise clear fluid becomes milky white — a striking visual confirmation that the two phases are becoming indistinguishable. These fluctuations also mean that near-critical fluids are extremely sensitive to tiny changes in temperature and pressure: small perturbations cause large responses in density, heat capacity, and compressibility. For engineering applications near T_c, this sensitivity is both a feature (high tunability) and a challenge (precise control required). Understanding the critical point is not merely academic — it defines the operating envelope for high-pressure process equipment and sets the boundary conditions for equations of state used throughout chemical engineering design.
