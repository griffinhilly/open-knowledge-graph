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

## Questions

```yaml
- question: "After inserting a node, an AVL tree has a node A with balance factor -2 and A's right child B has balance factor -1. Which rotation fixes this?"
  type: multiple-choice
  options:
    - "Right rotation at A"
    - "Left rotation at A"
    - "Left rotation at B, then right rotation at A"
    - "Right rotation at B, then left rotation at A"
  answer: 1
  explanation: "A balance factor of -2 at A with B's right subtree being heavy is an RR case (right-right imbalance). A single left rotation at A lifts B up to replace A, which becomes B's left child. A right rotation at A would be used for LL cases. Double rotations are needed only for LR/RL cases where the imbalance zigzags."

- question: "Why do LR and RL imbalances require double rotations rather than a single rotation?"
  type: multiple-choice
  options:
    - "Because a single rotation would make the tree taller"
    - "Because a single rotation would violate the BST ordering property"
    - "Because a single rotation converts the zigzag into the mirror imbalance rather than fixing it"
    - "Because double rotations are faster to execute for these cases"
  answer: 2
  explanation: "In an LR case, the node is left-heavy but its left child is right-heavy — a zigzag pattern. Applying a single right rotation at the top just transforms the LR into an RL imbalance, swapping the problem. The fix is to first rotate the left child leftward (converting LR into LL), then rotate the original node rightward. Both single and double rotations preserve BST ordering — that is not the issue."

- question: "AVL trees guarantee O(log n) worst-case height because after any insertion, at most one rotation is needed to restore balance throughout the tree."
  type: true-false
  answer: true
  explanation: "This is true for insertion: at most one single or double rotation suffices to restore the balance invariant after inserting a node, and that rotation propagates the fix upward so no further rotations are needed. The resulting height bound of at most 1.44·log₂n then guarantees O(log n) operations. (Note: deletion may require O(log n) rotations propagating up, but the height guarantee still holds.)"

- question: "A rotation in an AVL tree changes the inorder traversal sequence of the nodes, which is why it must be applied carefully to avoid corrupting the BST property."
  type: true-false
  answer: false
  explanation: "Rotations are designed specifically to preserve BST ordering — the inorder traversal sequence is unchanged. A left rotation at node A lifts A's right child up while correctly reassigning subtrees so all nodes smaller than the new root remain to its left and all larger nodes remain to its right. The point of rotation is to restructure tree shape while leaving the logical ordering intact. Worrying about BST corruption is misplaced; rotation correctness depends on getting the pointer reassignments right, not on ordering."

- question: "Explain why the LR imbalance case requires a double rotation rather than a single rotation."
  type: short-answer
  answer: "In the LR case, a node is left-heavy but its left child's right subtree causes the imbalance — the path zigzags left then right. A single right rotation lifts the left child to the top, but since that child is right-heavy, the result immediately has an RL imbalance — the problem is mirrored, not solved. The double rotation straightens the zigzag first: a left rotation on the left child converts it to an LL case, then a right rotation on the original node completes the fix, placing the median of the three nodes at the root with balanced subtrees."
  explanation: "Single rotations only work when the heavy subtree is on the 'outside' of the path (LL or RR). When the heavy subtree is on the 'inside' (LR or RL), the path zigzags and a single rotation reverses the direction of the zigzag. The first rotation of the double straightens the path; the second balances it."
```

## Explainer

From binary search trees, you know that search, insertion, and deletion all take time proportional to the tree's height. The problem is that an unbalanced BST can degenerate into a linked list — insert keys 1, 2, 3, 4, 5 in order and you get a chain leaning entirely to the right, with height equal to n and O(n) operations. AVL trees prevent this by enforcing a strict invariant: at every node, the heights of the left and right subtrees differ by at most 1. This **balance factor** (left height minus right height) must always be -1, 0, or +1. When an insertion or deletion violates this invariant, the tree fixes itself through rotations.

A **rotation** is a local restructuring operation that changes parent-child relationships between two or three nodes while preserving the BST ordering property. Consider a right-heavy imbalance where a node's balance factor becomes -2 because its right child's right subtree is too tall (an **RR case**). A **left rotation** lifts the right child up to replace the imbalanced node, which becomes the new left child. The key insight is that this operation is O(1) — it only changes three pointers — yet it reduces the height of the subtree by one, restoring balance. The mirror case (left-heavy, **LL case**) uses a **right rotation** with the symmetric pointer changes.

The trickier cases are **LR** and **RL imbalances**, where the heavy subtree zigzags. If a node is left-heavy but its left child is right-heavy (LR case), a single rotation would not fix the problem — it would just create the mirror imbalance. The solution is a **double rotation**: first rotate the left child leftward to straighten the zigzag into a straight LL case, then rotate the original node rightward. The RL case is the mirror: rotate the right child rightward, then the original node leftward. In all four cases, the result is a balanced subtree with the median of the three involved nodes at the root, and the operation completes in O(1) time.

After each insertion or deletion, the algorithm walks back up the path from the affected node to the root, updating balance factors and performing at most one rotation (for insertion) or O(log n) rotations (for deletion) along the way. Because the tree always stays balanced, its height is guaranteed to be at most 1.44 · log₂(n), which means all operations remain O(log n) in the worst case. This is the fundamental tradeoff AVL trees make: every mutation pays a small constant overhead for balance checking and potential rotation, but in return, no sequence of operations can ever degrade the tree into the O(n) worst case that plagues ordinary BSTs.
