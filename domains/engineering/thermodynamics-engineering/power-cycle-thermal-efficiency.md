---
id: power-cycle-thermal-efficiency
title: Power Cycle Analysis and Thermal Efficiency
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: second-law-analysis-practical
  type: hard
- id: steady-flow-energy-equation-engineering
  type: soft
builds-toward:
- rankine-power-generation-cycles
- brayton-gas-turbine-cycles
- internal-combustion-engine-cycles
tags:
- cycles
- efficiency
- power
- carnot
stage: advanced
status: draft
---

# Power Cycle Analysis and Thermal Efficiency

## Core Idea
Power cycles convert heat input to net work output with thermal efficiency η = W_net/Q_in. The Carnot cycle sets an upper bound: η_Carnot = 1 - T_cold/T_hot. Real cycles (Rankine, Brayton, Otto) operate below Carnot due to irreversibilities and practical constraints. Cycle efficiency improves through higher pressure ratios, superheat, reheat, regeneration, and reduced losses.

## Explainer

You've already studied the second law and know that no heat engine can be 100% efficient — some heat must be rejected to a cold reservoir. **Thermal efficiency** is the quantitative expression of this constraint: η = W_net / Q_in, the fraction of heat input that becomes net work. For a cycle operating between a hot source at T_hot and a cold sink at T_cold (measured in Kelvin), the Carnot efficiency η_Carnot = 1 − T_cold/T_hot sets the absolute upper bound. No cycle, no matter how cleverly designed, can exceed Carnot efficiency between those two temperature limits. A power plant drawing heat from steam at 600°C (873 K) and rejecting to cooling water at 30°C (303 K) has a Carnot limit of about 65% — real plants achieve 40-45%, the gap representing irreversibilities.

The Carnot cycle itself is a theoretical benchmark, not a practical design: it requires processes that are infinitely slow (to remain reversible) and involves heat exchange at exactly T_hot and T_cold. Real cycles accept irreversibilities in exchange for finite power output. The **Rankine cycle** (steam power plants) replaces Carnot's isothermal compression of a wet vapor with easy pump compression of liquid water — far more practical, though less efficient. The **Brayton cycle** (gas turbines) operates entirely in the gas phase with continuous compression and expansion. The **Otto cycle** (gasoline engines) approximates the rapid combustion and expansion of a piston engine. Each is analyzed by tracking W_net = Q_in − Q_out across all components and computing η = W_net / Q_in.

The key to improving efficiency is to raise the average temperature at which heat is added and lower the average temperature at which it is rejected — getting as close to operating between T_hot and T_cold as possible. **Superheat** (heating steam above saturation) raises the average temperature of heat addition. **Higher pressure ratios** in Brayton or Rankine cycles allow expansion to extract more work before heat rejection. **Reheat** (expanding partially, reheating, then expanding again) keeps the working fluid hotter longer. **Regeneration** (using exhaust heat to preheat the incoming fluid) reduces Q_in for the same W_net by internal heat exchange — it does not break the Carnot limit, but it reduces the required fuel by recycling energy that would otherwise be wasted.

When analyzing a cycle, the systematic approach is: label each state point (1, 2, 3, 4, ...) around the cycle, write the first law for each device (w = h_in − h_out for turbines and compressors, q = h_out − h_in for boilers and condensers), sum to find W_net and Q_in, then compute η. Each device's first law is just the steady-flow energy equation applied to one component. The cycle analysis knits those device-level balances into a system-level efficiency. This framework carries directly into Rankine, Brayton, and Otto analysis, where you'll apply these same steps to specific working fluids and real operating conditions.
