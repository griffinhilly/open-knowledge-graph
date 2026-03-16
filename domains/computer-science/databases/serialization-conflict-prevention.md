---
id: serialization-conflict-prevention
title: Serialization and Conflict Prevention Techniques
domain: computer-science
course: databases
prerequisites:
- id: two-phase-locking
  type: hard
tags:
- concurrency
- serializability
- conflict-prevention
stage: formal-systems
status: draft
---

# Serialization and Conflict Prevention Techniques

## Core Idea
Serialization ensures that concurrent transactions produce results equivalent to serial execution. Two-phase locking and MVCC-based serialization use different mechanisms to prevent conflicts.

## How It's Best Learned
Trace through a conflict scenario and verify that locks or version checks prevent anomalies that would break serializability.

## Common Misconceptions
Serializable isolation does not mean transactions execute one at a time (serial)—it means the outcome is equivalent to some serial order. Read-only transactions can often run in parallel even at SERIALIZABLE level.

## Explainer

From two-phase locking, you already understand the basic mechanism: transactions acquire locks before accessing data and release them only after committing. Serialization builds on this foundation to answer a broader question — how do we guarantee that concurrent transactions produce a result indistinguishable from running them one after another? The answer is **serializability**, the gold standard of transaction correctness. A schedule of interleaved operations is serializable if its outcome matches some serial ordering of the same transactions, even though the operations actually overlapped in time.

The challenge is that conflicts arise when two transactions access the same data and at least one of them writes. There are three types of conflicts: **read-write** (one reads what another will change), **write-read** (one writes what another will read), and **write-write** (both write to the same data). A conflict-serializable schedule is one where you can reorder non-conflicting operations to arrive at a serial schedule. Two-phase locking (2PL) prevents conflicts by ensuring that once a transaction starts releasing locks, it cannot acquire new ones — this growing-then-shrinking pattern guarantees conflict serializability without needing to check the schedule after the fact.

**MVCC-based serialization** takes a different approach. Instead of blocking concurrent access with locks, the system maintains multiple versions of each data item. Readers see a consistent snapshot from their transaction's start time, so they never block writers and writers never block readers. At commit time, the system checks whether the transaction's reads and writes would conflict with any concurrently committed transaction. If a conflict is detected — for example, if another transaction modified data this transaction read — the system aborts and retries the conflicting transaction. This is sometimes called **optimistic concurrency control** because it assumes conflicts are rare and only checks at commit time.

The practical tradeoff is straightforward: lock-based approaches (2PL) prevent conflicts proactively by making transactions wait, which can cause deadlocks and reduced throughput under contention. MVCC-based approaches allow more concurrency but pay the cost of occasional aborts and retries when conflicts do occur. Workloads with mostly reads and rare conflicts favor MVCC; workloads with heavy contention on the same rows may perform better with locking. Understanding both mechanisms lets you choose the right isolation strategy and diagnose concurrency problems when transactions fail or behave unexpectedly.
