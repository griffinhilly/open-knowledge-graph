---
id: multiversion-concurrency-mvcc
title: Multiversion Concurrency Control (MVCC) and Snapshot Isolation
domain: computer-science
course: databases
prerequisites:
- id: sql-isolation-levels-anomalies
  type: hard
builds-toward:
- snapshot-isolation-write-skew
tags:
- MVCC
- versioning
- snapshot
- timestamp
- SI
stage: formal-systems
status: validated
---

# Multiversion Concurrency Control (MVCC) and Snapshot Isolation

## Core Idea
MVCC maintains multiple versions of data items, each with creation and deletion timestamps. Readers access versions appropriate for their transaction timestamp without blocking writers; writers create new versions without invalidating readers. This eliminates most read-write conflicts. PostgreSQL, Oracle, and others use MVCC variants. Garbage collection removes old versions no longer needed by any transaction, managing version bloat.

## Questions

```yaml
- question: "Transaction A starts at timestamp 100. At timestamp 105, Transaction B updates a customer's balance from $500 to $600 and commits. At timestamp 110, Transaction A reads that balance. What does Transaction A see?"
  type: multiple-choice
  options:
    - "$600 — Transaction B committed before Transaction A read, so A sees the latest committed value"
    - "$500 — Transaction A's snapshot was taken at timestamp 100, before B's update"
    - "An error — MVCC aborts one transaction when concurrent modifications are detected"
    - "Either value — MVCC provides no guarantee about which version a transaction sees"
  answer: 1
  explanation: "MVCC gives Transaction A a snapshot of the database as it existed at A's start timestamp (100). Even though Transaction B committed at timestamp 105 — before A's read at 110 — B's update is invisible to A because it postdates A's snapshot. Transaction A continues to see $500 throughout its lifetime. This is snapshot isolation in action: A reads from a frozen view of the database, unaffected by concurrent commits. Option A describes standard read-committed behavior (which uses a fresh snapshot per statement), not snapshot isolation."

- question: "A PostgreSQL database is experiencing performance degradation and storage growth. The DBA discovers a read-only reporting query that has been running for 6 hours. Why might this cause degradation even though the query only reads?"
  type: multiple-choice
  options:
    - "Long-running read queries consume excessive CPU and slow other transactions"
    - "The open snapshot prevents the garbage collector (VACUUM) from reclaiming obsolete row versions created after timestamp 100, causing table bloat"
    - "Read-only transactions acquire shared locks that block write transactions from completing"
    - "Long read transactions are unrelated to MVCC; this is a network or index issue"
  answer: 1
  explanation: "MVCC retains old row versions as long as any active transaction might need to read them. A 6-hour-old snapshot means all row versions created since that snapshot's start time must be preserved — even rows that have been updated or deleted dozens of times since then. PostgreSQL's autovacuum process cannot reclaim those dead versions while the old snapshot is open, causing the table to accumulate dead tuples (table bloat), degrade sequential scan performance, and consume disk space. This is why long-running transactions in MVCC systems are dangerous: even a read-only transaction can pin a snapshot that blocks garbage collection and cascades into significant operational problems."

- question: "Under MVCC snapshot isolation, a transaction that starts at time T will see the same value for a row every time it reads that row, even if another transaction commits an update to that row during T's lifetime."
  type: true-false
  answer: true
  explanation: "Snapshot isolation provides repeatable reads as a built-in property: Transaction T always reads from its start-time snapshot. Any updates committed after T began are invisible to T — they create new row versions with later timestamps, but T only accesses versions that existed at its start. This eliminates the 'non-repeatable read' anomaly (where the same read within a transaction returns different values) without requiring any read locks. The consistency of the snapshot view is guaranteed until T commits or aborts."

- question: "MVCC completely eliminates all conflicts between concurrent transactions — since readers never block writers and writers never block readers, no transaction ever needs to be aborted due to concurrent activity."
  type: true-false
  answer: false
  explanation: "MVCC eliminates read-write conflicts but not write-write conflicts. If two concurrent transactions both attempt to update the same row, the database detects that the second writer is modifying a row that has already been updated by another committed transaction since the second writer's snapshot. The database cannot silently apply both updates, so it aborts one transaction (typically the second writer) and forces it to retry. MVCC's promise is that readers never block writers and writers never block readers — but when two writers target the same row, a conflict is unavoidable and one must lose."

- question: "Explain how MVCC allows readers and writers to proceed concurrently without blocking each other, and describe the operational cost of this approach."
  type: short-answer
  answer: "MVCC avoids blocking by keeping multiple versions of each row rather than overwriting data in place. When a writer updates a row, it creates a new version with a new timestamp and marks the old version as deleted; the old version is not immediately removed. When a reader queries the row, the database returns the version that was current at the reader's start timestamp — not the latest version. Because readers and writers access different versions of the same row, neither needs to wait for the other. The operational cost is version bloat: old row versions accumulate until a background garbage collection process (e.g., PostgreSQL's VACUUM) identifies versions no longer needed by any active snapshot and reclaims their storage. Long-running transactions exacerbate this cost by keeping old snapshots alive and preventing garbage collection."
  explanation: "This tradeoff is fundamental to MVCC: you get high concurrency (no reader-writer blocking) at the cost of storage overhead and background maintenance complexity. Systems like PostgreSQL expose this tradeoff through configuration options (autovacuum aggressiveness) and monitoring metrics (dead tuple count, table bloat). Understanding why VACUUM is necessary — and what happens when it falls behind — requires understanding the MVCC mechanism that makes it necessary in the first place."
```

