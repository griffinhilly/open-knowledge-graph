---
id: deques-double-ended-queues
title: Deques and Double-Ended Queues
domain: computer-science
course: data-structures-and-algorithms
prerequisites:
- id: doubly-linked-lists
  type: soft
- id: queues-data-structure
  type: hard
tags:
- deques
- stacks
- queues
- double-ended
- sliding-window
stage: formal-systems
status: draft
---

# Deques and Double-Ended Queues

## Core Idea
A deque (double-ended queue) supports O(1) insertion and deletion at both front and back, combining stack and queue properties. Deques are typically implemented with circular arrays or doubly linked lists and are essential for sliding-window problems, efficient iterative DFS, and algorithms requiring bidirectional access.

## How It's Best Learned
Implement using both circular arrays (handling wraparound indices) and doubly linked lists; compare space and time trade-offs. Solve sliding-window maximum and implement DFS iteratively using a deque to appreciate its utility.

## Common Misconceptions
- Deques are slower than specialized queues or stacks (both ends are O(1) with the right implementation). - Deques have niche applications (they are fundamental to many algorithms).
