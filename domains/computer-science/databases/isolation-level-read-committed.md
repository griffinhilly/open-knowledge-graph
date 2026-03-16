---
id: isolation-level-read-committed
title: 'Isolation Level: READ COMMITTED'
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
builds-toward:
- nonrepeatable-read-anomaly
tags:
- isolation
- concurrency
- anomalies
stage: formal-systems
status: draft
---

# Isolation Level: READ COMMITTED

## Core Idea
READ COMMITTED prevents dirty reads by only reading committed data, but allows non-repeatable reads and phantom reads. It is the default level in many databases.

## How It's Best Learned
Observe how two concurrent sessions interact: the first reads data, the second modifies and commits, and the first re-reads and sees the change.

## Explainer

From your study of concurrency control, you know that transactions running simultaneously can interfere with each other in ways that produce incorrect results. Isolation levels are the database's way of letting you choose how much interference you are willing to tolerate in exchange for performance. **READ COMMITTED** is the most widely used default — it is the out-of-the-box isolation level in PostgreSQL, Oracle, and SQL Server — because it strikes a practical balance between safety and concurrency.

The guarantee READ COMMITTED provides is simple: your transaction will never see data that another transaction has written but not yet committed. This eliminates **dirty reads**, where you might act on data that gets rolled back moments later. Imagine transaction A updates an account balance from $1000 to $500, and before A commits, transaction B reads the balance and sees $500. If A then rolls back, B made a decision based on data that never actually existed. Under READ COMMITTED, B would still see $1000 — the last committed value — until A commits its change.

The mechanism behind this varies by database engine but typically involves one of two approaches. In lock-based implementations, a writer holds an exclusive lock on modified rows until commit, and readers block until the lock is released. In **multi-version concurrency control** (MVCC), which PostgreSQL and Oracle use, each write creates a new version of the row. Readers see the most recently committed version at the time of each individual statement, so they never block on writers and writers never block on readers. The MVCC approach is generally preferred because it allows much higher concurrency — readers and writers can operate on the same rows simultaneously without waiting.

The critical limitation of READ COMMITTED is what it does *not* prevent. If your transaction reads the same row twice, and another transaction commits a change to that row in between, your second read will see the new value. This is the **non-repeatable read** anomaly — your transaction sees a different snapshot at different points in time. It also does not prevent **phantom reads**, where new rows matching your query appear between two executions of the same query. For many applications — web requests, short-lived transactions, reporting on recent data — these anomalies are acceptable because each statement sees a consistent committed state. But for transactions that must see a frozen snapshot of the database (like generating a financial report while other transactions are posting entries), you need a higher isolation level like REPEATABLE READ or SERIALIZABLE.
