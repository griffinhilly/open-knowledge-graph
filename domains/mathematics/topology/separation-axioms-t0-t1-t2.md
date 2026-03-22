---
id: separation-axioms-t0-t1-t2
title: 'Separation Axioms: T₀, T₁, and T₂ (Hausdorff)'
domain: mathematics
course: topology
prerequisites:
- id: limit-points-convergence-topology
  type: hard
builds-toward:
- hausdorff-spaces
- separation-axioms-t3-regular
tags:
- separation-axioms
- t0
- t1
- t2
- hausdorff
stage: advanced
status: draft
---

# Separation Axioms: T₀, T₁, and T₂ (Hausdorff)

## Core Idea
Separation axioms form a hierarchy measuring how well a topology distinguishes points. T₀ (Kolmogorov) requires that for any two distinct points, at least one has an open neighborhood not containing the other. T₁ (Fréchet) strengthens this so that each point has a neighborhood excluding the other, which is equivalent to requiring all singletons to be closed. T₂ (Hausdorff) requires disjoint open neighborhoods for any two distinct points, guaranteeing that limits of convergent sequences are unique. Each level excludes more pathological spaces: most spaces encountered in analysis and geometry are at least Hausdorff, making T₂ the practical baseline for well-behaved topology.

## How It's Best Learned
Examine concrete examples at each level: the indiscrete topology fails even T₀, the cofinite topology on an infinite set is T₁ but not T₂, and the Euclidean topology is T₂. Seeing exactly where each axiom fails in these examples makes the hierarchy concrete.

## Common Misconceptions
T₁ does not imply Hausdorff—the cofinite topology on an infinite set separates points from each other with open sets but cannot produce disjoint neighborhoods. Students also sometimes think Hausdorff is an exotic condition, when in fact most familiar spaces (metric spaces, manifolds) are automatically Hausdorff.

## Explainer

The **separation axioms** T₀, T₁, and T₂ form a hierarchy that measures how effectively a topology distinguishes between points. At the weakest level, **T₀ (Kolmogorov)** requires that for any two distinct points, at least one has an open neighborhood not containing the other — the topology can tell the points apart, but only asymmetrically. **T₁ (Frechet)** strengthens this: for any two distinct points x and y, there is an open set containing x but not y, and simultaneously an open set containing y but not x. This is equivalent to requiring that every singleton {x} is a closed set. **T₂ (Hausdorff)** is stronger still: any two distinct points have disjoint open neighborhoods — open sets that separate them completely, with no overlap.

The cofinite topology on an infinite set is the standard example illustrating the gap between T₁ and T₂. In this topology, the open sets are ∅ and all subsets whose complement is finite. For any two distinct points x ≠ y, the set X \ {y} is open (its complement {y} is finite) and contains x but not y, so T₁ is satisfied. However, any two nonempty open sets must intersect — their complements are both finite, so their union of complements is finite, meaning their intersection is cofinite (and hence nonempty in an infinite set). Since no two nonempty open sets are disjoint, T₂ fails. This demonstrates that T₁ achieves point separation "one direction at a time" but does not guarantee the simultaneous disjoint separation that T₂ demands.

The Hausdorff condition has a critical consequence: **uniqueness of limits**. In a T₂ space, if a sequence (or net) converges, its limit is unique. The proof is a clean application of the definition: if xₙ → x and xₙ → y with x ≠ y, take disjoint open sets U ∋ x and V ∋ y. Eventually all terms are in U (by convergence to x) and in V (by convergence to y), but U ∩ V = ∅ — contradiction. In spaces that fail T₂, such as the cofinite topology, a sequence of distinct points converges to every point simultaneously. This is why T₂ is the practical baseline for well-behaved topology: without it, limits lose their deterministic character.

Most spaces encountered in analysis and geometry are Hausdorff. All metric spaces are T₂ (given distinct points, open balls of radius less than half their distance are disjoint). All manifolds are T₂ by convention. The Hausdorff condition is also essential for many theorems: compact subsets of Hausdorff spaces are closed, limits of convergent sequences are unique, and the diagonal {(x, x) : x ∈ X} is closed in X × X if and only if X is Hausdorff. The separation axioms T₀ through T₂ represent increasing demands on how finely the topology resolves individual points, with T₂ being the threshold at which the topology becomes analytically tractable.

