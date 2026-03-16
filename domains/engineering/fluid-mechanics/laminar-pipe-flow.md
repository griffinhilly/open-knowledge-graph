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
stage: formal-systems
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

## Explainer

Laminar pipe flow is one of the few situations in fluid mechanics where the Navier-Stokes equations yield an exact, closed-form solution. The key is the geometry: a long straight circular pipe, flow that doesn't change along its length (fully developed), and a Reynolds number below about 2300. From your prerequisite on viscosity and Newtonian fluids, you know that viscosity is the resistance of a fluid to shearing — layers of fluid resist sliding past one another. In a pipe, the no-slip condition forces fluid at the wall to be stationary, while fluid at the center moves fastest. Viscosity transmits this drag radially inward, and the pressure gradient along the pipe provides the driving force that keeps the fluid moving. The balance between these two — viscous drag and pressure gradient — determines the velocity at every radial position.

The exact solution is a **parabolic velocity profile**: u(r) = (R² − r²)/(4μ) · (−dP/dx). At the centerline (r = 0), velocity is maximum; at the wall (r = R), it is zero. The average velocity is exactly half the centerline velocity — a result that surprises many students. This parabola isn't assumed; it falls directly out of the Navier-Stokes equations when you apply cylindrical symmetry and the no-slip boundary condition. Integrating the velocity profile over the pipe cross-section gives the **Hagen-Poiseuille law**: Q = πR⁴ΔP/(8μL). This formula has four critical features worth understanding separately: flow rate grows with the fourth power of radius, decreases linearly with viscosity, increases linearly with pressure drop, and decreases linearly with length.

The R⁴ dependence is the most important result, and its magnitude is consistently underestimated. If you double the pipe radius, flow rate increases by 2⁴ = 16 times for the same pressure drop. Conversely, halving the radius reduces flow by a factor of 16 — which is why arterial narrowing (stenosis) in the body is so dangerous: a 50% reduction in arterial radius cuts blood flow to 1/16 of normal. This is also why your Reynolds number prerequisite matters here: Re = ρVD/μ. If Re stays below 2300, the flow remains laminar and this R⁴ relationship holds exactly. Above that threshold, the flow transitions to turbulence, the profile flattens, and friction increases dramatically — a topic for turbulent pipe flow.

The laminar friction factor f = 64/Re provides a dimensionless measure of pressure loss per unit length: ΔP = f·(L/D)·(½ρV²). What's notable is that f depends only on Re in laminar flow, not on pipe roughness. This is because the orderly, layered nature of laminar flow means the fluid doesn't "see" small surface imperfections — the viscous sublayer completely suppresses roughness effects. In turbulent flow, roughness becomes dominant. This explains why smooth copper tubing and rough cast iron pipe behave identically below Re ≈ 2300 but very differently above it.
