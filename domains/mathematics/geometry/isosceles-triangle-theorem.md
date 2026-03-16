---
id: isosceles-triangle-theorem
title: Isosceles Triangle Theorem
domain: mathematics
course: geometry
prerequisites:
  - id: triangle-congruence-sas
    type: hard
  - id: cpctc
    type: hard
builds-toward:
  - perpendicular-bisectors
  - coordinate-geometry-proofs
tags: [triangles, isosceles, congruence, base-angles]
stage: abstract-reasoning
status: validated
---

# Isosceles Triangle Theorem

## Core Idea
The Isosceles Triangle Theorem states that if two sides of a triangle are congruent, then the angles opposite those sides (the base angles) are congruent. The converse is also true: if two angles are congruent, the sides opposite them are congruent. The proof uses the angle bisector from the vertex angle to create two congruent triangles via SAS. This theorem connects side relationships to angle relationships.

## How It's Best Learned
Draw the angle bisector from the vertex of an isosceles triangle and prove the two halves congruent. Solve problems with variable expressions for base angles. Extend to equilateral triangles (a special case where all three sides and all three angles are congruent, each 60 degrees).

## Common Misconceptions
- Confusing which angles are the "base angles" (they are opposite the congruent sides, not adjacent to them).
- Assuming the converse without proof.
- Forgetting that the equilateral triangle is a special case of isosceles.

## Explainer

Using your knowledge of SAS congruence and CPCTC, you can now understand why isosceles triangles behave so symmetrically. An **isosceles triangle** is one with two equal sides, called the **legs**. The angle between the two legs is the **vertex angle**, and the two remaining angles — each opposite one leg — are the **base angles**. The theorem says: equal sides force equal opposite angles.

The proof works by creating a clever self-comparison. Draw the **angle bisector** from the vertex angle down to the opposite side. This divides the triangle into two smaller triangles. Now check what SAS requires: two sides and the included angle. The two legs are given as equal (the definition of isosceles). The angle bisector creates two equal halves of the vertex angle. The bisector itself is shared by both smaller triangles — equal to itself by the reflexive property. That gives you two sides and the included angle equal in the two smaller triangles — exactly SAS. Now apply CPCTC: the base angles are corresponding parts of these congruent triangles, so they must be equal.

The **converse** works in the other direction: if two angles of a triangle are equal, the sides opposite them are equal. This means angle information implies side information, and vice versa. Together, theorem and converse establish that isosceles triangles are exactly those where legs and base angles come in matched pairs. The equilateral triangle is the limiting case — all three sides equal means all three angles equal, and since the angles must sum to 180°, each is exactly 60°.

When solving problems, the most common error is misidentifying the base angles. Base angles are opposite the congruent sides — they are not necessarily at the geometric "bottom" of the figure. If a diagram shows an isosceles triangle tilted or inverted, the base angles are still the two equal ones, wherever they happen to be. In algebraic problems, this equality lets you set up equations: if the base angles are expressed as (3x + 10)° and (5x − 14)°, setting them equal and solving gives x, and then the angle measure follows. The theorem converts the geometry into an equation.
