---
id: closure-interior-boundary
title: Closure, Interior, and Boundary of Sets
domain: mathematics
course: topology
prerequisites:
- id: closed-sets-topology
  type: hard
- id: open-sets-topology
  type: hard
- id: boundary-set-topology
  type: soft
builds-toward:
- limit-points-and-accumulation
- continuous-functions-topology
tags:
- closure
- interior
- boundary
stage: formal-systems
status: validated
---
# Closure, Interior, and Boundary of Sets

## Core Idea
For a set A: the closure Ā is the smallest closed set containing A; the interior A° is the largest open set contained in A; the boundary ∂A = Ā \ A°. These are fundamental closure operators in topology.

## Questions

```yaml
- question: "Let A = [0, 1) in ℝ with the standard topology. What is the boundary ∂A?"
  type: multiple-choice
  options:
    - "{0} — only the left endpoint, since 1 is not in A"
    - "{0, 1} — both endpoints are in the closure but not the interior"
    - "∅ — A contains all its limit points"
    - "(0, 1) — all interior points form the boundary"
  answer: 1
  explanation: "The interior A° = (0,1): points strictly inside have open neighborhoods fitting within A. The closure Ā = [0,1]: both endpoints 0 and 1 are limit points (every open interval around them hits A). The boundary ∂A = Ā \\ A° = [0,1] \\ (0,1) = {0,1}. Both endpoints satisfy the boundary condition: every open neighborhood of 0 and every open neighborhood of 1 intersects both A and its complement. The fact that 1 is not in A is irrelevant to whether it's a boundary point — boundary is defined by the closure-minus-interior formula."

- question: "Suppose Ā = A for a set A in some topological space. What can you conclude about A?"
  type: multiple-choice
  options:
    - "A is open, because the closure operation produces open sets"
    - "A is closed, because A equals the smallest closed set containing itself"
    - "A has empty boundary, because no points need to be added to A to close it"
    - "A is both open and closed (clopen), because it satisfies a fixed-point condition"
  answer: 1
  explanation: "The closure Ā is defined as the smallest closed set containing A. If A = Ā, then A is equal to a closed set, so A is closed. This is the definition: a set is closed if and only if it contains all its limit points, which is equivalent to equaling its own closure. Option C is tempting but wrong — ∂A = Ā \\ A° = A \\ A° could still be non-empty if A is not open. Option D overclaims; Ā = A just says A is closed, not that it is also open."

- question: "A set A is open if and only if A equals its own closure."
  type: true-false
  answer: false
  explanation: "This confuses the characterization of open sets with that of closed sets. A set is closed if and only if it equals its own closure (Ā = A). A set is open if and only if it equals its own interior (A° = A). These are distinct properties: closure is about containing limit points, interior is about being 'surrounded' by the set. An open interval (0,1) satisfies A° = A but Ā = [0,1] ≠ A. A closed interval [0,1] satisfies Ā = A but A° = (0,1) ≠ A."

- question: "The boundary of any open set is always disjoint from the set itself."
  type: true-false
  answer: true
  explanation: "If A is open, then A = A° (an open set equals its own interior). The boundary is ∂A = Ā \\ A°. Since A° = A, we have ∂A = Ā \\ A. Because Ā \\ A and A are always disjoint by set subtraction, ∂A ∩ A = ∅. Intuitively: boundary points have every neighborhood intersecting both A and its complement, so they cannot be interior points — but all points of an open set are interior points. A boundary point of an open set must lie outside the set."

- question: "Explain why a set A is closed if and only if A equals its own closure, using the definition of closure as the smallest closed set containing A."
  type: short-answer
  answer: "By definition, Ā is the smallest closed set containing A, so A ⊆ Ā always. If A is closed, then A itself is a closed set containing A, and since Ā is the smallest such set, Ā ⊆ A. Combined with A ⊆ Ā, we get Ā = A. Conversely, if Ā = A, then A equals the closed set Ā, so A is closed. The equivalence follows directly from the minimality in the definition of closure."
  explanation: "The argument is a clean minimality argument: closure is defined as the smallest closed superset, so any closed superset of A is at least as large as Ā. If A is itself closed, it is the smallest closed set containing A, so it must equal Ā. The converse is immediate because Ā is always closed. This characterization is foundational — it makes 'closed set' and 'equals its own closure' synonymous, which is constantly used in continuity proofs."
```

## Explainer

From your work with open and closed sets, you know that a set can be open, closed, both, or neither — and that open and closed are not opposites in topology. The trio of **closure**, **interior**, and **boundary** gives you a precise vocabulary for describing how any set sits inside its ambient space, regardless of whether the set itself is open or closed.

Start with the **interior** A°. A point x is in A° if there exists an open set U with x ∈ U ⊆ A — in other words, x is "surrounded" by A, with a whole open neighborhood fitting inside A. The interior is the largest open set contained in A. Think of A = [0,1] in ℝ: the interior is (0,1), because every point strictly between 0 and 1 has a small open interval around it still inside [0,1], but 0 and 1 do not. The interior captures the "purely inside" part of A.

The **closure** Ā adds to A all points that are "limit points" — every open neighborhood of x intersects A. Equivalently, Ā is the smallest closed set containing A. For A = (0,1), the closure is [0,1]: the endpoints 0 and 1 are limit points because every open interval around them overlaps with (0,1). The closure captures A together with everything it is "trying to approach." A set is closed if and only if it equals its own closure.

The **boundary** ∂A = Ā \ A° consists of points that are in the closure but not the interior — points where every open neighborhood intersects both A and its complement. For A = (0,1), the boundary is {0, 1}. Boundary points are "on the edge": you cannot put an open ball around them that stays entirely inside A or entirely outside A. Notice that ∂A is always a closed set (as the difference of two closed sets), and that X is partitioned into three disjoint pieces: A°, ∂A (intersected with A and its complement), and the exterior (interior of the complement). These three operators together give a complete topological decomposition of how A relates to the ambient space, and they arise constantly in continuity proofs and limit point arguments that build on this foundation.
