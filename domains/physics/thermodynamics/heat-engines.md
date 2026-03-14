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
