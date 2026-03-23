---
id: brayton-gas-turbine-cycles
title: Brayton Cycle and Gas Turbine Engines
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: brayton-cycle-gas-turbine
  type: hard
- id: power-cycle-thermal-efficiency
  type: soft
builds-toward:
- brayton-cycle-intercooling-reheating
- combined-gas-steam-cycles
tags:
- brayton
- gas-turbine
- compression
- combustion
stage: formal-systems
status: draft
---

# Brayton Cycle and Gas Turbine Engines

## Core Idea
The Brayton cycle (compressor, combustor, turbine, exhaust) uses compressed air at high pressure for efficient combustion. Ideal efficiency η = 1 - 1/r_p^((γ-1)/γ) depends directly on pressure ratio r_p. Modern gas turbines operate at 35-40% simple-cycle efficiency; combined with steam recovery, integrated gasification combined cycle (IGCC) plants exceed 50% overall efficiency.

## Questions

```yaml
- question: "A gas turbine currently operating at pressure ratio r_p = 20 is redesigned to r_p = 40, with turbine inlet temperature held constant by material limits. The engineer expects higher efficiency. Why might efficiency peak or decline instead?"
  type: multiple-choice
  options:
    - "Higher pressure ratios mechanically stress compressor blades, reducing isentropic efficiency"
    - "The compressor outlet temperature rises toward the fixed turbine inlet temperature, shrinking the temperature rise the combustor can add and reducing net useful work"
    - "Doubling the pressure ratio always halves the thermal efficiency according to the Brayton formula"
    - "The working fluid's specific heat ratio γ changes at high pressures, invalidating the efficiency formula"
  answer: 1
  explanation: "Higher pressure ratio increases the compressor outlet temperature. If turbine inlet temperature is fixed (by blade material limits), the combustor temperature rise ΔT = T_inlet − T_compressor_out shrinks. Less heat is added per unit of compressed air, and the cycle approaches a degenerate limit where the compressor and turbine cancel each other. The efficiency formula η = 1 − 1/r_p^((γ−1)/γ) predicts monotonic improvement only for the ideal cycle with unlimited turbine inlet temperature. In real design, the optimal pressure ratio for maximum efficiency is determined by the turbine inlet temperature limit."

- question: "In the ideal Brayton cycle, the efficiency formula η = 1 − 1/r_p^((γ-1)/γ) is structurally similar to Carnot efficiency 1 − T_cold/T_hot. What does a higher pressure ratio physically accomplish that explains its effect on efficiency?"
  type: multiple-choice
  options:
    - "Higher r_p increases combustor temperature, directly raising T_hot"
    - "Higher r_p increases mass flow through the turbine, producing more shaft work"
    - "Higher r_p expands the exhaust gas further, so turbine exit temperature falls — effectively lowering the 'cold reservoir' temperature and reducing waste heat"
    - "Higher r_p decreases the compressor work, leaving more net output from the turbine"
  answer: 2
  explanation: "The Brayton efficiency gain from higher pressure ratio comes from more complete expansion in the turbine. With higher r_p, the turbine expands the gas over a larger pressure range, extracting more work and exhausting at a lower temperature. This is analogous to reducing T_cold in the Carnot formula — less heat is rejected to the atmosphere. The key physical insight is that it is the turbine exit temperature, not the combustor temperature, that determines how much energy is wasted."

- question: "In a combined-cycle power plant, the hot gas turbine exhaust (at ~550°C) is used to generate steam for a Rankine bottoming cycle, raising overall plant efficiency well above what the simple Brayton cycle alone achieves."
  type: true-false
  answer: true
  explanation: "A simple-cycle gas turbine exhausts at 500–600°C — still very hot, representing a large fraction of unrecovered thermal energy. A heat recovery steam generator (HRSG) captures this waste heat to produce steam, driving a second (Rankine) turbine. The combined system achieves 55–60% thermal efficiency versus 35–40% for the gas turbine alone. The efficiency gain is not from burning more fuel but from extracting useful work from heat that would otherwise be vented to the atmosphere. This is why virtually all modern natural-gas power plants are combined-cycle."

- question: "In real gas turbine operation, increasing the compressor pressure ratio always improves thermal efficiency regardless of the turbine inlet temperature constraint."
  type: true-false
  answer: false
  explanation: "Real turbine blades have material temperature limits (~1400–1600°C for modern superalloys with cooling). As pressure ratio increases, compressor outlet temperature rises. If turbine inlet temperature is fixed, the temperature difference across the combustor shrinks, reducing the heat addition per unit mass flow. At some pressure ratio, this effect dominates, and efficiency peaks then declines. Even for the ideal Brayton cycle, real engineering optimization always involves the turbine inlet temperature as a co-parameter — the optimal pressure ratio increases with turbine inlet temperature, making materials research and blade cooling as important as compressor design."

- question: "Explain why combining a gas turbine with a steam turbine (combined cycle) approaches 60% efficiency while the gas turbine alone achieves only 35–40%."
  type: short-answer
  answer: "The gas turbine exhausts at 500–600°C — still containing substantial thermal energy that a simple-cycle plant vents to the atmosphere. In a combined-cycle plant, this exhaust passes through a heat recovery steam generator that produces steam for a Rankine bottoming cycle. The Rankine cycle converts a significant fraction of that waste heat into additional shaft work. Because no additional fuel is burned, the extra electricity comes 'free' from heat that was already in the system. The combined first-law efficiency reflects the sum of both cycles' work outputs divided by the original fuel input."
  explanation: "The thermodynamic principle is that the combined cycle attacks waste heat from both ends: the Brayton cycle does not exhaust until temperatures drop to ~550°C, and the Rankine cycle starts with that 550°C steam. Each Joule that would have been rejected by the simple Brayton cycle is now a potential input to the bottoming cycle. The practical limit is set by Rankine cycle efficiency at its operating temperatures (~30–35%) and by HRSG heat transfer effectiveness. The result — 55–60% — is close to the theoretical maximum for a two-stage cascade operating between combustion temperature and ambient."
```

