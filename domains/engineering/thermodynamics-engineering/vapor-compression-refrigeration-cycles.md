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
tags:
- refrigeration
- vapor-compression
- cooling
- cop
stage: formal-systems
status: validated
---
# Vapor-Compression Refrigeration Cycles

## Core Idea
Vapor-compression cycles (evaporator, compressor, condenser, throttle valve) deliver cooling by compressing refrigerant vapor, enabling condensation at elevated pressure, then expanding to low pressure for evaporation. Coefficient of performance COP = Q_c/W_in depends on evaporator and condenser temperatures; real systems achieve 40-70% of Carnot COP due to compressor inefficiency and pressure drops.

## Questions

```yaml
- question: "A refrigerator maintains a cold space at 4°C (277 K) against a 35°C (308 K) ambient environment. What is the theoretical maximum (Carnot) COP?"
  type: multiple-choice
  options:
    - "308/277 ≈ 1.11 — the ratio of hot to cold absolute temperatures"
    - "277/31 ≈ 8.9 — the cold temperature divided by the temperature difference"
    - "31/277 ≈ 0.11 — the temperature difference divided by the cold temperature"
    - "(308 − 277)/308 ≈ 0.10 — analogous to the Carnot heat engine efficiency"
  answer: 1
  explanation: "Carnot COP for a refrigerator = T_L / (T_H − T_L) = 277 / (308 − 277) = 277/31 ≈ 8.9. This means an ideal refrigerator could deliver 8.9 units of cooling per unit of work input. Option A gives the Carnot heat engine efficiency formula, applied incorrectly. Option C inverts the Carnot COP formula. Option D is the Carnot heat engine efficiency — a completely different metric for a different cycle direction."

- question: "An engineer adds subcooling to a vapor-compression system — cooling the liquid refrigerant further past state 3 before it reaches the throttle valve. Why does this improve COP?"
  type: multiple-choice
  options:
    - "It lowers the compressor inlet temperature, reducing the work the compressor must do"
    - "It increases the enthalpy drop across the evaporator (more cooling per unit mass of refrigerant circulated) without increasing compressor work"
    - "It raises the condensing pressure, reducing the pressure ratio across the compressor"
    - "It converts liquid to vapor before the throttle valve, recovering expansion work"
  answer: 1
  explanation: "Subcooling reduces the enthalpy at state 3 (h_3 decreases). Since the throttle is isenthalpic (h_4 = h_3), h_4 also decreases. The cooling effect is q_L = h_1 − h_4, so a lower h_4 increases q_L. Compressor work (h_2 − h_1) is unchanged because subcooling occurs after the compressor. COP = q_L/w_compressor therefore improves. The compressor inlet (state 1) is unaffected by subcooling — that state is determined by the evaporator, not the condenser."

- question: "The coefficient of performance of a refrigerator must always be less than 1 because delivering more cooling than the electrical work input would violate conservation of energy."
  type: true-false
  answer: false
  explanation: "COP can greatly exceed 1 — typical household refrigerators have COP of 2 to 4, and the Carnot limit can approach 9 or higher for mild temperature differences. Energy is conserved because the system moves heat, not converts it. The energy balance is: W (work in) + Q_c (heat from cold space) = Q_H (heat rejected to hot environment). COP = Q_c/W, and since Q_c can be much larger than W, COP >> 1 is perfectly consistent with the first law. Confusing COP with heat engine efficiency is the common error — efficiency of a heat engine must be less than 1, but COP of a refrigerator or heat pump has no such constraint."

- question: "The throttle (expansion) valve in a vapor-compression cycle is an isenthalpic device — enthalpy is conserved across it, not entropy."
  type: true-false
  answer: true
  explanation: "The throttle valve is a highly irreversible device: the refrigerant passes through a restriction, pressure drops dramatically, and entropy increases (irreversibility). Enthalpy, however, is conserved (h_4 = h_3) because the process is adiabatic and no work is done. This contrasts with an isentropic turbine, where entropy is conserved and enthalpy drops as work is extracted. A turbine would recover expansion work but is impractical for refrigeration (two-phase flow, small size, cost); the simpler throttle valve trades work recovery for mechanical simplicity."

- question: "Why does COP decrease as the temperature difference between the cold space and the hot environment increases, and what does this imply for practical refrigerator and heat pump design?"
  type: short-answer
  answer: "Carnot COP = T_L / (T_H − T_L). As the temperature difference grows, the denominator increases and COP falls — more work is required per unit of cooling or heating delivered. A freezer at −20°C against 30°C ambient (ΔT = 50 K) has much lower Carnot COP than a refrigerator at +4°C against the same ambient (ΔT = 26 K). Practically, this means: (1) systems should minimize unnecessary temperature lifts — don't cool a space colder than needed; (2) subcooling and superheating help by narrowing the effective temperature range over which heat exchange occurs; and (3) condensers should be kept as cool as possible (e.g., by using ambient air efficiently) to reduce T_H."
  explanation: "This also explains why geothermal heat pumps outperform air-source heat pumps in cold climates: ground temperature is more stable (smaller ΔT) than air temperature in winter, so the ground-source system operates at a higher COP year-round."
```

