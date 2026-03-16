---
id: root-locus-construction-rules
title: Root Locus Construction Rules
domain: engineering
course: control-systems
prerequisites:
- id: root-locus-method
  type: hard
- id: transfer-functions-control
  type: hard
tags:
- root-locus
- asymptotes
- breakaway-points
- departure-angles
- arrival-angles
- real-axis-segments
stage: advanced
status: draft
---

# Root Locus Construction Rules

## Core Idea
The root locus construction rules provide a systematic procedure for sketching the paths of closed-loop poles as gain K varies from 0 to ∞ without solving the characteristic equation numerically. The key rules are: (1) the number of branches equals the number of open-loop poles n; (2) branches start at open-loop poles (K = 0) and terminate at open-loop zeros or at infinity (K → ∞); (3) the locus is symmetric about the real axis; (4) real-axis segments exist to the left of an odd total count of real-axis poles and zeros; (5) n − m branches go to infinity along asymptotes with angles θ = 180°(2k + 1)/(n − m) emanating from the centroid σ_a = (Σpoles − Σzeros)/(n − m); (6) breakaway and break-in points on the real axis satisfy dK/ds = 0, found by differentiating K = −1/G(s)H(s); (7) departure angles from complex poles and arrival angles at complex zeros are computed from the angle condition by summing contributions from all other poles and zeros. Together these rules allow accurate hand-sketching of the locus, revealing how gain selection affects stability, damping, and natural frequency.

## How It's Best Learned
Apply the full rule set to progressively more complex open-loop transfer functions: start with two-pole systems, then three poles and one zero, then systems with complex pole pairs. Sketch each locus by hand, computing asymptote angles, centroids, breakaway points, and departure angles step by step, then overlay your sketch on MATLAB's rlocus() output to identify where your approximation deviates and why.

## Common Misconceptions
- Breakaway points do not always lie midway between adjacent poles — they are determined by dK/ds = 0 and can be at non-obvious locations, especially when zeros are present.
- The centroid formula (Σpoles − Σzeros)/(n − m) only determines where the asymptotes radiate from, not where the locus branches themselves intersect; branches may curve significantly before approaching the asymptotes.
- Departure angles from complex poles are not optional refinements — without computing them, sketches of systems with complex open-loop poles will be qualitatively wrong, potentially missing whether branches initially move toward or away from the right half-plane.

## Explainer

The root locus you studied introduced the concept: as gain K increases from 0 to ∞, the closed-loop poles trace continuous paths in the complex plane. The construction rules make those paths sketchable by hand, deriving everything from a single condition — the **angle condition**: a point s lies on the root locus if and only if ∠G(s)H(s) = ±180°(2k+1) for some integer k. Every construction rule is a consequence of enforcing this condition in a different geometric setting.

Rules 1–4 build the skeleton. **Branches** equal the number of open-loop poles n, each starting at a pole (K=0, where the closed-loop pole coincides with the open-loop pole) and ending at a zero or at infinity (K→∞). Symmetry about the real axis follows from the fact that characteristic polynomial coefficients are real — complex roots come in conjugate pairs, so if s is on the locus, so is s*. The **real-axis rule** derives from the angle condition evaluated on the real axis: complex poles and zeros each contribute ±180° that cancel in conjugate pairs, leaving only real-axis elements to contribute phase. Each real pole or zero to the right of a test point contributes ±180°. The net angle is ±180°(odd) exactly when there is an odd number of real poles and zeros to the right — so those segments belong to the locus.

Rules 5–7 handle the harder geometry. The **asymptote rule** describes the n−m branches headed to infinity. Far from the origin, all finite poles and zeros merge into an equivalent system with n−m excess poles concentrated at the **centroid** σ_a = (Σpoles − Σzeros)/(n−m). The asymptote angles θ = 180°(2k+1)/(n−m) distribute these branches evenly around the centroid. A 3-pole, 1-zero system has two branches going to infinity at ±90° from the centroid — regardless of where the specific poles and zeros sit. **Breakaway and break-in points** are where the locus enters or leaves the real axis; multiple branches pass through the same point at the same gain, which requires dK/ds = 0. **Departure angles** from complex poles are computed by applying the angle condition at a point infinitesimally close to the pole: the contributions from all other poles and zeros are known, and the required total of ±180° determines which direction the branch must depart.

Together, the rules give a qualitative picture of how all closed-loop poles move across all gain values simultaneously — something no single root-finding computation can provide. The design payoff: if a set of open-loop poles places locus branches heading toward the right half-plane at moderate gain, you can add a compensator zero to bend them back. If the asymptotes project into the right half-plane, you can shift the centroid leftward by adding a pole-zero pair that adjusts Σpoles − Σzeros. The construction rules are the analytical vocabulary for reading and manipulating this picture systematically.
