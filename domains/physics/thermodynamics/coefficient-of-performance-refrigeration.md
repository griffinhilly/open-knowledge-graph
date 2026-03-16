---
id: coefficient-of-performance-refrigeration
title: 'Coefficient of Performance: Heat Pumps and Refrigerators'
domain: physics
course: thermodynamics
prerequisites:
- id: heat-engines
  type: hard
- id: heat-engine-efficiency-and-carnot
  type: hard
builds-toward:
- refrigerators-and-heat-pumps
tags:
- heat-pump
- refrigeration
- cop
- cycle
stage: formal-systems
status: draft
---

# Coefficient of Performance: Heat Pumps and Refrigerators

## Core Idea
Heat pumps and refrigerators transfer heat from cold to hot, requiring work input. Their efficiency is measured by coefficient of performance (COP): COP_heat = Q_H/W, COP_ref = Q_C/W. The Carnot COP limit is COP_heat = T_H/(T_H − T_C), reflecting the second law's constraints on reversed cycles.

## Explainer

You already know that a heat engine operates by absorbing heat Q_H from a hot reservoir, converting some to work W, and rejecting the remainder Q_C = Q_H − W to a cold reservoir. The efficiency η = W/Q_H is bounded above by the Carnot efficiency η_C = 1 − T_C/T_H. A **refrigerator** or **heat pump** runs this cycle in reverse: work is supplied to move heat from a cold reservoir to a hot one. The first law still applies — energy is conserved — so Q_H = Q_C + W. You're spending work to "pump" heat uphill against the natural flow.

The term **coefficient of performance** (COP) replaces "efficiency" because the ratio of output to input can exceed 1, making "efficiency" misleading. For a **refrigerator**, the useful output is the heat removed from the cold space, Q_C, and the cost is the work input W: COP_ref = Q_C/W. A higher COP means more cooling per unit of electricity. For a **heat pump**, the useful output is the heat delivered to the warm space, Q_H: COP_heat = Q_H/W. Since Q_H = Q_C + W, we have COP_heat = COP_ref + 1 — a heat pump always delivers more heat energy than the work it consumes. This is why heat pumps are far more efficient for space heating than electric resistance heaters (which have a COP of exactly 1).

The Carnot limit applies here too. The most efficient possible refrigerator operating between temperatures T_C and T_H has COP_ref,Carnot = T_C/(T_H − T_C), and COP_heat,Carnot = T_H/(T_H − T_C). These limits follow directly from Carnot's theorem applied to a reversed cycle: any irreversibility — friction, heat transfer across finite temperature differences, non-quasi-static processes — reduces the COP below the Carnot value. Notice that as T_H − T_C → 0 (the temperature difference shrinks), both Carnot COPs diverge: pumping heat across a tiny temperature difference requires very little work. As T_H − T_C grows, the Carnot COP falls. A refrigerator cooling to −20°C in a 35°C environment (T_C ≈ 253 K, T_H ≈ 308 K) has a Carnot COP_ref of 253/55 ≈ 4.6; real systems achieve perhaps half of this.

The practical implication for design is that COP improves when the temperature difference between source and sink is minimized. A ground-source heat pump exploits the relatively stable underground temperature (≈10°C year-round) rather than the cold winter air (−10°C or colder), achieving a much smaller T_H − T_C and therefore a much higher COP than an air-source system. This is a direct application of Carnot's result: technology cannot overcome the thermodynamic bound, but engineering can choose conditions that make the bound more favorable.
