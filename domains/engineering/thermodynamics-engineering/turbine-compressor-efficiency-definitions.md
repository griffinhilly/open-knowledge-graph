---
id: turbine-compressor-efficiency-definitions
title: Isentropic Efficiency of Turbines and Compressors
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: isentropic-efficiency-devices
  type: hard
- id: steady-flow-energy-equation-engineering
  type: soft
builds-toward:
- power-cycle-thermal-efficiency
- rankine-power-generation-cycles
- brayton-gas-turbine-cycles
tags:
- isentropic-efficiency
- turbines
- compressors
- performance
stage: advanced
status: draft
---

# Isentropic Efficiency of Turbines and Compressors

## Core Idea
Isentropic efficiency compares actual to reversible work: η_T = W_actual/W_isentropic for turbines, η_C = W_isentropic/W_actual for compressors. Both are <100% due to friction, turbulence, and non-ideal flows. Typical values: turbines 85-90%, compressors 80-88%. Even 1% efficiency improvement in a large power plant saves significant fuel and operating costs annually.

## Explainer

You already know that isentropic processes are reversible and adiabatic — they represent the best-case scenario for work-producing or work-consuming devices. **Isentropic efficiency** uses this ideal as a yardstick: it compares what a real device achieves to what a perfect isentropic device would achieve between the same inlet and outlet pressures.

For a **turbine**, the ideal is to extract as much work as possible. The isentropic turbine produces work W_s by expanding from inlet to outlet pressure with no entropy generation. The real turbine, plagued by fluid friction, turbulence, tip leakage, and heat loss, produces less: W_actual < W_s. So turbine isentropic efficiency is η_T = W_actual / W_isentropic = (h_in − h_out,actual) / (h_in − h_out,s), where the denominator is the maximum possible enthalpy drop. If η_T = 0.87, the turbine delivers 87% of the work that a perfect expansion would yield; the other 13% is lost to internal irreversibilities that heat the fluid (raising its entropy and exit enthalpy above the isentropic exit state).

For a **compressor**, the logic flips because work is being consumed, not produced. The ideal isentropic compressor requires the minimum work W_s to achieve a given pressure rise. The real compressor requires more: W_actual > W_s. So compressor isentropic efficiency is η_C = W_isentropic / W_actual = (h_out,s − h_in) / (h_out,actual − h_in). If η_C = 0.83, the compressor consumes 1/0.83 ≈ 1.20 times the minimum necessary work — 20% extra energy wasted to friction and flow irreversibilities. The real compressor exit state is at higher temperature and enthalpy than the isentropic exit state, because the wasted work goes into heating the working fluid.

The asymmetry between the two definitions — numerator for turbines, denominator for compressors — ensures that both efficiencies are numbers between 0 and 1. It is easy to mix them up: always ask "which is larger, actual or ideal?" For turbines, actual work is smaller (bad), so divide actual by ideal. For compressors, actual work is larger (bad), so divide ideal by actual. A good mnemonic: efficiency is always (what you want) / (what you pay). For the turbine, you want work and pay nothing extra; for the compressor, you want pressure rise and pay in work.

These efficiencies are not just academic — they cascade through cycle analysis. In a Brayton gas turbine cycle, combining a turbine at η_T = 0.87 and a compressor at η_C = 0.83 can reduce the overall cycle efficiency from a Carnot-ideal 48% down to a real 30-35%. Improving each device by a few percentage points meaningfully shifts the system thermal efficiency. This is why turbomachinery aerodynamics — blade profiles, tip clearances, inlet conditions — is a major engineering discipline. Every percentage point of isentropic efficiency translates directly into fuel saved and emissions reduced.
