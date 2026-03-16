---
id: planar-graphs
title: Planar Graphs and Euler's Formula
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-connectivity
  type: hard
- id: trees-in-graph-theory
  type: soft
builds-toward:
- graph-coloring
tags:
- planar-graphs
- euler-formula
- kuratowski
- faces
- four-color-theorem
stage: formal-systems
status: validated
---

# Planar Graphs and Euler's Formula

## Core Idea
A graph is planar if it can be drawn in the plane with no edge crossings. For any connected planar graph, Euler's formula states V − E + F = 2, where V, E, F are the counts of vertices, edges, and faces (including the unbounded outer face). This implies every simple planar graph satisfies E ≤ 3V − 6, providing a quick non-planarity test. Kuratowski's theorem characterizes planarity completely: a graph is planar if and only if it contains no subdivision of K₅ or K₃,₃.

## How It's Best Learned
Draw K₄ without crossings to see planarity, then try and fail with K₅ and K₃,₃. Apply Euler's formula to derive the edge bound and use it to prove specific graphs are non-planar. Connect to map coloring (planar graphs model maps) as a natural application of the four-color theorem.

## Common Misconceptions
- Concluding a graph is non-planar because one particular drawing has crossings — what matters is whether any crossing-free drawing exists.
- Forgetting to count the outer unbounded region as a face when applying Euler's formula.

## Explainer

A graph is **planar** if it can be drawn in the plane with no two edges crossing. Notice the careful phrasing: it is not that a specific drawing is crossing-free, but that *some* drawing exists with no crossings. K₄ (four vertices, every pair connected) looks tangled when drawn naively, but it can be redrawn with one vertex inside a triangle — no crossings. That's enough to make it planar. The question is always existential: does any valid embedding exist?

When a planar graph *is* drawn without crossings, its edges divide the plane into regions called **faces**. Count the regions, including the unbounded outer region that surrounds the whole drawing. For any connected planar graph, these quantities satisfy a remarkable identity discovered by Euler: **V − E + F = 2**, where V is vertices, E is edges, and F is faces. Try it on K₄ drawn as a triangle with an interior point: V = 4, E = 6, F = 4 (three inner faces plus the outer). Indeed 4 − 6 + 4 = 2. This identity is not just a curiosity — it is a powerful counting tool.

The most useful application of Euler's formula is proving non-planarity without finding a specific bad drawing. In any simple planar graph, every face is bounded by at least 3 edges, and every edge borders at most 2 faces, giving 3F ≤ 2E. Substituting F = 2 − V + E from Euler's formula yields **E ≤ 3V − 6**. For K₅: V = 5, so 3V − 6 = 9, but E = 10. Since 10 > 9, K₅ cannot be planar. This one inequality, derived from Euler's formula, immediately disqualifies K₅ without any case analysis on drawings.

**Kuratowski's theorem** completes the picture by giving an exact characterization: a graph is planar if and only if it contains no *subdivision* of K₅ or K₃,₃ as a subgraph (a subdivision replaces edges with paths through new vertices). This means non-planarity always reduces to one of these two "obstructions." Your prerequisite on graph connectivity matters here because Euler's formula applies to connected planar graphs; for disconnected graphs the formula generalizes to V − E + F = 1 + C where C is the number of connected components. The four-color theorem — that every planar map can be colored with four colors — is one of the deepest downstream applications of planarity theory.
