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
status: validated
---

# Electric Field from Point Charges

## Core Idea
The electric field E at position r due to a point charge q is E = kq/r² r̂, where r̂ is the unit vector from the charge. Field strength decreases as inverse square of distance; direction is radially outward for positive charge, inward for negative.

## How It's Best Learned
Plot field lines for single charges, then for multiple charges using superposition. Use field visualization software to develop intuition before calculations.

## Questions

```yaml
- question: "Two positive charges +q₁ and +q₂ are separated by 1 meter. A student computes the electric field at the midpoint by finding the magnitudes |E₁| = kq₁/(0.5)² and |E₂| = kq₂/(0.5)², then adds them as scalars. What is wrong with this approach?"
  type: multiple-choice
  options:
    - "She should use r = 1 m (the full separation), not 0.5 m"
    - "She treated the fields as scalars. At the midpoint, E₁ points away from q₁ (toward q₂) and E₂ points away from q₂ (toward q₁) — they point in opposite directions and must be added as vectors, potentially partially or fully canceling"
    - "The formula E = kq/r² applies only to negative charges; for positive charges a different formula is needed"
    - "She should average the fields, not add them, since there are two source charges"
  answer: 1
  explanation: "Electric field contributions from multiple charges must be added as vectors, not scalars. At the midpoint between two positive charges, E₁ points from q₁ toward the midpoint (i.e., in the +x direction if q₂ is to the right), and E₂ points from q₂ toward the midpoint (i.e., in the −x direction). They oppose each other. If q₁ = q₂, the fields cancel exactly and the net field is zero. Adding the magnitudes would give a nonzero answer regardless — the classic error of ignoring direction when applying superposition."

- question: "Which statement best explains why the electric field framework is more than just a notational convenience for restating Coulomb's law?"
  type: multiple-choice
  options:
    - "It simplifies calculations by avoiding the need to track vector directions"
    - "It separates field creation (source charge) from field response (test charge), which becomes physically necessary when charges move — field changes propagate at the speed of light, so the interaction cannot be instantaneous"
    - "It eliminates the need for Coulomb's constant k in calculations involving multiple charges"
    - "It is purely a notational convenience; Coulomb's law and the field description are always physically equivalent"
  answer: 1
  explanation: "For static charges, Coulomb's law and the field description give identical results. But when charges are moving or accelerating, the field picture becomes physically essential: changes in a charge's position create changes in the field that propagate outward at c (the speed of light), not instantaneously. The 'action at a distance' implied by Coulomb's law breaks down. The field is a real physical entity with energy stored in it — not just a bookkeeping device — and this distinction is what leads ultimately to electromagnetic waves and special relativity."

- question: "The electric field at a point in space exists primarily if there is a test charge placed there to detect it."
  type: true-false
  answer: false
  explanation: "The electric field is a property of space itself, created by source charges and existing independently of whether any test charge is present to measure it. We *define* the field in terms of the force it would exert on a hypothetical positive test charge, but that test charge need not actually be there. This field-as-a-physical-entity picture is crucial: it is the field (not the source charges directly) that exerts forces on other charges, and field energy propagates through space even in the absence of charges."

- question: "When computing the electric field at a point due to multiple charges, each charge's vector contribution uses a distance r measured from that specific source charge to the field point."
  type: true-false
  answer: true
  explanation: "This is the most operationally important rule of superposition for electric fields. Each charge 'sees' the field point at its own distance and in its own direction. A common error is to compute |E| using the distance from the first charge and then reuse the same r for all other charges. Each contribution E_i = kq_i/r_i² r̂_i requires its own r_i (distance from charge i to the field point) and its own r̂_i (unit vector pointing from charge i toward the field point). Only after computing all individual vectors are they added component by component."

- question: "Explain why the direction of the electric field is defined as the force on a positive test charge, and what happens to the field direction when the source charge is negative."
  type: short-answer
  answer: "The convention defines E as the force per unit charge that a small positive test charge would experience: E = F/q₀ where q₀ > 0. This means the field direction is 'the way a positive charge would be pushed.' For a positive source charge, the force on a positive test charge is repulsive — pointing away from the source — so E points radially outward. For a negative source charge, the force on a positive test charge is attractive — pointing toward the source — so E points radially inward. The field direction is always defined by the source's sign, regardless of what charge you place there."
  explanation: "Using a positive test charge as the reference is a convention chosen for consistency: the field direction and force direction are identical for positive test charges, and opposite for negative ones. This means field lines tell you exactly which way a positive charge would accelerate. If you place a negative charge q at a point where E points right, the force on it is −qE, which points left — the force and field directions are opposed for negative charges. The field itself hasn't changed; the sign of the responding charge determines whether the force is parallel or antiparallel to E."
```

## Explainer

You already know from Coulomb's law that two charges exert forces on each other. The **electric field** is a conceptual upgrade that separates this interaction into two steps: first, a source charge *creates* a field that fills the surrounding space; second, any other charge placed in that field *feels* a force from the field at its location. The field exists independently — even if there is nothing there to feel it. This two-step picture is more than bookkeeping: it is physically necessary when charges are moving, because changes in the field propagate at the speed of light, not instantaneously.

For a point charge q, the field at position r is **E = kq/r² r̂**, where r̂ is the unit vector pointing away from the charge. The magnitude falls off as 1/r², matching Coulomb's law exactly — which makes sense, since the force on a test charge q₀ is F = q₀E. The direction encodes the sign of the source: positive charges produce field lines radiating outward (they would push a positive test charge away), while negative charges produce field lines pointing inward (a positive test charge would be pulled toward them). Always draw the direction as "what would happen to a positive test charge."

When multiple charges are present, you use the **superposition principle** from your prerequisite: add the vector contributions from each charge independently. This is what makes the electric field framework powerful. To find the field at a point due to three charges, compute three separate field vectors using E = kq/r² r̂ for each charge, then add them as vectors, component by component. The distance r and direction r̂ must be measured from each individual source charge to the field point — a common error is reusing the same r for all charges.

Field lines give a visual summary of the vector field. They point in the direction of E everywhere, their density is proportional to field strength, they begin on positive charges and end on negative charges, and they never cross. For a single positive charge the lines radiate symmetrically in all directions; for a positive–negative pair (a **dipole**) the lines curve from the positive to the negative charge. Visualizing these patterns before computing develops the intuition needed to check whether calculated results are physically reasonable — a calculated field pointing "the wrong way" usually signals a sign or direction error in the vector setup.
