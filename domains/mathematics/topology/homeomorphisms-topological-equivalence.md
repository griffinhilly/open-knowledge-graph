---
id: homeomorphisms-topological-equivalence
title: Homeomorphisms and Topological Equivalence
domain: mathematics
course: topology
prerequisites:
- id: continuity-topological-spaces
  type: hard
builds-toward:
- topological-invariants
- classification-compact-surfaces
tags:
- homeomorphisms
- topological-equivalence
- isomorphisms
stage: advanced
status: draft
---

# Homeomorphisms and Topological Equivalence

## Core Idea
A homeomorphism is a continuous bijection with continuous inverse; two spaces are topologically equivalent if a homeomorphism exists between them. Homeomorphisms preserve all topological properties—they capture the intuition that two spaces have the same shape if one can be continuously deformed into the other without tearing or gluing.

## Questions

```yaml
- question: "Let f: [0, 1) → S¹ be the map f(t) = (cos 2πt, sin 2πt). This map is a continuous bijection. Why is it NOT a homeomorphism?"
  type: multiple-choice
  options:
    - "It is a homeomorphism — any continuous bijection between topological spaces is a homeomorphism"
    - "The inverse f⁻¹ is not continuous: a small open arc near the point (1, 0) on S¹ maps back to a set that is not open in [0, 1), violating the requirement for a continuous inverse"
    - "f is not bijective because the circle has more points than the half-open interval"
    - "f is not continuous at t = 0 because the interval is half-open"
  answer: 1
  explanation: "A homeomorphism requires that BOTH f and f⁻¹ are continuous. Here f is a continuous bijection, but f⁻¹ fails at (1, 0): any small open arc on S¹ containing (1, 0) pulls back under f⁻¹ to a set that includes points near 0 AND near 1 in [0, 1) — which is not open in [0, 1). Option A is the central misconception: continuity of the bijection alone is insufficient. The continuous inverse condition is a real, non-trivial requirement."

- question: "You want to prove that the closed interval [0, 1] and the open interval (0, 1) are NOT homeomorphic. Which argument works?"
  type: multiple-choice
  options:
    - "They have different lengths, and homeomorphisms must preserve length"
    - "[0, 1] is compact (every open cover has a finite subcover) and (0, 1) is not; compactness is a topological invariant preserved by homeomorphisms, so no homeomorphism can exist"
    - "A homeomorphism would have to map the endpoints of [0, 1] to something in (0, 1), which is impossible because (0, 1) has no endpoints"
    - "They cannot be homeomorphic because one is a closed set and the other is open"
  answer: 1
  explanation: "To prove non-homeomorphism, you need a topological invariant — a property preserved by all homeomorphisms — that differs between the spaces. Compactness is such an invariant: [0, 1] is compact (it is closed and bounded in ℝ, so Heine-Borel applies), but (0, 1) is not compact (the open cover {(1/n, 1)}_{n≥2} has no finite subcover). Option C describes geometric intuition but is not rigorous; option D is wrong because open/closed are relative to the ambient space, not intrinsic topological properties."

- question: "The open interval (0, 1) and the real line ℝ are not homeomorphic because (0, 1) is bounded and ℝ is unbounded."
  type: true-false
  answer: false
  explanation: "Boundedness is NOT a topological invariant — it depends on a metric (distance function), not on the open-set structure alone. Two spaces can be homeomorphic even if one is bounded in its usual metric embedding and the other is not. The map f(x) = tan(π(x − 1/2)) is a homeomorphism from (0, 1) to ℝ. Topological properties are preserved; metric properties like boundedness, diameter, and distance are not."

- question: "To prove two topological spaces are homeomorphic, it suffices to find a bijection between them that preserves the number of connected components and compact subsets."
  type: true-false
  answer: false
  explanation: "To prove homeomorphism, you must construct an explicit continuous bijection with a continuous inverse — you cannot just match invariants. Matching invariants is a strategy for proving non-homeomorphism (finding an invariant that differs). Shared invariants only show the spaces are 'not obviously different.' Two spaces can share many invariants and still fail to be homeomorphic (e.g., the sphere S² and the torus T² have the same number of connected components but are not homeomorphic, as their fundamental groups differ)."

- question: "Explain why the condition that f⁻¹ must also be continuous is a non-trivial requirement in the definition of a homeomorphism, and give an intuitive description of what goes wrong when it fails."
  type: short-answer
  answer: "Continuity of f means that nearby points in X map to nearby points in Y. But this alone doesn't ensure the spaces are topologically identical — f might 'glue together' distinct points of X that should remain distinct in Y, while still being injective and continuous. The inverse f⁻¹ measures whether nearby points in Y came from nearby points in X. If f⁻¹ is not continuous, then some points that are close in Y correspond to points far apart in X — the space Y has been 'folded' or 'compressed' relative to X in a way that can't be undone continuously. The [0, 1) → S¹ example illustrates this: the circle 'wraps around' and connects the two ends of [0, 1), creating a topology at the join point that cannot be continuously unwrapped."
  explanation: "The two-sided continuity requirement is what makes homeomorphisms true equivalences — they identify spaces that are structurally identical from the topological perspective. One-sided continuous bijections can 'collapse' topological structure in one direction. Requiring both f and f⁻¹ to be continuous ensures that open sets are identified with open sets in both directions, making the spaces indistinguishable topologically."
```

## Explainer

In algebra, an isomorphism is a structure-preserving bijection — a map that respects all the operations and whose inverse does too. Topology has the same concept: a **homeomorphism** is the topological version of an isomorphism, a bijection that preserves the open-set structure in both directions. Formally, f: X → Y is a homeomorphism if f is bijective, f is continuous (preimages of open sets are open), and f⁻¹ is also continuous. That third condition is not automatic. A continuous bijection can fail to have a continuous inverse: map [0, 1) onto the circle S¹ by f(t) = (cos 2πt, sin 2πt). This is a continuous bijection, but f⁻¹ is not continuous at the point (1, 0) — a small open arc on the circle maps back to a set that is not open in [0, 1). The two spaces are not homeomorphic.

The power of homeomorphisms is that they make two spaces completely interchangeable for any topological purpose. The open interval (0, 1) and the entire real line ℝ are homeomorphic: the map f(x) = tan(π(x − 1/2)) is a homeomorphism from (0, 1) to ℝ. They "look different" — one is bounded, the other infinite — but boundedness is not a topological concept (it depends on a metric, not just open sets). Both spaces have the same connected components, the same number of holes, the same "local" structure at every point. Topologically they are identical.

To prove two spaces are homeomorphic you must construct an explicit homeomorphism. To prove they are **not** homeomorphic you must find a **topological invariant** — a property preserved by all homeomorphisms — that differs between them. The closed interval [0, 1] and the open interval (0, 1) are not homeomorphic: [0, 1] is compact (every open cover has a finite subcover) and (0, 1) is not. Since compactness is a topological invariant, no homeomorphism can exist. Similarly, a circle (S¹) and a figure-eight (S¹ ∨ S¹) are not homeomorphic: removing one point from S¹ leaves a connected space, but removing the central crossing point of the figure-eight leaves two disconnected arcs.

The topological invariants you will study next — compactness, connectedness, and the fundamental group — are the vocabulary for distinguishing spaces up to homeomorphism. Each invariant is a theorem of the form "if f: X → Y is a homeomorphism, then X and Y have the same [invariant]." The classification program of topology is exactly this: identify all topological spaces up to homeomorphism, and compile enough invariants to tell them apart. For compact surfaces (the sphere, torus, Klein bottle, etc.), this classification is complete — the genus and orientability determine the homeomorphism type.
