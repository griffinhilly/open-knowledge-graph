---
id: carnot-efficiency
title: Carnot Efficiency and Maximum Efficiency Theorem
domain: physics
course: thermodynamics
prerequisites:
- id: carnot-cycle
  type: hard
- id: thermal-efficiency
  type: hard
- id: entropy-in-thermodynamic-processes
  type: soft
- id: heat-transfer-radiation
  type: soft
tags:
- Carnot-efficiency
- maximum-efficiency
- temperature-ratio
- reversible-engine
stage: formal-systems
status: validated
---
# Carnot Efficiency and Maximum Efficiency Theorem

## Core Idea
The efficiency of a Carnot engine is e_Carnot = 1 − T_C/T_H, where temperatures are in Kelvin. This is the maximum possible efficiency for any engine operating between T_H and T_C — no real engine can exceed it. Carnot's theorem states that all reversible engines operating between the same two reservoirs have the same efficiency, and any irreversible engine has strictly lower efficiency. Improving efficiency requires raising T_H or lowering T_C, with diminishing returns as T_C approaches absolute zero.

## How It's Best Learned
Calculate Carnot efficiency for realistic temperature ranges: a steam turbine at 600°C rejecting to 30°C gives e_Carnot ≈ 66%. Compare to actual efficiencies of 35–45% — the gap is due to irreversibilities. Notice that efficiency is determined entirely by temperature ratio, independent of the working fluid.

## Common Misconceptions
- Carnot efficiency gives an upper bound, not a target — real engineers optimize for power output per unit cost, not maximum theoretical efficiency.
- Efficiency approaching 100% requires T_C → 0 K or T_H → ∞, both physically unattainable.
- The Carnot limit applies to heat engines; it does not directly apply to fuel cells or other non-thermal converters.
