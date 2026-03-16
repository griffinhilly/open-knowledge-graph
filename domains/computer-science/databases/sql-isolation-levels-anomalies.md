---
id: sql-isolation-levels-anomalies
title: 'Transaction Isolation Levels: READ UNCOMMITTED to SERIALIZABLE'
domain: computer-science
course: databases
prerequisites:
- id: database-transactions
  type: hard
- id: transaction-properties-acid
  type: hard
- id: concurrency-control-databases
  type: hard
builds-toward:
- optimistic-concurrency-control-occ
- multiversion-concurrency-mvcc
tags:
- isolation-levels
- anomalies
- dirty-read
- phantom-read
- SERIALIZABLE
stage: formal-systems
status: draft
---

# Transaction Isolation Levels: READ UNCOMMITTED to SERIALIZABLE

## Core Idea
SQL isolation levels define how much concurrent transactions can interfere: READ UNCOMMITTED allows dirty reads, READ COMMITTED prevents dirty reads but allows non-repeatable reads, REPEATABLE READ prevents both but allows phantoms, and SERIALIZABLE provides complete isolation as if transactions ran sequentially. Higher isolation prevents more anomalies but reduces concurrency and throughput.

## Explainer

You already know that transactions must satisfy the ACID properties, and that isolation is the "I" — the guarantee that concurrent transactions do not interfere with each other in harmful ways. But full isolation (serializability) is expensive in practice, so SQL defines four levels that let you trade correctness guarantees for performance. Understanding these levels means understanding the specific **anomalies** each one permits or prevents.

A **dirty read** occurs when transaction T1 reads data that T2 has written but not yet committed. If T2 rolls back, T1 has acted on data that never officially existed. This is the most dangerous anomaly, and only **READ UNCOMMITTED** allows it — a level rarely used in practice except for rough monitoring queries where approximate data is acceptable. Moving up to **READ COMMITTED**, the database guarantees you only see committed data. But a new anomaly becomes possible: the **non-repeatable read**. Transaction T1 reads a row, T2 modifies and commits that row, and when T1 reads the same row again, it gets a different value. Your transaction sees a consistent snapshot at each statement, but not across statements.

**REPEATABLE READ** fixes this by guaranteeing that if you read a row, reading it again within the same transaction returns the same value. But it permits **phantom reads**: T1 runs a query with a WHERE clause and gets a set of rows, T2 inserts a new row that matches the same WHERE clause and commits, and when T1 re-runs the query, a new row appears that was not there before. The existing rows are stable, but the set of matching rows can change. Finally, **SERIALIZABLE** prevents all three anomalies — dirty reads, non-repeatable reads, and phantoms — by ensuring the result is equivalent to running the transactions one at a time.

The practical decision depends on your workload. Most production applications use READ COMMITTED (the default in PostgreSQL and Oracle) because it provides a reasonable balance: no dirty reads, good concurrency, and the anomalies it permits are manageable for most business logic. Financial calculations, inventory systems, or anything where reading stale or changing data mid-transaction could cause real harm may need REPEATABLE READ or SERIALIZABLE. The key insight is that higher isolation is not always better — it comes with costs in the form of lock contention, aborted transactions, and reduced throughput. Choose the weakest level that your application's correctness requirements can tolerate.
