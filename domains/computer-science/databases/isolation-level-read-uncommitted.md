---
id: isolation-level-read-uncommitted
title: 'Isolation Level: READ UNCOMMITTED (Dirty Reads)'
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
builds-toward:
- dirty-read-anomaly
tags:
- isolation
- concurrency
- anomalies
stage: formal-systems
status: draft
---

# Isolation Level: READ UNCOMMITTED (Dirty Reads)

## Core Idea
READ UNCOMMITTED is the lowest isolation level; it allows transactions to read uncommitted (dirty) data from other transactions, offering maximum concurrency but minimum isolation.

## Explainer

You already understand concurrency control in databases — the idea that multiple transactions may execute simultaneously and the database must manage conflicts between them. Isolation levels define how much one transaction can see of another's uncommitted work. **READ UNCOMMITTED** is the lowest isolation level, where a transaction can read data that another transaction has modified but not yet committed. This produces **dirty reads** — reads of data that may never actually persist.

Consider a concrete scenario. Transaction A updates an account balance from $1000 to $500 (a withdrawal) but has not yet committed. Under READ UNCOMMITTED, Transaction B can read that $500 balance immediately. If Transaction A then rolls back (perhaps the withdrawal failed validation), the balance reverts to $1000 — but Transaction B already acted on the $500 value, which never actually existed in any committed state. B's computation was based on phantom data. This is a dirty read, and it can cause cascading errors: if B used that balance to approve a loan, deny a transaction, or generate a report, all those downstream decisions rest on data that was never finalized.

Why would anyone use READ UNCOMMITTED? The answer is **performance**. Because transactions at this level do not need to acquire read locks or check whether data has been committed, they impose virtually no overhead on concurrent writers. The database never blocks a reader waiting for a writer to finish. For certain workloads — approximate analytics queries on massive tables, progress monitoring dashboards, or rough row counts — the small risk of reading uncommitted data is an acceptable tradeoff for dramatically reduced lock contention and faster query execution. A reporting query that scans millions of rows to compute an approximate average does not need perfect accuracy, and running it at READ UNCOMMITTED avoids blocking the production transactions that are doing the actual writes.

In the hierarchy of SQL isolation levels — READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, and SERIALIZABLE — READ UNCOMMITTED sits at the bottom. Each level above it prevents additional anomalies at the cost of more locking or versioning overhead. READ COMMITTED prevents dirty reads by only showing committed data. REPEATABLE READ additionally prevents non-repeatable reads. SERIALIZABLE prevents all anomalies. Most production applications use READ COMMITTED or higher as their default. READ UNCOMMITTED should be understood as a deliberate, informed choice to sacrifice correctness guarantees for concurrency — never used carelessly, and never used for transactions that make decisions requiring accurate data.
