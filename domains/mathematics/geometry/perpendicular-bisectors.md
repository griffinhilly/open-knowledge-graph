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

## Explainer

You know how to find the midpoint of a segment and measure distances between points. A **perpendicular bisector** combines both ideas: it is the unique line that passes through the midpoint of a segment and is perpendicular to it. But the most powerful way to think about it is not as a construction — it is the set of all points that are **equidistant** from the two endpoints. That equidistance characterization is what makes perpendicular bisectors useful.

Here is why the equidistance property holds. Let A and B be the endpoints and M their midpoint. Take any point P on the perpendicular bisector. Draw segments PA and PB. The triangles PMA and PMB share side PM, have equal legs MA = MB (M is the midpoint), and both have right angles at M (perpendicularity). By SAS congruence, the triangles are congruent, so PA = PB. The **Perpendicular Bisector Theorem** follows: every point on the perpendicular bisector is equidistant from both endpoints. The converse is equally true: if PA = PB for some point P, then P lies on the perpendicular bisector of AB. This two-way relationship — on the bisector if and only if equidistant — is the key to applying the theorem.

The circumcenter of a triangle is where this becomes powerful. Take the perpendicular bisectors of two sides of a triangle, say AB and BC. Their intersection point O satisfies OA = OB (from the bisector of AB) and OB = OC (from the bisector of BC), so OA = OB = OC. By the converse theorem, O must also lie on the perpendicular bisector of AC. This proves that all three perpendicular bisectors are **concurrent** at O, called the **circumcenter** — and since OA = OB = OC, the circumcenter is the center of the unique circle passing through all three vertices, called the **circumscribed circle** or circumcircle.

The circumcenter's location depends on the triangle's type. For an **acute** triangle, all three perpendicular bisectors intersect inside the triangle — the circumcenter is interior. For a **right** triangle, the circumcenter falls exactly at the midpoint of the hypotenuse (the hypotenuse itself is the diameter of the circumcircle — a fact related to Thales' theorem about angles in a semicircle). For an **obtuse** triangle, the circumcenter lies outside the triangle, on the opposite side of the longest side from the obtuse angle. These location shifts follow directly from where the bisectors' intersection moves as the angles change, and they provide a useful check when constructing circumcenters in coordinate geometry problems.
