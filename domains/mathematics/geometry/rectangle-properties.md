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

## Questions

```yaml
- question: "A parallelogram is known to have both pairs of opposite sides equal and diagonals that bisect each other. You then learn its diagonals are congruent. What can you conclude?"
  type: multiple-choice
  options:
    - "It must be a square"
    - "It must be a rectangle"
    - "It must be a rhombus"
    - "Nothing additional — congruent diagonals don't help classify a parallelogram"
  answer: 1
  explanation: "Congruent diagonals are the defining additional property that distinguishes a rectangle from a general parallelogram. The theorem works both ways: if a parallelogram has congruent diagonals, it is a rectangle. A square is a special case (also a rectangle with equal sides), but the correct classification given only this information is rectangle — not square."

- question: "In rectangle ABCD, you draw both diagonals. Which of the following is true?"
  type: multiple-choice
  options:
    - "The diagonals are perpendicular bisectors of each other"
    - "The diagonals are congruent and bisect each other but are not necessarily perpendicular"
    - "The diagonals are congruent and perpendicular but do not bisect each other"
    - "The diagonals bisect each other at right angles only if the rectangle is a square"
  answer: 1
  explanation: "Rectangle diagonals are congruent (the property unique to rectangles among parallelograms) and bisect each other (inherited from the parallelogram). They are NOT necessarily perpendicular — perpendicular diagonals belong to rhombuses. Only when a rectangle is also a square (all sides equal) are the diagonals perpendicular. Confusing congruent diagonals with perpendicular diagonals is one of the most common errors on rectangle problems."

- question: "Every square is a rectangle."
  type: true-false
  answer: true
  explanation: "A rectangle is defined as a parallelogram with four right angles. A square satisfies this — it has four right angles and all four sides equal. The square is a special case of rectangle (a rectangle with equal sides), just as a rectangle is a special case of parallelogram. The hierarchy runs: square ⊂ rectangle ⊂ parallelogram ⊂ quadrilateral. Saying 'a square is not a rectangle' confuses the special case with a separate category."

- question: "The diagonals of a rectangle are perpendicular to each other."
  type: true-false
  answer: false
  explanation: "This is a very common misconception. Rectangle diagonals are congruent and bisect each other, but they are NOT generally perpendicular. Perpendicular diagonals are a property of rhombuses (including squares). Only when a rectangle is also a square do the diagonals happen to be perpendicular. A non-square rectangle's diagonals cross at an oblique angle — you can verify this by drawing any non-square rectangle and measuring the crossing angle."

- question: "Why is it sufficient to prove that just one angle of a parallelogram is 90° to conclude that all four angles are 90°?"
  type: short-answer
  answer: "In a parallelogram, opposite angles are equal and consecutive angles are supplementary (sum to 180°). If one angle is 90°, its opposite angle must also be 90°, and each consecutive angle must be 180° − 90° = 90°. So proving one right angle forces all four to be right angles."
  explanation: "This is why the definition of a rectangle only requires 'a parallelogram with right angles' — you don't need to verify all four corners. The parallelogram constraints propagate the right-angle condition around the entire figure. It also underlies the coordinate-geometry test: prove the shape is a parallelogram, then show one pair of adjacent sides is perpendicular (slopes are negative reciprocals), and you're done."
```

## Explainer

Because you have already studied parallelograms, you can think of a rectangle as a parallelogram with one extra constraint: all four angles are right angles. Since opposite angles in a parallelogram are equal and consecutive angles are supplementary, forcing one angle to be 90° forces all four to be 90°. You don't need to verify all four corners — just one. This inheritance structure is important: a rectangle automatically has all parallelogram properties (opposite sides parallel and equal, diagonals bisect each other, opposite angles equal), plus the right-angle condition.

The most important property unique to rectangles — beyond right angles themselves — is that the **diagonals are congruent**. This can be proved cleanly using congruent triangles: in rectangle ABCD, triangles ABD and BCD share side BD, have equal sides AB = CD (opposite sides of the parallelogram), and both contain the right angle at the vertices. By SAS congruence, the triangles are congruent, so AC = BD. The converse is equally important: if a parallelogram has congruent diagonals, it must be a rectangle. This gives you a useful two-way test — you can prove something is a rectangle by proving it is a parallelogram and then showing its diagonals are equal in length.

A common source of confusion is the relationship between rectangles and squares. A **square** is a rectangle with all four sides equal. This means every square is a rectangle, but not every rectangle is a square. The rectangle is the more general class; the square is a special case. Similarly, a square is also a rhombus (all sides equal), so a square sits at the intersection of rectangles and rhombuses. Keeping this hierarchy in mind — square ⊂ rectangle ⊂ parallelogram ⊂ quadrilateral — helps you know exactly which properties apply.

In coordinate geometry, rectangles are particularly easy to work with. To verify that four points form a rectangle, check two things: the midpoints of the two diagonals coincide (which confirms it is a parallelogram), and two adjacent sides are perpendicular (slopes are negative reciprocals). The diagonal lengths are then automatically equal by the Pythagorean theorem. This coordinate approach is the standard proof strategy when working with vertices given as ordered pairs, and it builds directly on the parallelogram tools you already have.
