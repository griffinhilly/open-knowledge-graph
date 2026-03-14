---
id: distributed-loads-beams
title: Distributed Loads on Beams
domain: engineering
course: statics-and-dynamics
prerequisites:
- id: support-reactions-beams
  type: hard
- id: equivalent-force-systems
  type: soft
builds-toward:
- shear-force-bending-moment-diagrams
- internal-forces-members
tags:
- statics
- beams
- distributed loads
- equivalent point loads
- integration
stage: formal-systems
status: draft
---

# Distributed Loads on Beams

## Core Idea
Distributed loads are forces spread continuously over a length (force per unit length, w(x), in N/m or lb/ft) rather than applied at a single point. A uniform distributed load has constant intensity; a triangularly or arbitrarily varying load changes along the beam's length. For calculating support reactions and external equilibrium, a distributed load can be replaced by a single equivalent resultant force equal to the area under the loading diagram, acting at the centroid of that area. The resultant magnitude is F_R = integral of w(x) dx over the loaded length, and its location x-bar is determined by the first moment of the loading area. This equivalence holds only for external equilibrium — internal force calculations at a specific section require the actual distributed load, not the resultant.

## How It's Best Learned
Sketch the loading diagram as a geometric shape (rectangle for uniform, triangle for linearly varying) and compute its area and centroid using known formulas before resorting to integration. For combined loadings, break the distribution into simpler shapes and superpose their resultants. Always verify by checking that the sum of reaction forces equals the total resultant load.

## Common Misconceptions
- Placing the equivalent resultant at the midpoint of the loaded span rather than at the centroid of the loading shape — these coincide only for uniform loads.
- Using the equivalent resultant to find internal forces at a cut section, where only the portion of the distributed load on one side of the cut should be included.
- Confusing force per unit length (w, in N/m) with total force (F, in N) — units must be tracked carefully.
