---
id: inscribed-angles
title: Inscribed Angles
domain: mathematics
course: geometry
prerequisites:
  - id: central-angles-and-arcs
    type: hard
builds-toward:
  - coordinate-geometry-proofs
tags: [circles, inscribed-angles, arcs, half-the-arc]
stage: abstract-reasoning
status: validated
---

# Inscribed Angles

## Core Idea
An inscribed angle has its vertex on the circle and its sides are chords. The Inscribed Angle Theorem states that an inscribed angle is half the measure of its intercepted arc (and therefore half the corresponding central angle). Corollaries: inscribed angles intercepting the same arc are congruent, an angle inscribed in a semicircle is a right angle, and opposite angles of an inscribed quadrilateral are supplementary.

## How It's Best Learned
Start with measurement: draw several inscribed angles intercepting the same arc and verify they are equal and half the central angle. Prove the theorem for the case where one side passes through the center, then extend to the general case. Practice applying the corollaries, especially the semicircle-right-angle result.

## Common Misconceptions
- Thinking inscribed angle equals the arc (it is half the arc).
- Confusing inscribed angles with central angles.
- Not recognizing the semicircle corollary: any angle inscribed in a semicircle is exactly 90 degrees.
- Applying the theorem to angles whose vertex is not on the circle.

## Questions

```yaml
- question: "An inscribed angle intercepts an arc of 80°. What is the measure of the inscribed angle?"
  type: multiple-choice
  options:
    - "80° — the inscribed angle equals the arc it intercepts"
    - "160° — the arc is twice the inscribed angle, so the angle doubles the arc"
    - "40° — the inscribed angle is half the intercepted arc"
    - "90° — any inscribed angle equals 90°"
  answer: 2
  explanation: "The Inscribed Angle Theorem states that an inscribed angle is exactly half the measure of its intercepted arc. Half of 80° is 40°. The most common error is option A — confusing an inscribed angle with a central angle. A central angle equals the arc it intercepts; an inscribed angle (vertex on the circle) is always half that value."

- question: "A triangle is inscribed in a circle so that one side is a diameter. Regardless of where the third vertex is placed on the circle, the angle opposite the diameter always measures:"
  type: multiple-choice
  options:
    - "60°, because a triangle inscribed in a circle is always equilateral"
    - "Equal to the central angle that subtends the same arc as the diameter"
    - "90°, because any inscribed angle intercepting a semicircle (180° arc) is half of 180°"
    - "It varies depending on where the third vertex is placed"
  answer: 2
  explanation: "The semicircle corollary: the intercepted arc is the semicircle = 180°, so the inscribed angle = 180° / 2 = 90°. This is true regardless of where on the remaining arc the third vertex sits — the intercepted arc is always the same 180°. Option D is the common misconception: students think moving the vertex changes the angle, but the Inscribed Angle Theorem guarantees it stays 90° so long as the vertex is on the circle and the sides pass through the diameter's endpoints."

- question: "Two inscribed angles in the same circle both intercept the same arc. They must be equal in measure."
  type: true-false
  answer: true
  explanation: "Both inscribed angles equal half of the same arc, so they are equal to each other. This 'equal-arcs corollary' holds for any two inscribed angles intercepting the same arc, regardless of where their vertices are placed on the remaining arc. The result feels counterintuitive — moving a vertex along the arc seems like it should change the angle — but the theorem guarantees equality."

- question: "In a cyclic quadrilateral (a quadrilateral inscribed in a circle), opposite angles are equal."
  type: true-false
  answer: false
  explanation: "Opposite angles in a cyclic quadrilateral are supplementary — they sum to 180° — not equal. Each pair of opposite angles intercepts arcs that together make up the full 360°. Since each inscribed angle equals half its arc, the two opposite angles together equal half of 360° = 180°. They are equal only in the special case where each arc is 180° (a rectangle inscribed in a circle)."

- question: "Why is an angle inscribed in a semicircle always exactly 90°, regardless of where on the arc the vertex is placed?"
  type: short-answer
  answer: "The intercepted arc is the semicircle, which always measures 180°. By the Inscribed Angle Theorem, an inscribed angle equals half its intercepted arc — and half of 180° is always 90°. Moving the vertex along the arc does not change which arc is intercepted (it is always the semicircle defined by the diameter), so the inscribed angle stays 90° no matter where the vertex sits."
  explanation: "The key insight is that the intercepted arc is fixed by the diameter — it does not change as the vertex moves. The Inscribed Angle Theorem then guarantees a constant result: half of a fixed arc is always the same angle. This makes the semicircle corollary one of the most useful results in circle geometry, providing a reliable construction for right angles."
```

## Explainer

From your study of **central angles and arcs**, you know that a central angle equals the arc it intercepts — a 60° central angle cuts off a 60° arc, and the arc measure is defined by the central angle. An **inscribed angle** is different: its vertex lies *on* the circle, and its two sides are chords. The surprising result — the **Inscribed Angle Theorem** — is that an inscribed angle is always exactly half the central angle intercepting the same arc. A 60° arc produces a 30° inscribed angle; a 180° arc (a semicircle) produces a 90° inscribed angle.

The proof builds directly on what you know about central angles. The cleanest case: suppose one chord of the inscribed angle passes through the center, forming a diameter. The inscribed angle and the central angle then share a chord, and the triangle formed has two sides equal to the radius — making it isosceles. The central angle is an exterior angle of this isosceles triangle, so it equals the sum of the two equal base angles, which is exactly twice the inscribed angle. For the general case where neither chord passes through the center, draw a diameter from the vertex and apply the special case twice — once for each chord — adding or subtracting results depending on the configuration. The half-arc relationship holds in all cases.

The corollaries are as useful as the theorem itself. The **semicircle corollary**: any angle inscribed in a semicircle is exactly 90°. This is immediate — the intercepted arc is 180°, so the inscribed angle is half of 180°. This gives a beautiful construction shortcut: to guarantee a right angle, put the two points of a diameter as the "base" of an inscribed triangle, and the apex will always be a right angle regardless of where you place it on the circle. The **equal-arcs corollary**: all inscribed angles intercepting the *same* arc are congruent. Fix two points on a circle; every third point anywhere on the major arc produces the same angle — a deeply counterintuitive result worth verifying empirically.

The **inscribed quadrilateral theorem** follows from the same logic: opposite angles in a cyclic quadrilateral (one inscribed in a circle) are supplementary — they sum to 180°. Each opposite angle intercepts one of two arcs, and the two arcs together make the full 360°. So the two opposite angles, each half their respective arc, sum to half of 360° = 180°. This gives a powerful test for cyclic quadrilaterals: if opposite angles are supplementary, the quadrilateral can be inscribed in a circle. Together, these corollaries make the Inscribed Angle Theorem one of the most productive theorems in circle geometry — a single fact that unlocks an entire family of results.
