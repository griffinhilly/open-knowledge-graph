---
id: fundamental-group-of-circle
title: Fundamental Group of the Circle
domain: mathematics
course: topology
prerequisites:
- id: fundamental-group-definition
  type: hard
builds-toward:
- van-kampen-theorem
- covering-spaces
tags:
- circle
- fundamental-group
- winding-number
stage: advanced
status: validated
---

# Fundamental Group of the Circle

## Core Idea
The fundamental group π₁(S¹) is isomorphic to ℤ, the integers under addition. The isomorphism assigns to each loop its winding number—the net number of times it wraps around the circle, with counterclockwise positive and clockwise negative. A loop that winds twice composes with one that winds three times to give a loop winding five times, mirroring addition in ℤ. The proof uses the covering space ℝ → S¹ given by the exponential map t ↦ e^{2πit}, lifting loops to paths in ℝ and reading off the winding number as the endpoint. This computation is the foundational example in algebraic topology, demonstrating how topological features (the "hole" in S¹) are captured by algebraic invariants.

## How It's Best Learned
Draw loops on S¹ with different winding numbers and verify that composition corresponds to addition. Then study the covering space ℝ → S¹ to see how lifting makes the winding number rigorous, turning a geometric intuition into an algebraic proof.

## Common Misconceptions
The winding number is not about the shape of the loop but only about its net winding. A complicated loop that winds forward and backward may have winding number zero. Students also sometimes confuse π₁(S¹) ≅ ℤ with π₁(S²) ≅ 0—the sphere is simply connected because loops can be contracted over the surface.

## Explainer

The fundamental group of the circle, π₁(S¹), is isomorphic to the integers ℤ under addition. This is the first nontrivial computation in algebraic topology and serves as the prototype for all subsequent fundamental group calculations. The isomorphism assigns to each homotopy class of loops its **winding number** — the net number of times the loop wraps around the circle, counted positive for counterclockwise and negative for clockwise. A loop that winds twice counterclockwise represents the integer 2; a loop that winds once clockwise represents −1. Concatenation of loops corresponds to addition of winding numbers: a loop of class 2 followed by a loop of class 3 gives a loop of class 5.

The winding number depends only on the net wrapping, not on the geometric complexity of the loop. A loop that winds 50 times counterclockwise and then 50 times clockwise has winding number 0 — it is homotopic to the constant loop, regardless of how elaborate its trajectory appears. This is a fundamental principle in algebraic topology: the homotopy class captures what cannot be continuously undone, not the visual complexity of the path. Two loops are homotopic if and only if they have the same winding number, so the homotopy classes are in exact bijection with the integers.

The rigorous proof that π₁(S¹) ≅ ℤ uses the **covering space** ℝ → S¹ given by the exponential map p(t) = e^{2πit}. This map wraps the real line around the circle: every integer maps to the basepoint 1 ∈ S¹, and the intervals [n, n+1] each map onto exactly one full traversal of the circle. Given a loop γ in S¹ based at 1, the unique path lifting property of covering spaces produces a path γ̃ in ℝ starting at 0. Since γ is a loop (it returns to 1), the lifted path γ̃ must end at some integer n. This integer is the winding number. Crucially, homotopic loops in S¹ lift to paths with the same endpoint in ℝ — the lifting is homotopy-invariant — so the map [γ] ↦ n is a well-defined group homomorphism, and one can verify it is a bijection.

This computation has far-reaching consequences. It proves that the circle is not simply connected (π₁(S¹) is nontrivial), which distinguishes S¹ from contractible spaces like the disk. It provides the topological foundation for the argument that every polynomial has a root (a winding-number argument). It also explains why π₁(S²) is trivial: on the 2-sphere, any loop can slide over the surface and shrink to a point — there is no hole for a loop to wrap around. The contrast between π₁(S¹) ≅ ℤ and π₁(S²) = 0 illustrates how the fundamental group detects one-dimensional holes: the circle has one, the sphere does not.

## Questions

