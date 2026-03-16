---
id: potential-flow-theory
title: Potential Flow Theory
domain: engineering
course: fluid-mechanics
prerequisites:
- id: fluid-kinematics
  type: hard
- id: partial-derivatives
  type: hard
- id: gradient-vector
  type: soft
- id: bernoullis-equation
  type: soft
- id: navier-stokes-equations
  type: soft
builds-toward:
- drag-and-lift-aerodynamics
tags:
- potential flow
- irrotational
- stream function
- velocity potential
- superposition
stage: formal-systems
status: validated
---
# Potential Flow Theory

## Core Idea
For irrotational, incompressible flow (∇×V = 0 and ∇·V = 0), the velocity field can be derived from a scalar potential φ: V = ∇φ, where φ satisfies Laplace's equation ∇²φ = 0. A stream function ψ can also be defined such that V = ∇×(ψk̂). Because Laplace's equation is linear, elementary flows (uniform flow, source, sink, doublet, vortex) can be superposed to construct complex flows. Potential flow gives excellent pressure distributions away from walls but fails near boundaries where viscous effects matter.

## How It's Best Learned
Build complex flows by superposing elementary solutions: uniform flow + doublet = flow past a cylinder; add a vortex to get lift. Verify with the Bernoulli equation that the pressure distribution is correct. Note the symmetric pressure distribution for the cylinder case (d'Alembert's paradox: zero drag in potential flow) and discuss why real flows differ.

## Common Misconceptions
- Potential flow is not just 'inviscid flow' — it additionally requires irrotationality. Viscous wakes and boundary layers can produce rotational regions even in high-Re flows.
- d'Alembert's paradox (zero drag in potential flow) seems to contradict reality; real drag comes from viscous effects and the separated wake not captured by potential flow.
- Streamlines and equipotential lines are always orthogonal in 2D potential flow, which helps visualize the flow but can be mistaken for a general truth.

## Explainer

From fluid kinematics you know that the **vorticity** of a flow, ∇×V, describes the local rotation of fluid elements. Setting vorticity to zero — **irrotational flow** — is a strong constraint, but it purchases an enormous simplification: the velocity field can be written as the gradient of a scalar function, V = ∇φ. This **velocity potential** φ plays the same role that gravitational potential plays in mechanics: just as gravitational force is minus the gradient of potential energy, fluid velocity is the gradient of φ. Combining irrotationality with incompressibility (∇·V = 0) yields Laplace's equation ∇²φ = 0 — one of the most studied equations in mathematics, with a vast catalog of known solutions.

The second key function is the **stream function** ψ, defined so that streamlines (paths of constant ψ) coincide with the actual flow paths. In 2D, ψ and φ are related as **conjugate harmonic functions**: ∂φ/∂x = ∂ψ/∂y and ∂φ/∂y = −∂ψ/∂x. This means that lines of constant φ (equipotential lines) are always perpendicular to lines of constant ψ (streamlines), forming an orthogonal grid that is extremely useful for visualizing flow patterns. Together, φ and ψ can be combined into a single **complex potential** w = φ + iψ, which is an analytic function of the complex variable z = x + iy — opening the full power of complex analysis to fluid flow problems.

The reason potential flow is so useful is that **Laplace's equation is linear**: any linear combination of solutions is also a solution. This means you can build complex flows by adding together simple **elementary flows**. The catalog includes uniform flow (φ = Ux), a point source (φ = m ln r / 2π), a doublet (two opposite sources merged in the limit), and a point vortex (φ = Γθ / 2π). Superposing uniform flow and a doublet gives exactly the velocity field for flow past a circular cylinder. Add a vortex of circulation Γ to the cylinder, and the flow develops an asymmetry — the pressure on top and bottom differs, producing a net **lift force** proportional to Γ. This is the Kutta-Joukowski theorem, and it is the foundation of classical airfoil theory.

Once you have the velocity field from φ, you recover pressure using the Bernoulli equation from your prerequisites: p + ½ρV² = constant along any streamline (and throughout the entire potential flow field, since the flow is irrotational). The pressure distribution around the cylinder with no vortex is symmetric fore-and-aft, leading to the famous **d'Alembert's paradox**: potential flow predicts zero drag on any body, which is obviously wrong for real fluids. The paradox is resolved by recognizing what potential flow omits — viscosity, boundary layers, and the separated wake that forms behind bluff bodies. In those regions, vorticity is generated and the irrotational assumption breaks down entirely.

The practical scope of potential flow is thus limited to the region **away from solid boundaries** in high-Reynolds-number flows: in the outer flow far from walls, irrotationality is a good approximation, and potential flow correctly predicts the pressure distribution that drives lift. Near the surface, the viscous boundary layer must be treated separately. This matching of an outer potential solution to an inner viscous solution is the conceptual foundation of boundary layer theory, and understanding where potential flow succeeds and fails is as important as knowing how to compute it.
