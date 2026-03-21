---
id: avl-trees
title: AVL Trees
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-search-trees
  type: hard
- id: time-space-complexity
  type: soft
- id: logarithms-intro
  type: soft
tags:
- AVL-tree
- balanced-BST
- rotations
- self-balancing
stage: formal-systems
status: validated
---

# AVL Trees

## Core Idea
An AVL tree is a self-balancing binary search tree where the heights of the left and right subtrees of any node differ by at most one (the balance factor is in {−1, 0, +1}). After each insertion or deletion, the tree checks balance factors and performs rotations — single or double — to restore balance. This guarantees O(log n) worst-case time for all operations. AVL trees were the first self-balancing BST; red-black trees are often preferred in practice for slightly lower rotation overhead.

## How It's Best Learned
First master BST insertions, then study rotations in isolation. Implement AVL insertion with balance-factor tracking. The four rotation cases (LL, RR, LR, RL) are best understood through diagrams before translating to code.

## Common Misconceptions
- Rotations preserve the BST ordering property; they only restructure the tree shape without violating the BST invariant.
- AVL trees require rebalancing on deletion as well as insertion, which is often overlooked in initial implementations.

## Questions

```yaml
- question: "After performing a left rotation to correct a right-heavy imbalance in an AVL tree, which property is guaranteed?"
  type: multiple-choice
  options:
    - "The height of the rotated subtree decreases by exactly 1"
    - "Every node in the subtree now has balance factor 0"
    - "The inorder traversal of the tree is unchanged"
    - "No further balance checks are needed above the rotation point"
  answer: 2
  explanation: "Rotations are defined specifically to preserve the BST invariant: for any node, left subtree keys are smaller and right subtree keys are larger. A rotation reshapes local structure without moving any key to a position that violates ordering. The inorder traversal before and after any rotation is identical. Options A and B are false in general — height change and zero balance factors are not guaranteed for every rotation. Option D is false: ancestors of the rotated subtree may still need balance factor updates."

- question: "An AVL node has balance factor +2 and its left child has balance factor -1 (right-heavy). Which fix restores AVL balance?"
  type: multiple-choice
  options:
    - "A single right rotation at the unbalanced node"
    - "A single left rotation at the unbalanced node"
    - "A left rotation at the left child, then a right rotation at the unbalanced node (LR double rotation)"
    - "A right rotation at the left child, then a left rotation at the unbalanced node (RL double rotation)"
  answer: 2
  explanation: "This is the LR case: the unbalanced node is left-heavy (+2) but its left child is right-heavy (-1), creating a zigzag. A single right rotation at the root would still leave the tree unbalanced because the imbalance bends the wrong way. The fix is a double rotation: rotate the left child leftward first (converting the zigzag into an LL straight line), then rotate the unbalanced node rightward. Option A fails for this zigzag configuration. Option D describes the RL case, which applies when the imbalance goes the other direction."

- question: "A rotation in an AVL tree never changes the relative ordering of nodes in an inorder traversal."
  type: true-false
  answer: true
  explanation: "Rotations only restructure which node is the local root and how children are attached — they always maintain the BST invariant that left subtree keys < node key < right subtree keys. The inorder traversal (sorted order) is identical before and after any rotation. This is why rotations are safe: they fix tree shape (the balance problem) without corrupting the search property (the BST invariant)."

- question: "A single deletion from an AVL tree can require O(n) rotations to restore balance."
  type: true-false
  answer: false
  explanation: "Deletions in AVL trees may require checking balance factors at each level from the deleted node to the root — at most O(log n) levels — and potentially a rotation at each level. But the height of an AVL tree is O(log n), so the worst case is O(log n) rotations, never O(n). Insertions are even cheaper: at most 1 or 2 rotations are needed regardless of tree size. The O(log n) height bound is what limits cascade costs."

- question: "Why does the AVL balance condition guarantee O(log n) height, and why does that guarantee matter for operations?"
  type: short-answer
  answer: "The AVL condition (balance factors in {-1, 0, +1}) ensures no subtree can be more than one level taller than its sibling. This means the minimum number of nodes in an AVL tree of height h grows exponentially with h (following a Fibonacci-like recurrence), so h = O(log n). Since every BST operation — search, insert, delete — traverses a path from root to a leaf, height directly bounds their time complexity. O(log n) height means O(log n) worst-case for all operations, eliminating the O(n) worst case of unbalanced BSTs."
  explanation: "The contrast with unbalanced BSTs is stark: inserting sorted data into a plain BST yields a linked list of height n, making search O(n). AVL trees eliminate this by paying O(log n) overhead per insertion and deletion for balance maintenance. Since rotations are O(1) and occur at most O(log n) times per operation, this overhead is absorbed. In practice, red-black trees are often preferred for their lower rotation counts, but AVL trees produce tighter balance and are faster for lookup-heavy workloads."
```

## Explainer

From your work with binary search trees, you know the fundamental problem: a BST's performance depends entirely on its shape. Insert elements in sorted order and you get a linked list with O(n) operations; insert them in a balanced way and you get O(log n). The trouble is that you rarely control the insertion order. An **AVL tree** solves this by automatically restructuring itself after every modification to guarantee that the tree stays approximately balanced — specifically, that no node's left and right subtrees differ in height by more than one.

Each node in an AVL tree tracks its **balance factor**: the height of its left subtree minus the height of its right subtree. A balance factor of 0 means the subtrees are the same height; +1 means the left is one taller; −1 means the right is one taller. All of these are acceptable. But after an insertion or deletion, some node might end up with a balance factor of +2 or −2 — that node's subtrees have become too uneven, and the tree must be corrected.

The correction mechanism is the **rotation**, which reshapes a local portion of the tree without violating the BST ordering invariant. There are four cases. If a node is left-heavy (+2) and its left child is also left-heavy or balanced (+1 or 0), a single **right rotation** fixes it: the left child moves up to take the unbalanced node's place, and the unbalanced node becomes the right child. The mirror case — right-heavy with right-heavy child — uses a single **left rotation**. The trickier cases arise when the imbalance zigzags: a left-heavy node with a right-heavy left child (or vice versa). These require a **double rotation** — first rotate the child to straighten the zigzag into a straight line, then rotate the unbalanced node. These four cases (LL, RR, LR, RL) cover every possible imbalance.

The height guarantee is what makes AVL trees powerful. Because every node's subtrees differ in height by at most one, the maximum height of an AVL tree with n nodes is approximately 1.44 log₂(n). Since every BST operation — search, insert, delete — takes time proportional to the tree's height, AVL trees guarantee **O(log n) worst-case** performance for all operations. The cost is that insertions and deletions require walking back up the tree to check balance factors and possibly perform rotations (at most O(log n) balance checks and at most two rotations per insertion, though deletions can cascade). In practice, red-black trees are often preferred because they require fewer rotations on average, but AVL trees produce more tightly balanced trees and are faster for lookup-heavy workloads.
