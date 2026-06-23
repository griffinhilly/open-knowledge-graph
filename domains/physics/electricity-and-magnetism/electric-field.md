---
id: electric-field
title: Electric Field
domain: physics
course: electricity-and-magnetism
prerequisites:
- id: electric-charge-and-coulombs-law
  type: hard
- id: vectors-in-two-dimensions
  type: hard
- id: vector-fields
  type: soft
- id: electric-fields-intro
  type: soft
builds-toward:
- electric-flux
- electric-potential
- gauss-law
tags:
- electric-field
- field-lines
- superposition
- electrostatics
stage: formal-systems
status: validated
---

# Electric Field

## Core Idea
The electric field E at a point in space is defined as the force per unit positive test charge placed at that point: E = F/q. It is a vector field, meaning it has both magnitude and direction at every location. For a point charge Q, E = kQ/r² directed radially outward (for positive Q). The superposition principle allows the total field from multiple charges to be found by vector addition of individual contributions.

## How It's Best Learned
Draw field vectors at several points around simple charge distributions before moving to field-line diagrams. Work problems computing E at specific points before tackling more abstract questions about field patterns.

## Common Misconceptions
- The electric field exists independently of any test charge — it is a property of space created by source charges.
- Field lines never cross; if they did, the field would have two directions at one point.
- A uniform field (like between parallel plates) does not mean the charges are at rest.

## Questions

```yaml
- question: "A positive test charge of 2 μC placed at a point experiences a force of 8 N to the right. If the test charge is replaced with a 4 μC charge at the same point, what is the electric field at that point?"
  type: multiple-choice
  options: ["16 N/C to the right", "4 N/C to the right", "4 × 10⁶ N/C to the right", "The field doubles to 8 × 10⁶ N/C"]
  answer: 1
  explanation: "E = F/q = 8 N / (2 × 10⁻⁶ C) = 4 × 10⁶ N/C. With the 4 μC charge, F = 16 N, but E = 16 N / (4 × 10⁻⁶ C) = 4 × 10⁶ N/C — unchanged. The electric field is a property of the space created by source charges, not of the test charge placed there. Doubling the test charge doubles the force but the ratio F/q stays constant."

- question: "Removing most test charges from a region of space eliminates the electric field that existed there."
  type: true-false
  answer: false
  explanation: "The electric field exists independently of any test charge — it is a property of space created by the source charges. The test charge is only a conceptual probe to measure the field; its absence does not change the field. This is one of the most important conceptual shifts in moving from Coulomb's law to the field concept."

- question: "Two equal positive charges are placed 10 cm apart. Describe the direction of the electric field at the exact midpoint between them."
  type: short-answer
  answer: "The electric field at the midpoint is zero. The field from the left charge points to the right (away from positive), and the field from the right charge points to the left (away from positive). The two contributions are equal in magnitude and opposite in direction, so they cancel by vector superposition."
  explanation: "This question tests whether students can apply the superposition principle as a vector sum rather than a scalar sum. Each charge contributes a field at the midpoint, but because the charges are equal and the distances are equal, the magnitudes are the same while the directions are opposite — they sum to zero."
```

## Explainer

From Coulomb's law you know that two charges exert forces on each other: F = kQq/r². But this framing has a subtle problem — it suggests that charges act on each other directly across empty space, which puzzled physicists for centuries. The electric field concept reframes this: instead of saying charge Q pushes on charge q, we say charge Q *creates a field throughout space*, and that field then acts locally on q. The field is real and exists whether or not there is anything to feel it.

Formally, the electric field E at a point is defined as the force a positive test charge would experience *per unit charge* if placed there: **E = F/q**. The test charge is conceptual — a hypothetical +1 C probe. If a real +2 μC charge at a point experiences 8 N to the right, the field there is 8/2×10⁻⁶ = 4×10⁶ N/C to the right. Crucially, that field value does not depend on the test charge you use to measure it. Double the test charge, the force doubles, but E = F/q stays constant. The field is a property of the location, created by the source charges.

For a single point charge Q, the field at distance r is **E = kQ/r²**, directed radially outward if Q is positive and inward if Q is negative. Notice the structural similarity to Coulomb's law — E just replaces F/q, with q factored out. This means you already know how E falls off with distance (inverse-square) and how it depends on the source charge.

When multiple source charges are present, the **superposition principle** lets you find the total field by vector addition. Each source charge contributes its own field independently; you add the vectors. This is why the field at the exact midpoint between two equal positive charges is zero — the rightward field from the left charge and the leftward field from the right charge cancel perfectly. Always treat this as vector addition, not scalar addition, or you will get wrong answers whenever contributions point in different directions.

Field lines are a visualization tool for understanding field patterns. They point in the direction a positive test charge would move, and their density indicates field strength. Two rules follow from the field's mathematical properties: field lines start on positive charges and end on negative charges, and they never cross (because the field has exactly one direction at every point). These patterns will become critical when you reach Gauss's law and electric potential, where the geometry of field lines carries quantitative information.
