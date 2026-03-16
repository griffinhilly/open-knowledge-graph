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

## Explainer

You already know that a singly linked list is a chain of nodes where each node holds a value and a pointer to the next node. Advanced operations on linked lists are really exercises in thinking carefully about what happens when you rearrange those pointers. The simplest example is **reversal**: to reverse a singly linked list in place, you walk through the list and, at each node, redirect its `next` pointer to point backward instead of forward. You maintain three references — the previous node, the current node, and the next node — so that you never lose access to the rest of the list while rewiring. After one pass through all n nodes, the old tail becomes the new head.

**Cycle detection** addresses a subtle problem: what if a linked list's tail points back to some earlier node, forming a loop? You cannot simply traverse the list looking for `null` because you will loop forever. Floyd's tortoise-and-hare algorithm solves this elegantly using two pointers that start at the head. The **slow pointer** advances one node per step; the **fast pointer** advances two nodes per step. If there is no cycle, the fast pointer reaches `null` and you are done. If there is a cycle, the fast pointer eventually "laps" the slow pointer and they meet inside the loop. The mathematical insight is that the distance between the two pointers shrinks by exactly one node per step once both are inside the cycle, so a meeting is guaranteed in O(n) time with O(1) extra space — no hash set needed.

**Merging two sorted linked lists** combines your understanding of pointer manipulation with comparison logic. You compare the heads of both lists, pick the smaller value, advance that list's pointer, and attach the chosen node to a growing result list. This is the same logic as the merge step in merge sort, but performed on linked structures instead of arrays. The key detail is using a dummy head node for the result list so you do not need to special-case the first attachment.

Finding the **Nth node from the end** uses another two-pointer technique. Start both pointers at the head, advance the first pointer N steps ahead, then move both pointers forward together one step at a time. When the first pointer reaches `null`, the second pointer is exactly at the Nth node from the end. This works because the two pointers maintain a fixed gap of N nodes throughout the traversal. All of these operations share a common theme: by maintaining just a few well-chosen pointer variables, you can achieve complex structural transformations in a single pass without extra data structures.
