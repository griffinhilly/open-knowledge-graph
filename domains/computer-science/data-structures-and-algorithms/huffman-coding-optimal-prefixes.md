---
id: huffman-coding-optimal-prefixes
title: 'Huffman Coding: Optimal Prefix Codes via Greedy'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: greedy-algorithms
  type: hard
- id: heap-structure-and-heapify-operations
  type: soft
- id: probability-axioms-and-rules
  type: soft
tags:
- greedy
- coding
- compression
stage: formal-systems
status: draft
---

# Huffman Coding: Optimal Prefix Codes via Greedy

## Core Idea
Huffman coding constructs an optimal prefix-free code for a given frequency distribution. Repeatedly merge the two least-frequent nodes into a new parent. The resulting tree encodes frequent symbols with shorter code lengths, minimizing expected code length. Proof via exchange argument shows optimality.

## How It's Best Learned
Implement Huffman coding using a min-heap. Build the tree, extract codes, and measure compression on real text. Compare code lengths to fixed-length and other variable-length schemes.

## Common Misconceptions
- Assuming Huffman codes are always optimal; they're optimal for the given frequency distribution but not for adaptive/online scenarios.
- Not recognizing that Huffman is a greedy algorithm; the exchange argument proves correctness.
- Forgetting that the code tree must be transmitted with the compressed data, adding overhead.

## Explainer

You already know that a greedy algorithm builds a solution piece by piece, always choosing the locally optimal next step. Huffman coding applies this strategy to a specific problem: given a set of symbols with known frequencies, assign binary codes so that the total number of bits used is minimized. The key constraint is that the code must be **prefix-free** — no codeword is a prefix of another — so the decoder can read a stream of bits and unambiguously determine where each symbol ends without needing delimiters.

The algorithm works bottom-up. Start with each symbol as a leaf node, weighted by its frequency. Repeatedly extract the two nodes with the smallest frequencies — this is where your knowledge of heaps pays off, since a **min-heap** makes this extraction O(log n) — and merge them into a new internal node whose frequency is their sum. This new node goes back into the heap. Continue until only one node remains: the root of the Huffman tree. Every left branch gets a 0 and every right branch gets a 1, and the code for each symbol is the sequence of bits on the path from root to its leaf.

Why does this produce optimal codes? The intuition is that the two least-frequent symbols should be the deepest in the tree (longest codes), because they contribute the least to the total bit count. The **exchange argument** formalizes this: if the two least-frequent symbols were not siblings at the maximum depth, you could swap them into that position and reduce or maintain the total cost, contradicting the assumption that the original tree was optimal. By induction, the greedy merging strategy yields the minimum expected code length for any prefix-free code.

Consider a concrete example: if you have symbols A (50%), B (25%), C (15%), D (10%), the algorithm first merges C and D (combined 25%), then merges that node with B (combined 50%), then merges with A. The result: A gets a 1-bit code, B gets a 2-bit code, and C and D get 3-bit codes. Compare this to a fixed 2-bit code for all four symbols — Huffman's variable-length scheme uses fewer bits overall because it assigns shorter codes to more frequent symbols. This is the core insight: **frequency determines depth**, and the greedy merge ensures the mapping is optimal.
