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

## Explainer

From your study of saturated and superheated property regions, you know that inside the two-phase dome on a T-s or P-v diagram, liquid and vapor coexist at the same temperature and pressure. A pot of boiling water at atmospheric pressure is at exactly 100°C whether it's mostly liquid (just starting to boil) or mostly steam (nearly all evaporated). The intensive properties — temperature and pressure — are fixed by the saturation condition, but the *amount* of vapor relative to liquid can be anything from 0% to 100%. **Quality** x is the number that pins down exactly where in the two-phase region a given state lies.

Quality is defined as x = m_vapor / m_total — the fraction of the total mass that has become vapor. At x = 0, you have saturated liquid (the left edge of the dome). At x = 1, you have saturated vapor (the right edge, or "dry saturated steam"). Any state inside the dome has a quality between 0 and 1. The practical power of quality is that it turns property lookups into simple linear interpolations: any specific property y at quality x equals y_f + x·y_fg, where y_f is the saturated liquid value and y_fg = y_g − y_f is the difference between saturated vapor and saturated liquid. This works for enthalpy, entropy, specific volume, and internal energy — all of them follow the same linear mixing rule.

Consider what happens in a throttle valve in a refrigeration cycle. The refrigerant enters as a compressed or saturated liquid at high pressure. The throttle is an adiabatic, isenthalpic device (no work, no heat): enthalpy in = enthalpy out. But at the low downstream pressure, the saturation temperature is much lower than the inlet temperature, so the fluid must cool to reach saturation — and it does this by partially vaporizing. You can compute the exit quality directly: x_exit = (h_in − h_f,exit) / h_fg,exit. Typical values are around 0.2–0.4, meaning 20–40% of the mass has flashed to vapor. This vapor fraction carries no additional refrigerating capacity — it arrived cold but already vaporized — so minimizing x at the throttle inlet (subcooling the liquid before throttling) improves cycle efficiency.

At the turbine exit of a steam power cycle, quality takes on a different significance. Steam turbines work by expanding vapor through rotating blades. If quality drops below about 0.85 (more than 15% moisture), liquid droplets impact the blades at high relative velocity, causing **erosion** — physically gouging the blade material away. Long last-stage blades in large steam turbines are especially vulnerable because blade tip speeds are highest there. Engineers either design the cycle so the exit state remains above x ≈ 0.88, use **moisture separators** between turbine stages, or employ **superheated steam** at inlet so the expansion path through the T-s diagram stays in the superheated or high-quality region throughout. Quality analysis — which your prerequisite on two-phase equilibrium established — is the quantitative tool that makes all of this tractable.

