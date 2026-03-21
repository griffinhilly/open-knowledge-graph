---
id: convergence-in-topology
title: Convergence in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: limit-points-and-accumulation
  type: hard
builds-toward:
- sequential-compactness
- continuous-functions-topology
tags:
- convergence
- sequences
stage: advanced
status: draft
---

# Convergence in Topological Spaces

## Core Idea
A sequence (xₙ) converges to x if every neighborhood of x contains all but finitely many terms. Unlike metric spaces, limits need not be unique in general topological spaces, and sequences alone cannot always describe the topology—nets or filters are sometimes necessary.

## Questions

```yaml
- question: "A set X = {a, b, c} is given the indiscrete topology (only ∅ and X are open). The constant sequence a, a, a, ... converges to:"
  type: multiple-choice
  options:
    - "Only the point a, since the sequence is eventually constant at a"
    - "The points a and b but not c, since c was never a term of the sequence"
    - "No point, since the indiscrete topology lacks enough open sets to define convergence"
    - "Every point in X — all of a, b, and c simultaneously"
  answer: 3
  explanation: "A sequence converges to x if every open neighborhood of x contains all but finitely many terms. In the indiscrete topology, the only open set containing any point is all of X. Since X trivially contains every term of any sequence, every point qualifies as a limit. This is not a defect of the definition — it is a consequence of the topology being too coarse to separate points. Limit non-uniqueness is not a failure of convergence; it is a property of the topology itself."

- question: "In a topological space that is NOT first-countable, why are sequences sometimes insufficient to describe the topology?"
  type: multiple-choice
  options:
    - "Sequences can only converge in metric spaces where distances are defined"
    - "A point x may be a limit point of a set A — every open neighborhood of x meets A — yet no sequence from A converges to x, because sequences indexed by ℕ cannot probe all open neighborhoods when no countable neighborhood basis exists"
    - "In non-first-countable spaces, sequences have no well-defined ordering and cannot converge"
    - "Sequences only fail in finite topological spaces, not in infinite ones"
  answer: 1
  explanation: "Sequences are indexed by ℕ, so they can only 'probe' a limit point using countably many terms. If a point x has uncountably many incomparable open neighborhoods, a sequence may not eventually enter all of them — some neighborhoods are missed entirely. In a first-countable space, a countable neighborhood basis exists, so a sequence can detect all limit points by working through the basis. When first-countability fails, you need nets (indexed by general directed sets) to capture all topological information. This is one of the deepest differences between metric and general topological spaces."

- question: "In a Hausdorff (T₂) topological space, every convergent sequence has a unique limit."
  type: true-false
  answer: true
  explanation: "In a Hausdorff space, any two distinct points x and y have disjoint open neighborhoods U and V. If a sequence converged to both x and y, then U would need to contain all but finitely many terms AND V would also need to contain all but finitely many terms. But U and V are disjoint — no term can be in both — so this is impossible. The Hausdorff property is precisely what gives the topology enough 'separation' to force limits to be unique. Without it (as in the indiscrete topology), distinct points share all the same neighborhoods and can both be limits of any sequence."

- question: "In a general topological space, a point x is in the closure of a set A if and only if some sequence of points from A converges to x."
  type: true-false
  answer: false
  explanation: "This characterization holds in metric spaces and more generally in first-countable spaces, but fails in general topology. A point x can be a limit point of A — every open neighborhood of x meets A — without any sequence from A converging to x. This happens precisely in spaces that are not first-countable, where the natural numbers are not rich enough to index the neighborhoods around x. The correct generalization requires nets: x is in the closure of A if and only if some net from A converges to x. This is a core reason why nets, not sequences, are the fundamental notion of convergence in general topology."

- question: "What property of a topological space guarantees that limits of sequences are unique, and why does that property force uniqueness?"
  type: short-answer
  answer: "The Hausdorff (T₂) property guarantees unique limits. A space is Hausdorff if any two distinct points can be separated by disjoint open neighborhoods. If a sequence converged to two distinct points x and y, their separating neighborhoods U and V would each need to contain all but finitely many terms — but disjoint sets cannot both do this simultaneously, giving a contradiction."
  explanation: "The proof is short but structurally revealing: assume xₙ → x and xₙ → y with x ≠ y. By Hausdorff, find disjoint open U ∋ x and V ∋ y. By convergence to x, all but finitely many terms lie in U; by convergence to y, all but finitely many terms lie in V. But U ∩ V = ∅, so no term can be in both — a contradiction. Uniqueness of limits is thus a consequence of separation, not of convergence itself. This is why studying separation axioms (T₁, T₂, T₃, ...) matters: they control which convergence-like properties the topology supports."
```

## Explainer

In a metric space, you said xₙ → x when the distances d(xₙ, x) → 0 — a numerical condition that uniquely pins down the limit. In a general topological space, there are no distances, only open sets. The topological definition replaces "distance less than ε" with "inside some open neighborhood": the sequence **(xₙ) converges to x** if for every open set U containing x, all but finitely many terms of the sequence lie in U. This is a direct translation: instead of "eventually within distance ε," you say "eventually inside every open neighborhood." When the topology comes from a metric, the two definitions agree exactly, since open balls form a neighborhood basis.

The loss of a metric introduces a phenomenon that never occurs in metric spaces: **non-uniqueness of limits**. In the **indiscrete topology** (only ∅ and the whole space X are open), every sequence converges to every point — because the only open set containing any point is all of X, which automatically contains all sequence terms. This seems pathological, but it is not a defect of the definition; it is a consequence of the topology being too coarse to separate points. In a **Hausdorff space** (also called T₂), any two distinct points have disjoint open neighborhoods, which forces limits to be unique: if xₙ → x and xₙ → y with x ≠ y, you can separate them by disjoint opens, which cannot both contain all but finitely many terms simultaneously. Uniqueness of limits is thus a property of the topology, not of convergence itself.

A deeper surprise is that **sequences are sometimes insufficient** to describe the topology. In a metric space, every topological property — continuity, closure, compactness — can be characterized in terms of sequences. In a general topological space, this fails. A point x may be a limit point of a set A (every open set around x meets A) without any sequence of points in A converging to x. This phenomenon occurs in spaces that are not first-countable (no countable neighborhood basis exists at x). The fix is to generalize sequences to **nets** (directed systems) or **filters**, which are indexed by more general ordered sets instead of the natural numbers. In a general topological space, x is in the closure of A if and only if some net from A converges to x — the sequence version requires first countability.

Understanding this progression — metric convergence → topological neighborhood convergence → nets and filters — reflects a broader theme in topology: the goal is to find the minimal structure needed for each concept. Sequences capture convergence perfectly in metric spaces because the countable naturals are rich enough to probe all open sets around a limit point. When open sets are structured differently, you need a more powerful indexing apparatus. This is why convergence in topology is not just a definition to memorize but a window into the difference between what "nearness" means in different mathematical contexts.


