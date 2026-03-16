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

## Explainer

A **heat engine** is any device that converts thermal energy into mechanical work by operating cyclically between a hot reservoir at temperature T_H and a cold reservoir at temperature T_C. From your study of the Carnot cycle, you know one specific example: the ideal engine that runs through two isothermal and two adiabatic steps. Engine **efficiency** is defined as the fraction of the heat absorbed from the hot reservoir that gets converted to useful work: η = W_net / Q_H. Since energy is conserved over one cycle (ΔU = 0), we have W_net = Q_H − Q_C, so η = 1 − Q_C / Q_H. The question is: how small can Q_C / Q_H be?

The answer comes from the second law of thermodynamics. In any cyclic process, the total entropy change of the universe must be non-negative. The engine absorbs Q_H from the hot reservoir (lowering its entropy by Q_H / T_H) and dumps Q_C into the cold reservoir (raising its entropy by Q_C / T_C). The second law requires: Q_C / T_C − Q_H / T_H ≥ 0, which means Q_C / Q_H ≥ T_C / T_H. Substituting into the efficiency formula: η ≤ 1 − T_C / T_H. The **Carnot efficiency** η_C = 1 − T_C / T_H is the upper bound — achieved only when the entropy inequality is an equality, which happens only for a reversible engine.

Carnot's theorem states this more directly: no engine operating between two thermal reservoirs can be more efficient than a reversible engine operating between those same two reservoirs. All reversible engines operating between T_H and T_C achieve exactly η_C, regardless of their working substance or cycle details. Any irreversible engine achieves less. This is not an engineering limitation waiting to be overcome with better materials — it is a consequence of the second law of thermodynamics, as fundamental as energy conservation.

The practical implications are sobering. A coal power plant operating between a flame at roughly 800 K and the environment at 300 K faces a Carnot limit of 1 − 300/800 ≈ 62.5%. Real plants achieve 35–45% due to irreversibilities. A car engine operating between combustion temperatures (~2000 K) and ambient (~300 K) has a Carnot limit near 85%, but real engines achieve 25–35%. The gap between ideal and actual efficiency is the engineer's challenge, but the ceiling itself is set by T_C / T_H — which is why industrial processes burn fuel as hot as possible and exhaust heat as cold as possible. The efficiency formula η_C = 1 − T_C / T_H also shows that η_C → 1 only when T_C → 0 (absolute zero) or T_H → ∞, neither of which is achievable in practice.
