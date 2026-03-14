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
stage: abstract-reasoning
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
