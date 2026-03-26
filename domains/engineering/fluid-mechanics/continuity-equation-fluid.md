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
- id: conservation-laws-em
  type: hard
- id: conservation-of-mass
  type: hard
- id: conservation-of-linear-momentum
  type: hard
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

## Questions

```yaml
- question: "Water flows steadily through a pipe that narrows from a cross-sectional area of 0.04 m² to 0.01 m². If the inlet velocity is 2 m/s, what is the outlet velocity?"
  type: multiple-choice
  options: ["0.5 m/s", "2 m/s", "4 m/s", "8 m/s"]
  answer: 3
  explanation: "For incompressible steady flow, A₁V₁ = A₂V₂. So V₂ = (A₁/A₂)V₁ = (0.04/0.01)(2) = 8 m/s. The velocity must increase by the area ratio because the same volume of fluid must pass through a smaller opening per unit time."

- question: "Incompressibility (∇·V = 0) is a property of the fluid material itself, meaning mainly liquids like water can satisfy it."
  type: true-false
  answer: false
  explanation: "Incompressibility is a flow assumption, not a material property. Gases — which are physically compressible — can be treated as incompressible when the Mach number is low (roughly Ma < 0.3). At low speeds, density changes in a gas are negligible, and ∇·V = 0 is an excellent approximation. The assumption describes the flow regime, not the fluid."

- question: "What does the condition ∇·V = 0 physically mean for an incompressible velocity field?"
  type: short-answer
  answer: "∇·V = 0 means the velocity field has zero divergence everywhere: there are no sources or sinks of fluid volume. Any fluid element that flows into a control volume must be matched by an equal volume flowing out. Volume is neither created nor destroyed within the flow domain."
  explanation: "The divergence of a vector field measures the net outward flux per unit volume. For incompressible flow, this is zero everywhere, enforcing that mass (and volume, since density is constant) is conserved locally at every point — not just globally across a duct. This constraint severely restricts what velocity fields are physically realizable."
```

## Explainer

Conservation of mass is one of the most fundamental principles in physics, and the continuity equation is simply what this principle looks like when applied to a flowing fluid. The core idea is straightforward: mass cannot appear or disappear. Whatever mass flows into a region must either accumulate there or flow back out. For a steady flow with no accumulation, the mass flowing in must exactly equal the mass flowing out.

The simplest version of this principle is the duct equation A₁V₁ = A₂V₂ for incompressible flow. When a pipe narrows, the velocity must increase because the same volumetric flow rate must pass through a smaller opening — like squeezing a garden hose to make the water spray faster. This result is deceptively powerful: it lets you predict velocity changes across any duct geometry using nothing more than areas, without solving any differential equations.

The differential form ∂ρ/∂t + ∇·(ρV) = 0 is the full statement, valid for compressible, unsteady flows. The term ∂ρ/∂t is the rate of density change at a fixed point; the term ∇·(ρV) is the net mass flux leaving a small control volume. Their sum equals zero because mass is conserved. For incompressible flow (ρ constant), the first term vanishes and we get ∇·V = 0 — the velocity field must be divergence-free everywhere.

A common confusion is treating incompressibility as a property of the fluid rather than the flow. Air is physically compressible, but at wind speeds well below the speed of sound (Mach number below about 0.3), density changes are negligibly small and ∇·V = 0 is an excellent approximation. This is why aerodynamics of slow aircraft and most HVAC engineering can treat air as incompressible. The continuity equation does not determine pressure or individual velocity components on its own; it is one equation in a system that includes the momentum equations (Navier-Stokes). Together they close the problem.
