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

## Explainer

From your study of the Carnot cycle and thermal efficiency, you know that a heat engine absorbs heat Q_H from a hot reservoir, does work W, and rejects heat Q_C to a cold reservoir. Thermal efficiency is defined as η = W/Q_H = 1 − Q_C/Q_H. The Carnot cycle is special: it consists entirely of reversible processes (two isothermal and two adiabatic legs), and it is this reversibility that determines its efficiency. The question that Carnot's theorem answers is: what is the maximum efficiency any engine can achieve between the same two temperature reservoirs?

The proof of Carnot's theorem uses a clever reductio ad absurdum. Suppose an engine exists with efficiency greater than the Carnot efficiency. Run the Carnot engine in reverse as a refrigerator, pumping heat from cold to hot. Drive this refrigerator using the output of the super-efficient engine. If the hypothetical engine could beat Carnot, the net effect would be a spontaneous flow of heat from the cold reservoir to the hot reservoir with no other effect — a violation of the second law of thermodynamics. Since that is impossible, no engine can exceed Carnot efficiency. The same argument shows that all reversible engines between the same reservoirs must have the same efficiency: if one reversible engine were more efficient than another, the less efficient one could run in reverse to create the same violation.

The formula **η_Carnot = 1 − T_C/T_H** (with temperatures in Kelvin) follows from computing the heat exchanged in each isothermal leg. During the isothermal expansion at T_H, the engine absorbs Q_H; during the isothermal compression at T_C, it rejects Q_C. For a reversible process, the entropy change of the reservoir equals −Q/T. Since the cycle returns the engine to its initial state (zero net entropy change for the engine), the entropy changes in the two reservoirs must cancel: Q_H/T_H = Q_C/T_C. Substituting this into the efficiency formula gives the Carnot result immediately.

The practical implications are stark. A coal power plant operating between a steam temperature of 600°C (873 K) and a condenser at 30°C (303 K) has a Carnot limit of 1 − 303/873 ≈ 65%. Real plants achieve 35–45% due to friction, heat losses, and irreversibilities. Raising T_H or lowering T_C both improve the limit, but with diminishing returns: halving T_C/T_H doesn't halve the gap to 100%. The formula also reveals a deep asymmetry — a small increase in T_H at already high temperatures buys less efficiency than the same increase near the bottom of the temperature scale. This is why cryogenic engineering can achieve striking efficiencies for refrigeration, but why no practical heat engine can approach 100% efficiency given any realistic temperature constraints.
