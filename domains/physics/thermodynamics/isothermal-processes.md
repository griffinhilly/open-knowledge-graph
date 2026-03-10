---
id: isothermal-processes
title: Isothermal Processes
domain: physics
course: thermodynamics
prerequisites:
- id: thermodynamic-processes
  type: hard
- id: ideal-gas-law
  type: hard
- id: work-as-integral
  type: soft
builds-toward:
- carnot-cycle
tags:
- isothermal
- constant-temperature
- Boyles-law
- work
- heat
stage: formal-systems
status: draft
---

# Isothermal Processes

## Core Idea
An isothermal process occurs at constant temperature. For an ideal gas, ΔU = 0 in any isothermal process (since U depends only on T), so by the first law, Q = W. The work done by the gas in expanding isothermally from V₁ to V₂ is W = nRT ln(V₂/V₁). On a PV diagram, an isotherm follows the hyperbola PV = constant. Isothermal processes require slow, quasi-static changes with continuous heat exchange to maintain constant temperature.

## How It's Best Learned
Derive the isothermal work integral from W = ∫P dV with P = nRT/V. Evaluate for specific numbers (e.g., 1 mol of gas at 300 K doubling its volume). Compare to the work that would be done in a free expansion — which is zero and is not quasi-static.

## Common Misconceptions
- Isothermal does not mean no heat exchange — isothermal processes require continuous heat exchange to maintain constant temperature.
- Real processes are not truly isothermal unless done infinitely slowly with a perfect heat reservoir.
