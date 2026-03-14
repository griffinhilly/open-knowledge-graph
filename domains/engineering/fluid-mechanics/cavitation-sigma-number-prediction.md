---
id: cavitation-sigma-number-prediction
title: Cavitation Number and Cavitation Prediction
domain: engineering
course: fluid-mechanics
prerequisites:
- id: cavitation-inception-vapor-formation
  type: hard
- id: bernoullis-equation
  type: soft
- id: stagnation-pressure-and-total-head
  type: soft
tags:
- cavitation
- sigma-number
- npsh
stage: formal-systems
status: draft
---

# Cavitation Number and Cavitation Prediction

## Core Idea
The cavitation number σ = (P - P_vapor)/(0.5ρV²) quantifies the margin between local pressure and vapor pressure relative to dynamic pressure. Cavitation inception occurs when σ drops below a critical value σ_i, which depends on geometry and Reynolds number. Predicting and avoiding cavitation requires monitoring inlet conditions (absolute pressure, temperature), flow velocity, and system design. The NPSH (net positive suction head) requirement of a pump must be less than NPSH available to prevent cavitation damage.

## How It's Best Learned
Set up a cavitation tunnel or pump system where inlet pressure can be reduced. Observe cavitation inception at different flow rates and speeds. Measure onset conditions and relate to cavitation number calculations. Record acoustic signals and erosion patterns to visualize cavitation bubble collapse.
