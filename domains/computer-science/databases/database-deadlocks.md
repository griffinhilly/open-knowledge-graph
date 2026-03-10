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
status: draft
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
