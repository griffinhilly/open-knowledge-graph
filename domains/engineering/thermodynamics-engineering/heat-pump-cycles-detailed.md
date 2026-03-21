---
id: heat-pump-cycles-detailed
title: Heat Pump Cycles and Heating Applications
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: heat-pump-heating-cooling-analysis
  type: hard
- id: vapor-compression-refrigeration-cycles
  type: soft
builds-toward:
- combined-gas-steam-cycles
tags:
- heat-pump
- heating
- cop
- coefficient-performance
stage: advanced
status: draft
---

# Heat Pump Cycles and Heating Applications

## Core Idea
Heat pumps reverse refrigeration cycles to deliver heating; coefficient of performance COP_heating = Q_h/W_in = COP_cooling + 1. Modern air-source and ground-source heat pumps achieve seasonal COP of 2.5-4.0, making them 2-4 times more efficient than electric resistance heating. Performance degrades at low outdoor temperatures unless supplemented with auxiliary heating.

## Questions

```yaml
- question: "A heat pump delivers 9 kW of heat to a building while its compressor consumes 3 kW of electricity. What is COP_heating, and which statement best explains why this doesn't violate energy conservation?"
  type: multiple-choice
  options:
    - "COP = 3.0; the heat pump creates three times as much heat as electricity consumed, which does violate energy conservation and indicates a faulty measurement"
    - "COP = 3.0; the first law is satisfied because the heat pump also extracts 6 kW of heat from the outdoor environment, which combines with the 3 kW of electrical work to produce 9 kW of heat delivered"
    - "COP = 0.33; all real heating devices must have efficiency below 1 by the second law"
    - "COP = 3.0; this performance is only achievable by a Carnot heat pump operating between ideal reservoirs"
  answer: 1
  explanation: "Q_hot = Q_cold + W_in by the first law. The heat pump extracts Q_cold = 6 kW from the outdoor air and adds W_in = 3 kW of compressor work, delivering Q_hot = 9 kW indoors. Energy is conserved — the 'extra' heat comes from the outdoor environment, not from nowhere. COP_heating = Q_hot / W_in = 9/3 = 3.0. No thermodynamic law is violated; the heat pump is a heat mover, not a heat creator."

- question: "On a cold day (−15°C outdoors, 20°C indoors), an air-source heat pump achieves COP_heating = 1.5, while an electric resistance baseboard heater always has COP = 1.0. Which is the better choice for energy efficiency?"
  type: multiple-choice
  options:
    - "The resistance heater, because heat pumps become unreliable and inefficient below freezing"
    - "The heat pump, because COP 1.5 > 1.0 — it delivers 50% more heat per unit of electricity consumed than resistance heating, even at this degraded cold-weather performance"
    - "They are equivalent in practice; the 0.5 COP difference is within measurement uncertainty for real systems"
    - "The resistance heater, because the defrost cycles required at −15°C reduce the effective COP below 1.0"
  answer: 1
  explanation: "Even at COP = 1.5 on a very cold day, the heat pump delivers 1.5 kWh of heat per kWh of electricity — 50% more than resistance heating. As long as COP_heating > 1.0, the heat pump is more efficient. COP > 1 is guaranteed by COP_heating = COP_cooling + 1 ≥ 1 for any physically operating heat pump with non-negative COP_cooling. The degraded cold-weather performance is real but does not eliminate the efficiency advantage."

- question: "The coefficient of performance of a heat pump in heating mode is always greater than 1, even for a very poorly performing real heat pump."
  type: true-false
  answer: true
  explanation: "COP_heating = COP_cooling + 1. Since COP_cooling = Q_cold / W_in ≥ 0 (removing some heat from the cold reservoir is always non-negative for a physically operating system), COP_heating ≥ 1. This is why even a very inefficient heat pump delivers at least as much heat as resistance heating. The COP approaches 1 only in the limit where COP_cooling → 0 (no heat extracted from the cold reservoir, all heat from work alone — essentially resistance heating)."

- question: "A heat pump with COP = 4 creates heat from electrical energy, which is why it can deliver 4 kWh of thermal energy for every 1 kWh of electricity consumed."
  type: true-false
  answer: false
  explanation: "This is the central misconception. A heat pump does not create heat — it moves heat. The compressor uses 1 kWh of electricity to pump 3 kWh of heat from the cold outdoor environment to the warm indoor space, delivering 4 kWh total. The 'extra' 3 kWh was already present in the outdoor air; the compressor work provided the thermodynamic lift to move it against the temperature gradient. Energy is neither created nor destroyed — only relocated."

- question: "Explain why a heat pump with COP = 3 does not violate energy conservation, even though it delivers 3 kWh of heat for every 1 kWh of electricity consumed."
  type: short-answer
  answer: "The first law of thermodynamics requires Q_hot = Q_cold + W_in. The heat pump delivers 3 kWh to the building: 1 kWh comes from the electrical work input (W_in) and 2 kWh comes from heat extracted from the outdoor environment (Q_cold). The compressor uses electricity to drive the refrigerant cycle, which absorbs heat from the cold outdoor air at the evaporator and rejects it at higher temperature to the building at the condenser. Total energy in (1 kWh electricity + 2 kWh from outdoor air) equals total energy out (3 kWh heat to building). No energy is created — it is moved from outside to inside."
  explanation: "The distinction between 'moving heat' and 'creating heat' is the conceptual heart of heat pump thermodynamics. The COP can exceed 1 precisely because the heat pump is not converting work to heat (which would give COP = 1) but using work to pump heat from a reservoir that already contains it."
```

