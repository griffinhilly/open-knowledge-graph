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
