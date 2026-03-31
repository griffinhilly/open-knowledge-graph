---
id: graph-coloring-chromatic
title: Graph Coloring and Chromatic Number
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: soft
builds-toward:
- chromatic-polynomial-computation
tags:
- graph-theory
- coloring
stage: formal-systems
status: validated
---

# Graph Coloring and Chromatic Number

## Core Idea
A proper vertex coloring assigns colors to vertices such that adjacent vertices receive different colors. The chromatic number χ(G) is the minimum number of colors needed. Graph coloring has applications in scheduling, register allocation, and map coloring.

## Questions

```yaml
- question: "Graph G contains a complete subgraph K₄ (four mutually adjacent vertices). What can you immediately conclude about the chromatic number χ(G)?"
  type: multiple-choice
  options:
    - "χ(G) = 4, because K₄ forces exactly four colors"
    - "χ(G) ≥ 4, because the K₄ subgraph alone requires four distinct colors"
    - "χ(G) ≤ 4, because planar graphs need at most four colors"
    - "χ(G) = Δ(G) + 1, because the maximum degree determines the chromatic number"
  answer: 1
  explanation: "The clique number ω(G) provides a lower bound: χ(G) ≥ ω(G). Since K₄ is a clique of size 4, all four vertices are mutually adjacent and must each receive a distinct color — so at least 4 colors are needed. But χ(G) could be larger than 4 if the rest of the graph forces more colors. Option A is too strong: the clique gives a lower bound, not an exact value. The Four Color Theorem (option C) applies to planar graphs, but G may not be planar."

- question: "Five tasks (A, B, C, D, E) must be scheduled into time slots. Conflicts exist between A–B, B–C, C–D, D–E, and A–E (forming a 5-cycle, C₅). What is the minimum number of time slots needed?"
  type: multiple-choice
  options:
    - "2 — since no three tasks all conflict with each other"
    - "3 — a 5-cycle contains no triangle but cannot be 2-colored"
    - "5 — each task needs its own slot because the cycle has no independent set"
    - "4 — the maximum degree is 2, so Δ + 1 = 3 is insufficient"
  answer: 1
  explanation: "A 5-cycle (odd cycle) cannot be properly 2-colored: starting with color 1 on A, alternating forces color 1 on both D and E, but A and E conflict. Three colors suffice: color A=1, B=2, C=1, D=2, E=3. The largest clique in C₅ has size 2 (any edge), so ω = 2, but χ = 3 — demonstrating that the chromatic number can exceed the clique number."

- question: "The greedy coloring algorithm usually finds the minimum number of colors needed to properly color a graph."
  type: true-false
  answer: false
  explanation: "Greedy coloring is not optimal in general. It produces a valid proper coloring using at most Δ(G) + 1 colors, but the result depends on the order vertices are processed. For some orderings it may use more colors than χ(G). For example, a bipartite graph has χ = 2, but a greedy coloring in a bad vertex order could use more than 2. Greedy provides an upper bound on χ(G), not the exact value."

- question: "The chromatic number χ(G) of a graph is generally equal to the size of its largest clique ω(G)."
  type: true-false
  answer: false
  explanation: "This is false in general. The clique number ω(G) gives a lower bound — χ(G) ≥ ω(G) — but χ can be strictly larger. A famous example is the Mycielski graphs: they have ω = 2 (no triangle) but arbitrarily high chromatic number. For odd cycles Cₙ (n ≥ 5), ω = 2 but χ = 3. The gap between ω and χ reveals that graph coloring is not reducible to clique detection."

- question: "What does the chromatic number χ(G) measure, and why does the clique number ω(G) provide a lower bound for it?"
  type: short-answer
  answer: "The chromatic number χ(G) is the minimum number of colors needed to assign colors to all vertices so that no two adjacent vertices share a color. The clique number ω(G) is the size of the largest complete subgraph (clique). In any clique, every vertex is adjacent to every other, so all vertices in the clique must receive distinct colors. Therefore the clique alone forces at least ω(G) colors to be used, making ω(G) a lower bound for χ(G)."
  explanation: "The lower bound argument is tight and clean: a clique of size k is a subgraph that by itself requires k colors, so χ(G) ≥ k for any k-clique G contains. The upper bound comes from greedy: χ(G) ≤ Δ(G) + 1. The actual chromatic number lies somewhere in the range [ω(G), Δ(G)+1], and determining the exact value is NP-hard in general."
```

## Explainer

From graph theory fundamentals, you know that adjacency captures "connected by an edge." Graph coloring adds a constraint: adjacent vertices must receive different **colors** (which in practice represent any distinguishable labels). A **proper coloring** is any assignment of colors to vertices that satisfies this constraint. The question is: what is the minimum number of colors required?

That minimum is the **chromatic number** χ(G) (chi of G). For a path or tree, two colors always suffice — you alternate colors as you traverse. For a triangle (a 3-cycle), you need at least three colors because all three vertices are mutually adjacent. For a complete graph Kₙ, where every vertex touches every other, you need exactly n colors. Recognizing the structure of a graph gives you bounds on its chromatic number before you even start coloring.

The **greedy coloring** algorithm provides an upper bound: process vertices one by one, assigning the smallest color not already used by a neighbor. Greedy does not always find the optimal coloring, but it uses at most Δ(G)+1 colors, where Δ(G) is the maximum degree. A graph's **clique number** ω(G) — the size of its largest complete subgraph — gives a lower bound: you need at least ω(G) colors because that clique alone forces them all. So ω(G) ≤ χ(G) ≤ Δ(G)+1, though χ can be much larger than ω in general graphs.

The applications make the abstraction concrete. In **scheduling**, vertices are tasks and edges connect tasks that must not run simultaneously (they share a resource); coloring with k colors gives a schedule using k time slots. In **register allocation** in compilers, variables that are "live" at the same time cannot share a register; the register conflict graph's chromatic number is the minimum number of registers needed. In map coloring, regions sharing a border cannot share a color — the celebrated Four Color Theorem proves that planar graphs (maps drawn without edge crossings) always have χ(G) ≤ 4.
