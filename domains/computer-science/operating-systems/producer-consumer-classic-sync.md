---
id: producer-consumer-classic-sync
title: 'Producer-Consumer Problem: Classic Synchronization'
domain: computer-science
course: operating-systems
prerequisites:
- id: counting-semaphores-resource-pools
  type: hard
- id: condition-variables-and-monitors
  type: soft
tags:
- synchronization-patterns
- classic-problems
- coordination
stage: formal-systems
status: draft
---

# Producer-Consumer Problem: Classic Synchronization

## Core Idea
The producer-consumer problem is a classic synchronization scenario where producers generate data and consumers process it via a bounded buffer. Producers must block when full; consumers must block when empty. Solutions using semaphores (separate empty/full counters) or condition variables illustrate fundamental synchronization design.

## How It's Best Learned
Implement producer-consumer using semaphores, then with condition variables, comparing designs and observing behavior under load.

## Explainer

The producer-consumer problem is one of the most practical synchronization challenges you will encounter, and it builds directly on your understanding of counting semaphores and resource pools. Imagine a factory assembly line: one worker places items onto a conveyor belt (the producer), and another worker picks items off the belt to package them (the consumer). The belt has limited space — it can hold, say, ten items. If the producer works faster than the consumer, the belt fills up and the producer must wait. If the consumer works faster, the belt empties and the consumer must wait. The **bounded buffer** is the programming equivalent of this conveyor belt: a fixed-size data structure shared between threads that produce data and threads that consume it.

The classic solution uses three synchronization primitives working together. Two **counting semaphores** track the buffer's state: one counts the number of empty slots (initialized to the buffer size), and the other counts the number of filled slots (initialized to zero). A **mutex** (or binary semaphore) protects the buffer itself from simultaneous access. When a producer wants to add an item, it first waits on the empty-slot semaphore (decrementing it — blocking if no slots are available), then acquires the mutex, writes to the buffer, releases the mutex, and finally signals the filled-slot semaphore (incrementing it to wake any waiting consumer). The consumer does the mirror image: wait on filled, lock, read, unlock, signal empty.

The order of these operations matters critically. If a producer acquires the mutex before waiting on the empty semaphore, and the buffer is full, the producer will hold the mutex while blocked — preventing any consumer from ever acquiring the mutex to remove an item. This is a **deadlock**, and it is the single most common bug in producer-consumer implementations. The rule is simple: always acquire the counting semaphore before the mutex. The semaphore gates entry; the mutex protects the shared data structure once you know you have permission to proceed.

An alternative design uses **condition variables** with a monitor instead of semaphores. Here, the mutex protects the buffer, and two condition variables represent "buffer not full" and "buffer not empty." A producer locks the mutex, checks whether the buffer is full, and if so calls wait on the not-full condition (which atomically releases the mutex and blocks). When a consumer removes an item, it signals not-full to wake a waiting producer. This approach is more expressive — you can check arbitrary predicates, not just counter values — but requires care to avoid **spurious wakeups**, which is why the wait must always occur inside a while loop that rechecks the condition, never a bare if statement.
