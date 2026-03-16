---
id: graph-coloring
title: Graph Coloring and the Chromatic Number
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-connectivity
  type: hard
- id: planar-graphs
  type: soft
- id: bipartite-graphs
  type: soft
- id: pigeonhole-principle
  type: soft
tags:
- graph-coloring
- chromatic-number
- four-color-theorem
- brooks-theorem
stage: formal-systems
status: validated
---

# Graph Coloring and the Chromatic Number

## Core Idea
A proper k-coloring assigns one of k colors to each vertex so that no two adjacent vertices share a color. The chromatic number χ(G) is the minimum k for which a proper coloring exists. Bipartite graphs have χ = 2; complete graphs Kₙ require n colors. The greedy coloring algorithm gives an upper bound of Δ(G)+1, and Brook's theorem tightens this to χ(G) ≤ Δ(G) except for complete graphs and odd cycles. The celebrated four-color theorem states every planar graph satisfies χ ≤ 4.

## How It's Best Learned
Color progressively complex graphs by hand — trees, even cycles, odd cycles, wheel graphs — and determine the chromatic number by finding both a valid coloring (upper bound) and an argument why fewer colors fail (lower bound). Scheduling problems (exam timetabling, register allocation) make the applications tangible.

## Common Misconceptions
- Thinking the chromatic number always equals the size of the largest clique — the clique number is a lower bound but not always achieved (see the Mycielski construction).
- Confusing vertex coloring (chromatic number) with edge coloring (chromatic index), which is a separate problem.

## Questions

```yaml
- question: "What is the chromatic number of the cycle graph C₅ (a pentagon — 5 vertices in a single cycle)?"
  type: multiple-choice
  options: ["2", "3", "4", "5"]
  answer: 1
  explanation: "Odd cycles require 3 colors. Try 2-coloring C₅: alternate colors around the cycle, but the 5th vertex is adjacent to both the 4th vertex and the 1st, which have different colors — yet both colors are already used by its neighbors. A 3-coloring works: assign color 1, 2, 1, 2, 3 around the pentagon. Even cycles (C₄, C₆, …) are bipartite and need only 2 colors."

- question: "The chromatic number of any graph equals the size of its largest clique."
  type: true-false
  answer: false
  explanation: "The clique number ω(G) is always a lower bound for χ(G) — a clique of size k requires k colors — but it is not always tight. The Mycielski construction produces graphs that are triangle-free (ω = 2) yet have arbitrarily large chromatic number. This shows that the global coloring structure of a graph can force many colors even without any large complete subgraph."

- question: "To prove that χ(G) = k for some specific graph G, what two things must you demonstrate?"
  type: short-answer
  answer: "You must show (1) that a valid k-coloring exists, establishing χ(G) ≤ k, and (2) that no valid (k−1)-coloring exists, establishing χ(G) ≥ k. Together, the upper and lower bounds pin down χ(G) = k exactly."
  explanation: "This two-part structure — an explicit construction for the upper bound and an impossibility argument for the lower bound — is the standard proof template for chromatic number. The lower bound often uses a large clique, an odd cycle, or a counting/pigeonhole argument."
```

## Explainer

Graph coloring asks for the minimum number of colors needed to paint the vertices of a graph so that no two adjacent vertices share a color. That minimum is the chromatic number χ(G). The problem appears in disguise everywhere: scheduling exams so no student has two at once, assigning radio frequencies so nearby towers don't interfere, and allocating registers in a compiler so no two live variables share the same register — all reduce to graph coloring.

To determine χ(G) precisely, you need both an upper bound and a lower bound. The upper bound comes from exhibiting an explicit valid coloring: "here is a k-coloring, so χ(G) ≤ k." The lower bound comes from an argument that fewer colors cannot work: "any (k−1)-coloring fails because…" The most common lower bound argument is finding a clique — a set of mutually adjacent vertices — of size k, since every pair in the clique must receive a different color. However, the clique number ω(G) is only a lower bound. There exist graphs where χ(G) is much larger than ω(G); the Mycielski construction builds triangle-free graphs (ω = 2) that require arbitrarily many colors. Do not assume χ = ω without proof.

Special structures give clean answers. Bipartite graphs — those whose vertices split into two groups with all edges going between groups — have χ = 2: just assign one color to each side. An equivalent characterization: bipartite graphs have no odd cycles. Odd cycles themselves need exactly 3 colors (try 2-coloring a pentagon and you will get stuck at the last vertex). Complete graphs Kₙ need exactly n colors, one per vertex.

Two useful theorems bound χ from above. The greedy algorithm — color each vertex with the smallest color not used by any of its already-colored neighbors — uses at most Δ(G) + 1 colors, where Δ(G) is the maximum degree. Brook's theorem sharpens this: χ(G) ≤ Δ(G) for every graph except complete graphs and odd cycles, which achieve χ = Δ + 1. These theorems guarantee that coloring is rarely as expensive as the worst case suggests.

The four-color theorem — every planar graph satisfies χ ≤ 4 — is one of the most famous results in mathematics. It was conjectured in 1852 and not proved until 1976, when Appel and Haken verified it by reducing the problem to checking roughly 1,500 configurations by computer. It directly implies that any flat map, with countries as vertices and shared borders as edges, can be colored with four colors so no neighboring countries share a color.
