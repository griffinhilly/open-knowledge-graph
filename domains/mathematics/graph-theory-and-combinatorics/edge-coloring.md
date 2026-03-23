---
id: edge-coloring
title: Edge Coloring and Chromatic Index
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-coloring
  type: hard
builds-toward:
- vizings-theorem
tags:
- graph-theory
- edge-coloring
stage: formal-systems
status: validated
---

# Edge Coloring and Chromatic Index

## Core Idea
Edge coloring assigns colors to edges so no two edges sharing a vertex have the same color. The chromatic index is the minimum colors needed. Edge coloring has practical applications in scheduling and frequency assignment, and relates closely to finding matchings.

## Questions

```yaml
- question: "A round-robin tournament has 8 teams, and each pair must play exactly once, with each team playing at most one game per round. What does the chromatic index of K₈ tell you?"
  type: multiple-choice
  options:
    - "The minimum number of games played in a single round"
    - "The total number of games in the tournament"
    - "The minimum number of rounds needed to complete the tournament"
    - "The maximum number of games any single team plays"
  answer: 2
  explanation: "Each color class in an edge coloring forms a matching — a set of games played simultaneously where no team appears twice. The chromatic index is the minimum number of matchings needed to cover all edges, which equals the minimum number of rounds. For K₈ (8 teams, n even), χ'(K₈) = 7 rounds. This scheduling interpretation is one of the primary practical applications of edge coloring."

- question: "A graph has maximum degree Δ = 5. Vizing's theorem tells you that its chromatic index χ'(G) is:"
  type: multiple-choice
  options:
    - "Exactly 5 — the chromatic index always equals the maximum degree"
    - "Either 5 or 6 — the chromatic index is always Δ or Δ+1"
    - "Between 1 and 5, depending on the specific structure"
    - "At least 5, with no tighter upper bound guaranteed"
  answer: 1
  explanation: "Vizing's theorem states that for any simple graph, χ'(G) ∈ {Δ, Δ+1}. The lower bound χ'(G) ≥ Δ is easy: all edges incident to a maximum-degree vertex need distinct colors. Vizing's remarkable result is that you never need more than Δ+1. Graphs achieving χ' = Δ are Class 1; those requiring Δ+1 are Class 2. Determining which class a given graph belongs to is NP-complete in general."

- question: "In a valid edge coloring, all edges assigned the same color form a matching — a set of edges with no two sharing a vertex."
  type: true-false
  answer: true
  explanation: "This follows directly from the edge coloring rule: no two edges sharing a vertex can have the same color. Therefore any two edges of the same color have no vertex in common — which is exactly the definition of a matching. An edge coloring is equivalent to partitioning all edges into matchings, and the chromatic index is the minimum number of matchings needed to cover every edge."

- question: "Bipartite graphs always require Δ+1 colors for edge coloring, making them Class 2 graphs."
  type: true-false
  answer: false
  explanation: "This is the opposite of the truth. Bipartite graphs are always Class 1 — they require exactly Δ colors, never Δ+1. This is König's theorem. The difficulty lies in Class 2 graphs (those requiring Δ+1), and even determining whether an arbitrary graph is Class 1 or Class 2 is NP-complete."

- question: "Why must the chromatic index of any graph be at least Δ, and what does Vizing's theorem add beyond this lower bound?"
  type: short-answer
  answer: "The lower bound χ'(G) ≥ Δ follows directly: every edge incident to a maximum-degree vertex must receive a distinct color (since they all share that vertex), requiring at least Δ colors. Vizing's theorem adds the upper bound: you never need more than Δ+1. The answer always lies in {Δ, Δ+1} — but determining which value applies to a specific graph is NP-complete."
  explanation: "The lower bound is local (one high-degree vertex forces it); the upper bound is global (Vizing's proof shows the entire graph can always be edge-colored with Δ+1 colors via a careful recoloring argument). The stunning result is how tight this is: one extra color beyond the obvious lower bound is always enough, no matter how complex the graph."
```

## Explainer

From vertex coloring, you learned to assign colors to vertices so that no two adjacent vertices share a color. **Edge coloring** flips the question: assign colors to *edges* so that no two edges sharing a *vertex* share a color. Two edges are in conflict when they meet at a vertex, and a valid edge coloring eliminates all conflicts. The minimum number of colors needed for a valid edge coloring is called the **chromatic index**, written χ'(G).

Why does this matter? Notice that all edges of the same color form a **matching** — a set of edges with no shared endpoints. So an edge coloring is exactly a partition of all edges into matchings, and the chromatic index is the fewest matchings needed to cover all edges. This connection to matchings is what makes edge coloring both deep and useful. A concrete scheduling example: suppose you have a round-robin tournament where every pair of teams must play once, and each team plays at most one game per time slot. Each time slot corresponds to a matching (games played simultaneously), and the chromatic index tells you the minimum number of slots needed. For n teams (the complete graph Kₙ), this turns out to be n−1 if n is even and n if n is odd.

A fundamental observation: every vertex has degree Δ (using Δ for the maximum degree), and all edges at that vertex need different colors, so χ'(G) ≥ Δ. You might hope χ'(G) = Δ always, but it isn't quite that clean. **Vizing's theorem** — the central result of edge coloring — says the truth is very close: χ'(G) is either Δ or Δ+1. Graphs achieving χ'(G) = Δ are called **Class 1**; those requiring Δ+1 colors are **Class 2**. Bipartite graphs are always Class 1 (a theorem of König), but determining whether an arbitrary graph is Class 1 or Class 2 is NP-complete. This makes Vizing's theorem particularly striking: the answer lies in a range of just two values, but pinning down which one is computationally hard.

The practical intuition for why one extra color can be necessary: imagine a vertex with very high degree. All its incident edges need distinct colors, saturating Δ colors just at that one vertex. If the rest of the graph's edge-matching structure doesn't align cleanly with that vertex's demands, one additional color becomes unavoidable. Vizing's proof shows this can always be resolved with at most one extra, which is a remarkably tight bound — a testament to the hidden structure in how edges and vertices interact.