## Explainer

The Brayton cycle is the thermodynamic description of the jet engine and the land-based gas turbine power plant. Unlike the Rankine cycle (your prior thermodynamics context), which works with a condensing-vaporizing working fluid, the Brayton cycle uses gas — typically air — throughout. The four processes are isentropic compression in the compressor, constant-pressure heat addition in the combustor, isentropic expansion through the turbine, and constant-pressure heat rejection to the atmosphere (or equivalently, exhaust and intake of fresh air). The turbine and compressor are mechanically linked on the same shaft; the turbine must produce enough work to drive the compressor, and the net output is the surplus.

The ideal efficiency formula η = 1 − 1/r_p^((γ−1)/γ) looks abstract but has a clear physical story. Here r_p is the **pressure ratio** (outlet pressure divided by inlet pressure in the compressor), and γ is the specific heat ratio of the working gas (about 1.4 for air). Higher pressure ratio means the air enters combustion at a higher temperature and leaves the turbine at a lower temperature — you extract more work from the same fuel. The formula is structurally analogous to the Carnot efficiency 1 − T_cold/T_hot: both capture how much of the energy input you fail to convert to work. For the Brayton cycle, higher r_p shrinks the "cold reservoir" effectively by expanding the gas further. Modern gas turbines use pressure ratios of 20–40, achieving isentropic compression and expansion temperatures that bound the efficiency.

In practice, real Brayton cycles fall short of ideal for two reasons. First, compressors and turbines are not perfectly isentropic — **isentropic efficiency** (typically 85–90%) accounts for internal irreversibilities. Second, the **turbine inlet temperature** is limited by what turbine blade materials can survive (around 1400–1600°C for modern superalloys with blade cooling). Increasing pressure ratio without increasing turbine inlet temperature actually reduces efficiency at some point because the compressor outlet temperature rises toward the turbine inlet temperature, shrinking the temperature difference the combustor can add. The optimal pressure ratio for a given turbine inlet temperature is a design trade-off.

The path to higher overall efficiency is combining the Brayton cycle with a **bottoming Rankine cycle** — what power engineers call a combined cycle. The exhaust gas from the gas turbine, still at 500–600°C, passes through a heat recovery steam generator (HRSG) that produces steam for a steam turbine. The combined system achieves 55–60% overall efficiency, nearly double the simple-cycle Brayton. This is why modern natural-gas power plants are almost exclusively combined-cycle plants, and why the efficiency of gas turbine exhaust recovery is critical to the economics and environmental performance of gas-fired generation.
