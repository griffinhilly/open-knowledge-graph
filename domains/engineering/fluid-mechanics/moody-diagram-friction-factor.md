---
id: moody-diagram-friction-factor
title: Moody Diagram and Friction Factor
domain: engineering
course: fluid-mechanics
prerequisites:
- id: turbulent-pipe-flow
  type: hard
- id: reynolds-number
  type: hard
tags:
- Moody diagram
- Darcy friction factor
- Colebrook equation
- pipe roughness
- flow regimes
- Darcy-Weisbach
stage: formal-systems
status: draft
---
# Moody Diagram and Friction Factor

## Core Idea
The Moody diagram is the central engineering tool for pipe flow analysis, plotting the Darcy friction factor f against Reynolds number Re_D for various values of relative roughness ε/D. It encodes three regimes: laminar (f = 64/Re, independent of roughness), transitional (Re ≈ 2000–4000, uncertain and avoided in design), and turbulent (f depends on both Re and ε/D). In the turbulent regime, smooth pipes follow the Blasius correlation (f ≈ 0.316/Re^0.25) at moderate Re, while at high Re the friction factor becomes independent of Re and depends only on roughness — the fully rough regime. The implicit Colebrook equation, 1/√f = −2.0 log(ε/3.7D + 2.51/Re√f), unifies the smooth and rough limits and is the basis for the turbulent portion of the Moody diagram. The friction factor enters the Darcy-Weisbach equation h_f = f(L/D)(V²/2g) to compute head loss in pipes.

## How It's Best Learned
Use the Moody diagram to solve a series of pipe flow problems: given flow rate, pipe size, and material (roughness), find the pressure drop; then reverse the problem to find required diameter for a given allowable head loss. Iterate the Colebrook equation by hand for one case, then compare against the explicit Swamee-Jain approximation. Plot your own Moody diagram from the Colebrook equation to understand why the curves fan out at higher roughness and collapse to the laminar line at low Re.

## Common Misconceptions
- The Darcy friction factor is 4 times the Fanning friction factor. Confusing the two introduces a factor-of-4 error in head loss — always check which convention a source uses.
- Roughness that matters is the sand-grain equivalent roughness ε, not the actual surface profile. Real surfaces have different roughness characters (riveted steel vs. corroded cast iron) that map to different equivalent sand-grain values.
- The "fully rough" regime does not mean the flow is more turbulent — it means the roughness elements protrude beyond the viscous sublayer, so viscous effects no longer influence the friction factor and f becomes independent of Re.
