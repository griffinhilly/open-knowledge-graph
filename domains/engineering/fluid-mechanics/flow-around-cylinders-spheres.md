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
stage: advanced
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

## Explainer

The flow around a bluff body like a cylinder or sphere is one of fluid mechanics' most studied problems because it captures the full range of flow physics in a single geometry. Your prerequisite, the **Reynolds number** Re = ρVD/μ, is the organizing variable: it compares inertial to viscous forces and acts as a dial that, as you turn it up, progressively hands control from viscosity to inertia. At each Re regime the flow looks qualitatively different, and each transition introduces new physics.

At very low Re (Re < 1) you are in **Stokes (creeping) flow**. Viscosity completely dominates: the flow wraps smoothly around the body, is symmetric fore and aft, and drag is purely viscous. For a sphere, Stokes derived the elegant result F_D = 3πμVD, giving C_D = 24/Re. This describes a red blood cell settling through plasma or a sand grain falling in still water. As Re climbs into the 10–100 range, inertia becomes significant. The downstream (wake) side can no longer sustain the symmetric pattern, the boundary layer **separates** from the rear surface, and a recirculating wake forms. The flow is no longer reversible — a parcel of fluid swept around the front does not retrace its path back.

At Re ~ 40–200 for a cylinder, the wake becomes unstable and sheds vortices alternately from each side in a repeating pattern — the **von Karman vortex street**. This periodic shedding has a well-defined frequency characterized by the **Strouhal number** St = fD/V ≈ 0.21, which remains nearly constant across three decades of Re. The shedding has direct engineering consequences: it creates an oscillating side force on the body at frequency f = 0.21V/D. If that frequency matches a structure's natural frequency, resonance follows. This is why power lines sing in the wind, why suspension bridge cables need dampers, and why heat exchanger tubes must be designed so their natural frequency does not coincide with the vortex shedding frequency at typical flow speeds.

At Re ~ 3×10⁵ a counterintuitive phenomenon called the **drag crisis** occurs. The laminar boundary layer transitions to turbulent, which allows it to remain attached further around the body before separating. The **separation point** moves downstream, the wake shrinks dramatically, and C_D drops from about 0.5 to about 0.1. Golf balls exploit this: their dimples trip the boundary layer turbulent at lower Re, lowering the drag crisis speed into the range of typical golf shots and producing a longer, lower-drag flight. The broader lesson is that reducing drag on a bluff body is not about streamlining the front — it is about controlling where the flow separates at the rear.
