---
id: adiabatic-processes
title: Adiabatic Processes
domain: physics
course: thermodynamics
prerequisites:
- id: thermodynamic-processes
  type: hard
- id: equipartition-theorem
  type: soft
- id: heat-capacity-of-gases
  type: soft
builds-toward:
- carnot-cycle
tags:
- adiabatic
- no-heat-transfer
- adiabatic-exponent
- gamma
- temperature-change
stage: formal-systems
status: validated
---
# Adiabatic Processes

## Core Idea
An adiabatic process involves no heat exchange with the surroundings (Q = 0), so all work done comes at the expense of internal energy: ΔU = −W. For an ideal gas undergoing a reversible adiabatic process, PV^γ = constant, where γ = Cp/Cv is the adiabatic index (ratio of heat capacities). Adiabatic processes occur in rapid compressions/expansions where heat exchange is too slow: diesel engine compression, sound propagation, and rising air masses in the atmosphere.

## How It's Best Learned
Compare the slope of an adiabat versus an isotherm on a PV diagram — the adiabat is steeper (slope −γP/V vs −P/V) because compression heats the gas, raising pressure more than the isotherm predicts. Derive PV^γ = constant from the first law and the ideal gas law.

## Common Misconceptions
- Adiabatic does not mean isothermal — in adiabatic compression the temperature increases; in adiabatic expansion it decreases.
- Adiabatic processes are only reversible if quasi-static; a rapid free expansion is adiabatic but irreversible.

## Questions

```yaml
- question: "A piston rapidly compresses an ideal gas with no heat exchanged with the surroundings. What happens to the temperature of the gas?"
  type: multiple-choice
  options:
    - "It stays constant — an adiabatic process means no temperature change"
    - "It decreases — compression always cools a gas"
    - "It increases — since Q = 0, all work done on the gas increases its internal energy and therefore its temperature"
    - "It depends on the piston speed — temperature only changes in fast compressions"
  answer: 2
  explanation: "The key relation is ΔU = −W (from the first law with Q = 0). Work done on the gas (positive W on the gas) increases internal energy. For an ideal gas, internal energy is U = nCᵥT, so rising internal energy means rising temperature. The common misconception is confusing adiabatic with isothermal — isothermal processes keep temperature constant by allowing heat to flow; adiabatic processes allow no heat flow, so the temperature must change to accommodate energy changes from work."

- question: "On a PV diagram, compare an adiabatic expansion and an isothermal expansion starting from the same state. Which curve falls more steeply as volume increases?"
  type: multiple-choice
  options:
    - "The isotherm — constant temperature means pressure drops faster with volume"
    - "The adiabat — because γ > 1, the slope magnitude |dP/dV| = γP/V exceeds the isotherm slope P/V"
    - "They trace the same path — adiabatic and isothermal processes are equivalent at high speeds"
    - "The adiabat is shallower — gas cooling during expansion reduces pressure less than temperature alone would predict"
  answer: 1
  explanation: "On an isotherm (constant T), P = nRT/V so the slope is dP/dV = −P/V. On an adiabat, the slope is dP/dV = −γP/V, steeper by the factor γ > 1. The physical reason: during adiabatic expansion, the gas does work and cools (temperature drops), which reduces pressure by more than the volume increase alone would. The cooling effect adds to the pressure drop, making the adiabat fall faster. This is why the adiabat and isotherm through the same point always cross at that point, with the adiabat steeper."

- question: "An adiabatic process is the same as an isothermal process — both maintain constant conditions by preventing heat from entering or leaving the system."
  type: true-false
  answer: false
  explanation: "These are entirely different processes. Adiabatic means Q = 0 — no heat transfer — but temperature is free to change as a consequence of work. Isothermal means constant temperature — but to maintain constant temperature while work is done, heat must flow in or out. An isothermal compression requires the gas to expel heat to keep T constant; an adiabatic compression allows no heat to flow, so the temperature rises instead. The two processes are thermodynamically opposite in how they handle temperature versus heat exchange."

- question: "During adiabatic compression of an ideal gas, the temperature increases because all work done on the gas is converted into internal energy."
  type: true-false
  answer: true
  explanation: "This follows directly from the first law with Q = 0: ΔU = −W, meaning any work done on the gas (which contributes negative W in the convention ΔU = Q − W) shows up entirely as increased internal energy. For an ideal gas, internal energy depends only on temperature, so rising internal energy means rising temperature. This is why diesel engines achieve ignition without a spark — the adiabatic compression of air raises the temperature high enough to ignite fuel spontaneously."

- question: "Why does adiabatic compression heat a gas while isothermal compression does not, even though both processes increase the pressure on the gas?"
  type: short-answer
  answer: "In isothermal compression, the temperature is held constant by allowing heat to flow out of the gas as it is compressed — the work done on the gas is immediately exported as heat, so internal energy and temperature stay the same. In adiabatic compression, no heat can escape. All the work done on the gas must appear as increased internal energy, and for an ideal gas, increased internal energy means increased temperature. The difference comes down to what happens to the energy from the work: in isothermal, it leaves as heat; in adiabatic, it stays in the gas and raises its temperature."
  explanation: "The first law makes this precise: ΔU = Q − W. Set Q = 0 (adiabatic) and you get ΔU = −W — work done on gas raises internal energy. Set ΔU = 0 (isothermal, since internal energy of an ideal gas depends only on T) and you get Q = W — heat must flow out equal to the work done on the gas. The two constraints are simply different choices about which term in the first law you hold fixed."
```

