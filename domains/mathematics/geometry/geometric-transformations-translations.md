---
id: geometric-transformations-translations
title: "Geometric Transformations: Translations"
domain: mathematics
course: geometry
prerequisites:
  - id: coordinate-plane-intro
    type: hard
builds-toward:
  - reflections
  - dilations
  - coordinate-geometry-proofs
tags: [transformations, translations, rigid-motions, vectors]
stage: abstract-reasoning
status: validated
---

# Geometric Transformations: Translations

## Core Idea
A translation slides every point of a figure the same distance in the same direction. It is defined by a translation vector (a, b), which maps each point (x, y) to (x+a, y+b). Translations are rigid motions (isometries): they preserve distance, angle measure, and orientation. The image is congruent to the preimage. Translations can be described using vector notation or coordinate rules.

## How It's Best Learned
Start with sliding physical shapes on grid paper. Introduce vector notation and the coordinate rule. Practice translating individual points, then entire figures. Verify that distances and angles are preserved. Connect to real-world examples (sliding a puzzle piece, scrolling a screen).

## Common Misconceptions
- Confusing translation direction (positive y is up, not down).
- Thinking translations change the size or shape of the figure.
- Mixing up the coordinate rule signs (adding when should subtract, or vice versa).

## Explainer

You already know how to plot points and navigate the coordinate plane — now you can use that knowledge to move entire figures with mathematical precision. A **translation** is the simplest geometric transformation: every point in the figure slides the same distance in the same direction. If you translate a triangle 3 units right and 2 units up, every vertex moves exactly 3 right and 2 up. The shape does not rotate, flip, or resize — it simply relocates.

The coordinate rule captures this precisely. A translation by **vector (a, b)** maps every point (x, y) to (x + a, y + b). If a is positive, points move right; if negative, they move left. If b is positive, points move up; if negative, they move down. To translate a whole figure, apply the rule to each vertex and reconnect. For example, translating the point (2, 5) by vector (−3, 4) gives (2 + (−3), 5 + 4) = (−1, 9). The vector tells you both direction and distance in one compact notation.

Because every point moves by the same displacement, translations are **isometries** — they preserve distance, angle measure, and shape. The translated figure (called the **image**) is congruent to the original (the **preimage**). You can verify this with coordinates: if two points P and Q are distance d apart, their images P' and Q' are still distance d apart, because adding the same constant to both coordinates cancels out in the distance formula. **Orientation** is also preserved — clockwise stays clockwise — which distinguishes translations from reflections, which flip orientation.

Translations appear everywhere in mathematics and its applications. In computer graphics, sliding an object across the screen is a translation. In physics, a rigid body moving without rotating undergoes pure translation. In more advanced geometry, you will find that two translations compose to another translation (just add the vectors), but a translation followed by a rotation produces a more complex transformation. These composition rules make the set of all translations a group under composition — a structure that becomes important in abstract algebra. For now, the key intuition is that a translation is the purest kind of motion: everything moves together, nothing changes shape, and the rule is just addition.
