---
id: euler-circuits-and-paths
title: Eulerian Circuits and Paths
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-connectivity
  type: hard
- id: graph-theory-intro
  type: hard
builds-toward:
- hamiltonian-circuits
tags:
- euler-circuit
- euler-path
- eulerian-graph
- konigsberg-bridges
stage: formal-systems
status: validated
---

# Eulerian Circuits and Paths

## Core Idea
An Eulerian circuit is a closed walk traversing every edge exactly once; an Eulerian path is an open walk doing the same. Euler's theorem (1736) states: a connected graph has an Eulerian circuit if and only if every vertex has even degree, and an Eulerian path (but not circuit) if and only if exactly two vertices have odd degree. The Königsberg bridge problem — can one cross all seven bridges without repeating any? — was Euler's original motivation and arguably the founding problem of graph theory.

## How It's Best Learned
Attempt Eulerian circuits on small graphs by hand before seeing the theorem. Verify Euler's condition on several examples. Connect to practical route-planning problems (mail delivery, snow plowing) where the goal is to traverse all edges with minimum repetition.

## Common Misconceptions
- Confusing Eulerian circuits (edges traversed once) with Hamiltonian circuits (vertices visited once) — these are fundamentally different problems with very different theories.
- Thinking even degree is sufficient without the connectivity requirement.

## Explainer

Euler's theorem is one of the most elegant results in graph theory: a complete solution to a natural traversal problem, given by a single, easy-to-check condition. You've studied graph connectivity and the basic vocabulary of graphs. Now the question is: can you plan a walk that uses every edge exactly once? Think of the graph as a map where edges are streets and vertices are intersections — you want a route that covers every street exactly once, ideally returning to where you started.

The key insight comes from thinking locally about each vertex. Every time a walk passes through a vertex (entering, then leaving), it consumes two edges — one in, one out. For a **circuit** (a closed walk that returns to its starting vertex) to traverse every edge exactly once, every vertex must balance its arrivals and departures perfectly. This forces every vertex to have **even degree** — an equal number of edges on each side of any passage. If any vertex has odd degree, it cannot be perfectly balanced, meaning the walk must either start or end there, making a closed circuit impossible.

Euler's theorem converts this local observation into a complete characterization. For a connected graph: it has an **Eulerian circuit** if and only if every vertex has even degree; it has an **Eulerian path** (open walk through every edge once) if and only if exactly two vertices have odd degree — those two are the start and end of the path. Connectivity is also required: you cannot traverse edges in a component you can never reach. The Königsberg bridge problem, which motivated Euler's 1736 paper, had four land masses each with an odd number of bridge connections — so no Eulerian path was possible, proving the famous walk impossible.

One distinction is critical to keep sharp: **Eulerian** circuits cover every **edge** once, while **Hamiltonian** circuits visit every **vertex** once. These problems sound related but are fundamentally different in difficulty. Eulerian circuit existence is solvable in linear time — just check that all degrees are even and the graph is connected. Hamiltonian circuit existence is NP-complete, with no known efficient algorithm. The degree condition works for Euler because edges are "used up" as you traverse them, allowing a clean local argument to close the analysis. No comparable local condition exists for Hamilton, which is why the two problems, despite their surface similarity, have completely different theories.
