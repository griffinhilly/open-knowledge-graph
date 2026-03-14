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
