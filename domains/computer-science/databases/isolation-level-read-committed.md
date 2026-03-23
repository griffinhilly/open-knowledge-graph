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
status: validated
---

# Isolation Level: READ COMMITTED

## Core Idea
READ COMMITTED prevents dirty reads by only reading committed data, but allows non-repeatable reads and phantom reads. It is the default level in many databases.

## How It's Best Learned
Observe how two concurrent sessions interact: the first reads data, the second modifies and commits, and the first re-reads and sees the change.

## Questions

```yaml
- question: "Transaction A reads a row showing a balance of $1,000. Transaction B then updates that balance to $500 and commits. Transaction A reads the same row again. Under READ COMMITTED, what does transaction A see on its second read?"
  type: multiple-choice
  options:
    - "$1,000 — READ COMMITTED ensures a consistent snapshot for the entire transaction"
    - "$500 — each statement sees the latest committed data at the time it runs"
    - "An error — concurrent reads and writes are blocked under READ COMMITTED"
    - "$1,000 — READ COMMITTED only prevents dirty reads, not committed changes"
  answer: 1
  explanation: "Under READ COMMITTED, each individual statement sees the most recently committed version of data at the time that statement executes — not a frozen snapshot from when the transaction began. So transaction A's second read sees $500, the newly committed value. This is the non-repeatable read anomaly: the same query returns different results within one transaction. Option D is a common confusion — READ COMMITTED does prevent dirty reads, but it does NOT freeze the snapshot across statements, which is why non-repeatable reads are still possible."

- question: "Which of the following is NOT prevented by the READ COMMITTED isolation level?"
  type: multiple-choice
  options:
    - "Reading data that another transaction has written but not yet committed"
    - "Acting on a value that will later be rolled back by another transaction"
    - "Seeing different values for the same row in two reads within one transaction"
    - "Reading a version of a row created by a transaction that subsequently aborted"
  answer: 2
  explanation: "Options A, B, and D all describe dirty reads — reading uncommitted data — which READ COMMITTED specifically prevents. Option C describes a non-repeatable read: two reads of the same row within one transaction return different committed values because another transaction committed a change in between. READ COMMITTED does NOT prevent this. To prevent non-repeatable reads, you need a higher isolation level like REPEATABLE READ or SERIALIZABLE."

- question: "Under READ COMMITTED, a transaction always sees the same data every time it reads the same row."
  type: true-false
  answer: false
  explanation: "This is the key limitation of READ COMMITTED. While it guarantees you only see committed data, it does not guarantee consistency across multiple reads within the same transaction. Another transaction can commit a change between your first and second read of the same row, causing you to see different values — the non-repeatable read anomaly. For a frozen, consistent snapshot across all reads in a transaction, you need REPEATABLE READ or SERIALIZABLE."

- question: "READ COMMITTED prevents dirty reads by ensuring that a transaction only ever reads data that has already been committed by other transactions."
  type: true-false
  answer: true
  explanation: "This is precisely the guarantee READ COMMITTED provides. In MVCC-based databases like PostgreSQL, each statement sees the most recently committed version of each row at the time the statement runs. In lock-based implementations, readers wait for exclusive write locks to be released before reading. Either way, the result is the same: you never see uncommitted data that might later be rolled back. This is the defining property that distinguishes READ COMMITTED from READ UNCOMMITTED (which allows dirty reads)."

- question: "Explain why READ COMMITTED prevents dirty reads but not non-repeatable reads, and describe a scenario where this distinction matters."
  type: short-answer
  answer: "READ COMMITTED ensures each statement sees only committed data at the moment it runs. This prevents dirty reads because you never act on data from an in-progress transaction that hasn't committed. However, if you read the same row twice within your transaction, the second read takes a fresh snapshot — so if another transaction commits a change in between, you see the new value. This is a non-repeatable read. A scenario where it matters: a transaction reads an account balance, performs a calculation, then re-reads the balance before writing. If another transaction commits a deposit in between, the two reads disagree, and the calculation may be wrong."
  explanation: "The core distinction is between statement-level consistency (READ COMMITTED) and transaction-level consistency (REPEATABLE READ). READ COMMITTED gives you a fresh snapshot per statement — great for concurrency, but it means the same query can return different results within one transaction. Applications that read-then-act (especially those that read multiple times) are vulnerable to non-repeatable read anomalies. Financial report generation is a classic example: if rows change between the start and end of a large aggregation query, the totals may be internally inconsistent."
```

## Explainer

From your study of concurrency control, you know that transactions running simultaneously can interfere with each other in ways that produce incorrect results. Isolation levels are the database's way of letting you choose how much interference you are willing to tolerate in exchange for performance. **READ COMMITTED** is the most widely used default — it is the out-of-the-box isolation level in PostgreSQL, Oracle, and SQL Server — because it strikes a practical balance between safety and concurrency.

The guarantee READ COMMITTED provides is simple: your transaction will never see data that another transaction has written but not yet committed. This eliminates **dirty reads**, where you might act on data that gets rolled back moments later. Imagine transaction A updates an account balance from $1000 to $500, and before A commits, transaction B reads the balance and sees $500. If A then rolls back, B made a decision based on data that never actually existed. Under READ COMMITTED, B would still see $1000 — the last committed value — until A commits its change.

The mechanism behind this varies by database engine but typically involves one of two approaches. In lock-based implementations, a writer holds an exclusive lock on modified rows until commit, and readers block until the lock is released. In **multi-version concurrency control** (MVCC), which PostgreSQL and Oracle use, each write creates a new version of the row. Readers see the most recently committed version at the time of each individual statement, so they never block on writers and writers never block on readers. The MVCC approach is generally preferred because it allows much higher concurrency — readers and writers can operate on the same rows simultaneously without waiting.

The critical limitation of READ COMMITTED is what it does *not* prevent. If your transaction reads the same row twice, and another transaction commits a change to that row in between, your second read will see the new value. This is the **non-repeatable read** anomaly — your transaction sees a different snapshot at different points in time. It also does not prevent **phantom reads**, where new rows matching your query appear between two executions of the same query. For many applications — web requests, short-lived transactions, reporting on recent data — these anomalies are acceptable because each statement sees a consistent committed state. But for transactions that must see a frozen snapshot of the database (like generating a financial report while other transactions are posting entries), you need a higher isolation level like REPEATABLE READ or SERIALIZABLE.
