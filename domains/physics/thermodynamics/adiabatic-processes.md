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
builds-toward:
- carnot-cycle
tags:
- adiabatic
- no-heat-transfer
- adiabatic-exponent
- gamma
- temperature-change
stage: formal-systems
status: draft
---

# Adiabatic Processes

## Core Idea
An adiabatic process involves no heat exchange with the surroundings (Q = 0), so all work done comes at the expense of internal energy: ΔU = −W. For an ideal gas undergoing a reversible adiabatic process, PV^γ = constant, where γ = Cp/Cv is the adiabatic index (ratio of heat capacities). Adiabatic processes occur in rapid compressions/expansions where heat exchange is too slow: diesel engine compression, sound propagation, and rising air masses in the atmosphere.

## How It's Best Learned
Compare the slope of an adiabat versus an isotherm on a PV diagram — the adiabat is steeper (slope −γP/V vs −P/V) because compression heats the gas, raising pressure more than the isotherm predicts. Derive PV^γ = constant from the first law and the ideal gas law.

## Common Misconceptions
- Adiabatic does not mean isothermal — in adiabatic compression the temperature increases; in adiabatic expansion it decreases.
- Adiabatic processes are only reversible if quasi-static; a rapid free expansion is adiabatic but irreversible.
