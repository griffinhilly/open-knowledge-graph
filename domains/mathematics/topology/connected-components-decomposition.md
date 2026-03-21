---
id: connected-components-decomposition
title: Connected Components
domain: mathematics
course: topology
prerequisites:
- id: connected-spaces-definition
  type: hard
tags:
- connected-components
- decomposition
stage: formal-systems
status: draft
---

# Connected Components

## Core Idea
The connected component of a point x is the maximal connected subset containing x. Connected components partition X into connected pieces. A space is connected iff it has one component. Component spaces are topological invariants; they classify spaces into their 'pieces.' Connected components of the identity in topological groups are normal subgroups.

## Questions

```yaml
- question: "Consider X = {1, 2, 3} with the discrete topology (every subset is open). How many connected components does X have?"
  type: multiple-choice
  options:
    - "1 — the whole space is the single connected piece"
    - "2 — the space can be split into two open sets"
    - "3 — each singleton {x} is its own component"
    - "It cannot be determined without knowing the metric"
  answer: 2
  explanation: "In the discrete topology, every singleton {x} is both open and closed. For any two points p, q ∈ X, the sets {p} and X \\ {p} form a separation — so no two-point subset is connected. Each singleton is therefore its own maximal connected subset, meaning each singleton is a connected component. The discrete topology is the extreme case of total disconnectedness. The tempting answer is 1 (the whole space), but X cannot be connected if it can be split into disjoint nonempty open sets — and {1} and {2, 3} are both open in the discrete topology."

- question: "Which statement best explains why the number of connected components is a topological invariant?"
  type: multiple-choice
  options:
    - "Any homeomorphism is a bijection, so it maps the same number of points to the same number of points"
    - "Connected components are preserved under any homeomorphism: since homeomorphisms map open sets to open sets and are bijective, connected subsets map to connected subsets, so components correspond bijectively"
    - "Two spaces with the same number of points must have the same number of components"
    - "Topological invariants are only preserved under homotopy equivalences, which are weaker than homeomorphisms"
  answer: 1
  explanation: "A homeomorphism is a continuous bijection with a continuous inverse. Because it maps open sets to open sets, it preserves connectedness: the image of a connected set under a homeomorphism is connected. The component of a point x maps to the component of its image f(x). Since the homeomorphism is a bijection, the components are in bijective correspondence — same number of components. This makes component count an invariant: spaces with different component counts cannot be homeomorphic. Option A is wrong because equal point count does not imply equal component count."

- question: "A topological space is connected if and only if it has exactly one connected component."
  type: true-false
  answer: true
  explanation: "By definition, the connected components partition the space into maximal connected pieces. If the space itself is connected, it cannot be written as a union of two disjoint nonempty open sets — it is its own maximal connected subset and therefore its own single component. Conversely, if there is more than one component, the space has at least two disjoint nonempty connected pieces, which contradicts connectedness. The equivalence is direct."

- question: "The connected component of a point x is the smallest connected subset of X containing x."
  type: true-false
  answer: false
  explanation: "This is the critical misconception to avoid. The connected component is the *largest* (maximal) connected subset containing x — it is the union of *all* connected subsets that contain x. The smallest connected subset containing x would just be {x} itself (a singleton is always connected in any topology). The maximality is what gives components their structure: you expand as far as possible while maintaining connectedness, and that maximum is the component."

- question: "Why is the 'maximal' qualifier in the definition of a connected component essential? What would go wrong without it?"
  type: short-answer
  answer: "Without maximality, every point would belong to many different connected subsets (including singletons, intervals, and the whole component), and there would be no unique 'piece' associated with a point. Maximality forces each point into exactly one piece: its component is the union of all connected sets containing it, and since that union is itself connected, it is the unique largest connected subset containing x. Without maximality, we could not define a partition — points would belong to overlapping connected sets with no canonical choice."
  explanation: "The definition works because the union of connected sets sharing a common point is connected. This means the union of all connected subsets through x is still connected, and it is maximal by construction — no larger connected set contains it without being it. Dropping 'maximal' would lose the partition property that makes connected components useful for classifying spaces into distinct pieces."
```

## Explainer

You already know what it means for a topological space to be connected: it cannot be written as a union of two disjoint nonempty open sets. Now the natural follow-up question is: what if the space *isn't* connected? How do we systematically decompose it into its connected "pieces"? That is exactly what connected components formalize.

The **connected component** of a point x is defined as the union of all connected subsets of X that contain x. This is always well-defined because the union of connected sets that share a common point is itself connected — so the union is still connected, and it is the largest such set. Every point belongs to exactly one component, so the components **partition** X: every point is in precisely one piece, and no two pieces overlap. If X is already connected, there is just one component — all of X. At the other extreme, if X carries the discrete topology (every subset is open), each singleton {x} is its own component, and the space has as many pieces as it has points.

A useful example: take ℝ and remove the rationals. The resulting space of irrationals is **totally disconnected** — every connected component is a single point. Between any two irrationals there is a rational, which has been removed, so no interval of irrationals can be connected (any two-point subset can be separated by choosing a rational between them). Compare this to ℝ itself, which is connected (one component), or to a figure-eight graph, which is connected, or to two disjoint circles, which has two components. Counting components is a rough but useful measure of a space's "connectivity."

Connected components are **topological invariants**: any homeomorphism between spaces must map components of one space bijectively onto components of the other. This makes the number of components a tool for distinguishing spaces — if two spaces have different numbers of components, no homeomorphism between them exists. In topological groups — structures that are simultaneously groups and topological spaces, with the group operations continuous — the connected component of the identity element is always a **normal subgroup**. This connects topological structure to algebraic structure and is a foundational fact in the theory of Lie groups, where the component of the identity is often the most important part of the group.
