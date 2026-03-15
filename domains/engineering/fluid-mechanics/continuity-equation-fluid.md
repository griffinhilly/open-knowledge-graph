---
id: continuity-equation-fluid
title: The Continuity Equation (Conservation of Mass)
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-kinematics
  type: hard
- id: double-integrals-cartesian
  type: soft
- id: divergence-theorem
  type: soft
- id: partial-derivatives
  type: soft
builds-toward:
- bernoullis-equation
- navier-stokes-equations
- control-volume-momentum
- flow-measurement-methods
tags:
- conservation of mass
- continuity
- control volume
- incompressible flow
stage: formal-systems
status: validated
---

# The Continuity Equation (Conservation of Mass)

## Core Idea
The continuity equation expresses conservation of mass for a fluid: ∂ρ/∂t + ∇·(ρV) = 0. For incompressible flow (ρ constant), this reduces to ∇·V = 0, meaning the velocity field is divergence-free. In its integral form for a control volume, the net mass flux out equals the rate of decrease of mass inside: d/dt∫∫∫ρ dV + ∫∫ρV·n̂ dA = 0. For simple duct flows with uniform inlet/outlet, this reduces to the familiar A₁V₁ = A₂V₂.

## How It's Best Learned
Start with the simple duct form A₁V₁ = A₂V₂ to build intuition about flow speeding up in constrictions. Then derive the differential form from the integral form using the divergence theorem. Apply to branching pipe networks and verify mass balance.

## Common Misconceptions
- Incompressibility (∇·V = 0) is a flow assumption, not a material property — gases can often be treated as incompressible at low Mach numbers.
- Continuity constrains velocity, not pressure; pressure enters through the momentum equation.
- The average velocity times area gives volume flow rate only when the velocity is uniform across the cross-section; otherwise, integration is needed.
