---
id: concurrency-control-databases
title: Concurrency Control in Databases
domain: computer-science
course: databases
prerequisites:
- id: acid-properties
  type: hard
- id: threads-and-concurrency
  type: soft
- id: mutex-and-locks
  type: soft
builds-toward:
- two-phase-locking
- database-deadlocks
tags:
- concurrency control
- isolation levels
- dirty read
- phantom read
- MVCC
- serializability
stage: formal-systems
status: draft
---

# Concurrency Control in Databases

## Core Idea
Concurrency control ensures that concurrent transactions produce results equivalent to some serial execution, preventing read anomalies: dirty reads (reading uncommitted data), non-repeatable reads (a row changes between two reads in the same transaction), and phantom reads (new rows matching a predicate appear between reads). The SQL standard defines four isolation levels — READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE — that progressively prevent more anomalies at increasing performance cost. Multi-Version Concurrency Control (MVCC) allows readers to see a consistent snapshot without blocking writers by maintaining multiple versions of each row.

## How It's Best Learned
Reproduce read anomalies experimentally with two database sessions: start a transaction in one, modify data, then read from the other before committing. Switch isolation levels and observe which anomalies are prevented.

## Common Misconceptions
- Higher isolation levels don't prevent all concurrency bugs — application-level race conditions still require careful design.
- MVCC doesn't use locks for reads but still uses locks (or optimistic checks) for writes to prevent write-write conflicts.
- READ COMMITTED (the common default in PostgreSQL, Oracle) still allows non-repeatable reads within a single transaction.
