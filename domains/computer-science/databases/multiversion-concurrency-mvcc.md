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
status: draft
---

# Multiversion Concurrency Control (MVCC) and Snapshot Isolation

## Core Idea
MVCC maintains multiple versions of data items, each with creation and deletion timestamps. Readers access versions appropriate for their transaction timestamp without blocking writers; writers create new versions without invalidating readers. This eliminates most read-write conflicts. PostgreSQL, Oracle, and others use MVCC variants. Garbage collection removes old versions no longer needed by any transaction, managing version bloat.

## Explainer

From your study of isolation levels, you know the core tension in concurrent database access: readers and writers can interfere with each other, causing anomalies like dirty reads, non-repeatable reads, and phantom rows. Traditional locking solves this by making transactions wait — a reader blocks writers, a writer blocks readers. This is safe but kills performance under high concurrency. **Multiversion Concurrency Control (MVCC)** takes a fundamentally different approach: instead of making transactions wait, it gives each transaction its own consistent **snapshot** of the database, so readers never block writers and writers never block readers.

The mechanism works by keeping **multiple versions** of each row. When a transaction updates a row, it does not overwrite the existing data. Instead, it creates a new version of the row and marks the old version with a deletion timestamp. Each version carries metadata: the transaction ID that created it and (when applicable) the transaction ID that deleted or replaced it. When a transaction reads a row, the database does not simply return the latest version — it returns the version that was current as of that transaction's **start timestamp**. This means that even if another transaction modifies or deletes the row after your transaction started, you continue to see the data as it existed at the moment your transaction began. You are reading from a frozen snapshot.

Consider a concrete example: Transaction A starts at timestamp 100 and reads a customer's balance as $500. Transaction B starts at timestamp 101, updates the balance to $600, and commits. If Transaction A reads the balance again, it still sees $500 — it only sees versions created before timestamp 100. This is **snapshot isolation** in action, and it eliminates dirty reads and non-repeatable reads without any locking. Write-write conflicts are still handled: if Transaction A also tries to update the same row, the database detects the conflict (another committed transaction modified this row since A's snapshot) and typically aborts Transaction A, forcing it to retry.

The cost of MVCC is **version bloat**. Because old versions are retained as long as any active transaction might need them, the database accumulates obsolete row versions over time. A background process called **garbage collection** (or **vacuuming**, in PostgreSQL's terminology) periodically identifies versions that are no longer visible to any running transaction and reclaims their storage. If garbage collection falls behind — for example, due to a long-running transaction that pins an old snapshot — the table bloats with dead versions, degrading both storage efficiency and scan performance. This is why PostgreSQL's `VACUUM` process and autovacuum settings are critical for operational health, and why long-running transactions in MVCC systems are more dangerous than they might appear.
