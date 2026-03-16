---
id: simply-connected-spaces
title: Simply Connected Spaces
domain: mathematics
course: topology
prerequisites:
- id: fundamental-group-definition
  type: hard
builds-toward:
- covering-spaces
- van-kampen-theorem
tags:
- simply-connected
- trivial-fundamental-group
- contractible
stage: advanced
status: draft
---

# Simply Connected Spaces

## Core Idea
A space is simply connected if it is path-connected and its fundamental group is trivial (every loop is homotopic to the constant loop). Intuitively, a simply connected space is path-connected with no 'holes.' Simply connected spaces form an important class in algebraic topology where global properties are heavily constrained by topology.

## Explainer

From your prerequisite on the **fundamental group**, you know that π₁(X, x₀) records the homotopy classes of loops based at x₀ — loops that can be continuously deformed into each other are identified, and the group operation is concatenation of loops. A **simply connected space** is one where this group is trivial: π₁(X, x₀) = {e}, the group with one element. Combined with path-connectedness, this means every loop in X can be continuously contracted to a point.

The intuition is best built through examples. The plane ℝ² is simply connected: any loop drawn in the plane can be shrunk to a point without leaving the plane. The 2-sphere S² is also simply connected: any loop on a sphere can be pulled to the north pole. But the circle S¹ is not simply connected — a loop that goes around the circle once cannot be contracted to a point without leaving S¹. The **fundamental group of S¹ is ℤ**, with the integer recording how many times a loop winds around. Similarly, the torus T² = S¹ × S¹ has π₁ = ℤ × ℤ, capturing two independent types of non-contractible loops (going around the hole, and going through the hole). The "holes" that obstruct simple connectivity are 1-dimensional tunnels or punctures — removing a point from ℝ² creates a copy of ℝ² \ {0}, which deformation retracts to S¹ and so has π₁ = ℤ.

A subtlety: simple connectivity is specifically about **1-dimensional** holes. A space can be simply connected yet still have interesting higher homotopy groups. The 2-sphere S² is simply connected (no 1-dimensional loops) but has nontrivial π₂ — there are 2-spheres worth of holes. The simply connected condition rules out the "simplest" kind of topological obstruction, which is why it appears as a hypothesis in many theorems. In complex analysis, the proof that every holomorphic function on a simply connected domain has an antiderivative, and Cauchy's theorem that loop integrals vanish, both hinge on simply connectivity: the absence of 1-dimensional holes is exactly what prevents line integrals from being path-dependent.

Simply connected spaces are the "nicely behaved" spaces for much of algebraic topology. **Covering space theory** is most transparent over a simply connected base: the universal cover of any connected, locally path-connected, semi-locally simply connected space is itself simply connected, and it is the "largest" covering space. The **van Kampen theorem**, which you will study next, computes fundamental groups by breaking a space into simpler pieces — and the pieces you want to be "invisible" to the fundamental group computation are exactly the simply connected ones. Simply connected spaces also arise in differential geometry (the Poincaré conjecture concerns which 3-manifolds are simply connected and topologically equivalent to the 3-sphere) and physics (gauge theories and the existence of potentials are constrained by the topology of configuration spaces).
