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
stage: advanced
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

## Questions

```yaml
- question: "A pipe carrying water in laminar flow has its radius halved by mineral scale buildup, while the pressure drop across the pipe is held constant. By what factor does the volumetric flow rate change?"
  type: multiple-choice
  options:
    - "It decreases by a factor of 16, because Q ∝ R⁴ and (1/2)⁴ = 1/16"
    - "It decreases by a factor of 2, because flow rate scales linearly with the pipe cross-section"
    - "It decreases by a factor of 4, because Q scales with the cross-sectional area R²"
    - "It decreases by a factor of 8, because Q scales with volume (R³)"
  answer: 0
  explanation: "The Hagen-Poiseuille equation states Q = πR⁴ΔP/(8μL). Flow rate depends on the FOURTH power of radius. Halving R gives Q_new = Q_old × (R/2)⁴/R⁴ = Q_old/16. This extreme sensitivity is why even modest deposits dramatically reduce flow. Options 1–3 reflect intuitions from 2D area or 3D volume scaling — neither applies here. The R⁴ dependence is the single most important practical implication of Hagen-Poiseuille."

- question: "An engineer compares two laminar flow systems: one with smooth glass tubing, one with rough steel pipes where roughness elements protrude about 5% of the pipe radius. Both have the same diameter, length, fluid, and pressure drop. Which system delivers greater flow rate?"
  type: multiple-choice
  options:
    - "Both deliver the same flow rate — roughness has no effect on laminar flow because viscous forces dominate and the flow never interacts with wall features"
    - "The smooth glass system delivers more, because roughness increases friction and pressure losses"
    - "The rough steel system delivers more, because roughness disrupts the boundary layer and promotes mixing that reduces viscous losses"
    - "The smooth glass system delivers more, but only for Reynolds numbers above 1,000; below that, roughness is irrelevant"
  answer: 0
  explanation: "In laminar flow, f = 64/Re — roughness does not appear in this expression at all. The viscous sublayer in laminar flow is so thick that it completely engulfs wall roughness features; the orderly, layer-by-layer flow never 'sees' the wall texture. Roughness only matters in turbulent flow, where high-momentum fluid reaches the wall. This is why the Moody chart's laminar region (f = 64/Re) is a single line with no roughness parameter."

- question: "In fully developed laminar pipe flow, the maximum fluid velocity occurs at the pipe wall."
  type: true-false
  answer: false
  explanation: "Maximum velocity occurs at the CENTERLINE (r = 0), where V = Vmax. The no-slip condition requires the fluid velocity to be exactly zero at the wall (r = R). The parabolic profile V(r) = Vmax(1 − r²/R²) decreases monotonically from center to wall. This is the opposite of what might be intuitively expected if one imagines 'friction at the wall slowing everything equally' — in fact, the wall completely arrests flow locally, and the centerline fluid is least affected by wall friction."

- question: "The average velocity in fully developed laminar pipe flow equals exactly half the centerline (maximum) velocity."
  type: true-false
  answer: true
  explanation: "Integrating the parabolic profile V(r) = Vmax(1 − r²/R²) over the circular cross-section yields Vavg = Vmax/2. This factor of two has practical importance: a velocity probe placed at the centerline (common in measurement) reads twice the average velocity. An engineer who misidentifies centerline velocity as average velocity will overestimate volumetric flow rate by exactly 2×."

- question: "Why does the Hagen-Poiseuille equation predict that surface roughness has no effect on laminar flow resistance, and what happens to this immunity as Reynolds number increases toward transition?"
  type: short-answer
  answer: "In laminar flow, the viscous sublayer is thick relative to wall roughness elements — the orderly, layered flow is entirely within this viscous region and never contacts rough wall features with appreciable momentum. Friction depends only on the velocity gradient at the wall (a viscous effect), not on surface texture. As Re increases toward ~2,300, the viscous sublayer thins and eventually turbulent fluctuations begin to sweep fluid directly against the wall. Once fully turbulent, roughness elements protrude through the viscous sublayer and dramatically increase friction — which is why the Moody chart's turbulent region splits into many roughness-dependent curves."
  explanation: "The immunity to roughness in laminar flow is not approximate — it is exact. The laminar f = 64/Re formula applies identically to commercial steel, glass, and corroded pipes, as long as flow remains laminar. This changes categorically at the laminar-turbulent transition, one of the most consequential regime shifts in fluid mechanics."
```

## Explainer

You know from laminar pipe flow prerequisites that viscous forces dominate at low Reynolds numbers, producing orderly, layer-by-layer fluid motion. The Hagen-Poiseuille equation describes the fully developed end-state of that flow — after the entrance region (which you studied separately) has ended and the velocity profile has stopped changing along the pipe. At that point, a steady, axisymmetric, **parabolic velocity profile** exists: V(r) = V_max(1 − (r/R)²), with maximum velocity at the centerline and zero velocity at the wall (the no-slip condition).

The parabola arises from a simple force balance. At any cylindrical shell of radius r inside the pipe, the pressure force pushing fluid forward — ΔP times the cross-sectional area πr² — must equal the viscous shear force acting on the shell's cylindrical surface — μ(dV/dr) times the surface area 2πrL. Solving this ODE with the boundary condition V(R) = 0 gives the parabola directly. A key consequence: the average velocity is exactly half the centerline velocity, V_avg = V_max/2. This factor of two matters in instrumentation — a velocity probe at the centerline overestimates the average by 2x.

Integrating the parabolic profile over the circular cross-section yields the **Hagen-Poiseuille equation**: Q = πR⁴ΔP/(8μL). The most important feature is the R⁴ dependence. Doubling pipe diameter increases flow rate by a factor of 16 at fixed pressure drop. This extreme sensitivity means that small reductions in effective radius — from biofilm, mineral scale, or corrosion — cause dramatic flow reductions in laminar systems. It also explains why your blood vessels must remain open: even small constrictions require the heart to work much harder to maintain the same flow.

The friction factor f = 64/Re follows algebraically from Hagen-Poiseuille when you express head loss in the Darcy-Weisbach form. Notice what is absent from this formula: **surface roughness**. In laminar flow, the viscous sublayer completely engulfs wall roughness features, and the orderly flow never interacts with them. Roughness becomes important only in turbulent flow, where high-momentum fluid reaches the wall. The laminar f = 64/Re relationship is also the basis for the Moody chart's leftmost region — the straight line at low Reynolds numbers — which you'll use when computing friction losses in pipe systems through the Darcy-Weisbach equation.
