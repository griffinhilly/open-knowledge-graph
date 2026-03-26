---
id: sql-isolation-levels-anomalies
title: 'Transaction Isolation Levels: READ UNCOMMITTED to SERIALIZABLE'
domain: computer-science
course: databases
prerequisites:
- id: database-transactions
  type: hard
- id: acid-properties
  type: hard
- id: concurrency-control-databases
  type: hard
builds-toward:
- optimistic-concurrency-control
- multi-version-concurrency-control
tags:
- isolation-levels
- anomalies
- dirty-read
- phantom-read
- SERIALIZABLE
stage: formal-systems
status: validated
---

# Transaction Isolation Levels: READ UNCOMMITTED to SERIALIZABLE

## Core Idea
SQL isolation levels define how much concurrent transactions can interfere: READ UNCOMMITTED allows dirty reads, READ COMMITTED prevents dirty reads but allows non-repeatable reads, REPEATABLE READ prevents both but allows phantoms, and SERIALIZABLE provides complete isolation as if transactions ran sequentially. Higher isolation prevents more anomalies but reduces concurrency and throughput.

## Questions

```yaml
- question: "Transaction T1 reads a row, then Transaction T2 modifies that row and commits, then T1 reads the same row again within its transaction and gets a different value. What anomaly is this, and what isolation level prevents it?"
  type: multiple-choice
  options:
    - "Dirty read; READ COMMITTED prevents it"
    - "Non-repeatable read; REPEATABLE READ prevents it"
    - "Phantom read; SERIALIZABLE prevents it"
    - "Dirty read; REPEATABLE READ prevents it"
  answer: 1
  explanation: "A non-repeatable read occurs when a transaction reads the same row twice and gets different values because another committed transaction modified it in between. READ COMMITTED prevents dirty reads (reads of uncommitted data) but still allows non-repeatable reads. REPEATABLE READ prevents this specific anomaly by holding read locks on rows already read. A phantom read, by contrast, involves new rows appearing in a query's result set — not existing rows changing."

- question: "A dashboard query runs at READ UNCOMMITTED to display near-real-time totals. A bulk-insert transaction begins, writes 50,000 rows, and then rolls back due to an error. What risk did the dashboard face?"
  type: multiple-choice
  options:
    - "The dashboard would see stale data from before the bulk insert started"
    - "The dashboard may have displayed totals that included the 50,000 rows that officially never existed after the rollback"
    - "The dashboard would be blocked and unable to query while the insert was in progress"
    - "The dashboard's query would fail with a lock timeout error"
  answer: 1
  explanation: "READ UNCOMMITTED allows dirty reads — the dashboard can see uncommitted data from in-progress transactions. If that transaction rolls back, the dashboard has acted on data that never officially existed. This is the defining danger of READ UNCOMMITTED and why it is rarely used in production outside of scenarios (like approximate monitoring) where acting on rolled-back data has no real consequences."

- question: "SERIALIZABLE isolation guarantees that concurrent transactions can seldom overlap in time — they physically execute one at a time."
  type: true-false
  answer: false
  explanation: "SERIALIZABLE guarantees that the *result* is equivalent to some serial (sequential) execution — but the transactions may still run concurrently. The database ensures the outcome is indistinguishable from some sequential ordering, using techniques like locking or multi-version concurrency control. Physical sequentiality is not required and would be enormously inefficient. The guarantee is about logical equivalence, not physical ordering."

- question: "At READ COMMITTED isolation, a transaction may read different values for the same row if it queries that row twice within a single transaction."
  type: true-false
  answer: true
  explanation: "READ COMMITTED guarantees you only see committed data, but only at the statement level — not for the entire transaction duration. If T1 reads a row, then T2 modifies and commits it, then T1 reads the row again, T1 sees the new value. This is a non-repeatable read, and it is explicitly permitted at READ COMMITTED. REPEATABLE READ closes this gap by holding read locks (or using snapshot isolation) for the duration of the transaction."

- question: "Why might a financial application choose REPEATABLE READ or SERIALIZABLE rather than the READ COMMITTED default, even though higher isolation reduces throughput?"
  type: short-answer
  answer: "Financial calculations often require consistent reads across multiple statements within a transaction — for example, computing a balance that is read, then used to validate a transfer, then updated. At READ COMMITTED, another transaction could modify the balance between those steps, causing the calculation to be based on stale or inconsistent data. The cost of acting on anomalous data (incorrect transfers, double-spending) outweighs the performance cost of higher isolation."
  explanation: "The key principle is 'choose the weakest isolation level your correctness requirements can tolerate.' For most read-heavy web applications, READ COMMITTED is fine — anomalies are rare and the consequences are minor. For systems where mid-transaction data changes could cause incorrect monetary decisions, the correctness requirement is stronger and justifies the performance cost of REPEATABLE READ or SERIALIZABLE."
```

## Explainer

You already know that transactions must satisfy the ACID properties, and that isolation is the "I" — the guarantee that concurrent transactions do not interfere with each other in harmful ways. But full isolation (serializability) is expensive in practice, so SQL defines four levels that let you trade correctness guarantees for performance. Understanding these levels means understanding the specific **anomalies** each one permits or prevents.

A **dirty read** occurs when transaction T1 reads data that T2 has written but not yet committed. If T2 rolls back, T1 has acted on data that never officially existed. This is the most dangerous anomaly, and only **READ UNCOMMITTED** allows it — a level rarely used in practice except for rough monitoring queries where approximate data is acceptable. Moving up to **READ COMMITTED**, the database guarantees you only see committed data. But a new anomaly becomes possible: the **non-repeatable read**. Transaction T1 reads a row, T2 modifies and commits that row, and when T1 reads the same row again, it gets a different value. Your transaction sees a consistent snapshot at each statement, but not across statements.

**REPEATABLE READ** fixes this by guaranteeing that if you read a row, reading it again within the same transaction returns the same value. But it permits **phantom reads**: T1 runs a query with a WHERE clause and gets a set of rows, T2 inserts a new row that matches the same WHERE clause and commits, and when T1 re-runs the query, a new row appears that was not there before. The existing rows are stable, but the set of matching rows can change. Finally, **SERIALIZABLE** prevents all three anomalies — dirty reads, non-repeatable reads, and phantoms — by ensuring the result is equivalent to running the transactions one at a time.

The practical decision depends on your workload. Most production applications use READ COMMITTED (the default in PostgreSQL and Oracle) because it provides a reasonable balance: no dirty reads, good concurrency, and the anomalies it permits are manageable for most business logic. Financial calculations, inventory systems, or anything where reading stale or changing data mid-transaction could cause real harm may need REPEATABLE READ or SERIALIZABLE. The key insight is that higher isolation is not always better — it comes with costs in the form of lock contention, aborted transactions, and reduced throughput. Choose the weakest level that your application's correctness requirements can tolerate.
