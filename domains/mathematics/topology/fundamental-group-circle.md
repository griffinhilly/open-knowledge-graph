---
id: fundamental-group-circle
title: The Fundamental Group of the Circle
domain: mathematics
course: topology
prerequisites:
- id: fundamental-group-definition
  type: hard
builds-toward:
- covering-spaces
- van-kampen-theorem
tags:
- fundamental-group
- circle
stage: abstract-reasoning
status: draft
---

# The Fundamental Group of the Circle

## Core Idea
π₁(S¹) ≅ ℤ, where an integer n corresponds to the homotopy class of loops that wind around the circle n times. This is computed using the universal covering map ℝ → S¹.

## Explainer

You already know that the **fundamental group** π₁(X, x₀) consists of homotopy classes of loops based at x₀ — loops that can be continuously deformed into each other are considered the same element. The circle S¹ is the first nontrivial example: a loop on the circle can wind around it any integer number of times, and two loops are homotopic if and only if they wind the same number of times. This yields the isomorphism π₁(S¹) ≅ ℤ, where the integer is the **winding number**.

The winding number has an intuitive picture: stand at the center of the circle and watch a point trace a loop. Count how many full counterclockwise revolutions it completes (clockwise counts as negative). A loop that goes around once counterclockwise has winding number +1; one that doubles back once clockwise has winding number −1; a contractible loop (one that never truly goes around) has winding number 0. The group operation in π₁ corresponds to concatenating loops, which adds winding numbers — exactly the group operation in ℤ.

The proof uses the **universal covering map** p: ℝ → S¹ defined by p(t) = e^{2πit} (wrapping the real line around the circle). The key property is that every loop γ in S¹ starting at 1 **lifts uniquely** to a path γ̃ in ℝ starting at 0. The endpoint γ̃(1) is an integer because p(γ̃(1)) = γ(1) = 1, meaning γ̃(1) must be an integer. This endpoint is the winding number. Homotopic loops lift to paths with the same endpoint, so the map [γ] ↦ γ̃(1) is well-defined on homotopy classes; it is straightforward to check it is a group isomorphism.

This computation has consequences far beyond its apparent simplicity. Since π₁(S¹) ≅ ℤ ≠ 0, the circle is not simply connected — loops around it cannot all be contracted to a point. This distinguishes S¹ from the disk D² (which is simply connected). The result also underpins the Brouwer fixed-point theorem, the fundamental theorem of algebra, and the theory of covering spaces you will study next: every covering of S¹ corresponds to a subgroup of ℤ, which are exactly the subgroups nℤ for n ≥ 0.
