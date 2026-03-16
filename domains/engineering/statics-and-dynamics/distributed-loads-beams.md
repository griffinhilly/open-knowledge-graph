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

## Explainer

From your work with support reactions, you know how to find the unknown forces and moments at beam supports when concentrated point loads and couples are applied. Distributed loads extend this problem: instead of a force at a single point, you now have a **force per unit length** w(x) (measured in N/m or lb/ft) spread continuously along the beam. The total load applied over a segment is the integral — or, geometrically, the area under the w(x) diagram. For a 4-meter beam with a uniform load of 10 N/m, the total force is simply 10 × 4 = 40 N. For a triangularly varying load, you compute the area of the triangle instead.

The key insight is the **equivalent resultant**: for the purpose of computing support reactions and checking overall equilibrium, the entire distributed load can be replaced by a single concentrated force. That resultant force has two properties: its magnitude equals the total area under the loading diagram, and it acts at the **centroid** of that area. For a uniform load, the centroid is at the midpoint of the loaded span — the resultant sits in the middle. For a triangularly varying load (zero at one end, maximum at the other), the centroid is one-third of the span from the heavier end. This is where students frequently lose points: the centroid of a triangle is not at its midpoint. Always identify the loading shape first (rectangle, triangle, trapezoid) and apply the known centroid formula rather than guessing.

This equivalence comes directly from your prerequisite knowledge of equivalent force systems: any distributed loading is, mathematically, a system of infinitely many infinitesimal forces, and you are simply computing their resultant. The resultant force and the original distribution produce identical reactions at the supports — the rest of the structure cannot "tell the difference" as far as the global equilibrium equations are concerned. This is why you can compute ΣFy = 0 and ΣM = 0 using the equivalent resultant and get the correct support reactions.

However — and this is the critical limitation — the equivalence holds **only for external equilibrium**. Once you make an imaginary cut through the beam to find internal shear forces and bending moments at a specific cross-section, you must use the actual distributed load, not the resultant. The reason is that the resultant lumps all the force at one point; that point may be on the wrong side of your cut, or at the wrong location relative to it. The correct procedure is: choose a cut location, isolate one segment, and integrate (or compute the area of) only the portion of the distributed load on that segment, applied at its own local centroid, to find the internal forces on that segment.

For combined loading diagrams — a uniform load over part of the beam plus a triangular load over another part, for example — the most reliable approach is to decompose the distribution into simple geometric shapes. Compute each shape's area and centroid independently, then treat each as its own resultant. These can then be handled by straightforward superposition in the equilibrium equations. Keeping careful track of units throughout (w in N/m, lengths in m, forces in N, moments in N·m) prevents the most common arithmetic errors.
