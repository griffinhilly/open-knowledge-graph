---
id: avl-tree-balance-rotations-maintenance
title: 'AVL Trees: Rotations and Balancing Strategies'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-search-tree-search-insert-delete
  type: hard
- id: avl-trees
  type: soft
tags:
- avl-tree
- balancing
- rotation
stage: formal-systems
status: draft
---

# AVL Trees: Rotations and Balancing Strategies

## Core Idea
AVL trees maintain balance via rotations: single rotations fix LL and RR imbalance; double rotations fix LR and RL. After each insertion/deletion, the height-balance property (|left height - right height| ≤ 1) is restored, guaranteeing O(log n) operations.

## Explainer

From binary search trees, you know that search, insertion, and deletion all take time proportional to the tree's height. The problem is that an unbalanced BST can degenerate into a linked list — insert keys 1, 2, 3, 4, 5 in order and you get a chain leaning entirely to the right, with height equal to n and O(n) operations. AVL trees prevent this by enforcing a strict invariant: at every node, the heights of the left and right subtrees differ by at most 1. This **balance factor** (left height minus right height) must always be -1, 0, or +1. When an insertion or deletion violates this invariant, the tree fixes itself through rotations.

A **rotation** is a local restructuring operation that changes parent-child relationships between two or three nodes while preserving the BST ordering property. Consider a right-heavy imbalance where a node's balance factor becomes -2 because its right child's right subtree is too tall (an **RR case**). A **left rotation** lifts the right child up to replace the imbalanced node, which becomes the new left child. The key insight is that this operation is O(1) — it only changes three pointers — yet it reduces the height of the subtree by one, restoring balance. The mirror case (left-heavy, **LL case**) uses a **right rotation** with the symmetric pointer changes.

The trickier cases are **LR** and **RL imbalances**, where the heavy subtree zigzags. If a node is left-heavy but its left child is right-heavy (LR case), a single rotation would not fix the problem — it would just create the mirror imbalance. The solution is a **double rotation**: first rotate the left child leftward to straighten the zigzag into a straight LL case, then rotate the original node rightward. The RL case is the mirror: rotate the right child rightward, then the original node leftward. In all four cases, the result is a balanced subtree with the median of the three involved nodes at the root, and the operation completes in O(1) time.

After each insertion or deletion, the algorithm walks back up the path from the affected node to the root, updating balance factors and performing at most one rotation (for insertion) or O(log n) rotations (for deletion) along the way. Because the tree always stays balanced, its height is guaranteed to be at most 1.44 · log₂(n), which means all operations remain O(log n) in the worst case. This is the fundamental tradeoff AVL trees make: every mutation pays a small constant overhead for balance checking and potential rotation, but in return, no sequence of operations can ever degrade the tree into the O(n) worst case that plagues ordinary BSTs.
