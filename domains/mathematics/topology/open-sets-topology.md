---
id: open-sets-topology
title: Open Sets in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: topological-spaces-definition
  type: hard
builds-toward:
- closed-sets-topology
- continuous-functions-topology
- basis-for-topology
tags:
- open-sets
- fundamental
stage: formal-systems
status: draft
---

# Open Sets in Topological Spaces

## Core Idea
A set U in a topological space (X, τ) is open if U ∈ τ. Open sets are the building blocks of a topology and generalize open intervals from ℝ. They are defined by closure under arbitrary unions and finite intersections rather than by distance.

## Questions

```yaml
- question: "In the discrete topology on a non-empty set X (where τ = P(X), the power set), which statement is true?"
  type: multiple-choice
  options: ["Only X and ∅ are open", "Every subset of X is open", "Only finite subsets are open", "A set is open if and only if it contains at least one point"]
  answer: 1
  explanation: "By definition, the discrete topology on X takes τ = P(X) — every possible subset is declared open. This is the finest possible topology on X. In contrast, the indiscrete topology takes τ = {∅, X}, making option A true for that topology. Options C and D do not correspond to any standard topology."

- question: "In any topological space, a set can be simultaneously open and closed."
  type: true-false
  answer: true
  explanation: "Such sets are called 'clopen.' In every topological space, ∅ and X are both open (by the axioms) and closed (each is the complement of the other open set). In the discrete topology, every set is clopen. A connected space is precisely one where the only clopen sets are ∅ and X, so clopen sets are a meaningful concept, not a contradiction."

- question: "Why can't we define open sets in a general topological space by saying 'a set is open if every point has a positive distance to the boundary'?"
  type: short-answer
  answer: "A general topological space may have no notion of distance at all. Open sets are defined purely by membership in the collection τ satisfying three axioms (containing ∅ and X, closed under arbitrary unions, closed under finite intersections), which requires no metric."
  explanation: "The distance-to-boundary characterization works in metric spaces (like ℝⁿ) where d(x, boundary) > 0 captures open sets perfectly. But topology was developed precisely to study spaces where distance is absent or irrelevant — function spaces, quotient spaces, abstract manifolds. The axiomatic definition via τ captures the essential 'neighborhood' structure without needing a metric."
```

## Explainer

When you study real analysis, an open set in ℝ is typically defined as a set where every point has some open interval around it that stays inside the set — the set (0, 1) is open because for any x ∈ (0, 1), you can find ε > 0 so that (x−ε, x+ε) ⊆ (0, 1). This definition relies entirely on distance. Topology asks: what if we strip away distance but keep the essential structure that makes "open" useful? The answer is to simply declare which sets count as open.

A **topology** on a set X is a collection τ of subsets of X satisfying three axioms: (1) ∅ and X are in τ; (2) any union of sets in τ is in τ; (3) any finite intersection of sets in τ is in τ. A set is **open** if and only if it belongs to τ — that is the entire definition. Notice there is no mention of distance, neighborhoods, or real numbers. The axioms capture the algebraic behavior of open sets in ℝ while leaving the concept free to apply to any set at all.

The two extreme topologies illustrate the range of possibilities. The **indiscrete topology** τ = {∅, X} is the coarsest: only the empty set and the whole space are open. The **discrete topology** τ = P(X) is the finest: every subset is open. Most useful topologies live between these extremes. The standard topology on ℝ — where open sets are arbitrary unions of open intervals — is one such topology, and it can be recovered from the axiomatic definition by verifying the three properties hold.

Why only *finite* intersections? If you allow infinite intersections, open sets are no longer stable under intersection: in ℝ, the sets (-1/n, 1/n) are all open, but their intersection is {0}, which is not open. The axiom is designed to exclude this case. Arbitrary unions are allowed because union only makes sets bigger, which does not cause similar problems. These asymmetries — arbitrary unions, finite intersections — reappear constantly in topology and are worth memorizing.

Open sets are the raw material from which all other topological concepts are built. Closed sets are defined as complements of open sets. Continuity of a function f: X → Y means the preimage of every open set in Y is open in X. Compactness, connectedness, and convergence are all ultimately defined in terms of open sets. This is why getting comfortable with what "open" means at the axiomatic level — membership in τ, not proximity — is so foundational.
