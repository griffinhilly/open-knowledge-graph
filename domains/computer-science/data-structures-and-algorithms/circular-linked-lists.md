---
id: circular-linked-lists
title: Circular Linked Lists
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: singly-linked-lists
  type: hard
builds-toward:
- deques-double-ended-queues
tags:
- linked-lists
- circular
- cycle
- round-robin
stage: formal-systems
status: draft
---

# Circular Linked Lists

## Core Idea
A circular linked list has the last node's next pointer pointing back to the first node, forming a cycle and eliminating the null tail terminator. This structure enables round-robin algorithms to continue indefinitely and is useful for circular buffers, job scheduling queues, and contexts where wraparound is natural.

## How It's Best Learned
Implement traversal carefully—use a sentinel node or counter to avoid infinite loops. Practice merging circular lists and detecting cycles. Implement a simple round-robin scheduler to see the structure in practical action.

## Common Misconceptions
- Circular lists are inherently better than linear lists (they solve specific problems elegantly; linear lists remain simpler and more common).

## Questions

```yaml
- question: "You are traversing a circular linked list using the loop `while (current != null) { current = current.next; }`. What happens?"
  type: multiple-choice
  options:
    - "The loop terminates correctly when it reaches the last node"
    - "The loop runs forever, because no node's next pointer is null"
    - "The loop terminates after visiting half the nodes"
    - "A NullPointerException is thrown on the second pass"
  answer: 1
  explanation: "In a circular linked list, the last node's next pointer points back to the first node — there is no null sentinel. A null-check termination condition will never be satisfied, causing an infinite loop. You must use a different termination strategy: save a reference to the starting node and stop when you return to it, use a sentinel node, or count iterations."

- question: "You need to merge two circular linked lists, given one pointer to any node in each list. What is the minimum time complexity for this operation?"
  type: multiple-choice
  options:
    - "O(n) — you must traverse both lists to find all nodes"
    - "O(n log n) — merging requires sorting the two sequences"
    - "O(1) — swap two next pointers to splice the loops together"
    - "O(n²) — each node in one list must be linked to each node in the other"
  answer: 2
  explanation: "Given a pointer to one node in each circular list, you can merge them in O(1) by swapping two next pointers. Concretely: save A.next and B.next, then set A.next = B's original next and B.next = A's original next. This splices the two loops into one. This is a distinctive advantage of the circular structure — you don't need to find the tail node first, because any node's successor pointer can serve as the splice point."

- question: "Circular linked lists are generally faster than singly linked lists for the same sequential access workload."
  type: true-false
  answer: false
  explanation: "Circular linked lists do not offer faster sequential traversal than singly linked lists. Both require O(n) time to visit all n nodes. The circular structure's advantage is structural convenience for wraparound problems (e.g., round-robin scheduling), not raw speed. For most sequential-access tasks, a singly linked list is simpler and less error-prone, because traversal has a natural null terminator."

- question: "In a round-robin job scheduler implemented with a circular linked list, advancing from the last job in the list automatically brings you back to the first job without any conditional reset logic."
  type: true-false
  answer: true
  explanation: "This is precisely the structural advantage the circular list provides. Because the last node's next pointer points to the first node, following any node's next pointer wraps around to the beginning. A linear list requires detecting null and resetting the pointer to the head; a circular list makes wraparound implicit in the structure itself, which is why it is the natural data structure for round-robin algorithms."

- question: "Why does traversing a circular linked list require a different termination condition than traversing a singly linked list, and what are two valid approaches?"
  type: short-answer
  answer: "A singly linked list ends with a null pointer, so traversal terminates when current == null. A circular list has no null — the last node points back to the first — so that condition never triggers. Two valid approaches: (1) save a reference to the starting node before the loop and stop when you return to it (current == start); (2) use a sentinel node as a permanent marker and stop when you reach the sentinel."
  explanation: "The null sentinel is the normal structural signal that a linear list has ended. Removing it enables wraparound but transfers the termination burden to the programmer. Failing to account for this is the most common bug when first working with circular lists, and it produces infinite loops that are hard to debug because the program doesn't crash — it just never stops."
```

## Explainer

In the singly linked lists you already know, the last node's next pointer is null — it marks the end of the list. A **circular linked list** changes one thing: the last node's next pointer points back to the first node instead of null, forming a closed loop. This simple modification eliminates the concept of "end" and creates a structure that naturally wraps around, which turns out to be exactly what certain problems require.

The most intuitive application is **round-robin scheduling**. Imagine an operating system that gives each of five processes a time slice in rotation: P1, P2, P3, P4, P5, P1, P2, P3, ... With a linear list, when you reach P5 you hit null and must reset your pointer to the head. With a circular list, advancing past P5 automatically brings you back to P1 — the wraparound is built into the structure. The same pattern appears in circular buffers, turn-based game logic, and any scenario where you cycle through a fixed set of items indefinitely.

Traversal is where you must be careful. In a linear list, you iterate until you hit null — a natural stopping condition. In a circular list there is no null, so a naive `while (current != null)` loop runs forever. You need a different termination condition: either keep a reference to your starting node and stop when you return to it, or use a **sentinel node** (a special dummy node that marks the "logical start"), or simply count iterations. Insertion and deletion work much like a regular singly linked list, with one extra consideration: when inserting at the "front" or deleting the node that your external reference points to, you must update the last node's pointer as well to maintain the circular link.

One practical advantage of a circular list is that you can reach any node from any other node — there is no need to maintain a pointer to the head specifically, since traversing far enough from any starting point will visit every node. This property also means that **merging two circular lists** is efficient: given a pointer to any node in each list, you can splice them together in O(1) by swapping two next pointers. Despite these strengths, circular lists are a specialized tool. For most sequential-access problems, a standard singly linked list is simpler and less error-prone. Reach for a circular list when the problem itself is inherently cyclic.
