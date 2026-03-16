---
id: trapezoid-properties
title: Trapezoid Properties
domain: mathematics
course: geometry
prerequisites:
  - id: parallel-lines-and-transversals
    type: hard
  - id: midsegment-theorem
    type: soft
builds-toward:
  - coordinate-geometry-proofs
tags: [quadrilaterals, trapezoids, midsegment, isosceles-trapezoid]
stage: abstract-reasoning
status: validated
---

# Trapezoid Properties

## Core Idea
A trapezoid is a quadrilateral with exactly one pair of parallel sides (the bases). The non-parallel sides are the legs. The midsegment (median) of a trapezoid connects the midpoints of the legs and is parallel to both bases with length equal to the average of the base lengths. An isosceles trapezoid has congruent legs, congruent base angles, and congruent diagonals. The area is (1/2)(b1 + b2)(h).

## How It's Best Learned
Define and classify trapezoids. Prove the midsegment theorem using coordinate geometry or similar triangles. For isosceles trapezoids, prove the base angle and diagonal congruence theorems. Practice area calculations. Contrast with parallelograms (which some definitions include as special trapezoids).

## Common Misconceptions
- Confusion about whether parallelograms are trapezoids (depends on whether the definition says "at least one" or "exactly one" pair of parallel sides; standard US convention uses "exactly one").
- Assuming all trapezoids are isosceles.
- Forgetting the midsegment length formula (average of the two bases).

## Explainer

A **trapezoid** is defined by what makes it just barely a quadrilateral with parallel sides: exactly one pair of opposite sides is parallel. Those parallel sides are called the **bases** (typically labeled b₁ and b₂), and the non-parallel sides are the **legs**. The defining property — one pair parallel, one pair not — is what you need to keep in mind when using your knowledge of **parallel lines and transversals**. Because the legs cross both parallel bases, the co-interior (same-side interior) angles between each leg and the two bases are supplementary. This means in any trapezoid, each leg creates two pairs of angles that add to 180° — a useful constraint for finding missing angles.

The **midsegment** (also called the median) connects the midpoints of the two legs. Its two key properties follow from the same parallel-line logic: it is parallel to both bases, and its length equals the *average* of the two base lengths: m = (b₁ + b₂)/2. You can build intuition for this formula by imagining sliding the shorter base partway toward the longer one — halfway across, the midsegment is precisely the arithmetic mean, balancing both extremes.

An **isosceles trapezoid** is the symmetric special case: both legs are congruent. Symmetry here has cascading consequences. The base angles are congruent (the two angles sharing each base are equal). The diagonals are congruent. And if you fold the figure along the line of symmetry, both halves match exactly. These properties make isosceles trapezoids especially common in geometry proofs and real-world design (arches, tabletops, certain bridge cross-sections).

The area formula **A = ½(b₁ + b₂)h** is best remembered as "average of the bases times height." Think of it this way: if you had a rectangle with width equal to the average base and height h, it would have the same area as the trapezoid. This makes intuitive sense — the trapezoid is "wider than the shorter base and narrower than the longer base," so its average width is the right representative measure.
