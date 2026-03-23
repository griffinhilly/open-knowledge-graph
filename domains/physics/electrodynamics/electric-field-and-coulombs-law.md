---
id: electric-field-and-coulombs-law
title: Electric Field and Coulomb's Law
domain: physics
course: electrodynamics
prerequisites:
- id: multivariable-calculus
  type: hard
- id: classical-mechanics
  type: soft
builds-toward:
- electric-potential-and-potential-energy
- electric-flux-and-gauss-law
tags:
- electrostatics
- field-theory
- forces
stage: expert
status: validated
---

# Electric Field and Coulomb's Law

## Core Idea
Coulomb's law describes the electrostatic force between two point charges as inversely proportional to the square of their separation. The electric field E is defined as the force per unit charge and satisfies superposition. Understanding the electric field as a fundamental entity allows treatment of distributed charges and is the foundation for all classical electromagnetism.

## How It's Best Learned
Start with Coulomb's law for point charges and visualize field lines. Use symmetry arguments and Gauss's law for extended charge distributions. Practice calculating fields for spheres, infinite planes, and line charges.

## Common Misconceptions
Confusing electric field (force per unit charge) with potential (energy per unit charge). Field lines are not particles but representations of field strength and direction.

## Questions

```yaml
- question: "A source charge Q = +4 μC is fixed in space. A test charge q = +2 μC is placed 0.3 m away. What does the electric field E at that location represent?"
  type: multiple-choice
  options:
    - "The total electrostatic force on the test charge q"
    - "The force per unit positive test charge — a property of that point in space, independent of q"
    - "The potential energy stored between Q and q"
    - "The force multiplied by the distance between Q and q"
  answer: 1
  explanation: "The electric field E at a point is defined as the force per unit positive test charge: E = F/q. It is a property of that location in space due to the source charges, independent of whatever test charge you place there. The actual force on a specific charge q is F = qE. Confusing 'field' with 'force on a specific charge' misses the key abstraction: the field exists everywhere in space whether or not a test charge is present, and tells you what force any charge placed there would experience."

- question: "Two electric field lines are drawn crossing at a point in a diagram. What does this indicate?"
  type: multiple-choice
  options:
    - "The field is especially strong at that point"
    - "A charge must be located precisely at the crossing point"
    - "This is impossible — field lines never cross because the field has only one direction at each point"
    - "The two field lines originated from charges of opposite sign"
  answer: 2
  explanation: "Electric field lines never cross because the electric field has a unique direction at every point in space. If two lines crossed, the field at that intersection would have two directions simultaneously — a physical contradiction. The field direction at any point is determined by the vector sum of contributions from all source charges (superposition), which always yields exactly one resultant vector. Crossing field lines indicate an error in the drawing, not a real phenomenon."

- question: "The electric field at a point in space exists only when a test charge is physically present there to experience it."
  type: true-false
  answer: false
  explanation: "The electric field is a property of space itself, created by source charges, and exists at every point regardless of whether a test charge is present. This is the key conceptual shift in field theory: instead of treating interactions as direct action-at-a-distance between charges, the source charge creates a field throughout space, and any charge placed in that field experiences a force. The field is real — it carries energy and momentum — not just a bookkeeping device. This becomes essential later when fields propagate as electromagnetic waves, entirely independent of the charges that created them."

- question: "The electric potential at a point and the electric field at that point both measure the same physical quantity, expressed in different units."
  type: true-false
  answer: false
  explanation: "Electric field E is force per unit charge (N/C, equivalently V/m). Electric potential V is potential energy per unit charge (volts = J/C). They are related — E = −∇V — but they are fundamentally different quantities. The field is a vector (direction matters); the potential is a scalar. Confusing them is one of the most common errors in introductory electromagnetism. A region can have a nonzero potential but zero field (e.g., inside a conductor at equilibrium), and vice versa. Keeping force and energy clearly distinct is the prerequisite for understanding both."

- question: "Why is the concept of the electric field — rather than simply applying Coulomb's law between pairs of charges — essential for describing electromagnetic phenomena?"
  type: short-answer
  answer: "Coulomb's law only describes the force between two isolated point charges. The electric field concept enables superposition: the total field at any point equals the vector sum of contributions from every source charge, turning multi-charge problems into tractable calculations. For continuous charge distributions, this sum becomes a vector integral. More fundamentally, the field is an entity that exists independently of test charges, carries energy, and propagates at the speed of light as an electromagnetic wave. The field picture is the correct framework for radiation, relativity, and ultimately quantum electrodynamics — none of which can be described by direct action-at-a-distance."
  explanation: "The 'action-at-a-distance' picture (charge A directly pushes charge B) works for static point charges but breaks down when charges accelerate and when fields propagate through vacuum. The field is the intermediary that makes the causal chain local: the source creates the field, the field travels through space, and the field acts on the test charge. This locality is what makes the theory compatible with special relativity."
```

## Explainer

From classical mechanics, you know Newton's law: force causes acceleration, and forces between objects act along the line connecting them. Coulomb's law follows this template: two point charges q₁ and q₂ separated by distance r attract or repel with force **F** = k q₁q₂/r² r̂, where k = 1/(4πε₀) ≈ 9 × 10⁹ N·m²/C² and r̂ is the unit vector pointing from one charge to the other. Like charges repel; unlike charges attract. The inverse-square form mirrors gravity, but with charges replacing masses and far greater typical magnitudes (electrostatic forces dominate over gravity at atomic scales by roughly 10³⁹).

The concept of the **electric field** E is the critical abstraction that takes you beyond two-body interactions. Instead of always asking "what force does charge A exert on charge B?", define the field **E**(**r**) as the force that would be experienced by a unit positive test charge placed at position **r**, due to all other charges in the system. For a point charge Q: **E** = k Q/r² r̂. Now the field is a property of space itself — it exists everywhere, regardless of whether a test charge is present. The force on any charge q placed in the field is simply **F** = q**E**. This split into "source creates field, field acts on test charge" is not mere bookkeeping; it becomes essential when fields carry energy, propagate as waves, and exist independently of the charges that created them.

**Superposition** is the property that makes the field concept powerful. The total electric field at a point is the vector sum of contributions from every source charge: **E**_total = **E**₁ + **E**₂ + .... For continuous distributions (a charged rod, a disk, a volume), the sum becomes an integral. Your background in multivariable calculus is indispensable here: you integrate infinitesimal charge elements dq over the source distribution, each contributing d**E** = k dq/r² r̂ to the field at the observation point. The direction of each contribution depends on where dq sits relative to the observation point, so these are *vector* integrals — you integrate x, y, and z components separately.

**Electric field lines** are a visualization tool: they start on positive charges, end on negative charges, and are drawn so that the local tangent gives the field direction and the line density indicates field strength. Crucially, field lines never cross — at any given point there is only one field direction. For a single positive charge, the lines radiate outward uniformly in all directions (the inverse-square law makes the density fall as 1/r², matching the spreading area). For two opposite charges, the lines arc from positive to negative, sketching out the familiar dipole pattern. These pictures are not optional decoration; they train the spatial intuition that later carries into Gauss's law, where the total number of field lines through a closed surface tells you the total charge enclosed.
