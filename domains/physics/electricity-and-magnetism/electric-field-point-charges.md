---
id: electric-field-point-charges
title: Electric Field from Point Charges
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: coulomb-law-point-interactions
  type: hard
- id: electric-field-superposition-principle
  type: hard
- id: vector-fields
  type: hard
builds-toward:
- electric-field-continuous-distributions
- electric-flux-and-divergence
tags:
- field
- point-charge
- calculation
stage: formal-systems
status: draft
---

# Electric Field from Point Charges

## Core Idea
The electric field E at position r due to a point charge q is E = kq/r² r̂, where r̂ is the unit vector from the charge. Field strength decreases as inverse square of distance; direction is radially outward for positive charge, inward for negative.

## How It's Best Learned
Plot field lines for single charges, then for multiple charges using superposition. Use field visualization software to develop intuition before calculations.

## Explainer

You already know from Coulomb's law that two charges exert forces on each other. The **electric field** is a conceptual upgrade that separates this interaction into two steps: first, a source charge *creates* a field that fills the surrounding space; second, any other charge placed in that field *feels* a force from the field at its location. The field exists independently — even if there is nothing there to feel it. This two-step picture is more than bookkeeping: it is physically necessary when charges are moving, because changes in the field propagate at the speed of light, not instantaneously.

For a point charge q, the field at position r is **E = kq/r² r̂**, where r̂ is the unit vector pointing away from the charge. The magnitude falls off as 1/r², matching Coulomb's law exactly — which makes sense, since the force on a test charge q₀ is F = q₀E. The direction encodes the sign of the source: positive charges produce field lines radiating outward (they would push a positive test charge away), while negative charges produce field lines pointing inward (a positive test charge would be pulled toward them). Always draw the direction as "what would happen to a positive test charge."

When multiple charges are present, you use the **superposition principle** from your prerequisite: add the vector contributions from each charge independently. This is what makes the electric field framework powerful. To find the field at a point due to three charges, compute three separate field vectors using E = kq/r² r̂ for each charge, then add them as vectors, component by component. The distance r and direction r̂ must be measured from each individual source charge to the field point — a common error is reusing the same r for all charges.

Field lines give a visual summary of the vector field. They point in the direction of E everywhere, their density is proportional to field strength, they begin on positive charges and end on negative charges, and they never cross. For a single positive charge the lines radiate symmetrically in all directions; for a positive–negative pair (a **dipole**) the lines curve from the positive to the negative charge. Visualizing these patterns before computing develops the intuition needed to check whether calculated results are physically reasonable — a calculated field pointing "the wrong way" usually signals a sign or direction error in the vector setup.
