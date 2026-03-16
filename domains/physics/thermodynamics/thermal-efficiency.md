---
id: thermal-efficiency
title: Thermal Efficiency of Heat Engines
domain: physics
course: thermodynamics
prerequisites:
- id: heat-engines
  type: hard
builds-toward:
- refrigerators-and-heat-pumps
- carnot-efficiency
tags:
- efficiency
- thermal-efficiency
- work-output
- heat-input
- energy-conversion
stage: formal-systems
status: validated
---

# Thermal Efficiency of Heat Engines

## Core Idea
The thermal efficiency of a heat engine is e = W/Q_H = 1 − Q_C/Q_H — the fraction of the input heat that is converted to useful work. Since W = Q_H − Q_C, and Q_C > 0 always, efficiency is always less than 100%. Efficiency measures how effectively an engine uses its fuel. Real engines (gasoline ≈ 25–35%, diesel ≈ 35–45%, combined-cycle gas turbines ≈ 55–60%) fall well below the theoretical Carnot maximum.

## How It's Best Learned
Compute efficiency for engines described by Q_H and Q_C values, then relate those to the temperatures using the Carnot limit as a reference. Explore why improving efficiency matters practically: a 1% increase in car engine efficiency reduces fuel consumption and emissions significantly across a fleet.

## Common Misconceptions
- Efficiency of 0.30 means 30% of heat in becomes work — not 70% loss due to poor engineering alone; 70% is rejected heat, bounded by thermodynamic limits.
- Higher efficiency does not always mean more power output; efficiency and power are separate quantities.

## Explainer

From heat engines, you know the basic setup: a working fluid absorbs heat Q_H from a hot reservoir, performs work W on the surroundings, and rejects heat Q_C to a cold reservoir. Energy conservation applied to one complete cycle (the fluid returns to its initial state, so ΔU = 0) gives W = Q_H − Q_C. **Thermal efficiency** e = W/Q_H asks: of all the heat energy you paid for, what fraction became useful mechanical work? The remainder, 1 − e = Q_C/Q_H, was dumped as waste heat to the cold reservoir.

Why is efficiency always less than 1? The second law forbids an engine that operates using only a single thermal reservoir — you cannot complete a cycle without a cold sink. The working fluid must return to its initial state after each cycle; rejecting Q_C to a cold reservoir is the mechanism by which it does so. This is not an engineering failure that better materials could fix — it is a fundamental thermodynamic constraint. The maximum possible efficiency for any engine operating between temperatures T_H and T_C is set by the **Carnot efficiency** e_Carnot = 1 − T_C/T_H. No engine, regardless of design or working fluid, can exceed this limit. The Carnot engine achieves it by operating entirely reversibly — no friction, no heat transfer across finite temperature differences, no irreversibility of any kind.

Real engines fall below the Carnot limit because every real process generates entropy. A gasoline engine operating between combustion temperatures (~2000 K) and ambient (~300 K) has a theoretical Carnot ceiling of about 85%, yet achieves only 25–35% in practice. The ~50% gap represents **entropy generation** through combustion irreversibility, friction, heat loss through cylinder walls, and turbulence. Diesel engines run hotter and achieve 35–45%. Combined-cycle gas turbines (~60%) close the gap by cascading: hot exhaust from the gas turbine drives a steam cycle, so what would be wasted heat becomes the hot input of a second engine. Each stage extracts work from the remaining temperature gradient, reducing the overall waste.

A practical skill: use the formula e = 1 − Q_C/Q_H to convert between the three quantities W, Q_H, and Q_C for any specified operating condition. If an engine with e = 0.35 produces 700 kJ of work per cycle, then Q_H = 700/0.35 = 2000 kJ absorbed and Q_C = 2000 − 700 = 1300 kJ rejected. Efficiency and power output are separate quantities that can trade off against each other: an engine running slowly at maximum efficiency may produce less power per unit time than one running faster but less efficiently. Turbine designers face this tradeoff explicitly — the efficiency-maximizing operating point is rarely the power-maximizing one, and the best choice depends on whether fuel cost or peak output is the binding constraint.
