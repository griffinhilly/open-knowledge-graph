---
id: electric-potential-definition
title: Electric Potential and Potential Difference
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: gauss-law-problem-solving
  type: hard
- id: line-integrals-scalar
  type: hard
builds-toward:
- potential-energy-systems
- equipotential-surfaces
- relationship-e-field-potential
tags:
- potential
- voltage
- scalar
stage: formal-systems
status: draft
---

# Electric Potential and Potential Difference

## Core Idea
Electric potential V at a point is defined as work per unit charge to bring a test charge from infinity: V = U/q. Potential difference ΔV = V_B − V_A is path-independent and related to work done by the field.

## Questions

```yaml
- question: "Two different paths connect points A and B through an electric field. Along path 1, the work done by the electric force on a 1 μC test charge is 5 μJ. What is the work done along path 2?"
  type: multiple-choice
  options:
    - "It depends on the strength of the electric field along path 2"
    - "5 μJ — the work done by a conservative force is path-independent"
    - "More than 5 μJ, since path 2 is longer"
    - "Less than 5 μJ, since path 2 avoids the strongest field regions"
  answer: 1
  explanation: "The electric force is conservative, meaning the work it does between any two points is independent of the path taken. This is precisely what allows us to define electric potential as a unique scalar value at each point: V(r) = −∫ E · dl, and the result is the same regardless of which path you integrate along. The potential difference ΔV = V_B − V_A encodes this path-independent work per unit charge. Options C and D represent the misconception that path length or field strength along the route determines work."

- question: "A positive charge is placed at a point where the electric potential is high. In which direction will it naturally accelerate?"
  type: multiple-choice
  options:
    - "Toward regions of higher potential, gaining potential energy"
    - "Toward regions of lower potential, converting potential energy to kinetic energy"
    - "In the direction of the electric field, which always points toward higher potential"
    - "It will not accelerate — potential determines energy storage, not force direction"
  answer: 1
  explanation: "A positive charge accelerates toward lower potential — exactly like a ball rolling downhill. The electric field E = −∇V points in the direction of steepest *decrease* in potential, and the force F = qE on a positive charge points in the same direction as E. As the charge moves to lower potential, its potential energy U = qV decreases and its kinetic energy increases. Option C has the direction of E reversed — the field points downhill (toward lower V), not uphill toward higher potential."

- question: "Electric potential is a vector quantity that points in the same direction as the electric field."
  type: true-false
  answer: false
  explanation: "Electric potential V is a scalar — it assigns a single number (in volts) to each point in space, with no directional component. The electric field E is the vector quantity; it points in the direction of steepest decrease in potential and is related to potential by E = −∇V. One of the main advantages of working with potential is that scalars are easier to combine algebraically than vectors — you can add potentials from multiple charges by ordinary addition, without vector decomposition."

- question: "Moving a charge along an equipotential surface requires no work by the electric field."
  type: true-false
  answer: true
  explanation: "An equipotential surface has constant V, so ΔV = 0 for any displacement along it. Since the work by the electric field equals q·ΔV, no work is done. This also means E must be perpendicular to equipotential surfaces everywhere — any component of E parallel to the surface would do work and violate the constant-potential condition. The perpendicularity of E and equipotential surfaces is a geometric consequence of E = −∇V."

- question: "Why is the path-independence of electric potential physically significant, and what property of the electric force makes it possible?"
  type: short-answer
  answer: "Path-independence means the potential difference between two points is a well-defined number, not dependent on how a charge travels between them. This allows us to assign a unique potential value to each point in space — a scalar field — making electrostatics tractable. It is possible because the electric force is conservative, which for Coulomb's law follows from the 1/r² radial dependence: tangential displacement does zero work, so only the radial component matters, and the integral depends only on endpoints."
  explanation: "If the electric force were not conservative, 'potential' would be meaningless — its value would change depending on the route, and equipotential surfaces couldn't be drawn. The conservation follows from Coulomb's law's mathematical form: the force between point charges is always radial (along the line connecting them), so any perpendicular displacement does no work. The deeper mathematical statement is that the curl of E is zero (∇ × E = 0), which is equivalent to saying E can be written as the gradient of a scalar. Gravity has the same structure, which is why gravitational potential energy is also path-independent."
```

## Explainer

From Gauss's law, you know how to find the electric field **E** for symmetric charge distributions. From scalar line integrals, you know how to accumulate a quantity along a path. Electric potential brings these two tools together into something more powerful than working with **E** directly: instead of a vector at every point in space, potential gives you a single **scalar** number at each point, encoding all the same information in a form that is far easier to work with algebraically.

The key definition is V = U/q: the electric potential at a point equals the electric potential energy per unit positive test charge placed there. Equivalently, V(r) = −∫(∞ to r) **E** · d**l**, where you integrate the field along any path from the reference point at infinity to r. The fact that this integral gives the same answer regardless of path taken is not obvious — it follows from the fact that the electric force is **conservative**, a consequence of Coulomb's law having a 1/r² form. You encountered this implicitly when using Gauss's law: the field depends only on radial distance from a point charge, so any tangential displacement does zero work against it.

The practical meaning of potential is this: a positive test charge naturally moves from regions of high potential to low potential, losing potential energy and gaining kinetic energy — exactly like a ball rolling downhill. The "landscape" of potential values in space is a terrain whose hills and valleys tell you which way forces push charges. The potential difference ΔV = V_B − V_A is what matters physically: it is the work per unit charge done by the electric field as a charge moves from A to B. If ΔV is negative (B is at lower potential than A), the field does positive work on a positive charge moving from A to B.

The connection back to **E** is that **E** = −∇V: the electric field points in the direction of steepest decrease in potential, always "downhill" on the potential landscape. **Equipotential surfaces** — surfaces of constant V — are always perpendicular to **E**, because no work is done moving a charge along them. These structures (potential as a scalar landscape, **E** as the gradient pointing downhill) recur throughout electrostatics, capacitance, and eventually quantum mechanics, where the potential energy landscape directly shapes the allowed wavefunctions of bound particles.
