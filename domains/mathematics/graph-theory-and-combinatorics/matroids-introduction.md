---
id: matroids-introduction
title: Introduction to Matroids
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-theory-intro
  type: soft
tags:
- combinatorics
- matroids
stage: advanced
status: draft
---

# Introduction to Matroids

## Core Idea
A matroid is a pair (E, I) where E is a finite set and I is a family of subsets (independent sets) satisfying exchange properties, generalizing linear independence and forests. Matroids unify diverse concepts: graphic matroids (forest spanning), linear matroids (linear independence), partition matroids. Greedy algorithms on matroids yield optimal solutions.

## How It's Best Learned
Work with specific matroid examples (graphic, linear, partition) and verify the independence axioms hold for each.

## Common Misconceptions
Matroids generalize both linear independence and forests, but not all set systems satisfying certain properties are matroids; the exchange axiom is crucial.

## Explainer

Think about two things you already know from graph theory. First: the **forests** of a graph — subsets of edges with no cycles. Any subset of a forest is itself a forest, and if you have two forests of different sizes, you can always add an edge from the larger one to the smaller to get a bigger forest. Second: **linear independence** in a vector space. Any subset of an independent set is independent, and if you have two independent sets of different sizes, you can always add a vector from the larger to the smaller and preserve independence. These two properties — closure under taking subsets, and the "exchange" property — are not just a coincidence. They're the axioms of a **matroid**.

Formally, a matroid is a pair (E, I) where E is a finite ground set and I is a collection of **independent sets** satisfying three axioms: (1) the empty set is independent; (2) any subset of an independent set is independent; (3) if A and B are both independent and |A| < |B|, then there exists an element in B \ A that can be added to A while preserving independence. Axiom (3) is the **exchange axiom** — the defining property that separates matroids from arbitrary set systems. It ensures that all "maximal independent sets" (called **bases**) have the same size, a key structural fact.

The two motivating examples are **graphic matroids** and **linear matroids**. In a graphic matroid, E is the edge set of a graph and I is the family of forests (acyclic subgraphs). Bases are spanning forests. In a linear matroid (also called a vector matroid), E is a set of vectors and I is the collection of linearly independent subsets. Bases are maximal linearly independent sets. Both satisfy the matroid axioms — this is a theorem, not just an analogy. A third example is the **partition matroid**: partition E into groups, and declare a set independent if it takes at most kᵢ elements from group i. The constraints are independent per group, and the exchange axiom holds.

The payoff for this abstraction is the **greedy algorithm theorem**: if you want to find a maximum-weight basis of a matroid (equivalently, a maximum-weight independent set that can't be extended), the greedy algorithm works — always add the highest-weight element that keeps the current set independent. This theorem explains why Kruskal's minimum spanning tree algorithm is correct (graphic matroid), why greedy works for certain scheduling problems (partition matroids), and why it fails for many other problems (those not describable as matroids). Matroids are precisely the combinatorial structures on which greedy is optimal — a beautiful and exact characterization.
