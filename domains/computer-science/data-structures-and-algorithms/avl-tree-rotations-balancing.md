---
id: avl-tree-rotations-balancing
title: AVL Tree Rotations and Balancing
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-search-trees
  type: hard
- id: tree-node-structure-properties
  type: hard
builds-toward:
- red-black-trees
tags:
- avl-trees
- balancing
- rotations
- self-balancing
- binary-search
stage: formal-systems
status: draft
---

# AVL Tree Rotations and Balancing

## Core Idea
AVL trees maintain height-balance: the height difference of left and right subtrees at every node is at most 1. When insertion or deletion violates this property, rotations (single or double) restore balance in O(log n) time per operation. This guarantees O(log n) search, insert, and delete regardless of insertion order.

## How It's Best Learned
Draw insertion sequences that trigger imbalance. Trace through single rotations (LL, RR cases) and double rotations (LR, RL cases). Implement rotation operations and rebalancing logic carefully. Understand how balance factors propagate upward during insertion.

## Common Misconceptions
- Rotations cost O(n) (they are O(1) each; O(log n) total per operation). - Every node must have perfect balance (AVL requires only |height difference| ≤ 1).

## Explainer

From your work with binary search trees, you know the core problem: a BST gives you O(log n) operations only when the tree is reasonably balanced, but ordinary insertions can produce a lopsided tree — in the worst case, a straight chain with O(n) height. An **AVL tree** (named after Adelson-Velsky and Landis, who invented it in 1962) is a BST that fixes this by enforcing a strict balance rule and using **rotations** to restore it whenever an insertion or deletion causes a violation.

The balance rule is simple: at every node, the heights of the left and right subtrees may differ by at most 1. Each node stores a **balance factor** — the height of its left subtree minus the height of its right subtree — which must be −1, 0, or +1. After you insert a new node (using standard BST insertion), you walk back up the path from the new node to the root, updating balance factors. If any node's balance factor becomes −2 or +2, that node is the **violation point**, and you apply a rotation to fix it.

There are four cases, but they reduce to two patterns. If the imbalance is "left-left" (the left child's left subtree is too tall) or "right-right" (symmetric), a **single rotation** fixes it. Think of it like straightening a bent arm: you rotate the violation node down and its heavy child up, and the BST ordering property is preserved because you are only rearranging the relative positions of three nodes and their subtrees. If the imbalance is "left-right" or "right-left" — a zig-zag pattern — a single rotation would just flip the imbalance to the other side. Instead, you apply a **double rotation**: first rotate the grandchild up to eliminate the zig-zag, then apply the single rotation. In code, a double rotation is literally two single rotations composed.

The critical insight is that each rotation is **O(1)** — it reassigns a constant number of pointers regardless of tree size. After an insertion, at most one rotation (single or double) at the lowest violation point is needed to restore balance for the entire tree. After a deletion, you may need to rotate at multiple ancestors as you walk up, but the number of rotations is bounded by the height, which is O(log n). This is what gives AVL trees their guarantee: because the height is always O(log n), and each rotation is O(1), every search, insert, and delete operation takes O(log n) time in the worst case, regardless of what order you inserted the keys. The tradeoff compared to a plain BST is the bookkeeping — maintaining balance factors and checking for violations — but the payoff is eliminating the possibility of degeneration entirely.
