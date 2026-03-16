---
id: transcritical-and-supercritical-cycles
title: Transcritical and Supercritical Power Cycles
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: rankine-cycle-thermodynamic-analysis
  type: hard
- id: critical-point-behavior-substances
  type: hard
tags:
- transcritical
- supercritical
- co2
- power-cycle
- efficiency
stage: advanced
status: draft
---

# Transcritical and Supercritical Power Cycles

## Core Idea
Supercritical Rankine cycles operate above the critical point (T > T_c, P > P_c), avoiding two-phase expansion and allowing continuous pressure-temperature paths. Transcritical cycles compress above critical pressure but cool below critical temperature. Advantages include higher cycle efficiency (especially with heat recovery), better turbine inlet conditions, and smaller component sizes. CO₂ cycles exploit these benefits for low-grade heat recovery.

## Explainer

In a conventional Rankine cycle, the working fluid is pumped as a liquid, heated until it boils, superheated as steam, and then expanded through a turbine. The two-phase boiling region — the dome on the P-v or T-s diagram — is where heat addition occurs at constant temperature and pressure. This isothermal boiling is efficient in one sense, but it creates a fixed relationship between heat-source temperature and cycle pressure that can make it hard to match the temperature profile of the heat source, and it produces wet steam at the turbine exit if care is not taken. Both of these issues disappear above the **critical point**.

At pressures above the critical pressure P_c and temperatures above the critical temperature T_c, the distinction between liquid and vapor ceases to exist. There is no dome, no phase boundary, no latent heat — just a single continuous supercritical fluid whose properties change smoothly with temperature and pressure. In a **supercritical Rankine cycle**, the pump raises pressure above P_c, and the "boiler" is replaced by a **supercritical heat exchanger** that heats the fluid from a dense, liquid-like state through the pseudocritical region (where properties change most rapidly) and into a low-density, gas-like state, all without any phase transition. This continuous heating profile allows the cycle's heat-addition curve on a T-s diagram to follow the heat source's temperature profile much more closely — reducing the temperature difference that drives irreversibility in the heat exchangers. Modern ultra-supercritical coal plants operate at ~30 MPa and ~600°C for this reason: higher pressure and temperature both raise thermal efficiency.

A **transcritical cycle** is a hybrid: the high-pressure side operates above P_c but the cooling side drops below the critical temperature, so the working fluid condenses conventionally on the low-pressure side. The CO₂ (carbon dioxide) cycle is the most important example. CO₂ has a critical point at only 31°C and 7.4 MPa — meaning it can be compressed to supercritical pressure relatively easily, but its critical temperature is close to ambient, so condensation on the low-pressure side occurs as normal liquid CO₂. The CO₂ transcritical cycle is used in heat pumps and refrigeration (it replaced CFCs in car air conditioners), and it is actively studied for waste-heat recovery from industrial processes and geothermal sources. Because CO₂ is non-flammable, non-toxic, cheap, and has a very small global-warming potential relative to synthetic refrigerants, these cycles are gaining significant commercial traction.

The main design challenge in both supercritical and transcritical cycles is the **internal heat exchanger** (or recuperator). Because the supercritical fluid's specific heat varies dramatically near the pseudocritical point, careful thermal design is needed to avoid large temperature mismatches within the recuperator itself. Poor recuperator design can undercut much of the efficiency gain. Compact high-effectiveness heat exchangers — often printed-circuit or microchannel designs — are typically required, which is why supercritical CO₂ (sCO₂) Brayton cycles for next-generation nuclear and concentrated solar power plants are physically much smaller than equivalent steam Rankine systems, even at the same power output.


