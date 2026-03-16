---
id: graph-minors
title: Graph Minors and Minor-Closed Families
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-theory-intro
  type: hard
tags:
- graph-theory
- minors
- structure
stage: advanced
status: draft
---

# Graph Minors and Minor-Closed Families

## Core Idea
A graph H is a minor of G if H can be obtained by deleting vertices/edges and contracting edges. Minor-closed families are sets closed under taking minors (e.g., planar graphs, forests, bounded treewidth graphs). The theory of graph minors underpins modern structural graph theory and has led to deep results about decomposition and decidability.

## Explainer

You know from graph theory that subgraphs are obtained by removing vertices and edges. **Graph minors** introduce a third operation: **edge contraction**. To contract an edge {u, v}, you merge u and v into a single new vertex w, and every edge that previously connected to u or v now connects to w (deleting any resulting loops or duplicate edges). A graph H is a **minor** of G if H can be obtained from G by any combination of these three operations — deleting vertices, deleting edges, and contracting edges — in any order. Crucially, H doesn't need to look anything like a subgraph of G; contraction lets you "collapse" structure in ways that deletion alone cannot.

The best way to build intuition is with a concrete example. Start with a cycle on 5 vertices (C₅). Contract one edge — you merge two adjacent vertices and get a cycle on 4 vertices (C₄). Contract another — you get a triangle (C₃). So C₃ is a minor of C₅. More dramatically: the complete graph K₄ is a minor of almost any sufficiently connected graph, because you can always find four "blobs" of vertices that are mutually connected and contract each blob to a single vertex. The **complete graph K₅** and the **complete bipartite graph K₃,₃** are the two obstructions to planarity in Kuratowski's theorem, but the minor version (Wagner's theorem) says a graph is planar if and only if it has neither K₅ nor K₃,₃ as a **minor** — a cleaner and more fundamental statement.

A family of graphs is **minor-closed** if, whenever G is in the family, every minor of G is also in the family. Planar graphs form a minor-closed family: any minor of a planar graph is still planar (deleting or contracting edges can't introduce crossings). Forests (acyclic graphs) are minor-closed: removing edges or contracting them in a tree gives smaller trees or single vertices. **Bounded treewidth** graphs are minor-closed, and treewidth is a fundamental measure of how "tree-like" a graph is — many NP-hard problems become polynomial when restricted to bounded-treewidth graphs.

The deepest result in this area is the **Robertson-Seymour theorem** (Graph Minor Theorem): in any infinite sequence of graphs, some graph is a minor of a later one. Equivalently, every minor-closed family can be characterized by a *finite* list of **forbidden minors** — graphs not in the family such that any minor not in the family contains one of these as a minor. Planar graphs have exactly two forbidden minors (K₅ and K₃,₃). Forests have one (a triangle). The Robertson-Seymour theorem guarantees such a finite list exists for *every* minor-closed family, even when we don't know what the list is. This connects abstract structure theory to algorithms: if you can recognize a forbidden minor in polynomial time, you can recognize membership in the family in polynomial time, giving a meta-theorem that produces efficient algorithms from structural characterizations.
