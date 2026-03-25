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
- id: colebrook-white-friction-correlation
  type: soft
builds-toward:
- pipe-flow-network-analysis
tags:
- friction
- pressure-drop
- pipe-flow
stage: formal-systems
status: validated
---
# Friction Factor and the Darcy-Weisbach Equation

## Core Idea
The Darcy-Weisbach equation h_f = f(L/D)(V²/2g) relates head loss to friction factor, pipe length and diameter, and velocity. The friction factor f depends on Reynolds number and surface roughness (relative roughness ε/D); the Moody diagram presents this relationship. For laminar flow f = 64/Re; for turbulent flow, the Colebrook equation implicitly defines f and accounts for both viscous and form effects.

## Questions

```yaml
- question: "An engineer doubles the flow velocity in a smooth pipe with laminar flow. What happens to the friction factor and head loss?"
  type: multiple-choice
  options:
    - "Friction factor doubles, head loss quadruples"
    - "Friction factor halves (since Re doubles), but head loss still doubles because the velocity-squared term dominates"
    - "Friction factor halves and head loss also halves"
    - "Friction factor is unchanged since it only depends on pipe roughness"
  answer: 1
  explanation: "In laminar flow, f = 64/Re. Doubling velocity doubles Re, so f halves. Head loss h_f = f(L/D)(V²/2g): with f halving and V² doubling, h_f = (f/2)(4V²/2g)... wait — f halves while V² doubles, so h_f doubles overall. This is counterintuitive: faster flow halves the friction factor, but head loss still increases because the velocity-squared term grows faster than f shrinks. Option D is wrong: in laminar flow f depends on Re (and thus on velocity), not roughness."

- question: "At very high Reynolds numbers in a rough pipe, what primarily determines the friction factor?"
  type: multiple-choice
  options:
    - "Reynolds number alone — faster flow always reduces friction factor"
    - "Relative roughness ε/D alone — the viscous sublayer is thinner than roughness elements so Re no longer matters"
    - "The Colebrook equation reduces to f = 64/Re at high Re"
    - "Friction factor goes to zero at very high Reynolds numbers because turbulence fully develops"
  answer: 1
  explanation: "This is the 'hydraulically rough' or 'fully rough' regime. At very high Re, the viscous sublayer at the pipe wall becomes thinner than the roughness elements. Turbulent eddies interact directly with roughness protrusions, and pressure drag from those elements dominates over viscous wall stress. The Colebrook equation reduces to 1/√f = −2 log₁₀(ε/3.7D), which is independent of Re — the flat rightward portion of the Moody diagram. Option A is true for laminar flow but fails at very high Re in rough pipes."

- question: "In turbulent pipe flow, increasing the flow velocity always decreases the friction factor."
  type: true-false
  answer: false
  explanation: "This is true in laminar flow (f = 64/Re) and in the smooth-pipe turbulent regime, but NOT in the hydraulically rough regime. Once Re is high enough that the viscous sublayer is thinner than the roughness elements, f becomes constant — independent of velocity. The Moody diagram shows a clear transition: f decreases with Re in the smooth-pipe region, then levels off to a horizontal asymptote in the fully rough regime. Applying the laminar intuition to turbulent rough-pipe flow is a common error."

- question: "The Colebrook equation is preferred over f = 64/Re for turbulent flow partly because it is explicit in f, making it easy to solve directly."
  type: true-false
  answer: false
  explanation: "The Colebrook equation is preferred for turbulent flow because it accounts for both viscous effects (Re term) and roughness (ε/D term). However, it is *implicit* in f — f appears on both sides: 1/√f = −2 log₁₀(ε/3.7D + 2.51/Re√f). This requires iterative solution or an explicit approximation like the Swamee-Jain formula. The implicitness is precisely why engineers use the Moody diagram graphically or rely on explicit approximations in practice."

- question: "Explain the physical reason why the Darcy friction factor for turbulent flow depends on pipe roughness (ε/D), while for laminar flow it does not."
  type: short-answer
  answer: "In laminar flow, the velocity profile is smooth and parabolic, with a thick viscous sublayer near the wall that completely submerges roughness elements — the flow does not 'see' wall irregularities. Friction comes only from viscous shear in the sublayer, giving f = 64/Re regardless of roughness. In turbulent flow, chaotic eddies extend toward the wall. When the viscous sublayer is thinner than the roughness protrusions (hydraulically rough regime), turbulent bursts strike the protrusions directly, creating pressure drag ('form drag') on each bump. This form drag depends on the size and density of roughness elements (captured by ε/D) and dominates over viscous drag."
  explanation: "This explains why pipe material matters in turbulent applications: commercial steel (ε ≈ 0.046 mm) behaves much like a smooth pipe at moderate Re but diverges significantly from cast iron (ε ≈ 0.26 mm) at high Re. Selecting pipe material based on expected flow regime is an engineering decision informed directly by this physics."
```

## Explainer

When fluid flows through a pipe, it loses energy to friction — pressure drops, and if you think in terms of equivalent fluid height, this drop is the **head loss** h_f. The Darcy-Weisbach equation gives you that loss: h_f = f(L/D)(V²/2g). Every term has intuitive meaning. Longer pipes lose more head (factor L). Narrower pipes create higher velocity gradients and more friction resistance (factor 1/D). Faster flow means more energy available to lose (factor V²/2g, the velocity head). The **Darcy friction factor** f bundles all the complexity of the flow regime and pipe surface into one dimensionless number.

The Moody diagram you mastered as a prerequisite tells you how to find f. The key insight from that diagram: there are two physically different regimes. In **laminar flow** (Re < ~2300), the parabolic velocity profile is smooth and analytically tractable, giving the exact result f = 64/Re — friction factor simply decreases as flow speeds up. In **turbulent flow**, the physics change completely. The chaotic eddies from your turbulent flow prerequisite now do two things: they flatten the velocity profile (less viscous wall stress) but also pummel the pipe wall with pressure fluctuations. Surface roughness ε matters enormously here because turbulent bursts reach the wall and interact with protrusions that viscous flow would have smoothed over.

For turbulent flow, the **Colebrook equation** captures this physics: 1/√f = −2 log₁₀(ε/3.7D + 2.51/Re√f). Notice it is implicit in f — you need to iterate or use an explicit approximation like the Swamee-Jain formula. At very high Reynolds numbers, the viscous sublayer at the wall becomes thinner than the roughness elements, and f reaches a constant "fully rough" value that depends only on ε/D, not Re at all. This is the flat rightward portion of the Moody diagram — the **hydraulically rough** regime where faster flow doesn't reduce friction.

The practical workflow in pipe system design flows from this equation. Given a pipe geometry and flow rate, you know V and Re. You look up (or calculate) f, compute h_f, and that head loss tells you how much pump work is required to maintain the flow. Conversely, given a fixed pump and known h_f budget, you can size the pipe diameter. The Darcy-Weisbach equation is the accounting tool; the friction factor is the physical quantity that turns fluid mechanics theory into an engineering number. Real pipe networks with bends, valves, and fittings add **minor losses** (expressed as equivalent lengths or loss coefficients), but the Darcy-Weisbach framework handles all of them by superposition.
