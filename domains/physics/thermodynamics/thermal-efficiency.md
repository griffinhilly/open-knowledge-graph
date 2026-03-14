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
