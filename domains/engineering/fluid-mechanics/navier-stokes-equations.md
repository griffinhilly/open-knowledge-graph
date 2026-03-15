---
id: navier-stokes-equations
title: The Navier-Stokes Equations
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-kinematics
  type: hard
- id: viscosity-and-newtonian-fluids
  type: hard
- id: partial-derivatives
  type: hard
- id: continuity-equation-fluid
  type: hard
- id: curl-and-divergence
  type: hard
- id: vector-fields
  type: soft
- id: partial-differential-equations
  type: soft
- id: differential-equations-intro
  type: hard
builds-toward:
- laminar-pipe-flow
- boundary-layer-theory
- potential-flow-theory
tags:
- Navier-Stokes
- momentum equation
- viscous flow
- governing equations
stage: formal-systems
status: validated
---

# The Navier-Stokes Equations

## Core Idea
The Navier-Stokes equations are Newton's second law applied to a viscous fluid element: ρ(DV/Dt) = −∇P + μ∇²V + ρg. The left side is mass times acceleration (using the material derivative); the right side includes pressure gradient, viscous diffusion, and body forces. Together with the continuity equation, they fully describe incompressible Newtonian flow. Exact solutions exist only for simple geometries; most engineering applications require simplification or numerical methods.

## How It's Best Learned
Derive the equations by applying Newton's second law to a differential fluid element, accounting for normal and shear stresses on each face. Solve simplified cases: Couette flow (shear driven), Poiseuille flow (pressure driven), and flow down an inclined plane. These exact solutions reveal the structure of the equations.

## Common Misconceptions
- The Navier-Stokes equations are not 'solved' in general — the existence and smoothness of solutions in 3D is one of the Millennium Prize Problems.
- The viscous term μ∇²V is only the diffusion of momentum; viscosity also appears in the stress tensor through normal stress terms.
- Dropping the viscous term gives Euler's equations (for inviscid flow), not Bernoulli's equation — Bernoulli requires additional integration along a streamline.
