---
id: vapor-compression-refrigeration-cycles
title: Vapor-Compression Refrigeration Cycles
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: vapor-compression-refrigeration-cycle
  type: hard
- id: isentropic-efficiency-devices
  type: soft
builds-toward:
- absorption-refrigeration-systems
- heat-pump-cycles-detailed
- throttling-expansion-isenthalpic-process
tags:
- refrigeration
- vapor-compression
- cooling
- cop
stage: advanced
status: draft
---

# Vapor-Compression Refrigeration Cycles

## Core Idea
Vapor-compression cycles (evaporator, compressor, condenser, throttle valve) deliver cooling by compressing refrigerant vapor, enabling condensation at elevated pressure, then expanding to low pressure for evaporation. Coefficient of performance COP = Q_c/W_in depends on evaporator and condenser temperatures; real systems achieve 40-70% of Carnot COP due to compressor inefficiency and pressure drops.

## Explainer

The vapor-compression refrigeration cycle is the Rankine cycle run backward — instead of using heat to produce work, you use work to move heat from a cold space to a warm one. You already understand vapor-compression refrigeration at a conceptual level from your prerequisite. Here the goal is to master the state-by-state thermodynamic analysis so you can compute exactly how much cooling a given system delivers and how efficiently it does so.

The cycle has four components and four state points. Starting at **state 1** — low-pressure, saturated (or slightly superheated) vapor leaving the evaporator: the refrigerant has absorbed heat from the cold space at low pressure and temperature. The **compressor** raises the refrigerant to high pressure, increasing both temperature and enthalpy; for an isentropic compressor, s_2 = s_1 and h_2 = h_1 + w_compressor. At **state 2** — high-pressure superheated vapor — the refrigerant enters the **condenser**, where it rejects heat to the warm environment at constant pressure and condenses to saturated liquid (**state 3**). The heat rejected is q_H = h_2 − h_3. The refrigerant then passes through the **throttle valve** (expansion valve), an isenthalpic process (h_4 = h_3) that drops pressure and temperature dramatically, producing a two-phase mixture at **state 4**. The low-pressure, low-temperature mixture enters the **evaporator**, absorbing heat from the cold space as it boils back to vapor, completing the cycle. The cooling load is q_L = h_1 − h_4.

**Coefficient of performance** COP = q_L / w_compressor = (h_1 − h_4) / (h_2 − h_1). Unlike a heat engine's efficiency (which is always less than 1), COP can be much greater than 1 — a typical household refrigerator has COP ≈ 2 to 4, meaning it delivers 2–4 units of cooling per unit of electricity consumed. The theoretical upper limit is the Carnot COP = T_L / (T_H − T_L), where temperatures are in Kelvin. A refrigerator maintaining a space at 4°C (277 K) against a 35°C (308 K) environment has Carnot COP = 277/31 ≈ 8.9. Real systems achieve 40–70% of this because compressors have isentropic efficiency below 1, pressure drops occur in lines and heat exchangers, and heat transfer requires finite temperature differences.

The key insight for design is that COP improves dramatically as the temperature difference narrows. Subcooling the liquid below state 3 (cooling it further in the condenser) increases h_3 − h_4 and thus the refrigerating effect without changing compressor work, improving COP. Superheating at the compressor inlet ensures no liquid enters the compressor (which would cause damage) and slightly increases the refrigerating effect. These are the standard practical modifications to the ideal vapor-compression cycle, and their thermodynamic justification is visible directly on the p-h (pressure-enthalpy) diagram, which is the refrigeration engineer's preferred cycle representation.
