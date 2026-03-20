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
stage: advanced
status: draft
---

# Morley Rank and Degree: Dimension in Strongly Minimal Sets

## Core Idea
Morley rank is a notion of dimension for definable sets in strongly minimal theories. A definable set has rank 0 if it is finite, rank 1 if it has infinitely many disjoint definable subsets of rank 0, etc. Morley degree counts maximal independent families of sets of the same rank. These notions allow algebraic-like dimension theory in any structure satisfying strong minimality.

## Explainer

In algebraic geometry, the dimension of a variety measures how many independent coordinates you need to specify a generic point. Morley rank generalizes this intuition to any strongly minimal structure. From your prerequisite work on strongly minimal sets, you know that a strongly minimal set D has the property that every definable subset is either finite or cofinite. This makes D "one-dimensional" in a precise sense — you can't further decompose it into infinitely many infinite pieces. Morley rank makes this precise and extends it.

**Morley rank** is defined by ordinal induction. A definable set X has **rank 0** (written MR(X) = 0) if X is finite. It has **rank ≥ 1** if there exist infinitely many pairwise disjoint definable subsets of X each of rank ≥ 0 — that is, if X contains infinitely many distinct finite pieces (which means X is infinite). More generally, MR(X) ≥ α + 1 if there exist infinitely many pairwise disjoint definable subsets of X each with Morley rank ≥ α. In a strongly minimal structure, the universe D has rank exactly 1: it is infinite (rank ≥ 1), but you cannot find infinitely many disjoint infinite definable pieces (by strong minimality, each would have to be cofinite, which is impossible). So MR(D) = 1.

**Morley degree** (MD) captures multiplicity within a given rank. Once you know MR(X) = α, MD(X) is the maximum number of pairwise disjoint definable subsets of X that each have rank exactly α. Degree 1 means X is "irreducible" at its rank level — analogous to an irreducible variety. Degree 2 means X splits into exactly two rank-α pieces. In algebraically closed fields, a definable set corresponding to a degree-d polynomial curve has Morley degree d.

The power of rank and degree is that they turn model-theoretic questions about definable sets into something that behaves like algebraic dimension theory. You can add ranks (MR of a product is the sum of ranks), compare definable sets by dimension, and classify types by their rank. In the strongly minimal setting, a type p ∈ S(A) has a well-defined Morley rank (the rank of the definable set it "concentrates on"), and rank 1 types over algebraically closed sets are the "generic" types — the model-theoretic analogues of generic points on a variety. This machinery is the foundation for Morley's categoricity theorem and the broader stability program.
