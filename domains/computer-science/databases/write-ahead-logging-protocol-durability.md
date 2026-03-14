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
