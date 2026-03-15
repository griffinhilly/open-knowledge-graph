---
id: reynolds-number
title: The Reynolds Number and Flow Regimes
domain: engineering
course: fluid-mechanics
prerequisites:
- id: viscosity-and-newtonian-fluids
  type: hard
- id: fluid-kinematics
  type: soft
- id: viscosity-gas-liquid-transport
  type: soft
- id: kinetic-molecular-theory
  type: soft
builds-toward:
- laminar-pipe-flow
- turbulent-pipe-flow
- boundary-layer-theory
- dimensional-analysis-and-similarity
tags:
- Reynolds number
- laminar
- turbulent
- transition
- dimensionless
stage: abstract-reasoning
status: validated
---

# The Reynolds Number and Flow Regimes

## Core Idea
The Reynolds number Re = ρVL/μ = VL/ν is the ratio of inertial to viscous forces in a flow. Below a critical Re (≈2300 for pipe flow), viscous forces dominate and flow is laminar — orderly and predictable. Above transition Re (≈4000 for pipes), inertia dominates and flow becomes turbulent — chaotic with enhanced mixing and higher friction. The critical Re depends on geometry (pipe, flat plate, sphere) and flow configuration.

## How It's Best Learned
Observe laminar-to-turbulent transition in a dye injection experiment (Reynolds' original demonstration). Calculate Re for everyday flows — faucets, rivers, blood vessels — to develop intuition about which flows are laminar. Note that Re is the first major dimensionless number encountered; others follow from dimensional analysis.

## Common Misconceptions
- The critical Reynolds number is not a universal constant; 2300 applies to pipe flow but different geometries have different critical values.
- Laminar flow is not always slow and turbulent flow is not always fast — Re depends on viscosity and length scale, not just speed.
- Transition does not happen instantaneously at a single Re; there is a transitional regime between fully laminar and fully turbulent.