## Explainer

From your study of isolation levels, you know the core tension in concurrent database access: readers and writers can interfere with each other, causing anomalies like dirty reads, non-repeatable reads, and phantom rows. Traditional locking solves this by making transactions wait — a reader blocks writers, a writer blocks readers. This is safe but kills performance under high concurrency. **Multiversion Concurrency Control (MVCC)** takes a fundamentally different approach: instead of making transactions wait, it gives each transaction its own consistent **snapshot** of the database, so readers never block writers and writers never block readers.

The mechanism works by keeping **multiple versions** of each row. When a transaction updates a row, it does not overwrite the existing data. Instead, it creates a new version of the row and marks the old version with a deletion timestamp. Each version carries metadata: the transaction ID that created it and (when applicable) the transaction ID that deleted or replaced it. When a transaction reads a row, the database does not simply return the latest version — it returns the version that was current as of that transaction's **start timestamp**. This means that even if another transaction modifies or deletes the row after your transaction started, you continue to see the data as it existed at the moment your transaction began. You are reading from a frozen snapshot.

Consider a concrete example: Transaction A starts at timestamp 100 and reads a customer's balance as $500. Transaction B starts at timestamp 101, updates the balance to $600, and commits. If Transaction A reads the balance again, it still sees $500 — it only sees versions created before timestamp 100. This is **snapshot isolation** in action, and it eliminates dirty reads and non-repeatable reads without any locking. Write-write conflicts are still handled: if Transaction A also tries to update the same row, the database detects the conflict (another committed transaction modified this row since A's snapshot) and typically aborts Transaction A, forcing it to retry.

The cost of MVCC is **version bloat**. Because old versions are retained as long as any active transaction might need them, the database accumulates obsolete row versions over time. A background process called **garbage collection** (or **vacuuming**, in PostgreSQL's terminology) periodically identifies versions that are no longer visible to any running transaction and reclaims their storage. If garbage collection falls behind — for example, due to a long-running transaction that pins an old snapshot — the table bloats with dead versions, degrading both storage efficiency and scan performance. This is why PostgreSQL's `VACUUM` process and autovacuum settings are critical for operational health, and why long-running transactions in MVCC systems are more dangerous than they might appear.
