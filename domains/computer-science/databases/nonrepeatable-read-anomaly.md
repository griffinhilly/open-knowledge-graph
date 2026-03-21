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

## Questions

```yaml
- question: "Transaction T1 reads an account balance and sees $1000. T2 then updates the balance to $200 and commits. T1 re-reads the same row and sees $200. Which isolation level permits this behavior?"
  type: multiple-choice
  options:
    - "SERIALIZABLE"
    - "REPEATABLE READ"
    - "READ COMMITTED"
    - "This behavior is impossible under any standard isolation level"
  answer: 2
  explanation: "Under READ COMMITTED, each statement sees the latest committed snapshot at the moment that statement begins. Since T2 committed before T1's second SELECT, T1 sees the new value — a non-repeatable read. Both REPEATABLE READ and SERIALIZABLE prevent this by ensuring T1's snapshot is held for the entire transaction, not just per statement."

- question: "Which of the following scenarios describes a non-repeatable read (and not another isolation anomaly)?"
  type: multiple-choice
  options:
    - "T1 reads uncommitted changes written by T2 that T2 later rolls back"
    - "T1 reads a row, T2 updates and commits it, T1 re-reads the same row and sees a different value"
    - "T1 issues a range query, T2 inserts a new matching row, T1 re-issues the query and sees an extra row"
    - "T1 and T2 both read and then update the same row, and T1's update overwrites T2's"
  answer: 1
  explanation: "A non-repeatable read involves reading the same specific existing row twice and getting different values because another transaction modified it in between. Option A is a dirty read (uncommitted data). Option C is a phantom read (new rows in a range). Option D is a lost update. All involve concurrency anomalies but are distinct phenomena."

- question: "The non-repeatable read anomaly can occur under READ COMMITTED isolation."
  type: true-false
  answer: true
  explanation: "READ COMMITTED guarantees consistency per-statement, not per-transaction. Each new SELECT within a transaction sees the latest committed data at the time that statement runs. If another transaction commits a change between your first and second SELECT on the same row, your second SELECT sees the new value. This is the definition of a non-repeatable read."

- question: "A non-repeatable read and a phantom read are the same anomaly described differently."
  type: true-false
  answer: false
  explanation: "They are distinct. A non-repeatable read involves a specific existing row returning a different VALUE on re-read (due to an UPDATE or DELETE by another transaction). A phantom read involves a range query returning DIFFERENT ROWS on re-execution (due to INSERTs by another transaction). One is about changed values in existing rows; the other is about new rows appearing in a result set."

- question: "Why does REPEATABLE READ prevent non-repeatable reads, and what is the cost of this stronger guarantee?"
  type: short-answer
  answer: "REPEATABLE READ gives each transaction a consistent snapshot — either at transaction start or first statement — that doesn't change even if other transactions commit updates. T1 always sees the same row values throughout its life. The cost is reduced concurrency: lock-based systems hold shared read locks for the entire transaction duration (increasing blocking and deadlock risk); MVCC systems must retain old row versions for longer, increasing storage overhead."
  explanation: "The tradeoff is always consistency vs. concurrency. REPEATABLE READ trades some throughput for predictable within-transaction behavior: you can safely read the same data multiple times and reason about it. Systems that need high concurrency often accept the weaker READ COMMITTED guarantee and handle the resulting inconsistencies in application logic."
```

## Explainer

You already understand that under READ COMMITTED isolation, a transaction only sees data that has been committed — no dirty reads. But READ COMMITTED makes a subtle promise that is weaker than many people assume: it guarantees a consistent snapshot *per statement*, not per transaction. Each SQL statement you execute within a transaction sees the latest committed data at the moment *that statement* begins. If another transaction commits a change between your first and second SELECT, your second SELECT sees the new value. This is the **non-repeatable read** anomaly.

Here is a concrete scenario. Suppose you are building a banking application, and transaction T1 needs to check an account balance twice during its work — first to verify the account has sufficient funds, and later to compute a transfer amount. T1 reads the balance and sees $1000. Meanwhile, transaction T2 withdraws $800 and commits. When T1 reads the balance again, it now sees $200. T1's logic assumed the balance was $1000 throughout, but the ground shifted beneath it. The read was not "repeatable" — the same query on the same row returned different results within the same transaction.

The anomaly is called "non-repeatable" because the original read cannot be repeated with the same result. This differs from a **dirty read** (which sees uncommitted data) and from a **phantom read** (which sees new rows appearing in a range query). A non-repeatable read involves a specific row that you already read, whose *value* changed because another committed transaction modified or deleted it. All three anomalies involve interference between concurrent transactions, but they target different aspects: dirty reads concern uncommitted writes, non-repeatable reads concern committed updates to existing rows, and phantoms concern committed inserts of new rows.

To prevent non-repeatable reads, you need the **REPEATABLE READ** isolation level or higher. Under REPEATABLE READ, each transaction sees a consistent snapshot taken at the start of the transaction (or at the start of the first statement, depending on the implementation). No matter how many times T1 reads that account balance within its transaction, it will always see the value as of its snapshot — T2's committed change is invisible until T1 commits or rolls back and starts a new transaction. The cost is reduced concurrency: in lock-based systems, shared read locks are held for the duration of the transaction rather than released after each statement, which increases the chance of blocking and deadlocks. In MVCC systems, the cost is more subtle — long-running transactions may force the database to retain old row versions longer, increasing storage overhead. The design decision is always the same tradeoff: stronger consistency guarantees versus higher concurrency and throughput.
