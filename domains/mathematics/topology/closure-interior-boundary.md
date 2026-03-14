---
id: closure-interior-boundary
title: Closure, Interior, and Boundary
domain: mathematics
course: topology
prerequisites:
- id: closed-sets-topology
  type: hard
- id: open-sets-topology
  type: hard
builds-toward:
- limit-points-and-accumulation
tags:
- operators
- set-operations
stage: advanced
status: draft
---

# Closure, Interior, and Boundary

## Core Idea
For a set A: the closure Ā is the smallest closed set containing A; the interior A° is the largest open set in A; the boundary ∂A = Ā \ A°. These three operators decompose the space into three regions: points strictly in A, points strictly outside, and boundary points separating them.

## How It's Best Learned
In ℝ²: visualize [0,1) with closure [0,1], interior (0,1), boundary {0,1}. Practice computing all three for various sets, then verify properties like Ā = A ∪ ∂A and A ∪ Aᶜ = X.

## Common Misconceptions
- Confusing closure with boundary (boundary is just the edge).
- Assuming interior is nonempty (discrete topology: interior of any singleton is empty).
