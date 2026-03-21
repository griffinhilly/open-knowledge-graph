---
id: write-ahead-logging-protocol-durability
title: Write-Ahead Logging (WAL) and Durability Guarantees
domain: computer-science
course: databases
prerequisites:
- id: database-transactions
  type: hard
- id: transaction-properties-acid
  type: hard
builds-toward:
- crash-recovery-undo-redo
- checkpoint-fuzzy-recovery
tags:
- WAL
- logging
- durability
- redo-log
- force-log
stage: formal-systems
status: draft
---

# Write-Ahead Logging (WAL) and Durability Guarantees

## Core Idea
Write-Ahead Logging ensures durability by forcing log records to stable storage before corresponding data changes. Each modification generates a log record with transaction ID, operation type, and before/after values. The buffer pool can hold modified pages in memory, but the log guarantees that if a transaction committed, its effects survive system failure. Sequential log writes are optimized, making logging efficient despite synchronization requirements.

## Questions

```yaml
- question: "A transaction commits successfully. The database has written all its log records to disk but the corresponding data pages are still dirty in the memory buffer pool. The system crashes 1 second later. What happens to the committed transaction's changes?"
  type: multiple-choice
  options:
    - "The changes are lost — the data pages were never flushed to disk"
    - "The changes survive — the log records on disk allow the recovery process to redo the changes to the data pages"
    - "The changes are partially lost depending on which pages were flushed before the crash"
    - "The database rolls back the transaction since it can't verify completion"
  answer: 1
  explanation: "This is exactly what WAL is designed for. The rule is: log records must be on stable storage before a commit is acknowledged. Once the log is durable, the data pages can stay dirty in memory indefinitely — after a crash, the recovery process reads the log and replays (redoes) all committed transactions whose data pages may not have been flushed. The log is the source of truth; the data files are just a cache that gets brought into sync during recovery."

- question: "Why does WAL improve database performance compared to forcing all modified data pages to disk at commit time?"
  type: multiple-choice
  options:
    - "WAL reduces the number of transactions that need to be committed per second"
    - "Log writes are sequential appends to one file, which are much faster than flushing scattered dirty pages at random disk locations"
    - "WAL compresses data before writing it, reducing the total bytes written to disk"
    - "WAL batches transactions together so each one doesn't need its own fsync call"
  answer: 1
  explanation: "The performance advantage is about I/O pattern. A transaction might modify pages scattered across many locations on disk — flushing all of them at commit time would require multiple random writes, which are expensive (especially on spinning disks). Log records, by contrast, are sequential appends to a single file — a few kilobytes written in one contiguous region. Sequential I/O is dramatically faster than random I/O. WAL trades a small sequential write at commit time for the freedom to defer expensive random page flushes to later, asynchronous checkpointing."

- question: "The WAL protocol requires that log records describing a modification must be written to stable storage before the corresponding data page is written to disk."
  type: true-false
  answer: true
  explanation: "This is precisely the WAL rule (also called the 'force-log-at-commit' rule, or the 'no steal / force' variants). The log must 'write ahead' of the data — it must be durable first. This ordering guarantee is what allows durability without requiring data pages to be flushed at commit time. If a data page were written to disk without its log record, a crash could leave an inconsistent data file with no way to reconstruct what should have been there."

- question: "After a crash, WAL recovery only needs to redo the changes of committed transactions — there is no need to undo anything because uncommitted transactions never wrote to disk."
  type: true-false
  answer: false
  explanation: "WAL systems typically use 'steal' buffer management — dirty pages from uncommitted transactions CAN be written to disk (evicted from the buffer pool early). This means uncommitted changes may be partially on disk at crash time. Recovery must therefore both redo committed transactions (whose log is durable but data pages may not be flushed) AND undo uncommitted transactions (whose partial writes may have made it to disk). This undo/redo duality is why WAL log records include both before-image and after-image values."

- question: "Explain the WAL rule in your own words and why it achieves durability without requiring data pages to be flushed to disk at commit time."
  type: short-answer
  answer: "WAL requires that before any data page modification reaches disk, the log record describing that modification must already be on stable storage. At commit, only the log records are forced to disk (via fsync). Because the log records survive, after a crash the recovery process can reconstruct the committed state by replaying them — even if data pages were never flushed. The log is the durable record of intent; the data files are just a derived representation that recovery brings back into sync."
  explanation: "The key insight is separating 'recording the intent' (sequential log write — cheap) from 'materializing the result' (random data page flush — expensive). By making the log durable at commit time and deferring data page flushes, WAL gets both durability (log survives crash) and performance (no expensive random I/O on the critical path). Recovery reconstructs data file state from the log when needed — which is rare enough that the cost is acceptable."
```

## Explainer

You already understand that ACID transactions promise **durability** — once a transaction commits, its changes survive even if the system crashes a millisecond later. But think about what that means physically. The database modifies pages in a memory buffer pool for performance, and those dirty pages get written back to disk eventually. If the system crashes before a dirty page is flushed, the committed changes are lost. **Write-Ahead Logging (WAL)** solves this problem with an elegant rule: before any data page is written to disk, the log records describing those changes must be written to stable storage first. Hence "write-ahead" — the log always leads.

The mechanics work like this. Every modification — an INSERT, UPDATE, or DELETE — generates a **log record** containing the transaction ID, which page was modified, and enough information to both redo the change (if committed but not yet flushed) and undo it (if not committed). These log records are appended sequentially to a log file. When a transaction commits, the database forces all its log records to disk with an `fsync` call. The actual data pages can remain dirty in memory as long as they want — what matters is that the log is durable.

Why is this efficient? Because log writes are **sequential appends**, which are dramatically faster than the random I/O required to flush scattered data pages across the disk. A single transaction might modify pages in ten different locations on disk, but its log records are just a few kilobytes appended to one file. The database trades a small amount of sequential I/O at commit time for the freedom to batch and optimize the much more expensive random data page writes later.

After a crash, the recovery process reads the log from the last **checkpoint** forward. It replays (redoes) all changes from committed transactions whose data pages may not have been flushed, and rolls back (undoes) any changes from transactions that were active but uncommitted at crash time. The log is the single source of truth — the data files on disk might be in any state, but the log tells the recovery process exactly what the database should look like. This is why WAL is the foundation of crash recovery in virtually every modern relational database, from PostgreSQL to MySQL's InnoDB to SQLite.
