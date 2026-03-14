---
id: flow-around-cylinders-spheres
title: Flow Around Cylinders and Spheres
domain: engineering
course: fluid-mechanics
prerequisites:
- id: drag-coefficient-bluff-bodies
  type: hard
- id: reynolds-number
  type: hard
tags:
- cylinder flow
- sphere flow
- Stokes flow
- creeping flow
- flow separation
- wake
- von Karman vortex street
stage: formal-systems
status: draft
---
# Flow Around Cylinders and Spheres

## Core Idea
The flow around a cylinder or sphere is the canonical problem for understanding external flow phenomena across the full range of Reynolds numbers. At very low Re (Re < 1), Stokes (creeping) flow dominates: inertia is negligible, the flow is symmetric fore and aft, and drag is purely viscous (F_D = 3πμVD for a sphere, giving C_D = 24/Re). As Re increases (Re ~ 10–40 for a cylinder), the flow separates from the rear surface and a steady recirculating wake forms. At Re ~ 40–200, the wake becomes unstable and alternating vortices shed from each side of the cylinder in a periodic pattern — the von Karman vortex street — with a well-defined Strouhal number St = fD/V ≈ 0.21. At higher Re, the wake becomes turbulent, vortex shedding persists but becomes less regular, and the drag coefficient plateaus until the drag crisis at Re ~ 3×10⁵ (for a sphere) where the turbulent boundary layer transition delays separation. These phenomena govern wind loads on structures, heat exchanger tube vibrations, and sediment transport.

## How It's Best Learned
Watch flow visualization videos showing the progression from creeping flow to steady separation to vortex shedding to turbulent wake as Re increases. Calculate the Stokes drag on a settling particle and compare it to the drag using the empirical C_D(Re) curve. Estimate the vortex shedding frequency for wind blowing over a flagpole or power line using the Strouhal number and assess whether it could excite resonance. Solve for the terminal velocity of a sphere falling through a viscous fluid by balancing weight, buoyancy, and Stokes drag.

## Common Misconceptions
- Stokes flow (C_D = 24/Re) applies only at very low Re — using it at Re = 100 gives errors exceeding 100%. The empirical C_D vs. Re curve or correlations (like the Schiller-Naumann formula) must be used at moderate Re.
- The von Karman vortex street is not random turbulence — it is a highly organized, periodic instability. Its frequency is predictable from the Strouhal number, which is remarkably constant (St ≈ 0.21 for a cylinder) over a wide range of Re (300–10⁵).
- Flow separation on a cylinder or sphere does not occur at the equator (90 degrees from the stagnation point). For laminar boundary layers, separation occurs at about 80 degrees; for turbulent boundary layers, it delays to about 120 degrees, which is why the wake is smaller and drag is lower after the drag crisis.
