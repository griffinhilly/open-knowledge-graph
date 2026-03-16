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

## Explainer

A heat pump is mechanically identical to a refrigerator — the same vapor-compression cycle, the same compressor, the same refrigerant. The difference is which heat exchange you care about. A refrigerator removes heat from a cold space (the interior) and rejects it to a warm space (the kitchen); you value Q_cold, the heat removed from inside. A heat pump does the same thermodynamic cycle but you value Q_hot, the heat delivered to the warm space (the room being heated). The compressor work W_in drives the cycle, and by the first law, Q_hot = Q_cold + W_in. This single energy balance is the source of the key relationship: **COP_heating = Q_hot / W_in = (Q_cold + W_in) / W_in = COP_cooling + 1**.

That "+1" is the crucial insight. Since COP_cooling is always positive, COP_heating is always greater than 1. An electric resistance heater converts exactly 1 kWh of electrical work into 1 kWh of heat — a COP of 1 by definition. A heat pump delivers *more* heat energy than the electrical energy it consumes, because it is not converting electricity to heat; it is using electricity to *move* heat from outside to inside. A COP of 3 means 3 kWh of heat delivered per kWh of electricity consumed — three times as efficient as resistance heating. The "extra" energy comes from the outdoor air or ground, which cools down slightly as the heat pump extracts heat from it.

**Air-source heat pumps** extract heat from outdoor air. The Carnot limit for heating is COP_Carnot = T_hot / (T_hot − T_cold) in absolute temperatures. As outdoor temperature T_cold drops, the denominator grows and the Carnot limit falls — meaning real performance must also fall. At −10°C outdoors with 20°C indoors, T_hot = 293 K and T_cold = 263 K gives Carnot COP_heating = 293/30 ≈ 9.8, but real systems achieve only 2–2.5 at such temperatures due to compression irreversibilities, heat-exchanger temperature differences, and defrost cycles needed to prevent ice buildup on the outdoor coil. Below some balance-point temperature, the heat pump cannot meet the full heating load and auxiliary resistance heating supplements it.

**Ground-source heat pumps** (geothermal) avoid this degradation by extracting heat from the ground or groundwater, which stays near 10–15°C year-round in temperate climates. The more stable source temperature means the temperature difference across the cycle stays nearly constant, so COP remains in the 3–5 range regardless of outdoor air temperature. The trade-off is installation cost: buried ground loops require excavation or boreholes. Analysis of a heat pump system involves computing the seasonal COP over a range of operating conditions, integrating across the heating season's temperature distribution, and comparing total electrical consumption to the equivalent resistance-heating baseline. The crossover — where the capital cost of a heat pump is recovered through operating savings — depends on local electricity and fuel prices and climate.