## Questions

```yaml
- question: "The cofinite topology on ℝ (open sets are those with finite complement, plus ∅) — which separation axioms does it satisfy?"
  type: multiple-choice
  options:
    - "T₀ only — only one point can be separated from the other"
    - "T₁ but not T₂ — every point has a neighborhood excluding any other, but no two disjoint open sets exist"
    - "T₂ (Hausdorff) — cofinite sets are large enough to separate any two points"
    - "None of T₀, T₁, or T₂ — the cofinite topology is too coarse"
  answer: 1
  explanation: "For any two points x ≠ y in ℝ, the set ℝ \\ {y} is open in the cofinite topology (its complement {y} is finite) and contains x but not y; similarly ℝ \\ {x} contains y but not x. This satisfies T₁. However, T₂ requires two disjoint open sets U ∋ x and V ∋ y. In the cofinite topology on ℝ, any two nonempty open sets have cofinite complements, so their union of complements is finite — meaning their intersection is cofinite (in particular nonempty). No two nonempty open sets are ever disjoint, so T₂ fails."

- question: "In a topological space, requiring that every singleton {x} is a closed set is equivalent to which separation axiom?"
  type: multiple-choice
  options:
    - "T₀ — distinct points can be topologically distinguished"
    - "T₁ — for any two distinct points, each has an open neighborhood not containing the other"
    - "T₂ — any two distinct points have disjoint open neighborhoods"
    - "Neither — closedness of singletons is unrelated to separation axioms"
  answer: 1
  explanation: "{x} is closed iff its complement is open. In T₁, for every y ≠ x there exists an open set Uᵧ containing y but not x. The union of all such Uᵧ over y ≠ x equals ℝ \\ {x} and is open (unions of open sets are open), so {x} is closed. Conversely, if every singleton is closed, then ℝ \\ {x} is open and serves as the T₁ neighborhood of every y ≠ x. The equivalence fails for T₀ (which only requires asymmetric separation) and T₂ (which requires the stronger disjoint-neighborhood condition)."

- question: "Every T₁ space is Hausdorff (T₂)."
  type: true-false
  answer: false
  explanation: "This is the central subtlety of the separation hierarchy: T₁ does not imply T₂. The cofinite topology on any infinite set provides a canonical counterexample. It satisfies T₁ (each point has an open neighborhood excluding every other point) but fails T₂ because no two nonempty open sets are disjoint — the 'separating neighborhoods' for two points always overlap. T₁ requires separating each point from the other one at a time; T₂ requires achieving separation simultaneously with disjoint sets, a strictly stronger demand."

- question: "In any Hausdorff (T₂) space, a sequence can converge to at most one limit."
  type: true-false
  answer: true
  explanation: "Uniqueness of limits is exactly what T₂ guarantees and what weaker axioms cannot. Suppose xₙ → x and xₙ → y with x ≠ y. By Hausdorff, there exist disjoint open sets U ∋ x and V ∋ y. Since xₙ → x, eventually all xₙ ∈ U; since xₙ → y, eventually all xₙ ∈ V. But U ∩ V = ∅, a contradiction. In non-Hausdorff spaces (like the cofinite topology on ℝ), every sequence can converge to every point simultaneously."

- question: "Why does satisfying T₁ (each point has an open neighborhood excluding every other point) fail to guarantee that any two points can be simultaneously separated by disjoint open sets?"
  type: short-answer
  answer: "T₁ only requires that for each ordered pair (x, y), there exists an open set containing x but not y. These separating sets for (x, y) and (y, x) are found independently and need not be disjoint. The cofinite topology on an infinite set illustrates this: for any x ≠ y, the set ℝ \\ {y} separates x from y, and ℝ \\ {x} separates y from x — T₁ holds. But any two nonempty open sets in this topology must intersect (their complements are finite, so they share cofinitely many points). Producing disjoint open neighborhoods requires a global constraint — that the two sets can be chosen simultaneously so neither contains any point of the other — which T₁ does not impose."
```

