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
status: validated
---

# Multi-Version Concurrency Control (MVCC)

## Core Idea
MVCC maintains multiple versions of rows, allowing readers to access consistent snapshots without blocking writers. Each transaction sees data as of a snapshot timestamp, reducing lock contention.

## How It's Best Learned
Observe that in a database with MVCC (PostgreSQL, MySQL InnoDB), read operations do not block writes and vice versa, even without explicit locking.

## Common Misconceptions
MVCC still prevents write-write conflicts via locking; it only eliminates read-write blocking. Old versions are garbage-collected when no active transaction references them.

## Questions

```yaml
- question: "Transaction T1 started at time 10. Transaction T2 started at time 15 and is currently updating row R. At time 20, T1 reads row R. What does T1 see under MVCC?"
  type: multiple-choice
  options:
    - "T1 blocks until T2 commits, then reads the new version"
    - "T1 reads the version of R that was committed before T1's snapshot time (time 10)"
    - "T1 reads the version of R that T2 is currently writing (the in-progress update)"
    - "T1 receives an error because row R is locked"
  answer: 1
  explanation: "Under MVCC, each transaction reads from a snapshot taken at its start time. T1's snapshot was taken at time 10, before T2 started. When T1 reads row R, the database finds the most recent committed version of R that existed before time 10 — not T2's in-progress update. This is the core MVCC guarantee: readers never block writers and writers never block readers. T1 proceeds immediately without waiting for T2."

- question: "Under MVCC, two transactions simultaneously attempt to update the same row. What happens?"
  type: multiple-choice
  options:
    - "Both updates succeed simultaneously, with MVCC creating two new versions"
    - "The second transaction reads the old version and writes independently, causing no conflict"
    - "The second transaction must wait or abort — write-write conflicts still require coordination"
    - "MVCC prevents this situation by making rows read-only during updates"
  answer: 2
  explanation: "MVCC eliminates read-write blocking but does NOT eliminate write-write conflicts. When two transactions try to update the same row, the database must serialize them. PostgreSQL uses a 'first updater wins' policy: the second transaction blocks until the first commits or rolls back, then either proceeds on the new version or aborts depending on the isolation level. This is a critical misconception to avoid: MVCC is not a universal lock eliminator."

- question: "Under MVCC, a long-running analytical query can cause the database to retain old row versions that would otherwise be garbage collected."
  type: true-false
  answer: true
  explanation: "This is a real and important operational concern. MVCC garbage collection (VACUUM in PostgreSQL) can only reclaim a row version when no active transaction has a snapshot older than that version. A long-running analytical query that holds an old snapshot prevents the database from reclaiming any versions created after its snapshot time. This causes 'table bloat' — the table grows on disk even if rows are being deleted — and can severely degrade performance. It's one of the key reasons why long-running transactions are problematic in MVCC databases."

- question: "MVCC completely eliminates the need for any locking in the database."
  type: true-false
  answer: false
  explanation: "MVCC eliminates read-write locking — readers and writers no longer block each other. But write-write conflicts still require locking or conflict detection. When two transactions try to modify the same row, the database must serialize them. Additionally, DDL operations (schema changes), certain isolation levels (serializable), and explicit user-level locks (SELECT FOR UPDATE) still involve traditional locking. MVCC's promise is specifically that reads do not block writes and vice versa — not that locks disappear entirely."

- question: "Explain why old row versions in an MVCC database cannot be immediately deleted when a transaction updates a row."
  type: short-answer
  answer: "Old versions must be retained as long as any active transaction has a snapshot older than that version. A transaction reads from a consistent snapshot of the database at its start time, and may need to access old versions to satisfy that snapshot. Only once all active transactions have snapshots newer than the old version — meaning no transaction will ever need to see it — can the version be safely reclaimed by garbage collection."
  explanation: "This lifecycle is what makes MVCC work: creating a new version on update, retaining old versions for active snapshots, and garbage collecting when versions are no longer visible to any active transaction. The failure to garbage collect promptly (due to long-running transactions or a misconfigured autovacuum in PostgreSQL) leads to table bloat, increased disk I/O, and degraded query performance."
```

## Explainer

You already understand that concurrent database access creates problems: one transaction might read data that another is in the middle of modifying, or two transactions might try to update the same row simultaneously. Traditional locking-based concurrency control solves this by making readers wait for writers and writers wait for readers, but this serialization kills throughput. **Multi-Version Concurrency Control (MVCC)** offers an elegant alternative: instead of forcing transactions to wait, the database keeps multiple versions of each row so that readers and writers can operate simultaneously without blocking each other.

The core mechanism works like this: when a transaction modifies a row, the database does not overwrite the existing version. Instead, it creates a **new version** of the row tagged with the writing transaction's ID or timestamp. The old version remains available for other transactions that started before the write. Each transaction operates against a **snapshot** — a consistent view of the database as it existed at the transaction's start time. When transaction T1 reads a row, the database finds the most recent version of that row that was committed before T1's snapshot timestamp. Even if transaction T2 is actively modifying that same row, T1 sees the old version and proceeds without waiting.

This means **readers never block writers, and writers never block readers** — a dramatic improvement over lock-based schemes where a long-running analytical query could stall all concurrent updates. However, MVCC does not eliminate all conflicts. **Write-write conflicts** still require coordination: if two transactions attempt to modify the same row, the second one must either wait or abort, depending on the database's conflict resolution strategy. PostgreSQL, for example, uses a "first updater wins" policy — the second transaction blocks until the first commits or rolls back, then either proceeds or aborts depending on the outcome.

The cost of maintaining multiple versions is **storage overhead and garbage collection**. As transactions create new versions, old versions accumulate. The database must periodically determine which old versions are no longer visible to any active transaction and reclaim their storage — a process PostgreSQL calls **VACUUM** and MySQL/InnoDB handles through a background purge thread. If garbage collection falls behind (for example, because a long-running transaction holds an old snapshot open), the database accumulates bloat that degrades performance. Understanding this lifecycle — version creation, snapshot visibility, and garbage collection — is essential for diagnosing performance problems in MVCC-based systems like PostgreSQL, MySQL InnoDB, and Oracle.
