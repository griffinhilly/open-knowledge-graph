---
id: rectangle-properties
title: Rectangle Properties
domain: mathematics
course: geometry
prerequisites:
  - id: parallelogram-properties
    type: hard
builds-toward:
  - coordinate-geometry-proofs
tags: [quadrilaterals, rectangles, properties, diagonals]
stage: abstract-reasoning
status: validated
---

# Rectangle Properties

## Core Idea
A rectangle is a parallelogram with four right angles. It inherits all parallelogram properties and adds: diagonals are congruent. Conversely, if a parallelogram has congruent diagonals, it is a rectangle. A rectangle is the intersection of the parallelogram and right-angle conditions.

## How It's Best Learned
Start from the parallelogram properties and add the right-angle condition. Prove that diagonals are congruent using congruent triangles (SAS with right angles). Practice identifying rectangles from given properties. Use coordinate geometry to verify: show a quadrilateral is a parallelogram (midpoints of diagonals coincide) and has a right angle (perpendicular sides via slopes).

## Common Misconceptions
- Thinking a square is not a rectangle (it is; a square is a special rectangle with all sides equal).
- Assuming the diagonals of a rectangle are perpendicular (they are not, unless it is also a square).
- Forgetting to prove the parallelogram condition first before using the diagonal criterion.

## Explainer

Because you have already studied parallelograms, you can think of a rectangle as a parallelogram with one extra constraint: all four angles are right angles. Since opposite angles in a parallelogram are equal and consecutive angles are supplementary, forcing one angle to be 90° forces all four to be 90°. You don't need to verify all four corners — just one. This inheritance structure is important: a rectangle automatically has all parallelogram properties (opposite sides parallel and equal, diagonals bisect each other, opposite angles equal), plus the right-angle condition.

The most important property unique to rectangles — beyond right angles themselves — is that the **diagonals are congruent**. This can be proved cleanly using congruent triangles: in rectangle ABCD, triangles ABD and BCD share side BD, have equal sides AB = CD (opposite sides of the parallelogram), and both contain the right angle at the vertices. By SAS congruence, the triangles are congruent, so AC = BD. The converse is equally important: if a parallelogram has congruent diagonals, it must be a rectangle. This gives you a useful two-way test — you can prove something is a rectangle by proving it is a parallelogram and then showing its diagonals are equal in length.

A common source of confusion is the relationship between rectangles and squares. A **square** is a rectangle with all four sides equal. This means every square is a rectangle, but not every rectangle is a square. The rectangle is the more general class; the square is a special case. Similarly, a square is also a rhombus (all sides equal), so a square sits at the intersection of rectangles and rhombuses. Keeping this hierarchy in mind — square ⊂ rectangle ⊂ parallelogram ⊂ quadrilateral — helps you know exactly which properties apply.

In coordinate geometry, rectangles are particularly easy to work with. To verify that four points form a rectangle, check two things: the midpoints of the two diagonals coincide (which confirms it is a parallelogram), and two adjacent sides are perpendicular (slopes are negative reciprocals). The diagonal lengths are then automatically equal by the Pythagorean theorem. This coordinate approach is the standard proof strategy when working with vertices given as ordered pairs, and it builds directly on the parallelogram tools you already have.
