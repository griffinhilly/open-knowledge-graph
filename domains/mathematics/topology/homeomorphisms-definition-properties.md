---
id: homeomorphisms-definition-properties
title: Homeomorphisms and Topological Equivalence
domain: mathematics
course: topology
prerequisites:
- id: continuity-topological-definition
  type: hard
builds-toward:
- quotient-maps-definition
tags:
- homeomorphism
- equivalence
stage: formal-systems
status: validated
---

# Homeomorphisms and Topological Equivalence

## Core Idea
A homeomorphism is a continuous bijection with continuous inverse. Two spaces are homeomorphic if such a map exists; they are topologically identical. Homeomorphisms preserve all topological properties: compactness, connectedness, dimension, fundamental groups. Classification of topological spaces is the problem of describing spaces up to homeomorphism.

## Questions

```yaml
- question: "The map f: [0,1) → S¹ defined by f(t) = (cos 2πt, sin 2πt) is a continuous bijection. Is it a homeomorphism?"
  type: multiple-choice
  options:
    - "Yes — any continuous bijection between topological spaces is a homeomorphism"
    - "No — the map is not continuous at t = 0"
    - "No — the inverse f⁻¹ is not continuous: a small open arc near the seam of S¹ pulls back to a disconnected set near both 0 and 1 in [0,1), so open sets in S¹ do not correspond to open sets in [0,1)"
    - "No — bijectivity requires both spaces to have the same cardinality, which fails here"
  answer: 2
  explanation: "f is continuous and bijective, but f⁻¹ fails to be continuous at the identification point. A small open arc near the 'seam' of S¹ pulls back to a set near t = 0 and t approaching 1 in [0,1) — a disconnected preimage. A homeomorphism requires both f and f⁻¹ to be continuous, so f is not a homeomorphism. The key lesson: continuous bijection ≠ homeomorphism."

- question: "To show that [0,1] and S¹ are not homeomorphic, a topologist removes a point from each space and compares the results. What does this argument show?"
  type: multiple-choice
  options:
    - "Removing an interior point from [0,1] disconnects it, while removing any point from S¹ leaves it connected — so they cannot be homeomorphic"
    - "Removing a point from S¹ always creates a disconnected arc"
    - "Removing a point from [0,1] always leaves a connected space since intervals are path-connected"
    - "The argument only works if you remove corresponding points from both spaces"
  answer: 0
  explanation: "Removing an interior point from [0,1] splits it into two disjoint open intervals — the space becomes disconnected. But removing any single point from S¹ leaves a connected arc. Since homeomorphisms preserve connectedness, and the 'remove a point' operation yields different connectivity results, the two spaces cannot be homeomorphic. This is the template: find a topological invariant they disagree on."

- question: "A continuous bijection f: X → Y is always a homeomorphism."
  type: true-false
  answer: false
  explanation: "A homeomorphism requires both f and f⁻¹ to be continuous. A continuous bijection can fail to be a homeomorphism when the inverse is discontinuous. The standard example: f: [0,1) → S¹ wrapping the interval onto the circle is continuous and bijective, but the inverse is not continuous at the identification point. Continuity of f and bijectivity together do not force f⁻¹ to be continuous."

- question: "If f: X → Y is a homeomorphism, then X is compact if and only if Y is compact."
  type: true-false
  answer: true
  explanation: "Compactness is a topological property — preserved by homeomorphisms in both directions. The continuous image of a compact space under f is compact (so Y is compact if X is), and the continuous image under f⁻¹ is compact (so X is compact if Y is). Any property defined purely in terms of the topology is preserved by homeomorphisms."

- question: "Why must the inverse of a homeomorphism also be continuous — what goes wrong if we only require f to be continuous and bijective?"
  type: short-answer
  answer: "A homeomorphism is supposed to establish that X and Y have identical topological structure — the same open sets, just relabeled. Continuity of f means open sets in Y pull back to open sets in X. Without continuity of f⁻¹, open sets in X need not push forward to open sets in Y, so the topology of X and Y could be entirely different despite f being continuous. A bijection with only one-way continuity can collapse topological structure rather than preserve it."
  explanation: "This is why homeomorphism is defined as a continuous bijection with continuous inverse: equivalence requires the relationship to be symmetric, which is what continuity of f⁻¹ provides."
```

## Explainer

From the topological definition of continuity, you know that a continuous function f: X → Y "respects" the topology: preimages of open sets in Y are open in X. But continuity alone, even with bijectivity, does not make f a topological equivalence. A **homeomorphism** adds the requirement that the inverse f⁻¹ is also continuous — so the topology flows both ways, and open sets in X correspond exactly to open sets in Y. A homeomorphism is the topology's notion of "being the same."

A classic example reveals why the inverse's continuity matters. Consider the map f: [0,1) → S¹ defined by f(t) = (cos 2πt, sin 2πt) — wrapping the half-open interval onto the unit circle. This is a continuous bijection, but f⁻¹ is not continuous (small open sets near the "seam" of the circle pull back to disconnected sets near 0 and 1). So f is not a homeomorphism: [0,1) and S¹ are topologically distinct. The circle is compact; the half-open interval is not — and compactness is a topological property that homeomorphisms must preserve.

**Topological properties** are precisely those that homeomorphisms preserve: compactness, connectedness, path-connectedness, the number of connected components, the fundamental group, and dimension. If X and Y are homeomorphic, they must agree on all of these. This turns homeomorphism classification into a game: to show two spaces are homeomorphic, exhibit a homeomorphism; to show they are not, find a topological property they disagree on. The circle S¹ and the interval [0,1] both have one connected component, but removing a point from S¹ leaves the space connected while removing an interior point from [0,1] disconnects it — so they are not homeomorphic.

The popular analogy — a topologist cannot tell a coffee mug from a donut — captures this precisely. Both have exactly one "hole" (they are homeomorphic to each other and to S¹ × D²), and any property topology can detect, they share. The program of **classifying spaces up to homeomorphism** is one of topology's central ambitions: the classification of compact surfaces (sphere, torus, Klein bottle, …) and the ongoing program of understanding three-manifolds are examples at different levels of complexity. Every theorem you will prove about continuous functions on topological spaces — quotient maps, the Tietze extension theorem — depends on understanding when two spaces are genuinely different versus merely described differently.
