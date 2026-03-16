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

## Explainer

You already know that electric charge is a conserved property — charge is not created or destroyed, only transferred. Coulomb's law tells you what charge actually *does* to other charge nearby. Two charges exert forces on each other that depend on both their magnitudes and the square of the distance between them. The key features: the force is repulsive for like-sign charges, attractive for opposite-sign charges, and it falls off as 1/r², exactly like gravity (but governed by charge rather than mass). The constant k ≈ 9×10⁹ N·m²/C² tells you that electrostatic forces are enormously strong compared to gravity at atomic scales.

The force is a **vector** — it has both magnitude and direction. The direction is always along the line connecting the two charges. To use Coulomb's law in any real situation, you must treat F as a vector and decompose it into components. This is where your prerequisite skills in vector arithmetic become essential. For a positive test charge, the force from a nearby positive source charge points directly away from that source; from a negative source charge, it points directly toward it.

The **superposition principle** is what makes electrostatics tractable for more than two charges. It states that the total force on any one charge due to multiple other charges equals the vector sum of the individual pairwise forces, calculated as if each other charge were alone. Critically, the presence of charge C does not affect the force between charges A and B — each pair interacts independently. This is a profound and non-obvious claim: electric forces do not saturate or interfere with each other. Superposition is what allows you to build up complex charge distributions piece by piece.

A concrete example: three charges placed at the corners of an equilateral triangle. To find the net force on one of them, you calculate two Coulomb forces (one from each of the other charges), draw them as vectors, and add them head-to-tail. The answer is a single resultant vector. You could not find this answer from one scalar magnitude — the geometry matters completely. This is why learning to decompose vectors into x and y components is a prerequisite skill, not optional bookkeeping. The superposition principle and vector addition together form the complete toolkit for electrostatics with discrete charges, and the same logic will extend directly to continuous charge distributions when you compute electric fields from charge densities.
