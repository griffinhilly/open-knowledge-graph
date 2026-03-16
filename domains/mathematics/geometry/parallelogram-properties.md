---
id: parallelogram-properties
title: Parallelogram Properties
domain: mathematics
course: geometry
prerequisites:
- id: parallel-lines-and-transversals
  type: hard
- id: triangle-congruence-sas
  type: hard
- id: alternate-interior-angles
  type: hard
- id: cpctc
  type: soft
builds-toward:
- rectangle-properties
- rhombus-properties
- coordinate-geometry-proofs
tags:
- quadrilaterals
- parallelograms
- properties
- proof
stage: abstract-reasoning
status: validated
---
# Parallelogram Properties

## Core Idea
A parallelogram is a quadrilateral with both pairs of opposite sides parallel. Key properties: opposite sides are congruent, opposite angles are congruent, consecutive angles are supplementary, and diagonals bisect each other. Conversely, if any of these properties hold for a quadrilateral, it is a parallelogram. These properties are proven using alternate interior angles and triangle congruence.

## How It's Best Learned
Prove each property from the definition using diagonal-created triangles and alternate interior angles. Then practice the converses: given information about a quadrilateral, determine whether it must be a parallelogram. Use coordinate geometry to verify properties. Connect to real-world examples (tables, doors).

## Common Misconceptions
- Assuming diagonals are congruent (they are not in general parallelograms; that is a rectangle property).
- Assuming diagonals are perpendicular (that is a rhombus property).
- Confusing necessary conditions with sufficient conditions for proving a quadrilateral is a parallelogram.

## Explainer

A **parallelogram** is defined by a simple condition: both pairs of opposite sides are parallel. Everything else — all the properties you need to know — follows from this single definition using tools you already have: parallel lines and transversals, and triangle congruence. The key move is to draw a diagonal, splitting the parallelogram into two triangles. Those triangles will turn out to be congruent, and CPCTC then delivers the properties for free.

Draw diagonal AC in parallelogram ABCD. Because AB ∥ CD, the diagonal AC is a transversal, so angle BAC = angle DCA (alternate interior angles). Because AD ∥ BC, the same transversal gives angle DAC = angle BCA. The triangles ABC and CDA share side AC, so by ASA they are congruent. From CPCTC: AB = CD and AD = BC — **opposite sides are congruent**. The same congruence also gives angle B = angle D — **opposite angles are congruent**. For consecutive angles, note that AB ∥ CD means angles A and D are co-interior angles (same-side interior), which sum to 180° — **consecutive angles are supplementary**.

The diagonal property is slightly different. Draw both diagonals and call their intersection E. Show that triangles AEB and CED are congruent (two pairs of alternate interior angles plus opposite sides AB = CD from above). This gives AE = CE and BE = DE — **diagonals bisect each other**. Notice what is *not* claimed: the diagonals are not necessarily equal in length (that requires a rectangle) and not necessarily perpendicular (that requires a rhombus).

The converses are just as important: if you can prove *any one* of these properties for an unknown quadrilateral, you have proven it is a parallelogram. Both pairs of opposite sides equal? Parallelogram. Diagonals bisect each other? Parallelogram. One pair of sides both parallel and equal? Parallelogram. This makes the family of sufficient conditions a toolkit for writing proofs — you pick whichever property your given information most directly implies. The properties and their converses form the bridge between the basic definition and the richer special cases (rectangles, rhombuses, squares) you will study next.
