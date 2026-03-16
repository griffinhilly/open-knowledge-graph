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
stage: abstract-reasoning
status: draft
---

# Electric Field and Coulomb's Law

## Core Idea
Coulomb's law describes the electrostatic force between two point charges as inversely proportional to the square of their separation. The electric field E is defined as the force per unit charge and satisfies superposition. Understanding the electric field as a fundamental entity allows treatment of distributed charges and is the foundation for all classical electromagnetism.

## How It's Best Learned
Start with Coulomb's law for point charges and visualize field lines. Use symmetry arguments and Gauss's law for extended charge distributions. Practice calculating fields for spheres, infinite planes, and line charges.

## Common Misconceptions
Confusing electric field (force per unit charge) with potential (energy per unit charge). Field lines are not particles but representations of field strength and direction.

## Explainer

From classical mechanics, you know Newton's law: force causes acceleration, and forces between objects act along the line connecting them. Coulomb's law follows this template: two point charges q₁ and q₂ separated by distance r attract or repel with force **F** = k q₁q₂/r² r̂, where k = 1/(4πε₀) ≈ 9 × 10⁹ N·m²/C² and r̂ is the unit vector pointing from one charge to the other. Like charges repel; unlike charges attract. The inverse-square form mirrors gravity, but with charges replacing masses and far greater typical magnitudes (electrostatic forces dominate over gravity at atomic scales by roughly 10³⁹).

The concept of the **electric field** E is the critical abstraction that takes you beyond two-body interactions. Instead of always asking "what force does charge A exert on charge B?", define the field **E**(**r**) as the force that would be experienced by a unit positive test charge placed at position **r**, due to all other charges in the system. For a point charge Q: **E** = k Q/r² r̂. Now the field is a property of space itself — it exists everywhere, regardless of whether a test charge is present. The force on any charge q placed in the field is simply **F** = q**E**. This split into "source creates field, field acts on test charge" is not mere bookkeeping; it becomes essential when fields carry energy, propagate as waves, and exist independently of the charges that created them.

**Superposition** is the property that makes the field concept powerful. The total electric field at a point is the vector sum of contributions from every source charge: **E**_total = **E**₁ + **E**₂ + .... For continuous distributions (a charged rod, a disk, a volume), the sum becomes an integral. Your background in multivariable calculus is indispensable here: you integrate infinitesimal charge elements dq over the source distribution, each contributing d**E** = k dq/r² r̂ to the field at the observation point. The direction of each contribution depends on where dq sits relative to the observation point, so these are *vector* integrals — you integrate x, y, and z components separately.

**Electric field lines** are a visualization tool: they start on positive charges, end on negative charges, and are drawn so that the local tangent gives the field direction and the line density indicates field strength. Crucially, field lines never cross — at any given point there is only one field direction. For a single positive charge, the lines radiate outward uniformly in all directions (the inverse-square law makes the density fall as 1/r², matching the spreading area). For two opposite charges, the lines arc from positive to negative, sketching out the familiar dipole pattern. These pictures are not optional decoration; they train the spatial intuition that later carries into Gauss's law, where the total number of field lines through a closed surface tells you the total charge enclosed.
