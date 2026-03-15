---
id: trees-and-tree-properties
title: Trees and Forest Structures
domain: mathematics
course: discrete-math
prerequisites:
- id: connectivity-components-discrete
  type: hard
- id: trees-in-graph-theory
  type: soft
builds-toward:
- minimum-spanning-trees-discrete
- graph-traversal-algorithms
tags:
- trees
- forests
- leaves
- parent-child
- properties
stage: formal-systems
status: draft
---

# Trees and Forest Structures

## Core Idea
A tree is a connected acyclic graph. It has exactly n−1 edges for n vertices, a unique path between any two vertices, and no cycles. Trees generalize to forests (disjoint unions of trees). Rooted trees model hierarchies, with roots at top and leaves at bottom.

## How It's Best Learned
Recognize that any two of these properties imply the third: connected, n−1 edges, acyclic. Build spanning trees of given graphs. Use tree terminology: parent, child, ancestor, depth, height.

## Common Misconceptions
Not all trees are rooted; an unrooted tree has no distinguished root. A path graph and a star graph are both trees but very different structurally.
