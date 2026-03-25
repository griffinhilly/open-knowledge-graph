---
id: readers-writers-problem-synchronization
title: Readers-Writers Problem and Lock Patterns
domain: computer-science
course: operating-systems
prerequisites:
- id: monitors-and-condition-variables
  type: hard
tags:
- synchronization-patterns
- fairness
- reader-writer-locks
stage: formal-systems
status: validated
---

# Readers-Writers Problem and Lock Patterns

## Core Idea
The readers-writers problem allows multiple readers concurrently but requires exclusive access for writers. Simple solutions risk starving one group. Reader-preference solutions favor readers; writer-preference favor writers. Fair solutions prevent starvation via condition variables tracking reader/writer counts.

## Common Misconceptions
Any solution works (reader-preference starves writers; writer-preference starves readers). Readers never conflict (they do; writes require exclusive access).

## Questions

```yaml
- question: "A database uses reader-preference locks. Traffic is 95% reads and 5% writes. Which problem is most likely to occur?"
  type: multiple-choice
  options:
    - "Deadlock between multiple readers waiting for each other"
    - "Writer starvation — writers may wait indefinitely while readers continuously arrive"
    - "Reader starvation — writers will lock out readers for long periods"
    - "Race conditions — concurrent readers can corrupt the shared data"
  answer: 1
  explanation: "Reader-preference allows new readers to enter as long as no writer is active. If reads are frequent (95%), there will almost always be at least one active reader, meaning the reader count never drops to zero and writers can wait indefinitely — writer starvation. Readers don't block each other (no deadlock between readers). Race conditions don't occur because writers still get exclusive access; the problem is that writers can't get that access promptly."

- question: "What is the minimum information a fair readers-writers solution must track that a simple reader-preference solution does not?"
  type: multiple-choice
  options:
    - "The number of active readers"
    - "Whether any writer is currently active"
    - "The arrival order or waiting queues for both readers and writers"
    - "The total number of reads and writes that have occurred"
  answer: 2
  explanation: "Reader-preference tracks only the number of active readers and whether a writer is active — a purely count-based policy. This allows arbitrarily many new readers to jump ahead of a waiting writer. A fair solution must track arrival order so that when a writer is waiting, subsequent readers queue behind it rather than being admitted immediately. Fairness requires preventing queue-jumping, which requires knowing when each thread arrived relative to others."

- question: "In a reader-preference solution, allowing multiple readers to access data simultaneously is safe because reads do not modify shared state."
  type: true-false
  answer: true
  explanation: "Correct. The fundamental insight of the readers-writers problem is that read operations are non-destructive — two threads can read the same memory simultaneously without corrupting data or producing incorrect results. The exclusion requirement is only between writers and other accessors. Reader-preference exploits this safely by allowing concurrent reads, restricting only writer access to periods when no readers are active."

- question: "Writer-preference solutions prevent writer starvation and should therefore be preferred over reader-preference solutions in all real-world systems."
  type: true-false
  answer: false
  explanation: "False. Writer-preference prevents writer starvation but introduces reader starvation: if writes are frequent, readers may wait indefinitely. Neither preference-based solution is universally better — the right choice depends on the workload. Read-heavy systems may accept reader-preference; write-critical systems may prefer writer-preference. For balanced workloads, a fair solution (FIFO ordering, turnstile) prevents starvation on both sides but adds implementation complexity."

- question: "Why does a fair readers-writers solution batch waiting readers together rather than serving them one at a time in strict FIFO order?"
  type: short-answer
  answer: "If waiting readers were admitted one at a time in strict per-thread FIFO, the performance advantage of concurrent reading would be lost — readers would effectively be serialized. By releasing all readers queued behind a writer simultaneously once the writer completes, the system allows the concurrent reads that motivated the readers-writers design. The batching preserves the key insight: reads don't conflict with each other, so all readers waiting behind a writer can proceed together."
  explanation: "Strict per-reader FIFO would be correct (no starvation) but wasteful: R1 would acquire the lock, R2 would wait, R1 releases, R2 acquires — all sequential. Batching means: when writer W releases, all readers queued behind W are released together and read concurrently. The lock count climbs to n, they all read, the count drops to 0, allowing the next writer to proceed. This is both fair (W served before readers who arrived after W) and concurrent."
```

## Explainer

The readers-writers problem captures a pattern that appears constantly in real systems: many threads need to read shared data, but occasionally one thread needs to update it. A simple mutex would work — lock before access, unlock after — but it would force readers to wait for each other even though simultaneous reads are perfectly safe. The whole point of the readers-writers problem is to allow **concurrent reads** while still guaranteeing **exclusive writes**. Since you already understand condition variables and monitors, you have the tools to build solutions; the challenge is choosing *which* solution and understanding its fairness tradeoffs.

The simplest approach is **reader-preference**: readers can always enter as long as no writer is active. A shared counter tracks the number of active readers. The first reader to arrive locks out writers; the last reader to leave unlocks the resource. Writers must wait until the reader count drops to zero. This maximizes read throughput, but if readers arrive continuously, a writer may wait forever — this is **writer starvation**. In a system where reads vastly outnumber writes and write latency is not critical, this tradeoff might be acceptable, but in general it is dangerous.

The mirror image is **writer-preference**: when a writer is waiting, no new readers are admitted. Arriving readers queue behind the pending writer. This guarantees writers make progress but can starve readers if writes are frequent. The solution uses a condition variable for waiting readers and a separate one for waiting writers, with the monitor deciding whom to wake. You can think of it as a priority system: writers jump the queue ahead of new readers, though currently-active readers are allowed to finish.

A **fair solution** prevents starvation for both sides. One common approach uses a turnstile — a semaphore or condition variable that writers lock when they arrive, forcing subsequent readers to queue behind the writer in arrival order. Once the writer finishes, the queued readers are released together and can read concurrently until the next writer arrives. Another fair approach uses a single FIFO queue where readers and writers are served in order of arrival, with consecutive readers batched together. The key insight is that fairness requires tracking arrival order, not just counts. When implementing these patterns, the condition variable predicates from your prerequisite knowledge — "wait while the condition is not met, re-check after being signaled" — are exactly the mechanism that makes each variant work.
