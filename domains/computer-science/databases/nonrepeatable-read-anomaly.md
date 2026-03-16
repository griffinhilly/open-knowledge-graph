---
id: nonrepeatable-read-anomaly
title: Non-Repeatable Read Anomaly
domain: computer-science
course: databases
prerequisites:
- id: isolation-level-read-committed
  type: hard
tags:
- concurrency
- anomalies
- isolation-problems
stage: formal-systems
status: draft
---

# Non-Repeatable Read Anomaly

## Core Idea
A non-repeatable read occurs when a transaction reads a row, another transaction modifies it, and the first transaction re-reads the same row and sees different data.

## Explainer

You already understand that under READ COMMITTED isolation, a transaction only sees data that has been committed — no dirty reads. But READ COMMITTED makes a subtle promise that is weaker than many people assume: it guarantees a consistent snapshot *per statement*, not per transaction. Each SQL statement you execute within a transaction sees the latest committed data at the moment *that statement* begins. If another transaction commits a change between your first and second SELECT, your second SELECT sees the new value. This is the **non-repeatable read** anomaly.

Here is a concrete scenario. Suppose you are building a banking application, and transaction T1 needs to check an account balance twice during its work — first to verify the account has sufficient funds, and later to compute a transfer amount. T1 reads the balance and sees $1000. Meanwhile, transaction T2 withdraws $800 and commits. When T1 reads the balance again, it now sees $200. T1's logic assumed the balance was $1000 throughout, but the ground shifted beneath it. The read was not "repeatable" — the same query on the same row returned different results within the same transaction.

The anomaly is called "non-repeatable" because the original read cannot be repeated with the same result. This differs from a **dirty read** (which sees uncommitted data) and from a **phantom read** (which sees new rows appearing in a range query). A non-repeatable read involves a specific row that you already read, whose *value* changed because another committed transaction modified or deleted it. All three anomalies involve interference between concurrent transactions, but they target different aspects: dirty reads concern uncommitted writes, non-repeatable reads concern committed updates to existing rows, and phantoms concern committed inserts of new rows.

To prevent non-repeatable reads, you need the **REPEATABLE READ** isolation level or higher. Under REPEATABLE READ, each transaction sees a consistent snapshot taken at the start of the transaction (or at the start of the first statement, depending on the implementation). No matter how many times T1 reads that account balance within its transaction, it will always see the value as of its snapshot — T2's committed change is invisible until T1 commits or rolls back and starts a new transaction. The cost is reduced concurrency: in lock-based systems, shared read locks are held for the duration of the transaction rather than released after each statement, which increases the chance of blocking and deadlocks. In MVCC systems, the cost is more subtle — long-running transactions may force the database to retain old row versions longer, increasing storage overhead. The design decision is always the same tradeoff: stronger consistency guarantees versus higher concurrency and throughput.
