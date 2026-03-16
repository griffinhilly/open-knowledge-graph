---
id: write-ahead-logging
title: Write-Ahead Logging and Database Recovery
domain: computer-science
course: databases
prerequisites:
- id: acid-properties
  type: hard
- id: database-transactions
  type: hard
- id: file-system-concepts
  type: soft
tags:
- WAL
- write-ahead logging
- recovery
- durability
- REDO
- UNDO
- checkpointing
stage: formal-systems
status: validated
---

# Write-Ahead Logging and Database Recovery

## Core Idea
Write-Ahead Logging (WAL) ensures atomicity and durability by requiring that every modification be recorded in a sequential log file before being applied to data pages. On crash recovery, the database REDOs all changes from committed transactions not yet reflected in data files, and UNDOs all changes from transactions that were in-flight at crash time, restoring a consistent state. Checkpoints periodically flush dirty buffer pages to disk and record a safe restart point, bounding the amount of log that must be replayed during recovery.

## How It's Best Learned
Trace the WAL protocol through a simulated crash at various points (before commit, after commit but before flush, mid-write) to understand what REDO and UNDO must handle. Study the ARIES recovery algorithm at a conceptual level.

## Common Misconceptions
- WAL makes the log durable, not the data pages immediately — data pages may still reside in the buffer pool unflushed.
- Asynchronous WAL flushing (async commit in PostgreSQL) improves throughput but risks losing the most recent committed transactions on a crash.
- Checkpointing is an internal recovery optimization, not a backup — it does not support point-in-time restore.

## Explainer

You already understand that ACID transactions guarantee atomicity (all or nothing) and durability (committed data survives crashes). But how does a database actually deliver these guarantees when it can crash at any moment — mid-write, after updating some pages but not others, or right after acknowledging a commit? The answer is **Write-Ahead Logging (WAL)**: a deceptively simple protocol that underpins crash recovery in virtually every modern database.

The core rule is: **before any change is applied to a data page on disk, the description of that change must first be written to a sequential log file and that log record must be flushed to stable storage.** This is the "write-ahead" part — the log always leads the data. When you execute an UPDATE, the database writes a log record describing the change (old value, new value, transaction ID, page number), forces that record to disk, and only then is it safe to modify the actual data page. The data page itself might linger in the buffer pool in memory for a while before being written to disk — and that is perfectly fine, because the log already contains everything needed to reconstruct the change.

When a crash occurs, recovery proceeds in two phases. The **REDO phase** replays the log forward from the last checkpoint, reapplying all changes from committed transactions that may not have been flushed to data pages yet. This restores the effects of completed work. The **UNDO phase** reverses changes from transactions that were in progress but never committed at crash time — these partial changes may have reached data pages (since the buffer pool can flush dirty pages at any time), so they must be rolled back to maintain atomicity. After both phases complete, the database is in a consistent state: every committed transaction's effects are present, and every uncommitted transaction's effects are gone.

**Checkpoints** are the mechanism that keeps recovery time bounded. Without checkpoints, recovery would have to replay the entire log from the beginning of time. A checkpoint flushes all dirty buffer pages to disk and records a log sequence number marking a known-good state. On recovery, the database only needs to replay log records after the last checkpoint. In PostgreSQL, you can observe this directly: the `checkpoint_timeout` and `max_wal_size` settings control how often checkpoints occur, balancing recovery speed against I/O overhead during normal operation. More frequent checkpoints mean faster recovery but more background I/O; less frequent checkpoints mean longer recovery windows but smoother performance during steady-state operation.
