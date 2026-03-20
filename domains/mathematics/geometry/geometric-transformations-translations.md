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

## Questions

```yaml
- question: "Point A is at (3, −2). It is translated by vector (−5, 4). What are the coordinates of A'?"
  type: multiple-choice
  options:
    - "(8, −6)"
    - "(−2, 2)"
    - "(−15, −8)"
    - "(3, −2) — a translation doesn't change coordinates"
  answer: 1
  explanation: "Apply the rule (x + a, y + b): (3 + (−5), −2 + 4) = (−2, 2). Option A adds 5 instead of −5 — a sign error that is the most common mistake. Option C multiplies instead of adds, confusing translation with dilation. Option D misunderstands what a translation does. A translation always adds the vector components; it never multiplies or leaves coordinates unchanged (unless the vector is (0, 0))."

- question: "A triangle with side lengths 3, 4, and 5 is translated 20 units to the left. What are the side lengths of the image?"
  type: multiple-choice
  options:
    - "3, 4, and 5 — translations preserve all distances"
    - "23, 24, and 25 — the translation distance is added to each side"
    - "−17, −16, and −15 — moving left subtracts from the measurements"
    - "It depends on the orientation of the triangle"
  answer: 0
  explanation: "Translations are isometries — they preserve all distances. Side lengths are unchanged regardless of how far or in what direction the figure moves. Only dilations change size. The translation vector affects position, not shape or size. A common misconception conflates moving a figure with scaling it."

- question: "Two consecutive translations — first by vector (3, −1) and then by (−7, 4) — produce the same result as a single translation by (−4, 3)."
  type: true-false
  answer: true
  explanation: "Translations compose by vector addition: (3 + (−7), −1 + 4) = (−4, 3). The combined effect is always another translation. This works because each translation applies the same constant addition to every point, and additions accumulate linearly. The set of all translations forms a group under composition — a structure where combining two elements always yields another element of the same type."

- question: "Translating a figure can change its orientation — for example, a clockwise-oriented triangle may become counterclockwise-oriented after translation."
  type: true-false
  answer: false
  explanation: "Translations preserve orientation. Every point moves by the same displacement, so there is no flipping or rotating. Clockwise stays clockwise; counterclockwise stays counterclockwise. Orientation reversal is caused by reflections (which flip the figure), not translations. This is one of the key distinctions between translation and reflection as types of rigid motions."

- question: "Explain why a translation is called an isometry, and what this guarantees about the relationship between a figure and its translated image."
  type: short-answer
  answer: "An isometry is a transformation that preserves all distances. In a translation by vector (a, b), every point (x, y) maps to (x+a, y+b). If two points P and Q are distance d apart, their images P' and Q' are still distance d apart — the added constants (a, b) cancel when you compute the distance between them. Since all distances are preserved, angle measures are also preserved (angles depend only on distances between three points). The image is therefore congruent to the preimage: same shape, same size, different location."
  explanation: "Congruence is the practical payoff of isometry. Whenever you need to prove two figures are congruent in geometry, demonstrating they are related by a translation (or other isometry) is a valid proof strategy. The isometry property is also what distinguishes translations from dilations, which scale distances and produce similar but not congruent images."
```

## Explainer

You already know how to plot points and navigate the coordinate plane — now you can use that knowledge to move entire figures with mathematical precision. A **translation** is the simplest geometric transformation: every point in the figure slides the same distance in the same direction. If you translate a triangle 3 units right and 2 units up, every vertex moves exactly 3 right and 2 up. The shape does not rotate, flip, or resize — it simply relocates.

The coordinate rule captures this precisely. A translation by **vector (a, b)** maps every point (x, y) to (x + a, y + b). If a is positive, points move right; if negative, they move left. If b is positive, points move up; if negative, they move down. To translate a whole figure, apply the rule to each vertex and reconnect. For example, translating the point (2, 5) by vector (−3, 4) gives (2 + (−3), 5 + 4) = (−1, 9). The vector tells you both direction and distance in one compact notation.

Because every point moves by the same displacement, translations are **isometries** — they preserve distance, angle measure, and shape. The translated figure (called the **image**) is congruent to the original (the **preimage**). You can verify this with coordinates: if two points P and Q are distance d apart, their images P' and Q' are still distance d apart, because adding the same constant to both coordinates cancels out in the distance formula. **Orientation** is also preserved — clockwise stays clockwise — which distinguishes translations from reflections, which flip orientation.

Translations appear everywhere in mathematics and its applications. In computer graphics, sliding an object across the screen is a translation. In physics, a rigid body moving without rotating undergoes pure translation. In more advanced geometry, you will find that two translations compose to another translation (just add the vectors), but a translation followed by a rotation produces a more complex transformation. These composition rules make the set of all translations a group under composition — a structure that becomes important in abstract algebra. For now, the key intuition is that a translation is the purest kind of motion: everything moves together, nothing changes shape, and the rule is just addition.
