---
id: heat-engines
title: Heat Engines
domain: physics
course: thermodynamics
prerequisites:
- id: first-law-of-thermodynamics
  type: hard
- id: thermodynamic-processes
  type: hard
- id: isobaric-and-isochoric-processes
  type: soft
builds-toward:
- thermal-efficiency
- refrigerators-and-heat-pumps
- second-law-of-thermodynamics
- carnot-cycle
tags:
- heat-engine
- thermodynamic-cycle
- work-output
- hot-reservoir
- cold-reservoir
stage: formal-systems
status: validated
---
# Heat Engines

## Core Idea
A heat engine is a device that converts thermal energy into mechanical work by operating in a cycle between a hot reservoir (at temperature T_H) and a cold reservoir (at temperature T_C). In each cycle, the engine absorbs heat Q_H from the hot reservoir, converts some to work W, and rejects the remainder Q_C to the cold reservoir. By the first law for a complete cycle (ΔU = 0): W = Q_H − Q_C. No heat engine converts heat entirely into work — some is always rejected.

## How It's Best Learned
Draw an energy flow diagram (Sankey diagram) for a heat engine showing Q_H flowing in, W exiting, and Q_C flowing out. Apply this to familiar examples: steam turbines, internal combustion engines, jet engines. The constraint that Q_C > 0 is a consequence of the Second Law, not the First.

## Common Misconceptions
- A heat engine does not 'use up' heat — it degrades high-quality thermal energy into lower-quality rejected heat plus useful work.
- 100% efficiency is impossible not because of friction or practical limitations, but due to a fundamental thermodynamic principle (Second Law).

## Explainer

From the first law of thermodynamics, you know that energy is conserved: ΔU = Q − W for any process. A heat engine is a device that exploits this relationship cyclically. "Cyclically" is the key word — after one full cycle, the working substance (steam, gas, or whatever) returns to its original state, so ΔU = 0 for the full cycle. The first law then gives W = Q_net = Q_H − Q_C: the net work output equals the heat absorbed from the hot reservoir minus the heat rejected to the cold reservoir. This is not an approximation or an idealization — it is just energy conservation.

The efficiency η = W/Q_H = 1 − Q_C/Q_H measures how much of the input heat is converted to useful work. The constraint Q_C > 0 (some heat must always be rejected) is not a consequence of friction or engineering imperfection — it is required by the Second Law. A machine that absorbed Q_H and converted all of it to work would be a **perpetual motion machine of the second kind**, impossible not because it violates energy conservation (the first law is satisfied) but because it would require heat to flow spontaneously from cold to hot or entropy to decrease. The direction of heat flow — always from hot to cold — is itself the Second Law's content.

Visualizing the engine as an energy flow diagram helps: Q_H flows into the engine from the hot reservoir, the engine outputs W upward (as mechanical work, electricity, or other useful forms), and Q_C flows downward to the cold reservoir. The three quantities satisfy Q_H = W + Q_C at all times. Common real engines — steam turbines in power plants, the gasoline engine in a car, jet engines in aircraft — all fit this template. In a car engine, the hot reservoir is the burning fuel mixture (~2000 K), the cold reservoir is the exhaust (~700 K), and W drives the crankshaft. The actual efficiency of a car engine (typically 20–35%) is much less than the theoretical maximum because of friction, non-ideal processes, and heat losses.

The theoretical maximum efficiency for any engine operating between T_H and T_C is the **Carnot efficiency** η_Carnot = 1 − T_C/T_H, which you will derive when studying the Carnot cycle. The Carnot limit shows that efficiency increases as the temperature ratio T_H/T_C grows larger. This is why power plant engineers work hard to raise steam temperatures (T_H) and use cooling towers to lower rejection temperatures (T_C) — every degree of improvement in the ratio means more work out per unit of fuel consumed.
