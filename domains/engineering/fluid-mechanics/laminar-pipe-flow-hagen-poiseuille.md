---
id: laminar-pipe-flow-hagen-poiseuille
title: Laminar Pipe Flow (Hagen-Poiseuille)
domain: engineering
course: fluid-mechanics
prerequisites:
- id: laminar-pipe-flow
  type: hard
- id: entrance-region-developing-flow-pipe
  type: soft
builds-toward:
- friction-factor-darcy-weisbach-equation
tags:
- laminar
- pipe-flow
- analytical
stage: formal-systems
status: draft
---

# Laminar Pipe Flow (Hagen-Poiseuille)

## Core Idea
In fully developed laminar pipe flow, the velocity profile is parabolic: V(r) = V_max(1 − (r/R)²), resulting in a volumetric flow rate Q = πR⁴ΔP/(8μL). For laminar flow (Re < 2,300), the friction factor f = 64/Re is independent of surface roughness, and head loss varies linearly with velocity.

## How It's Best Learned
Measure pressure drop in laminar flow through tubes of different diameters and lengths at various flow rates. Verify that pressure drop is inversely proportional to the fourth power of diameter and proportional to flow rate.

## Common Misconceptions
- The maximum velocity in laminar pipe flow occurs at the wall (it occurs at the centerline due to the no-slip condition and parabolic profile).
- Friction factor depends on surface roughness in laminar flow (it depends only on Reynolds number; roughness has no effect in laminar flow because viscous forces dominate).

## Explainer

You know from laminar pipe flow prerequisites that viscous forces dominate at low Reynolds numbers, producing orderly, layer-by-layer fluid motion. The Hagen-Poiseuille equation describes the fully developed end-state of that flow — after the entrance region (which you studied separately) has ended and the velocity profile has stopped changing along the pipe. At that point, a steady, axisymmetric, **parabolic velocity profile** exists: V(r) = V_max(1 − (r/R)²), with maximum velocity at the centerline and zero velocity at the wall (the no-slip condition).

The parabola arises from a simple force balance. At any cylindrical shell of radius r inside the pipe, the pressure force pushing fluid forward — ΔP times the cross-sectional area πr² — must equal the viscous shear force acting on the shell's cylindrical surface — μ(dV/dr) times the surface area 2πrL. Solving this ODE with the boundary condition V(R) = 0 gives the parabola directly. A key consequence: the average velocity is exactly half the centerline velocity, V_avg = V_max/2. This factor of two matters in instrumentation — a velocity probe at the centerline overestimates the average by 2x.

Integrating the parabolic profile over the circular cross-section yields the **Hagen-Poiseuille equation**: Q = πR⁴ΔP/(8μL). The most important feature is the R⁴ dependence. Doubling pipe diameter increases flow rate by a factor of 16 at fixed pressure drop. This extreme sensitivity means that small reductions in effective radius — from biofilm, mineral scale, or corrosion — cause dramatic flow reductions in laminar systems. It also explains why your blood vessels must remain open: even small constrictions require the heart to work much harder to maintain the same flow.

The friction factor f = 64/Re follows algebraically from Hagen-Poiseuille when you express head loss in the Darcy-Weisbach form. Notice what is absent from this formula: **surface roughness**. In laminar flow, the viscous sublayer completely engulfs wall roughness features, and the orderly flow never interacts with them. Roughness becomes important only in turbulent flow, where high-momentum fluid reaches the wall. The laminar f = 64/Re relationship is also the basis for the Moody chart's leftmost region — the straight line at low Reynolds numbers — which you'll use when computing friction losses in pipe systems through the Darcy-Weisbach equation.
