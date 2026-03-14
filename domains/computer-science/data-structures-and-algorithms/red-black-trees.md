---
id: red-black-trees
title: Red-Black Trees
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: binary-search-trees
  type: hard
- id: tree-node-structure-properties
  type: soft
tags:
- red-black-trees
- self-balancing
- binary-search
- balancing
- rotations
stage: formal-systems
status: draft
---

# Red-Black Trees

## Core Idea
Red-black trees are self-balancing binary search trees where each node is colored red or black, subject to five invariants: root is black, leaves are black, red nodes have only black children, all paths have equal black-node counts, and no two consecutive red nodes exist. These properties guarantee O(log n) height while requiring fewer rotations than AVL trees during insertion and deletion.

## How It's Best Learned
Study the five properties and understand why they imply logarithmic height (the proof is subtle). Trace insertion with recoloring and rotations. Compare to AVL trees: red-black has fewer rebalancing operations but is less tightly balanced. Implement insertion algorithm carefully.

## Common Misconceptions
- Red-black properties directly imply height bounds (they do, but the proof requires careful analysis). - Red-black trees are always better than AVL (red-black has fewer rotations; AVL is more balanced; choice depends on use case).
