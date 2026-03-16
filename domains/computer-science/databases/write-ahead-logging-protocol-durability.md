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

## Explainer

You already understand that ACID transactions promise **durability** — once a transaction commits, its changes survive even if the system crashes a millisecond later. But think about what that means physically. The database modifies pages in a memory buffer pool for performance, and those dirty pages get written back to disk eventually. If the system crashes before a dirty page is flushed, the committed changes are lost. **Write-Ahead Logging (WAL)** solves this problem with an elegant rule: before any data page is written to disk, the log records describing those changes must be written to stable storage first. Hence "write-ahead" — the log always leads.

The mechanics work like this. Every modification — an INSERT, UPDATE, or DELETE — generates a **log record** containing the transaction ID, which page was modified, and enough information to both redo the change (if committed but not yet flushed) and undo it (if not committed). These log records are appended sequentially to a log file. When a transaction commits, the database forces all its log records to disk with an `fsync` call. The actual data pages can remain dirty in memory as long as they want — what matters is that the log is durable.

Why is this efficient? Because log writes are **sequential appends**, which are dramatically faster than the random I/O required to flush scattered data pages across the disk. A single transaction might modify pages in ten different locations on disk, but its log records are just a few kilobytes appended to one file. The database trades a small amount of sequential I/O at commit time for the freedom to batch and optimize the much more expensive random data page writes later.

After a crash, the recovery process reads the log from the last **checkpoint** forward. It replays (redoes) all changes from committed transactions whose data pages may not have been flushed, and rolls back (undoes) any changes from transactions that were active but uncommitted at crash time. The log is the single source of truth — the data files on disk might be in any state, but the log tells the recovery process exactly what the database should look like. This is why WAL is the foundation of crash recovery in virtually every modern relational database, from PostgreSQL to MySQL's InnoDB to SQLite.
