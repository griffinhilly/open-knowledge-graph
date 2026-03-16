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

## Explainer

You already know translations from your prerequisites — a translation slides every point of a figure the same distance in the same direction, and the figure lands in a new position with the same orientation. A **reflection** is a different kind of rigid motion: instead of sliding, it flips. Every point maps to a mirror image across a fixed **line of reflection**. The precise rule is that the line of reflection is the **perpendicular bisector** of the segment connecting each original point to its image. This means the line sits exactly halfway between the original and its image, and the connecting segment crosses the line at a right angle.

On the coordinate plane, the most important reflections have clean algebraic rules. Reflection over the **x-axis** maps (x, y) to (x, −y): the x-coordinate stays, the y-coordinate flips sign. Reflection over the **y-axis** maps (x, y) to (−x, y): the y-coordinate stays, the x-coordinate flips. Reflection over the line **y = x** maps (x, y) to (y, x): the coordinates swap. You can derive each of these from the perpendicular bisector definition — the x-axis sits halfway between y and −y, and the segment from (x, y) to (x, −y) is vertical, which is perpendicular to the horizontal x-axis.

Reflections are **rigid motions**, also called isometries: they preserve distance and angle measure, so the image is congruent to the original. But there is one thing a reflection changes that a translation does not: **orientation**. If you label the vertices of a triangle clockwise as A → B → C, after a reflection the image vertices run counterclockwise. Think of a transparent figure: you can slide it around a table (translation), but you cannot slide it to match its mirror image without lifting it off the table and flipping it. This orientation reversal is the defining difference between direct isometries (translations, rotations) and indirect isometries (reflections and glide reflections).

The line of reflection does not need to be the x-axis or y-axis — it can be any line, including diagonal lines like y = x, y = −x, or y = 2x + 1. For a general line, computing the image requires finding the foot of the perpendicular from the point to the line, then doubling the distance. This connects directly to the dot product and perpendicular projection ideas you will use in coordinate geometry proofs and linear algebra.
