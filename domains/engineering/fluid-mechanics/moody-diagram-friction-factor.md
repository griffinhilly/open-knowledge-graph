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
stage: advanced
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

## Explainer

Pipe flow problems share a common structure: you know the geometry (length, diameter, roughness) and the flow rate, and you need to find the pressure drop — or vice versa. The Darcy-Weisbach equation, h_f = f(L/D)(V²/2g), reduces all the fluid physics to a single dimensionless number: the **Darcy friction factor** f. But f is not a constant — it depends on flow regime and surface condition, which is exactly what the Moody diagram encodes.

From your Reynolds number prerequisite, you know Re = VD/ν and that laminar flow (Re < 2000) has a parabolic velocity profile with analytic friction behavior. In laminar flow, f = 64/Re exactly — no roughness dependence, because the smooth viscous sublayer that covers the wall completely masks whatever roughness lies beneath it. As Re increases into the turbulent regime (Re > 4000), the viscous sublayer thins. Once it becomes thin enough that roughness elements protrude through it, those elements generate turbulent eddies and pressure-drag contributions that add to friction. Smooth-pipe turbulence follows the Blasius correlation — f ≈ 0.316/Re^0.25 — valid for moderate Re. Rough pipes follow a higher f that depends on relative roughness ε/D, where ε is the sand-grain equivalent roughness. At very high Re, the sublayer is so thin that the rough elements fully dominate and f becomes independent of Re: this is the **fully rough** regime, represented by the horizontal asymptotes at the right edge of the Moody diagram.

The **Colebrook equation** — 1/√f = −2.0 log(ε/3.7D + 2.51/Re√f) — is the implicit formula that generates the entire turbulent region of the Moody diagram. It is implicit in f, so solving it requires iteration: start with a first guess (e.g., f = 0.02), substitute into the right side, compute a new f, repeat until convergence (2–3 iterations typically suffice). The explicit Swamee-Jain approximation avoids iteration at the cost of a small error. In practice, the Moody diagram is a graphical version of the Colebrook equation: you locate your Re on the x-axis, trace horizontally to your ε/D curve, then read f on the y-axis.

Using the diagram for a real problem: you need the pipe diameter to deliver a specified flow rate within an allowable pressure drop. This "sizing" problem is iterative because both Re and f depend on V, which depends on the diameter you're trying to find. The standard approach is to assume a diameter, compute Re and ε/D, read f from the Moody diagram, check the head loss, and adjust. Alternatively, because f varies weakly with Re in the turbulent regime, a first guess of f ≈ 0.02 followed by one or two diagram corrections typically converges quickly. Every pipe system — water distribution networks, HVAC ducting, oil pipelines — runs through this same calculation, making the Moody diagram one of the most practically used figures in all of engineering fluid mechanics.
