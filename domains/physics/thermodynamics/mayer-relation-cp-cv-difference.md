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
status: validated
---

# Mayer's Relation: Cp − Cv = R

## Core Idea
Mayer's relation states that for an ideal gas, Cp − Cv = R (per mole). This arises because at constant pressure, part of the heat goes into work: Cp − Cv = P(∂V/∂T)_P = R. The difference reflects the flow work required for expansion at constant pressure.

## Questions

```yaml
- question: "A student argues that since heating at constant volume involves no work, Cv captures 'pure' heat input, making Cv larger than Cp. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "The student is correct — Cv > Cp because no energy is wasted on work"
    - "Cp > Cv because at constant pressure, extra heat must supply both the temperature rise and the expansion work against the surroundings"
    - "Cv = Cp for all ideal gases because internal energy depends only on temperature"
    - "Cp > Cv only for monatomic gases; for diatomic gases they are equal"
  answer: 1
  explanation: "The student has the causal direction backwards. At constant pressure, the gas expands and does PdV work on its surroundings. That work energy leaves the system without raising temperature, so you must supply more heat to achieve the same ΔT as you would at constant volume. This is why Cp is always larger than Cv — the 'extra' heat goes into expansion work, quantified exactly as R per mole for ideal gases."

- question: "A monatomic ideal gas has Cv = (3/2)R. What is its Cp, and what is the physical origin of the difference?"
  type: multiple-choice
  options:
    - "Cp = (3/2)R — the same as Cv because monatomic gases have no rotational modes"
    - "Cp = (5/2)R — the extra R accounts for the PdV expansion work done at constant pressure"
    - "Cp = (7/2)R — the extra 2R accounts for both rotational and vibrational modes"
    - "Cp = 2R — the extra R/2 accounts for kinetic energy of translation in the pressure direction"
  answer: 1
  explanation: "By Mayer's relation, Cp = Cv + R = (3/2)R + R = (5/2)R. The extra R is the same for all ideal gases regardless of molecular complexity — it comes from the P(∂V/∂T)_P = R work term, not from any internal degrees of freedom. For a diatomic ideal gas, Cv = (5/2)R and Cp = (7/2)R — still differing by exactly R."

- question: "The difference Cp − Cv = R holds exactly for all ideal gases, regardless of whether they are monatomic, diatomic, or polyatomic."
  type: true-false
  answer: true
  explanation: "Yes — the derivation of Mayer's relation uses only two properties of ideal gases: (1) PV = nRT, which gives P(∂V/∂T)_P = nR, and (2) internal energy depends only on temperature, so (∂U/∂T)_P = (∂U/∂T)_V = Cv. Neither assumption depends on molecular structure. The extra R always comes from expansion work, making Cp − Cv = R universal for ideal gases regardless of how many degrees of freedom the molecule has."

- question: "For a real gas at high pressure near its condensation point, the difference Cp − Cv will be approximately R, just as for an ideal gas."
  type: true-false
  answer: false
  explanation: "For real gases with significant intermolecular interactions, Cp − Cv deviates from R. The exact relation is Cp − Cv = −T(∂P/∂V)_T(∂V/∂T)²_P, which reduces to R only when (∂U/∂V)_T = 0 — i.e., when molecules don't interact and compressing them doesn't change their potential energy. Near condensation, intermolecular attractions are strong and (∂U/∂V)_T ≠ 0, so the departure from R is a measurable diagnostic of intermolecular interactions."

- question: "Why does heating an ideal gas at constant pressure require more energy than heating it to the same final temperature at constant volume?"
  type: short-answer
  answer: "At constant pressure, the gas expands as it heats, doing work on its surroundings (W = PΔV = nRΔT for an ideal gas). That work energy leaves the system without contributing to the temperature rise. To reach the same final temperature, you must supply extra heat equal to nRΔT to compensate for the energy lost to expansion work. At constant volume, no expansion occurs and all heat goes directly into raising internal energy (and thus temperature). The difference in heat required per degree — Cp − Cv = R — equals exactly the work done per mole per kelvin of temperature rise."
  explanation: "The key is that heat and work are both forms of energy transfer. At constant pressure, the total heat input must cover two things: the internal energy increase (same as at constant volume) plus the expansion work done against the surroundings. For ideal gases, the work term PdV = nRdT per degree, so Cp = Cv + R. This is why Cₚ > Cᵥ for any substance, and why the difference equals exactly R for ideal gases — it is a direct measure of the expansion work term in the first law."
```

