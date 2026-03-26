---
id: perpendicular-bisectors
title: Perpendicular Bisectors
domain: mathematics
course: geometry
prerequisites:
- id: midpoint-formula
  type: hard
- id: segment-and-distance
  type: hard
- id: cpctc
  type: soft
- id: isosceles-triangle-theorem
  type: soft
builds-toward:
- coordinate-geometry-proofs
tags:
- bisectors
- perpendicular
- circumcenter
- equidistance
stage: abstract-reasoning
status: validated
---
# Perpendicular Bisectors

## Core Idea
A perpendicular bisector of a segment is a line that is perpendicular to the segment at its midpoint. The Perpendicular Bisector Theorem states that any point on the perpendicular bisector is equidistant from the two endpoints. The converse also holds. The three perpendicular bisectors of a triangle's sides are concurrent at the circumcenter, which is equidistant from all three vertices.

## How It's Best Learned
Construct perpendicular bisectors with compass and straightedge. Verify equidistance by measurement. Prove the theorem using congruent triangles (SSS or SAS with the right angle). Explore the circumcenter by constructing all three perpendicular bisectors of a triangle and observing they meet at a single point.

## Common Misconceptions
- Confusing perpendicular bisectors with angle bisectors (different constructions, different concurrency points).
- Thinking the circumcenter is always inside the triangle (it is outside for obtuse triangles).
- Forgetting that "perpendicular bisector" requires both conditions: perpendicular AND bisecting.

## Questions

```yaml
- question: "Point P is equidistant from the two endpoints of segment AB (PA = PB). What can you conclude about P?"
  type: multiple-choice
  options:
    - "P is the midpoint of AB"
    - "P lies on the perpendicular bisector of AB"
    - "P is the circumcenter of any triangle containing AB"
    - "P lies on the angle bisector of any angle formed at A or B"
  answer: 1
  explanation: "By the converse of the Perpendicular Bisector Theorem, equidistance from both endpoints is sufficient to place P on the perpendicular bisector of AB — this is the biconditional at the heart of the theorem. P being the midpoint (option A) would require P to be *on* AB, not just equidistant. And equidistance from two vertices only, not all three, is not enough to make P the circumcenter."

- question: "A triangle has one obtuse angle. Where is its circumcenter located?"
  type: multiple-choice
  options:
    - "At the midpoint of the longest side"
    - "Inside the triangle, near the obtuse vertex"
    - "Outside the triangle, beyond the longest side"
    - "At the vertex of the obtuse angle"
  answer: 2
  explanation: "For an obtuse triangle, the three perpendicular bisectors intersect at a point outside the triangle — on the far side of the longest side, opposite the obtuse angle. The common misconception is that the circumcenter is always interior, which is only true for acute triangles. For a right triangle, it falls exactly at the midpoint of the hypotenuse."

- question: "Any point that is equidistant from both endpoints of a segment must lie on the perpendicular bisector of that segment."
  type: true-false
  answer: true
  explanation: "This is the converse of the Perpendicular Bisector Theorem, and it holds. The theorem is actually a biconditional: a point lies on the perpendicular bisector of a segment *if and only if* it is equidistant from both endpoints. Equidistance is not merely consistent with lying on the bisector — it guarantees it."

- question: "The circumcenter of a triangle is generally located inside the triangle."
  type: true-false
  answer: false
  explanation: "The circumcenter is inside only for acute triangles. For a right triangle, it lies exactly at the midpoint of the hypotenuse (on the triangle's boundary). For an obtuse triangle, it lies entirely outside the triangle. This is a persistent misconception that comes from confusing the circumcenter with the centroid or incenter, both of which are always interior."

- question: "Why does the Perpendicular Bisector Theorem guarantee that all three perpendicular bisectors of a triangle meet at a single point (the circumcenter)?"
  type: short-answer
  answer: "The perpendicular bisectors of sides AB and BC meet at a point O where OA = OB (from the bisector of AB) and OB = OC (from the bisector of BC). By transitivity, OA = OB = OC. By the converse theorem, any point equidistant from both endpoints of a segment lies on its perpendicular bisector — so O must also lie on the perpendicular bisector of AC. This proves all three bisectors are concurrent."
  explanation: "The key move is chaining the equidistance relationships from two bisectors, then using the converse to conclude the third bisector passes through the same point. Without the converse, you couldn't close the argument. The circumcenter's equal distance from all three vertices also directly implies it is the center of the circumscribed circle."
```

## Explainer

You know how to find the midpoint of a segment and measure distances between points. A **perpendicular bisector** combines both ideas: it is the unique line that passes through the midpoint of a segment and is perpendicular to it. But the most powerful way to think about it is not as a construction — it is the set of all points that are **equidistant** from the two endpoints. That equidistance characterization is what makes perpendicular bisectors useful.

Here is why the equidistance property holds. Let A and B be the endpoints and M their midpoint. Take any point P on the perpendicular bisector. Draw segments PA and PB. The triangles PMA and PMB share side PM, have equal legs MA = MB (M is the midpoint), and both have right angles at M (perpendicularity). By SAS congruence, the triangles are congruent, so PA = PB. The **Perpendicular Bisector Theorem** follows: every point on the perpendicular bisector is equidistant from both endpoints. The converse is equally true: if PA = PB for some point P, then P lies on the perpendicular bisector of AB. This two-way relationship — on the bisector if and only if equidistant — is the key to applying the theorem.

The circumcenter of a triangle is where this becomes powerful. Take the perpendicular bisectors of two sides of a triangle, say AB and BC. Their intersection point O satisfies OA = OB (from the bisector of AB) and OB = OC (from the bisector of BC), so OA = OB = OC. By the converse theorem, O must also lie on the perpendicular bisector of AC. This proves that all three perpendicular bisectors are **concurrent** at O, called the **circumcenter** — and since OA = OB = OC, the circumcenter is the center of the unique circle passing through all three vertices, called the **circumscribed circle** or circumcircle.

The circumcenter's location depends on the triangle's type. For an **acute** triangle, all three perpendicular bisectors intersect inside the triangle — the circumcenter is interior. For a **right** triangle, the circumcenter falls exactly at the midpoint of the hypotenuse (the hypotenuse itself is the diameter of the circumcircle — a fact related to Thales' theorem about angles in a semicircle). For an **obtuse** triangle, the circumcenter lies outside the triangle, on the opposite side of the longest side from the obtuse angle. These location shifts follow directly from where the bisectors' intersection moves as the angles change, and they provide a useful check when constructing circumcenters in coordinate geometry problems.
