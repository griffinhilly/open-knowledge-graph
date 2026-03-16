---
id: jet-impact-force-momentum-buckets
title: Jet Impact Force and Momentum Analysis
domain: engineering
course: fluid-mechanics
prerequisites:
- id: control-volume-momentum
  type: hard
- id: bernoullis-equation
  type: soft
tags:
- momentum
- jet
- force
stage: formal-systems
status: draft
---

# Jet Impact Force and Momentum Analysis

## Core Idea
The momentum equation applied to a control volume surrounding an impacting jet yields the force on a surface: F = ṁ(V_exit - V_inlet) = ρQ(V_exit - V_inlet). When a jet deflects by 180° on a flat plate, the force is F = 2ρQV; when deflected by θ, F = ρQV(1 - cosθ). This principle governs Pelton wheel bucket design, rocket control systems, and hydraulic actuators.

## Explainer

A jet of water striking a surface is one of the cleanest applications of the control volume momentum equation you already know. Draw the control volume enclosing the region where the jet meets the surface. Continuity demands that whatever mass flow enters must exit (neglecting splashing). The force the jet exerts on the surface is then entirely determined by the change in momentum flux between inlet and outlet — you do not need to know the pressure or velocity anywhere inside the control volume.

For a **flat plate perpendicular to the jet**, the flow arrives with velocity V in the x-direction and exits sideways with zero x-momentum. Applying the x-momentum equation: F = ṁV_in - ṁV_out,x = ṁV - 0 = ρAV². The force on the plate equals the incoming momentum flux. Now consider a **curved vane that deflects the jet 180°** — a bucket that turns the flow back on itself. The exit velocity is −V (in the x-direction), so F = ṁV - ṁ(−V) = 2ṁV = 2ρAV². Doubling the deflection angle doubles the force. For an arbitrary deflection angle θ, the x-component of exit velocity is V·cosθ, giving F = ρAV²(1 − cosθ), which ranges from zero at θ = 0° (the jet passes straight through, unchanged) to 2ρAV² at θ = 180°.

This is exactly why **Pelton wheel buckets** are designed as hemispherical cups that turn the jet nearly 180°. Each bucket catches the jet and reverses its momentum, extracting the maximum possible force and therefore maximum work from the water. In practice the angle is slightly less than 180° to prevent the exiting water from interfering with the next bucket, but the design target is always as close to 180° as mechanically feasible.

When the vane is **moving** at velocity u (as on a real Pelton wheel or turbine blade), the analysis still applies but the relative velocity of the jet with respect to the vane determines the momentum exchange: the effective jet velocity becomes (V − u), so F = ρA(V−u)²(1 − cosθ). The power delivered is F·u = ρA(V−u)²(1−cosθ)·u, which reaches a maximum when u = V/3 for a flat plate (θ = 90°) or u = V/3 for the general case — an important result for turbomachinery optimization.

The key discipline in these problems is careful sign convention. Choose a positive x-direction, write V_exit as a signed vector component, and let the algebra work out the direction of the force. A negative result simply means the force acts in the direction opposite to your assumed positive. Once you can confidently set up the control volume, identify all momentum fluxes with correct signs, and apply continuity, jet impact problems become straightforward and satisfying — a direct application of Newton's second law to a practical engineering system.
