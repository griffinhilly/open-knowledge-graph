---
id: laminar-turbulent-transition-critical-reynolds
title: Laminar-Turbulent Transition and Critical Reynolds Number
domain: engineering
course: fluid-mechanics
prerequisites:
- id: reynolds-number
  type: hard
- id: viscosity-temperature-dependence
  type: soft
builds-toward:
- friction-factor-determination-methods
tags:
- transition
- laminar
- turbulent
- instability
stage: formal-systems
status: draft
---

# Laminar-Turbulent Transition and Critical Reynolds Number

## Core Idea
Flow transitions from laminar to turbulent at a critical Reynolds number that depends on disturbance intensity and geometry. In pipes, the transition occurs approximately at Re ≈ 2,300, though transition can begin earlier under disturbing conditions and extend to Re ≈ 4,000 (transitional region). Understanding this region is essential for predicting heat transfer and pressure drop in operating equipment where conditions may straddle the boundary.

## Questions

```yaml
- question: "A pipe flow has Re = 3,200. An engineer needs to calculate the pressure drop per unit length. What is the best approach?"
  type: multiple-choice
  options:
    - "Use f = 64/Re from the Hagen-Poiseuille laminar formula, since Re < 4,000"
    - "Use the turbulent Moody chart friction factor, since Re > 2,300"
    - "Recognize that Re = 3,200 is in the transitional region; neither the laminar nor turbulent formula is reliable, and additional information about disturbance levels is needed"
    - "Average the laminar and turbulent friction factors for Re = 3,200"
  answer: 2
  explanation: "Re = 3,200 falls in the transitional region (roughly 2,300–4,000) where the flow can flicker between laminar and turbulent states depending on inlet conditions, pipe roughness, and vibration. Neither the laminar Hagen-Poiseuille result nor the turbulent Moody chart is reliably applicable. In practice, engineers often design to avoid this region because the friction factor — and heat transfer — are unpredictable there. The sharp answer '< 4,000 means laminar' is the dangerous misconception; transition begins around 2,300, not 4,000."

- question: "Why does the friction factor jump so dramatically when pipe flow transitions from laminar to turbulent at the same Reynolds number?"
  type: multiple-choice
  options:
    - "Turbulent flow has higher viscosity, which increases the wall shear stress"
    - "Turbulent eddies bring high-momentum fluid from the core to the wall region, dramatically increasing wall shear stress beyond what viscous laminar flow produces"
    - "Transition increases the effective pipe diameter, changing the Re calculation"
    - "The pressure drop formula changes from linear to quadratic only because of the different Reynolds number used"
  answer: 1
  explanation: "In laminar flow, momentum transfer to the wall occurs only through viscous diffusion — a slow process that produces the smooth parabolic velocity profile and moderate wall shear. In turbulent flow, eddies actively mix high-velocity fluid from the core toward the wall, dramatically steepening the velocity gradient near the wall and greatly increasing shear stress. This is why the turbulent friction factor is 4–10× higher than the laminar value at the same Re. Viscosity itself doesn't change — the mechanism of momentum transport changes."

- question: "Under carefully controlled laboratory conditions with very smooth pipes and disturbance-free flow, laminar flow can persist well above Re = 2,300."
  type: true-false
  answer: true
  explanation: "Re ≈ 2,300 is a practical engineering threshold, not an absolute physical law. In the laboratory, laminar pipe flow has been maintained to Re > 100,000 by meticulously eliminating inlet disturbances, vibration, and roughness. The transition is a physical instability: at Re > 2,300, small disturbances *can* grow rather than being damped by viscosity, but only if those disturbances are present. In ordinary engineering conditions disturbances are unavoidable, making 2,300 the practical transition point — but the underlying physics is about disturbance amplification, not a hard switch."

- question: "The transition from laminar to turbulent flow occurs instantaneously at Re = 2,300 — below this value the flow is laminar, above it turbulent."
  type: true-false
  answer: false
  explanation: "Transition is not a sharp switch — it is a region. In pipes, flow is reliably laminar below Re ≈ 2,300 and reliably turbulent above Re ≈ 4,000, but the region between these values is transitional: flow can intermittently switch between states, and the friction factor is neither predictable nor well-described by either the laminar or turbulent formula. The precise transition point within this range depends on inlet conditions, surface roughness, and disturbance levels."

- question: "Why does temperature have opposite effects on laminar-turbulent transition tendency for liquids versus gases?"
  type: short-answer
  answer: "Temperature affects the dynamic viscosity μ, which appears in the denominator of Re = ρVD/μ. For liquids, viscosity decreases with temperature — a hotter liquid is less viscous, so Re rises at fixed velocity, making turbulence more likely as the liquid heats up. For gases, viscosity increases with temperature (due to greater molecular collision frequency), so Re falls at fixed velocity, making turbulence less likely as gas heats. The direction of the temperature effect on transition therefore depends entirely on which way viscosity moves, and liquids and gases behave oppositely."
  explanation: "This is a direct application of viscosity-temperature dependence to the Reynolds number formula. The intuition: viscosity is the 'resistance to turbulence' in the Re ratio. Higher viscosity (lower Re) means viscous damping is relatively stronger and laminar flow is more stable. Lower viscosity (higher Re) means inertial forces dominate and transition is more likely. Because liquids and gases have opposite viscosity-temperature relationships, their transition behaviors with heating are also opposite."
```

