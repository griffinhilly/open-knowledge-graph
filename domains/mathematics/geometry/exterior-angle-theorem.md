---
id: exterior-angle-theorem
title: Exterior Angle Theorem
domain: mathematics
course: geometry
prerequisites:
  - id: triangle-angle-sum
    type: hard
  - id: angle-pairs
    type: hard
builds-toward:
  - triangle-inequality
  - polygon-angle-sums
tags: [triangles, exterior-angles, angle-relationships]
stage: abstract-reasoning
status: validated
---

# Exterior Angle Theorem

## Core Idea
An exterior angle of a triangle is formed by extending one side. The Exterior Angle Theorem states that the measure of an exterior angle equals the sum of the two nonadjacent (remote) interior angles. This follows directly from the Triangle Angle Sum Theorem: the exterior angle and its adjacent interior angle are supplementary, so the exterior angle equals 180 minus the adjacent interior, which equals the sum of the other two.

## How It's Best Learned
Draw several triangles with extended sides. Measure to verify the relationship. Prove it algebraically from the angle sum theorem. Give problems where students must find exterior angles, and vice versa. Emphasize that this gives a quick shortcut for many angle problems.

## Common Misconceptions
- Confusing the exterior angle with one of the remote interior angles.
- Forgetting which two interior angles are "remote" (nonadjacent) to a given exterior angle.
- Thinking every triangle has only one exterior angle (each vertex has two, and there are six total, in congruent pairs).

## Explainer

You know from the **Triangle Angle Sum Theorem** that the three interior angles of any triangle always add to 180°. The Exterior Angle Theorem is a short but powerful consequence of that fact. When you extend one side of a triangle past a vertex, the angle formed outside the triangle — the **exterior angle** — has a surprisingly direct relationship to the triangle's interior angles.

Here's the proof in two steps. Call the interior angles A, B, and C, where C is the angle adjacent to the exterior angle we'll call E. Because E and C are on a straight line, they are **supplementary**: E + C = 180°. But we also know A + B + C = 180°. Setting these equal: E + C = A + B + C. Subtract C from both sides and you get E = A + B. The exterior angle equals the sum of the two **remote interior angles** — the two interior angles that are *not* adjacent to it.

This result is more useful than it first appears because it converts a two-step calculation (find the third angle, subtract from 180°) into a one-step shortcut. If you know two angles of a triangle are 40° and 65°, you immediately know the exterior angle at the third vertex is 105° — no subtraction from 180° needed. The theorem also gives you a quick inequality: an exterior angle is always *larger* than either of the remote interior angles individually, since it equals their sum and both are positive. This inequality is actually the key ingredient in proving the Triangle Inequality (that any side of a triangle is shorter than the sum of the other two).

A common source of confusion is identifying the *right* remote interior angles for a given exterior angle. Remember: only one exterior angle is formed at each extended vertex, and the remote angles are the *other* two interior angles — the ones at the far ends of the triangle, not the one sitting right next to the exterior angle. Drawing a fresh diagram and labeling all three interior angles before using the theorem eliminates most errors.
