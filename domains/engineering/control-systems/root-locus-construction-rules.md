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
