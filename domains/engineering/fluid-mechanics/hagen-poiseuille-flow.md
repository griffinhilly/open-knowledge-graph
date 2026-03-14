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
stage: formal-systems
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
