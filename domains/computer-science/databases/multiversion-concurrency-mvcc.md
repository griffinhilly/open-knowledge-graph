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
