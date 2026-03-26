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

## Questions

```yaml
- question: "Triangle ABC is dilated by scale factor k = −2 from the origin. Which statement correctly describes the image?"
  type: multiple-choice
  options:
    - "The image is congruent to the original — a scale factor of 2 means equal-sized figures"
    - "The image is twice as large and appears rotated 180° around the origin"
    - "The image is half as large and reflected over the x-axis"
    - "The image is congruent and reflected, since the negative sign creates a reflection without size change"
  answer: 1
  explanation: "A negative scale factor combines scaling and reflection through the center. |k| = 2 doubles each point's distance from the origin, so the image is twice as large — similar to, not congruent with, the original. The negative sign places every image point on the opposite side of O from its preimage, producing a 180° rotation effect. Option 0 confuses magnitude with congruence. Option 2 has the size backwards (|−2| = 2, not 1/2). Option 3 incorrectly claims congruence."

- question: "Point P is 5 units from the center of dilation. After a dilation with k = 3/4, how far is P' from the center, and what happened to the angle measure at P?"
  type: multiple-choice
  options:
    - "P' is 15/4 units from center; the angle at P decreased proportionally"
    - "P' is 15/4 units from center; the angle at P is unchanged"
    - "P' is 20/3 units from center; the angle at P is unchanged"
    - "P' is 20/3 units from center; the angle at P increased proportionally"
  answer: 1
  explanation: "Distance from the center scales by |k|: 5 × 3/4 = 15/4. But dilations preserve ALL angle measures — this is the defining property that makes the image similar to the preimage. The common misconception is that scaling changes angles proportionally; it does not. Angles are invariant under dilation precisely because both coordinate axes scale by the same factor k, keeping the ratio that determines any angle constant."

- question: "A dilation generally changes the position of a figure in the plane."
  type: true-false
  answer: false
  explanation: "When k = 1, every point P maps to P' such that OP' = 1 · OP — meaning P' = P for every point. The figure is unchanged in position and size. So a dilation with k = 1 is the identity transformation. A dilation also does not change the position of any point that lies at the center of dilation (it maps to itself for any k). 'Always changes position' is too strong a claim."

- question: "After a dilation, the sides of the image figure are parallel to the corresponding sides of the preimage."
  type: true-false
  answer: true
  explanation: "Dilations preserve angle measures. Since the angle each side makes with any reference direction is an angle measure, corresponding sides maintain the same orientation — they are parallel (or collinear if the center lies on the side). This is a consequence of the uniform scaling of both coordinate axes: the direction of each side (rise over run) is unchanged by k."

- question: "Why does a dilation produce a similar figure rather than a congruent one, and under what condition would the image be congruent to the preimage?"
  type: short-answer
  answer: "A dilation scales all distances from the center by |k|, changing the figure's size while preserving all angle measures. Equal angles and proportional sides is the definition of similarity, not congruence. The image is congruent only when |k| = 1 — either k = 1 (identity, no change) or k = −1 (a point reflection through the center that preserves distances while reflecting through the center)."
  explanation: "The key distinction is that congruence requires preserving distances AND angles, while similarity only requires preserving angles (distances may scale). A dilation with |k| ≠ 1 specifically changes the scale, which is why it produces similarity. This is why dilations are the 'missing transformation' in the similarity story: rigid motions give congruence; rigid motions plus dilation give the full family of similarity transformations."
```

## Explainer

You already know that similar triangles have equal angles and proportional sides — one is a scaled version of the other. A **dilation** is the transformation that makes this precise: it's the exact geometric operation that produces similarity. Given a **center of dilation** O and a **scale factor** k, every point P moves to a new point P' such that O, P, and P' are collinear, and OP' = k · OP. The point travels along the ray from O through P, stopping at k times its original distance from O. When k = 2, every point doubles its distance from O; the figure doubles in size but keeps its exact shape.

From the coordinate plane you know well, dilations centered at the origin are especially clean: the point (x, y) maps to (kx, ky). You're scaling both coordinates by the same factor. This is why dilations preserve angle measures — if you scale x and y by the same k, the ratio that determines any angle stays constant. What changes is distance: the distance between two points scales by |k|. This is the crucial contrast with the rigid motions (translations, rotations, reflections) you've seen: rigid motions preserve all distances and angles, so the image is congruent to the preimage. Dilations preserve angles but scale distances, so the image is **similar** to the preimage, not congruent (unless k = 1).

The sign and magnitude of k determine the character of the transformation. When k > 1, the figure enlarges. When 0 < k < 1, it shrinks — every point moves closer to the center, but the shape is intact. When k < 0, something more interesting happens: the point P' lands on the opposite side of O from P (since you're traveling a negative distance along the ray from O through P). This simultaneously scales and reflects through the center, producing a figure that is similar to the original but rotated 180°. The magnitude |k| still controls the size change.

For dilations with non-origin centers, you can always translate so that the center lands at the origin, apply the coordinate rule, then translate back — connecting your knowledge of translations directly. Two figures are similar if and only if one can be mapped to the other by a sequence of dilations and rigid motions. So dilations are the missing piece that completes the similarity story: congruence transformations (rigid motions alone) plus dilation gives the full family of similarity transformations. Every similar-triangles result from your AA similarity work corresponds to a concrete dilation you could explicitly construct.
