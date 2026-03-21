---
id: central-angles-and-arcs
title: Central Angles and Arcs
domain: mathematics
course: geometry
prerequisites:
  - id: circle-basics
    type: hard
  - id: angle-basics-and-classification
    type: hard
builds-toward:
  - inscribed-angles
  - arc-length
  - sector-area
tags: [circles, central-angles, arcs, arc-measure]
stage: abstract-reasoning
status: validated
---

# Central Angles and Arcs

## Core Idea
A central angle has its vertex at the center of the circle. The arc intercepted by a central angle has the same degree measure as the angle. A minor arc (less than 180 degrees) and a major arc (greater than 180 degrees) together comprise the full circle (360 degrees). A semicircle is an arc of exactly 180 degrees. The Arc Addition Postulate states that adjacent arcs can be added. Central angles and arcs connect angle measurement to arc measurement.

## How It's Best Learned
Draw central angles and identify their intercepted arcs. Practice finding arc measures given central angles and vice versa. Introduce three-letter arc notation for major arcs. Use the Arc Addition Postulate to find unknown arc measures. Connect to pie charts and clock angles for real-world context.

## Common Misconceptions
- Confusing arc measure (in degrees) with arc length (a linear measurement that depends on the radius).
- Using two letters for a major arc (three letters are needed to specify which arc is meant).
- Thinking all arcs of the same degree measure have the same length (they do only in circles of the same radius).

## Questions

```yaml
- question: "Two circles have the same center. One has radius 3 cm and the other has radius 6 cm. Each has a central angle of 60°. Which statement is true?"
  type: multiple-choice
  options:
    - "Both arcs have the same measure (60°) and the same length"
    - "The larger circle's arc has a greater degree measure because its radius is larger"
    - "Both arcs have the same degree measure (60°), but the larger circle's arc is longer"
    - "The smaller circle's arc is longer because it curves more sharply"
  answer: 2
  explanation: "Arc measure (in degrees) equals the central angle — 60° in both cases — regardless of radius. But arc length is a linear distance that depends on radius: a larger circle has a longer circumference, so the same 60° represents a longer physical arc. This is the critical distinction between arc measure and arc length. Two arcs can have identical degree measures yet completely different lengths if their circles have different radii."

- question: "In a circle, points A, B, and C lie on the circle with C on the minor arc from A to B. The measure of arc AC is 40° and the measure of arc CB is 75°. What is the measure of central angle AOB (where O is the center)?"
  type: multiple-choice
  options:
    - "35°"
    - "75°"
    - "115°"
    - "245°"
  answer: 2
  explanation: "By the Arc Addition Postulate, arc AB = arc AC + arc CB = 40° + 75° = 115°. The central angle AOB equals the measure of its intercepted arc, so the central angle is also 115°. The Arc Addition Postulate works just like the Segment Addition Postulate: if C is between A and B on the arc, the pieces add to the whole."

- question: "A central angle of 90° always intercepts an arc of 90°, no matter the size of the circle."
  type: true-false
  answer: true
  explanation: "Arc measure equals the central angle, always — this relationship is independent of the circle's radius. A 90° central angle cuts off exactly one quarter of the circle (since 90/360 = 1/4), so the arc measures 90° whether the circle has radius 2 cm or radius 200 km. The proportional relationship between central angle and arc is what makes arc measure useful: it depends only on the angle, not on the circle's size."

- question: "If two arcs have the same degree measure, they must have the same arc length."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about arc measure. Arc measure (degrees) and arc length (a linear distance) are different quantities. Two arcs with the same degree measure have the same arc length only if they belong to circles of the same radius. A 90° arc on a circle of radius 10 cm is much longer than a 90° arc on a circle of radius 1 cm, even though both arcs measure 90°. Arc length formula (which you'll study next) shows that arc length = (θ/360°) × 2πr — the radius r appears in the formula for length but not for measure."

- question: "A diameter divides a circle into two semicircles. Explain why each semicircle measures exactly 180°, using the relationship between central angles and arc measures."
  type: short-answer
  answer: "A diameter passes through the center, so it forms a central angle of 180° (a straight angle). By the central angle-arc measure relationship, the intercepted arc equals the central angle — so each semicircle measures 180°. Alternatively: a full circle is 360°, and a diameter divides it into two equal arcs (since the diameter is a line of symmetry through the center), so each arc is 360° ÷ 2 = 180°."
  explanation: "Both approaches reach the same answer. The first uses the definition directly: the central angle formed by a diameter is a straight angle (180°), and arc measure equals central angle. The second uses the symmetry of a diameter plus the fact that the full circle is 360°. Understanding why the arc is 180° — not just that it is — requires connecting the straight-angle property of a diameter to the arc measure theorem."
```

## Explainer

From your study of circle basics, you know that a circle is defined by its center and radius, and that all points on the circle are equidistant from the center. A **central angle** is simply an angle whose vertex sits exactly at that center. Because the center is the "hub" of the circle, a central angle has a uniquely direct relationship with the arc it cuts off: the arc's degree measure equals the angle's degree measure, exactly.

Why is this true? Imagine the circle as a full rotation of 360°. A central angle that opens to 90° claims exactly one quarter of that full rotation — and the arc it intercepts is exactly one quarter of the circle. The fraction of the full angle equals the fraction of the full circle. This proportionality is what makes arc measure so clean: a 60° central angle cuts off a 60° arc, always, regardless of the radius. You're dividing the circle proportionally, and both the angle and the arc share the same proportion.

This leads directly to the vocabulary you need. A **minor arc** is the smaller of the two arcs formed by two points on the circle — it corresponds to a central angle less than 180°. The **major arc** is the larger piece, corresponding to a reflex angle greater than 180°. Together they sum to 360°. A **semicircle** is the special case where both arcs are equal — exactly 180° each, cut by a diameter. Because two-letter arc notation (arc AB) is ambiguous for major arcs (it could refer to either arc), you use three letters to specify the path: arc ACB traces from A through point C to B, leaving no ambiguity about which arc is meant.

The **Arc Addition Postulate** mirrors the Segment Addition Postulate you already know from angle basics. If C is a point on arc AB (between A and B), then the measure of arc AC plus the measure of arc CB equals the measure of arc AB. This additive structure lets you build up unknown arc measures from known pieces, just as you add angle measures to find totals. One important clarification before moving on: arc *measure* (in degrees) and arc *length* (in centimeters or meters) are different quantities. Two arcs can have the same 90° measure but very different lengths if they come from circles of different radii. Arc length depends on radius; arc measure does not. That distinction becomes essential when you study arc length formulas next.
