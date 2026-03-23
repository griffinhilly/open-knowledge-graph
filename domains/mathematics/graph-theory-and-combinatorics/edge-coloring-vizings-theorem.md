---
id: edge-coloring-vizings-theorem
title: Edge Coloring and Vizing's Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: chromatic-polynomial
  type: soft
builds-toward:
- list-coloring
tags:
- edge-coloring
- vizings-theorem
- chromatic-index
stage: formal-systems
status: validated
---

# Edge Coloring and Vizing's Theorem

## Core Idea
The chromatic index χ'(G) is the minimum colors needed for a proper edge coloring. Vizing's theorem states χ'(G) ∈ {Δ(G), Δ(G)+1}, classifying graphs as Class 1 or Class 2. Determining which class a graph belongs to is NP-complete in general.

## How It's Best Learned
Compute edge colorings for small graphs and verify that the chromatic index is either Δ or Δ+1. Try to find patterns distinguishing Class 1 from Class 2 graphs.

## Common Misconceptions
- Thinking edge coloring relates to vertex coloring in a straightforward way; the two are different optimization problems.
- Assuming all graphs are easily classifiable as Class 1 or Class 2 (classification is hard in general).

## Questions

```yaml
- question: "A graph G has maximum degree Δ(G) = 7. According to Vizing's theorem, what are the only possible values of the chromatic index χ'(G)?"
  type: multiple-choice
  options:
    - "Any integer from 1 to 7"
    - "Exactly 7 or exactly 8"
    - "Exactly 7 (since bipartite graphs always achieve the lower bound)"
    - "At most 14 (since the theorem guarantees χ'(G) ≤ 2Δ)"
  answer: 1
  explanation: "Vizing's theorem states that for any simple graph, χ'(G) ∈ {Δ(G), Δ(G)+1}. With Δ = 7, the chromatic index must be exactly 7 (Class 1) or exactly 8 (Class 2) — no other values are possible. This tight two-outcome result is the remarkable content of the theorem: despite no obvious reason why it should be so constrained, the chromatic index never exceeds the obvious lower bound by more than 1."

- question: "An employee scheduling problem models workers as vertices and required meetings between pairs of workers as edges. Each meeting needs a time slot, and two meetings sharing a worker cannot occupy the same slot. After modelling this as a graph with maximum degree Δ = 5, a manager claims the schedule can always be completed in 5 or 6 time slots. What justifies this claim?"
  type: multiple-choice
  options:
    - "König's theorem guarantees that scheduling graphs are always bipartite and therefore require only Δ slots"
    - "Vizing's theorem guarantees χ'(G) ∈ {Δ, Δ+1} for any simple graph, so the minimum slots needed is either 5 or 6"
    - "The chromatic polynomial shows that any graph with Δ = 5 requires exactly 5 colors for a proper edge coloring"
    - "Vertex coloring with 5 colors implies edge coloring with 5 colors by a standard reduction"
  answer: 1
  explanation: "Vizing's theorem converts the unbounded question 'how many time slots?' into the binary question 'are Δ slots enough, or do we need Δ+1?' For any scheduling graph with Δ = 5, we are guaranteed that 6 slots always suffice and 5 may suffice. Option A is true for bipartite graphs specifically (König's theorem) but cannot be asserted for general graphs. Option D reflects the common misconception that vertex and edge coloring are closely related — they are different problems with different bounds."

- question: "Because Vizing's theorem constrains the chromatic index to only two possible values, determining which value applies to a given graph is computationally tractable in polynomial time."
  type: true-false
  answer: false
  explanation: "This is the central surprise: despite the output being binary (Class 1 or Class 2), deciding which class a graph belongs to is NP-complete in general. A narrow answer space does not imply computational ease. This is a recurring theme in graph theory: the difficulty of a problem is not determined by the size of its output space. Vizing's theorem is valuable because it bounds the answer, not because it makes finding the answer easy."

- question: "All bipartite graphs are Class 1, meaning their chromatic index equals their maximum degree Δ."
  type: true-false
  answer: true
  explanation: "This is König's edge coloring theorem: for bipartite graphs, χ'(G) = Δ(G). Bipartite structure prevents the 'bottlenecks' that force Class 2 graphs to need an extra color. This is why scheduling problems modeled as bipartite graphs (e.g., tasks on one side, machines on the other) can always be solved optimally with Δ slots. Non-bipartite graphs — including odd cycles, complete graphs Kₙ for odd n, and the Petersen graph — may be Class 2."

- question: "Why is it surprising that determining a graph's class (Class 1 vs. Class 2) is NP-complete, given that the chromatic index can only be one of two values?"
  type: short-answer
  answer: "Intuitively, a problem with only two possible outputs should be easy — it seems like a yes/no question. But NP-completeness captures the difficulty of verifying or constructing the coloring that witnesses the answer, not just the size of the answer space. Even knowing χ'(G) ∈ {Δ, Δ+1}, we have no known polynomial-time algorithm for determining which value applies, because the structural properties that force Class 2 membership (like the presence of certain subgraph configurations) are globally complex to detect. This contrasts with, say, checking bipartiteness (easy), which immediately guarantees Class 1."
  explanation: "This observation also highlights the value of special cases: for bipartite graphs (König's theorem) and regular graphs (Vizing-type results), classification is tractable. The NP-hardness applies in general, which means practical edge-coloring algorithms often rely on graph-specific structure. Vizing's theorem is still useful as an upper bound guarantee even without knowing the exact class — you can always build a valid coloring with Δ+1 colors in polynomial time."
```

## Explainer

**Edge coloring** assigns colors to the edges of a graph so that no two edges sharing a vertex get the same color. This models scheduling problems: if vertices are jobs and edges are time slots during which two jobs share a resource, an edge coloring finds a valid schedule. The minimum number of colors needed is called the **chromatic index**, written χ'(G) (to distinguish it from the vertex chromatic number χ(G) from your work on the chromatic polynomial).

What is the obvious lower bound for χ'(G)? Every edge incident to a high-degree vertex must get a distinct color, so you need at least Δ(G) colors, where Δ(G) is the **maximum degree** — the maximum number of edges meeting at any single vertex. The remarkable fact that Vizing proved in 1964 is that you never need more than Δ(G) + 1 colors: χ'(G) ∈ {Δ(G), Δ(G)+1}. This is a tight two-outcome theorem — graphs are partitioned into **Class 1** (chromatic index exactly Δ) and **Class 2** (chromatic index Δ + 1). Every graph lands in one of only two possibilities, with no room in between.

Bipartite graphs are always Class 1 — König's theorem guarantees this. Complete graphs Kₙ illustrate the two cases: K₄ has Δ = 3 and χ' = 3 (Class 1), while K₃ has Δ = 2 and χ' = 3 (Class 2). The Petersen graph, a well-known cubic graph with Δ = 3, is Class 2 with χ' = 4 and resists many simpler edge colorings. These examples suggest that Class 2 graphs are somehow "more constrained" — they have structural bottlenecks preventing the optimal Δ-coloring — but characterizing exactly which graphs are Class 2 has resisted a simple closed-form answer.

The difficulty is computational: deciding whether a graph is Class 1 is NP-complete in general, even though the answer is constrained to just two values. This is a recurring theme in graph theory — problems that seem to have limited output space are often computationally hard. The contrast with vertex coloring is instructive: vertex coloring has no tight universal bound like Vizing's theorem, while edge coloring does, yet edge coloring is just as computationally hard. Vizing's theorem is valuable precisely because it converts an unbounded question ("how many colors?") into a yes/no classification question ("are Δ colors enough?"), which in turn focuses research on identifying structural properties that determine class membership.