## Explainer

From your study of heat capacities and enthalpy, you have two distinct ways to heat a gas: hold the volume fixed, or hold the pressure fixed. At constant volume, all the heat you add goes directly into increasing the internal energy of the gas — raising the kinetic energy of the molecules. At constant pressure, the gas is free to expand, and when it expands it pushes on its surroundings, doing work. This means heating at constant pressure requires extra energy: you must supply both the thermal energy to raise the temperature and the mechanical energy to push back the atmosphere. **Cₚ is always larger than Cᵥ** for any substance, but for ideal gases the difference is exactly R, a universal constant.

The derivation makes this precise. The first law at constant pressure gives dQ = dU + PdV. By definition, Cₚ = (dQ/dT)_P = (dU/dT)_P + P(dV/dT)_P. The second term, P(∂V/∂T)_P, is the work term. For an ideal gas, PV = nRT, so P(∂V/∂T)_P = nR. Meanwhile, for an ideal gas, internal energy U depends only on temperature (not volume) — the molecules don't interact, so squeezing them together or spreading them apart doesn't change U. Therefore (∂U/∂T)_P = (∂U/∂T)_V = Cᵥ. Putting it together: Cₚ = Cᵥ + nR, or per mole, Cₚ − Cᵥ = R ≈ 8.314 J/(mol·K).

The physical picture is straightforward. When you add 1 mole of heat at constant volume, the temperature rises by ΔT = Q/Cᵥ. All of that heat went into molecular kinetic energy. When you add the same 1 mole of heat at constant pressure, the temperature rise is smaller: ΔT = Q/Cₚ < Q/Cᵥ. The "missing" temperature rise went into expansion work. For a monatomic ideal gas, Cᵥ = (3/2)R (three translational degrees of freedom, each contributing R/2 from the equipartition theorem), so Cₚ = (5/2)R. For a diatomic gas at room temperature, Cᵥ = (5/2)R (adding two rotational degrees of freedom), so Cₚ = (7/2)R. In both cases the difference is exactly R.

The ratio γ = Cₚ/Cᵥ = (Cᵥ + R)/Cᵥ appears throughout thermodynamics and is directly measurable. For monatomic gases γ = 5/3 ≈ 1.67; for diatomic gases γ = 7/5 = 1.40. This ratio sets the speed of sound: v = √(γRT/M), which is why sound travels faster in helium (γ = 5/3, M small) than in air (γ = 7/5). It also governs adiabatic processes: when a gas expands adiabatically, TV^{γ−1} = const and PV^γ = const. The steepness of the adiabatic curve on a PV diagram relative to the isothermal curve is exactly γ. Every time you calculate an adiabatic compression, an engine efficiency, or an acoustic velocity, Mayer's relation is quietly behind the γ that appears.

Mayer's relation holds exactly for ideal gases because the assumption (∂U/∂V)_T = 0 is exact for non-interacting molecules. For real gases, molecules do interact, and compressing them changes their potential energy as well as kinetic energy. The general relation is Cₚ − Cᵥ = −T(∂P/∂V)_T(∂V/∂T)²_P, which reduces to R for ideal gases but gives corrections for real gases near condensation or at high pressure. The departure from Cₚ − Cᵥ = R is itself a useful diagnostic: it measures intermolecular interactions through the **internal pressure** (∂U/∂V)_T, a term that vanishes for ideal gases and grows as conditions depart from ideality.


