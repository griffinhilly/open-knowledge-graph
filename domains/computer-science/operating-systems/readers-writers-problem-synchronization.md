---
id: readers-writers-problem-synchronization
title: Readers-Writers Problem and Lock Patterns
domain: computer-science
course: operating-systems
prerequisites:
- id: condition-variables-and-monitors
  type: hard
tags:
- synchronization-patterns
- fairness
- reader-writer-locks
stage: formal-systems
status: draft
---

# Readers-Writers Problem and Lock Patterns

## Core Idea
The readers-writers problem allows multiple readers concurrently but requires exclusive access for writers. Simple solutions risk starving one group. Reader-preference solutions favor readers; writer-preference favor writers. Fair solutions prevent starvation via condition variables tracking reader/writer counts.

## Common Misconceptions
Any solution works (reader-preference starves writers; writer-preference starves readers). Readers never conflict (they do; writes require exclusive access).

## Explainer

The readers-writers problem captures a pattern that appears constantly in real systems: many threads need to read shared data, but occasionally one thread needs to update it. A simple mutex would work — lock before access, unlock after — but it would force readers to wait for each other even though simultaneous reads are perfectly safe. The whole point of the readers-writers problem is to allow **concurrent reads** while still guaranteeing **exclusive writes**. Since you already understand condition variables and monitors, you have the tools to build solutions; the challenge is choosing *which* solution and understanding its fairness tradeoffs.

The simplest approach is **reader-preference**: readers can always enter as long as no writer is active. A shared counter tracks the number of active readers. The first reader to arrive locks out writers; the last reader to leave unlocks the resource. Writers must wait until the reader count drops to zero. This maximizes read throughput, but if readers arrive continuously, a writer may wait forever — this is **writer starvation**. In a system where reads vastly outnumber writes and write latency is not critical, this tradeoff might be acceptable, but in general it is dangerous.

The mirror image is **writer-preference**: when a writer is waiting, no new readers are admitted. Arriving readers queue behind the pending writer. This guarantees writers make progress but can starve readers if writes are frequent. The solution uses a condition variable for waiting readers and a separate one for waiting writers, with the monitor deciding whom to wake. You can think of it as a priority system: writers jump the queue ahead of new readers, though currently-active readers are allowed to finish.

A **fair solution** prevents starvation for both sides. One common approach uses a turnstile — a semaphore or condition variable that writers lock when they arrive, forcing subsequent readers to queue behind the writer in arrival order. Once the writer finishes, the queued readers are released together and can read concurrently until the next writer arrives. Another fair approach uses a single FIFO queue where readers and writers are served in order of arrival, with consecutive readers batched together. The key insight is that fairness requires tracking arrival order, not just counts. When implementing these patterns, the condition variable predicates from your prerequisite knowledge — "wait while the condition is not met, re-check after being signaled" — are exactly the mechanism that makes each variant work.
