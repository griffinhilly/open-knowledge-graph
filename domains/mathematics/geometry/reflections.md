---
id: reflections
title: "Geometric Transformations: Reflections"
domain: mathematics
course: geometry
prerequisites:
  - id: geometric-transformations-translations
    type: soft
  - id: coordinate-plane-intro
    type: hard
builds-toward:
  - rotations
  - coordinate-geometry-proofs
tags: [transformations, reflections, rigid-motions, symmetry]
stage: abstract-reasoning
status: validated
---

# Geometric Transformations: Reflections

## Core Idea
A reflection flips a figure over a line of reflection. Each point maps to a point the same distance from the line but on the opposite side. Key coordinate rules: reflection over the x-axis maps (x, y) to (x, -y); over the y-axis to (-x, y); over y = x to (y, x). Reflections are rigid motions that preserve distance and angle measure but reverse orientation (the image is a mirror image, not a direct copy).

## How It's Best Learned
Use mirrors or folding paper to demonstrate reflections physically. Practice reflecting points and figures over the x-axis, y-axis, and the line y = x. Note the orientation reversal: a clockwise-labeled figure becomes counterclockwise. Explore lines of symmetry in figures.

## Common Misconceptions
- Confusing the coordinate rules for different lines of reflection.
- Not recognizing that reflections reverse orientation (turn clockwise into counterclockwise).
- Thinking the line of reflection must be horizontal or vertical (it can be any line).

## Questions

```yaml
- question: "Triangle ABC has vertices A(2, 3), B(5, 1), C(4, 6). It is reflected over the y-axis. What are the coordinates of the image vertex A'?"
  type: multiple-choice
  options:
    - "(2, -3)"
    - "(-2, 3)"
    - "(-2, -3)"
    - "(3, 2)"
  answer: 1
  explanation: "Reflection over the y-axis maps (x, y) to (−x, y): the x-coordinate changes sign, the y-coordinate stays the same. So A(2, 3) maps to A'(−2, 3). A common error is flipping both coordinates (which would be reflection over the origin, not the y-axis) or swapping them (which is reflection over y = x). Each axis of reflection has its own rule: y-axis changes x, x-axis changes y, and y = x swaps them."

- question: "A figure is reflected over the line y = x. The original figure has vertices labeled clockwise as P, Q, R. After the reflection, how are the image vertices oriented?"
  type: multiple-choice
  options:
    - "Clockwise — reflections preserve orientation"
    - "Counterclockwise — reflections reverse orientation"
    - "Clockwise — the line y = x is a special case that preserves orientation"
    - "The orientation depends on the specific coordinates of P, Q, R"
  answer: 1
  explanation: "All reflections reverse orientation — this is a fundamental property that distinguishes reflections (indirect isometries) from translations and rotations (direct isometries). If vertices are labeled clockwise before a reflection, they are labeled counterclockwise after, for any line of reflection. The line y = x has no special exception. Think of it physically: a reflection is like lifting a figure off the table and flipping it over — the mirror image of a clockwise-labeled triangle is always counterclockwise."

- question: "A reflection is a rigid motion, which means it preserves the distances between all points and the measures of all angles in the figure."
  type: true-false
  answer: true
  explanation: "Correct. Reflections are isometries (rigid motions) — the image is always congruent to the original figure. Distance between any two points is preserved, and all angle measures are preserved. What a reflection changes is orientation: clockwise becomes counterclockwise. This distinguishes reflections from non-rigid transformations like dilations, which scale distances."

- question: "The line of reflection is expected to be one of the coordinate axes or the line y = x — reflections over other lines are not standard geometric transformations."
  type: true-false
  answer: false
  explanation: "A reflection can be defined over any line in the plane — horizontal, vertical, diagonal, or any oblique line like y = 2x + 1. The coordinate axis reflections and y = x are taught first because they have clean algebraic rules, but they are special cases of the general definition. The perpendicular bisector definition works for any line: the line of reflection is the perpendicular bisector of the segment connecting each original point to its image. Reflections over general lines require more computation (finding the foot of the perpendicular) but are fully standard transformations."

- question: "Explain what it means for the line of reflection to be the 'perpendicular bisector' of each point and its image, and why this fully determines where every point maps to."
  type: short-answer
  answer: "For any point P and its image P' under a reflection, the line of reflection sits exactly halfway between them (bisects the segment PP') and crosses PP' at a right angle (is perpendicular to it). This two-part condition uniquely determines P': given P and the line of reflection, there is exactly one point P' such that the line perpendicularly bisects PP'. To find P', you drop a perpendicular from P to the line, find the foot F of that perpendicular, then extend the same distance on the other side: P' is the point such that F is the midpoint of PP' and PP' is perpendicular to the line."
  explanation: "The perpendicular bisector definition works for any line of reflection and explains why the coordinate rules work. For reflection over the x-axis: the midpoint of (x,y) and (x,−y) is (x,0) which lies on the x-axis, and the segment from (x,y) to (x,−y) is vertical (perpendicular to the horizontal x-axis). Both conditions of the perpendicular bisector are satisfied, confirming the rule is correct."
```

## Explainer

You already know translations from your prerequisites — a translation slides every point of a figure the same distance in the same direction, and the figure lands in a new position with the same orientation. A **reflection** is a different kind of rigid motion: instead of sliding, it flips. Every point maps to a mirror image across a fixed **line of reflection**. The precise rule is that the line of reflection is the **perpendicular bisector** of the segment connecting each original point to its image. This means the line sits exactly halfway between the original and its image, and the connecting segment crosses the line at a right angle.

On the coordinate plane, the most important reflections have clean algebraic rules. Reflection over the **x-axis** maps (x, y) to (x, −y): the x-coordinate stays, the y-coordinate flips sign. Reflection over the **y-axis** maps (x, y) to (−x, y): the y-coordinate stays, the x-coordinate flips. Reflection over the line **y = x** maps (x, y) to (y, x): the coordinates swap. You can derive each of these from the perpendicular bisector definition — the x-axis sits halfway between y and −y, and the segment from (x, y) to (x, −y) is vertical, which is perpendicular to the horizontal x-axis.

Reflections are **rigid motions**, also called isometries: they preserve distance and angle measure, so the image is congruent to the original. But there is one thing a reflection changes that a translation does not: **orientation**. If you label the vertices of a triangle clockwise as A → B → C, after a reflection the image vertices run counterclockwise. Think of a transparent figure: you can slide it around a table (translation), but you cannot slide it to match its mirror image without lifting it off the table and flipping it. This orientation reversal is the defining difference between direct isometries (translations, rotations) and indirect isometries (reflections and glide reflections).

The line of reflection does not need to be the x-axis or y-axis — it can be any line, including diagonal lines like y = x, y = −x, or y = 2x + 1. For a general line, computing the image requires finding the foot of the perpendicular from the point to the line, then doubling the distance. This connects directly to the dot product and perpendicular projection ideas you will use in coordinate geometry proofs and linear algebra.
