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
- id: partial-derivatives-basics
  type: hard
- id: vector-analysis-and-components
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

## Questions

```yaml
- question: "In the Navier-Stokes momentum equation ρ(DV/Dt) = −∇P + μ∇²V + ρg, which term represents the diffusion of momentum due to fluid viscosity?"
  type: multiple-choice
  options: ["ρ(DV/Dt)", "−∇P", "μ∇²V", "ρg"]
  answer: 2
  explanation: "The term μ∇²V is the viscous diffusion term: it represents how momentum spreads through the fluid due to internal friction between fluid layers. The Laplacian ∇²V is analogous to the diffusion term in the heat equation. −∇P is the pressure force, ρg is the gravitational body force, and ρ(DV/Dt) is mass times acceleration."

- question: "Removing the viscous term μ∇²V from the Navier-Stokes equations directly yields Bernoulli's equation."
  type: true-false
  answer: false
  explanation: "Removing the viscous term gives Euler's equations for inviscid flow: ρ(DV/Dt) = −∇P + ρg. Bernoulli's equation is obtained by a further step: integrating Euler's equations along a streamline under steady, incompressible conditions. Bernoulli is a scalar energy relationship derived from Euler's vector equation, not the equation itself."

- question: "Why do exact analytical solutions to the Navier-Stokes equations exist only for a small class of simple flows?"
  type: short-answer
  answer: "The Navier-Stokes equations are nonlinear partial differential equations due to the convective acceleration term V·∇V in the material derivative. This nonlinearity prevents the superposition of solutions and makes general closed-form solutions impossible. Exact solutions require geometric simplifications (e.g., fully developed channel or pipe flow) that eliminate the nonlinear term."
  explanation: "The convective term V·∇V couples the velocity components together nonlinearly, meaning the equations cannot be solved by standard linear methods. For Couette or Poiseuille flow, the geometry forces the flow to be unidirectional, eliminating the convective acceleration entirely and leaving a linear ODE. In general 3D flow, no such simplification is available, requiring numerical methods (CFD)."
```

## Explainer

You already know Newton's second law: force equals mass times acceleration. The Navier-Stokes equations are precisely this principle applied to a small parcel of viscous fluid. The left-hand side, ρ(DV/Dt), is the mass per unit volume multiplied by the fluid acceleration. The right-hand side is the sum of all forces per unit volume acting on the parcel: pressure gradient, viscous stresses, and body forces like gravity.

The material derivative DV/Dt = ∂V/∂t + (V·∇)V deserves special attention because it is where the physics of fluid flow departs from solid mechanics. For a rigid body, acceleration is straightforward. For a fluid, you must track a parcel as it moves through space, and its acceleration has two parts: the local change at a fixed point (∂V/∂t) and the change due to the parcel moving to a new location with a different velocity (V·∇V). This second term is the convective acceleration, and it makes the equations nonlinear — the source of nearly all the mathematical difficulty in fluid mechanics.

Each term on the right side tells a physical story. The pressure gradient −∇P drives fluid from high pressure to low pressure. The viscous term μ∇²V diffuses momentum from fast-moving regions to slow ones, exactly as heat diffuses from hot to cold. Body forces ρg include gravity and are often negligible in flows dominated by inertia or pressure, but are essential in buoyancy-driven flows. Removing the viscous term gives Euler's equations for inviscid flow; integrating those along a streamline under steady, incompressible conditions gives Bernoulli's equation.

Together with the continuity equation ∇·V = 0 for incompressible flow, the Navier-Stokes equations form a closed system: four equations (three momentum components plus continuity) for four unknowns (three velocity components plus pressure). Exact solutions exist only when the geometry is simple enough to eliminate the nonlinear convective term — Couette flow between parallel plates, Poiseuille flow in a pipe, or flow down an inclined plane. For all other geometries, engineers rely on numerical methods (computational fluid dynamics, or CFD), dimensional analysis, or simplified models like boundary layer theory.
