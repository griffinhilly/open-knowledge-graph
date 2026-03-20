---
id: friction-factor-darcy-weisbach-equation
title: Friction Factor and the Darcy-Weisbach Equation
domain: engineering
course: fluid-mechanics
prerequisites:
- id: moody-diagram-friction-factor
  type: hard
- id: turbulent-flow-structure-properties
  type: soft
builds-toward:
- pipe-flow-network-analysis
tags:
- friction
- pressure-drop
- pipe-flow
stage: advanced
status: draft
---

# Friction Factor and the Darcy-Weisbach Equation

## Core Idea
The Darcy-Weisbach equation h_f = f(L/D)(V²/2g) relates head loss to friction factor, pipe length and diameter, and velocity. The friction factor f depends on Reynolds number and surface roughness (relative roughness ε/D); the Moody diagram presents this relationship. For laminar flow f = 64/Re; for turbulent flow, the Colebrook equation implicitly defines f and accounts for both viscous and form effects.

## Explainer

When fluid flows through a pipe, it loses energy to friction — pressure drops, and if you think in terms of equivalent fluid height, this drop is the **head loss** h_f. The Darcy-Weisbach equation gives you that loss: h_f = f(L/D)(V²/2g). Every term has intuitive meaning. Longer pipes lose more head (factor L). Narrower pipes create higher velocity gradients and more friction resistance (factor 1/D). Faster flow means more energy available to lose (factor V²/2g, the velocity head). The **Darcy friction factor** f bundles all the complexity of the flow regime and pipe surface into one dimensionless number.

The Moody diagram you mastered as a prerequisite tells you how to find f. The key insight from that diagram: there are two physically different regimes. In **laminar flow** (Re < ~2300), the parabolic velocity profile is smooth and analytically tractable, giving the exact result f = 64/Re — friction factor simply decreases as flow speeds up. In **turbulent flow**, the physics change completely. The chaotic eddies from your turbulent flow prerequisite now do two things: they flatten the velocity profile (less viscous wall stress) but also pummel the pipe wall with pressure fluctuations. Surface roughness ε matters enormously here because turbulent bursts reach the wall and interact with protrusions that viscous flow would have smoothed over.

For turbulent flow, the **Colebrook equation** captures this physics: 1/√f = −2 log₁₀(ε/3.7D + 2.51/Re√f). Notice it is implicit in f — you need to iterate or use an explicit approximation like the Swamee-Jain formula. At very high Reynolds numbers, the viscous sublayer at the wall becomes thinner than the roughness elements, and f reaches a constant "fully rough" value that depends only on ε/D, not Re at all. This is the flat rightward portion of the Moody diagram — the **hydraulically rough** regime where faster flow doesn't reduce friction.

The practical workflow in pipe system design flows from this equation. Given a pipe geometry and flow rate, you know V and Re. You look up (or calculate) f, compute h_f, and that head loss tells you how much pump work is required to maintain the flow. Conversely, given a fixed pump and known h_f budget, you can size the pipe diameter. The Darcy-Weisbach equation is the accounting tool; the friction factor is the physical quantity that turns fluid mechanics theory into an engineering number. Real pipe networks with bends, valves, and fittings add **minor losses** (expressed as equivalent lengths or loss coefficients), but the Darcy-Weisbach framework handles all of them by superposition.
