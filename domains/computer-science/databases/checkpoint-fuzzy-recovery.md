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

## Explainer

You already know that write-ahead logging (WAL) ensures durability by recording every change in a log before modifying the actual data pages, and that crash recovery replays or undoes log entries to restore the database to a consistent state. But consider what happens if the system has been running for months — the log could contain millions of entries. Replaying from the very beginning on every crash would be catastrophically slow. **Checkpointing** solves this by periodically creating a known-good synchronization point between the log and the data on disk, so recovery only needs to process log entries after the most recent checkpoint.

A **sharp checkpoint** (also called a consistent checkpoint) is the conceptually simple approach: pause all transaction processing, flush every dirty page in the buffer pool to disk, write a checkpoint record to the log, and then resume. After a sharp checkpoint, every committed transaction's changes are safely on disk, and recovery can ignore all log entries before the checkpoint record. The problem is obvious — the system is completely unavailable during the flush. If the buffer pool is large and many pages are dirty, this pause can last seconds or even minutes, which is unacceptable for production systems.

**Fuzzy checkpointing** eliminates the pause by allowing transactions to continue while dirty pages are flushed in the background. The checkpoint record notes which pages are dirty at the time the checkpoint begins and where each active transaction stands. Pages are then written to disk asynchronously while new transactions modify other pages freely. The tradeoff is that the checkpoint no longer represents a perfectly consistent snapshot — some pages on disk are from before the checkpoint, others from after. Recovery must account for this by using the checkpoint's dirty page list and active transaction table to determine exactly where to start replaying the log. The ARIES recovery algorithm, used in most commercial databases, is specifically designed to work with fuzzy checkpoints.

Checkpointing also serves a second critical function: **log truncation**. Without checkpoints, the WAL would grow without bound because you could never be sure which log records might be needed for recovery. A checkpoint establishes that all data up to a certain log sequence number (LSN) is safely on disk, so log records before that LSN can be archived or discarded. In practice, databases maintain a "minimum recovery LSN" derived from the checkpoint's record of the oldest active transaction and the oldest dirty page — no log record before this point is needed for crash recovery. This is what keeps the active log at a manageable size, even in systems that process millions of transactions per day.
