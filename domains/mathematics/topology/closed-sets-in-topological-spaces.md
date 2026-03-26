---
id: closed-sets-in-topological-spaces
title: Closed Sets in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: open-sets-in-topological-spaces
  type: hard
builds-toward:
- closure-interior-and-boundary
- limit-points-convergence-topology
tags:
- closed-sets
- topology
- complements
stage: advanced
status: validated
---

# Closed Sets in Topological Spaces

## Core Idea
A set is closed if its complement is open; this definition generalizes the intuition from the real line where closed sets include their boundary points. Closed sets are dual to open sets and satisfy: the whole space and empty set are closed, arbitrary intersections of closed sets are closed, and finite unions are closed.

## Explainer

In a topological space (X, τ), a set C is **closed** if its complement X \ C is an open set — that is, X \ C ∈ τ. This definition derives entirely from the open-set structure: the topology τ specifies which sets are open, and closed sets are defined as complements of those. From your study of open sets in topological spaces, you know that τ satisfies three axioms (∅ and X belong to τ, arbitrary unions of τ-members belong to τ, finite intersections of τ-members belong to τ). Closed sets inherit a dual set of axioms via De Morgan's laws.

The closed-set axioms are: (1) ∅ and X are closed (since their complements X and ∅ are open). (2) Arbitrary intersections of closed sets are closed — because the complement of an arbitrary intersection is an arbitrary union of open sets. (3) Finite unions of closed sets are closed — because the complement of a finite union is a finite intersection of open sets. The union/intersection duality is important: open sets allow arbitrary unions but only finite intersections; closed sets allow arbitrary intersections but only finite unions. A standard counterexample shows that infinite unions of closed sets need not be closed: in ℝ, each singleton {1/n} is closed, but ∪{1/n : n ∈ ℕ} = {1, 1/2, 1/3, ...} is not closed because 0 is a limit point not in the set.

A key conceptual point is that "open" and "closed" are not mutually exclusive. A set can be both open and closed — such sets are called **clopen**. In every topology, ∅ and X are clopen. In a connected space these are the only clopen sets, but in a disconnected space nontrivial clopen sets exist and in fact witness the disconnection. A set can also be neither open nor closed: in ℝ, the interval [0, 1) is neither (its complement (−∞, 0) ∪ [1, ∞) is not open, so [0, 1) is not closed; and [0, 1) is not in the standard topology, so it is not open). The four possibilities — open only, closed only, both, neither — all occur in practice.

The definition of closed sets by complement may seem indirect, but it reflects a deliberate design choice in topology. The open sets are the primitive objects, specified by the axioms. Everything else — closed sets, closure, interior, continuity — is derived from them. This makes the theory economical: you do not need separate axioms for closed sets, because they follow automatically from the open-set axioms via complementation. Every theorem about open sets has a dual theorem about closed sets, obtained by replacing "open" with "closed," "union" with "intersection," and vice versa. This open/closed duality is one of the organizing principles of point-set topology.

## Questions

```yaml
- question: "In the standard topology on ℝ, can a set be both open and closed at the same time?"
  type: multiple-choice
  options:
    - "No — a set is either open or closed, never both, because the definitions are mutually exclusive"
    - "Yes, but only the empty set has this property"
    - "Yes — the empty set and ℝ itself are both open and closed in any topology"
    - "Yes, but only in discrete topologies, not standard ones"
  answer: 2
  explanation: "In any topological space, both the empty set and the whole space are simultaneously open and closed — they are called 'clopen' sets. The empty set's complement is the whole space (open), so it is closed; the whole space's complement is the empty set (open), so it too is closed. The idea that open and closed are mutually exclusive is a common misconception — the definitions are not opposites but are defined independently via the complement relationship."

- question: "In the standard topology on ℝ, which of the following sets is closed?"
  type: multiple-choice
  options:
    - "(0, 1) — because it is a bounded interval"
    - "[0, 1] — because its complement (−∞, 0) ∪ (1, ∞) is open"
    - "(0, ∞) — because it extends to infinity"
    - "[0, 1) — because it contains its left endpoint"
  answer: 1
  explanation: "A set is closed if and only if its complement is open. The complement of [0,1] is (−∞,0) ∪ (1,∞), which is a union of open intervals and therefore open — so [0,1] is closed. The set (0,1) is open (not closed), [0,1) contains 0 but its complement (−∞,0) ∪ [1,∞) is not open (since 1 is a boundary point with no open neighborhood contained in the complement), and (0,∞) is open."

- question: "The union of infinitely many closed sets is typically closed."
  type: true-false
  answer: false
  explanation: "Closed sets are closed under finite unions, but NOT arbitrary (infinite) unions. A classic counterexample: the sets {1/n} for n = 1, 2, 3, … are each closed in ℝ (single points are closed), but their union {1, 1/2, 1/3, …} is not closed — the limit point 0 is not in the set, yet every neighborhood of 0 intersects the union. Contrast with intersections: arbitrary intersections of closed sets ARE always closed."

- question: "In the standard topology on ℝ, the set [0, 1] is closed because its complement (−∞, 0) ∪ (1, ∞) is open."
  type: true-false
  answer: true
  explanation: "This is the direct application of the definition: a set C is closed if and only if its complement is open. The complement of [0,1] in ℝ is (−∞,0) ∪ (1,∞), which is a union of two open intervals and therefore open in the standard topology. Hence [0,1] is closed. This also illustrates why [0,1] 'includes its boundary points' — removing either endpoint would leave a set whose complement is no longer open."

- question: "Why is a set defined as 'closed' when its complement is open, rather than closed sets being defined by their own direct properties?"
  type: short-answer
  answer: "In topology, 'open sets' are the primitive objects — they are specified directly by the axioms of a topology. Closed sets are then defined derivatively as complements of open sets, which allows the entire theory of closed sets (and their properties like containing limit points) to be derived from the open set axioms without introducing new axioms. This duality means that every theorem about open sets has a dual theorem about closed sets, making the framework economical."
  explanation: "The definition-by-complement approach reflects the foundational structure of topology: the open sets are the basic data from which everything else is built. Defining closed sets as complements of open sets is not circular — it's a deliberate design choice that makes the open/closed duality a theorem (not an axiom) and ensures that the familiar properties of closed sets (containing limit points, being stable under arbitrary intersection) follow automatically from the open set axioms."
```
