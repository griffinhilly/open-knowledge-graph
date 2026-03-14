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
