---
id: mayer-relation-cp-cv-difference
title: 'Mayer''s Relation: Cp − Cv = R'
domain: physics
course: thermodynamics
prerequisites:
- id: heat-capacity-constant-volume-pressure
  type: hard
- id: enthalpy-definition-and-significance
  type: hard
tags:
- heat-capacity
- ideal-gas
- thermodynamic-relations
stage: formal-systems
status: draft
---

# Mayer's Relation: Cp − Cv = R

## Core Idea
Mayer's relation states that for an ideal gas, Cp − Cv = R (per mole). This arises because at constant pressure, part of the heat goes into work: Cp − Cv = P(∂V/∂T)_P = R. The difference reflects the flow work required for expansion at constant pressure.

## Explainer

From your study of heat capacities and enthalpy, you have two distinct ways to heat a gas: hold the volume fixed, or hold the pressure fixed. At constant volume, all the heat you add goes directly into increasing the internal energy of the gas — raising the kinetic energy of the molecules. At constant pressure, the gas is free to expand, and when it expands it pushes on its surroundings, doing work. This means heating at constant pressure requires extra energy: you must supply both the thermal energy to raise the temperature and the mechanical energy to push back the atmosphere. **Cₚ is always larger than Cᵥ** for any substance, but for ideal gases the difference is exactly R, a universal constant.

The derivation makes this precise. The first law at constant pressure gives dQ = dU + PdV. By definition, Cₚ = (dQ/dT)_P = (dU/dT)_P + P(dV/dT)_P. The second term, P(∂V/∂T)_P, is the work term. For an ideal gas, PV = nRT, so P(∂V/∂T)_P = nR. Meanwhile, for an ideal gas, internal energy U depends only on temperature (not volume) — the molecules don't interact, so squeezing them together or spreading them apart doesn't change U. Therefore (∂U/∂T)_P = (∂U/∂T)_V = Cᵥ. Putting it together: Cₚ = Cᵥ + nR, or per mole, Cₚ − Cᵥ = R ≈ 8.314 J/(mol·K).

The physical picture is straightforward. When you add 1 mole of heat at constant volume, the temperature rises by ΔT = Q/Cᵥ. All of that heat went into molecular kinetic energy. When you add the same 1 mole of heat at constant pressure, the temperature rise is smaller: ΔT = Q/Cₚ < Q/Cᵥ. The "missing" temperature rise went into expansion work. For a monatomic ideal gas, Cᵥ = (3/2)R (three translational degrees of freedom, each contributing R/2 from the equipartition theorem), so Cₚ = (5/2)R. For a diatomic gas at room temperature, Cᵥ = (5/2)R (adding two rotational degrees of freedom), so Cₚ = (7/2)R. In both cases the difference is exactly R.

The ratio γ = Cₚ/Cᵥ = (Cᵥ + R)/Cᵥ appears throughout thermodynamics and is directly measurable. For monatomic gases γ = 5/3 ≈ 1.67; for diatomic gases γ = 7/5 = 1.40. This ratio sets the speed of sound: v = √(γRT/M), which is why sound travels faster in helium (γ = 5/3, M small) than in air (γ = 7/5). It also governs adiabatic processes: when a gas expands adiabatically, TV^{γ−1} = const and PV^γ = const. The steepness of the adiabatic curve on a PV diagram relative to the isothermal curve is exactly γ. Every time you calculate an adiabatic compression, an engine efficiency, or an acoustic velocity, Mayer's relation is quietly behind the γ that appears.

Mayer's relation holds exactly for ideal gases because the assumption (∂U/∂V)_T = 0 is exact for non-interacting molecules. For real gases, molecules do interact, and compressing them changes their potential energy as well as kinetic energy. The general relation is Cₚ − Cᵥ = −T(∂P/∂V)_T(∂V/∂T)²_P, which reduces to R for ideal gases but gives corrections for real gases near condensation or at high pressure. The departure from Cₚ − Cᵥ = R is itself a useful diagnostic: it measures intermolecular interactions through the **internal pressure** (∂U/∂V)_T, a term that vanishes for ideal gases and grows as conditions depart from ideality.


