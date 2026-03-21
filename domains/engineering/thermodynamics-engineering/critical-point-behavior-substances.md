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

## Questions

```yaml
- question: "Carbon dioxide has a critical temperature of 31°C and a critical pressure of 73 atm. A cylinder contains CO₂ at 50°C. What happens if you continuously increase the pressure inside the cylinder?"
  type: multiple-choice
  options:
    - "The CO₂ will eventually liquefy once pressure exceeds 73 atm"
    - "The CO₂ will solidify at sufficiently high pressure"
    - "The CO₂ remains a single supercritical fluid phase regardless of how high the pressure rises"
    - "The CO₂ will condense into liquid once pressure exceeds twice the critical pressure"
  answer: 2
  explanation: "At 50°C — above the critical temperature of 31°C — CO₂ is in the supercritical region. The defining property of the supercritical region is that no amount of pressure can cause the gas to liquefy. There is no liquid-gas phase boundary above Tc. Increasing pressure compresses the supercritical fluid (increasing its density), but it never crosses a phase boundary because none exists above Tc. This is the core insight: the critical point is the temperature above which liquefaction by pressure alone is impossible."

- question: "Why are supercritical fluids useful as industrial solvents, such as in coffee decaffeination?"
  type: multiple-choice
  options:
    - "They have extremely low density, allowing them to penetrate solid matrices more deeply than liquids"
    - "They combine liquid-like densities (high solvating power) with gas-like viscosities (rapid mass transfer), and their properties are tunable by adjusting pressure and temperature"
    - "They operate at very low temperatures, preventing degradation of heat-sensitive compounds"
    - "They dissolve only polar compounds, making them highly selective solvents"
  answer: 1
  explanation: "The industrial utility of supercritical fluids comes from their hybrid properties: their density is high (liquid-like), giving strong solvating power to dissolve target compounds; but their viscosity and diffusivity remain gas-like, allowing rapid penetration and mass transfer through solid matrices. Crucially, the density — and therefore the selectivity for different compounds — can be dialed by adjusting pressure and temperature, a tunability unavailable with conventional liquid solvents. Option A has it backwards: high density (not low) drives solvating power."

- question: "As a substance approaches its critical point along the liquid-gas coexistence curve, the densities of the liquid and vapor phases become equal."
  type: true-false
  answer: true
  explanation: "This is precisely what defines the critical point: the two coexisting phases become identical. Moving up the vapor pressure curve, the liquid phase becomes less dense as it expands thermally, while the gas phase becomes denser as pressure rises. These densities converge until they meet at the critical density ρ_c at (Tc, Pc). At this point the meniscus — the visible interface between the two phases — disappears, because there is no longer a density difference to create a surface. Above the critical point, only one fluid phase exists."

- question: "A supercritical fluid can be converted to a liquid by increasing the pressure sufficiently, as long as the temperature is not too far above the critical temperature."
  type: true-false
  answer: false
  explanation: "This is the central misconception about the critical point. Above the critical temperature Tc, there is no liquid phase — the liquid-gas coexistence curve terminates at the critical point. No matter how high the pressure, a fluid above Tc remains a single supercritical fluid phase. The pressure-temperature phase diagram shows a solid, liquid, and gas region separated by phase boundaries, but the liquid-gas boundary ends at the critical point. What increasing pressure above Tc does is increase the density of the supercritical fluid, but it does not cross any phase boundary."

- question: "What is 'critical opalescence,' and what does it reveal about the physical state of a fluid near its critical point?"
  type: short-answer
  answer: "Critical opalescence is the phenomenon where a normally transparent fluid becomes milky-white as it approaches its critical point. It is caused by large-scale density fluctuations: near the critical point, the distinction between liquid and gas phases nearly vanishes, so large regions of the fluid fluctuate between liquid-like and gas-like densities. These density fluctuations scatter light across a wide range of wavelengths, producing the opalescent appearance. It reveals that the restoring force against compression nearly vanishes near the critical point, making the fluid extremely sensitive to small perturbations."
  explanation: "Critical opalescence is a direct visual confirmation that the two phases are becoming indistinguishable — it is not just an aesthetic curiosity but a window into the thermodynamic instability near the critical point. The same sensitivity that causes opalescence makes near-critical fluids highly responsive to small pressure and temperature changes, which is both useful (precise tunability) and challenging (difficult process control) for engineering applications."
```

## Explainer

Start with the phase diagram you know: pressure on the vertical axis, temperature on the horizontal, with a vapor pressure curve separating the liquid and gas regions. This curve represents conditions where liquid and gas coexist in equilibrium. Move up that curve — increasing both pressure and temperature — and something remarkable happens at the **critical point** (Tc, Pc): the distinction between liquid and gas disappears entirely. The density of the liquid phase decreases and the density of the gas phase increases as you approach the critical point, until they converge to the same value — the **critical density** ρ_c. At and above the critical point, there is only one fluid phase.

The van der Waals equation you've studied is the simplest model that captures this. The critical point occurs where the pressure-volume isotherm has an inflection point — both (∂P/∂V)_T = 0 and (∂²P/∂V²)_T = 0 simultaneously. These two conditions, applied to the van der Waals equation, yield T_c = 8a/(27Rb), P_c = a/(27b²), and V_c = 3nb — explicit expressions for the critical properties in terms of the molecular interaction parameters a (attraction) and b (excluded volume). The critical point is the temperature and pressure at which the attractive and repulsive contributions exactly balance at the inflection. Below T_c, the P-V isotherm has an S-curve with a physical two-phase region (the Maxwell equal-area construction gives the actual phase boundary). Above T_c, the isotherm is monotonically decreasing — a single fluid phase at all pressures.

Above the critical point is the **supercritical fluid** region. A supercritical fluid has no meniscus (the liquid-gas interface that you see when boiling), and you cannot liquefy it by applying pressure alone — no matter how high you raise the pressure, it remains a single phase. Its properties are intermediate: liquid-like densities (which give high solvating power) combined with gas-like viscosities and diffusivities (which give rapid mass transfer). Supercritical CO₂ (T_c = 31°C, P_c = 73 atm) is the industrial workhorse: coffee decaffeination, pharmaceutical extraction, polymer processing, and dry cleaning all exploit its tunability. By adjusting pressure and temperature, you can dial the density — and therefore the solubility of target compounds — with precision not available in either a pure liquid or a pure gas.

Near the critical point, large density fluctuations develop because the restoring force against compression nearly vanishes. Light scattering from these fluctuations produces **critical opalescence** — an otherwise clear fluid becomes milky white — a striking visual confirmation that the two phases are becoming indistinguishable. These fluctuations also mean that near-critical fluids are extremely sensitive to tiny changes in temperature and pressure: small perturbations cause large responses in density, heat capacity, and compressibility. For engineering applications near T_c, this sensitivity is both a feature (high tunability) and a challenge (precise control required). Understanding the critical point is not merely academic — it defines the operating envelope for high-pressure process equipment and sets the boundary conditions for equations of state used throughout chemical engineering design.
