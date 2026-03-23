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
status: validated
---

# Relating Electric Field to Potential

## Core Idea
The electric field is the negative gradient of potential: E = −∇V. In one dimension, E_x = −dV/dx, showing field points toward lower potential and has magnitude equal to steepness of V.

## Questions

```yaml
- question: "A student maps the potential around a charge distribution and concludes that the electric field at every point must point toward the region of highest potential, since 'field lines go toward strong sources.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — the electric field always points toward high potential"
    - "The electric field points in the direction of steepest decrease in potential (away from high V, toward low V) — the negative sign in E = −∇V reverses the gradient direction"
    - "The electric field is perpendicular to the potential gradient and has no component toward high or low potential"
    - "The electric field direction depends only on the sign of the source charge, not on the potential"
  answer: 1
  explanation: "The negative sign in E⃗ = −∇V is the critical physics. The gradient ∇V points in the direction of steepest increase of V, but the field is the negative gradient — it points toward lower potential. A positive test charge spontaneously accelerates from high V to low V, gaining kinetic energy as it loses potential energy, just as a ball rolls downhill. The field points 'downhill' on the potential surface, not uphill."

- question: "On a field diagram, an equipotential line is drawn through a region. What must be true about electric field lines in that region?"
  type: multiple-choice
  options:
    - "Electric field lines run parallel to the equipotential line, since they trace the same potential"
    - "Electric field lines are perpendicular to the equipotential line, crossing it at right angles"
    - "There are no electric field lines where an equipotential exists"
    - "Electric field lines and equipotential lines are the same thing labeled differently"
  answer: 1
  explanation: "Since E⃗ = −∇V and the gradient of V is always perpendicular to the level surfaces of V (the equipotentials), the field must be perpendicular to the equipotentials. If the field had any component along an equipotential surface, it would do work on a charge moving along that surface — but a charge moving along an equipotential does zero work by definition (ΔV = 0). Therefore the field can only be perpendicular to equipotential surfaces, never parallel."

- question: "If the electric potential is constant throughout a region of space, the electric field in that region is zero."
  type: true-false
  answer: true
  explanation: "E⃗ = −∇V. If V is constant, its gradient is zero in all directions, so E⃗ = 0. This is exactly what happens inside an ideal conductor at electrostatic equilibrium: the entire conductor (interior and surface) is at the same potential, so the internal field vanishes. Any non-zero field inside would accelerate free charges until they redistributed to eliminate the field — which is why equilibrium requires E = 0 inside."

- question: "A positive test charge placed in an electric field will naturally accelerate from regions of low electric potential toward regions of high electric potential."
  type: true-false
  answer: false
  explanation: "A positive charge accelerates from high potential to low potential. The electric force on a positive charge is F⃗ = qE⃗ = q(−∇V), pointing in the direction of decreasing V. This is analogous to gravity: a positive potential energy corresponds to a high position, and objects spontaneously move to lower potential energy. Moving from high V to low V decreases the electric potential energy (U = qV for positive q), so the charge gains kinetic energy — the motion is spontaneous in that direction, not the reverse."

- question: "A positive charge is released from rest in a non-uniform electric field. Describe the relationship between the potential at its starting point and the direction it moves. Why does the negative sign in E⃗ = −∇V matter physically, not just mathematically?"
  type: short-answer
  answer: "The charge accelerates toward lower potential. The negative sign means the field points in the direction of decreasing V — down the potential gradient, like a ball rolling downhill. Physically, the sign encodes the fact that a positive charge loses potential energy (U = qV) as it moves to lower V, and this loss becomes kinetic energy. Without the negative sign, the math would say the field points up the potential hill, which would predict spontaneous acceleration toward higher potential energy — violating conservation of energy."
  explanation: "Students often treat E⃗ = −∇V as a formula to memorize without grasping why the sign is there. The physical content is: positive charges roll downhill in potential, just as masses roll downhill in gravitational potential. The gradient ∇V points uphill; the field (−∇V) points downhill. This is why the sign matters: it determines the direction of force and therefore the direction of motion, not just the magnitude of the field."
```

## Explainer

You already know two things: the electric potential V at a point is the potential energy per unit charge, and the gradient operator ∇ picks out the direction and rate of steepest increase of a scalar field. The relationship E⃗ = −∇V unifies these: the **electric field** is simply the negative gradient of the electric potential. The negative sign carries the physics — a positive charge spontaneously accelerates from high potential to low potential, just as a ball rolls downhill, so the force (and field) points in the direction of *decreasing* V.

In one dimension this is especially transparent: E_x = −dV/dx. If you plot voltage versus position along a line, the electric field at any point is the negative slope of that plot. Where V drops steeply, E is large; where V is flat (an equipotential region), E is zero. This is the calculus you already know from the derivative — the field is the spatial rate of change of potential, with a sign flip. In conductors at electrostatic equilibrium, the interior is an equipotential volume (all of the surface and interior is at the same V), and sure enough, the electric field inside an ideal conductor is zero.

In three dimensions, ∇V is a vector pointing in the direction in which V increases most rapidly. The field E⃗ = −∇V therefore points *perpendicular* to the equipotential surfaces, in the direction of steepest descent. This is why equipotential lines and field lines are always perpendicular to each other on field diagrams. The topology of the potential surface completely determines the field: steep hillsides correspond to strong fields, gentle slopes to weak ones.

The inverse relationship — recovering V from E⃗ — requires integration: V(b) − V(a) = −∫_a^b E⃗·dl⃗. This line integral is path-independent for electrostatic fields (because ∇ × E⃗ = 0 in electrostatics), which is why the potential is well-defined as a scalar function. In practice, it is often much easier to calculate V by summing scalar contributions from each charge and then differentiate to get E⃗, rather than computing the vector field directly. This strategy — work in potentials, convert to fields at the end — is the computational workhorse of electrostatics and will remain essential through boundary-value problems and the theory of conductors.
