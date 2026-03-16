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

## Explainer

From the formal definitions of graph theory, you know that the **degree** of a vertex is the number of edges incident to it. The **degree sequence** of a graph is the list of all vertex degrees arranged in non-increasing order. For example, a path on 4 vertices has degrees 1, 2, 2, 1 — degree sequence (2, 2, 1, 1). A complete graph K₄ has every vertex with degree 3 — degree sequence (3, 3, 3, 3). The degree sequence is a simple invariant: isomorphic graphs have the same degree sequence. But the converse is false — two non-isomorphic graphs can share a degree sequence. Despite this limitation, degree sequences reveal a surprising amount about a graph's structure.

The first necessary condition for a sequence to be **graphical** (realizable by some simple graph) comes from the **handshaking lemma**: the sum of all degrees equals twice the number of edges, so the sum must be even. The sequence (3, 3, 1) has sum 7, which is odd — impossible for any graph. But even-sum is not sufficient. The sequence (3, 3, 3, 1) has even sum 10, but can you draw it? Each of the three degree-3 vertices needs 3 neighbors, and the single degree-1 vertex can only serve as a neighbor once — you'll quickly run into trouble. The sequence is not graphical despite having an even sum.

The **Erdős–Gallai theorem** gives a complete characterization. Sort the sequence in non-increasing order as d₁ ≥ d₂ ≥ ⋯ ≥ dₙ. The sequence is graphical if and only if (1) the sum is even, and (2) for every k from 1 to n, the sum of the first k terms is at most k(k−1) plus the sum of min(dᵢ, k) for i from k+1 to n. The left side counts the degree "budget" of the k highest-degree vertices; the right side bounds how many edges they can actually have. The bound k(k−1) accounts for edges among the top-k vertices themselves; the sum accounts for edges from those vertices to the remaining n−k vertices. If this inequality is ever violated, the k highest-degree vertices simply cannot all be satisfied simultaneously.

A complementary tool is the **Havel-Hakimi algorithm**: repeatedly take the vertex of highest degree d, connect it to the next d vertices in the sorted list, remove it, and continue. If the sequence is graphical, this construction succeeds; if you ever need to connect to a vertex with degree 0, it fails. Havel-Hakimi is both an existence proof and a construction method. Together, Erdős–Gallai and Havel-Hakimi give you two perspectives on the same question: one tells you *whether* a sequence is graphical via inequalities, the other *constructs* a graph realizing it (if one exists).
