---
id: rhombus-properties
title: Rhombus Properties
domain: mathematics
course: geometry
prerequisites:
  - id: parallelogram-properties
    type: hard
builds-toward:
  - coordinate-geometry-proofs
tags: [quadrilaterals, rhombus, properties, diagonals]
stage: abstract-reasoning
status: validated
---

# Rhombus Properties

## Core Idea
A rhombus is a parallelogram with four congruent sides. It inherits all parallelogram properties and adds: diagonals are perpendicular and each diagonal bisects a pair of opposite angles. Conversely, if a parallelogram has perpendicular diagonals, it is a rhombus. The area of a rhombus equals half the product of its diagonals.

## How It's Best Learned
Build on parallelogram properties. Prove perpendicularity of diagonals using congruent triangles (SSS with all sides equal). Show that each diagonal is an angle bisector. Practice computing area using diagonals. Compare and contrast with rectangles and squares in the quadrilateral hierarchy.

## Common Misconceptions
- Thinking a rhombus must have acute and obtuse angles (a square is a special rhombus with right angles).
- Confusing the diagonal properties of rhombuses (perpendicular) with those of rectangles (congruent).
- Forgetting that a rhombus is always a parallelogram.

## Explainer

A **rhombus** is a parallelogram with one additional constraint: all four sides are equal in length. From your study of parallelograms, you already know that opposite sides are parallel and equal, opposite angles are equal, consecutive angles are supplementary, and the diagonals bisect each other. The rhombus inherits all of these properties — it is a specialization of the parallelogram, not a different kind of figure. The key question is: what does adding "all four sides equal" buy you beyond the parallelogram properties?

The answer is perpendicular diagonals. Here is why: label the rhombus ABCD and let the diagonals intersect at point E. Consider triangles ABE and ADE. Side AB = AD (all sides of a rhombus are equal), side AE = AE (shared), and side BE = DE (diagonals bisect each other, which you know from parallelogram properties). By SSS congruence, triangles ABE and ADE are congruent. Since the angles at E are supplementary (they form a straight line) and equal (by congruence), each must be 90°. This is the complete proof: equal sides force the diagonals to meet at right angles.

A second consequence of equal sides is that each **diagonal bisects the opposite vertex angles**. The diagonal AC, for instance, divides angle A into two equal parts. This follows from the same SSS congruence argument: since triangles ABC and ADC are congruent (all three sides equal), the angles at A must split equally. Think of each diagonal as a line of symmetry — the rhombus is symmetric about each of its diagonals, which explains both the angle bisection and the perpendicularity simultaneously.

The **area formula** area = (1/2)d₁d₂ comes directly from the perpendicular diagonals. The two diagonals divide the rhombus into four right triangles. Each right triangle has legs d₁/2 and d₂/2, so its area is (1/2)(d₁/2)(d₂/2) = d₁d₂/8. Four such triangles give total area 4 × d₁d₂/8 = d₁d₂/2. To keep the quadrilateral hierarchy clear: every square is a rhombus (all sides equal, all angles 90°), every rhombus is a parallelogram, but a rhombus with a right angle is necessarily a square. The rhombus and rectangle are "cousins" in the parallelogram family — the rhombus specializes on equal sides; the rectangle specializes on equal angles (right angles). The square is their intersection.
