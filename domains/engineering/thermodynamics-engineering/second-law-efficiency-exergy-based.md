---
id: second-law-efficiency-exergy-based
title: Second Law Efficiency and Exergy-Based Metrics
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: exergy-balance-control-volume
  type: hard
- id: chemical-exergy-fuel-combustion
  type: soft
tags:
- second-law-efficiency
- exergy-efficiency
- raquette-inequality
- lost-work
stage: advanced
status: draft
---

# Second Law Efficiency and Exergy-Based Metrics

## Core Idea
Second law efficiency η_II = useful exergy output / exergy input quantifies how closely a device approaches reversibility. Unlike first law efficiency, it accounts for availability destruction. For power cycles: η_II = W_net / (Ex_fuel input). Values typically 40-60% for thermal power plants; improvements require reducing heat transfer irreversibility and incomplete expansion/compression.

## Explainer

From your exergy balance studies, you know that every real process destroys exergy in proportion to entropy generated: Ẋ_destroyed = T₀ · Ṡ_gen. Exergy destruction represents permanently lost work potential — once exergy is destroyed, no engineering improvement can recover it. First-law efficiency measures energy retention; **second-law efficiency** measures how much of the available work potential you actually convert to useful output.

The distinction matters because energy is always conserved (first law), so first-law efficiency can appear high even when a process is deeply wasteful. Consider a gas furnace heating a building: 95% of the chemical energy in the fuel reaches the building as heat. First-law efficiency = 95%. Yet the fuel burns at ~2000°C to heat a room to 22°C — the maximum work extractable from this temperature difference (Carnot efficiency between 2000°C and 22°C) is enormous, and nearly all of it is thrown away by transferring heat across the massive temperature gradient. The second-law efficiency — useful exergy delivered divided by exergy of fuel consumed — might be only 4 or 5%, revealing the profound thermodynamic waste invisible to first-law analysis.

**Second-law efficiency** is defined as η_II = (useful exergy output)/(exergy input), normalized so that a reversible process achieves η_II = 1. The definition of "useful exergy output" depends on the device purpose. For a turbine: W_actual / ΔEx_stream (how much work you extracted versus maximum possible). For a heat pump: the exergy delivered to the heated space (Q_H × (1 − T₀/T_H)) divided by the work input W. For a combustion power plant: W_net / Ex_fuel, where Ex_fuel is the chemical exergy of the fuel (approximately equal to its lower heating value for most fuels). Typical power plant values of 40–60% reflect unavoidable irreversibilities: combustion itself, heat transfer across temperature differences, friction, and incomplete expansion.

To improve second-law efficiency, you must reduce the sources of exergy destruction: heat transfer across large ΔT (match source and process temperatures — this is why combined-cycle plants route hot gas turbine exhaust into a heat recovery steam generator rather than venting it), mixing of streams at different compositions, fluid friction, and incomplete reactions. The **combined-cycle gas turbine** is the most visible application: the Brayton cycle's exhaust at ~600°C has substantial remaining exergy that a Rankine cycle then converts to additional work. The result is first-law efficiency ~60% and second-law efficiency ~55–58%, nearly double the simple Rankine cycle. Exergy analysis identifies *where* efficiency is lost; second-law efficiency quantifies *how much* — together, they are the diagnostic tools for rational energy system design.
