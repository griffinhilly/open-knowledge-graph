---
id: relationship-e-field-potential
title: Relating Electric Field to Potential
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-potential-definition
  type: hard
- id: gradient-vector
  type: hard
builds-toward:
- conductors-electrostatic-behavior
- electric-dipole-moment-field
tags:
- field
- potential
- gradient
stage: formal-systems
status: draft
---

# Relating Electric Field to Potential

## Core Idea
The electric field is the negative gradient of potential: E = −∇V. In one dimension, E_x = −dV/dx, showing field points toward lower potential and has magnitude equal to steepness of V.

## Explainer

You already know two things: the electric potential V at a point is the potential energy per unit charge, and the gradient operator ∇ picks out the direction and rate of steepest increase of a scalar field. The relationship E⃗ = −∇V unifies these: the **electric field** is simply the negative gradient of the electric potential. The negative sign carries the physics — a positive charge spontaneously accelerates from high potential to low potential, just as a ball rolls downhill, so the force (and field) points in the direction of *decreasing* V.

In one dimension this is especially transparent: E_x = −dV/dx. If you plot voltage versus position along a line, the electric field at any point is the negative slope of that plot. Where V drops steeply, E is large; where V is flat (an equipotential region), E is zero. This is the calculus you already know from the derivative — the field is the spatial rate of change of potential, with a sign flip. In conductors at electrostatic equilibrium, the interior is an equipotential volume (all of the surface and interior is at the same V), and sure enough, the electric field inside an ideal conductor is zero.

In three dimensions, ∇V is a vector pointing in the direction in which V increases most rapidly. The field E⃗ = −∇V therefore points *perpendicular* to the equipotential surfaces, in the direction of steepest descent. This is why equipotential lines and field lines are always perpendicular to each other on field diagrams. The topology of the potential surface completely determines the field: steep hillsides correspond to strong fields, gentle slopes to weak ones.

The inverse relationship — recovering V from E⃗ — requires integration: V(b) − V(a) = −∫_a^b E⃗·dl⃗. This line integral is path-independent for electrostatic fields (because ∇ × E⃗ = 0 in electrostatics), which is why the potential is well-defined as a scalar function. In practice, it is often much easier to calculate V by summing scalar contributions from each charge and then differentiate to get E⃗, rather than computing the vector field directly. This strategy — work in potentials, convert to fields at the end — is the computational workhorse of electrostatics and will remain essential through boundary-value problems and the theory of conductors.
