---
id: continuity-topological-definition
title: Continuity in Topological Spaces
domain: mathematics
course: topology
prerequisites:
- id: open-sets-definition-examples
  type: hard
- id: neighborhoods-topology-definition
  type: soft
builds-toward:
- homeomorphisms-definition-properties
- quotient-maps-definition
tags:
- continuity
- maps
stage: abstract-reasoning
status: draft
---

# Continuity in Topological Spaces

## Core Idea
A function f: X → Y is continuous if the preimage of every open set in Y is open in X. Equivalently: the preimage of every closed set is closed; f is continuous at x if for every neighborhood V of f(x), there exists a neighborhood U of x with f(U) ⊆ V. This generalizes ε-δ continuity and is the natural definition in topology.

## Explainer

You know what open sets are: subsets whose structure is defined by the topology axioms rather than by a distance formula. Continuity in topology is defined entirely through open sets, stripping away the ε-δ machinery of calculus while capturing the same essential idea — that nearby inputs produce nearby outputs.

The definition: f: X → Y is **continuous** if for every open set V ⊆ Y, its **preimage** f⁻¹(V) = {x ∈ X : f(x) ∈ V} is open in X. The preimage pulls a subset of the output space back to a subset of the input space. Continuity says: the topology on X is fine-grained enough to detect all the open structure of Y through f. To see why this matches the intuitive idea, compare with ε-δ: f is continuous at x₀ if for every open ball around f(x₀), there is an open ball around x₀ that maps inside it. The topological version simply replaces "open ball" with "open set" — and since open balls generate the topology on metric spaces, the two definitions agree there.

The power of the topological definition is that it works in any topological space, not just metric spaces or ℝⁿ. You never need a notion of distance — only the topology (the collection of open sets). This lets you talk about continuous functions between function spaces, infinite-dimensional manifolds, or combinatorial structures where no natural metric exists. The preimage direction also has clean logical structure: to check continuity you look at what happens to neighborhoods of the output and ask whether their preimages are open in the input. You are checking a **global** condition on the function, not a local ε-δ condition at each point separately.

A key application is the characterization of **homeomorphisms** — topological equivalences. A homeomorphism is a continuous bijection f: X → Y whose inverse f⁻¹ is also continuous. Two spaces are homeomorphic if there is a homeomorphism between them, meaning their open sets correspond exactly under f. They are "the same" topologically: every topological property of one holds for the other. The topological definition of continuity is what makes this equivalence relation precise, and the preimage formulation is what makes it tractable to verify.
