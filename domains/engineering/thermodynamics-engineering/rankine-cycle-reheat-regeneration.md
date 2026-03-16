---
id: rankine-cycle-reheat-regeneration
title: 'Rankine Cycle Improvements: Reheat and Regenerative Feedwater Heating'
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: rankine-cycle-thermodynamic-analysis
  type: hard
tags:
- rankine-cycle
- reheat
- regeneration
- power-plants
stage: advanced
status: draft
---

# Rankine Cycle Improvements: Reheat and Regenerative Feedwater Heating

## Core Idea
Reheat (reheating vapor mid-expansion) and regeneration (extracting intermediate steam to preheat boiler feedwater) both improve Rankine efficiency and are ubiquitous in modern power plants. These modifications reduce exergy destruction, lower cooling water requirements, and allow higher turbine outlet qualities (less moisture damage). Analysis of multi-stage reheated and regenerative cycles requires careful state tracking and appropriate component models.

## Explainer

The basic Rankine cycle you analyzed as a prerequisite has a fundamental efficiency limitation: heat addition in the boiler occurs over a range of temperatures (as compressed water is heated, vaporized, and superheated), but the condensation temperature is fixed by the cold reservoir. Carnot's theorem says efficiency improves when you raise the average temperature at which heat is added. Both reheat and regeneration are engineering strategies to do exactly that — raise the mean temperature of heat addition without violating material or safety constraints.

**Reheat** addresses a specific problem: as high-pressure steam expands through the turbine, its quality (fraction vapor) drops. If expansion continues too far, you enter the wet region where liquid droplets erode turbine blades. The fix is to extract the steam partway through expansion (at an intermediate pressure P_rh), send it back to the boiler where it is reheated to near the original turbine inlet temperature, and then expand it through a second (low-pressure) turbine stage. The work output from both turbine stages increases, and the turbine exit quality improves because you are now expanding from a higher temperature at the intermediate pressure. The thermodynamic analysis requires tracking two expansion states: state 1 → state 2 (high-pressure turbine, HP-T), reheating from state 2 → state 3, then expanding state 3 → state 4 (low-pressure turbine, LP-T). Net work = (h₁ − h₂) + (h₃ − h₄) and heat input = (h₁ − h_feed) + (h₃ − h₂).

**Regeneration** works on a different principle. In the basic Rankine cycle, feedwater entering the boiler is cold (near saturation temperature at condenser pressure — typically around 40–50°C). Heating this cold water through the subcooled liquid region in the boiler is thermodynamically wasteful because it occurs far from the boiler pressure saturation temperature. In a **regenerative Rankine cycle**, you bleed a fraction ṁ_bleed of steam from an intermediate turbine stage and mix it with the cold feedwater in an **open feedwater heater (OFWH)**. The bleed steam condenses, heating the feedwater to the saturation temperature at the bleed pressure. The remaining feedwater enters the boiler much hotter, so less heat needs to be added in the inefficient low-temperature region. The analysis requires a mass balance on the OFWH: ṁ_bleed × h_bleed + (1 − ṁ_bleed) × h_pump_out = 1 × h_sat_liquid_bleed, which determines the bleed fraction.

In practice, modern power plants combine multiple stages of reheat and regeneration — typically one or two reheat stages and five to eight feedwater heaters operating at different extraction pressures. The result is a cycle whose heat addition profile more closely approximates a constant high-temperature source, approaching (but never reaching) Carnot efficiency. State-tracking becomes the main analytical challenge: you must label every state point, apply energy and mass balances to each component, and correctly account for the varying mass flow rates through different sections of the turbine. The reward for this complexity is real: a modern coal plant with reheat and regeneration achieves thermal efficiencies of 38–45%, compared to roughly 25–30% for the ideal simple Rankine cycle at the same operating pressures.
