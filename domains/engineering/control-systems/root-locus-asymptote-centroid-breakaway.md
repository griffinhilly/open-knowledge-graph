---
id: root-locus-asymptote-centroid-breakaway
title: 'Root Locus: Asymptotes, Centroid, and Breakaway Points'
domain: engineering
course: control-systems
prerequisites:
- id: root-locus-angle-magnitude-equations
  type: hard
builds-toward:
- compensation-design-tradeoffs-cascadefeedback
tags:
- root-locus
- asymptotes
- centroid
- breakaway-points
stage: formal-systems
status: draft
---

# Root Locus: Asymptotes, Centroid, and Breakaway Points

## Core Idea
Asymptotes describe locus behavior at high frequency (σ = Σpoles - Σzeros)/(#poles - #zeros), angles = 180°(2k+1)/(n-m)). Centroid is their intersection point. Breakaway/break-in points occur where dK/ds = 0, indicating multiple roots. These features enable sketching the locus without computing every point.

## Explainer

From your work on the root locus angle and magnitude equations, you know that as gain K increases from 0 to ∞, the closed-loop poles travel continuously along paths in the s-plane that start at the open-loop poles (K = 0) and end at the open-loop zeros (K → ∞). If there are more poles than zeros — which is almost always true in physical systems — some branches cannot end at finite zeros. Instead, they travel outward toward infinity along **asymptotes**. Understanding where those asymptotes go is essential for predicting whether a high-gain system will be stable.

The **asymptote angles** are evenly spaced at 180°(2k+1)/(n−m) degrees, where n is the number of poles and m the number of zeros, and k = 0, 1, 2, … up to (n−m−1). For a system with 3 poles and 1 zero, there are 2 asymptotes at angles of 90° and 270° (straight up and straight down in the s-plane). For 3 poles and 0 zeros, the asymptotes are at 60°, 180°, and 300°. The **centroid** σ_a is where all asymptotes intersect the real axis: σ_a = (Σ real parts of poles − Σ real parts of zeros) / (n − m). This single point anchors all the asymptotes and tells you immediately whether the branches escaping to infinity are heading into the left half-plane (stable) or right half-plane (unstable). A centroid deep in the left half-plane is reassuring; a centroid near the imaginary axis warns that high-gain instability is possible.

**Breakaway and break-in points** occur where two or more branches of the locus coincide — that is, where the characteristic equation has repeated roots. On the real axis, branches that are traveling along the real axis in opposite directions will meet at some point and break away from the real axis into complex conjugate pairs (a **breakaway point**). Conversely, complex conjugate branches can meet on the real axis and re-enter it (a **break-in point**). These points occur where dK/ds = 0, since K is an implicit function of s along the locus. Differentiating the characteristic equation 1 + KG(s)H(s) = 0 gives a polynomial whose real roots are the candidate breakaway and break-in points.

Together, these three features — asymptote angles, centroid, and breakaway points — let you sketch the qualitative shape of the entire root locus with only arithmetic. You can immediately identify how many branches go unstable at high gain, roughly where they cross the imaginary axis, and whether the closed-loop poles pass through any real breakaway geometry. The sketch won't give you exact crossover frequencies (use the Routh criterion or Bode plot for that), but it gives you the topological picture of how pole locations evolve with gain — which is exactly the information needed for initial compensator design.
