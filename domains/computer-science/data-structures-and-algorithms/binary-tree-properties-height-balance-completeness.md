---
id: binary-tree-properties-height-balance-completeness
title: 'Binary Tree Properties: Height, Balance, Completeness'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-tree-structure-node-representation
  type: hard
builds-toward:
- binary-search-tree-search-insert-delete
tags:
- binary-tree
- properties
- analysis
stage: formal-systems
status: draft
---

# Binary Tree Properties: Height, Balance, Completeness

## Core Idea
Height is the longest path from root to leaf. A balanced tree has height O(log n), enabling efficient operations. Complete trees have all levels full except possibly the last. These properties directly impact algorithm performance.

## Questions

```yaml
- question: "You insert the values 1, 2, 3, 4, 5 into a plain (non-self-balancing) binary search tree in that order. What is the height of the resulting tree?"
  type: multiple-choice
  options:
    - "2 — BSTs automatically balance themselves during insertion"
    - "3 — each level contains one more node than the previous"
    - "4 — each node becomes the right child of the previous, forming a degenerate chain"
    - "The height depends only on the number of nodes, not the insertion order"
  answer: 2
  explanation: "Inserting sorted values into a plain BST produces the worst case: a right-leaning chain where every node has one child. With 5 nodes, the height is 4 (number of edges from root to leaf). This degenerate tree has O(n) search, insert, and delete — as slow as a linked list. This is why insertion order matters and why self-balancing trees (AVL, red-black) exist."

- question: "Which of the following best explains why a complete binary tree can be stored in an array without pointers?"
  type: multiple-choice
  options:
    - "The left-to-right filling rule ensures node i always has children at indices 2i+1 and 2i+2, with no gaps in the array"
    - "Complete trees have no wasted memory because every level is fully filled"
    - "Array storage works for any binary tree; complete trees are not special in this regard"
    - "Complete trees are stored by writing the in-order traversal into consecutive array slots"
  answer: 0
  explanation: "The key is the index formula: in a complete binary tree stored in a 0-indexed array, node i's left child is at 2i+1 and right child is at 2i+2. This works because complete trees fill levels left-to-right with no gaps, guaranteeing that array slots 0 through n-1 are all occupied with valid nodes. Sparse trees would leave holes requiring explicit null slots or pointers. Heaps exploit this exact property."

- question: "A binary tree with n nodes always has height O(log n)."
  type: true-false
  answer: false
  explanation: "Only balanced trees guarantee O(log n) height. A degenerate tree — formed, for example, by inserting sorted values into a plain BST — has height n−1, which is O(n). The difference matters enormously for performance: a 1,000-node balanced tree has height ~10; a degenerate chain has height 999. O(log n) height requires active balancing (as in AVL or red-black trees) or a structured insertion pattern."

- question: "A complete binary tree has all levels fully filled except possibly the last, which is filled from left to right."
  type: true-false
  answer: true
  explanation: "This is the definition of a complete binary tree. It distinguishes 'complete' from 'perfect' (all levels fully filled) and 'full' (every node has 0 or 2 children). The left-to-right filling constraint is what enables array storage without gaps and guarantees minimum height ⌊log₂ n⌋ for n nodes. The heap data structure depends entirely on this property."

- question: "Why does the height of a binary tree matter for algorithm performance, and what is the worst-case height of a plain binary search tree with n nodes?"
  type: short-answer
  answer: "Most tree operations (search, insert, delete) traverse from root to leaf, visiting one node per level. The height is therefore the worst-case number of steps for these operations. For a balanced tree, height is O(log n), giving O(log n) operations. The worst case for a plain BST is height n−1 — a degenerate chain where every node has only one child — which occurs when values are inserted in sorted order. This reduces performance to O(n), equivalent to a linked list."
  explanation: "Height is the performance story for any tree-based data structure. The gap between O(log n) and O(n) is the gap between searching 1,000 nodes in 10 steps versus 999 steps. Self-balancing trees pay a small overhead per insertion to guarantee the O(log n) height bound, which makes all subsequent operations fast regardless of insertion order."
```

## Explainer

Now that you understand how binary trees are structured — nodes with left and right children forming a recursive hierarchy — the next question is: what makes one binary tree better than another? The answer lies in three measurable properties that directly determine how fast tree operations run: **height**, **balance**, and **completeness**.

The **height** of a binary tree is the number of edges on the longest path from the root to any leaf. A single-node tree has height 0. Why does height matter? Because most tree operations — search, insert, delete — work by walking from the root toward a leaf, examining one node per level. The height is therefore the worst-case number of steps. A tree with n nodes can have height as large as n−1 (a degenerate chain where every node has only one child — essentially a linked list) or as small as ⌊log₂ n⌋ (a perfectly packed tree where every level is full). The difference is dramatic: searching a chain of 1,000 nodes takes 999 steps; searching a tree of height 9 takes at most 9 steps.

A tree is **balanced** when its height is O(log n) — close to the theoretical minimum. The precise definition varies by context: some definitions require that every node's left and right subtrees differ in height by at most 1 (as in AVL trees), while others allow a constant factor of slack. The important insight is that balance is what separates efficient trees from degenerate ones. If you insert sorted data into a plain binary search tree, you get the worst case: a chain. Self-balancing tree variants (AVL, red-black) maintain balance through rotations during insertion and deletion, guaranteeing O(log n) operations regardless of insertion order.

A **complete binary tree** has a specific shape: every level is fully filled except possibly the last, which is filled from left to right. A **full binary tree** is even stricter — every node has either zero or two children, no singles. A **perfect binary tree** has both properties: every level is completely filled. Complete trees are significant because they pack nodes as tightly as possible, minimizing height for a given number of nodes, and they can be stored efficiently in an array without pointers. The heap data structure exploits this: because a complete binary tree of n nodes always has height ⌊log₂ n⌋ and maps cleanly to array indices (node i's children are at 2i+1 and 2i+2), heaps achieve O(log n) insert and delete with minimal overhead. Understanding these properties gives you the vocabulary to evaluate any tree-based data structure: ask about its height guarantee, and you know its performance story.
