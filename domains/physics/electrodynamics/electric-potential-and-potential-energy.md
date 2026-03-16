---
id: electric-potential-and-potential-energy
title: Electric Potential and Potential Energy
domain: physics
course: electrodynamics
prerequisites:
- id: electric-field-and-coulombs-law
  type: hard
- id: multivariable-calculus
  type: hard
builds-toward:
- scalar-and-vector-potentials
- boundary-value-problems-em
tags:
- electrostatics
- potential-theory
- energy
stage: abstract-reasoning
status: draft
---

# Electric Potential and Potential Energy

## Core Idea
Electric potential V is the work per unit charge to bring a test charge from infinity to a point. Potential relates to electric field by E = -∇V. The scalar potential often simplifies calculations compared to working directly with fields.

## Explainer

From Coulomb's law and the electric field concept, you know that a charge Q creates an electric field E = kQ/r² pointing radially outward. Moving a test charge q through this field requires work, and that work depends only on the start and end points — not on the path taken — because the electric force is **conservative**. This path-independence is the key that lets us define a scalar quantity, the **electric potential** V, that fully encodes the energy landscape without keeping track of directions.

The potential V at a point is defined as the work done per unit positive test charge to bring it from a reference point (conventionally infinity, where V = 0) to that point: V = W/q. For a single point charge Q at the origin, V = kQ/r — a simple scalar that falls off as 1/r, in contrast to the electric field which falls off as 1/r² and must be tracked as a vector. The **electric potential energy** of a charge q placed at a location where the potential is V is then U = qV, analogous to gravitational potential energy mgh. Moving the charge from point A to point B changes its potential energy by ΔU = q(V_B − V_A) = −W_by_field, the work done by the field is the negative of the change in potential energy, just as in mechanics.

The connection between potential and field is the gradient relation **E = −∇V**. You learned the gradient from multivariable calculus: ∇V is the vector of partial derivatives (∂V/∂x, ∂V/∂y, ∂V/∂z), pointing in the direction of steepest increase of V. The minus sign means the electric field points in the direction of steepest *decrease* of potential — like water flowing downhill from high to low potential. This is conceptually powerful: if you can find V (a scalar, requiring one calculation instead of three), you can recover E (a vector) by differentiation. For many geometries — especially those with symmetry — finding V by summing kQ/r contributions is far easier than summing vectorial E contributions, and then differentiating gives E.

Surfaces where V = constant are called **equipotential surfaces**, and they are always perpendicular to the electric field lines (since E = −∇V means E is perpendicular to surfaces of constant V). No work is done moving a charge along an equipotential surface. This geometric picture unifies static and dynamic problems: the motion of a charged particle in an electric field is formally identical to the motion of a mass in a gravitational field, with V playing the role of gravitational altitude and qV playing the role of potential energy mgh. This analogy carries forward into boundary value problems, Poisson's equation ∇²V = −ρ/ε₀, and ultimately the four-potential formalism of relativistic electrodynamics.
