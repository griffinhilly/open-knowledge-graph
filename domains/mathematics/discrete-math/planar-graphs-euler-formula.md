---
id: planar-graphs-euler-formula
title: Planar Graphs, Euler's Formula, and Structure
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-fundamentals
  type: soft
tags:
- graph-theory
- planar-graphs
stage: formal-systems
status: draft
---

# Planar Graphs, Euler's Formula, and Structure

## Core Idea
A planar graph can be drawn on a plane without edge crossings. For any connected planar graph: V - E + F = 2 (Euler's formula, where V is vertices, E is edges, F is faces). Kuratowski's theorem: a graph is planar if and only if it contains no K₅ or K₃,₃ subdivisions.

## Explainer

From graph theory fundamentals, you know vertices and edges can be connected in arbitrary ways. But draw a graph on paper and edges might cross. **Planarity** asks whether there exists *some* drawing of the graph where no two edges cross — it's a property of the abstract graph, not any particular drawing. Many graphs that look messy at first glance can be redrawn cleanly. K₄ (four vertices, all pairs connected) looks like it needs crossings, but it can be drawn as a triangle with the fourth vertex inside and edges to all corners.

Once you have a planar graph drawn without crossings, it divides the plane into regions called **faces** — including the unbounded outer region. Count the vertices (V), edges (E), and faces (F) of any connected planar graph, and you'll always find V - E + F = 2. This is **Euler's formula**, and it's remarkably universal. For a triangle: V=3, E=3, F=2 (one inner face + one outer). For a square with a diagonal: V=4, E=5, F=3 (two inner + one outer). Check: 4 - 5 + 3 = 2. The formula can be proved by induction: start with a spanning tree (which has V-1 edges and 1 face, giving V - (V-1) + 1 = 2), then add edges back one at a time, each adding one edge and splitting one face into two, keeping V - E + F constant.

Euler's formula gives you a powerful tool to *prove* a graph is not planar without needing to try every possible drawing. Since every face in a simple graph is bounded by at least 3 edges, and each edge borders at most 2 faces, we get 3F ≤ 2E, or F ≤ 2E/3. Substituting into Euler's formula: E ≤ 3V - 6. K₅ has 5 vertices and 10 edges. But 3(5) - 6 = 9 < 10, so K₅ violates the inequality and cannot be planar. Similarly K₃,₃ is ruled out using the tighter bound for bipartite graphs (every face has ≥ 4 edges).

**Kuratowski's theorem** makes this classification complete: a graph is planar *if and only if* it contains no subdivision of K₅ or K₃,₃. A subdivision means you can insert extra vertices along edges. This means those two graphs are essentially the only "obstruction" to planarity — any non-planar graph has one of them lurking inside it, possibly disguised by extra vertices on edges. This is a deep structural result: it characterizes planarity not just by a necessary inequality but by an exact forbidden-substructure criterion, connecting the combinatorial (edge counting) with the topological (embeddability in the plane).
