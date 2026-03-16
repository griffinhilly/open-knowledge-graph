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

## Explainer

You already know from studying two-phase locking that transactions acquire locks before accessing data and hold them until commit. You also know the four Coffman conditions required for deadlock: mutual exclusion, hold and wait, no preemption, and circular wait. Database deadlocks are what happens when all four conditions are met simultaneously in a live system — and unlike the theoretical treatment, they happen routinely in production.

Picture two transactions running concurrently. Transaction A locks row 1, then tries to lock row 2. Transaction B locks row 2, then tries to lock row 1. Each is holding a lock the other needs, and neither will release its lock until it finishes — but neither can finish because it's waiting. This circular dependency is a **deadlock**, and no amount of waiting will resolve it. The system must intervene. The standard mechanism is a **wait-for graph**: a directed graph where nodes are transactions and an edge from T1 to T2 means "T1 is waiting for a lock held by T2." If this graph contains a cycle, a deadlock exists.

Once a deadlock is detected, the database must choose a **victim** — one transaction to abort so the others can proceed. The victim's locks are released, its changes are rolled back, and it typically retries automatically or returns an error to the application. Victim selection policies vary: some systems abort the youngest transaction (least work lost), others consider the cost of rollback (number of rows modified), and some use priority schemes. The key insight is that deadlock handling is not a bug fix but a normal part of database operation — your application code should expect occasional deadlock-induced aborts and implement retry logic.

**Prevention** strategies avoid deadlocks entirely by breaking one of the four Coffman conditions. The most practical approach is eliminating circular wait by imposing a **global lock ordering** — if all transactions always lock rows in the same order (say, by primary key), cycles cannot form. Timestamp-based protocols offer another option: in **wait-die**, an older transaction waits for a younger one, but a younger transaction is aborted rather than waiting for an older one. In **wound-wait**, the older transaction forces the younger to abort. Both schemes guarantee no cycles because the wait direction is always consistent with timestamp order. Prevention eliminates deadlocks but can increase aborts; detection allows maximum concurrency but requires periodic graph analysis. Most production databases use detection with victim selection, since deadlocks are rare enough that the occasional abort is cheaper than the overhead of strict prevention.
