---
id: priority-queue-implementations
title: 'Priority Queues: Heap-Based and Binary Search Tree Implementations'
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: heap-structure-and-heapify-operations
  type: hard
builds-toward:
- dijkstras-algorithm
- astar-search-algorithm
tags:
- priority-queue
- heap
- queue
stage: formal-systems
status: validated
---

# Priority Queues: Heap-Based and Binary Search Tree Implementations

## Core Idea
A priority queue supports extracting elements by priority, not insertion order. Heap-based implementations are efficient (O(log n) insert/extract) and space-efficient. BST-based versions offer O(log n) operations too but with higher overhead.

## Questions

```yaml
- question: "A scheduling system needs to insert jobs and always retrieve the highest-priority job quickly. A colleague suggests using a balanced BST instead of a binary heap. What is the strongest argument for the binary heap?"
  type: multiple-choice
  options:
    - "Binary heaps support O(1) search for arbitrary elements, which BSTs cannot match"
    - "Binary heaps are stored in a flat array, giving better cache performance and no pointer overhead"
    - "Binary heaps support O(log n) deletion of arbitrary elements, which BSTs cannot"
    - "Binary heaps maintain sorted order, enabling efficient in-order traversal"
  answer: 1
  explanation: "The binary heap's key advantage is its array-based storage: the element at index i has children at 2i+1 and 2i+2, with no pointers needed. This compact layout gives excellent cache locality and low constant factors. BSTs actually support arbitrary element search and deletion (things heaps do poorly), and heaps do NOT maintain sorted order or support efficient arbitrary deletion. The tradeoff is flipped: use a heap for pure insert/extract-min; use a BST when you also need search by value."

- question: "Both binary heaps and balanced BSTs offer O(log n) insert and extract-min. Why does the binary heap tend to dominate in practice for priority queue workloads?"
  type: multiple-choice
  options:
    - "Heap operations have O(1) amortized complexity, while BST operations are always O(log n)"
    - "BSTs cannot implement a priority queue because they lack a natural notion of 'priority'"
    - "Heaps use array storage with no pointer overhead and better cache locality than pointer-based BSTs"
    - "BSTs require rebalancing after every insertion, making them O(n) in the worst case"
  answer: 2
  explanation: "Both structures are O(log n), so the advantage is in constant factors. A heap's flat array layout means each level-traversal step accesses adjacent memory, which the CPU cache handles efficiently. A BST's nodes are individually heap-allocated and scattered in memory, causing cache misses on each pointer dereference. Rebalancing BSTs is O(log n), not O(n). And BSTs can absolutely implement priority queues — the leftmost node is the minimum."

- question: "A binary heap priority queue stores data as a flat array rather than a linked tree structure."
  type: true-false
  answer: true
  explanation: "This is correct and is the key structural insight. In a binary heap, the element at index i has its left child at 2i+1 and right child at 2i+2, with the parent at floor((i-1)/2). This implicit tree structure means no pointers are needed — the entire heap is a contiguous array. This gives excellent cache performance and eliminates the per-node pointer overhead that BSTs require."

- question: "If you need a priority queue that also supports fast search for and deletion of arbitrary elements by value, a binary heap is the better choice over a BST."
  type: true-false
  answer: false
  explanation: "This is backwards. Binary heaps are efficient only for insert and extract-min/max. Finding or deleting an arbitrary element in a heap requires O(n) linear search because the heap property provides no guidance for locating non-root elements. A balanced BST supports O(log n) search, insertion, and deletion by value, making it the right choice when those operations are needed alongside priority access."

- question: "Why does the heap 'bubble up' operation preserve the heap property after insertion, and what property of the heap structure guarantees the operation terminates in O(log n) steps?"
  type: short-answer
  answer: "After inserting at the bottom, the new element is swapped with its parent whenever it violates the heap property (e.g., is smaller than its parent in a min-heap). Each swap moves the element one level up. The operation terminates because the heap is a complete binary tree — every path from root to leaf has length at most log n — so at most log n comparisons and swaps are needed before the element reaches its correct position or the root."
  explanation: "The bubble-up process works because the heap property is local: each node need only be <= (or >=) its parent. A swap fixes the local violation at each level. The O(log n) bound comes directly from the height of the tree: a complete binary tree with n nodes has height floor(log2 n), bounding the number of levels the element can traverse."
```

## Explainer

A **priority queue** is an abstract data type where each element has an associated priority, and the operation you care most about is "give me the highest-priority element." Unlike a regular queue where the first item in is the first out, a priority queue always serves the most urgent item first, regardless of when it arrived. The question is: what concrete data structure should back this abstraction?

The dominant answer is a **binary heap**, which you studied in heap structure and heapify operations. A min-heap keeps the smallest element at the root; a max-heap keeps the largest. Insertion works by placing the new element at the bottom of the heap and "bubbling up" — comparing with its parent and swapping until the heap property is restored. Extraction removes the root, moves the last element to the root position, and "bubbles down" — swapping with the smaller (or larger) child until the heap property holds again. Both operations are O(log n) because the heap is a complete binary tree with height log n. Crucially, heaps are stored in a flat array with no pointer overhead: the children of element at index i live at indices 2i+1 and 2i+2. This compact layout gives excellent cache performance and makes heaps the default choice for priority queues in practice.

A **balanced binary search tree** (like a red-black tree or AVL tree) can also implement a priority queue: the minimum is always the leftmost node, extractable in O(log n), and insertion is O(log n). BSTs additionally support operations that heaps cannot efficiently provide — finding an arbitrary element, deleting by value, or iterating in sorted order. However, BSTs carry per-node pointer overhead (left child, right child, parent, balance metadata), worse cache locality due to scattered memory allocation, and more complex rebalancing logic. If all you need is insert and extract-min, this extra machinery is wasted.

The choice between implementations reduces to what operations you need. If your workload is purely "insert elements, extract the best one," a binary heap wins on simplicity, memory, and constant factors. If you also need to search for or delete arbitrary elements by value — as in some scheduling algorithms — a BST or an augmented heap (like an indexed priority queue) is worth the overhead. Algorithms like Dijkstra's shortest path and A* search rely heavily on priority queues, performing one extract-min and potentially many decrease-key operations per iteration, which is why the efficiency of the underlying heap directly determines the algorithm's practical speed.