## Explainer

The vapor-compression refrigeration cycle is the Rankine cycle run backward — instead of using heat to produce work, you use work to move heat from a cold space to a warm one. You already understand vapor-compression refrigeration at a conceptual level from your prerequisite. Here the goal is to master the state-by-state thermodynamic analysis so you can compute exactly how much cooling a given system delivers and how efficiently it does so.

The cycle has four components and four state points. Starting at **state 1** — low-pressure, saturated (or slightly superheated) vapor leaving the evaporator: the refrigerant has absorbed heat from the cold space at low pressure and temperature. The **compressor** raises the refrigerant to high pressure, increasing both temperature and enthalpy; for an isentropic compressor, s_2 = s_1 and h_2 = h_1 + w_compressor. At **state 2** — high-pressure superheated vapor — the refrigerant enters the **condenser**, where it rejects heat to the warm environment at constant pressure and condenses to saturated liquid (**state 3**). The heat rejected is q_H = h_2 − h_3. The refrigerant then passes through the **throttle valve** (expansion valve), an isenthalpic process (h_4 = h_3) that drops pressure and temperature dramatically, producing a two-phase mixture at **state 4**. The low-pressure, low-temperature mixture enters the **evaporator**, absorbing heat from the cold space as it boils back to vapor, completing the cycle. The cooling load is q_L = h_1 − h_4.

**Coefficient of performance** COP = q_L / w_compressor = (h_1 − h_4) / (h_2 − h_1). Unlike a heat engine's efficiency (which is always less than 1), COP can be much greater than 1 — a typical household refrigerator has COP ≈ 2 to 4, meaning it delivers 2–4 units of cooling per unit of electricity consumed. The theoretical upper limit is the Carnot COP = T_L / (T_H − T_L), where temperatures are in Kelvin. A refrigerator maintaining a space at 4°C (277 K) against a 35°C (308 K) environment has Carnot COP = 277/31 ≈ 8.9. Real systems achieve 40–70% of this because compressors have isentropic efficiency below 1, pressure drops occur in lines and heat exchangers, and heat transfer requires finite temperature differences.

The key insight for design is that COP improves dramatically as the temperature difference narrows. Subcooling the liquid below state 3 (cooling it further in the condenser) increases h_3 − h_4 and thus the refrigerating effect without changing compressor work, improving COP. Superheating at the compressor inlet ensures no liquid enters the compressor (which would cause damage) and slightly increases the refrigerating effect. These are the standard practical modifications to the ideal vapor-compression cycle, and their thermodynamic justification is visible directly on the p-h (pressure-enthalpy) diagram, which is the refrigeration engineer's preferred cycle representation.
