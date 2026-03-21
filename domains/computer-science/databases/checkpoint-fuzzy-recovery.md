---
id: checkpoint-fuzzy-recovery
title: 'Checkpointing: Sharp and Fuzzy Checkpoints'
domain: computer-science
course: databases
prerequisites:
- id: crash-recovery-undo-redo-logs
  type: hard
- id: write-ahead-logging-protocol-durability
  type: hard
tags:
- checkpoint
- fuzzy-checkpoint
- recovery-time
- log-truncation
stage: formal-systems
status: draft
---

# Checkpointing: Sharp and Fuzzy Checkpoints

## Core Idea
Checkpoints create known good states for faster recovery. Sharp checkpoints stop all activity and flush dirty pages, creating precise recovery points but causing long pauses. Fuzzy checkpoints allow transactions to continue while recording which pages are being flushed, reducing latency but complicating recovery. Checkpoints also truncate logs, discarding records for committed transactions, preventing infinite log growth.

## Questions

```yaml
- question: "After a fuzzy checkpoint, the database crashes. A junior engineer suggests replaying the log only from the checkpoint record's position, since 'the checkpoint marks a known good state.' What is wrong with this?"
  type: multiple-choice
  options:
    - "Nothing — this is exactly what recovery should do after any kind of checkpoint"
    - "Fuzzy checkpoints flush pages in the background while transactions continue modifying other pages, so the on-disk state at checkpoint time is not internally consistent — recovery must consult the checkpoint's dirty page table and active transaction list to find the true minimum recovery LSN"
    - "The checkpoint record position is not stored in the log, so recovery cannot locate it"
    - "Fuzzy checkpoints only apply to read-only transactions, so this procedure would miss updates from write transactions"
  answer: 1
  explanation: "This is the central distinction between sharp and fuzzy checkpoints. A sharp checkpoint pauses all activity and flushes everything, so the checkpoint record is a clean boundary — safe to replay from. A fuzzy checkpoint writes its record while dirty pages are still being flushed in the background, so some pre-checkpoint pages are on disk while others aren't. Recovery must use the dirty page table (which pages were being flushed and their recovery LSNs) and the active transaction list (which transactions were in-flight) embedded in the checkpoint record to compute the minimum LSN from which redo must start."

- question: "A developer argues: 'Checkpoints are only an optimization for recovery speed — they're not strictly necessary if we're willing to accept slow recovery after a crash.' What critical function does this miss?"
  type: multiple-choice
  options:
    - "Checkpoints are required for concurrency control — without them, transactions cannot acquire locks"
    - "Without checkpoints, the write-ahead log must retain every record ever written, because the system can never know which old records might be needed, causing the log to grow without bound"
    - "Without checkpoints, the buffer pool cannot evict dirty pages to disk"
    - "Checkpoints are required to enforce isolation levels above READ UNCOMMITTED"
  answer: 1
  explanation: "Log truncation is a second, equally critical function of checkpointing. The WAL guarantees durability only if every change is logged before being applied — but that produces a log that grows indefinitely. A checkpoint establishes a 'minimum recovery LSN': the earliest log record that could possibly be needed for crash recovery. All log records before that point can be safely archived or discarded. Without checkpoints, you can never establish this safe truncation point, and the log grows forever. Production systems process millions of transactions per day — an unbounded log would exhaust disk storage quickly."

- question: "A fuzzy checkpoint guarantees that all dirty pages in the buffer pool have been written to disk by the time the checkpoint record appears in the log."
  type: true-false
  answer: false
  explanation: "This describes a sharp checkpoint, not a fuzzy one. The entire point of fuzzy checkpointing is that the dirty page flush happens in the background after the checkpoint record is written, while transactions continue running. The checkpoint record captures which pages were dirty at the start of the flush and the positions of active transactions — it is a snapshot of what needs to be flushed, not a guarantee that flushing is complete. Recovery uses this information to determine what still needs to be applied from the log."

- question: "The minimum recovery LSN maintained by a database system determines the oldest log record that must be retained for crash recovery."
  type: true-false
  answer: true
  explanation: "The minimum recovery LSN (sometimes called the low-water mark) is derived from the checkpoint's dirty page table (the oldest recovery LSN of any dirty page that might not be on disk) and the active transaction table (the log position of the oldest active transaction's first record). Log records before this LSN cannot be needed for redo or undo of any in-progress or not-yet-flushed operation. This is what enables safe log truncation — any log record with an LSN below the minimum recovery LSN can be archived or discarded."

- question: "What information does a fuzzy checkpoint record contain, and why does crash recovery need each piece?"
  type: short-answer
  answer: "A fuzzy checkpoint record contains the dirty page table (which pages were dirty at checkpoint start and their recovery LSNs) and the active transaction table (which transactions were in progress and their last log record positions). Recovery needs the dirty page table to identify the earliest LSN from which redo must begin — any dirty page whose recovery LSN is earlier than this must be redone. Recovery needs the active transaction table to identify in-progress transactions that must be undone if they did not commit before the crash. Together, these two tables let the recovery algorithm (such as ARIES) determine the exact minimum LSN to start replaying from, rather than replaying the entire log."
  explanation: "The key is that a fuzzy checkpoint cannot be a clean boundary because pages are still being flushed while the record is written. The dirty page table and active transaction table capture the precise 'in-flight' state at checkpoint time, giving recovery the information needed to distinguish what's already safe on disk from what needs to be reapplied. Without these tables, recovery would have to replay from the beginning of time to be safe."
```

## Explainer

You already know that write-ahead logging (WAL) ensures durability by recording every change in a log before modifying the actual data pages, and that crash recovery replays or undoes log entries to restore the database to a consistent state. But consider what happens if the system has been running for months — the log could contain millions of entries. Replaying from the very beginning on every crash would be catastrophically slow. **Checkpointing** solves this by periodically creating a known-good synchronization point between the log and the data on disk, so recovery only needs to process log entries after the most recent checkpoint.

A **sharp checkpoint** (also called a consistent checkpoint) is the conceptually simple approach: pause all transaction processing, flush every dirty page in the buffer pool to disk, write a checkpoint record to the log, and then resume. After a sharp checkpoint, every committed transaction's changes are safely on disk, and recovery can ignore all log entries before the checkpoint record. The problem is obvious — the system is completely unavailable during the flush. If the buffer pool is large and many pages are dirty, this pause can last seconds or even minutes, which is unacceptable for production systems.

**Fuzzy checkpointing** eliminates the pause by allowing transactions to continue while dirty pages are flushed in the background. The checkpoint record notes which pages are dirty at the time the checkpoint begins and where each active transaction stands. Pages are then written to disk asynchronously while new transactions modify other pages freely. The tradeoff is that the checkpoint no longer represents a perfectly consistent snapshot — some pages on disk are from before the checkpoint, others from after. Recovery must account for this by using the checkpoint's dirty page list and active transaction table to determine exactly where to start replaying the log. The ARIES recovery algorithm, used in most commercial databases, is specifically designed to work with fuzzy checkpoints.

Checkpointing also serves a second critical function: **log truncation**. Without checkpoints, the WAL would grow without bound because you could never be sure which log records might be needed for recovery. A checkpoint establishes that all data up to a certain log sequence number (LSN) is safely on disk, so log records before that LSN can be archived or discarded. In practice, databases maintain a "minimum recovery LSN" derived from the checkpoint's record of the oldest active transaction and the oldest dirty page — no log record before this point is needed for crash recovery. This is what keeps the active log at a manageable size, even in systems that process millions of transactions per day.
