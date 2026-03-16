---
id: isentropic-efficiency-devices
title: Isentropic Efficiency of Turbines, Compressors, and Pumps
domain: engineering
course: thermodynamics-engineering
prerequisites:
- id: isentropic-process-reversible
  type: hard
tags:
- efficiency
- isentropic
- devices
stage: advanced
status: draft
---

# Isentropic Efficiency of Turbines, Compressors, and Pumps

## Core Idea
Isentropic efficiency compares actual device performance to an ideal isentropic process, quantifying the fraction of available energy extracted (turbines) or the additional work required (compressors). For a turbine, η_s = (actual work)/(isentropic work); for a pump or compressor, η_s = (isentropic work)/(actual work). Typical values range 0.75–0.95 depending on machine design and operating conditions.

## How It's Best Learned
Calculate isentropic work (assuming S = const) using property tables, then use actual outlet conditions to find actual work and efficiency. Recognize that turbine efficiency is always less than 100% (actual work less than isentropic), while compressor efficiency is also less than 100% (actual work greater than isentropic). Use typical efficiency values (0.85 for turbines, 0.80 for compressors) to estimate real performance when exact data is unavailable.

## Common Misconceptions
- Isentropic efficiency is the same for turbines and compressors; the definitions have numerator and denominator reversed.
- Improving isentropic efficiency requires only smoother passages; it also depends on Reynolds number, stage design, and multi-stage effects.
- An isentropic efficiency of 0.90 means 90% of energy is converted to useful work; it means the device extracts 90% of the maximum possible work in an ideal process.

## Explainer

You already know that an isentropic process is reversible and adiabatic — entropy stays constant. In that ideal world, a turbine would extract the maximum possible work from a steam or gas stream, and a compressor would require the minimum possible work to raise pressure. Real devices cannot achieve this because of friction, flow separation, heat transfer, and turbulence. **Isentropic efficiency** is the single number that quantifies how far a real device falls short of the isentropic ideal.

For a **turbine**, the isentropic process represents the most work you could possibly extract from a fluid entering at state 1 and leaving at the exit pressure. The ideal exit state (state 2s, with "s" for isentropic) is found by drawing a vertical line on an h-s diagram down to the exit pressure — entropy constant, pressure drops. The actual exit state (state 2a) lies to the right of this ideal point on the h-s diagram, at higher entropy and higher enthalpy, because irreversibilities dissipate energy as heat within the fluid rather than converting it to shaft work. The turbine isentropic efficiency is η_t = w_actual / w_isentropic = (h1 - h2a) / (h1 - h2s). Since h2a > h2s, the numerator is smaller than the denominator, giving η_t < 1.

For a **compressor or pump**, the situation is exactly reversed. The isentropic ideal minimizes the work you must input to raise the fluid's pressure. Real irreversibilities make you do more work than this minimum. The actual exit enthalpy h2a is higher than the isentropic ideal h2s (more energy stored in the fluid, mostly as heat from friction). The compressor isentropic efficiency is η_c = w_isentropic / w_actual = (h2s - h1) / (h2a - h1). Both numerator and denominator represent work inputs, but isentropic work is always less than actual, so again η_c < 1. The important asymmetry: the definition is inverted relative to turbines — you divide by the larger quantity in both cases to keep efficiency below 1.

To solve a practical problem, you work in three steps. First, locate the inlet state on steam tables or using the ideal gas relations and read off h1 and s1. Second, set s2s = s1 and find h2s at the exit pressure — this gives the isentropic work. Third, apply the efficiency definition to find h2a, then use h2a to find the actual exit state and any other desired properties (temperature, quality, entropy). The h-s (Mollier) diagram is your visualization tool: turbines move down-right (expanding, entropy increasing), compressors move up-right (compressing, entropy increasing).

The efficiency value matters enormously in cycle analysis. In a Rankine cycle, reducing turbine efficiency from 0.90 to 0.80 might drop overall cycle efficiency by 3-5 percentage points — a significant penalty. In a Brayton cycle, both turbine and compressor efficiency appear, and their effects compound: a slightly less efficient compressor forces the turbine to work harder just to recover the compressor penalty, before producing any net work. This sensitivity is why turbomachinery design invests heavily in blade geometry, tip clearance, and stage matching to push isentropic efficiencies toward 0.90 and above.
