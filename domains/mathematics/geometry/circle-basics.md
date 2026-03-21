---
id: circle-basics
title: "Circle Basics: Radius, Diameter, and Chord"
domain: mathematics
course: geometry
prerequisites:
  - id: segment-and-distance
    type: hard
builds-toward:
  - central-angles-and-arcs
  - inscribed-angles
  - tangent-lines-to-circles
  - conic-sections-circles
tags: [circles, radius, diameter, chord, definitions]
stage: abstract-reasoning
status: validated
---

# Circle Basics: Radius, Diameter, and Chord

## Core Idea
A circle is the set of all points equidistant from a center point. The radius is the distance from the center to any point on the circle. The diameter is a chord passing through the center, equal to twice the radius. A chord is any segment with both endpoints on the circle. A secant is a line that intersects the circle at two points. These definitions are the foundation for all circle theorems.

## How It's Best Learned
Draw and label parts of a circle. Emphasize that a circle is a set of points (a curve), not the region inside it (that is a disk). Practice identifying radii, diameters, chords, and secants. Introduce the standard equation of a circle: (x-h)^2 + (y-k)^2 = r^2.

## Common Misconceptions
- Confusing radius and diameter (diameter = 2r).
- Thinking a circle includes its interior (a circle is just the boundary curve).
- Not recognizing that every diameter is a chord but not every chord is a diameter.
- Confusing chord and secant (a chord is a segment; a secant is a line).

## Questions

```yaml
- question: "Which of the following statements about the diameter of a circle is correct?"
  type: multiple-choice
  options:
    - "The diameter is any chord with both endpoints on the circle"
    - "The diameter is the longest possible chord and must pass through the center"
    - "The diameter equals twice the radius only when the circle is centered at the origin"
    - "The diameter is a segment from the center to any point on the circle"
  answer: 1
  explanation: "The diameter is uniquely defined as the chord that passes through the center — this makes it the longest possible chord, since any chord that doesn't pass through the center is shorter. Option A incorrectly describes all chords, not just diameters. Option C is wrong because d = 2r is true for every circle regardless of position. Option D describes the radius, not the diameter."

- question: "A chord is drawn in a circle that does not pass through the center. Which statement must be true about this chord?"
  type: multiple-choice
  options:
    - "It is equal in length to the radius"
    - "It divides the circle into two equal arcs"
    - "It is shorter than the diameter"
    - "It is the same as a secant"
  answer: 2
  explanation: "The diameter is the longest possible chord because it stretches across the widest point of the circle (through the center). Any chord that doesn't pass through the center is shorter. Option B is false — only a diameter divides a circle into two equal halves. Option D confuses chord (a segment with endpoints on the circle) with secant (a line that extends through those points infinitely)."

- question: "The equation (x − 3)² + (y + 2)² = 25 represents a circle with center (3, −2) and radius 5."
  type: true-false
  answer: true
  explanation: "The standard form of a circle is (x − h)² + (y − k)² = r², where (h, k) is the center and r is the radius. Here h = 3, k = −2 (note the sign flip: y + 2 = y − (−2)), and r² = 25, so r = 5. This equation is the distance formula in disguise: it says every point (x, y) on the circle is exactly 5 units from (3, −2)."

- question: "A circle is the set of all points inside and on a boundary curve that are equidistant from a center point."
  type: true-false
  answer: false
  explanation: "A circle is only the boundary curve — the set of points at exactly r units from the center. The filled-in region (including the interior) is called a disk, not a circle. This distinction matters in geometry: circle theorems apply to the curve, and equations like (x−h)² + (y−k)² = r² describe the boundary only. A common error is treating 'circle' and 'disk' interchangeably."

- question: "Explain why the diameter is always the longest chord in a circle."
  type: short-answer
  answer: "The diameter passes through the center — it connects two points on opposite sides of the circle with the center in between. Any other chord must 'miss' the center, meaning its two endpoints are not as far apart as possible. By the equidistance definition, every point on the circle is exactly r units from the center; a chord's length is maximized when the center lies on the chord, giving length 2r. Any chord that doesn't go through the center subtends a shorter distance."
  explanation: "This follows directly from the definition: if the center is on the chord, the chord consists of two radii laid end-to-end, giving total length 2r. If the center is not on the chord, the chord is like the base of a triangle whose other two sides are radii — and the third side of a triangle is always shorter than the sum of the other two sides (triangle inequality), confirming the chord is shorter than 2r."
```

## Explainer

A **circle** is defined by a single idea: equidistance. Pick a center point and a positive distance r. The circle is the set of all points in the plane that are exactly r units from the center — not closer, not farther. This makes a circle fundamentally different from a filled-in region (which is called a **disk**). The circle is the boundary curve alone.

From your prerequisite on segments and distance, you know how to measure the length between two points. The **radius** is the segment from the center to any point on the circle, and every radius of the same circle has the same length — that's the whole point of the equidistance definition. The **diameter** is a special chord: it passes through the center and connects two points on opposite sides of the circle. Because it consists of two radii laid end to end, the diameter is always exactly twice the radius: d = 2r. This relationship is worth memorizing because it appears in every circle formula you'll encounter.

A **chord** is any segment whose two endpoints both lie on the circle. The diameter is the longest possible chord — no chord can stretch farther than across the center. Every other chord is shorter, because straying from the center means the two endpoints are "closer together" along the circle. A **secant** generalizes the chord to a full line: where a chord is a segment that begins and ends on the circle, a secant is the infinite line that passes through those same two points, extending beyond the circle in both directions.

These definitions are not just vocabulary — they are the foundation for every theorem that follows. The circle's equation in coordinate geometry, (x − h)² + (y − k)² = r², is just the distance formula in disguise: any point (x, y) on a circle centered at (h, k) must satisfy the condition that its distance from the center equals r. When you see this equation later, recognize it as the definition of a circle restated algebraically. Every angle theorem, arc theorem, and tangent theorem you'll study builds directly on the precise meaning of radius, diameter, and chord established here.
