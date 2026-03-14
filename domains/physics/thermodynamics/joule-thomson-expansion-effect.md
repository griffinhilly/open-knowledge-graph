---
id: joule-thomson-expansion-effect
title: Joule-Thomson Expansion and the Joule-Thomson Effect
domain: physics
course: thermodynamics
prerequisites:
- id: real-gas-deviations
  type: hard
- id: heat-and-internal-energy
  type: soft
builds-toward:
- throttling-process-analysis
- rankine-cycle-steam-power
tags:
- real-gases
- refrigeration
- expansion
stage: formal-systems
status: draft
---

# Joule-Thomson Expansion and the Joule-Thomson Effect

## Core Idea
During isenthalpic expansion of a real gas, the temperature changes according to the Joule-Thomson coefficient μ_JT = (∂T/∂P)_H = (V/C_P)(αT - 1), where α is the thermal expansion coefficient. For most gases below the inversion temperature, μ_JT > 0, so pressure decrease causes temperature decrease (cooling); this effect is the basis for many liquefaction processes. Understanding the Joule-Thomson effect requires knowledge of real gas behavior and the relationship between measurable properties.

## How It's Best Learned
Calculate μ_JT for gases using the van der Waals equation. Identify the inversion temperature where μ_JT changes sign. Compare with experimental data.

## Common Misconceptions
- Thinking the Joule-Thomson effect is the same for all gases.
- Confusing it with adiabatic expansion (which changes enthalpy).
- Assuming ideal gases have zero Joule-Thomson coefficient (they do exactly, real gases don't).
