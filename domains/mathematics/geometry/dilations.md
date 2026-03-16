---
id: dilations
title: 'Geometric Transformations: Dilations'
domain: mathematics
course: geometry
prerequisites:
- id: similar-triangles-aa
  type: hard
- id: coordinate-plane-intro
  type: hard
- id: geometric-transformations-translations
  type: soft
builds-toward:
- coordinate-geometry-proofs
tags:
- transformations
- dilations
- similarity
- scale-factor
stage: abstract-reasoning
status: validated
---
# Geometric Transformations: Dilations

## Core Idea
A dilation scales a figure by a scale factor k from a center of dilation. Each point moves along the ray from the center through the point, to k times its original distance from the center. If k > 1, the figure enlarges; if 0 < k < 1, it shrinks; if k < 0, it also reflects. Dilations preserve angle measures and shape (the image is similar to the preimage) but not distances (unless k = 1). For a dilation centered at the origin, (x, y) maps to (kx, ky).

## How It's Best Learned
Draw a figure and its dilation from a center point using rays and a scale factor. Verify that angles are preserved and sides are proportional. Practice with the coordinate rule for dilations centered at the origin. Explore non-origin centers. Connect dilations to similarity: two figures are similar if and only if one can be obtained from the other by a sequence of rigid motions and dilations.

## Common Misconceptions
- Thinking a dilation with k < 1 makes the figure "negative" (it just makes it smaller).
- Forgetting that dilations change distances but preserve angles.
- Assuming dilations are always centered at the origin.
- Confusing dilation (changes size) with translation (changes position).

## Explainer

You already know that similar triangles have equal angles and proportional sides — one is a scaled version of the other. A **dilation** is the transformation that makes this precise: it's the exact geometric operation that produces similarity. Given a **center of dilation** O and a **scale factor** k, every point P moves to a new point P' such that O, P, and P' are collinear, and OP' = k · OP. The point travels along the ray from O through P, stopping at k times its original distance from O. When k = 2, every point doubles its distance from O; the figure doubles in size but keeps its exact shape.

From the coordinate plane you know well, dilations centered at the origin are especially clean: the point (x, y) maps to (kx, ky). You're scaling both coordinates by the same factor. This is why dilations preserve angle measures — if you scale x and y by the same k, the ratio that determines any angle stays constant. What changes is distance: the distance between two points scales by |k|. This is the crucial contrast with the rigid motions (translations, rotations, reflections) you've seen: rigid motions preserve all distances and angles, so the image is congruent to the preimage. Dilations preserve angles but scale distances, so the image is **similar** to the preimage, not congruent (unless k = 1).

The sign and magnitude of k determine the character of the transformation. When k > 1, the figure enlarges. When 0 < k < 1, it shrinks — every point moves closer to the center, but the shape is intact. When k < 0, something more interesting happens: the point P' lands on the opposite side of O from P (since you're traveling a negative distance along the ray from O through P). This simultaneously scales and reflects through the center, producing a figure that is similar to the original but rotated 180°. The magnitude |k| still controls the size change.

For dilations with non-origin centers, you can always translate so that the center lands at the origin, apply the coordinate rule, then translate back — connecting your knowledge of translations directly. Two figures are similar if and only if one can be mapped to the other by a sequence of dilations and rigid motions. So dilations are the missing piece that completes the similarity story: congruence transformations (rigid motions alone) plus dilation gives the full family of similarity transformations. Every similar-triangles result from your AA similarity work corresponds to a concrete dilation you could explicitly construct.
