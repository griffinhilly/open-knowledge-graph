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
