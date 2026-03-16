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
stage: advanced
status: draft
---

# Brayton Cycle and Gas Turbine Engines

## Core Idea
The Brayton cycle (compressor, combustor, turbine, exhaust) uses compressed air at high pressure for efficient combustion. Ideal efficiency η = 1 - 1/r_p^((γ-1)/γ) depends directly on pressure ratio r_p. Modern gas turbines operate at 35-40% simple-cycle efficiency; combined with steam recovery, integrated gasification combined cycle (IGCC) plants exceed 50% overall efficiency.

## Explainer

The Brayton cycle is the thermodynamic description of the jet engine and the land-based gas turbine power plant. Unlike the Rankine cycle (your prior thermodynamics context), which works with a condensing-vaporizing working fluid, the Brayton cycle uses gas — typically air — throughout. The four processes are isentropic compression in the compressor, constant-pressure heat addition in the combustor, isentropic expansion through the turbine, and constant-pressure heat rejection to the atmosphere (or equivalently, exhaust and intake of fresh air). The turbine and compressor are mechanically linked on the same shaft; the turbine must produce enough work to drive the compressor, and the net output is the surplus.

The ideal efficiency formula η = 1 − 1/r_p^((γ−1)/γ) looks abstract but has a clear physical story. Here r_p is the **pressure ratio** (outlet pressure divided by inlet pressure in the compressor), and γ is the specific heat ratio of the working gas (about 1.4 for air). Higher pressure ratio means the air enters combustion at a higher temperature and leaves the turbine at a lower temperature — you extract more work from the same fuel. The formula is structurally analogous to the Carnot efficiency 1 − T_cold/T_hot: both capture how much of the energy input you fail to convert to work. For the Brayton cycle, higher r_p shrinks the "cold reservoir" effectively by expanding the gas further. Modern gas turbines use pressure ratios of 20–40, achieving isentropic compression and expansion temperatures that bound the efficiency.

In practice, real Brayton cycles fall short of ideal for two reasons. First, compressors and turbines are not perfectly isentropic — **isentropic efficiency** (typically 85–90%) accounts for internal irreversibilities. Second, the **turbine inlet temperature** is limited by what turbine blade materials can survive (around 1400–1600°C for modern superalloys with blade cooling). Increasing pressure ratio without increasing turbine inlet temperature actually reduces efficiency at some point because the compressor outlet temperature rises toward the turbine inlet temperature, shrinking the temperature difference the combustor can add. The optimal pressure ratio for a given turbine inlet temperature is a design trade-off.

The path to higher overall efficiency is combining the Brayton cycle with a **bottoming Rankine cycle** — what power engineers call a combined cycle. The exhaust gas from the gas turbine, still at 500–600°C, passes through a heat recovery steam generator (HRSG) that produces steam for a steam turbine. The combined system achieves 55–60% overall efficiency, nearly double the simple-cycle Brayton. This is why modern natural-gas power plants are almost exclusively combined-cycle plants, and why the efficiency of gas turbine exhaust recovery is critical to the economics and environmental performance of gas-fired generation.
