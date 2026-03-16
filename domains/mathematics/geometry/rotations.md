---
id: rotations
title: "Geometric Transformations: Rotations"
domain: mathematics
course: geometry
prerequisites:
  - id: reflections
    type: soft
  - id: angle-basics-and-classification
    type: hard
  - id: coordinate-plane-intro
    type: hard
builds-toward:
  - coordinate-geometry-proofs
tags: [transformations, rotations, rigid-motions]
stage: abstract-reasoning
status: validated
---

# Geometric Transformations: Rotations

## Core Idea
A rotation turns a figure about a fixed point (the center of rotation) by a specified angle. A positive angle typically means counterclockwise. Key coordinate rules for rotations about the origin: 90 degrees maps (x, y) to (-y, x); 180 degrees to (-x, -y); 270 degrees to (y, -x). Rotations are rigid motions that preserve distance, angle measure, and orientation.

## How It's Best Learned
Use tracing paper or dynamic geometry software to rotate figures. Start with 90, 180, and 270-degree rotations about the origin and memorize the coordinate rules. Practice rotating about points other than the origin by translating to the origin, rotating, then translating back. Verify distances are preserved.

## Common Misconceptions
- Confusing clockwise and counterclockwise (positive angles are counterclockwise by convention).
- Mixing up the coordinate rules for 90 and 270-degree rotations.
- Thinking rotations change the size of the figure.
- Forgetting that rotation about a point other than the origin requires a different process.

## Explainer

A **rotation** is a rigid motion — it slides a figure around a fixed point without stretching, flipping, or distorting it. That fixed point is called the **center of rotation**. Like the reflections you've already studied, rotations preserve distances and angle measures, which is why they're called rigid motions or isometries. The difference is that reflections flip orientation (left and right swap), while rotations preserve orientation: a clockwise-labeled triangle stays clockwise after rotation.

The most useful rotations to memorize are the quarter-turn, half-turn, and three-quarter-turn about the origin. For a 90° counterclockwise rotation, the rule is (x, y) → (−y, x). You can verify this with a concrete point: (3, 0) should move to a point 3 units away, now pointing straight up, which is (0, 3). Applying the rule: (−0, 3) = (0, 3). Correct. For a 180° rotation, (x, y) → (−x, −y) — every point gets reflected through the origin. For 270° counterclockwise (same as 90° clockwise), (x, y) → (y, −x). Notice that applying the 90° rule twice gives the 180° rule, and three times gives 270° — the rules compose.

On the coordinate plane, these rules come from the angle addition in trigonometry, but you can derive them geometrically. When you rotate a point by 90° counterclockwise, the new x-coordinate equals the old y-coordinate negated (the point moved from the positive x-axis side toward the positive y-axis side), and the new y-coordinate equals the old x-coordinate. Drawing this out on graph paper for a few points builds the muscle memory faster than memorizing the formulas abstractly.

Rotating about a point other than the origin requires a three-step process. First, **translate** so the center of rotation moves to the origin (subtract the center's coordinates from every point). Second, **apply the rotation formula** as if rotating about the origin. Third, **translate back** (add the center's coordinates back). This works because rotation rules are defined relative to the origin — you temporarily relocate the center of rotation to the origin, do the rotation, then move everything back. For instance, to rotate point (5, 3) by 90° about center (2, 1): subtract the center to get (3, 2), apply the 90° rule to get (−2, 3), add the center back to get (0, 4).
