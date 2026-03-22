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

## Questions

```yaml
- question: "A database crashes immediately after a transaction commits and its log record is flushed to disk, but before the data pages are written to disk. What happens during recovery?"
  type: multiple-choice
  options:
    - "The committed data is lost — it never reached disk"
    - "The REDO phase replays the log to apply the committed changes to data pages"
    - "The UNDO phase rolls back the transaction since data pages were never updated"
    - "Nothing is needed — the commit acknowledgment guarantees data was written to disk"
  answer: 1
  explanation: "This is exactly the scenario WAL is designed for. The log record was flushed before the data pages (that is the 'write-ahead' guarantee), so the REDO phase can replay the committed change and apply it to the data pages. Option A is wrong because the log is durable even though data pages are not. Option C is wrong because UNDO is for *uncommitted* transactions. Option D mistakes the commit acknowledgment — which only guarantees the log was written — for a guarantee that data pages are on disk."

- question: "Which statement best describes the 'write-ahead' rule in WAL?"
  type: multiple-choice
  options:
    - "Data pages must be written to disk before the transaction can commit"
    - "Log records must be flushed to stable storage before the corresponding data pages are modified on disk"
    - "The client must be acknowledged before any log records are written"
    - "A checkpoint must be recorded before any data modification is allowed"
  answer: 1
  explanation: "The 'write-ahead' constraint means the log always leads the data: a log record describing a change must be durably written before the actual data page can be modified on disk. This is what makes REDO recovery possible — if a crash occurs before data pages flush, the log still has a complete record. Option A reverses the rule (data pages are intentionally allowed to lag behind). Options C and D describe no real WAL requirement."

- question: "A WAL checkpoint serves as a backup point: if a crash occurs after the checkpoint, the database can restore to the exact state captured at checkpoint time."
  type: true-false
  answer: false
  explanation: "Checkpoints are a recovery optimization, not backups. A checkpoint flushes dirty buffer pages to disk and records a log sequence number, so recovery only needs to replay log records *after* the checkpoint — bounding recovery time. But a checkpoint does not create a restorable snapshot; the database still requires REDO and UNDO of subsequent log records to reach a consistent state. Point-in-time restore requires separate backup mechanisms (e.g., base backups plus archived WAL logs)."

- question: "After WAL-based crash recovery completes, every transaction that had committed before the crash will have all its changes reflected in the data files."
  type: true-false
  answer: true
  explanation: "This is precisely what the REDO phase guarantees. The REDO phase replays all log records from committed transactions that may not have been flushed to data pages before the crash. After REDO completes, every committed transaction's effects are present in the data files. The UNDO phase then removes effects of uncommitted transactions, leaving the database in a consistent state where committed = durable and uncommitted = absent."

- question: "Why must WAL crash recovery include an UNDO phase, and what problem would occur if it were skipped?"
  type: short-answer
  answer: "The buffer pool can flush dirty pages to disk at any time — even for transactions that have not yet committed. If the database crashes mid-transaction, some of its partial writes may already be in the data files. Without UNDO, those partial changes would remain, violating atomicity (the all-or-nothing guarantee). The UNDO phase reverses changes from every transaction that was in-flight at crash time, ensuring no partially-committed work survives in the data files."
  explanation: "This is the key subtlety of WAL: durability (REDO) is needed because committed changes may not have hit disk yet, and atomicity (UNDO) is needed because uncommitted changes may have hit disk already. Both phases are required because the buffer pool can flush pages in either direction relative to commit boundaries. A system that only did REDO would be durable but not atomic; one that only did UNDO would be atomic but not durable."
```

## Explainer

You already understand that ACID transactions guarantee atomicity (all or nothing) and durability (committed data survives crashes). But how does a database actually deliver these guarantees when it can crash at any moment — mid-write, after updating some pages but not others, or right after acknowledging a commit? The answer is **Write-Ahead Logging (WAL)**: a deceptively simple protocol that underpins crash recovery in virtually every modern database.

The core rule is: **before any change is applied to a data page on disk, the description of that change must first be written to a sequential log file and that log record must be flushed to stable storage.** This is the "write-ahead" part — the log always leads the data. When you execute an UPDATE, the database writes a log record describing the change (old value, new value, transaction ID, page number), forces that record to disk, and only then is it safe to modify the actual data page. The data page itself might linger in the buffer pool in memory for a while before being written to disk — and that is perfectly fine, because the log already contains everything needed to reconstruct the change.

When a crash occurs, recovery proceeds in two phases. The **REDO phase** replays the log forward from the last checkpoint, reapplying all changes from committed transactions that may not have been flushed to data pages yet. This restores the effects of completed work. The **UNDO phase** reverses changes from transactions that were in progress but never committed at crash time — these partial changes may have reached data pages (since the buffer pool can flush dirty pages at any time), so they must be rolled back to maintain atomicity. After both phases complete, the database is in a consistent state: every committed transaction's effects are present, and every uncommitted transaction's effects are gone.

**Checkpoints** are the mechanism that keeps recovery time bounded. Without checkpoints, recovery would have to replay the entire log from the beginning of time. A checkpoint flushes all dirty buffer pages to disk and records a log sequence number marking a known-good state. On recovery, the database only needs to replay log records after the last checkpoint. In PostgreSQL, you can observe this directly: the `checkpoint_timeout` and `max_wal_size` settings control how often checkpoints occur, balancing recovery speed against I/O overhead during normal operation. More frequent checkpoints mean faster recovery but more background I/O; less frequent checkpoints mean longer recovery windows but smoother performance during steady-state operation.
