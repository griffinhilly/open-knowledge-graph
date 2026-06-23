---
id: binary-search-trees
title: Binary Search Trees
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-trees
  type: hard
- id: tree-traversals
  type: hard
- id: time-space-complexity
  type: soft
- id: binary-search-algorithm
  type: soft
- id: binary-tree-properties-height-balance-completeness
  type: soft
- id: tree-node-structure-properties
  type: soft
builds-toward:
- avl-tree-rotations-balancing
tags:
- BST
- binary-search-tree
- ordered-tree
- search
stage: formal-systems
status: validated
---
# Binary Search Trees

## Core Idea
A binary search tree (BST) is a binary tree where, for every node, all values in the left subtree are less than the node's value and all values in the right subtree are greater. This property allows searching, insertion, and deletion in O(h) time where h is the height. For a balanced tree, h = O(log n), giving efficient O(log n) operations. However, inserting sorted data produces a degenerate (linear) tree with h = O(n), making it no better than a linked list.

## How It's Best Learned
Implement BST search, insert, and delete from scratch. Pay close attention to the three cases in deletion: leaf node, one child, two children. Test with sorted and random insertion orders to observe the impact on tree shape.

## Common Misconceptions
- BSTs are not inherently balanced; their performance depends entirely on the distribution of insertions.
- Deletion is the trickiest operation: the two-child case requires finding the in-order successor (or predecessor) to replace the deleted node.

## Questions

```yaml
- question: "You insert the integers 1, 2, 3, 4, 5 into a BST in that order. What is the time complexity of a subsequent search operation?"
  type: multiple-choice
  options:
    - "O(log n), because a BST always organizes data for binary search"
    - "O(n), because sorted insertions produce a degenerate tree with height n"
    - "O(n log n), because the tree must be rebuilt before searching"
    - "O(1), because the last inserted node is always the root"
  answer: 1
  explanation: "When you insert keys in sorted order, each new key is always larger than all existing keys, so it always extends the rightmost branch. The result is a straight chain leaning right — effectively a linked list — with height n = 5. A search must traverse this entire chain in the worst case, giving O(n) time. This is the critical vulnerability of unbalanced BSTs: the O(log n) guarantee only holds for a balanced tree, and basic BSTs provide no balancing mechanism."

- question: "To delete a node with two children from a BST, you should replace it with which value?"
  type: multiple-choice
  options:
    - "The node's parent, then reattach both subtrees to the grandparent"
    - "The in-order successor (leftmost node of the right subtree) or in-order predecessor, then delete that successor"
    - "The root of the right subtree, discarding the left subtree to preserve the BST property"
    - "The average of the left and right children's keys"
  answer: 1
  explanation: "You cannot simply connect two subtrees to the parent — this would require a node to have three children and would violate the BST ordering property. The standard approach is to find the in-order successor (the smallest key in the right subtree) or in-order predecessor (the largest key in the left subtree). Copying that value into the deleted node preserves the BST property. The successor/predecessor is then deleted from its original location — it has at most one child, reducing to an easier deletion case."

- question: "A BST containing 15 nodes typically supports search in O(log 15) steps."
  type: true-false
  answer: false
  explanation: "BST performance depends on height, not just size. A 15-node BST has height between ⌊log₂ 15⌋ = 3 (perfectly balanced) and 14 (fully degenerate). If the 15 nodes were inserted in sorted order, the height is 14 and search takes O(n) in the worst case. The O(log n) guarantee only holds when the tree is balanced, which basic BSTs do not guarantee. Self-balancing variants like AVL trees maintain O(log n) height explicitly."

- question: "An in-order traversal of a BST visits nodes in sorted (ascending) order."
  type: true-false
  answer: true
  explanation: "This follows directly from the BST property: at every node, all left descendants are smaller and all right descendants are larger. In-order traversal visits left subtree, then root, then right subtree — which, by the BST property, always processes keys in ascending order. This is useful in practice: in-order traversal of a BST produces a sorted sequence in O(n) time."

- question: "Why is insertion order the critical factor in BST performance, and what is the worst-case insertion pattern?"
  type: short-answer
  answer: "BST performance is determined by tree height, and height is determined by insertion order. Each insertion walks from the root to a leaf, placing the new node where it belongs. If keys arrive in sorted (or reverse-sorted) order, each new key is always the largest (or smallest) so far, so it always extends the rightmost (or leftmost) chain. The tree degenerates into a linked list with height n, making all operations O(n). Random insertion order tends to produce a roughly balanced tree with O(log n) height on average, but this is not guaranteed."
  explanation: "This is why unbalanced BSTs are suitable for random data but dangerous for sorted or nearly-sorted data — a common real-world case. Self-balancing trees (AVL, red-black) fix this by performing rotations after insertions to maintain bounded height, sacrificing a constant overhead in exchange for worst-case O(log n) guarantees."
```

## Explainer

You already understand binary trees — each node has at most two children — and you know how to traverse them in various orders. A **binary search tree** adds one powerful constraint: for every node, all keys in its left subtree are smaller and all keys in its right subtree are larger. This is the same principle behind binary search on a sorted array, but embedded in a tree structure that supports efficient insertions and deletions — something sorted arrays cannot do without shifting elements.

To search a BST, start at the root and compare your target to the current node's key. If the target is smaller, go left; if larger, go right; if equal, you have found it. Each comparison eliminates an entire subtree, just as each step of binary search on an array eliminates half the remaining elements. The time this takes is proportional to the **height** h of the tree. For a balanced tree with n nodes, h is O(log n), giving you the same logarithmic search time as binary search. Insertion works similarly: walk down the tree using the same comparison logic until you reach a null pointer, then attach the new node there. The tree grows from the leaves.

Deletion is where things get interesting. Removing a leaf is trivial — just detach it. Removing a node with one child is almost as easy — replace the node with its child. But removing a node with **two children** requires finding a replacement that preserves the BST property. The standard approach is to find the node's **in-order successor** (the smallest key in its right subtree, which is the leftmost node in that subtree) or its **in-order predecessor** (the largest key in its left subtree). You copy that successor's key into the node being deleted, then delete the successor itself — which, by construction, has at most one child, reducing to an easier case.

The critical weakness of a basic BST is that its shape — and therefore its performance — depends entirely on the order of insertions. Insert the keys 1, 2, 3, 4, 5 in order, and you get a straight chain leaning right, with height n and O(n) operations — no better than a linked list. Insert them in the order 3, 1, 5, 2, 4, and you get a nicely balanced tree with height O(log n). Random insertions tend to produce roughly balanced trees on average, but the worst case is devastating. This vulnerability is exactly why **self-balancing BSTs** like AVL trees and red-black trees exist: they add rotation operations after insertions and deletions to guarantee O(log n) height regardless of insertion order. Understanding the basic BST's strengths and weaknesses is essential context for appreciating why those balancing mechanisms are needed.
