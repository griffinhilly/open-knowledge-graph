---
id: sequences-convergence-topology
title: Convergence of Sequences in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: limit-points-and-accumulation
  type: hard
builds-toward:
- continuous-functions-topology
- first-countable-spaces
tags:
- sequences
- convergence
stage: formal-systems
status: validated
---

# Convergence of Sequences in Topological Spaces

## Core Idea
A sequence (xₙ) converges to x in a topological space if every open set containing x eventually contains all terms of the sequence—that is, for every open U containing x, there exists N such that xₙ ∈ U for all n ≥ N. This generalizes the ε-ball definition from metric spaces. Unlike metric spaces, limits in general topological spaces need not be unique; uniqueness requires the Hausdorff separation axiom. Furthermore, sequences alone may not suffice to characterize the topology—in non-first-countable spaces, nets or filters are needed to fully describe convergence behavior.

## How It's Best Learned
Compare convergence in a metric space with convergence in the cofinite topology on an infinite set, where sequences can converge to every point simultaneously. This dramatic contrast motivates why separation axioms matter.

## Common Misconceptions
Students often assume sequential convergence fully determines the topology. This holds in metric and first-countable spaces but fails in general. Also, a sequence can have multiple limits in non-Hausdorff spaces—this is a feature of the topology, not an error.

## Explainer

A sequence (xₙ) in a topological space X **converges** to a point x if for every open set U containing x, there exists a natural number N such that xₙ ∈ U for all n ≥ N. In words: the sequence eventually enters and stays inside every open neighborhood of x. This generalizes the ε-ball definition from metric spaces — in a metric space, "every open set containing x" can be replaced by "every ball B(x, ε)," recovering the familiar condition d(xₙ, x) < ε for all sufficiently large n. But in a general topological space, there may be no metric, so the open-set formulation is the primitive definition.

A striking difference from metric spaces is that limits need not be unique. In the cofinite topology on an infinite set X, every open neighborhood of any point x has finite complement — so it contains all but finitely many elements of X. This means that any sequence of distinct points is eventually inside every neighborhood of every point, so it converges to every point simultaneously. Uniqueness of limits requires the **Hausdorff axiom** (T₂): if distinct points x and y have disjoint open neighborhoods U and V, then a sequence cannot eventually be in both, forcing at most one limit. In non-Hausdorff spaces, the failure of limit uniqueness is a feature of the topology, not an error.

Another fundamental limitation is that sequences may not suffice to characterize the topology. In metric spaces and more generally in **first-countable spaces** (where every point has a countable neighborhood base), sequences detect all topological information: a set is closed if and only if it is sequentially closed, and a function is continuous if and only if it preserves convergent sequences. But in spaces that are not first-countable — such as uncountable products with the product topology — a set can fail to be closed even though no sequence from the set converges outside it. Sequences, indexed by the countable set ℕ, cannot probe all the open neighborhoods of a point when there are uncountably many directions of approach.

To handle convergence in full generality, topology employs **nets** and **filters**. A net is a generalization of a sequence where the index set is an arbitrary directed set rather than ℕ. Nets can characterize all topological properties that sequences cannot: a set is closed if and only if it contains the limits of all convergent nets from the set, and a function is continuous if and only if it preserves convergent nets. Filters provide an equivalent framework using collections of subsets instead of indexed families. In first-countable spaces, nets and filters reduce to sequences, so the more general tools are genuinely needed only beyond the first-countable setting. Understanding where sequences suffice and where they fail is a key conceptual milestone in moving from metric topology to general topology.

## Questions

```yaml
- question: "In the cofinite topology on an infinite set X (open sets are sets with finite complement, plus ∅), what happens to sequences of distinct points?"
  type: multiple-choice
  options:
    - "No sequences converge, because the topology is too coarse to pin down a limit"
    - "Each sequence converges to at most one point, just as in a metric space"
    - "Every sequence of distinct points converges to every point in X simultaneously"
    - "Sequences converge only to accumulation points of the underlying set"
  answer: 2
  explanation: "In the cofinite topology, every open set containing any point x has a finite complement — so it contains all but finitely many elements of X. For a sequence (xₙ) of distinct points and any point x, every open neighborhood of x excludes only finitely many terms, so the sequence is eventually inside every such neighborhood. Therefore the sequence converges to x — and simultaneously to every other point. This dramatically illustrates why limits need not be unique in non-Hausdorff spaces."

- question: "A topology student claims: 'If x is a limit point of the set S, then there must be a sequence from S converging to x.' In a general topological space, this claim is:"
  type: multiple-choice
  options:
    - "Always true — limit points are defined precisely by sequences approaching them"
    - "False in general — in non-first-countable spaces, a point can be a limit point of S without any sequence from S converging to it; nets or filters are needed to detect all limit points"
    - "True in all Hausdorff spaces regardless of countability"
    - "True only in spaces where every open set is also closed"
  answer: 1
  explanation: "This is the key failure of sequences in general topology. In metric spaces and first-countable spaces, sequences detect limit points because every point has a countable neighborhood base. But in non-first-countable spaces (such as uncountable products with the product topology), a point can accumulate in a set without any sequence from that set converging to it — there are too many open sets and too few sequences to probe them all. Nets (indexed by directed sets) and filters are rich enough to detect all limit points. This is why sequences cannot fully characterize topology in general."

- question: "In a Hausdorff topological space, every convergent sequence has exactly one limit."
  type: true-false
  answer: true
  explanation: "The Hausdorff condition requires that any two distinct points have disjoint open neighborhoods. If (xₙ) converged to both x and y with x ≠ y, take disjoint open sets U ∋ x and V ∋ y. The sequence must eventually be in U (by convergence to x) and eventually in V (by convergence to y). But U ∩ V = ∅, so the sequence cannot eventually be in both — contradiction. The Hausdorff axiom is precisely the condition that forces limit uniqueness."

- question: "In a general topological space, knowing which sequences converge and to what limits is sufficient to largely determine the topology."
  type: true-false
  answer: false
  explanation: "This holds only in first-countable spaces (where every point has a countable neighborhood base), which includes all metric spaces. In spaces like an uncountable product with the product topology, or a space with the cocountable topology on an uncountable set, different topologies can agree on all sequence convergences yet be genuinely distinct. To fully characterize topology in general, nets (indexed by arbitrary directed sets) or filters are required. Sequences are indexed by ℕ and simply cannot probe all the open sets in non-first-countable spaces."

- question: "Why do sequences fail to fully characterize convergence in general topological spaces? What is needed instead, and why does this limitation not arise in metric spaces?"
  type: short-answer
  answer: "Sequences are indexed by the natural numbers — a countable index set. In a metric space, every point has a countable neighborhood base (the balls of radius 1/n), so all topological information about a point can be detected by a countable approach. But in general topological spaces, a point may have uncountably many 'directions' of approach, none of which can be captured by any single sequence. Nets generalize sequences by allowing the index set to be any directed set, and filters provide an equivalent framework using collections of subsets. Both are rich enough to detect all limit points and fully characterize the topology. The limitation does not arise in metric spaces because first-countability guarantees that sequences suffice — the countable neighborhood base acts as a 'decoder' from topological structure to sequential behavior."
  explanation: "First-countable spaces are precisely those where sequential convergence and topological convergence coincide. Beyond that class, topology and sequence behavior come apart — a function can preserve all convergent sequences without being continuous."
```

