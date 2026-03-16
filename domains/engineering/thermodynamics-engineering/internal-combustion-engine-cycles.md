---
id: internal-combustion-engine-cycles
title: 'Otto and Diesel Cycles: Internal Combustion Engines'
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: otto-cycle-spark-ignition-engine
  type: hard
- id: diesel-cycle-compression-ignition
  type: hard
builds-toward:
- combustion-stoichiometry-energy-release
- adiabatic-flame-temperature-calculation
tags:
- otto-cycle
- diesel-cycle
- internal-combustion
- efficiency
stage: advanced
status: draft
---

# Otto and Diesel Cycles: Internal Combustion Engines

## Core Idea
The Otto cycle (spark-ignition, constant-volume heat addition) achieves efficiency η = 1 - 1/r_c^(γ-1), where r_c is compression ratio. The Diesel cycle (compression-ignition, constant-pressure heat addition) uses higher compression and air-fuel stratification. Diesel engines typically achieve 40-50% brake thermal efficiency; spark-ignition engines 25-35%, with modern direct injection improving both.

## Explainer

Having studied the Otto and Diesel cycles individually, the key task here is deepening the comparison and connecting ideal cycle analysis to real engine performance. The essential distinction is **how heat is added**: in the Otto cycle, a nearly homogeneous air-fuel mixture ignites simultaneously at top dead center, adding heat at approximately constant volume in a single rapid event. In the Diesel cycle, fuel injects progressively after compression and burns at approximately constant pressure while the piston descends. This difference in heat addition mode drives all the performance differences between the two engine families.

The **Otto cycle efficiency** η = 1 − 1/r^(γ−1) depends only on the compression ratio r and the specific heat ratio γ ≈ 1.4 for air. Efficiency rises monotonically with r — so why don't gasoline engines use r = 20:1? Because at high compression ratios, the air-fuel mixture reaches its autoignition temperature during compression, before the spark fires. This uncontrolled ignition — **knock** — causes pressure spikes that damage pistons and bearings. Gasoline engines are therefore limited to compression ratios of roughly 9:1 to 12:1, directly limiting their efficiency. High-octane fuel resists autoignition, allowing slightly higher compression ratios, which is why premium fuel exists.

Diesel engines escape this constraint because they compress **pure air** during the compression stroke — there is no fuel present to autoignite. Fuel injects at top dead center into the hot, high-pressure air, and autoignition of the mixture is the goal, not the hazard. This allows compression ratios of 16:1 to 22:1. The Diesel cycle efficiency formula, η = 1 − (1/r^(γ−1)) · [(r_c^γ − 1)/(γ(r_c − 1))], includes a **cutoff ratio** r_c (the ratio of volume when fuel injection ends to volume at TDC) that penalizes the constant-pressure heat addition. At the same compression ratio, the Diesel efficiency is always lower than the Otto efficiency — the constant-pressure heat addition is thermodynamically less favorable than constant-volume. But because diesels operate at much higher compression ratios than gasoline engines can achieve, real diesel engines attain higher actual efficiency. This reconciliation is critical: the formula is "worse" at equal r, but real engines access higher r.

Real engines deviate from ideal cycles through friction, heat transfer to cylinder walls, incomplete combustion, valve flow restrictions, and the finite duration of combustion. **Brake thermal efficiency** — useful crankshaft work divided by fuel energy input — captures all these losses and is the practically relevant metric. Modern turbocharged direct-injection diesels achieve 44–48% brake thermal efficiency in passenger vehicles and exceed 50% in large marine two-stroke diesels. Modern spark-ignition engines with turbocharging, direct injection, and variable valve timing now reach 40–42% peak efficiency under optimal operating conditions. The efficiency gap has narrowed considerably through engineering, but the fundamental thermodynamic advantage of high compression ratio for the Diesel cycle remains.
