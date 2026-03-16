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
builds-toward:
- avl-trees
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

## Explainer

You already understand binary trees — each node has at most two children — and you know how to traverse them in various orders. A **binary search tree** adds one powerful constraint: for every node, all keys in its left subtree are smaller and all keys in its right subtree are larger. This is the same principle behind binary search on a sorted array, but embedded in a tree structure that supports efficient insertions and deletions — something sorted arrays cannot do without shifting elements.

To search a BST, start at the root and compare your target to the current node's key. If the target is smaller, go left; if larger, go right; if equal, you have found it. Each comparison eliminates an entire subtree, just as each step of binary search on an array eliminates half the remaining elements. The time this takes is proportional to the **height** h of the tree. For a balanced tree with n nodes, h is O(log n), giving you the same logarithmic search time as binary search. Insertion works similarly: walk down the tree using the same comparison logic until you reach a null pointer, then attach the new node there. The tree grows from the leaves.

Deletion is where things get interesting. Removing a leaf is trivial — just detach it. Removing a node with one child is almost as easy — replace the node with its child. But removing a node with **two children** requires finding a replacement that preserves the BST property. The standard approach is to find the node's **in-order successor** (the smallest key in its right subtree, which is the leftmost node in that subtree) or its **in-order predecessor** (the largest key in its left subtree). You copy that successor's key into the node being deleted, then delete the successor itself — which, by construction, has at most one child, reducing to an easier case.

The critical weakness of a basic BST is that its shape — and therefore its performance — depends entirely on the order of insertions. Insert the keys 1, 2, 3, 4, 5 in order, and you get a straight chain leaning right, with height n and O(n) operations — no better than a linked list. Insert them in the order 3, 1, 5, 2, 4, and you get a nicely balanced tree with height O(log n). Random insertions tend to produce roughly balanced trees on average, but the worst case is devastating. This vulnerability is exactly why **self-balancing BSTs** like AVL trees and red-black trees exist: they add rotation operations after insertions and deletions to guarantee O(log n) height regardless of insertion order. Understanding the basic BST's strengths and weaknesses is essential context for appreciating why those balancing mechanisms are needed.
