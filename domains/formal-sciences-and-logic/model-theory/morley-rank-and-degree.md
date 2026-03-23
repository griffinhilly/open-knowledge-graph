---
id: morley-rank-and-degree
title: 'Morley Rank and Degree: Dimension in Strongly Minimal Sets'
domain: formal-sciences-and-logic
course: model-theory
prerequisites:
- id: strongly-minimal-and-geometry
  type: hard
- id: definable-closure-independence
  type: hard
builds-toward:
- stability-and-instability-dividing-line
tags:
- Morley-rank
- degree
- strongly-minimal
- dimension
stage: expert
status: validated
---

# Morley Rank and Degree: Dimension in Strongly Minimal Sets

## Core Idea
Morley rank is a notion of dimension for definable sets in strongly minimal theories. A definable set has rank 0 if it is finite, rank 1 if it has infinitely many disjoint definable subsets of rank 0, etc. Morley degree counts maximal independent families of sets of the same rank. These notions allow algebraic-like dimension theory in any structure satisfying strong minimality.

## Questions

```yaml
- question: "In a strongly minimal structure, the universe D has Morley rank exactly 1. Why can D not have Morley rank 2?"
  type: multiple-choice
  options:
    - "D has rank 2 if it is uncountable, and rank 1 if it is countable — the rank depends on cardinality"
    - "Morley rank ≥ 2 would require infinitely many pairwise disjoint definable subsets of D each of rank ≥ 1 — but strong minimality says every definable subset is finite or cofinite, making this impossible"
    - "Rank 2 is reserved for structures with more than one sort, while D is a single-sorted domain"
    - "Rank is always 1 for any infinite set in first-order logic — the hierarchy only distinguishes finite from infinite"
  answer: 1
  explanation: "MR(D) ≥ 2 requires infinitely many pairwise disjoint definable subsets of D that each have MR ≥ 1, meaning each is infinite. But strong minimality says every definable subset of D is either finite or cofinite — so any infinite definable subset has cofinite complement, and you cannot fit infinitely many cofinite sets into D while keeping them pairwise disjoint. The rank therefore stops at exactly 1. D is infinite (rank ≥ 1) but cannot be decomposed into infinitely many infinite pieces (rank not ≥ 2). This is the precise sense in which strongly minimal sets are 'one-dimensional.'"

- question: "A definable set X in a strongly minimal structure has Morley rank 1 and Morley degree 2. What does this imply about X?"
  type: multiple-choice
  options:
    - "X contains exactly 2 elements"
    - "X can be partitioned into exactly 2 pairwise disjoint definable subsets each of rank 1 — it is 'reducible' into two rank-1 components"
    - "X has two equivalent definitions in the theory, reflecting a symmetry in the language"
    - "X is the union of a rank-1 set and a rank-0 (finite) set"
  answer: 1
  explanation: "Morley degree counts the maximum number of pairwise disjoint rank-α pieces that X can be partitioned into. If MR(X) = 1 and MD(X) = 2, then X decomposes into exactly two rank-1 definable parts and no more — analogous to a reducible algebraic curve of degree 2 that factors into two irreducible components. Degree 1 means X is 'irreducible' at its rank level; degree 2 means it splits into exactly two maximal pieces of the same rank. The count refers to pieces of the *same rank*, not to the total number of elements."

- question: "In algebraically closed fields, a definable set corresponding to a degree-d polynomial (viewed over an algebraically closed field) has Morley degree d, so Morley degree directly generalizes algebraic degree."
  type: true-false
  answer: true
  explanation: "This is precisely the connection that makes Morley rank and degree feel like a genuine generalization of algebraic geometry. In ACF, the zero set of an irreducible polynomial of degree d has Morley degree d — it splits into d irreducible algebraic components in the appropriate sense. The Morley rank of a curve (a one-dimensional algebraic set) is 1, and the Morley degree counts its 'algebraic multiplicity.' This parallel motivates why the model-theoretic machinery recovers genuine geometric intuition in the algebraic setting."

- question: "Morley rank is a measure of the cardinality of a definable set — a set with more elements always has higher Morley rank."
  type: true-false
  answer: false
  explanation: "Morley rank measures structural complexity, not cardinality. In a strongly minimal structure, every infinite definable set has Morley rank 1, regardless of whether it is countably or uncountably infinite. Finite sets have rank 0. Two infinite definable sets with very different cardinalities can have the same Morley rank. Conversely, a finite set and a cofinite set in a strongly minimal structure have ranks 0 and 1 respectively — the cardinality jump is enormous but the rank difference is just 1. Morley rank tracks how many levels of definable decomposition are possible, not raw size."

- question: "Why does a strongly minimal set have Morley rank exactly 1, rather than 0 or higher?"
  type: short-answer
  answer: "A strongly minimal set D has rank 0 only if it is finite — but strong minimality itself requires D to be infinite (the definition applies to an infinite domain where every definable subset is finite or cofinite). So rank is at least 1. Rank ≥ 2 would require infinitely many pairwise disjoint infinite definable subsets of D. But every infinite definable subset of D is cofinite by strong minimality, and you cannot have two disjoint cofinite subsets of D — each would contain all but finitely many elements, so they could not be disjoint. Therefore rank is exactly 1: D is infinite (rank ≥ 1) but cannot be decomposed into infinitely many infinite definable pieces (rank < 2)."
  explanation: "This argument is the heart of why strongly minimal sets are called 'one-dimensional.' The impossibility of infinite disjoint infinite decomposition is precisely the strong minimality condition translated into rank language. All of Morley's categoricity theorem and much of stability theory builds on this tight connection between the syntactic property (every formula defines a finite or cofinite set) and the rank-theoretic dimension theory."
```

