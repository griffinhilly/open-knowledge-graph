---
id: concurrency-isolation-control
title: Concurrency Control and Isolation Levels
domain: computer-science
course: databases
prerequisites:
- id: transaction-properties-acid
  type: hard
tags:
- concurrency
- isolation
- locking
- MVCC
- serializability
stage: formal-systems
status: draft
---

# Concurrency Control and Isolation Levels

## Core Idea
Concurrency control ensures multiple concurrent transactions do not interfere with each other. Isolation levels define the degree of isolation: read uncommitted, read committed, repeatable read, serializable. Mechanisms include pessimistic locking (locks), optimistic locking (version checks), and multi-version concurrency control (MVCC). Choosing appropriate isolation is crucial for correctness and performance.

## How It's Best Learned
Trace execution of concurrent transactions at different isolation levels, identify phenomena (dirty reads, non-repeatable reads, phantoms), understand locking protocols, and analyze trade-offs between isolation strength and concurrency.

## Common Misconceptions
Higher isolation levels are not always better—they reduce concurrency. Serializable isolation can bottleneck performance. Most applications use read committed as a pragmatic balance.

## Explainer

You already know from ACID properties that the "I" — isolation — means each transaction should behave as if it were running alone, even when many transactions execute simultaneously. In practice, full isolation is expensive, so databases offer a spectrum of **isolation levels** that trade correctness guarantees for performance. Understanding this spectrum is essential for building applications that are both correct and responsive under concurrent load.

The SQL standard defines four isolation levels, each preventing an increasingly dangerous set of anomalies. **Read Uncommitted** is the weakest: a transaction can see uncommitted changes from other transactions (a **dirty read**). This is rarely used because reading data that might be rolled back leads to nonsensical results. **Read Committed** prevents dirty reads — you only see data that has been committed — but if you read the same row twice within your transaction, another committed transaction might have changed it in between, producing a **non-repeatable read**. **Repeatable Read** prevents both dirty and non-repeatable reads by ensuring that any row you read will not change for the duration of your transaction. However, new rows matching your query's conditions can still appear — these **phantom reads** occur when another transaction inserts rows that satisfy a WHERE clause you already evaluated. **Serializable** prevents all three anomalies, guaranteeing that the outcome is equivalent to running the transactions one at a time in some serial order.

Databases enforce these levels through different mechanisms. **Pessimistic locking** acquires locks on data before accessing it: shared locks for reads, exclusive locks for writes. A transaction holds its locks until it commits or rolls back, blocking other transactions that need conflicting access. This is simple but can cause **deadlocks** when two transactions each hold a lock the other needs. **Optimistic concurrency control** takes a different approach: transactions proceed without locks and check at commit time whether any conflicts occurred. If another transaction modified the same data, the committing transaction is rolled back and retried. **Multi-version concurrency control** (MVCC), used by PostgreSQL and many modern databases, keeps multiple versions of each row. Readers see a snapshot of the database as of their transaction's start time, so they never block writers and writers never block readers. This dramatically improves throughput for read-heavy workloads.

The practical choice of isolation level depends on your application's tolerance for anomalies. Most production applications default to **Read Committed** because it prevents the worst anomaly (dirty reads) while allowing high concurrency. Financial applications or inventory systems that must prevent double-spending or overselling may require Repeatable Read or Serializable. The key insight is that stronger isolation is not "better" in an absolute sense — it is a tradeoff. Serializable isolation may force transactions to wait or abort, reducing throughput. The right level is the weakest one that still guarantees your application's correctness requirements.
