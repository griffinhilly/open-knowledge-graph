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
