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

## Questions

```yaml
- question: "Point A is at position 3 on a number line, point C is at position 11, and point B is between A and C at position 7. What is AB + BC, and what does this tell you?"
  type: multiple-choice
  options:
    - "AB + BC = 4 + 4 = 8; this is a coincidence for this specific case"
    - "AB + BC = 4 + 4 = 8 = AC; this confirms the Segment Addition Postulate because B lies between A and C"
    - "AB + BC = 7 + 4 = 11; you add the position of B to the remaining distance"
    - "AB + BC cannot be computed without knowing if A, B, C are collinear"
  answer: 1
  explanation: "AB = |7 − 3| = 4 and BC = |11 − 7| = 4, so AB + BC = 8 = AC = |11 − 3|. This illustrates the Segment Addition Postulate: when B lies between A and C on a line, the two partial lengths add to the total. Option D is wrong because on a number line, collinearity is given — all three points are on the same line by definition."

- question: "A student computes the distance from point P at (1, 2) to point Q at (4, 6) as (4−1) + (6−2) = 7. What error did they make?"
  type: multiple-choice
  options:
    - "They should have computed (4+1) + (6+2) = 13 instead"
    - "They added the horizontal and vertical differences directly instead of using the Pythagorean theorem: d = √(3² + 4²) = 5"
    - "They forgot to take the absolute value of each difference before adding"
    - "Distance in the coordinate plane cannot be computed from coordinates alone"
  answer: 1
  explanation: "The distance formula d = √((x₂−x₁)² + (y₂−y₁)²) comes from the Pythagorean theorem. The horizontal gap (3) and vertical gap (4) are the legs of a right triangle; the actual distance is the hypotenuse: √(9 + 16) = √25 = 5. Simply adding the differences gives the sum of the legs, not the hypotenuse — a common error that ignores the geometry underlying the formula."

- question: "Distance between two points can be negative if the second point is to the left of the first on a number line."
  type: true-false
  answer: false
  explanation: "Distance is always nonnegative. On a number line, distance is computed as |a − b|, and the absolute value ensures a positive result regardless of order. If A is at 8 and B is at 3, then AB = |3 − 8| = |−5| = 5, not −5. Directed distance (displacement) can be negative, but distance — which measures 'how far apart' — never can."

- question: "The Segment Addition Postulate applies only when B lies between A and C on the same line — not merely between them in everyday language."
  type: true-false
  answer: true
  explanation: "The geometric definition of 'between' is stricter than the everyday meaning. B is geometrically between A and C only if (1) all three points are collinear — on the same line — and (2) AB + BC = AC. If B is not on the line through A and C, you cannot use the postulate, even if B is spatially 'between' them in some loose sense. This precision matters in proofs and in problems where B's position must be established, not assumed."

- question: "Why do we use the absolute value when computing distance on a number line, and why is it not needed explicitly in the coordinate-plane distance formula?"
  type: short-answer
  answer: "On a number line, subtraction can yield a negative result depending on order (e.g., 3 − 7 = −4), but distance is always positive, so we write |a − b|. In the coordinate-plane formula, each difference is squared before taking the square root — squaring automatically makes the result nonnegative — so the absolute value is built into the squaring step."
  explanation: "This reveals the structural relationship between the number-line and coordinate-plane formulas: they are the same idea. The number-line version uses |a − b| to ensure positivity; the coordinate-plane version achieves the same result by squaring. Understanding this connection shows that the distance formula is not a separate rule to memorize but the Pythagorean theorem applied to coordinate differences."
```

## Explainer

From your work with points, lines, and planes, you know that a line extends infinitely in both directions. A **line segment** is what you get when you cut a line between two specific **endpoints** — it has a definite start and a definite end. The length of that segment is the **distance** between the two endpoints. Distance is always a nonnegative number; it measures "how far apart," not "which direction."

On a number line, computing distance is straightforward: just subtract and take the absolute value. If point A is at position 2 and point B is at position 7, then AB = |7 − 2| = 5. You need the absolute value (a concept you already know) because subtraction can produce a negative number, but distance cannot be negative. Whether you compute 7 − 2 or 2 − 7, the absolute value gives you the same positive answer.

In the coordinate plane, the same idea extends using the **distance formula**: d = √((x₂ − x₁)² + (y₂ − y₁)²). This formula comes directly from the Pythagorean theorem — the horizontal gap and vertical gap between two points form the legs of a right triangle, and the segment connecting the points is the hypotenuse. Squaring automatically removes the sign issue (so you do not need the absolute value), and the square root recovers the length.

The **Segment Addition Postulate** formalizes what it means for one point to lie between two others: B is between A and C (in the geometric sense) if and only if AB + BC = AC. This sounds obvious, but the postulate pins down the word "between" precisely — B must lie on the same line as A and C, and the two partial lengths must add to the total. This postulate is the engine behind almost every "find the missing length" problem in geometry, and it is the foundation for the midpoint concept you will encounter next.
