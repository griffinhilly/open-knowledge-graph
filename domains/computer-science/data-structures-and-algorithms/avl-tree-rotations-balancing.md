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
- avl-tree-rotations-balancing
- balancing
- rotations
- self-balancing
- binary-search
stage: formal-systems
status: validated
---

# AVL Tree Rotations and Balancing

## Core Idea
AVL trees maintain height-balance: the height difference of left and right subtrees at every node is at most 1. When insertion or deletion violates this property, rotations (single or double) restore balance in O(log n) time per operation. This guarantees O(log n) search, insert, and delete regardless of insertion order.

## How It's Best Learned
Draw insertion sequences that trigger imbalance. Trace through single rotations (LL, RR cases) and double rotations (LR, RL cases). Implement rotation operations and rebalancing logic carefully. Understand how balance factors propagate upward during insertion.

## Common Misconceptions
- Rotations cost O(n) (they are O(1) each; O(log n) total per operation). - Every node must have perfect balance (AVL requires only |height difference| ≤ 1).

## Questions

```yaml
- question: "After inserting a node into an AVL tree, a node has a balance factor of +2 and its left child has a balance factor of +1 (left-left case). How many pointer reassignments does the single right rotation require?"
  type: multiple-choice
  options:
    - "O(log n) reassignments, since the rotation propagates up toward the root"
    - "O(n) reassignments, since all nodes below must be updated"
    - "A constant number of pointer reassignments, regardless of tree size"
    - "O(height) reassignments, since each level on the path must be visited"
  answer: 2
  explanation: "Each rotation is O(1) — it reassigns a fixed, constant number of pointers among the three nodes involved and their subtrees. No other nodes need to be visited or updated. This is the central efficiency insight: rotations are cheap per-rotation, which is why AVL trees achieve O(log n) per operation overall. The common misconception that rotations propagate changes down the whole subtree confuses pointer reassignment with value propagation."

- question: "A newly inserted node creates a left-right (LR) imbalance — the violation node's left child's right subtree is too tall. Why does a single right rotation at the violation node fail to fix this?"
  type: multiple-choice
  options:
    - "Because LR imbalances require an O(n) correction pass"
    - "A single rotation at the violation node moves the left child up, but the heavy part (the grandchild) ends up in the wrong position, effectively flipping the imbalance"
    - "Single rotations only restore balance when the tree height is odd"
    - "The LR case means no balanced configuration exists for that subtree"
  answer: 1
  explanation: "In the LR case, the 'heavy' subtree is the left child's right subtree — a zig-zag pattern. Rotating the violation node right promotes the left child, but the grandchild (the actual source of imbalance) ends up in the wrong position and the tree is still unbalanced. The fix is a double rotation: first rotate the left child left (converting LR to LL), then rotate the violation node right. A double rotation is just two single rotations composed — it is still O(1) total."

- question: "Because AVL trees maintain O(log n) height and each rotation is O(1), all three core operations — search, insert, and delete — run in O(log n) worst-case time regardless of insertion order."
  type: true-false
  answer: true
  explanation: "This is the core guarantee of AVL trees. The height is always O(log n) because the balance factor constraint (|height difference| ≤ 1) prevents one-sided degeneration. Search traverses at most O(log n) nodes. Insert applies at most one rotation (single or double) after the O(log n) traversal. Delete may require rotations at multiple ancestors as you walk up, but the path length is bounded by O(log n), and each rotation is O(1). The worst-case O(log n) guarantee holds for all three."

- question: "When a node insertion into an AVL tree causes an imbalance, rotations must be performed at every ancestor node on the path from the new node to the root."
  type: true-false
  answer: false
  explanation: "For insertion, at most one rotation (single or double) at the lowest violation point fully restores balance — no further rotations are needed at higher ancestors. The reason: a rotation restores the subtree to its pre-insertion height, so no ancestor's balance factor changes after the rotation. This distinguishes insertion from deletion: after deletion, rotations may propagate upward through multiple ancestors because the height reduction can continue affecting ancestors above the rotation point."

- question: "Explain why the AVL balance requirement (|height difference| ≤ 1 at every node) guarantees O(log n) tree height, and why this matters for performance."
  type: short-answer
  answer: "The balance requirement prevents any subtree from becoming much taller than its sibling, forcing the tree to 'fan out' at every level. The minimum-size AVL tree of height h contains at least F(h+2) − 1 nodes (where F is Fibonacci), and Fibonacci numbers grow exponentially in h. Therefore h is at most ~1.44 log₂(n). Without the balance constraint, a BST can degenerate into a chain of height n, making every operation O(n)."
  explanation: "The practical importance is that O(log n) vs O(n) is the difference between a structure that scales and one that doesn't. For n = 1,000,000, log₂(n) ≈ 20 but n = 1,000,000. The balance constraint ensures that even in adversarial insertion sequences (which would produce a chain in a plain BST), the AVL tree stays shallow. The cost is the bookkeeping — storing balance factors and checking after every insert/delete — but this constant overhead is worth the guarantee."
```

## Explainer

From your work with binary search trees, you know the core problem: a BST gives you O(log n) operations only when the tree is reasonably balanced, but ordinary insertions can produce a lopsided tree — in the worst case, a straight chain with O(n) height. An **AVL tree** (named after Adelson-Velsky and Landis, who invented it in 1962) is a BST that fixes this by enforcing a strict balance rule and using **rotations** to restore it whenever an insertion or deletion causes a violation.

The balance rule is simple: at every node, the heights of the left and right subtrees may differ by at most 1. Each node stores a **balance factor** — the height of its left subtree minus the height of its right subtree — which must be −1, 0, or +1. After you insert a new node (using standard BST insertion), you walk back up the path from the new node to the root, updating balance factors. If any node's balance factor becomes −2 or +2, that node is the **violation point**, and you apply a rotation to fix it.

There are four cases, but they reduce to two patterns. If the imbalance is "left-left" (the left child's left subtree is too tall) or "right-right" (symmetric), a **single rotation** fixes it. Think of it like straightening a bent arm: you rotate the violation node down and its heavy child up, and the BST ordering property is preserved because you are only rearranging the relative positions of three nodes and their subtrees. If the imbalance is "left-right" or "right-left" — a zig-zag pattern — a single rotation would just flip the imbalance to the other side. Instead, you apply a **double rotation**: first rotate the grandchild up to eliminate the zig-zag, then apply the single rotation. In code, a double rotation is literally two single rotations composed.

The critical insight is that each rotation is **O(1)** — it reassigns a constant number of pointers regardless of tree size. After an insertion, at most one rotation (single or double) at the lowest violation point is needed to restore balance for the entire tree. After a deletion, you may need to rotate at multiple ancestors as you walk up, but the number of rotations is bounded by the height, which is O(log n). This is what gives AVL trees their guarantee: because the height is always O(log n), and each rotation is O(1), every search, insert, and delete operation takes O(log n) time in the worst case, regardless of what order you inserted the keys. The tradeoff compared to a plain BST is the bookkeeping — maintaining balance factors and checking for violations — but the payoff is eliminating the possibility of degeneration entirely.
