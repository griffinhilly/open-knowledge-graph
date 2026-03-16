---
id: compressor-staging-multistage
title: Multistage Compressor Design and Intercooling
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: polytropic-efficiency-real-machinery
  type: hard
- id: gas-mixtures-partial-pressures-daltons-law
  type: soft
builds-toward:
- brayton-cycle-intercooling-reheating
tags:
- compressor
- multistage
- intercooling
- pressure-ratio
- power-input
stage: advanced
status: draft
---

# Multistage Compressor Design and Intercooling

## Core Idea
Multistage compression with intercooling reduces the total compressor work by maintaining lower inlet temperatures to downstream stages. Optimal stage pressure ratios are equal when polytropic efficiency is constant. Intercooling between stages approaches isothermal compression in the limit, minimizing compression work while meeting high pressure ratios economically.

## Explainer

From your study of polytropic compression, you know that real compressor work lies between two idealized extremes: **isothermal compression** (constant temperature, minimum work, impossible to achieve exactly) and **isentropic compression** (adiabatic and reversible, maximum work for a given pressure ratio). A single-stage compressor compresses gas from inlet to final pressure in one pass. As the gas is compressed, its temperature rises substantially — and that hot, dense gas requires more work to compress further than cool gas at the same pressure would. The single-stage machine is fighting against its own heat output.

The central insight of multistage compression with **intercooling** is that you can partially undo this penalty. After the first stage raises gas pressure to an intermediate level, an intercooler (a heat exchanger) removes the heat of compression and returns the gas approximately to the original inlet temperature T₁. The second stage then compresses this cooler, lower-density gas — doing noticeably less work than if it had received the hot discharge from stage one. With more stages and intercoolers, the overall compression path becomes a staircase of isentropic rises and isobaric (constant pressure) coolings, approaching the isothermal limit as the number of stages increases.

The equal-pressure-ratio result follows from an optimization. For two stages with overall pressure ratio r_total = P_final/P_inlet, you choose intermediate pressure P_int to minimize total shaft work. Setting up the work expressions for each polytropic stage and differentiating with respect to P_int, the minimum occurs when P_int/P_inlet = P_final/P_int, meaning each stage handles the square root of the total pressure ratio. For n stages: r_stage = r_total^(1/n). This result assumes equal polytropic efficiency and that each intercooler returns gas to the same inlet temperature — both reasonable approximations for preliminary design. When efficiencies differ or intercooling is incomplete, the optimum shifts, but equal pressure ratios remain a practical starting point.

The engineering benefit compounds with more stages, but with diminishing returns. Two stages dramatically reduce work compared to one; three stages improve further but by less; six stages get very close to isothermal. Industrial gas compressors in air separation plants, natural gas processing, and chemical synthesis commonly use three to six stages. The tradeoffs are hardware cost (each stage and intercooler adds equipment), pressure drop in the intercoolers (which reduces the effective pressure ratio and hurts efficiency), and increased system complexity. The Brayton cycle with intercooling extends this principle to gas turbines, where intercooling reduces compressor work share of the cycle, improving overall thermal efficiency when combined with regeneration.
