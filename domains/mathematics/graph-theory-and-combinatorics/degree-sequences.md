---
id: degree-sequences
title: Degree Sequences and Graph Realization
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: graph-theory-intro
  type: hard
- id: graph-representation
  type: hard
builds-toward:
- erdos-gallai-theorem
tags:
- graph-theory
- sequences
- degrees
stage: advanced
status: validated
---

# Degree Sequences and Graph Realization

## Core Idea
A degree sequence is the list of degrees of all vertices in a graph, typically written in non-increasing order. The realization problem asks: given a sequence of non-negative integers, does there exist a simple graph having exactly that degree sequence? Understanding which sequences are graphical is fundamental to analyzing graph structure.

## Questions

```yaml
- question: "A student claims there exists a simple graph with 4 vertices whose degree sequence is (3, 3, 1, 1). The sum is 8, which is even — so shouldn't it be realizable? Is the student correct?"
  type: multiple-choice
  options:
    - "Yes, an even sum guarantees the sequence is graphical"
    - "No, the Erdős–Gallai condition fails: the two degree-3 vertices must each connect to all three other vertices, forcing the degree-1 vertices to actually have degree 2"
    - "No, because a simple graph with 4 vertices cannot have any vertex of degree 3"
    - "Yes, the Hakimi algorithm would successfully construct such a graph"
  answer: 1
  explanation: "Even sum is necessary but not sufficient. In a 4-vertex graph, a vertex of degree 3 must connect to all three other vertices. If both high-degree vertices need degree 3, vertex A connects to B, C, D, and vertex B connects to A, C, D. This gives C and D degree 2 each — but the sequence claims they have degree 1. Contradiction: no such simple graph can exist. The Erdős–Gallai condition catches exactly this: for k=2, the sum of the top two degrees (6) exceeds what the remaining vertices can absorb (max 4)."

- question: "A student finds the sequence (2, 2, 1, 1, 1, 1) and notices its sum is even (8). They conclude that an even sum is both necessary and sufficient for a sequence to be graphical. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — an even sum is both necessary and sufficient for graphical sequences"
    - "An even sum is necessary but not sufficient; Erdős–Gallai conditions impose additional constraints that some even-sum sequences fail"
    - "The sum must be divisible by 4, not just even"
    - "Sequences with odd-degree vertices can never be graphical, regardless of the sum"
  answer: 1
  explanation: "The handshaking lemma tells us the sum of degrees must be even — a necessary condition. But it is not sufficient. For example, (3, 3, 1, 1) has even sum 8 yet is not graphical. The Erdős–Gallai theorem provides a complete characterization: a sequence is graphical if and only if it satisfies both the even-sum condition and the Erdős–Gallai inequalities for every k. The student's reasoning confuses a necessary condition with a necessary-and-sufficient one."

- question: "If the sum of a degree sequence is odd, no simple graph with that degree sequence can exist."
  type: true-false
  answer: true
  explanation: "This follows directly from the handshaking lemma: the sum of all vertex degrees equals exactly twice the number of edges (each edge contributes 1 to each of its two endpoints' degrees). Therefore the degree sum is always even. An odd-sum sequence violates this, so no simple graph — or any graph without self-loops — can realize it. This is the quickest test for ruling out a sequence: check parity first."

- question: "Two graphs with the same degree sequence should be isomorphic — they have the same structure."
  type: true-false
  answer: false
  explanation: "Many non-isomorphic graphs share the same degree sequence. For example, both the path P₄ and the star K₁,₃ have three vertices of degree 1 in related configurations, and there exist pairs of 6-vertex non-isomorphic graphs with degree sequence (2,2,2,2,2,2) — one being a 6-cycle, the other being two disjoint triangles. The degree sequence is a coarse summary of graph structure; it tells you the 'shape' of connectivity in aggregate but not which specific vertices are connected."

- question: "State the handshaking lemma and explain why it is true from first principles."
  type: short-answer
  answer: "The handshaking lemma states that the sum of all vertex degrees equals twice the number of edges. It is true because each edge {u, v} contributes exactly 1 to the degree of u and exactly 1 to the degree of v — a total of 2 per edge. Summing degrees across all vertices is equivalent to counting each edge twice. Therefore: sum of degrees = 2 × |E|."
  explanation: "The immediate consequence is that degree sums are always even, and that an odd number of odd-degree vertices is impossible (since the sum of an odd count of odd numbers is odd, which can't equal 2|E|). These simple facts constrain degree sequences and are the first checks to apply before using more powerful tools like Erdős–Gallai."
```

## Explainer

You know from graph theory basics that the **degree** of a vertex is the number of edges incident to it. The **degree sequence** of a graph is simply the list of all vertex degrees, written in non-increasing order. For a triangle (3 vertices, 3 edges), every vertex has degree 2, so the degree sequence is (2, 2, 2). For a path of 4 vertices, the two endpoints have degree 1 and the two interior vertices have degree 2, giving (2, 2, 1, 1). The degree sequence is a coarse summary of a graph's structure — it tells you how "connected" the graph is without specifying which vertices connect to which.

The first essential fact is the **handshaking lemma**: the sum of all vertex degrees equals twice the number of edges. Each edge contributes 1 to the degree of each of its two endpoints, so it contributes 2 to the total degree count. Two immediate consequences: the sum of any degree sequence must be even, and an odd number of vertices with odd degree is impossible. These are necessary conditions for a sequence to be **graphical** — that is, realizable as the degree sequence of some simple graph. But they are not sufficient. The sequence (3, 1, 1, 1) sums to 6 (even) and describes a star graph K₁,₃. The sequence (3, 3, 2, 2, 2) sums to 12 (even) — is it realizable?

The **Erdős–Gallai theorem** gives a complete characterization of graphical sequences. A sequence d₁ ≥ d₂ ≥ ⋯ ≥ dₙ is graphical if and only if (1) the sum is even, and (2) for each k from 1 to n, the sum of the k largest degrees is at most k(k−1) plus the sum of min(dᵢ, k) for all remaining vertices. This looks complicated, but the idea is intuitive: the k highest-degree vertices can connect to at most k(k−1) other vertices among themselves (since it's a simple graph, no self-loops or multi-edges), and can only absorb min(dᵢ, k) connections from each remaining vertex. The theorem checks that no subset of high-degree vertices demands more connections than the rest of the graph can provide.

The realization problem also connects to graph representation: given a graphical sequence, you can construct a concrete graph using the **Hakimi algorithm** — repeatedly attach the highest-degree vertex to the next highest-degree vertices, reduce degrees accordingly, and repeat. This greedy construction always works if the sequence is graphical. Understanding degree sequences becomes foundational when you study random graphs (where you ask "what graph properties are typical for a random degree sequence?") and network analysis (where degree sequences characterize the connectivity structure of social networks, the internet, or biological systems).