## Explainer

You already know the first law of thermodynamics: ΔU = Q − W. An **adiabatic process** is defined by a single constraint: Q = 0. No heat flows in or out. This immediately means that every joule of work done on the gas shows up as increased internal energy, and every joule the gas does as work comes at the expense of its internal energy: ΔU = −W. The challenge is figuring out what this implies for pressure, volume, and temperature simultaneously — and that requires knowing how the internal energy of an ideal gas depends on temperature.

Here is where the equipartition theorem (your soft prerequisite) and the heat capacity at constant volume C_V come in. For an ideal gas, the internal energy is U = n C_V T, so any change in internal energy is a change in temperature: dU = n C_V dT. Now combine this with the first law (dU = −P dV for an adiabatic process) and the ideal gas law (PV = nRT). Differentiating the ideal gas law and substituting gives a differential equation that separates cleanly to yield the **adiabatic relation**: PV^γ = constant, where **γ = C_P / C_V** is the **adiabatic index**. For a monatomic ideal gas, γ = 5/3; for diatomic gases like air at room temperature, γ ≈ 1.4.

The adiabatic index γ > 1 is key to understanding why the adiabat is steeper than the isotherm on a PV diagram. On an isotherm (constant T), P = nRT/V so dP/dV = −P/V. On an adiabat, dP/dV = −γP/V — steeper by the factor γ. This makes sense physically: on an isotherm, compressing the gas raises pressure simply because volume decreases. On an adiabat, compressing the gas *also heats it up* (temperature rises), which raises the pressure by an extra factor. The reverse holds for expansion: adiabatic expansion causes cooling, which is why air cools when it rises in the atmosphere — the expansion against lower pressure is approximately adiabatic, and the drop in temperature (the adiabatic lapse rate) determines much of atmospheric structure.

Two subtle points are worth holding onto. First, "adiabatic" does not require that the process happen fast — it requires that no heat is exchanged. A perfectly insulated piston moves adiabatically at any speed. In practice, fast processes are *approximately* adiabatic because there is no time for heat to flow; slow processes with good insulation are adiabatic by design. Second, adiabatic does not imply reversible. A quick free expansion into a vacuum is adiabatic (no heat flows, no work done on surroundings either) but highly irreversible — the gas does no work and its temperature does not change, yet entropy increases. The special case where an adiabatic process is also reversible (quasi-static) is called an **isentropic process**, and it is the one described by PV^γ = constant.
