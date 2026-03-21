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

## Questions

```yaml
- question: "A gas furnace delivers 95% of the fuel's chemical energy to a building as heat (η_I = 95%). What can you conclude about its second-law efficiency?"
  type: multiple-choice
  options:
    - "η_II ≈ 95% — first and second law efficiencies are nearly equal for heating applications"
    - "η_II is approximately 100% minus heat losses, so also about 95%"
    - "η_II is far below η_I — burning fuel at ~2000°C to heat a room at 22°C wastes most of the available work potential"
    - "η_II cannot be determined without knowing the Carnot efficiency of the boiler"
  answer: 2
  explanation: "First-law efficiency measures energy retention; second-law efficiency measures how much of the available work potential (exergy) is actually used for the purpose. Fuel combustion at ~2000°C has enormous exergy. Delivering that energy as low-grade heat at 22°C destroys nearly all of it by transferring heat across a massive temperature gradient. The second-law efficiency — exergy of heat delivered divided by chemical exergy of fuel — might be only 4–5%. The furnace 'wastes' 95% of the fuel's quality from a second-law perspective, even though it 'wastes' only 5% from a first-law perspective. This is the defining contrast between the two metrics."

- question: "A combined-cycle power plant uses hot turbine exhaust to generate additional steam for a Rankine cycle. This primarily improves second-law efficiency by reducing heat transfer across large temperature differences."
  type: true-false
  answer: true
  explanation: "In a simple gas turbine, exhaust at ~600°C is vented to the atmosphere — that exergy is lost. The combined cycle routes this exhaust through a heat recovery steam generator (HRSG), where the steam is raised at a temperature close to the exhaust temperature. This reduces the ΔT across which heat transfer occurs, thereby reducing exergy destruction. By cascading two cycles to 'step down' the temperature in stages, the combined cycle extracts work at each stage before the temperature drops too far, achieving first-law efficiency ~60% and second-law efficiency ~55–58% — far above a simple cycle."

- question: "A process retains 100% of input energy (no heat loss to surroundings), so it must have a second-law efficiency of 100%."
  type: true-false
  answer: false
  explanation: "Energy conservation (η_I = 100%) is compatible with significant exergy destruction. For example, mixing two fluids at different temperatures conserves energy perfectly — the total enthalpy is unchanged — but the mixing is irreversible and destroys exergy proportional to the entropy generated. Similarly, heat transfer across any finite temperature difference conserves energy but destroys exergy. Second-law efficiency measures performance relative to a reversible ideal, not relative to energy retention. A lossless but irreversible process can have η_II much less than 1."

- question: "Second-law efficiency of 1 (100%) would require a fully reversible process."
  type: true-false
  answer: true
  explanation: "η_II = (useful exergy output)/(exergy input) = 1 when all input exergy is converted to useful output — no exergy is destroyed. Exergy destruction equals T₀ × Ṡ_gen by Gouy-Stodola theorem, so zero exergy destruction requires zero entropy generation. Zero entropy generation is the definition of a reversible process. Real processes always destroy some exergy through heat transfer across finite ΔT, friction, mixing, and incomplete reactions, so η_II < 1 in practice. The reversible limit provides the thermodynamic ceiling against which actual performance is judged."

- question: "Why does burning fuel at high temperature to heat a low-temperature room represent severe thermodynamic waste, even if no heat escapes to the environment?"
  type: short-answer
  answer: "The waste is not in the energy itself but in its quality — its capacity to do work. Chemical fuels carry high-grade exergy: their energy is available at very high temperature (~2000°C for combustion) and could in principle drive a heat engine operating between that temperature and the environment, extracting large amounts of work. Delivering this energy directly as room-temperature heat transfers the quantity of energy but destroys its quality. The Carnot efficiency between 2000°C and 22°C is about 87%, meaning 87% of the fuel's exergy could theoretically be converted to work before the remaining heat is delivered at room temperature. By skipping the work extraction entirely, the furnace destroys that 87% permanently — it is exergy destruction caused by heat transfer across an enormous temperature gradient."
  explanation: "This is why heat pumps are thermodynamically superior to resistance heaters even though both deliver heat to a room. A heat pump uses work (high-grade energy) to move heat from cold to warm, delivering 3–5 units of heat per unit of electrical work (COP = 3–5). An electric resistance heater converts work to heat at 1:1. The heat pump uses exergy efficiently; the resistance heater throws it away. The furnace is even worse: it destroys chemical exergy worth far more than any electrical work to produce low-grade heat."
```

## Explainer

From your exergy balance studies, you know that every real process destroys exergy in proportion to entropy generated: Ẋ_destroyed = T₀ · Ṡ_gen. Exergy destruction represents permanently lost work potential — once exergy is destroyed, no engineering improvement can recover it. First-law efficiency measures energy retention; **second-law efficiency** measures how much of the available work potential you actually convert to useful output.

The distinction matters because energy is always conserved (first law), so first-law efficiency can appear high even when a process is deeply wasteful. Consider a gas furnace heating a building: 95% of the chemical energy in the fuel reaches the building as heat. First-law efficiency = 95%. Yet the fuel burns at ~2000°C to heat a room to 22°C — the maximum work extractable from this temperature difference (Carnot efficiency between 2000°C and 22°C) is enormous, and nearly all of it is thrown away by transferring heat across the massive temperature gradient. The second-law efficiency — useful exergy delivered divided by exergy of fuel consumed — might be only 4 or 5%, revealing the profound thermodynamic waste invisible to first-law analysis.

**Second-law efficiency** is defined as η_II = (useful exergy output)/(exergy input), normalized so that a reversible process achieves η_II = 1. The definition of "useful exergy output" depends on the device purpose. For a turbine: W_actual / ΔEx_stream (how much work you extracted versus maximum possible). For a heat pump: the exergy delivered to the heated space (Q_H × (1 − T₀/T_H)) divided by the work input W. For a combustion power plant: W_net / Ex_fuel, where Ex_fuel is the chemical exergy of the fuel (approximately equal to its lower heating value for most fuels). Typical power plant values of 40–60% reflect unavoidable irreversibilities: combustion itself, heat transfer across temperature differences, friction, and incomplete expansion.

To improve second-law efficiency, you must reduce the sources of exergy destruction: heat transfer across large ΔT (match source and process temperatures — this is why combined-cycle plants route hot gas turbine exhaust into a heat recovery steam generator rather than venting it), mixing of streams at different compositions, fluid friction, and incomplete reactions. The **combined-cycle gas turbine** is the most visible application: the Brayton cycle's exhaust at ~600°C has substantial remaining exergy that a Rankine cycle then converts to additional work. The result is first-law efficiency ~60% and second-law efficiency ~55–58%, nearly double the simple Rankine cycle. Exergy analysis identifies *where* efficiency is lost; second-law efficiency quantifies *how much* — together, they are the diagnostic tools for rational energy system design.
