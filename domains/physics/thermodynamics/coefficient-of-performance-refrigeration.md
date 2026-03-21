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

## Questions

```yaml
- question: "A heat pump has a COP_heat of 3. For every 1 kJ of electrical work supplied, how much heat energy is delivered to the warm space?"
  type: multiple-choice
  options:
    - "1 kJ — equal to the work input, since energy is conserved"
    - "2 kJ — only the heat drawn from the cold reservoir is delivered"
    - "3 kJ — the work plus the heat drawn from the cold reservoir"
    - "More than 3 kJ — a Carnot heat pump always exceeds its COP rating"
  answer: 2
  explanation: "COP_heat = Q_H/W, so Q_H = COP × W = 3 × 1 kJ = 3 kJ. This is not a violation of energy conservation: the heat pump moves Q_C = 2 kJ from the cold reservoir and adds the 1 kJ of work as heat, delivering Q_H = 3 kJ total. Option A is the resistance-heater answer — it conflates moving heat with creating it."

- question: "A ground-source heat pump draws heat from underground soil at 10°C and delivers it to a house at 22°C. An air-source heat pump delivers heat to the same house but draws from outdoor air at −5°C. Which has a higher Carnot COP, and why?"
  type: multiple-choice
  options:
    - "The air-source pump, because colder outdoor air provides more thermal energy to extract"
    - "Both are identical — Carnot COP depends only on the indoor delivery temperature"
    - "The ground-source pump, because the smaller temperature difference between source and sink increases the Carnot COP"
    - "The ground-source pump, because underground heat is renewable and Carnot bounds only apply to fossil fuels"
  answer: 2
  explanation: "Carnot COP_heat = T_H/(T_H − T_C). The ground-source pump has T_H = 295 K, T_C = 283 K, giving 295/12 ≈ 24.6. The air-source pump has T_H = 295 K, T_C = 268 K, giving 295/27 ≈ 10.9. A smaller temperature difference means less work is required per unit of heat delivered — the thermodynamic bound is simply more favorable."

- question: "The coefficient of performance of a refrigerator (COP_ref = Q_C/W) can be greater than 1."
  type: true-false
  answer: true
  explanation: "Yes — COP_ref measures useful cooling output (heat removed from the cold space) per unit of work input. Since Q_C can be much larger than W, COP values of 2–5 are typical for modern refrigerators. The term 'coefficient of performance' was chosen precisely because 'efficiency' (usually capped at 100%) would be misleadingly restrictive for devices that move heat rather than convert it."

- question: "A refrigerator and a heat pump operating between the same two temperatures have equal coefficients of performance."
  type: true-false
  answer: false
  explanation: "COP_heat = Q_H/W and COP_ref = Q_C/W. Since Q_H = Q_C + W, we have COP_heat = COP_ref + 1. A heat pump always has a COP one unit higher than the refrigerator operating between the same temperatures. The heat pump's useful output includes both the heat drawn from the cold reservoir and the work input itself, while the refrigerator's useful output is only the heat removed from the cold space."

- question: "Why can the COP of a heat pump exceed 1, even though no energy conversion device can be more than 100% efficient?"
  type: short-answer
  answer: "A heat pump does not convert work into heat — it uses work to move heat from one place to another. The work input plus the heat drawn from the cold reservoir both end up delivered to the warm space. 'Efficiency' (output/input of the same energy form) caps at 1; COP measures a different ratio — useful heat delivered per unit of work — which can exceed 1 because the system harvests heat from the environment."
  explanation: "This is the key conceptual shift from heat engines. An electric resistance heater converts work to heat at COP = 1 (exactly). A heat pump uses the same work to leverage free environmental heat, delivering far more total heat. COP > 1 is not magic — it reflects the second law: moving heat from a warmer reservoir to an even warmer one requires relatively little work when the temperature difference is small."
```

## Explainer

You already know that a heat engine operates by absorbing heat Q_H from a hot reservoir, converting some to work W, and rejecting the remainder Q_C = Q_H − W to a cold reservoir. The efficiency η = W/Q_H is bounded above by the Carnot efficiency η_C = 1 − T_C/T_H. A **refrigerator** or **heat pump** runs this cycle in reverse: work is supplied to move heat from a cold reservoir to a hot one. The first law still applies — energy is conserved — so Q_H = Q_C + W. You're spending work to "pump" heat uphill against the natural flow.

The term **coefficient of performance** (COP) replaces "efficiency" because the ratio of output to input can exceed 1, making "efficiency" misleading. For a **refrigerator**, the useful output is the heat removed from the cold space, Q_C, and the cost is the work input W: COP_ref = Q_C/W. A higher COP means more cooling per unit of electricity. For a **heat pump**, the useful output is the heat delivered to the warm space, Q_H: COP_heat = Q_H/W. Since Q_H = Q_C + W, we have COP_heat = COP_ref + 1 — a heat pump always delivers more heat energy than the work it consumes. This is why heat pumps are far more efficient for space heating than electric resistance heaters (which have a COP of exactly 1).

The Carnot limit applies here too. The most efficient possible refrigerator operating between temperatures T_C and T_H has COP_ref,Carnot = T_C/(T_H − T_C), and COP_heat,Carnot = T_H/(T_H − T_C). These limits follow directly from Carnot's theorem applied to a reversed cycle: any irreversibility — friction, heat transfer across finite temperature differences, non-quasi-static processes — reduces the COP below the Carnot value. Notice that as T_H − T_C → 0 (the temperature difference shrinks), both Carnot COPs diverge: pumping heat across a tiny temperature difference requires very little work. As T_H − T_C grows, the Carnot COP falls. A refrigerator cooling to −20°C in a 35°C environment (T_C ≈ 253 K, T_H ≈ 308 K) has a Carnot COP_ref of 253/55 ≈ 4.6; real systems achieve perhaps half of this.

The practical implication for design is that COP improves when the temperature difference between source and sink is minimized. A ground-source heat pump exploits the relatively stable underground temperature (≈10°C year-round) rather than the cold winter air (−10°C or colder), achieving a much smaller T_H − T_C and therefore a much higher COP than an air-source system. This is a direct application of Carnot's result: technology cannot overcome the thermodynamic bound, but engineering can choose conditions that make the bound more favorable.
