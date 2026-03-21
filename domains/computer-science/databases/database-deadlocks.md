---
id: database-deadlocks
title: Deadlocks in Databases
domain: computer-science
course: databases
prerequisites:
- id: two-phase-locking
  type: hard
- id: deadlock-conditions
  type: hard
tags:
- deadlock
- wait-for graph
- deadlock detection
- deadlock prevention
- victim selection
stage: formal-systems
status: validated
---

# Deadlocks in Databases

## Core Idea
A database deadlock occurs when two or more transactions form a cycle in the wait-for graph — each holds a lock the next one needs, so none can proceed. Databases detect deadlocks by periodically checking the wait-for graph for cycles, then aborting one transaction (the victim, chosen by age, cost, or priority) to break the cycle. Prevention strategies include acquiring locks in a fixed global order or using timestamp-based protocols (wait-die: older waits, younger aborts; wound-wait: older aborts younger) that preclude cycle formation.

## How It's Best Learned
Reproduce a deadlock experimentally: open two sessions, have each lock a different row, then have each attempt to lock the row held by the other. Observe which session is chosen as the victim and retried.

## Common Misconceptions
- Deadlocks are not application bugs per se — they are an inherent risk of lock-based concurrency and must be handled by retrying the aborted transaction.
- Timeouts alone can falsely abort long-running transactions that are not deadlocked; wait-for graph analysis is more precise.
- Reducing lock granularity (fewer, coarser locks) reduces deadlock probability but also reduces concurrency.

## Questions

```yaml
- question: "Transaction T1 holds a lock on row A and is waiting for a lock on row B. Transaction T2 holds a lock on row B and is waiting for a lock on row A. What best describes this situation?"
  type: multiple-choice
  options:
    - "A race condition — the transaction that commits first wins, and the loser must retry"
    - "A deadlock — a cycle exists in the wait-for graph, and neither transaction can proceed without external intervention"
    - "A livelock — both transactions keep releasing and re-acquiring locks without making progress"
    - "A serialization failure — the transactions have conflicting schedules that cannot be serialized"
  answer: 1
  explanation: "This is a classic deadlock: T1→T2 (T1 waits for T2) and T2→T1 (T2 waits for T1) form a cycle in the wait-for graph. Neither transaction will ever release its lock voluntarily — each is waiting for the other forever. The database must detect this cycle and abort one transaction (the victim) to break it. A race condition (option A) describes concurrent access where ordering matters but no permanent blocking occurs. Livelock (option C) means transactions keep retrying but fail to progress. Option D describes a serialization anomaly, not a permanent blocking situation."

- question: "A database detects a deadlock and aborts transaction T2, rolling back its changes. What is the correct next step for the application?"
  type: multiple-choice
  options:
    - "Report a fatal database error — deadlocks indicate data corruption requiring manual recovery"
    - "Retry T2 from scratch — deadlock aborts are normal events that application code should handle with retry logic"
    - "Wait for T1 to commit, then re-acquire T2's original locks in reverse order to prevent future deadlocks"
    - "Escalate to table-level locks to prevent the row-level contention that caused the deadlock"
  answer: 1
  explanation: "Deadlock aborts are not bugs — they are the normal resolution mechanism for lock cycles, and the correct response is to retry the transaction. Application code should always handle deadlock-induced aborts with automatic retry logic. Option A is wrong because no data corruption has occurred; the rollback ensures atomicity. Option C describes lock ordering, which is a prevention strategy, not a recovery response. Option D might reduce future deadlocks but at the cost of concurrency, and it is not the immediate correct response to an abort."

- question: "Imposing a global lock-ordering rule (e.g., always lock rows in ascending primary key order) prevents deadlocks by eliminating the 'hold and wait' Coffman condition."
  type: true-false
  answer: false
  explanation: "Global lock ordering prevents deadlocks by eliminating the *circular wait* condition, not hold-and-wait. Transactions still hold locks while waiting for others — hold-and-wait remains present. What cannot happen is a cycle: if every transaction acquires locks in the same order, no transaction can be waiting for a lock that precedes one it already holds. Mutual exclusion, hold-and-wait, and no-preemption remain; it is circular wait specifically that the global ordering breaks."

- question: "A wait-for graph cycle involving three transactions always requires aborting at least two transactions to resolve the deadlock."
  type: true-false
  answer: false
  explanation: "Any cycle in a wait-for graph can be broken by removing a single edge, which corresponds to aborting one transaction and releasing all its locks. When the victim's locks are released, the transactions that were waiting for them can proceed — the cycle is fully dissolved with one abort. The database typically chooses the victim to minimize rollback cost (fewest rows modified, youngest transaction). Aborting two or more is unnecessary and wasteful."

- question: "Why is a wait-for graph cycle the right model for detecting database deadlocks, and why can't simple timeouts replace it?"
  type: short-answer
  answer: "A wait-for graph cycle directly captures the deadlock condition: a circular dependency that can never self-resolve. If a cycle exists, there is a deadlock; if no cycle exists, there is no deadlock — the detection is exact. Timeouts cannot distinguish a deadlocked transaction from a legitimately slow one (e.g., a complex query). A timeout set too low aborts valid long-running transactions unnecessarily; one set too high leaves deadlocked transactions blocked for too long. Wait-for graph analysis avoids both failure modes by detecting exactly and only real deadlocks."
  explanation: "The practical trade-off is that maintaining the wait-for graph and running periodic cycle detection has overhead, while timeouts are simple to implement. Most production databases accept this overhead because the occasional false abort from timeouts is more disruptive than the graph maintenance cost — especially for applications that depend on long-running transactions."
```