## Explainer

In algebraic geometry, the dimension of a variety measures how many independent coordinates you need to specify a generic point. Morley rank generalizes this intuition to any strongly minimal structure. From your prerequisite work on strongly minimal sets, you know that a strongly minimal set D has the property that every definable subset is either finite or cofinite. This makes D "one-dimensional" in a precise sense — you can't further decompose it into infinitely many infinite pieces. Morley rank makes this precise and extends it.

**Morley rank** is defined by ordinal induction. A definable set X has **rank 0** (written MR(X) = 0) if X is finite. It has **rank ≥ 1** if there exist infinitely many pairwise disjoint definable subsets of X each of rank ≥ 0 — that is, if X contains infinitely many distinct finite pieces (which means X is infinite). More generally, MR(X) ≥ α + 1 if there exist infinitely many pairwise disjoint definable subsets of X each with Morley rank ≥ α. In a strongly minimal structure, the universe D has rank exactly 1: it is infinite (rank ≥ 1), but you cannot find infinitely many disjoint infinite definable pieces (by strong minimality, each would have to be cofinite, which is impossible). So MR(D) = 1.

**Morley degree** (MD) captures multiplicity within a given rank. Once you know MR(X) = α, MD(X) is the maximum number of pairwise disjoint definable subsets of X that each have rank exactly α. Degree 1 means X is "irreducible" at its rank level — analogous to an irreducible variety. Degree 2 means X splits into exactly two rank-α pieces. In algebraically closed fields, a definable set corresponding to a degree-d polynomial curve has Morley degree d.

The power of rank and degree is that they turn model-theoretic questions about definable sets into something that behaves like algebraic dimension theory. You can add ranks (MR of a product is the sum of ranks), compare definable sets by dimension, and classify types by their rank. In the strongly minimal setting, a type p ∈ S(A) has a well-defined Morley rank (the rank of the definable set it "concentrates on"), and rank 1 types over algebraically closed sets are the "generic" types — the model-theoretic analogues of generic points on a variety. This machinery is the foundation for Morley's categoricity theorem and the broader stability program.
