---
id: linked-list-advanced-operations-cycle-detection
title: 'Linked-List Advanced Operations: Reversal, Cycle Detection, Merging'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: linked-list-singly-doubly-circular
  type: hard
tags:
- linked-list
- algorithms
- operations
stage: formal-systems
status: draft
---

# Linked-List Advanced Operations: Reversal, Cycle Detection, Merging

## Core Idea
Advanced linked-list operations—reversal, cycle detection (Floyd's tortoise-and-hare), merging, and finding the Nth node—require careful pointer manipulation. These are classic interview and DSA problems testing pointer reasoning.

## Questions

```yaml
- question: "You need to detect whether a singly linked list contains a cycle. Compared to tracking visited nodes in a hash set, what is the key advantage of Floyd's tortoise-and-hare algorithm?"
  type: multiple-choice
  options:
    - "It is faster — Floyd's runs in O(log n) time versus the hash set's O(n)"
    - "It uses O(1) space rather than O(n) space, with the same O(n) time guarantee"
    - "It works for doubly linked lists but the hash set approach does not"
    - "It detects cycles in one pass, while the hash set approach requires two passes"
  answer: 1
  explanation: "Both approaches run in O(n) time. The decisive advantage of Floyd's algorithm is space: the hash set stores up to n visited nodes (O(n) space), while Floyd's uses only two pointer variables regardless of list length (O(1) space). Options A and D are incorrect — Floyd's is not faster asymptotically, and both approaches complete in a single traversal."

- question: "In Floyd's cycle detection algorithm, once both the slow and fast pointers are inside the cycle, what mathematical property guarantees they will eventually meet?"
  type: multiple-choice
  options:
    - "The fast pointer eventually slows down to match the speed of the slow pointer"
    - "The gap between the two pointers decreases by exactly one node per step, so they must converge"
    - "The fast pointer reverses direction when it reaches the loop's entry point"
    - "The two pointers are guaranteed to start at the same position inside the cycle"
  answer: 1
  explanation: "Once both pointers are in the cycle, consider the distance between them. Each step, the slow pointer advances 1 node and the fast pointer advances 2, so the gap closes by 1 node per step. This is a deterministic countdown — the pointers cannot 'skip over' each other because the gap decreases by exactly 1 each step, not 2. They must meet in at most cycle_length steps."

- question: "In Floyd's cycle detection algorithm, if the linked list has no cycle, the fast pointer will reach null before the slow pointer does."
  type: true-false
  answer: true
  explanation: "The fast pointer advances two nodes per step while the slow pointer advances one. On a finite acyclic list, the fast pointer reaches the end in roughly n/2 steps while the slow pointer has only covered n/2 nodes. Since the fast pointer hits null first, this is the correct termination condition for the 'no cycle' case — you don't need to wait for the slow pointer."

- question: "Floyd's tortoise-and-hare algorithm requires O(n) extra space because it must track how many nodes each pointer has visited."
  type: true-false
  answer: false
  explanation: "Floyd's algorithm uses O(1) extra space — just two pointer variables, regardless of the list's length. It tracks no visited nodes, no counters, and no history. This is precisely its advantage over hash-set-based cycle detection: no auxiliary data structure grows with input size. The O(n) time complexity refers to how long it runs, not how much space it uses."

- question: "When reversing a singly linked list in place, why must you maintain three pointer variables (previous, current, next) rather than just two?"
  type: short-answer
  answer: "Before redirecting current.next to point backward (to previous), you must save the original forward link in a third variable (next). If you redirect current.next first, you lose access to the rest of the list — there is no other way to reach it. The three variables let you: (1) save the next node before rewiring, (2) redirect the current pointer, and (3) advance all three pointers forward. With only two variables you would lose the tail of the list the moment you rewire the first node."
  explanation: "This captures the key constraint of in-place pointer manipulation: rewiring destroys the only link you had to the rest of the list. This same principle applies in merging and other linked-list operations — before you change a pointer, save what it was pointing to. Three pointers is the minimum required for a single-pass reversal."
```

## Explainer

You already know that a singly linked list is a chain of nodes where each node holds a value and a pointer to the next node. Advanced operations on linked lists are really exercises in thinking carefully about what happens when you rearrange those pointers. The simplest example is **reversal**: to reverse a singly linked list in place, you walk through the list and, at each node, redirect its `next` pointer to point backward instead of forward. You maintain three references — the previous node, the current node, and the next node — so that you never lose access to the rest of the list while rewiring. After one pass through all n nodes, the old tail becomes the new head.

**Cycle detection** addresses a subtle problem: what if a linked list's tail points back to some earlier node, forming a loop? You cannot simply traverse the list looking for `null` because you will loop forever. Floyd's tortoise-and-hare algorithm solves this elegantly using two pointers that start at the head. The **slow pointer** advances one node per step; the **fast pointer** advances two nodes per step. If there is no cycle, the fast pointer reaches `null` and you are done. If there is a cycle, the fast pointer eventually "laps" the slow pointer and they meet inside the loop. The mathematical insight is that the distance between the two pointers shrinks by exactly one node per step once both are inside the cycle, so a meeting is guaranteed in O(n) time with O(1) extra space — no hash set needed.

**Merging two sorted linked lists** combines your understanding of pointer manipulation with comparison logic. You compare the heads of both lists, pick the smaller value, advance that list's pointer, and attach the chosen node to a growing result list. This is the same logic as the merge step in merge sort, but performed on linked structures instead of arrays. The key detail is using a dummy head node for the result list so you do not need to special-case the first attachment.

Finding the **Nth node from the end** uses another two-pointer technique. Start both pointers at the head, advance the first pointer N steps ahead, then move both pointers forward together one step at a time. When the first pointer reaches `null`, the second pointer is exactly at the Nth node from the end. This works because the two pointers maintain a fixed gap of N nodes throughout the traversal. All of these operations share a common theme: by maintaining just a few well-chosen pointer variables, you can achieve complex structural transformations in a single pass without extra data structures.
