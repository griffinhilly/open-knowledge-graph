---
id: semaphore-formal-definition
title: 'Semaphores: Formal Definition and Semantics'
domain: computer-science
course: operating-systems
prerequisites:
- id: semaphores
  type: hard
- id: test-and-set-primitive
  type: hard
builds-toward:
- condition-variable-patterns
- producer-consumer-synchronization
tags:
- semaphores
- synchronization
- formal
stage: formal-systems
status: draft
---

# Semaphores: Formal Definition and Semantics

## Core Idea
A semaphore is an integer with atomic operations wait (P: decrement, block if ≤0) and signal (V: increment, unblock one waiter). Binary semaphores (0/1) act as locks; counting semaphores manage resource pools. Formal analysis requires explicit invariants.

## How It's Best Learned
Solve producer-consumer and readers-writers problems with semaphores; formally verify that invariants hold before and after each operation.

## Common Misconceptions
- Confusing wait/signal semantics or order.
- Thinking semaphores guarantee fairness (they do not).
- Overlooking subtle deadlocks from wait order dependencies.
