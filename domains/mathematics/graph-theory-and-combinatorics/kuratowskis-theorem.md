---
id: kuratowskis-theorem
title: Kuratowski's Theorem and Forbidden Minors
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: planar-graphs
  type: hard
builds-toward:
- wagners-theorem
- graph-minors
tags:
- graph-theory
- planar-graphs
stage: formal-systems
status: draft
---

# Kuratowski's Theorem and Forbidden Minors

## Core Idea
Kuratowski's Theorem characterizes planar graphs by forbidden minors: a graph is planar if and only if it contains no subdivision of K₅ or K₃,₃. This shows that planarity is completely determined by the absence of two specific topological structures, providing a constructive understanding of why certain graphs cannot be drawn planar.

## Explainer

From your study of planar graphs, you know that a graph is **planar** if it can be drawn in the plane with no edge crossings. You also know that K₅ (the complete graph on 5 vertices) and K₃,₃ (the complete bipartite graph with three vertices on each side) are the two canonical non-planar graphs — both fail Euler's formula and cannot be drawn without crossings. Kuratowski's theorem tells you that these two graphs are not just examples of non-planarity — they are its complete explanation.

The precise statement involves **subdivisions**. A subdivision of a graph G is obtained by inserting additional vertices of degree 2 into edges, effectively replacing each edge with a path. This doesn't change the essential crossing structure — if K₅ can't be drawn planar, then a graph with a subdivided K₅ embedded inside it (as a subgraph after those edge-subdivision vertices are added) also can't be drawn planar. The theorem says: a graph is planar if and only if it contains no subgraph that is a subdivision of K₅ or K₃,₃. In other words, **K₅ and K₃,₃ are the only obstruction families for planarity**.

Why these two and not others? The intuition comes from counting. K₅ has 5 vertices and 10 edges; for a planar graph, Euler's formula gives E ≤ 3V − 6, so we need 10 ≤ 9 — a contradiction. K₃,₃ has 6 vertices and 9 edges; it's bipartite, so it has no triangles, meaning every face has at least 4 edges, which gives E ≤ 2V − 4 = 8 — another contradiction. These are the minimal graphs that violate planarity: remove any vertex or edge from either one and the result is planar. This minimality is exactly what makes them the right "forbidden" structures.

The proof that K₅ and K₃,₃ subdivisions are *sufficient* to obstruct planarity is the hard direction — it was proved by Kazimierz Kuratowski in 1930 and requires showing that any non-planar graph must contain one of them. The related **Wagner's theorem** (your next topic) gives an equivalent characterization using graph minors instead of subdivisions — contracting edges rather than inserting vertices. Together, these theorems opened the field of **graph minor theory**, culminating in the Robertson–Seymour theorem, which shows that every graph property closed under minors can be characterized by a finite list of forbidden minors. Planarity, with just two forbidden minors, was the first and simplest example of this deep pattern.
