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
