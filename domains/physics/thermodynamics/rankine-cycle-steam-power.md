---
id: rankine-cycle-steam-power
title: The Rankine Cycle and Steam Power Plants
domain: physics
course: thermodynamics
prerequisites:
- id: phase-transitions
  type: hard
- id: thermodynamic-processes
  type: hard
builds-toward:
  - ts-diagram-entropy-temperature
tags:
- cycles
- steam-power
- two-phase
stage: formal-systems
status: draft
---
# The Rankine Cycle and Steam Power Plants

## Core Idea
The Rankine cycle models steam power plants: isentropic compression of liquid water (pump), isobaric heat addition to produce steam (boiler), isentropic expansion through a turbine (power output), and isobaric heat rejection in the condenser. The Rankine efficiency is typically η = (W_net)/Q_in = (W_turbine - W_pump)/Q_boiler; real cycles have lower efficiency due to irreversibilities. Understanding the Rankine cycle is essential for power plant design and explains the two-phase behavior needed for efficient large-scale power generation.

## How It's Best Learned
Use steam tables to solve Rankine cycle problems. Plot cycles on T-S diagrams. Compare ideal (isentropic) with real (irreversible) turbines.

## Common Misconceptions
- Thinking the pump work is negligible (it is small compared to turbine work, but not zero).
- Assuming all expansion is isentropic (real turbines have non-zero entropy increase).
- Confusing the condenser temperature with ambient temperature (it can be higher due to pressure).

## Explainer

From your study of thermodynamic processes, you know how to describe isentropic (adiabatic reversible) and isobaric (constant pressure) processes on a system. The **Rankine cycle** chains four such processes into a loop that converts thermal energy from burning fuel into shaft work in a turbine — the basic design of every steam power plant, nuclear plant, and geothermal facility. The cycle runs in a regime your earlier work on phase transitions makes essential: water deliberately crosses the liquid-vapor boundary, because the latent heat of vaporization allows enormous amounts of energy to be stored and released at constant temperature.

Trace the cycle step by step. In the **pump** (state 1 → 2), liquid water at the condenser pressure is compressed isentropically to boiler pressure. Liquid is nearly incompressible, so very little work is required — this is why pump work is small compared to turbine work. In the **boiler** (state 2 → 3), high-pressure water is heated at constant pressure: first the liquid heats up to the saturation temperature, then it vaporizes (absorbing latent heat at constant temperature), and in a superheated cycle it continues heating as steam. This isobaric heat addition is where Q_in comes from — the furnace or reactor supplies this energy. In the **turbine** (state 3 → 4), high-pressure steam expands isentropically, doing work on the turbine blades as it drops in pressure and temperature. This is where the cycle's output comes from. In the **condenser** (state 4 → 1), the low-pressure steam is cooled at constant pressure, condensing back to liquid water by rejecting heat Q_out to the environment. The cycle then repeats.

The thermal efficiency η = W_net / Q_in = 1 − Q_out/Q_in is bounded above by the Carnot efficiency η_Carnot = 1 − T_cold/T_hot. In the Rankine cycle, T_hot corresponds to the maximum steam temperature and T_cold to the condenser temperature. This tells you directly how to improve efficiency: raise the boiler temperature and pressure (so T_hot increases), lower the condenser pressure (so T_cold decreases), or superheat the steam to increase the average temperature at which heat is added. Real cycles fall below the ideal because turbine expansion is irreversible (friction, heat loss), increasing entropy rather than keeping it constant. **Turbine isentropic efficiency** η_t = (h₃ − h₄_actual) / (h₃ − h₄_ideal) quantifies this degradation using steam table enthalpies.

The reason the Rankine cycle uses a two-phase working fluid rather than a simple ideal gas (as in the Brayton cycle for jet engines) is that condensation and boiling allow isothermal heat exchange at high heat transfer rates in compact equipment. A two-phase condenser can reject enormous heat while barely changing temperature. Superheating the steam before the turbine serves a practical purpose: if the turbine expansion enters the wet region (liquid droplets form), the droplets erode the turbine blades. Understanding the Rankine cycle as a T-S diagram — where the area inside the loop equals W_net and the area under the upper curve equals Q_in — gives you an immediate visual intuition for how cycle modifications trade off efficiency against hardware constraints.