## Explainer

You already know from studying two-phase locking that transactions acquire locks before accessing data and hold them until commit. You also know the four Coffman conditions required for deadlock: mutual exclusion, hold and wait, no preemption, and circular wait. Database deadlocks are what happens when all four conditions are met simultaneously in a live system — and unlike the theoretical treatment, they happen routinely in production.

Picture two transactions running concurrently. Transaction A locks row 1, then tries to lock row 2. Transaction B locks row 2, then tries to lock row 1. Each is holding a lock the other needs, and neither will release its lock until it finishes — but neither can finish because it's waiting. This circular dependency is a **deadlock**, and no amount of waiting will resolve it. The system must intervene. The standard mechanism is a **wait-for graph**: a directed graph where nodes are transactions and an edge from T1 to T2 means "T1 is waiting for a lock held by T2." If this graph contains a cycle, a deadlock exists.

Once a deadlock is detected, the database must choose a **victim** — one transaction to abort so the others can proceed. The victim's locks are released, its changes are rolled back, and it typically retries automatically or returns an error to the application. Victim selection policies vary: some systems abort the youngest transaction (least work lost), others consider the cost of rollback (number of rows modified), and some use priority schemes. The key insight is that deadlock handling is not a bug fix but a normal part of database operation — your application code should expect occasional deadlock-induced aborts and implement retry logic.

**Prevention** strategies avoid deadlocks entirely by breaking one of the four Coffman conditions. The most practical approach is eliminating circular wait by imposing a **global lock ordering** — if all transactions always lock rows in the same order (say, by primary key), cycles cannot form. Timestamp-based protocols offer another option: in **wait-die**, an older transaction waits for a younger one, but a younger transaction is aborted rather than waiting for an older one. In **wound-wait**, the older transaction forces the younger to abort. Both schemes guarantee no cycles because the wait direction is always consistent with timestamp order. Prevention eliminates deadlocks but can increase aborts; detection allows maximum concurrency but requires periodic graph analysis. Most production databases use detection with victim selection, since deadlocks are rare enough that the occasional abort is cheaper than the overhead of strict prevention.