## Explainer

A heat pump is mechanically identical to a refrigerator — the same vapor-compression cycle, the same compressor, the same refrigerant. The difference is which heat exchange you care about. A refrigerator removes heat from a cold space (the interior) and rejects it to a warm space (the kitchen); you value Q_cold, the heat removed from inside. A heat pump does the same thermodynamic cycle but you value Q_hot, the heat delivered to the warm space (the room being heated). The compressor work W_in drives the cycle, and by the first law, Q_hot = Q_cold + W_in. This single energy balance is the source of the key relationship: **COP_heating = Q_hot / W_in = (Q_cold + W_in) / W_in = COP_cooling + 1**.

That "+1" is the crucial insight. Since COP_cooling is always positive, COP_heating is always greater than 1. An electric resistance heater converts exactly 1 kWh of electrical work into 1 kWh of heat — a COP of 1 by definition. A heat pump delivers *more* heat energy than the electrical energy it consumes, because it is not converting electricity to heat; it is using electricity to *move* heat from outside to inside. A COP of 3 means 3 kWh of heat delivered per kWh of electricity consumed — three times as efficient as resistance heating. The "extra" energy comes from the outdoor air or ground, which cools down slightly as the heat pump extracts heat from it.

**Air-source heat pumps** extract heat from outdoor air. The Carnot limit for heating is COP_Carnot = T_hot / (T_hot − T_cold) in absolute temperatures. As outdoor temperature T_cold drops, the denominator grows and the Carnot limit falls — meaning real performance must also fall. At −10°C outdoors with 20°C indoors, T_hot = 293 K and T_cold = 263 K gives Carnot COP_heating = 293/30 ≈ 9.8, but real systems achieve only 2–2.5 at such temperatures due to compression irreversibilities, heat-exchanger temperature differences, and defrost cycles needed to prevent ice buildup on the outdoor coil. Below some balance-point temperature, the heat pump cannot meet the full heating load and auxiliary resistance heating supplements it.

**Ground-source heat pumps** (geothermal) avoid this degradation by extracting heat from the ground or groundwater, which stays near 10–15°C year-round in temperate climates. The more stable source temperature means the temperature difference across the cycle stays nearly constant, so COP remains in the 3–5 range regardless of outdoor air temperature. The trade-off is installation cost: buried ground loops require excavation or boreholes. Analysis of a heat pump system involves computing the seasonal COP over a range of operating conditions, integrating across the heating season's temperature distribution, and comparing total electrical consumption to the equivalent resistance-heating baseline. The crossover — where the capital cost of a heat pump is recovered through operating savings — depends on local electricity and fuel prices and climate.
