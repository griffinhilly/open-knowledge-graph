---
id: tree-traversals
title: Tree Traversals
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-trees
  type: hard
- id: stacks-data-structure
  type: soft
- id: queues-data-structure
  type: soft
builds-toward:
- binary-search-trees
- depth-first-search
- breadth-first-search
tags:
- traversal
- inorder
- preorder
- postorder
- level-order
stage: formal-systems
status: validated
---

# Tree Traversals

## Core Idea
Tree traversal visits every node in a tree exactly once. Depth-first traversals include inorder (left → root → right), preorder (root → left → right), and postorder (left → right → root); each visits nodes in a different order suited to different applications. Breadth-first (level-order) traversal visits nodes level by level using a queue. Inorder traversal of a binary search tree yields elements in sorted order, making it especially useful for validation and enumeration.

## How It's Best Learned
Implement all four traversals both recursively and iteratively (using an explicit stack or queue). For each, predict the output order by hand before running the code, then verify.

## Common Misconceptions
- Recursive implementations are elegant but can cause stack overflow on very deep or degenerate trees; iterative versions using explicit stacks are safer for production use.
- Inorder traversal yields sorted output ONLY for binary search trees, not arbitrary binary trees.

## Questions

```yaml
- question: "You need to delete all nodes in a binary tree, freeing memory in an order that ensures children are always deleted before their parent. Which traversal should you use?"
  type: multiple-choice
  options:
    - "Preorder (root, left, right) — visit parent first, then children"
    - "Inorder (left, root, right) — balanced between parent and children"
    - "Postorder (left, right, root) — visit both subtrees before the parent"
    - "Level-order — process nodes top to bottom by level"
  answer: 2
  explanation: "Postorder visits both child subtrees before the current node, which is exactly what's needed to safely delete a tree: you process and free all children before freeing the parent. Using preorder would free parents before children, creating dangling pointers. This is the canonical example of why traversal order matters: the application requirement (children before parents) maps directly onto postorder's structure."

- question: "You perform an inorder traversal on a binary tree and get the sequence: 15, 7, 22, 3, 11. What can you conclude?"
  type: multiple-choice
  options:
    - "Nothing — inorder traversal of an arbitrary binary tree tells you nothing about whether it is a BST"
    - "The tree is a valid BST, because inorder traversal always produces sorted output"
    - "The tree is not a valid BST, because the output is not in sorted order"
    - "You need to also check the preorder output before drawing any conclusion"
  answer: 2
  explanation: "Inorder traversal of a binary search tree always produces sorted output. Since this output (15, 7, 22, 3, 11) is not sorted, the tree violates BST ordering. This question targets the misconception in option B: inorder produces sorted output ONLY for BSTs, not arbitrary binary trees. Knowing this, an unsorted inorder output is definitive proof the tree is not a valid BST."

- question: "Inorder traversal of any binary tree produces elements in sorted order."
  type: true-false
  answer: false
  explanation: "Inorder traversal produces sorted output ONLY for binary search trees, where the BST property guarantees the left subtree contains values smaller than the root and the right subtree contains larger values. For an arbitrary binary tree with no ordering constraint, inorder traversal simply visits left subtree, then root, then right subtree — the output order depends entirely on how values happen to be arranged, which may not be sorted."

- question: "Preorder traversal visits a parent node before its children, which makes it naturally suited for copying a tree or producing a top-down representation of its structure."
  type: true-false
  answer: true
  explanation: "Preorder's root-first order means you process every parent before its children, preserving the hierarchical structure from top to bottom. To copy a tree, you create each node before attaching its children — exactly the order preorder provides. Similarly, prefix expressions (operators before operands) in expression trees correspond to preorder traversal. This contrasts with postorder (bottom-up, useful for aggregates) and inorder (interleaves root between subtrees)."

- question: "What determines which depth-first traversal (preorder, inorder, or postorder) to use, and why does the order matter?"
  type: short-answer
  answer: "The choice depends on the required relationship between a node and its children in the application. Preorder (root first) is used when a parent must be processed before its children — copying a tree, serializing structure, prefix expressions. Inorder (left, root, right) is used for sorted enumeration of a BST. Postorder (children first) is used when children must be processed before their parent — deletion, computing subtree aggregates like height or size."
  explanation: "The three traversals differ only in when the current node is visited relative to its children, but this single difference has significant practical consequences. The traversal order directly controls the sequencing of operations, and choosing the wrong order can produce incorrect results — freeing a parent before its children, or failing to get sorted output from a BST."
```

## Explainer

You already understand binary trees — each node has at most two children, called left and right. A **tree traversal** is a systematic way to visit every node exactly once, and the order in which you visit them determines what the traversal is useful for. There are four standard traversals, three depth-first and one breadth-first, and each answers a different question about the tree's contents.

The three **depth-first** traversals differ only in when they process the current node relative to its children. **Preorder** (root, left, right) visits the current node first, then recurses into the left subtree, then the right. This naturally produces a top-down view — you see parents before children, making preorder ideal for copying a tree or producing a prefix representation of an expression. **Inorder** (left, root, right) recurses into the left subtree first, then visits the current node, then the right subtree. For a binary search tree, this visits nodes in ascending sorted order — the left subtree contains smaller values, the root is next, and the right subtree contains larger values. **Postorder** (left, right, root) recurses into both subtrees before visiting the current node, giving a bottom-up view — you process children before parents, making it natural for computing aggregate properties (like subtree size or height) and for safely deleting a tree.

**Breadth-first** (level-order) traversal visits all nodes at depth 0, then depth 1, then depth 2, and so on. Instead of recursion, it uses a queue: enqueue the root, then repeatedly dequeue a node, process it, and enqueue its children. This produces a left-to-right, top-to-bottom sweep of the tree and is useful when you need to process nodes by level — for example, finding the shallowest node satisfying some condition, or printing a tree level by level.

The recursive implementations are concise — each depth-first traversal is about three lines of code. But recursion uses the call stack, and a deeply unbalanced tree (essentially a linked list) can cause stack overflow. The **iterative** versions use an explicit stack (for depth-first) or queue (for breadth-first), giving you direct control over memory. For iterative inorder, you push nodes as you go left, pop when there's nothing left to push, process the popped node, then move right. Mastering both recursive and iterative forms is important because the iterative versions reveal what the recursion is actually doing — managing a frontier of nodes yet to be visited — which is the same pattern you will encounter in graph traversal algorithms like depth-first search and breadth-first search.
