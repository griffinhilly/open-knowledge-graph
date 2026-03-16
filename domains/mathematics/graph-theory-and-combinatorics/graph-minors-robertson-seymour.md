---
id: graph-minors-robertson-seymour
title: Graph Minors and the Robertson–Seymour Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: planar-graphs-kuratowski-wagner
  type: soft
tags:
- graph-minors
- robertson-seymour
- well-quasi-order
stage: advanced
status: draft
---

# Graph Minors and the Robertson–Seymour Theorem

## Core Idea
A graph H is a minor of G if H can be obtained by deleting and contracting edges of G. The Robertson–Seymour theorem proves that the minor relation is a well-quasi-order, implying every minor-closed graph family is defined by finitely many forbidden minors. This deep result has profound algorithmic implications.

## How It's Best Learned
Compute minors by hand for small graphs, understanding how deletions and contractions reduce size. Recognize that tree-width and pathwidth are natural parameters arising from minor theory.

## Explainer

From your prerequisite on Kuratowski's and Wagner's theorems, you know that planarity can be characterized by forbidden substructures: a graph is planar if and only if it contains no subdivision of K₅ or K₃,₃. This is a special case of a much more general phenomenon, and the Robertson–Seymour theorem is what makes that generality precise.

A **minor** of a graph G is any graph H that can be obtained from G by three operations applied in any combination: deleting an edge, deleting an isolated vertex, or **contracting** an edge (merging the two endpoints of an edge into a single vertex and removing any resulting duplicate edges). Contraction is the key operation that distinguishes minors from subdivisions — it can reduce the size of the graph, not just refine it. Wagner's theorem, which you may have encountered alongside Kuratowski's, states that a graph is planar if and only if it has no K₅ or K₃,₃ **minor** (not just subdivision). Planarity is a **minor-closed** property: if G is planar and H is a minor of G, then H is also planar.

The **Robertson–Seymour theorem** generalizes this massively. It proves that the minor relation is a **well-quasi-order** on graphs: in any infinite sequence of graphs, some graph is a minor of a later one. This sounds technical, but its consequence is dramatic. For any minor-closed graph property (planarity, bounded tree-width, embeddability in a fixed surface), the set of graphs that are "just barely not in the family" — the **minimal forbidden minors** — is always finite. This was not obvious at all before Robertson and Seymour's work. There could in principle have been graph families requiring infinitely many forbidden minors to characterize, making any finite description impossible. The theorem rules this out entirely.

The algorithmic implications are profound: for any minor-closed property, there is a fixed-parameter tractable algorithm for testing membership, even though finding the actual forbidden minors for a given family may be extremely hard. Tree-width and path-width, which arise naturally as measures of how "tree-like" a graph is, are central parameters in this theory. Robertson and Seymour's proof, spanning over 20 papers and two decades of work, is one of the deepest results in combinatorics.
