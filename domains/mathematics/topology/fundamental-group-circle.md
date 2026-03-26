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
stage: advanced
status: validated
---

# The Fundamental Group of the Circle

## Core Idea
π₁(S¹) ≅ ℤ, where an integer n corresponds to the homotopy class of loops that wind around the circle n times. This is computed using the universal covering map ℝ → S¹.

## Questions

```yaml
- question: "A loop on S¹ winds counterclockwise twice, then clockwise once. What is its homotopy class in π₁(S¹) ≅ ℤ?"
  type: multiple-choice
  options:
    - "0, since it starts and ends at the same base point"
    - "1, since the net winding number is 2 − 1 = 1"
    - "3, since it made three total revolutions counting both directions"
    - "It is not a valid element of π₁(S¹) because it changes direction"
  answer: 1
  explanation: "The homotopy class is determined entirely by the winding number — how many net counterclockwise revolutions the loop completes. Going counterclockwise twice contributes +2 and clockwise once contributes −1, giving net winding number +1. The direction change is irrelevant; what matters is the total winding, which corresponds to the integer 1 in ℤ. Any two loops with the same winding number are homotopic, regardless of their specific paths."

- question: "What makes the universal covering map p: ℝ → S¹ the key tool for computing π₁(S¹)?"
  type: multiple-choice
  options:
    - "It shows that ℝ and S¹ are homeomorphic, so they have the same fundamental group"
    - "Every loop γ in S¹ based at 1 lifts uniquely to a path γ̃ in ℝ starting at 0, and the endpoint γ̃(1) is always an integer equal to the winding number"
    - "It provides a path connecting any two points on S¹ without passing through the base point"
    - "It shows that S¹ is simply connected, so all loops are contractible"
  answer: 1
  explanation: "The covering map p(t) = e^{2πit} wraps ℝ around S¹. Its key property is the unique path lifting: every loop in S¹ lifts uniquely to a path in ℝ. Since the loop starts and ends at 1 ∈ S¹, the lifted path starts at 0 and must end at some integer n (because p(n) = 1 requires n ∈ ℤ). This integer n is exactly the winding number, and the map [γ] ↦ γ̃(1) is the isomorphism π₁(S¹) ≅ ℤ. Note that ℝ and S¹ are not homeomorphic — ℝ is simply connected (π₁(ℝ) = 0), which is precisely why lifting to ℝ is useful."

- question: "Two loops on S¹ based at the same point are homotopic if and only if they have the same winding number."
  type: true-false
  answer: true
  explanation: "This is the content of π₁(S¹) ≅ ℤ. Homotopy classes of loops are in bijection with integers via the winding number. Loops with the same winding number can be continuously deformed into each other; loops with different winding numbers cannot. The winding number is a complete invariant for loop homotopy on S¹."

- question: "Since S¹ is a connected topological space, its fundamental group is expected to be trivial (i.e., nearly every loop is contractible to a point)."
  type: true-false
  answer: false
  explanation: "Connectivity and simple connectivity are different properties. A space is connected if it is in one piece; it is simply connected if every loop can be contracted to a point (i.e., π₁ = 0). The circle S¹ is connected but not simply connected: π₁(S¹) ≅ ℤ, meaning there are infinitely many distinct homotopy classes of loops. A loop that winds around the circle once cannot be continuously contracted to a point without leaving S¹. This is precisely what distinguishes S¹ from the disk D² (which is simply connected)."

- question: "Why must the endpoint γ̃(1) of a lifted loop γ̃: [0,1] → ℝ always be an integer, given that γ is a loop in S¹ based at 1?"
  type: short-answer
  answer: "Because γ is a loop, its endpoint equals its starting point: γ(1) = γ(0) = 1 ∈ S¹. The lifted path γ̃ satisfies p(γ̃(t)) = γ(t) for all t, so at t = 1: p(γ̃(1)) = γ(1) = 1. Since p(t) = e^{2πit}, the condition p(γ̃(1)) = 1 means e^{2πi·γ̃(1)} = 1, which holds precisely when γ̃(1) is an integer. Thus the loop condition in S¹ forces the lift to end at an integer, and that integer is the winding number."
  explanation: "The integer constraint comes entirely from the loop condition combined with the definition of p. This is why the universal covering space ℝ is so useful: paths in ℝ are determined uniquely by their starting point, and the algebraic structure of ℤ ⊂ ℝ captures exactly which endpoints correspond to loops downstairs. The uniqueness of lifting guarantees that homotopic loops lift to paths with the same endpoint, making the winding number a well-defined homotopy invariant."
```

## Explainer

You already know that the **fundamental group** π₁(X, x₀) consists of homotopy classes of loops based at x₀ — loops that can be continuously deformed into each other are considered the same element. The circle S¹ is the first nontrivial example: a loop on the circle can wind around it any integer number of times, and two loops are homotopic if and only if they wind the same number of times. This yields the isomorphism π₁(S¹) ≅ ℤ, where the integer is the **winding number**.

The winding number has an intuitive picture: stand at the center of the circle and watch a point trace a loop. Count how many full counterclockwise revolutions it completes (clockwise counts as negative). A loop that goes around once counterclockwise has winding number +1; one that doubles back once clockwise has winding number −1; a contractible loop (one that never truly goes around) has winding number 0. The group operation in π₁ corresponds to concatenating loops, which adds winding numbers — exactly the group operation in ℤ.

The proof uses the **universal covering map** p: ℝ → S¹ defined by p(t) = e^{2πit} (wrapping the real line around the circle). The key property is that every loop γ in S¹ starting at 1 **lifts uniquely** to a path γ̃ in ℝ starting at 0. The endpoint γ̃(1) is an integer because p(γ̃(1)) = γ(1) = 1, meaning γ̃(1) must be an integer. This endpoint is the winding number. Homotopic loops lift to paths with the same endpoint, so the map [γ] ↦ γ̃(1) is well-defined on homotopy classes; it is straightforward to check it is a group isomorphism.

This computation has consequences far beyond its apparent simplicity. Since π₁(S¹) ≅ ℤ ≠ 0, the circle is not simply connected — loops around it cannot all be contracted to a point. This distinguishes S¹ from the disk D² (which is simply connected). The result also underpins the Brouwer fixed-point theorem, the fundamental theorem of algebra, and the theory of covering spaces you will study next: every covering of S¹ corresponds to a subgroup of ℤ, which are exactly the subgroups nℤ for n ≥ 0.
