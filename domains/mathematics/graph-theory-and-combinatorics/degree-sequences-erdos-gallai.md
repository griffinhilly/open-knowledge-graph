---
id: degree-sequences-erdos-gallai
title: Degree Sequences and the Erdős–Gallai Theorem
domain: mathematics
course: graph-theory-and-combinatorics
prerequisites:
- id: formal-definitions-graph-theory
  type: hard
builds-toward:
- graph-operations-and-products
- extremal-graph-theory
tags:
- degree-sequences
- graph-characterization
- theorems
stage: formal-systems
status: draft
---

# Degree Sequences and the Erdős–Gallai Theorem

## Core Idea
A degree sequence is the ordered list of vertex degrees in a graph. Not every sequence of non-negative integers is graphical (realizable as a degree sequence). The Erdős–Gallai theorem provides a complete characterization: a sequence is graphical if and only if the sum is even and a specific inequality holds for each prefix.

## How It's Best Learned
Start with the handshaking lemma and verify why all graphical sequences have even sum. Then apply the Erdős–Gallai criterion to both graphical and non-graphical sequences to see where it catches impossible cases.

## Common Misconceptions
- Assuming that high average degree guarantees specific structures (e.g., a Hamiltonian cycle).
- Forgetting to check both the sum-is-even condition and the full Erdős–Gallai inequalities.
- Misunderstanding what 'lexicographically largest' means in the Havel-Hakimi algorithm.

## Questions

```yaml
- question: "The sequence (3, 3, 3, 1) has an even sum of 10. Is it graphical (realizable as a simple graph)?"
  type: multiple-choice
  options:
    - "Yes — any sequence with even sum can be realized as a simple graph"
    - "Yes — no degree exceeds n−1 = 3, so the sequence satisfies all necessary conditions"
    - "No — even though the sum is even, the three degree-3 vertices cannot all be simultaneously satisfied in a simple graph on 4 vertices"
    - "No — graphical sequences cannot contain odd numbers"
  answer: 2
  explanation: "Even sum is necessary but not sufficient. Each of the three degree-3 vertices needs 3 neighbors, but in a 4-vertex graph, each vertex can have at most 3 neighbors total. The degree-1 vertex can serve as a neighbor only once, and the three degree-3 vertices would need to share connections in a way that is impossible without multi-edges or self-loops. The Erdős–Gallai inequalities catch exactly this kind of overcommitment of degree budget."

- question: "The Erdős–Gallai theorem checks that for each k, the sum of the top-k degrees is at most k(k−1) plus the sum of min(dᵢ, k) for the remaining vertices. What does this inequality fundamentally constrain?"
  type: multiple-choice
  options:
    - "The total number of edges in the graph, ensuring it does not exceed the maximum for n vertices"
    - "How many edges the k highest-degree vertices can collectively have, accounting for edges among themselves and edges to the remaining vertices"
    - "Whether the graph contains a subgraph with a Hamiltonian cycle"
    - "The chromatic number of any graph realizing the sequence"
  answer: 1
  explanation: "The right side of the inequality has two parts: k(k−1) counts the maximum possible edges among the top-k vertices themselves (a complete graph on k vertices has k(k−1)/2 edges, contributing degree k−1 to each of the k vertices), and the sum of min(dᵢ, k) counts how many connections the remaining n−k vertices can contribute to the top-k group. If the top-k vertices claim more total degree than these two pools can supply, the sequence is impossible — no matter how you try to draw it."

- question: "By the handshaking lemma, the sum of all vertex degrees in any simple graph must be even."
  type: true-false
  answer: true
  explanation: "Every edge contributes exactly 2 to the total degree count — one for each of its two endpoints. Therefore the sum of all degrees equals 2|E|, which is always even. This is the first and simplest necessary condition for a sequence to be graphical. A sequence with odd sum — like (3, 3, 1) — can be rejected immediately without further analysis."

- question: "A non-increasing sequence of non-negative integers with an even sum is always graphical — it can always be realized as the degree sequence of some simple graph."
  type: true-false
  answer: false
  explanation: "Even sum is necessary but not sufficient. The sequence (3, 3, 3, 1) has even sum 10 but is not graphical: the three degree-3 vertices cannot all find 3 distinct neighbors in a 4-vertex simple graph. The Erdős–Gallai theorem exists precisely because even sum alone fails to capture all the constraints. Additional inequalities are required to ensure the degree budget of the highest-degree vertices can actually be distributed as valid edges."

- question: "Why does the Erdős–Gallai theorem need to check a family of prefix inequalities rather than just verify that the total sum is even? What structural impossibility does each inequality detect?"
  type: short-answer
  answer: "Even sum guarantees that the total degree budget could in principle correspond to some number of edges, but it does not guarantee that the degrees can be distributed among specific vertices without conflict. Each Erdős–Gallai inequality checks whether the k highest-degree vertices can collectively be satisfied given (a) the edges they can share among themselves and (b) the connections the remaining vertices can provide. If any prefix violates the inequality, those k vertices are overclaiming degree that cannot be physically supplied — an impossibility no matter how the rest of the graph is arranged."
  explanation: "The handshaking lemma is a global constraint; the Erdős–Gallai inequalities are local constraints on every subset of the highest-degree vertices. A globally valid sum can still fail locally — a few high-degree vertices can demand more connections than their neighborhood can supply. The Havel-Hakimi algorithm makes this concrete: if you greedily connect the highest-degree vertex to its required neighbors and the process fails, you have found the impossibility that Erdős–Gallai's inequality detected algebraically."
```

