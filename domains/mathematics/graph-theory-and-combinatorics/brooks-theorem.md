---
id: brooks-theorem
title: Brooks' Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: chromatic-number-bounds
  type: hard
tags:
- graph-theory
- coloring
stage: formal-systems
status: draft
---

# Brooks' Theorem

## Core Idea
Brooks' Theorem states that any connected graph with maximum degree Δ has chromatic number at most Δ, except for complete graphs and odd cycles (which need Δ+1). This result elegantly shows that maximum degree is nearly always sufficient for coloring, vastly improving the trivial Δ+1 bound.

## How It's Best Learned
First examine the exceptions (Kₙ and odd cycles) to understand why they require Δ+1 colors. Then trace through greedy colorings on larger graphs to see how the proof's degree arguments work.

## Common Misconceptions
Brooks' theorem says AT MOST Δ colors suffice (not exactly Δ), and the exceptions are specific. Cliques Kₙ need n colors (which equals degree n-1 plus one).

## Questions

```yaml
- question: "You have a connected graph G with maximum degree Δ = 5 that is neither a complete graph nor an odd cycle. What does Brooks' Theorem guarantee?"
  type: multiple-choice
  options:
    - "The graph requires exactly 5 colors — no more, no less"
    - "The graph can be properly colored with at most 5 colors"
    - "The graph requires at most 6 colors, because the trivial greedy bound always applies"
    - "The graph can always be 4-colored because Δ is only an upper bound"
  answer: 1
  explanation: "Brooks' Theorem gives an upper bound of Δ for all connected graphs except complete graphs and odd cycles. For this graph (Δ = 5, neither exception), at most 5 colors suffice. Option A is wrong — 'at most' does not mean 'exactly'; χ(G) might be 3 or 4. Option C applies the weaker trivial bound (Δ+1), which Brooks supersedes. Option D incorrectly extrapolates 'upper bound' to mean 'can always go lower.'"

- question: "Which of the following graphs requires Δ+1 colors according to Brooks' Theorem?"
  type: multiple-choice
  options:
    - "A connected 4-regular graph that is not a complete graph and not an odd cycle"
    - "The cycle graph C₇ (seven vertices arranged in a ring)"
    - "A 3-regular bipartite graph"
    - "A 5-regular graph that contains a triangle"
  answer: 1
  explanation: "C₇ is an odd cycle with maximum degree Δ = 2. By Brooks' Theorem, odd cycles are one of only two exception families requiring Δ+1 = 3 colors. You can 2-color any even cycle (alternating colors around the ring work out), but odd cycles force a color conflict at the wrap-around. Options A, C, and D all describe graphs that are not complete graphs or odd cycles, so they satisfy χ ≤ Δ."

- question: "Brooks' Theorem says every graph can be properly colored with exactly Δ colors."
  type: true-false
  answer: false
  explanation: "The theorem gives an upper bound: χ(G) ≤ Δ for graphs that are not complete graphs or odd cycles. 'At most Δ' does not mean 'exactly Δ.' A bipartite graph with Δ = 5 only requires 2 colors; a tree with Δ = 10 only requires 2 colors. Brooks' Theorem rules out needing more than Δ colors (outside the two exception families) but says nothing about whether fewer might suffice."

- question: "The complete graph K₅ has chromatic number 5, which equals Δ+1 for that graph."
  type: true-false
  answer: true
  explanation: "K₅ has 5 vertices, each adjacent to all other 4, so Δ = 4. Since every pair of vertices is connected, each vertex needs a distinct color, giving χ(K₅) = 5 = Δ+1. This makes Kₙ one of the two families that cannot be colored with Δ colors — which is exactly why Brooks' Theorem carves them out as exceptions. The theorem's upper bound of Δ is tight: complete graphs prove you cannot improve it further."

- question: "Why do odd cycles require Δ+1 colors, while even cycles only need Δ colors?"
  type: short-answer
  answer: "An odd cycle has Δ = 2 but requires 3 colors. When you try to 2-color by alternating colors around the ring, the last vertex before closing the loop is adjacent to the first vertex — and because the cycle has an odd number of vertices, those two vertices end up with the same color, creating a conflict. Even cycles avoid this: with an even number of vertices, the alternating pattern closes perfectly and the first and last vertices have different colors, so 2 colors suffice."
  explanation: "This is the cleanest example of why Brooks' Theorem needs exceptions. Odd cycles are sparse (Δ = 2) yet require an extra color — purely due to parity, not density. The proof of Brooks' Theorem works by finding orderings that let greedy coloring succeed within Δ colors, but no such ordering exists for odd cycles. Even cycles (also Δ = 2) are bipartite, which is why 2 colors always work for them."
```

## Explainer

From chromatic number bounds, you know the trivial upper bound: any graph with maximum degree Δ can be colored with Δ+1 colors, because a greedy algorithm can always find an available color for each vertex (it has at most Δ neighbors, so at least one of Δ+1 colors is unused). **Brooks' Theorem** tightens this bound dramatically, showing that Δ colors almost always suffice — the "+1" is only ever necessary for two specific families of graphs.

The two exceptions are the ones you'd predict from extremes. A **complete graph** Kₙ has every pair of vertices connected, so every vertex is adjacent to every other; you need a different color for each vertex, giving χ(Kₙ) = n = Δ+1. An **odd cycle** C_{2k+1} needs 3 colors despite having maximum degree 2 — you can 2-color any even cycle (alternate colors around the ring), but an odd cycle forces a third color when you wrap around and the start and end conflict. For every other connected graph, Δ colors are enough.

The proof idea is constructive. If the graph is not Kₙ or an odd cycle, you can find a clever vertex ordering that lets greedy coloring succeed within Δ colors. The key structural observation: in any graph that's neither a complete graph nor an odd cycle, there exists a vertex ordering where, when you color greedily in that order, every vertex has at most Δ−1 already-colored neighbors when you reach it — so one of the Δ colors is always free. The proof constructs this ordering using the structure of spanning trees rooted at a vertex of degree less than Δ (which must exist if the graph isn't Kₙ).

In practice, Brooks' Theorem tells you the **worst-case coloring cost** for most graphs: if you see a graph with Δ = 4, you can guarantee a proper 4-coloring exists unless it's K₅ or an odd cycle. This is especially useful in applications like register allocation (where a register-interference graph must be colored), scheduling (time slots = colors, conflicts = edges), and frequency assignment. The bound is tight — many Δ-regular graphs require exactly Δ colors — but it's never tighter than that outside the two exception families.
