---
id: multi-version-concurrency-control
title: Multi-Version Concurrency Control (MVCC)
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
tags:
- concurrency
- mvcc
- read-consistency
stage: formal-systems
status: draft
---

# Multi-Version Concurrency Control (MVCC)

## Core Idea
MVCC maintains multiple versions of rows, allowing readers to access consistent snapshots without blocking writers. Each transaction sees data as of a snapshot timestamp, reducing lock contention.

## How It's Best Learned
Observe that in a database with MVCC (PostgreSQL, MySQL InnoDB), read operations do not block writes and vice versa, even without explicit locking.

## Common Misconceptions
MVCC still prevents write-write conflicts via locking; it only eliminates read-write blocking. Old versions are garbage-collected when no active transaction references them.
