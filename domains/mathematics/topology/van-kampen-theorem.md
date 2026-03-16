---
id: van-kampen-theorem
title: van Kampen's Theorem
domain: mathematics
course: topology
prerequisites:
- id: fundamental-group-definition
  type: hard
- id: covering-spaces
  type: soft
builds-toward:
- classification-compact-surfaces
tags:
- van-kampen
- fundamental-group
- amalgamated-product
stage: advanced
status: draft
---

# van Kampen's Theorem

## Core Idea
van Kampen's theorem computes the fundamental group of a space glued from pieces: π₁(X) ≅ π₁(U) *_{π₁(U∩V)} π₁(V) when X = U ∪ V with overlapping U and V. This is the fundamental tool for computing fundamental groups of complex spaces from simpler pieces.

## Explainer

You know the fundamental group π₁(X, x₀): equivalence classes of loops based at x₀, where two loops are equivalent if one can be continuously deformed into the other (homotopy). Computing π₁ directly from the definition requires finding all loops and checking which homotopies exist, which is intractable for any but the simplest spaces. Van Kampen's theorem is the systematic computational engine: it expresses the fundamental group of a space assembled from pieces in terms of the fundamental groups of those pieces.

The setup: suppose X = U ∪ V where U and V are open, path-connected subsets of X, and their intersection U ∩ V is also path-connected (all three share a common basepoint). Then π₁(X) is the **amalgamated free product** π₁(U) \*_{π₁(U∩V)} π₁(V). Concretely, this means: take all the loops from U and all the loops from V as generators, and impose exactly the relations that come from U ∩ V — any loop in U ∩ V that looks like one loop when viewed inside U must equal the "same" loop when viewed inside V. No other relations are imposed.

The **wedge sum** S¹ ∨ S¹ (two circles joined at a point) illustrates the theorem cleanly. Take U to be an open neighborhood of the first circle (slightly overlapping the second near the join point), and V to be an open neighborhood of the second circle. Each of U and V deformation-retracts to a circle, so π₁(U) ≅ π₁(V) ≅ ℤ. The intersection U ∩ V deformation-retracts to the join point, which is simply connected: π₁(U ∩ V) = {e}. The amalgamated free product over a trivial group is just the **free product** ℤ \* ℤ, which is the free group on two generators. So π₁(S¹ ∨ S¹) ≅ ℤ \* ℤ — loops on the first circle and loops on the second circle generate independent, non-commuting elements.

The **torus** T² = S¹ × S¹ gives a richer example. Represent the torus as a square with opposite edges identified (top = bottom with label a, left = right with label b). Remove a small open disk from the interior to get U, and let V be a small open disk around the center. U deformation-retracts to the boundary square (a loop aba⁻¹b⁻¹), V is simply connected, and U ∩ V is a circle (simply connected intersection gives a free product, but the loop of U ∩ V bounds a disk in V). Van Kampen then gives π₁(T²) = ⟨a, b | aba⁻¹b⁻¹ = e⟩ = ℤ × ℤ: the two generators commute, reflecting the fact that going around the torus one way then the other way is homotopic to going the other way first. The theorem reduces a global topological question to an algebraic calculation from local data.
