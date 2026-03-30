---
id: vizings-theorem
title: Vizing's Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: edge-coloring
  type: hard
- id: edge-coloring-vizings-theorem
  type: soft
- id: mengers-theorem
  type: soft
- id: hamiltonian-cycles-dirac-ore
  type: soft
tags:
- graph-theory
- edge-coloring
stage: advanced
status: validated
---
# Vizing's Theorem

## Core Idea
Vizing's Theorem states that the chromatic index of any simple graph is either Δ or Δ+1, where Δ is maximum degree. Graphs achieving Δ are Class 1; those needing Δ+1 are Class 2. Despite this tight characterization, determining class membership is NP-hard in general.

## How It's Best Learned
Examine Class 1 graphs (bipartite graphs are always Class 1) and Class 2 graphs (odd cycles, complete odd cliques) to see patterns in edge structure.

## Common Misconceptions
Not all graphs are Class 1; many require Δ+1 colors despite the tight bound. Determining class membership is computationally hard.

## Questions

```yaml
- question: "A network engineer is scheduling data transfers between servers. Each server handles at most Δ = 8 simultaneous connections. She doesn't yet know whether the network graph is Class 1 or Class 2. What does Vizing's theorem guarantee?"
  type: multiple-choice
  options:
    - "She will need exactly 8 time slots"
    - "She will need exactly 9 time slots because most real-world graphs are Class 2"
    - "She will need at most 9 time slots — the schedule can always be completed in Δ+1 = 9 slots or fewer"
    - "Vizing's theorem does not apply to network scheduling problems"
  answer: 2
  explanation: "Vizing's theorem guarantees χ'(G) ≤ Δ+1 for any simple graph. Even without knowing whether the specific graph is Class 1 (needing 8 slots) or Class 2 (needing 9 slots), the engineer can guarantee the worst case requires at most 9 time slots. This upper bound is immediately useful for resource provisioning even before class membership is determined."

- question: "Which of the following is always a Class 1 graph, requiring exactly Δ colors for edge coloring?"
  type: multiple-choice
  options:
    - "Any graph with an odd number of vertices"
    - "Complete graphs on an odd number of vertices (K₂ₙ₊₁)"
    - "Any bipartite graph"
    - "Odd cycles"
  answer: 2
  explanation: "Bipartite graphs are always Class 1 — this follows from König's edge-coloring theorem, which proves Δ colors always suffice for bipartite graphs. Odd cycles are Class 2: a 5-cycle has Δ = 2 but needs 3 colors since alternating colors on an odd-length cycle forces a conflict. Complete graphs on an odd number of vertices (K₂ₙ₊₁) are also Class 2."

- question: "Vizing's theorem tells you exactly how many colors any specific graph needs for an optimal edge coloring."
  type: true-false
  answer: false
  explanation: "Vizing's theorem narrows the chromatic index to exactly two possible values (Δ or Δ+1), but does not determine which value applies to a given graph. Determining class membership — deciding whether a specific graph is Class 1 or Class 2 — is NP-complete in general. Vizing's theorem gives a two-value bound, not an exact computation."

- question: "Both bipartite graphs and complete graphs on an even number of vertices are Class 1 under Vizing's classification."
  type: true-false
  answer: true
  explanation: "Bipartite graphs are always Class 1 by König's theorem. Complete graphs K₂ₙ on an even number of vertices are also Class 1 — their edges decompose into exactly Δ = 2n−1 perfect matchings, yielding a Δ-edge-coloring. This contrasts with K₂ₙ₊₁ (odd vertex count), which is Class 2."

- question: "Vizing's theorem pins the chromatic index to one of two values. Why is this useful even though determining which value applies is NP-complete?"
  type: short-answer
  answer: "The theorem provides a guaranteed upper bound: no matter the graph, χ'(G) ≤ Δ+1. In any scheduling or resource-assignment problem modeled as edge coloring, you know the worst case requires at most Δ+1 resources, even before determining whether Δ suffices. This upper-bound guarantee is immediately actionable for worst-case planning, even if minimizing to Δ when possible requires expensive computation."
  explanation: "Knowing the answer lies in {Δ, Δ+1} is far more useful than knowing only χ'(G) ≥ Δ — it transforms a potentially unbounded search into a binary question, even if that binary question is itself hard to resolve."
```

## Explainer

From edge coloring, you know that the **chromatic index** χ'(G) is the minimum number of colors needed to color the edges of G so that no two edges sharing a vertex receive the same color. The trivial lower bound is immediate: if a vertex has degree Δ (the maximum degree in the graph), all Δ edges at that vertex must receive different colors, so χ'(G) ≥ Δ. The question is how much higher than Δ we might need to go.

**Vizing's Theorem** gives a striking answer: never more than Δ + 1. For any simple graph with maximum degree Δ, the chromatic index is either exactly Δ or exactly Δ + 1 — nothing else is possible. This pins χ'(G) to one of just two values, a remarkably tight classification given that Δ alone tells you almost nothing about the graph's global structure. Graphs achieving χ'(G) = Δ are called **Class 1**; those requiring χ'(G) = Δ + 1 are called **Class 2**. Every simple graph falls into exactly one class.

The Class 1/Class 2 distinction has satisfying examples on both sides. **Bipartite graphs are always Class 1** — this follows from König's edge-coloring theorem, which shows that Δ colors always suffice for bipartite graphs. Complete graphs on an even number of vertices (K_{2n}) are also Class 1, since their edges decompose into exactly Δ perfect matchings. On the Class 2 side, **odd cycles** need 3 colors for maximum degree 2, since the odd cycle forces color conflicts. Complete graphs on an odd number of vertices (K_{2n+1}) are also Class 2, because the odd vertex count prevents a clean Δ-coloring.

The frustrating twist is that despite knowing χ'(G) is Δ or Δ+1, determining which one applies is computationally hard — deciding whether a graph is Class 1 is **NP-complete** in general. This mirrors the situation with Hamiltonian cycles: the theorem gives a beautifully precise characterization, but computing which case applies is intractable in the worst case. In scheduling applications, where edges represent tasks sharing a resource and colors represent time slots, Vizing's theorem provides the key practical guarantee: you will never need more than Δ + 1 time slots, regardless of graph structure. That upper bound is what makes the theorem immediately useful even before you know whether your specific graph is Class 1 or Class 2.
