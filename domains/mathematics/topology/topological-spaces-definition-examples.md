---
id: topological-spaces-definition-examples
title: 'Topological Spaces: Definition and Examples'
domain: mathematics
course: topology
prerequisites:
- id: set-theory-basics
  type: hard
- id: equivalence-relations
  type: soft
builds-toward:
- open-sets-definition-examples
- neighborhoods-topology-definition
tags:
- foundations
- definition
stage: formal-systems
status: validated
---

# Topological Spaces: Definition and Examples

## Core Idea
A topological space (X, τ) consists of a set X and a collection τ of subsets called open sets satisfying: ∅ and X are open, any union of open sets is open, and finite intersections of open sets are open. This structure generalizes the notion of 'open' from real analysis to arbitrary sets and forms the foundation of topology.

## Questions

```yaml
- question: "Why does the definition of a topology require finite intersections of open sets to be open, but allows ARBITRARY (including infinite) unions of open sets to be open?"
  type: multiple-choice
  options:
    - "Finite intersections are computationally easier to verify, so the axiom is a practical convenience"
    - "Infinite unions can always be reduced to finite ones by compactness, so infinite unions are not a meaningful additional requirement"
    - "Infinite intersections of open sets can fail to be open — for example, the intersection of all intervals (−1/n, 1/n) in ℝ is {0}, which is not open — so allowing them would collapse the structure"
    - "The axiom is asymmetric for historical reasons only; both could have been stated for finite collections"
  answer: 2
  explanation: "The asymmetry is mathematically essential, not accidental. In ℝ, the open sets (−1/n, 1/n) for n = 1, 2, 3, … are each open, but their infinite intersection is exactly the single point {0}, which is closed (not open) in the standard topology. Allowing infinite intersections in the axioms would let you build closed sets from open ones through the back door, destroying the distinction between open and closed that topology depends on. Infinite unions pose no such problem: any union of open sets in ℝ is open."

- question: "On the set X = {a, b, c}, which of the following collections is a valid topology?"
  type: multiple-choice
  options:
    - "τ = {∅, {a}, {b}, X} — contains the required sets and several singletons"
    - "τ = {∅, {a}, {a, b}, X} — contains ∅ and X, and is closed under union and finite intersection"
    - "τ = {∅, {a}, {b, c}} — contains ∅ and a partition of X into two parts"
    - "τ = {{a}, {b}, {c}, X} — contains all singletons and the full set"
  answer: 1
  explanation: "Check τ = {∅, {a}, {a,b}, X}: unions — {a} ∪ {a,b} = {a,b} ✓; {a} ∪ ∅ = {a} ✓; all others stay in τ. Intersections — {a} ∩ {a,b} = {a} ✓; all others ✓. Option A fails: {a} ∪ {b} = {a,b} ∉ τ. Option C fails: it doesn't contain X. Option D fails: it doesn't contain ∅, and {a} ∪ {b} = {a,b} ∉ τ. The key check is always closure under union and finite intersection."

- question: "In the discrete topology on any set X, every subset of X is an open set."
  type: true-false
  answer: true
  explanation: "The discrete topology is τ = 𝒫(X) — the power set, all subsets of X. It satisfies all three axioms: ∅ and X are in 𝒫(X); any union of subsets of X is a subset of X; any finite intersection of subsets of X is a subset of X. It is the finest possible topology on X — no topology can have more open sets. In a metric space analogue, the discrete topology corresponds to every point being isolated, with every set of points being a union of isolated points and therefore open."

- question: "Any collection τ of subsets of X that contains both ∅ and X is a valid topology on X."
  type: true-false
  answer: false
  explanation: "Containing ∅ and X is necessary but not sufficient. τ must also be closed under arbitrary unions (any union of sets in τ must be in τ) and closed under finite intersections (any finite intersection of sets in τ must be in τ). For example, on X = {a,b,c}, the collection τ = {∅, {a}, {b}, X} contains ∅ and X but fails closure under union: {a} ∪ {b} = {a,b} ∉ τ. So τ is not a topology despite satisfying the first axiom."

- question: "What is the key conceptual advantage of defining topology without reference to distance? Why does this generalization matter for mathematics?"
  type: short-answer
  answer: "By replacing the distance-based definition of 'open set' with three axiomatic properties, topology makes the key theorems of analysis (continuity, convergence, connectedness, compactness) apply to any set where those axioms hold — regardless of whether distances make sense. This means a single proof in the topological setting yields results for real analysis, complex analysis, function spaces, manifolds, and purely combinatorial or algebraic structures simultaneously."
  explanation: "The metric definition of open set is specific to spaces where distance is defined. Many important mathematical objects — spaces of functions, quotient spaces, abstract algebraic structures — have meaningful notions of 'nearness' without a natural distance. Topology abstracts the essential behavior (what open sets do) from the specific mechanism (distance). Every theorem proved in pure topological language is automatically a theorem in every metric space, every manifold, and every other topological space. This is the payoff of the axiomatization."
```

## Explainer

In real analysis, an open set in ℝ is one where every point has an open interval around it entirely contained in the set. This definition works beautifully — but it depends on the notion of distance. What if you want to study continuity and connectedness on a set where there is no natural notion of distance? Topology answers this by isolating the minimum structure needed: instead of defining "open" in terms of distance, you simply declare which sets are open, subject to three axioms that capture how open sets in ℝ actually behave.

The three axioms for a **topology** τ on a set X are: (1) the empty set ∅ and the whole set X are in τ; (2) any union of sets in τ is in τ — even infinite unions; (3) any **finite** intersection of sets in τ is in τ. The asymmetry between (2) and (3) is deliberate and important. In ℝ, the intersection of the open sets (−1/n, 1/n) for all n = 1, 2, 3, … is the single point {0}, which is not open. Allowing infinite intersections would let you generate closed sets from open sets through the back door, collapsing the structure. The axioms are carefully calibrated to permit enough structure for interesting topology while avoiding this collapse.

To build intuition, consider three extreme examples on the same set X = {a, b, c}. The **discrete topology** τ = 𝒫(X) (all subsets are open) is the finest possible topology — every set is open. The **indiscrete topology** τ = {∅, X} is the coarsest — only the two required sets are open. Between these extremes lie all other topologies, such as τ = {∅, {a}, X}, which is finer than the indiscrete but coarser than the discrete. Each topology encodes a different notion of which points are "close together": in the indiscrete topology, you cannot separate any two points with open sets at all, so in a sense every point is adjacent to every other.

The payoff is generality with preservation of key theorems. Continuous functions, convergence, connectedness, and compactness can all be defined purely in terms of open sets — no distances required. This means every theorem you prove in the topological setting applies automatically to metric spaces, function spaces, and far stranger settings. The set X you bring to topology can be almost anything: the real line, a finite set, a space of functions, a manifold. The topology τ specifies what "nearby" means in that context, and the three axioms ensure the structure is rich enough to do geometry with.
