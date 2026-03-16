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

## Explainer

You already know the first law of thermodynamics: ΔU = Q − W. An **adiabatic process** is defined by a single constraint: Q = 0. No heat flows in or out. This immediately means that every joule of work done on the gas shows up as increased internal energy, and every joule the gas does as work comes at the expense of its internal energy: ΔU = −W. The challenge is figuring out what this implies for pressure, volume, and temperature simultaneously — and that requires knowing how the internal energy of an ideal gas depends on temperature.

Here is where the equipartition theorem (your soft prerequisite) and the heat capacity at constant volume C_V come in. For an ideal gas, the internal energy is U = n C_V T, so any change in internal energy is a change in temperature: dU = n C_V dT. Now combine this with the first law (dU = −P dV for an adiabatic process) and the ideal gas law (PV = nRT). Differentiating the ideal gas law and substituting gives a differential equation that separates cleanly to yield the **adiabatic relation**: PV^γ = constant, where **γ = C_P / C_V** is the **adiabatic index**. For a monatomic ideal gas, γ = 5/3; for diatomic gases like air at room temperature, γ ≈ 1.4.

The adiabatic index γ > 1 is key to understanding why the adiabat is steeper than the isotherm on a PV diagram. On an isotherm (constant T), P = nRT/V so dP/dV = −P/V. On an adiabat, dP/dV = −γP/V — steeper by the factor γ. This makes sense physically: on an isotherm, compressing the gas raises pressure simply because volume decreases. On an adiabat, compressing the gas *also heats it up* (temperature rises), which raises the pressure by an extra factor. The reverse holds for expansion: adiabatic expansion causes cooling, which is why air cools when it rises in the atmosphere — the expansion against lower pressure is approximately adiabatic, and the drop in temperature (the adiabatic lapse rate) determines much of atmospheric structure.

Two subtle points are worth holding onto. First, "adiabatic" does not require that the process happen fast — it requires that no heat is exchanged. A perfectly insulated piston moves adiabatically at any speed. In practice, fast processes are *approximately* adiabatic because there is no time for heat to flow; slow processes with good insulation are adiabatic by design. Second, adiabatic does not imply reversible. A quick free expansion into a vacuum is adiabatic (no heat flows, no work done on surroundings either) but highly irreversible — the gas does no work and its temperature does not change, yet entropy increases. The special case where an adiabatic process is also reversible (quasi-static) is called an **isentropic process**, and it is the one described by PV^γ = constant.
