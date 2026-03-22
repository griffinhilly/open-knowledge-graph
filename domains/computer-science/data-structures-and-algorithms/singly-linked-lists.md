---
id: singly-linked-lists
title: Singly Linked Lists
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-indexed-collections
  type: hard
- id: algorithm-design-basics
  type: soft
builds-toward:
- doubly-linked-lists
- stacks-data-structure
- queues-data-structure
tags:
- linked-lists
- pointers
- nodes
- sequential
- insertion
- deletion
stage: formal-systems
status: draft
---

# Singly Linked Lists

## Core Idea
A singly linked list is a sequence of nodes where each node holds a value and a single pointer to the next node, forming a unidirectional chain. Unlike arrays, linked lists enable O(1) insertion and deletion at any location if you possess a pointer to that location, but random access is O(n). This makes them ideal for applications with frequent insertions/deletions and unknown size.

## How It's Best Learned
Draw nodes and pointers visually; trace insertion and deletion step-by-step, carefully managing pointer updates. Implement core operations (insert, delete, search, reverse) from scratch, paying close attention to edge cases like inserting at the head or into an empty list.

## Common Misconceptions
- Singly linked lists are always faster than arrays (they're not; arrays excel at random access and cache locality). - You can insert anywhere in O(1) without a pointer (false; you must have a pointer to the location; finding it costs O(n)).

## Questions

```yaml
- question: "A developer claims: 'Linked lists are always faster than arrays for insertion because you just adjust a pointer instead of shifting elements.' What is the most important qualification missing from this claim?"
  type: multiple-choice
  options:
    - "Arrays are actually faster for insertion at all positions because of cache locality"
    - "Pointer adjustment is itself O(n) because every subsequent node must be updated"
    - "Linked list insertion is O(1) only if you already hold a pointer to the insertion location — traversing to find that location costs O(n)"
    - "Linked lists cannot perform insertion; they can only append to the end"
  answer: 2
  explanation: "The O(1) insertion claim is technically correct but practically misleading. Two pointer assignments insert a node in constant time — but only after you're already at the right position. If you start from the head and need to insert at position k, you must walk k nodes first: O(k) traversal + O(1) insertion. The total cost is O(n) in the worst case, matching array insertion. The advantage of linked lists is real only when you already hold a pointer to the target location."

- question: "Which operation takes the same time complexity in both a singly linked list and an unsorted array of equal length?"
  type: multiple-choice
  options:
    - "Accessing the element at index k"
    - "Inserting an element at a known pointer/position"
    - "Searching for a specific value by scanning all elements"
    - "Removing the first element"
  answer: 2
  explanation: "Searching by value requires examining each element in sequence until a match is found: O(n) for both structures in the worst case. Random access (option A) is O(1) for arrays but O(n) for linked lists. Insertion at a known location is O(1) for linked lists but O(n) for arrays due to shifting — except at the end. Removing the first element is O(1) for linked lists (update head) but O(n) for arrays (shift everything left)."

- question: "Inserting a new node at the head of a singly linked list is O(1) regardless of how many nodes the list contains."
  type: true-false
  answer: true
  explanation: "Head insertion requires exactly three steps: create a new node, set its next pointer to the current head, update the head pointer to the new node. None of these steps depend on the list's length — you never traverse any existing nodes. This constant-time head operation makes singly linked lists a natural foundation for stacks."

- question: "Singly linked lists are more cache-friendly than arrays when iterating through all elements, because nodes can be allocated in memory-optimal locations."
  type: true-false
  answer: false
  explanation: "Arrays store elements contiguously in memory, so the CPU can prefetch upcoming elements efficiently — accessing array[i] often brings array[i+1], array[i+2], etc. into cache automatically. Linked list nodes are allocated independently and can be scattered anywhere in memory. Traversing a linked list causes frequent cache misses as each node access may require fetching a new cache line. For sequential iteration, arrays are significantly faster in practice despite the same O(n) asymptotic complexity."

- question: "Why is O(1) insertion sometimes misleading as an advantage of linked lists over arrays?"
  type: short-answer
  answer: "O(1) insertion assumes you already hold a pointer to the insertion location. If you must first traverse the list to find that location, the traversal costs O(n), making the total operation O(n) — the same as shifting elements in an array. The O(1) advantage is real only when you already have the right pointer, such as when inserting at the head or maintaining a tail pointer."
  explanation: "The constant-time insertion claim is asymptotically accurate for the insertion step itself, but it ignores the cost of positioning. In practice, the choice between arrays and linked lists should be based on whether the workload involves known-pointer insertions (linked lists win) or predominantly indexed access and iteration (arrays win due to cache locality)."
```

## Explainer

You already know arrays: a contiguous block of memory where elements sit side by side, accessible by index in O(1). Arrays are powerful, but they have a structural limitation — inserting or deleting an element in the middle requires shifting all subsequent elements, which costs O(n). A **singly linked list** solves this by abandoning contiguous storage entirely. Instead, each element lives in its own **node**, a small container that holds two things: the data value and a **pointer** (or reference) to the next node. The last node's pointer is null, marking the end of the list. A separate **head pointer** tells you where the list begins.

This pointer-based structure means insertion and deletion are fundamentally different operations than in arrays. To insert a new node after a given node, you create the new node, set its next pointer to the given node's next, then update the given node's next pointer to the new node. Two pointer assignments — O(1) work, no shifting. Deletion is similar: to remove a node, you update its predecessor's next pointer to skip over it. The critical caveat is that you need a pointer to the right location first. If you only have the head pointer and want to insert at position k, you must walk k nodes to get there — O(k) traversal followed by O(1) insertion.

The head of the list is a special case worth internalizing. Inserting at the head is always O(1): create a new node, point it at the current head, update head. Deleting the head is also O(1): move head to head.next. This makes singly linked lists a natural foundation for **stacks** (push and pop at the head) and for building **queues** when combined with a tail pointer. Edge cases like operating on an empty list (head is null) or a single-element list are where most bugs occur — always check for null before dereferencing.

The tradeoff against arrays is real and important. Linked lists sacrifice **random access** — there is no way to jump to the 50th element without traversing 49 nodes. They also sacrifice **cache locality** — nodes are scattered across memory, so traversing them causes frequent cache misses on modern hardware. Arrays, by contrast, store elements contiguously, which means the CPU can prefetch upcoming elements efficiently. For workloads dominated by iteration or indexed access, arrays win. For workloads dominated by frequent insertions and deletions at known positions, or where the collection size is unpredictable, linked lists earn their place.
