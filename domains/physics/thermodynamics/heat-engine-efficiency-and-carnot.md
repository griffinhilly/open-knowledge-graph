---
id: heat-engine-efficiency-and-carnot
title: Heat Engine Efficiency and Carnot's Theorem
domain: physics
course: thermodynamics
prerequisites:
- id: heat-engines
  type: hard
- id: carnot-cycle
  type: hard
tags:
- heat-engines
- efficiency
- carnot
- second-law
stage: formal-systems
status: draft
---

# Heat Engine Efficiency and Carnot's Theorem

## Core Idea
Heat engine efficiency is η = W_net / Q_in. The Carnot engine, operating between two thermal reservoirs, achieves maximum efficiency: η_Carnot = 1 − T_C/T_H. No real engine can exceed this; it is an upper bound set by the second law. This shows the fundamental limit imposed by thermodynamics.

## Questions

```yaml
- question: "A heat engine absorbs heat from a reservoir at 800 K and exhausts to a cold reservoir at 200 K. What is the maximum possible efficiency?"
  type: multiple-choice
  options:
    - "25%"
    - "50%"
    - "60%"
    - "75%"
  answer: 3
  explanation: "η_Carnot = 1 − T_C/T_H = 1 − 200/800 = 1 − 0.25 = 0.75 = 75%. Temperatures must be in Kelvin (absolute). The 25% option is T_C/T_H itself — confusing the heat rejected fraction with the efficiency. No engine operating between these reservoirs can exceed 75%, regardless of its design, working fluid, or engineering quality."

- question: "An engineering team claims their frictionless, perfectly insulated engine operating between 600 K and 300 K achieves 60% efficiency. What can you conclude?"
  type: multiple-choice
  options:
    - "This is plausible — friction and insulation losses are the main practical barriers to high efficiency"
    - "This violates the second law of thermodynamics and is physically impossible"
    - "This is achievable with advanced materials that reduce irreversibilities"
    - "The claim is valid for certain working fluids but not others"
  answer: 1
  explanation: "η_Carnot for this engine = 1 − 300/600 = 50%. A claimed 60% exceeds the Carnot limit. Carnot's theorem states that no engine operating between two fixed reservoirs can exceed the efficiency of a reversible engine between those same reservoirs. This is not an engineering limitation — it is a consequence of the second law. No materials, working fluids, or engineering refinements can overcome it."

- question: "An engine operating between reservoirs at 1000 K and 500 K can theoretically achieve 80% efficiency with sufficiently advanced engineering."
  type: true-false
  answer: false
  explanation: "η_Carnot = 1 − 500/1000 = 50%. The 50% limit is set by the second law of thermodynamics, not by engineering imperfection. Even a perfectly reversible engine — the Carnot engine — achieves exactly 50% between these reservoirs. Claiming 80% would require violating the entropy non-decrease principle. Advanced engineering can close the gap between real and Carnot efficiency, but it cannot raise the ceiling."

- question: "To maximize the efficiency of a heat engine, an engineer should both increase the hot reservoir temperature and decrease the cold reservoir temperature."
  type: true-false
  answer: true
  explanation: "η_Carnot = 1 − T_C/T_H. Increasing T_H makes the fraction T_C/T_H smaller (better). Decreasing T_C also makes T_C/T_H smaller (better). Both changes independently improve efficiency, and together they compound. This is why industrial power plants burn fuel as hot as materials allow and exhaust heat through cooling towers to get T_C as close to ambient as possible."

- question: "Why can a heat engine never achieve 100% efficiency, and why does the Carnot formula use absolute temperatures in Kelvin rather than Celsius or Fahrenheit?"
  type: short-answer
  answer: "Efficiency reaches 100% only when T_C/T_H = 0, which requires either T_C = 0 K (absolute zero, unachievable by the third law) or T_H = ∞ (impossible). The Carnot formula derives from the entropy balance: ΔS_universe = Q_C/T_C − Q_H/T_H ≥ 0, where T must be absolute (Kelvin) because entropy change Q/T is only meaningful on the absolute scale. Celsius and Fahrenheit have arbitrary zeros and would give physically nonsensical results."
  explanation: "The entropy argument is the deep reason for both constraints. The second law requires Q_C/T_C ≥ Q_H/T_H, bounding Q_C from below. Efficiency η = 1 − Q_C/Q_H is therefore bounded above by 1 − T_C/T_H. Both T_C > 0 K (third law) and T_H < ∞ (practical) prevent the bound from reaching 1."
```

## Explainer

A **heat engine** is any device that converts thermal energy into mechanical work by operating cyclically between a hot reservoir at temperature T_H and a cold reservoir at temperature T_C. From your study of the Carnot cycle, you know one specific example: the ideal engine that runs through two isothermal and two adiabatic steps. Engine **efficiency** is defined as the fraction of the heat absorbed from the hot reservoir that gets converted to useful work: η = W_net / Q_H. Since energy is conserved over one cycle (ΔU = 0), we have W_net = Q_H − Q_C, so η = 1 − Q_C / Q_H. The question is: how small can Q_C / Q_H be?

The answer comes from the second law of thermodynamics. In any cyclic process, the total entropy change of the universe must be non-negative. The engine absorbs Q_H from the hot reservoir (lowering its entropy by Q_H / T_H) and dumps Q_C into the cold reservoir (raising its entropy by Q_C / T_C). The second law requires: Q_C / T_C − Q_H / T_H ≥ 0, which means Q_C / Q_H ≥ T_C / T_H. Substituting into the efficiency formula: η ≤ 1 − T_C / T_H. The **Carnot efficiency** η_C = 1 − T_C / T_H is the upper bound — achieved only when the entropy inequality is an equality, which happens only for a reversible engine.

Carnot's theorem states this more directly: no engine operating between two thermal reservoirs can be more efficient than a reversible engine operating between those same two reservoirs. All reversible engines operating between T_H and T_C achieve exactly η_C, regardless of their working substance or cycle details. Any irreversible engine achieves less. This is not an engineering limitation waiting to be overcome with better materials — it is a consequence of the second law of thermodynamics, as fundamental as energy conservation.

The practical implications are sobering. A coal power plant operating between a flame at roughly 800 K and the environment at 300 K faces a Carnot limit of 1 − 300/800 ≈ 62.5%. Real plants achieve 35–45% due to irreversibilities. A car engine operating between combustion temperatures (~2000 K) and ambient (~300 K) has a Carnot limit near 85%, but real engines achieve 25–35%. The gap between ideal and actual efficiency is the engineer's challenge, but the ceiling itself is set by T_C / T_H — which is why industrial processes burn fuel as hot as possible and exhaust heat as cold as possible. The efficiency formula η_C = 1 − T_C / T_H also shows that η_C → 1 only when T_C → 0 (absolute zero) or T_H → ∞, neither of which is achievable in practice.
