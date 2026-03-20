---
id: hagen-poiseuille-flow
title: Hagen-Poiseuille Flow
domain: engineering
course: fluid-mechanics
prerequisites:
- id: laminar-pipe-flow
  type: hard
- id: navier-stokes-equations
  type: soft
tags:
- Hagen-Poiseuille
- laminar pipe flow
- parabolic velocity profile
- pressure drop
- viscous flow
stage: advanced
status: draft
---
# Hagen-Poiseuille Flow

## Core Idea
Hagen-Poiseuille flow is the exact analytical solution for fully developed, steady, incompressible, laminar flow in a circular pipe. The Navier-Stokes equations reduce to a simple ODE when the flow is axisymmetric, unidirectional, and fully developed (∂u/∂x = 0 for the axial velocity profile shape). The resulting velocity profile is parabolic: u(r) = (ΔP/4μL)(R² − r²), with maximum velocity at the centerline equal to twice the mean velocity. The volumetric flow rate is Q = πR⁴ΔP/(8μL), showing the dramatic fourth-power dependence on radius — halving the pipe diameter requires 16 times the pressure drop for the same flow rate. This solution is valid only for Re_D < ~2100 and in the fully developed region downstream of the entrance length.

## How It's Best Learned
Derive the parabolic profile from the cylindrical Navier-Stokes equations step by step, applying no-slip and symmetry boundary conditions. Verify that the wall shear stress τ_w = 8μV_avg/D matches the Darcy friction factor f = 64/Re. Then solve practical problems: compute the pressure drop for oil flowing through a long capillary tube, or estimate the flow rate through a medical catheter given a pressure difference. Compare predictions against the Moody diagram in the laminar regime.

## Common Misconceptions
- The Q ∝ R⁴ relationship (Poiseuille's law) applies only to laminar flow. In turbulent flow, Q depends on R to a power closer to 2.5, mediated by the friction factor.
- Hagen-Poiseuille flow assumes the pipe is long enough for the flow to be fully developed. In short pipes or near inlets, the velocity profile is still developing and the pressure drop per unit length is higher.
- The parabolic profile means the fluid at the wall is stationary (no-slip) while the centerline fluid moves at twice the average velocity. This velocity non-uniformity is critical for understanding residence time distributions in chemical reactors and blood flow in arteries.

## Explainer

From your study of laminar pipe flow and viscosity, you know that fluid near a pipe wall is held stationary by the no-slip condition while fluid near the center moves fastest. Viscosity resists the relative sliding between fluid layers, and the applied pressure drop along the pipe provides the driving force to overcome that resistance. Hagen-Poiseuille flow is what results when these two effects reach a precise, steady balance — it is one of the rare exact analytical solutions in fluid mechanics, valid under conditions strict enough to be enforced but common enough to be routinely useful.

The derivation reduces the cylindrical Navier-Stokes equations to a simple radial ODE by applying three conditions: the flow is axisymmetric (nothing varies with angular position), it is fully developed (the velocity profile shape does not change along the pipe length, so the axial velocity gradient ∂u/∂x = 0), and it is steady and incompressible. Applying no-slip at the wall (u = 0 at r = R) and symmetry at the centerline (du/dr = 0 at r = 0) yields the **parabolic velocity profile**: u(r) = (ΔP/4μL)(R² − r²). The profile is a paraboloid of revolution: zero at the wall, maximum at the centerline, with the centerline velocity equal to exactly twice the cross-sectional average velocity. Integrating over the pipe cross-section gives the Hagen-Poiseuille equation: Q = πR⁴ΔP/(8μL).

The **R⁴ dependence** is the most practically significant result. Double the pipe radius while keeping all else fixed, and flow rate increases 16-fold. Equivalently, pushing the same flow rate through a pipe half the diameter requires 16 times the pressure drop. This extreme sensitivity to radius governs a wide range of physical systems. In medicine: atherosclerotic plaque reducing an artery's radius by 50% increases flow resistance by a factor of 16 — the heart cannot compensate, and blood flow drops severely. In microfluidics: channels machined at 10 μm diameter instead of 20 μm require 16-fold higher driving pressure for the same throughput. In IV therapy: a catheter selected one French size smaller dramatically reduces maximum flow rate. The R⁴ law demands respect in any system where small geometric changes have large hydraulic consequences.

The solution is exact, but its assumptions must all hold. Re < ~2100 is required for laminar flow; above that, turbulence destroys the parabolic profile and the linear Q–ΔP relationship. The flow must be **fully developed**: near the pipe entrance, the velocity profile is still transitioning from the flat entry profile to the parabola, and the entrance length L_e ≈ 0.06 Re·D can be many pipe diameters long for high Reynolds number laminar flows. During this entrance region, pressure drop per unit length is higher than the fully-developed value, which matters for short pipes. The pipe must also be straight and circular; bends, non-circular cross-sections, and wall roughness all invalidate the solution. When these conditions hold — as they commonly do in viscous flow applications — Hagen-Poiseuille provides exact, reliable predictions without numerical approximation.
