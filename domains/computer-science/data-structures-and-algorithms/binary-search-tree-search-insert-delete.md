---
id: binary-search-tree-search-insert-delete
title: 'Binary Search Trees: Search, Insertion, Deletion'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-tree-properties-height-balance-completeness
  type: hard
- id: binary-search-trees
  type: soft
builds-toward:
- avl-tree-balance-rotations-maintenance
- b-tree-multi-level-indexing
tags:
- bst
- search
- insertion
stage: formal-systems
status: draft
---

# Binary Search Trees: Search, Insertion, Deletion

## Core Idea
A BST maintains the invariant: left subtree < node < right subtree, enabling O(h) search and insertion. Deletion is trickier—removing a node with two children requires finding the successor. Unbalanced trees degrade to O(n).

## How It's Best Learned
Implement insertion and deletion from scratch. Trace each operation: insert elements to create an unbalanced tree, then delete various nodes (leaf, one child, two children). Measure tree height to see performance degradation.

## Common Misconceptions
- A BST is always efficient—unbalanced trees can be O(n) per operation.
- Deletion is easier than insertion—actually, deletion with two children is the hardest case.
- The successor is always the right-most node in the right subtree (true, but must find it iteratively or recursively).

## Questions

```yaml
- question: "You insert the values 1, 2, 3, 4, 5 into an empty BST in that order. What is the time complexity of a subsequent search for value 5?"
  type: multiple-choice
  options:
    - "O(log n) — BSTs always search in logarithmic time due to the BST property"
    - "O(n) — the tree has degenerated into a right-skewed linked list"
    - "O(n log n) — sorted insertion increases search complexity multiplicatively"
    - "O(1) — the BST property allows direct access to any value"
  answer: 1
  explanation: "Inserting sorted values into a BST causes each new value to be placed as the rightmost leaf (always larger than everything before it). The tree becomes a right-skewed chain with height h = n − 1 = 4. Searching for 5 requires traversing every node. BST search runs in O(h), not O(log n) — and h can equal n in the worst case. This is the critical performance trap of unbalanced BSTs and the motivation for self-balancing variants like AVL trees."

- question: "To delete a node with two children from a BST while maintaining the BST invariant, the standard procedure is to:"
  type: multiple-choice
  options:
    - "Remove the node and attach both orphaned subtrees directly to the root"
    - "Replace the node's value with its in-order successor's value, then delete the successor node"
    - "Replace the node with its left child, and discard the right subtree"
    - "Rebuild the entire subtree rooted at the deleted node from scratch"
  answer: 1
  explanation: "The in-order successor is the smallest value in the right subtree — found by going right once, then left as far as possible. This value is guaranteed to be larger than everything in the left subtree and smaller than everything else in the right subtree, so substituting it preserves the BST invariant. Crucially, the in-order successor has at most one child (no left child, since it's the leftmost node in its subtree), so deleting it reduces to the easy leaf or one-child case. This cascading reduction is the key insight."

- question: "BST search always runs in O(log n) time because the BST property guarantees each comparison eliminates half the remaining nodes."
  type: true-false
  answer: false
  explanation: "BST search runs in O(h) where h is the tree's height, not O(log n). In a balanced tree, h ≈ log₂ n, giving logarithmic search. But in an unbalanced tree — such as one built by inserting sorted data — h can equal n, making every operation O(n). The BST property only guarantees that you go left or right correctly at each step; it makes no promise about the depth of the tree. This is why balanced BSTs (AVL, red-black) are necessary for guaranteed logarithmic performance."

- question: "After a BST insertion, the new node always becomes a leaf in the tree."
  type: true-false
  answer: true
  explanation: "Insertion follows the same path as search: start at the root, compare, go left or right, and repeat until reaching a null pointer. That null pointer is exactly where the new node belongs by the BST ordering — and since it was null, it has no children. The new node is always attached as a leaf. This is also why insertion cannot violate the BST invariant for existing nodes: the new node is placed precisely where the search ordering dictates it should be."

- question: "Why can inserting already-sorted data into an empty BST lead to O(n) search time, and what property of balanced BSTs prevents this?"
  type: short-answer
  answer: "Sorted insertion causes each new value to always be placed as the rightmost (or leftmost) child, creating a degenerate tree that is effectively a linked list with height h = n. Search then requires O(n) comparisons. Balanced BSTs (AVL trees, red-black trees) perform rotations after insertions and deletions to ensure the height stays O(log n) regardless of insertion order, guaranteeing O(log n) search in all cases."
  explanation: "The degeneration happens because the BST property only requires left < node < right — it says nothing about balance. A sorted sequence satisfies the invariant perfectly while creating a maximally unbalanced tree. Balanced BSTs maintain an additional invariant: no subtree can be more than a constant factor taller than its sibling. Rotations are local operations that restructure the tree without changing in-order traversal, preserving the BST property while restoring balance."
```

## Explainer

You already know that a binary tree organizes data hierarchically and that properties like height and balance affect performance. A **binary search tree (BST)** adds one crucial rule: for every node, all values in its left subtree are smaller and all values in its right subtree are larger. This single invariant turns the tree into a searchable structure — at each node, you know which half of the remaining data to explore, much like binary search on a sorted array.

**Searching** is the most natural operation. Start at the root and compare your target value to the current node. If it matches, you are done. If the target is smaller, go left; if larger, go right. Each comparison eliminates an entire subtree, so search takes O(h) time where h is the tree's height. In a balanced tree with n nodes, h ≈ log₂(n), giving you the same logarithmic efficiency as binary search on an array. **Insertion** follows the same path: search for where the new value *would* be, and when you reach a null pointer (a missing child), attach the new node there. The new node always becomes a leaf, and the BST property is automatically maintained because you placed it exactly where the search ordering dictates.

**Deletion** is where things get interesting, because removing a node from the middle of the tree must preserve the BST invariant. There are three cases of increasing difficulty. Deleting a **leaf** (no children) is trivial — just remove it. Deleting a node with **one child** is almost as easy — replace the node with its single child, and the ordering is preserved because the child's entire subtree was already on the correct side. The hard case is deleting a node with **two children**. You cannot simply remove it without orphaning two subtrees. The solution is to find the node's **in-order successor** — the smallest value in its right subtree (found by going right once, then left as far as possible). This successor has at most one child (it cannot have a left child, or it would not be the leftmost node). Copy the successor's value into the node being deleted, then delete the successor node, which falls into the easy one-child or leaf case.

The critical performance caveat is that all three operations — search, insert, delete — are O(h), not O(log n). If you insert already-sorted data into an empty BST, each new value goes to the rightmost position, producing a degenerate tree that is effectively a linked list with h = n. In this worst case, every operation takes O(n) time. This is why balanced BST variants like AVL trees and red-black trees exist: they perform rotations after modifications to keep h close to log₂(n), guaranteeing logarithmic performance regardless of insertion order.
