---
id: multi-version-concurrency-control
title: Multi-Version Concurrency Control (MVCC)
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
tags:
- concurrency
- mvcc
- read-consistency
stage: formal-systems
status: draft
---

# Multi-Version Concurrency Control (MVCC)

## Core Idea
MVCC maintains multiple versions of rows, allowing readers to access consistent snapshots without blocking writers. Each transaction sees data as of a snapshot timestamp, reducing lock contention.

## How It's Best Learned
Observe that in a database with MVCC (PostgreSQL, MySQL InnoDB), read operations do not block writes and vice versa, even without explicit locking.

## Common Misconceptions
MVCC still prevents write-write conflicts via locking; it only eliminates read-write blocking. Old versions are garbage-collected when no active transaction references them.

## Explainer

You already understand that concurrent database access creates problems: one transaction might read data that another is in the middle of modifying, or two transactions might try to update the same row simultaneously. Traditional locking-based concurrency control solves this by making readers wait for writers and writers wait for readers, but this serialization kills throughput. **Multi-Version Concurrency Control (MVCC)** offers an elegant alternative: instead of forcing transactions to wait, the database keeps multiple versions of each row so that readers and writers can operate simultaneously without blocking each other.

The core mechanism works like this: when a transaction modifies a row, the database does not overwrite the existing version. Instead, it creates a **new version** of the row tagged with the writing transaction's ID or timestamp. The old version remains available for other transactions that started before the write. Each transaction operates against a **snapshot** — a consistent view of the database as it existed at the transaction's start time. When transaction T1 reads a row, the database finds the most recent version of that row that was committed before T1's snapshot timestamp. Even if transaction T2 is actively modifying that same row, T1 sees the old version and proceeds without waiting.

This means **readers never block writers, and writers never block readers** — a dramatic improvement over lock-based schemes where a long-running analytical query could stall all concurrent updates. However, MVCC does not eliminate all conflicts. **Write-write conflicts** still require coordination: if two transactions attempt to modify the same row, the second one must either wait or abort, depending on the database's conflict resolution strategy. PostgreSQL, for example, uses a "first updater wins" policy — the second transaction blocks until the first commits or rolls back, then either proceeds or aborts depending on the outcome.

The cost of maintaining multiple versions is **storage overhead and garbage collection**. As transactions create new versions, old versions accumulate. The database must periodically determine which old versions are no longer visible to any active transaction and reclaim their storage — a process PostgreSQL calls **VACUUM** and MySQL/InnoDB handles through a background purge thread. If garbage collection falls behind (for example, because a long-running transaction holds an old snapshot open), the database accumulates bloat that degrades performance. Understanding this lifecycle — version creation, snapshot visibility, and garbage collection — is essential for diagnosing performance problems in MVCC-based systems like PostgreSQL, MySQL InnoDB, and Oracle.
