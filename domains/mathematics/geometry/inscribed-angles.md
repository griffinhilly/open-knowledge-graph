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

## Explainer

From your study of **central angles and arcs**, you know that a central angle equals the arc it intercepts — a 60° central angle cuts off a 60° arc, and the arc measure is defined by the central angle. An **inscribed angle** is different: its vertex lies *on* the circle, and its two sides are chords. The surprising result — the **Inscribed Angle Theorem** — is that an inscribed angle is always exactly half the central angle intercepting the same arc. A 60° arc produces a 30° inscribed angle; a 180° arc (a semicircle) produces a 90° inscribed angle.

The proof builds directly on what you know about central angles. The cleanest case: suppose one chord of the inscribed angle passes through the center, forming a diameter. The inscribed angle and the central angle then share a chord, and the triangle formed has two sides equal to the radius — making it isosceles. The central angle is an exterior angle of this isosceles triangle, so it equals the sum of the two equal base angles, which is exactly twice the inscribed angle. For the general case where neither chord passes through the center, draw a diameter from the vertex and apply the special case twice — once for each chord — adding or subtracting results depending on the configuration. The half-arc relationship holds in all cases.

The corollaries are as useful as the theorem itself. The **semicircle corollary**: any angle inscribed in a semicircle is exactly 90°. This is immediate — the intercepted arc is 180°, so the inscribed angle is half of 180°. This gives a beautiful construction shortcut: to guarantee a right angle, put the two points of a diameter as the "base" of an inscribed triangle, and the apex will always be a right angle regardless of where you place it on the circle. The **equal-arcs corollary**: all inscribed angles intercepting the *same* arc are congruent. Fix two points on a circle; every third point anywhere on the major arc produces the same angle — a deeply counterintuitive result worth verifying empirically.

The **inscribed quadrilateral theorem** follows from the same logic: opposite angles in a cyclic quadrilateral (one inscribed in a circle) are supplementary — they sum to 180°. Each opposite angle intercepts one of two arcs, and the two arcs together make the full 360°. So the two opposite angles, each half their respective arc, sum to half of 360° = 180°. This gives a powerful test for cyclic quadrilaterals: if opposite angles are supplementary, the quadrilateral can be inscribed in a circle. Together, these corollaries make the Inscribed Angle Theorem one of the most productive theorems in circle geometry — a single fact that unlocks an entire family of results.
