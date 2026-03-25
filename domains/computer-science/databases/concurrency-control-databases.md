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
- id: mutual-exclusion-and-locks
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
status: validated
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

## Questions

```yaml
- question: "Transaction A reads a row, then Transaction B updates and commits that row before A finishes. When A reads the same row again, it gets the updated value. Which anomaly is this?"
  type: multiple-choice
  options: ["Dirty read", "Non-repeatable read", "Phantom read", "Lost update"]
  answer: 1
  explanation: "A non-repeatable read occurs when a transaction reads the same row twice and gets different values because another transaction committed an update in between. A dirty read would involve reading B's changes *before* B commits. A phantom read involves new rows appearing, not changed existing rows."

- question: "READ COMMITTED isolation level prevents non-repeatable reads."
  type: true-false
  answer: false
  explanation: "READ COMMITTED only prevents dirty reads (reading uncommitted data). It still allows non-repeatable reads because each statement sees a fresh snapshot, so the same row can return different values in two reads within the same transaction. REPEATABLE READ is required to prevent this anomaly."

- question: "How does MVCC allow readers and writers to operate concurrently without blocking each other?"
  type: short-answer
  answer: "MVCC keeps multiple versions of each row. Readers see a consistent snapshot from the start of their transaction (an older version), while writers create new row versions. Because reads never access the same version a writer is modifying, neither blocks the other."
  explanation: "This contrasts with lock-based concurrency where readers and writers compete for the same lock. MVCC's snapshot isolation means long-running read queries (like analytics) do not block writes, which is critical for throughput in production systems like PostgreSQL."
```

## Explainer

When two transactions execute against the same database simultaneously, their reads and writes can interleave in ways that produce surprising results — results that would never occur if the transactions ran one after the other. Concurrency control defines how the database manages these interactions. The goal is **serializability**: the outcome of concurrent transactions should be equivalent to *some* serial ordering, even though they actually ran in parallel.

Three classic read anomalies mark the failure modes. A **dirty read** occurs when transaction A reads data that transaction B has written but not yet committed — if B rolls back, A has read data that never officially existed. A **non-repeatable read** occurs when A reads a row, B updates and commits it, and A reads it again to get a different value within the same transaction. A **phantom read** is similar but involves rows disappearing or appearing: A queries for all rows matching a predicate, B inserts a matching row and commits, and A's second query finds a different set of rows.

The SQL standard defines four **isolation levels** that progressively prevent more anomalies. READ UNCOMMITTED allows all three anomalies (rarely used). READ COMMITTED (the default in PostgreSQL and Oracle) prevents dirty reads. REPEATABLE READ additionally prevents non-repeatable reads. SERIALIZABLE prevents all three, including phantom reads, at the cost of reduced throughput and potential transaction aborts. Choosing an isolation level is always a tradeoff between data consistency and performance.

**MVCC (Multi-Version Concurrency Control)** is the mechanism most modern databases use to implement these guarantees efficiently. Instead of locking rows so readers and writers block each other, MVCC maintains multiple timestamped versions of each row. When a transaction starts, it receives a snapshot timestamp and reads whichever row version was current at that moment. Writers create new versions without overwriting old ones. Because readers and writers operate on different versions, they never block each other — a long-running read query does not stall writes, and writes do not interrupt reads.

Understanding concurrency control ties directly back to the **Isolation** property in ACID: each transaction should appear to execute in isolation from others. The isolation levels are essentially a dial that trades more isolation for more performance. Most applications run at READ COMMITTED and handle residual anomalies at the application level, but correctness-critical operations (bank transfers, inventory updates) require REPEATABLE READ or SERIALIZABLE to avoid subtle bugs.

