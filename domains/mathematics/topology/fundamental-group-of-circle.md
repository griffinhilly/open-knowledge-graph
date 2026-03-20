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
status: draft
---

# Fundamental Group of the Circle

## Core Idea
The fundamental group π₁(S¹) is isomorphic to ℤ, the integers under addition. The isomorphism assigns to each loop its winding number—the net number of times it wraps around the circle, with counterclockwise positive and clockwise negative. A loop that winds twice composes with one that winds three times to give a loop winding five times, mirroring addition in ℤ. The proof uses the covering space ℝ → S¹ given by the exponential map t ↦ e^{2πit}, lifting loops to paths in ℝ and reading off the winding number as the endpoint. This computation is the foundational example in algebraic topology, demonstrating how topological features (the "hole" in S¹) are captured by algebraic invariants.

## How It's Best Learned
Draw loops on S¹ with different winding numbers and verify that composition corresponds to addition. Then study the covering space ℝ → S¹ to see how lifting makes the winding number rigorous, turning a geometric intuition into an algebraic proof.

## Common Misconceptions
The winding number is not about the shape of the loop but only about its net winding. A complicated loop that winds forward and backward may have winding number zero. Students also sometimes confuse π₁(S¹) ≅ ℤ with π₁(S²) ≅ 0—the sphere is simply connected because loops can be contracted over the surface.

