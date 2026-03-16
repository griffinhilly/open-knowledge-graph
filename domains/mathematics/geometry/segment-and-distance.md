---
id: segment-and-distance
title: Segments and Distance
domain: mathematics
course: geometry
prerequisites:
  - id: points-lines-planes
    type: hard
  - id: absolute-value
    type: soft
builds-toward:
  - midpoint-formula
  - triangle-inequality
tags: [measurement, segments, distance-formula]
stage: abstract-reasoning
status: validated
---

# Segments and Distance

## Core Idea
A line segment is a portion of a line bounded by two endpoints. The distance between two points is the length of the segment connecting them, always a nonneg value. On a number line, distance is computed via absolute value of the difference. The Segment Addition Postulate states that if B is between A and C, then AB + BC = AC. This concept underpins all measurement in geometry.

## How It's Best Learned
Start on a number line where distance = |a - b|. Then move to the coordinate plane and derive the distance formula from the Pythagorean theorem. Give problems where students must use the Segment Addition Postulate to find unknown lengths. Reinforce that distance is always positive.

## Common Misconceptions
- Forgetting absolute value and getting negative distances.
- Confusing "between" in everyday language with the geometric definition (B is between A and C only if A, B, C are collinear and AB + BC = AC).
- Applying the distance formula but forgetting to square the differences or forgetting the square root.

## Explainer

From your work with points, lines, and planes, you know that a line extends infinitely in both directions. A **line segment** is what you get when you cut a line between two specific **endpoints** — it has a definite start and a definite end. The length of that segment is the **distance** between the two endpoints. Distance is always a nonnegative number; it measures "how far apart," not "which direction."

On a number line, computing distance is straightforward: just subtract and take the absolute value. If point A is at position 2 and point B is at position 7, then AB = |7 − 2| = 5. You need the absolute value (a concept you already know) because subtraction can produce a negative number, but distance cannot be negative. Whether you compute 7 − 2 or 2 − 7, the absolute value gives you the same positive answer.

In the coordinate plane, the same idea extends using the **distance formula**: d = √((x₂ − x₁)² + (y₂ − y₁)²). This formula comes directly from the Pythagorean theorem — the horizontal gap and vertical gap between two points form the legs of a right triangle, and the segment connecting the points is the hypotenuse. Squaring automatically removes the sign issue (so you do not need the absolute value), and the square root recovers the length.

The **Segment Addition Postulate** formalizes what it means for one point to lie between two others: B is between A and C (in the geometric sense) if and only if AB + BC = AC. This sounds obvious, but the postulate pins down the word "between" precisely — B must lie on the same line as A and C, and the two partial lengths must add to the total. This postulate is the engine behind almost every "find the missing length" problem in geometry, and it is the foundation for the midpoint concept you will encounter next.
