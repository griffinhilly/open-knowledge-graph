---
id: closure-interior-and-boundary
title: Closure, Interior, and Boundary
domain: mathematics
course: topology
prerequisites:
- id: closed-sets-in-topological-spaces
  type: hard
builds-toward:
- limit-points-convergence-topology
- interior-closure-operators
tags:
- closure
- interior
- boundary
- derived-sets
stage: advanced
status: draft
---

# Closure, Interior, and Boundary

## Core Idea
For a set A in a topological space, the closure is the smallest closed set containing A, the interior is the largest open set contained in A, and the boundary consists of points in the closure but not the interior. These three operations decompose the space into three disjoint pieces relative to any subset and are fundamental to understanding local structure.

## Questions

```yaml
- question: "Let A = {(x, y) : x² + y² ≤ 1} (the closed unit disk) in ℝ². What is the interior of A?"
  type: multiple-choice
  options:
    - "The boundary circle {(x, y) : x² + y² = 1}"
    - "The open disk {(x, y) : x² + y² < 1}"
    - "A itself, because A is closed and therefore equals its own interior"
    - "The empty set, because only open sets have a non-empty interior"
  answer: 1
  explanation: "The interior of A is the largest open set contained in A. The closed disk includes its boundary circle, but boundary points fail the interior test: no open ball around a boundary point stays entirely inside the disk. Strip those boundary points away and you get the open disk {x² + y² < 1}, which is open and fits entirely inside A. The closed set A is not its own interior — closed sets contain their boundary, but interior points require a neighborhood that stays inside the set."

- question: "A point p has the property that every open neighborhood of p contains points in A and points not in A. What does this tell us about p?"
  type: multiple-choice
  options:
    - "p is in the interior of A, because it is reachable from within A"
    - "p is in the exterior of A, because it has access to points outside A"
    - "p is on the boundary of A, because every neighborhood straddles A and its complement"
    - "p is in the closure of A, but we cannot determine whether it is on the boundary without more information"
  answer: 2
  explanation: "The neighborhood characterization of the boundary is exactly this: a point p is a boundary point of A if and only if every open neighborhood of p intersects both A and the complement of A. Interior points have a neighborhood entirely inside A; exterior points have a neighborhood entirely outside A; boundary points are precisely those where no neighborhood can avoid touching both sides. This neighborhood definition is the one that generalizes cleanly to any topological space."

- question: "For any set A in a topological space, every point in the interior of A is also in the closure of A."
  type: true-false
  answer: true
  explanation: "The interior of A is a subset of A (it is the largest open set contained in A), and A is a subset of its own closure (since the closure adds limit points to A, never removes them). Therefore, interior(A) ⊆ A ⊆ closure(A). Interior points — those with an open neighborhood contained in A — certainly satisfy the closure condition: their neighborhoods intersect A (trivially, since the neighborhoods lie inside A)."

- question: "If p is in the closure of A, then p must be an element of A."
  type: true-false
  answer: false
  explanation: "The closure of A consists of A together with all its limit points — points every neighborhood of which intersects A. A limit point of A need not be in A itself. For example, take A = (0, 1) in ℝ. The point 0 is in the closure of A (every neighborhood of 0 intersects (0,1)), but 0 ∉ A. This is precisely why 'closure' adds something: it includes the limit points on the 'edge' of A that A itself may not contain."

- question: "Explain the duality between the interior and closure operations, and why it means you never need to define both independently."
  type: short-answer
  answer: "The interior of A equals the complement of the closure of the complement of A: int(A) = (cl(Aᶜ))ᶜ. Intuitively, a point is inside A if and only if it is not in the closure of the outside. This algebraic relationship means each operation determines the other: once you know how to compute closures (e.g., as intersections of closed sets), you can compute interiors via complement, and vice versa."
  explanation: "The duality reflects the symmetry between open and closed sets in topology: taking complements swaps open sets for closed sets. Because the interior is the largest open set inside A and the closure is the smallest closed set containing A, and because complements turn open sets into closed sets, the two operations are mirror images of each other. This is why most topology texts define closure axiomatically and derive interior from it."
```

## Explainer

Work first with the concrete example of an open disk in the plane: A = {(x, y) : x² + y² < 1}, the open unit disk. You already know what it means for a set to be closed (it contains all its limit points). The **interior** of A is the largest open set contained within A — here, it's A itself, because A is already open. The **closure** of A is the smallest closed set containing A — here, it's the closed disk {(x, y) : x² + y² ≤ 1}, which adds the boundary circle. The **boundary** of A is what's left: the circle {(x, y) : x² + y² = 1}. Every point of the plane belongs to exactly one of these three zones relative to A: the interior (strictly inside), the boundary (on the edge), or the exterior (strictly outside). Together they partition the whole space.

Each operation has a clean characterization in terms of neighborhoods. A point p is in the **interior** of A if some open neighborhood of p fits entirely inside A — you can step in any direction a little bit and stay in A. A point p is in the **closure** of A if every open neighborhood of p intersects A — no matter how small a neighborhood you take, it touches A. A **boundary point** satisfies both: every neighborhood intersects A and intersects the complement of A. Boundary points are precisely the points where A and its complement touch.

These definitions extend uniformly to any topological space, not just ℝ² with its familiar geometry. This is the power of the topological framework you've been building: the same concepts apply to function spaces, discrete topologies, or anything else equipped with a notion of open sets. Notice also that the interior and closure are "dual" operations: the interior of A is the complement of the closure of the complement of A. This algebraic relationship means you rarely need to define both separately — one determines the other.

A crucial subtlety: the closure of an open set is not always obtained by simply "closing it up." Consider A = (0, 1) ∪ (2, 3) in ℝ. Its closure is [0, 1] ∪ [2, 3] — two disjoint closed intervals, not one connected set. The boundary consists of {0, 1, 2, 3}. None of the topology's global structure is assumed; everything follows from which sets are declared open. Mastering these three operators gives you the vocabulary to describe local structure — how a set sits in its ambient space — and is prerequisite to discussing continuity, limit points, and compactness in the full generality of topology.
