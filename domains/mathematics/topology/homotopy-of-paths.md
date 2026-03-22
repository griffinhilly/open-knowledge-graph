---
id: homotopy-of-paths
title: Homotopy of Paths
domain: mathematics
course: topology
prerequisites:
- id: path-connectedness
  type: hard
- id: continuity-topological-spaces
  type: hard
builds-toward:
- fundamental-group-definition
tags:
- homotopy
- homotopic-paths
- path-deformation
stage: advanced
status: draft
---

# Homotopy of Paths

## Core Idea
Two paths are homotopic if one can be continuously deformed into the other while keeping endpoints fixed. This is an equivalence relation on paths, and the set of equivalence classes can be given a group structure (under concatenation) when the basepoint is fixed. Homotopy captures the intuition that topologically equivalent deformations preserve path structure.

## Questions

```yaml
- question: "Consider two paths in the punctured plane ℝ² \\ {0}, both going from (-1, 0) to (1, 0): path α travels above the origin, and path β travels below. Are α and β homotopic rel endpoints?"
  type: multiple-choice
  options:
    - "Yes — both paths connect the same endpoints, so they can always be continuously deformed into each other"
    - "No — the hole at the origin is a topological obstruction preventing any continuous deformation from α to β while fixing endpoints"
    - "Yes — but only if we allow the endpoints to move slightly during the deformation"
    - "No — because the paths have different arc lengths, so no length-preserving deformation exists"
  answer: 1
  explanation: "In ℝ² (no hole), any two paths with the same endpoints are homotopic via the straight-line homotopy H(t, s) = (1−s)α(t) + sβ(t). But in ℝ² \\ {0}, any deformation from α to β must at some point pass through the origin — which is removed from the space. No continuous map H: [0,1]×[0,1] → ℝ² \\ {0} can achieve the deformation, so α and β belong to different homotopy classes. Length is irrelevant to homotopy; only the topology of the space matters."

- question: "Why is the requirement that endpoints remain fixed throughout a path homotopy essential, rather than merely a technical convenience?"
  type: multiple-choice
  options:
    - "It is purely technical — it simplifies the proof that homotopy is an equivalence relation"
    - "Without fixing endpoints, any two paths in a path-connected space could be deformed into each other, erasing all topological information about the space"
    - "It ensures the homotopy is differentiable rather than merely continuous"
    - "It prevents the deformation from reversing the orientation of the path"
  answer: 1
  explanation: "If endpoints were allowed to move freely (free homotopy), then in any path-connected space you could slide one endpoint to meet the other and shrink the path to a point, making every path homotopic to every other. All topological information would be lost. Fixing the endpoints forces the homotopy to measure how paths 'go around' obstacles — holes, handles, etc. — between two fixed points. The distinction between free homotopy and homotopy rel endpoints is precisely what makes the fundamental group a meaningful invariant."

- question: "In ℝ², any two paths with the same endpoints are homotopic rel endpoints."
  type: true-false
  answer: true
  explanation: "ℝ² is convex: for any two paths α and β from p to q, the straight-line homotopy H(t, s) = (1−s)α(t) + sβ(t) is a valid homotopy. It is continuous, satisfies H(t, 0) = α(t) and H(t, 1) = β(t), and fixes both endpoints H(0, s) = p and H(1, s) = q for all s. No obstructions exist because the space has no holes."

- question: "A loop based at a point p that winds once around a hole and a loop that winds twice around the same hole are homotopic rel endpoints in any space containing that hole."
  type: true-false
  answer: false
  explanation: "These loops belong to different elements of the fundamental group π₁(X, p). In the punctured plane ℝ² \\ {0}, the fundamental group is ℤ, where the integer counts the winding number. A loop winding once corresponds to 1 ∈ ℤ and a loop winding twice corresponds to 2 ∈ ℤ. Since 1 ≠ 2, no homotopy rel endpoints exists between them. You cannot continuously deform one into the other without passing through the removed point."

- question: "What determines whether two paths between the same endpoints belong to the same homotopy class, and what does this have to do with the shape of the space?"
  type: short-answer
  answer: "Two paths are in the same homotopy class if and only if one can be continuously deformed into the other with endpoints fixed. Whether this is possible depends on the topology of the space — specifically, whether the region between the paths contains any holes or other obstructions. In simply connected spaces (no holes), all paths between the same endpoints are homotopic. In spaces with holes, paths that wind differently around those holes belong to different homotopy classes. The set of homotopy classes of loops at a basepoint, under concatenation, forms the fundamental group — which encodes the space's hole structure."
  explanation: "The key insight is that homotopy classes count topological obstructions. Two paths in the same class can be deformed into each other by sliding through the space continuously; paths in different classes are separated by a hole or feature that no continuous deformation can cross. This is why the fundamental group is a topological invariant: homeomorphic spaces have isomorphic fundamental groups, because a homeomorphism carries homotopy classes to homotopy classes."
```

## Explainer

From path-connectedness, you know that a space X is path-connected when any two points can be joined by a continuous path — a continuous map γ: [0, 1] → X with γ(0) = p and γ(1) = q. But path-connectedness only tells you that paths exist; it says nothing about how many "essentially different" paths there are. Homotopy is the tool for measuring that difference. Two paths α, β from p to q are **homotopic** (rel endpoints) if there exists a continuous map H: [0, 1] × [0, 1] → X such that H(t, 0) = α(t), H(t, 1) = β(t), H(0, s) = p, and H(1, s) = q for all t and s. Think of the second coordinate s as a "deformation parameter": at s = 0 you have the path α; at s = 1 you have the path β; in between, H(−, s) is a continuously varying family of paths, all sharing the same endpoints.

The geometric picture is immediate: imagine drawing two paths between the same two points on a piece of paper. You can always continuously deform one into the other by sliding it across the paper — the plane has no obstacles. Now imagine the same two paths on a surface with a hole (like an annulus, or the punctured plane ℝ² \ {0}). A path that loops around the hole and a path that does not loop around the hole cannot be deformed into each other without passing through the hole. Homotopy detects this topological obstruction. The paths live in the same space but belong to different **homotopy classes** — equivalence classes under the "can be continuously deformed" relation.

That homotopy is an equivalence relation (reflexive, symmetric, transitive) is a standard verification using the continuity you know from your second prerequisite: identity homotopies, reversals, and compositions of homotopies are all continuous. The deeper payoff is that homotopy classes of loops (paths with γ(0) = γ(1) = basepoint) can be composed by concatenation — traverse α then traverse β — and this composition is well-defined on equivalence classes. The resulting structure is the **fundamental group** π₁(X, p), the key invariant built in the next topic. The word "group" is justified because the concatenation operation has an identity (the constant loop at p) and inverses (the reverse path), with associativity holding up to homotopy.

The constraint that endpoints stay fixed throughout the deformation is essential and not merely technical. Without fixing endpoints, two paths between different pairs of points could be "homotoped" into each other in a connected space, losing all information. Fixing endpoints ensures homotopy measures how paths differ in their traversal of the space between two fixed points. This is the distinction between a free homotopy (endpoints can wander) and a homotopy rel endpoints, and in the context of the fundamental group, it is always the latter that matters. Every path has a homotopy class; those classes compose; and the resulting group carries deep information about the shape of the space — whether it has holes, handles, or other features that no amount of continuous deformation can remove.
