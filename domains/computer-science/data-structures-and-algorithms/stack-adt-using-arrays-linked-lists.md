---
id: stack-adt-using-arrays-linked-lists
title: 'Stack ADT: Array and Linked-List Implementations'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: arrays-and-indexed-collections
  type: hard
- id: linked-lists
  type: hard
builds-toward:
- stack-infix-postfix-expression-evaluation
tags:
- stack
- adt
- data-structure
stage: formal-systems
status: draft
---

# Stack ADT: Array and Linked-List Implementations

## Core Idea
A stack is a LIFO (Last-In-First-Out) data structure supporting push (insert) and pop (remove) operations. It can be implemented with an array (using an index pointer) or a linked list (using a head pointer), each with different space/time tradeoffs.

## How It's Best Learned
Implement a stack in your language of choice. Push and pop elements, and trace the state after each operation. Compare array vs. linked-list implementations: array is cache-friendly but risks overflow; linked list is flexible but uses extra pointers.

## Common Misconceptions
- A stack must be empty initially (false—it starts empty by definition).
- Stack overflow is only a memory issue (it's also a logic error—trying to pop from empty).
- Array-based stacks are always slower because of reallocation (amortized analysis shows they're O(1)).

## Questions

```yaml
- question: "An array-based stack doubles its capacity when full. A sequence of 1024 pushes is performed starting from capacity 1. Approximately how many total element-copy operations occur across all resize events?"
  type: multiple-choice
  options:
    - "1024 copies — each push copies one element"
    - "About 2048 copies total — each element is copied on average about twice, giving amortized O(1) per push"
    - "About 524,288 copies — each resize copies all elements and there are log₂(1024) resizes"
    - "Zero copies — modern arrays don't need to copy on resize"
  answer: 1
  explanation: "With doubling, resizes occur at sizes 1, 2, 4, 8, ..., 512, copying 1 + 2 + 4 + ... + 512 = 1023 elements total. Adding the 1024 pushes themselves, roughly 2047 operations total for 1024 pushes — under 2 operations per push on average. This is the amortized O(1) argument: even though the final resize alone copies 512 elements, that cost is 'paid for' by the preceding 512 cheap pushes. Option C overcounts by treating all resizes as if each one copied n elements."

- question: "You need a stack for a recursive depth-first search where the maximum depth is unpredictable. Which implementation concern is most relevant?"
  type: multiple-choice
  options:
    - "An array stack is preferred because it is cache-friendly and DFS typically reuses recently accessed elements"
    - "A linked-list stack eliminates capacity overflow risk, since each node is individually allocated — important when maximum depth is unknown"
    - "Both implementations are equivalent since both guarantee O(1) push and pop"
    - "A linked-list stack is always preferred over an array stack for correctness"
  answer: 1
  explanation: "When maximum stack depth is unpredictable, the array's capacity limit becomes a real concern — if the DFS reaches a depth exceeding the array's capacity (even with doubling, very deep recursion can require many doublings or hit memory limits in unexpected ways). A linked-list stack never needs a resize because each node is allocated independently; it naturally grows as long as heap memory is available. Both are O(1) amortized (B is more precise: O(1) worst-case for the linked list), but the unpredictability of depth makes the linked list's lack of capacity overhead more attractive."

- question: "The stack Abstract Data Type (ADT) defines the behavior — LIFO ordering, push, and pop — independently of how the data is actually stored in memory."
  type: true-false
  answer: true
  explanation: "True. This is the defining idea of an ADT: the interface (what operations are available and how they behave) is separated from the implementation (how the data is stored). A stack implemented with an array and a stack implemented with a linked list are both correct stacks as long as they both enforce LIFO ordering and provide O(1) push and pop. Users of the stack don't need to know — and shouldn't need to know — which internal representation is used."

- question: "In a linked-list stack, push must traverse to the end of the list to insert the new element, making it an O(n) operation."
  type: true-false
  answer: false
  explanation: "False. Push inserts at the HEAD of the linked list, not the tail. Creating a new node, setting its 'next' pointer to the current head, and updating the head pointer takes exactly three operations regardless of list length — O(1). Similarly, pop reads the head's value, advances the head to head.next, and returns the value — also O(1). Only operations like searching for a specific value or inserting at the tail require O(n) traversal."

- question: "Explain why an array-based stack that doubles its capacity when full achieves amortized O(1) push, even though individual resize operations cost O(n)."
  type: short-answer
  answer: "When the array doubles, say from size n to 2n, the resize copies n elements. But this resize only occurs after n pushes have been performed since the last resize — all of which were O(1). Spreading the O(n) resize cost across those n pushes gives O(n)/n = O(1) per push. More concretely: after k doublings the array holds 2^k elements, and the total copy work across all doublings is 1 + 2 + 4 + ... + 2^(k−1) = 2^k − 1 < 2^k — less than the total number of pushes. So amortized over all pushes, each push costs less than 2 operations on average."
  explanation: "The key is the doubling factor: doubling ensures that the number of cheap pushes between resizes always equals the cost of the resize itself. If you grew by only 1 each time, the resize at size n would cost O(n), but resizes would happen after every single push — giving O(n) amortized per push, not O(1). Doubling makes resizes rare enough to be 'paid for' by the intervening cheap operations."
```

## Explainer

A **stack** is one of the simplest and most useful abstract data types: it stores elements in a last-in, first-out (LIFO) order, supporting just two primary operations — **push** (add to the top) and **pop** (remove from the top). Think of a stack of plates in a cafeteria: you always add and remove from the top, so the most recently placed plate is the first one taken. This simple constraint turns out to be exactly what you need for tracking function calls (the call stack), undoing operations (undo history), parsing matched parentheses, and evaluating expressions.

Since you already understand arrays and linked lists, you can see that a stack is not a new storage mechanism — it is a *behavioral contract* imposed on top of a concrete data structure. The **array-based implementation** uses an integer variable `top` that tracks the index of the topmost element. Push increments `top` and writes the value; pop reads the value at `top` and decrements it. Both are O(1). The tradeoff is that an array has a fixed capacity — when it fills up, you must allocate a larger array and copy everything over. This resize is O(n) for that single operation, but because you typically double the array size, the cost amortizes to O(1) per push over a sequence of operations. Array-based stacks also benefit from **cache locality**: elements sit in contiguous memory, so the CPU cache can prefetch nearby data efficiently.

The **linked-list implementation** uses the head of the list as the top of the stack. Push creates a new node, sets its `next` pointer to the current head, and updates the head pointer. Pop saves the head's value, moves the head to `head.next`, and returns the saved value. Both operations are O(1) with no amortization needed — there is never a resize because each node is independently allocated. The tradeoff is that every element carries the overhead of a pointer (8 bytes on a 64-bit system), and nodes are scattered across memory, reducing cache performance compared to an array.

Choosing between the two comes down to your workload. If you know a reasonable upper bound on the stack size, or if you want the best raw performance from cache-friendly memory access, the array-based stack is usually preferable. If the stack size is highly unpredictable and you want to avoid any risk of expensive resize operations, the linked-list version offers more consistent per-operation cost. In practice, most standard library stack implementations (like Java's `ArrayDeque` or Python's `list` used as a stack) are array-based because the amortized O(1) guarantee and cache benefits outweigh the occasional resize cost.