## Explainer

From the formal definitions of graph theory, you know that the **degree** of a vertex is the number of edges incident to it. The **degree sequence** of a graph is the list of all vertex degrees arranged in non-increasing order. For example, a path on 4 vertices has degrees 1, 2, 2, 1 — degree sequence (2, 2, 1, 1). A complete graph K₄ has every vertex with degree 3 — degree sequence (3, 3, 3, 3). The degree sequence is a simple invariant: isomorphic graphs have the same degree sequence. But the converse is false — two non-isomorphic graphs can share a degree sequence. Despite this limitation, degree sequences reveal a surprising amount about a graph's structure.

The first necessary condition for a sequence to be **graphical** (realizable by some simple graph) comes from the **handshaking lemma**: the sum of all degrees equals twice the number of edges, so the sum must be even. The sequence (3, 3, 1) has sum 7, which is odd — impossible for any graph. But even-sum is not sufficient. The sequence (3, 3, 3, 1) has even sum 10, but can you draw it? Each of the three degree-3 vertices needs 3 neighbors, and the single degree-1 vertex can only serve as a neighbor once — you'll quickly run into trouble. The sequence is not graphical despite having an even sum.

The **Erdős–Gallai theorem** gives a complete characterization. Sort the sequence in non-increasing order as d₁ ≥ d₂ ≥ ⋯ ≥ dₙ. The sequence is graphical if and only if (1) the sum is even, and (2) for every k from 1 to n, the sum of the first k terms is at most k(k−1) plus the sum of min(dᵢ, k) for i from k+1 to n. The left side counts the degree "budget" of the k highest-degree vertices; the right side bounds how many edges they can actually have. The bound k(k−1) accounts for edges among the top-k vertices themselves; the sum accounts for edges from those vertices to the remaining n−k vertices. If this inequality is ever violated, the k highest-degree vertices simply cannot all be satisfied simultaneously.

A complementary tool is the **Havel-Hakimi algorithm**: repeatedly take the vertex of highest degree d, connect it to the next d vertices in the sorted list, remove it, and continue. If the sequence is graphical, this construction succeeds; if you ever need to connect to a vertex with degree 0, it fails. Havel-Hakimi is both an existence proof and a construction method. Together, Erdős–Gallai and Havel-Hakimi give you two perspectives on the same question: one tells you *whether* a sequence is graphical via inequalities, the other *constructs* a graph realizing it (if one exists).
