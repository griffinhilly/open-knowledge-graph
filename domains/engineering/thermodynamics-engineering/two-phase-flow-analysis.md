---
id: two-phase-flow-analysis
title: Two-Phase Flow and Quality Determination
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: two-phase-homogeneous-flow-equilibrium
  type: hard
- id: saturated-superheated-property-regions
  type: soft
builds-toward:
- vapor-compression-refrigeration-cycles
- rankine-power-generation-cycles
tags:
- two-phase
- quality
- dryness-fraction
- mixture
stage: advanced
status: draft
---

# Two-Phase Flow and Quality Determination

## Core Idea
In two-phase regions, quality x = m_g/(m_f + m_g) characterizes the mixture (mass fraction vapor). Properties are weighted averages: h = h_f + x*h_fg, s = s_f + x*s_fg. Quality ranges 0 (saturated liquid) to 1 (saturated vapor). Throttle valves produce x ≈ 0.3; turbine exits may have x > 0.85 (moisture damage concern for long-blade turbines).