## Explainer

You already know that the Reynolds number Re = ρVD/μ is the ratio of inertial to viscous forces in a flow. At low Re, viscosity dominates and damps out any disturbances — a small puff of dye injected into a pipe persists as a clean streak from inlet to outlet. This is **laminar flow**: every fluid particle travels in an orderly path parallel to its neighbors. At high Re, inertia dominates and the flow becomes chaotic, with eddies and mixing across the cross-section. This is **turbulent flow**. The transition between them is not a sharp switch but a physical instability process, and the **critical Reynolds number** marks where the orderly laminar solution can no longer resist disruption.

The physical story is one of competing forces. In a pipe, the laminar velocity profile is parabolic — fastest at the center, zero at the wall. This shear creates small perturbations (from wall roughness, pump pulsations, vibration). At low Re, viscosity dissipates these perturbations before they can grow. As Re increases, the inertial energy in the perturbations outpaces viscous damping. Beyond Re ≈ 2,300 in a pipe, small disturbances can amplify rather than decay, eventually rolling up into the three-dimensional vortical structures characteristic of turbulent flow. The transition region (roughly 2,300–4,000) is unstable: the flow can flicker between laminar and turbulent states depending on the disturbance level. In very carefully controlled laboratory conditions, laminar flow can persist to Re > 100,000 — there is nothing magical about 2,300 except that it is the practical threshold under ordinary engineering conditions.

Why does this matter so much for engineering calculations? Because the friction factor — and therefore the pressure drop per unit length of pipe — changes dramatically. In laminar flow, the Hagen-Poiseuille result gives f = 64/Re, a straight line on a log-log plot. In turbulent flow, the Moody chart shows f roughly 4–10× higher than the laminar value at the same Re, and f becomes sensitive to surface roughness. Heat transfer coefficients similarly jump by a large factor at transition, because turbulent mixing brings fluid from the bulk into contact with the wall far more effectively than laminar conduction alone. Designing a heat exchanger or piping system without knowing which regime you're in leads to wildly wrong predictions.

For flat plates and boundary layers, the critical Re is based on distance from the leading edge (Re_x = ρV∞x/μ), with transition occurring around Re_x ≈ 5×10⁵ for a smooth plate in low-turbulence flow. The geometry changes the number but not the concept: the ratio of inertial to viscous forces at some characteristic length scale determines when the laminar solution becomes unstable. Temperature affects transition through viscosity — from your prerequisite on viscosity-temperature dependence, you know that liquid viscosity decreases with temperature, raising Re at fixed velocity and making turbulence more likely as a fluid heats up, while gas viscosity increases with temperature, having the opposite effect.

