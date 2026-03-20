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
stage: advanced
status: draft
---

# Laminar-Turbulent Transition and Critical Reynolds Number

## Core Idea
Flow transitions from laminar to turbulent at a critical Reynolds number that depends on disturbance intensity and geometry. In pipes, the transition occurs approximately at Re ≈ 2,300, though transition can begin earlier under disturbing conditions and extend to Re ≈ 4,000 (transitional region). Understanding this region is essential for predicting heat transfer and pressure drop in operating equipment where conditions may straddle the boundary.

## Explainer

You already know that the Reynolds number Re = ρVD/μ is the ratio of inertial to viscous forces in a flow. At low Re, viscosity dominates and damps out any disturbances — a small puff of dye injected into a pipe persists as a clean streak from inlet to outlet. This is **laminar flow**: every fluid particle travels in an orderly path parallel to its neighbors. At high Re, inertia dominates and the flow becomes chaotic, with eddies and mixing across the cross-section. This is **turbulent flow**. The transition between them is not a sharp switch but a physical instability process, and the **critical Reynolds number** marks where the orderly laminar solution can no longer resist disruption.

The physical story is one of competing forces. In a pipe, the laminar velocity profile is parabolic — fastest at the center, zero at the wall. This shear creates small perturbations (from wall roughness, pump pulsations, vibration). At low Re, viscosity dissipates these perturbations before they can grow. As Re increases, the inertial energy in the perturbations outpaces viscous damping. Beyond Re ≈ 2,300 in a pipe, small disturbances can amplify rather than decay, eventually rolling up into the three-dimensional vortical structures characteristic of turbulent flow. The transition region (roughly 2,300–4,000) is unstable: the flow can flicker between laminar and turbulent states depending on the disturbance level. In very carefully controlled laboratory conditions, laminar flow can persist to Re > 100,000 — there is nothing magical about 2,300 except that it is the practical threshold under ordinary engineering conditions.

Why does this matter so much for engineering calculations? Because the friction factor — and therefore the pressure drop per unit length of pipe — changes dramatically. In laminar flow, the Hagen-Poiseuille result gives f = 64/Re, a straight line on a log-log plot. In turbulent flow, the Moody chart shows f roughly 4–10× higher than the laminar value at the same Re, and f becomes sensitive to surface roughness. Heat transfer coefficients similarly jump by a large factor at transition, because turbulent mixing brings fluid from the bulk into contact with the wall far more effectively than laminar conduction alone. Designing a heat exchanger or piping system without knowing which regime you're in leads to wildly wrong predictions.

For flat plates and boundary layers, the critical Re is based on distance from the leading edge (Re_x = ρV∞x/μ), with transition occurring around Re_x ≈ 5×10⁵ for a smooth plate in low-turbulence flow. The geometry changes the number but not the concept: the ratio of inertial to viscous forces at some characteristic length scale determines when the laminar solution becomes unstable. Temperature affects transition through viscosity — from your prerequisite on viscosity-temperature dependence, you know that liquid viscosity decreases with temperature, raising Re at fixed velocity and making turbulence more likely as a fluid heats up, while gas viscosity increases with temperature, having the opposite effect.

