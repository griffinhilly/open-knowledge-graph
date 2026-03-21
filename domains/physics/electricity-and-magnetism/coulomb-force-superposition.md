---
id: coulomb-force-superposition
title: Coulomb Force and Superposition
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: conservation-of-electric-charge
  type: soft
builds-toward:
- electric-field-from-distributions
tags:
- coulomb
- force
- superposition
stage: formal-systems
status: draft
---

# Coulomb Force and Superposition

## Core Idea
Coulomb's law describes the electrostatic force between two point charges as F = kq₁q₂/r², directed along the line connecting them. For multiple charges, the net force is the vector sum of pairwise forces—the superposition principle. This linear property of Coulomb's law is fundamental to all electromagnetic phenomena.

## Questions

```yaml
- question: "Three charges A, B, and C are placed in space. A new charge D is added nearby. How does adding D affect the force between A and B?"
  type: multiple-choice
  options:
    - "D's electric field partially screens A and B, reducing the force between them"
    - "Adding D increases the total electric field in the region, increasing the force between A and B"
    - "The force between A and B is unchanged — each pair interacts independently by the superposition principle"
    - "It depends on whether D has the same or opposite sign as A and B"
  answer: 2
  explanation: "The superposition principle states that the force between any two charges is completely independent of all other charges. Charge D contributes its own forces on A and on B, but it does not alter the A-B interaction in any way. Superposition means forces add linearly — D's presence doesn't screen, amplify, or modify the pairwise A-B force. This non-obvious independence is what makes electrostatics tractable: you can analyze each pair separately and add the results."

- question: "A positive charge Q is placed at the origin. A positive test charge q is placed to its right. Which of the following correctly describes the force on q?"
  type: multiple-choice
  options:
    - "A scalar magnitude F = kQq/r² directed toward Q, since opposite charges attract"
    - "A vector of magnitude kQq/r² pointing to the right, away from Q, since like charges repel"
    - "A vector of magnitude kQq/r² pointing to the left, toward Q, since the field pulls inward"
    - "A scalar F = kQq/r² with no direction, since the charges are stationary"
  answer: 1
  explanation: "Coulomb's law gives a vector force. Like charges (both positive) repel, so the force on q points away from Q — to the right. The magnitude is kQq/r². Option A has the direction wrong (that would be attraction between opposite charges). Option D treats the force as a scalar, which is incorrect — direction is essential for computing net forces when multiple charges are present. Option C would apply to opposite-sign charges."

- question: "The superposition principle implies that when computing the net force on a charge due to three others, you must add the three Coulomb forces as vectors, not as scalar magnitudes."
  type: true-false
  answer: true
  explanation: "Force is a vector quantity with both magnitude and direction. Three forces on the same charge generally point in different directions; adding their magnitudes gives the wrong answer except in special symmetric cases. You must decompose each force into x and y (and z) components, sum the components, and reconstruct the resultant vector. This is not optional bookkeeping — it is the only physically correct procedure. The superposition principle says the interactions are independent; vector addition is how you combine them into a net result."

- question: "Coulomb's law predicts that doubling the distance between two charges doubles the force between them."
  type: true-false
  answer: false
  explanation: "Coulomb's law is an inverse-square law: F = kq₁q₂/r². Doubling the distance (r → 2r) gives F ∝ 1/(2r)² = 1/(4r²), so the force decreases by a factor of 4, not 2. This 1/r² dependence, the same as gravity, means electrostatic forces fall off rapidly with distance. Confusing inverse-square with inverse-linear is a common error — the exponent on r in the denominator is 2, not 1."

- question: "Why must Coulomb forces be treated as vectors rather than scalars when finding the net force on a charge from multiple sources?"
  type: short-answer
  answer: "Each Coulomb force has a direction determined by the line connecting the two charges involved. When multiple forces act on the same charge from different directions, adding their magnitudes (scalar addition) ignores directionality and gives a physically wrong result. The correct procedure is vector addition: decompose each force into components, sum each component independently, and reconstruct the net force. The geometry of where the source charges are located determines the directions, which can cause forces to partially cancel or reinforce depending on angles."
  explanation: "The point of vector addition is that forces in perpendicular directions don't interfere — a 3 N force eastward and a 4 N force northward produce a 5 N force to the northeast, not a 7 N force in some vague direction. Scalar addition would give 7 N, which is wrong. In electrostatics, charge positions determine force directions, and those directions are almost never aligned — so vector decomposition is always necessary."
```

## Explainer

You already know that electric charge is a conserved property — charge is not created or destroyed, only transferred. Coulomb's law tells you what charge actually *does* to other charge nearby. Two charges exert forces on each other that depend on both their magnitudes and the square of the distance between them. The key features: the force is repulsive for like-sign charges, attractive for opposite-sign charges, and it falls off as 1/r², exactly like gravity (but governed by charge rather than mass). The constant k ≈ 9×10⁹ N·m²/C² tells you that electrostatic forces are enormously strong compared to gravity at atomic scales.

The force is a **vector** — it has both magnitude and direction. The direction is always along the line connecting the two charges. To use Coulomb's law in any real situation, you must treat F as a vector and decompose it into components. This is where your prerequisite skills in vector arithmetic become essential. For a positive test charge, the force from a nearby positive source charge points directly away from that source; from a negative source charge, it points directly toward it.

The **superposition principle** is what makes electrostatics tractable for more than two charges. It states that the total force on any one charge due to multiple other charges equals the vector sum of the individual pairwise forces, calculated as if each other charge were alone. Critically, the presence of charge C does not affect the force between charges A and B — each pair interacts independently. This is a profound and non-obvious claim: electric forces do not saturate or interfere with each other. Superposition is what allows you to build up complex charge distributions piece by piece.

A concrete example: three charges placed at the corners of an equilateral triangle. To find the net force on one of them, you calculate two Coulomb forces (one from each of the other charges), draw them as vectors, and add them head-to-tail. The answer is a single resultant vector. You could not find this answer from one scalar magnitude — the geometry matters completely. This is why learning to decompose vectors into x and y components is a prerequisite skill, not optional bookkeeping. The superposition principle and vector addition together form the complete toolkit for electrostatics with discrete charges, and the same logic will extend directly to continuous charge distributions when you compute electric fields from charge densities.
