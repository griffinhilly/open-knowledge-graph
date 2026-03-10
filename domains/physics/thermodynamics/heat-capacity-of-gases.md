---
id: heat-capacity-of-gases
title: Heat Capacities of Gases (Cv and Cp)
domain: physics
course: thermodynamics
prerequisites:
- id: specific-heat-capacity
  type: hard
- id: equipartition-theorem
  type: hard
- id: isobaric-and-isochoric-processes
  type: hard
builds-toward:
- adiabatic-processes
tags:
- heat-capacity
- Cv
- Cp
- monatomic
- diatomic
- adiabatic-index
stage: formal-systems
status: draft
---

# Heat Capacities of Gases (Cv and Cp)

## Core Idea
Gases have two important molar heat capacities: Cv (at constant volume) and Cp (at constant pressure). Equipartition gives Cv = (f/2)R where f is the number of active degrees of freedom. For monatomic gases f = 3, so Cv = (3/2)R and Cp = (5/2)R. For diatomic gases at room temperature f = 5, giving Cv = (5/2)R and Cp = (7/2)R. The ratio γ = Cp/Cv = (f+2)/f appears in adiabatic relations and determines the speed of sound.

## How It's Best Learned
Tabulate Cv, Cp, and γ for monatomic, diatomic, and triatomic gases and verify against experimental values. Notice that experimental Cv for diatomic gases at very high temperatures exceeds the f = 5 prediction — vibrational modes are activating.

## Common Misconceptions
- Cp and Cv are properties of the gas, not the process — the process determines which one is relevant.
- Classical equipartition predicts heat capacities that fail for gases at low temperature due to quantum effects (freezing of vibrational modes).
