---
id: laminar-pipe-flow
title: Laminar Pipe Flow (Hagen-Poiseuille)
domain: engineering
course: fluid-mechanics
prerequisites:
- id: reynolds-number
  type: hard
- id: navier-stokes-equations
  type: soft
- id: viscosity-and-newtonian-fluids
  type: hard
builds-toward:
- turbulent-pipe-flow
- pipe-system-losses
tags:
- Hagen-Poiseuille
- laminar flow
- parabolic profile
- pipe flow
stage: advanced
status: validated
---

# Laminar Pipe Flow (Hagen-Poiseuille)

## Core Idea
For fully developed laminar flow in a circular pipe (Re < 2300), the Navier-Stokes equations yield an exact solution: a parabolic velocity profile u(r) = (1/4μ)(-dP/dx)(R² − r²). The volume flow rate is Q = πR⁴ΔP/(8μL) — the Hagen-Poiseuille law. Friction factor for laminar flow is f = 64/Re, depending only on Reynolds number. Pressure drop scales linearly with flow rate and inversely with the fourth power of radius.

## How It's Best Learned
Derive the parabolic profile by applying the Navier-Stokes equations in cylindrical coordinates and integrating. Then measure Q as a function of tube radius and length in lab to confirm the R⁴ dependence — the dramatic effect of narrowing a tube. Compare with turbulent flow (flatter profile, higher friction).

## Common Misconceptions
- Laminar pipe flow has a maximum velocity at the centerline equal to twice the average velocity — not equal to it.
- The Hagen-Poiseuille law assumes fully developed flow (far from the entrance); near the inlet, the flow is still developing and the profile is not yet parabolic.
- The R⁴ dependence means halving the pipe radius increases pressure drop by a factor of 16 at the same flow rate — often underestimated.

## Questions

```yaml
- question: "Atherosclerotic plaque reduces an artery's internal radius from R to R/2. Assuming the same pressure gradient, by what factor does blood flow through the artery decrease?"
  type: multiple-choice
  options:
    - "By a factor of 2 (proportional to the radius reduction)"
    - "By a factor of 4 (proportional to radius squared)"
    - "By a factor of 8 (proportional to radius cubed)"
    - "By a factor of 16 (proportional to radius to the fourth power)"
  answer: 3
  explanation: "The Hagen-Poiseuille law Q = πR⁴ΔP/(8μL) shows flow scales with R⁴. Halving the radius gives (R/2)⁴ = R⁴/16, so flow decreases to 1/16 of original. This dramatic R⁴ dependence explains why arterial stenosis is so dangerous: a 50% reduction in radius cuts blood flow to 1/16 of normal. Options A, B, and C represent common underestimates of how sensitively flow responds to radius changes."

- question: "In fully developed laminar pipe flow, what is the centerline velocity relative to the cross-sectional average velocity?"
  type: multiple-choice
  options:
    - "Equal to the average velocity (uniform flow profile)"
    - "1.5 times the average velocity"
    - "2 times the average velocity"
    - "Dependent on the Reynolds number and pipe roughness"
  answer: 2
  explanation: "The parabolic velocity profile u(r) = (R² − r²)/(4μ)·(−dP/dx) reaches its maximum at the centerline (r = 0). Integrating this profile over the cross-section and dividing by area gives an average velocity equal to exactly half the centerline velocity. This is a consequence of the parabola's shape. Option D is incorrect because in laminar flow, the profile is determined entirely by the governing physics and does not depend on roughness."

- question: "In laminar pipe flow, a smooth-walled pipe and a rough-walled pipe of the same diameter will have the same friction factor if both operate at the same Reynolds number."
  type: true-false
  answer: true
  explanation: "The laminar friction factor f = 64/Re depends only on the Reynolds number, not on pipe roughness. Laminar flow consists of orderly, parallel layers — the viscous sublayer extends to the wall and completely suppresses the effect of surface imperfections. Fluid never 'feels' the roughness because the flow is not turbulent enough to throw fluid into contact with wall features. In turbulent flow, roughness becomes the dominant factor controlling friction."

- question: "According to the Hagen-Poiseuille law, doubling the pipe length has a larger effect on flow rate than halving the pipe radius."
  type: true-false
  answer: false
  explanation: "Q = πR⁴ΔP/(8μL). Doubling pipe length (L → 2L) reduces flow by a factor of 2. Halving the pipe radius (R → R/2) reduces flow by a factor of (1/2)⁴ = 16. The R⁴ dependence on radius far outweighs the linear dependence on length. This asymmetry is practically important: a modest reduction in pipe diameter creates a far larger pressure drop than a large increase in pipe length."

- question: "Why does the Hagen-Poiseuille law's R⁴ dependence make the internal radius of a blood vessel so critical to blood flow? Use the law to explain what happens during arterial narrowing."
  type: short-answer
  answer: "Q = πR⁴ΔP/(8μL) shows that flow rate is proportional to the fourth power of radius — flow is extraordinarily sensitive to radius changes. A 50% reduction in radius (R → R/2) reduces flow to (1/2)⁴ = 1/16 of its original value at the same driving pressure. During arterial narrowing (stenosis), even modest reductions in internal radius from plaque buildup produce catastrophic drops in blood flow to downstream tissue. The heart must increase pressure significantly to maintain flow, raising blood pressure and cardiac workload."
  explanation: "The R⁴ relationship is the key result of laminar pipe flow analysis and is routinely underestimated because people expect a linear or quadratic relationship. The fourth-power sensitivity arises because radius appears both in the cross-sectional area (πR²) and in the parabolic velocity profile (which steepens as the pipe widens, giving higher average velocity). These effects compound, yielding the fourth-power scaling."
```