```yaml
- question: "A loop on S¹ winds 3 times counterclockwise, then 1 time clockwise. What is its winding number, and what does this tell you about its homotopy class?"
  type: multiple-choice
  options:
    - "Winding number 4; it is in the same homotopy class as a loop that winds 4 times counterclockwise"
    - "Winding number 2; it is homotopic to a loop that winds exactly twice counterclockwise"
    - "Winding number 3; the clockwise winding doesn't subtract because winding numbers are always positive"
    - "Winding number 0; forward and backward windings always cancel completely"
  answer: 1
  explanation: "The winding number is the *net* count: 3 counterclockwise minus 1 clockwise equals 2. Under the isomorphism π₁(S¹) ≅ ℤ, loops with the same net winding number are homotopic — they can be continuously deformed into each other. This loop is in homotopy class [2], the same class as a simple loop winding twice counterclockwise. The shape and path of the loop are irrelevant; only the net winding number determines the homotopy class."

- question: "Why is π₁(S²) = 0 (the trivial group) while π₁(S¹) ≅ ℤ?"
  type: multiple-choice
  options:
    - "S² is a 2-dimensional space and the fundamental group of an n-dimensional space is always trivial for n ≥ 2"
    - "S² has no interior 'hole'; any loop drawn on the sphere's surface can slide over the top and shrink continuously to a point"
    - "The fundamental group of S² equals ℤ² since it has two dimensions, but this simplifies to 0 by convention"
    - "Loops on S² cannot be composed because the sphere is not a group under multiplication"
  answer: 1
  explanation: "S¹ has a hole — a loop that winds around the circle cannot be contracted to a point without leaving the space. S² has no such obstruction: any loop on the surface of a 2-sphere can be pulled toward one pole and shrunk to a point without tearing. This is what 'simply connected' means. Option A is wrong; ℝ² is 2-dimensional with trivial fundamental group, but the torus T² = S¹ × S¹ is 2-dimensional with π₁ = ℤ × ℤ. Dimension alone does not determine the fundamental group."

- question: "A loop on S¹ that is geometrically complicated — winding forward and backward many times — must have a nonzero winding number because its complexity prevents it from being contractible."
  type: true-false
  answer: false
  explanation: "The winding number tracks *net* wrapping, not geometric complexity. A loop can wind 100 times clockwise and 100 times counterclockwise, producing an intricate path, yet have winding number 0 — placing it in the trivial homotopy class, homotopic to a constant loop. Only the net count determines the homotopy class. This is the key conceptual point: topology cares about what cannot be continuously undone, not about visual complexity."

- question: "The composition of a loop with winding number 2 and a loop with winding number −3 represents an element of π₁(S¹) with winding number −1, consistent with the group operation corresponding to integer addition."
  type: true-false
  answer: true
  explanation: "Under the isomorphism π₁(S¹) ≅ ℤ, loop composition corresponds precisely to integer addition. A loop of winding number 2 followed by a loop of winding number −3 gives net winding 2 + (−3) = −1. This is the content of the isomorphism: the algebraic structure of the fundamental group (loop composition) mirrors the arithmetic of the integers (addition), with winding number serving as the isomorphism."

- question: "How does the covering space ℝ → S¹ (given by t ↦ e^{2πit}) make the winding number rigorous, and why does the integer endpoint of a lifted path capture the homotopy class of the loop?"
  type: short-answer
  answer: "Given a loop γ in S¹ based at 1, the covering map lets us lift γ to a path γ̃ in ℝ starting at 0. Since the map t ↦ e^{2πit} identifies all integers with the basepoint 1, the lifted path must end at some integer n — the winding number of γ. Two loops are homotopic in S¹ if and only if their lifts end at the same integer, so the endpoint gives a well-defined homotopy invariant. Composition of loops corresponds to concatenation of lifts, and concatenated lifts add their endpoints — which is why composition in π₁(S¹) corresponds to addition in ℤ."
  explanation: "The covering space proof is what elevates the winding number from geometric intuition to a rigorous algebraic invariant. The key facts are: (1) lifts are unique given a starting point, (2) homotopic loops lift to paths with the same endpoint, and (3) the endpoint is always an integer. Together these establish the isomorphism π₁(S¹) ≅ ℤ rather than just an analogy."
```
