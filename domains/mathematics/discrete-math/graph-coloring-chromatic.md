---
id: graph-coloring-chromatic
title: Graph Coloring and Chromatic Number
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-fundamentals
  type: soft
builds-toward:
- chromatic-polynomial-computation
tags:
- graph-theory
- coloring
stage: formal-systems
status: draft
---

# Graph Coloring and Chromatic Number

## Core Idea
A proper vertex coloring assigns colors to vertices such that adjacent vertices receive different colors. The chromatic number χ(G) is the minimum number of colors needed. Graph coloring has applications in scheduling, register allocation, and map coloring.

## Explainer

From graph theory fundamentals, you know that adjacency captures "connected by an edge." Graph coloring adds a constraint: adjacent vertices must receive different **colors** (which in practice represent any distinguishable labels). A **proper coloring** is any assignment of colors to vertices that satisfies this constraint. The question is: what is the minimum number of colors required?

That minimum is the **chromatic number** χ(G) (chi of G). For a path or tree, two colors always suffice — you alternate colors as you traverse. For a triangle (a 3-cycle), you need at least three colors because all three vertices are mutually adjacent. For a complete graph Kₙ, where every vertex touches every other, you need exactly n colors. Recognizing the structure of a graph gives you bounds on its chromatic number before you even start coloring.

The **greedy coloring** algorithm provides an upper bound: process vertices one by one, assigning the smallest color not already used by a neighbor. Greedy does not always find the optimal coloring, but it uses at most Δ(G)+1 colors, where Δ(G) is the maximum degree. A graph's **clique number** ω(G) — the size of its largest complete subgraph — gives a lower bound: you need at least ω(G) colors because that clique alone forces them all. So ω(G) ≤ χ(G) ≤ Δ(G)+1, though χ can be much larger than ω in general graphs.

The applications make the abstraction concrete. In **scheduling**, vertices are tasks and edges connect tasks that must not run simultaneously (they share a resource); coloring with k colors gives a schedule using k time slots. In **register allocation** in compilers, variables that are "live" at the same time cannot share a register; the register conflict graph's chromatic number is the minimum number of registers needed. In map coloring, regions sharing a border cannot share a color — the celebrated Four Color Theorem proves that planar graphs (maps drawn without edge crossings) always have χ(G) ≤ 4.