## Explainer

Laminar pipe flow is one of the few situations in fluid mechanics where the Navier-Stokes equations yield an exact, closed-form solution. The key is the geometry: a long straight circular pipe, flow that doesn't change along its length (fully developed), and a Reynolds number below about 2300. From your prerequisite on viscosity and Newtonian fluids, you know that viscosity is the resistance of a fluid to shearing — layers of fluid resist sliding past one another. In a pipe, the no-slip condition forces fluid at the wall to be stationary, while fluid at the center moves fastest. Viscosity transmits this drag radially inward, and the pressure gradient along the pipe provides the driving force that keeps the fluid moving. The balance between these two — viscous drag and pressure gradient — determines the velocity at every radial position.

The exact solution is a **parabolic velocity profile**: u(r) = (R² − r²)/(4μ) · (−dP/dx). At the centerline (r = 0), velocity is maximum; at the wall (r = R), it is zero. The average velocity is exactly half the centerline velocity — a result that surprises many students. This parabola isn't assumed; it falls directly out of the Navier-Stokes equations when you apply cylindrical symmetry and the no-slip boundary condition. Integrating the velocity profile over the pipe cross-section gives the **Hagen-Poiseuille law**: Q = πR⁴ΔP/(8μL). This formula has four critical features worth understanding separately: flow rate grows with the fourth power of radius, decreases linearly with viscosity, increases linearly with pressure drop, and decreases linearly with length.

The R⁴ dependence is the most important result, and its magnitude is consistently underestimated. If you double the pipe radius, flow rate increases by 2⁴ = 16 times for the same pressure drop. Conversely, halving the radius reduces flow by a factor of 16 — which is why arterial narrowing (stenosis) in the body is so dangerous: a 50% reduction in arterial radius cuts blood flow to 1/16 of normal. This is also why your Reynolds number prerequisite matters here: Re = ρVD/μ. If Re stays below 2300, the flow remains laminar and this R⁴ relationship holds exactly. Above that threshold, the flow transitions to turbulence, the profile flattens, and friction increases dramatically — a topic for turbulent pipe flow.

The laminar friction factor f = 64/Re provides a dimensionless measure of pressure loss per unit length: ΔP = f·(L/D)·(½ρV²). What's notable is that f depends only on Re in laminar flow, not on pipe roughness. This is because the orderly, layered nature of laminar flow means the fluid doesn't "see" small surface imperfections — the viscous sublayer completely suppresses roughness effects. In turbulent flow, roughness becomes dominant. This explains why smooth copper tubing and rough cast iron pipe behave identically below Re ≈ 2300 but very differently above it.
