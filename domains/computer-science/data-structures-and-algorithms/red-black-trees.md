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

## Questions

```yaml
- question: "Which pair of red-black properties together directly guarantees that tree height is O(log n)?"
  type: multiple-choice
  options:
    - "Root is black AND every null leaf is black"
    - "Red nodes have only black children AND all root-to-leaf paths have equal black-node counts"
    - "All nodes are colored AND no two consecutive red nodes exist on any path"
    - "Root is black AND red nodes have only black children"
  answer: 1
  explanation: "Property 5 (equal black-height on all paths) ensures the 'shortest' root-to-null path has some black count b. Property 4 (no consecutive reds) limits the 'longest' path to alternating red-black nodes: length ≤ 2b. Since all paths have the same black-height and b ≥ log₂(n+1)/2, total height is bounded by 2 log₂(n+1) = O(log n). Without both properties together the height bound breaks down."

- question: "A team is choosing between an AVL tree and a red-black tree for a container that undergoes frequent insertions and deletions with occasional lookups. Which is the better choice and why?"
  type: multiple-choice
  options:
    - "AVL tree — it has strictly tighter balance and therefore shorter height for the same node count"
    - "Red-black tree — it requires fewer rotations per modification, making insertions and deletions cheaper"
    - "AVL tree — red-black trees degenerate under many insertions"
    - "Red-black tree — it guarantees O(1) average lookup time"
  answer: 1
  explanation: "Red-black trees require at most 2 rotations per insertion and 3 per deletion, whereas AVL trees may rotate at every level up to O(log n) per operation to maintain their stricter balance invariant. For workloads dominated by modifications, this makes red-black trees faster in practice. AVL trees are preferred when pure lookups vastly dominate because their tighter balance keeps the tree shorter. The choice depends on the access pattern — neither is universally superior."

- question: "A new node is always inserted as red in a red-black tree because inserting it as black would immediately violate the black-height invariant."
  type: true-false
  answer: true
  explanation: "Property 5 requires every root-to-leaf path to have the same number of black nodes. Adding a black node on the new path increases its black count while leaving all other paths unchanged — an immediate violation. Inserting red avoids this, though it may create a consecutive-reds violation (property 4) if the parent is also red. A property-4 violation is fixable by local recoloring or at most two rotations; a property-5 violation would require rebalancing every other path in the tree."

- question: "Red-black trees are more strictly balanced than AVL trees, so their height is always shorter for the same number of nodes."
  type: true-false
  answer: false
  explanation: "AVL trees are more strictly balanced: they maintain the invariant that child subtree heights differ by at most 1, keeping height close to log₂(n). Red-black trees allow a longer worst-case height (up to 2 log₂(n+1)) because paths can alternate red and black nodes. Red-black trees trade some lookup efficiency for cheaper modification operations. This is why standard library containers (std::map, Java's TreeMap) typically use red-black trees — modifications are more common than pure lookups in general-purpose use."

- question: "Why does fixing a red-black violation after insertion require at most two rotations, regardless of tree size?"
  type: short-answer
  answer: "The fix works bottom-up: if the inserted red node's uncle is also red, the violation is resolved by recoloring alone (uncle and parent turn black; grandparent turns red) and the problem may propagate upward. If the uncle is black, the violation is fully resolved in one or two rotations plus recoloring at the current level without further propagation. The rotation cases always terminate immediately, so rotations total at most two per insertion regardless of how much recoloring propagates."
  explanation: "This bounded rotation count is the key practical advantage over AVL trees, which may require a rotation at each level on the way back up. Red-black trees' more relaxed invariant (black-height equality rather than height-difference ≤ 1) means most violations resolve with local recoloring that can propagate upward, requiring rotations only at the boundary cases, and never more than twice per insertion."
```

## Explainer

You already know that a binary search tree (BST) keeps elements in sorted order, allowing O(h) search, insertion, and deletion where h is the tree's height. The problem is that an unbalanced BST can degenerate into a linked list with h = n. A **red-black tree** solves this by attaching a color — red or black — to every node and enforcing invariants that prevent the tree from becoming too lopsided. The result is a guaranteed height of at most 2 log₂(n + 1), ensuring O(log n) worst-case operations.

The five **red-black properties** are: (1) every node is either red or black, (2) the root is black, (3) every null leaf is considered black, (4) a red node's children must both be black (no two consecutive reds on any path), and (5) every path from a given node to any of its descendant null leaves contains the same number of black nodes. Property 5 is the most important — it defines the **black-height** of the tree. Because no path can have consecutive red nodes (property 4) and all paths have the same black-height (property 5), the longest possible path (alternating red-black-red-black...) is at most twice the length of the shortest path (all black). This 2:1 ratio is what bounds the height.

When you insert a new node, you color it red (to preserve black-height) and then fix any violations of property 4 — the "no consecutive reds" rule. The fix involves **recoloring** nodes and performing **rotations**. A rotation is a local restructuring that shifts one node up and another down while preserving the BST ordering. There are two cases: if the new node's uncle (parent's sibling) is red, you can fix the violation by recoloring without rotation. If the uncle is black, you perform one or two rotations plus recoloring. The fix propagates upward at most O(log n) levels but requires at most two rotations total per insertion — this is fewer than AVL trees, which may rotate at every level.

Deletion is more complex but follows the same pattern: remove the node using standard BST deletion, then fix any black-height violations with recoloring and rotations (at most three per deletion). The practical significance of red-black trees is enormous — they are the implementation behind `std::map` and `std::set` in C++, Java's `TreeMap` and `TreeSet`, and the Linux kernel's process scheduler. They offer a pragmatic balance: slightly less rigidly balanced than AVL trees (so lookups may touch a few more nodes), but with cheaper insertions and deletions due to fewer rotations. For workloads dominated by modifications rather than pure lookups, red-black trees are typically the better choice.
