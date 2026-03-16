---
id: introduction-matroids
title: Introduction to Matroids
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: formal-definitions-graph-theory
  type: soft
- id: linear-independence
  type: soft
tags:
- matroids
- independence
- greedy-algorithms
stage: advanced
status: draft
---

# Introduction to Matroids

## Core Idea
A matroid abstracts the notion of independence familiar from linear algebra and graph theory. A matroid on a finite set E is defined by an independence system satisfying the exchange axiom. Matroids unify spanning forests, linear independence, and transversals, enabling elegant min-max theorems and efficient greedy algorithms.

## Explainer

A **matroid** is a mathematical structure designed to capture what "independence" means in the most general and abstract way. You have already seen independence in two settings from your prerequisites: in linear algebra, a set of vectors is **linearly independent** if none is a linear combination of the others; in graph theory, a set of edges is **acyclic** (forms a forest) if it contains no cycle. These two notions seem unrelated on the surface, but they share deep structural properties — and matroid theory identifies exactly what those properties are.

Formally, a matroid is a pair (E, I) where E is a finite **ground set** and I is a collection of **independent sets** satisfying three axioms: (1) the empty set is independent; (2) if a set is independent, every subset is too (the **hereditary property**); and (3) if I and J are both independent and |I| < |J|, then some element of J can be added to I to produce a larger independent set (the **exchange axiom**). The exchange axiom is the heart of matroid theory. In vector spaces, it corresponds to the basis extension theorem: a smaller independent set can always be extended to a basis by adding vectors from a larger one. In graphs, it corresponds to the fact that a smaller spanning forest of a graph can always be extended by adding an edge from a larger spanning forest.

The exchange axiom has a powerful algorithmic consequence: **greedy algorithms work optimally on matroids**. If each element of E has a weight, the greedy algorithm — always add the heaviest-weight element that keeps the current set independent — finds the maximum-weight basis. This unifies two classical algorithms: Kruskal's algorithm for minimum spanning trees (the **graphic matroid**, where independent sets are acyclic edge sets) and Gaussian elimination for finding a basis of a vector space (the **linear matroid**). Both are greedy algorithms, and both work correctly because they operate on a matroid. Wherever you see a greedy algorithm working without any clever argument, there is often a matroid structure lurking underneath.

Beyond graph and linear matroids, there are many others: **transversal matroids** arise from bipartite matchings (connecting to the Hall's theorem you may have seen), **partition matroids** arise from independence constraints within blocks, and **uniform matroids** treat all k-element subsets as independent. The **matroid intersection theorem** gives a min-max characterization of the largest common independent set of two matroids — a deep result with applications to scheduling, network design, and combinatorial optimization. Matroid theory also identifies exactly when greedy fails: if a combinatorial problem lacks a matroid structure, greedy typically produces suboptimal solutions, and the problem often becomes NP-hard. Recognizing matroid structure is therefore a key tool for algorithm designers.
