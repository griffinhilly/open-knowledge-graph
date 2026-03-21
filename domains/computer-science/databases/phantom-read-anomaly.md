---
id: phantom-read-anomaly
title: 'Phantom Read Anomaly: New Rows Appearing'
domain: computer-science
course: databases
prerequisites:
- id: isolation-level-repeatable-read
  type: hard
tags:
- concurrency
- anomalies
- isolation-problems
stage: formal-systems
status: draft
---

# Phantom Read Anomaly: New Rows Appearing

## Core Idea
A phantom read occurs when a transaction executes a query twice, and between the two executions another transaction inserts rows matching the WHERE clause, causing the result set size to change.

## Questions

```yaml
- question: "Transaction A runs SELECT * FROM orders WHERE status = 'pending' and gets 50 rows. Transaction B then inserts a new pending order and commits. Transaction A runs the same query again and gets 51 rows. Which isolation level, at minimum, prevents this anomaly?"
  type: multiple-choice
  options:
    - "Read committed — it only reads committed data"
    - "Repeatable read — it locks all rows read by the transaction"
    - "Serializable — it locks the predicate, preventing new matching rows from being inserted"
    - "Read uncommitted — it blocks all concurrent writes"
  answer: 2
  explanation: "Repeatable read prevents modification of rows already read, but it cannot prevent new rows from being inserted. The phantom row (row 51) didn't exist when Transaction A first read — there was nothing to lock. Serializable isolation prevents phantoms by locking the predicate (the condition 'status = pending'), so no new row matching that condition can be inserted while Transaction A holds its lock. Read committed and read uncommitted provide even weaker guarantees and cannot prevent phantom reads."

- question: "A banking system sums all transactions for an account within a transaction, then uses that sum to decide whether to approve a transfer. A phantom read occurs mid-transaction. What is the WORST CASE outcome?"
  type: multiple-choice
  options:
    - "The sum query fails with an error, forcing a retry"
    - "The transfer decision is made on a stale sum that doesn't reflect a concurrent deposit, potentially approving an incorrect amount"
    - "The transaction is automatically rolled back by the database"
    - "The sum is recalculated automatically to include the new row"
  answer: 1
  explanation: "Phantom reads are dangerous precisely because they are silent — no error is raised, no rollback occurs. The first query returned a correct sum at that moment; the decision logic proceeds as if that sum is definitive. But a new transaction committed between the two reads, making the sum stale. The database does not alert the transaction to this inconsistency under repeatable read or weaker isolation. This is why serializable isolation exists for financial applications where result set completeness matters."

- question: "Repeatable read isolation prevents phantom reads because it locks all rows that match a query's WHERE clause."
  type: true-false
  answer: false
  explanation: "Repeatable read locks rows that ALREADY EXIST and have been read — it prevents those specific rows from being modified by other transactions. But a phantom is a NEW row that didn't exist when the first read occurred. You cannot place a lock on a row that doesn't exist yet. Preventing phantoms requires locking the predicate (the WHERE condition itself), which is what serializable isolation provides. This is the architectural gap that repeatable read cannot bridge."

- question: "Preventing phantom reads requires locking not just existing data rows, but the predicate — the condition that defines which rows qualify — so that new qualifying rows cannot be inserted."
  type: true-false
  answer: true
  explanation: "This is the essential insight. Phantom prevention is fundamentally about locking the absence of data — the 'space' where new matching rows could appear. Implementations vary: some databases use predicate locks (explicit locks on WHERE conditions), others use index-range locks (locking ranges in an index that covers the predicate), and others use serializable snapshot isolation (detecting conflicts at commit time). All approaches must prevent another transaction from inserting a row that retroactively satisfies a predicate already evaluated."

- question: "Why can't row-level locking, even if perfectly implemented, prevent phantom reads? What additional mechanism is required?"
  type: short-answer
  answer: "Row-level locking can only apply to rows that already exist. A phantom is a row inserted by a concurrent transaction after the first read — there was no row to lock at the time of the first query. Preventing phantoms requires locking the predicate (the WHERE condition), so that any INSERT attempting to create a row matching that condition is blocked until the reading transaction completes. This requires predicate locking, index-range locking, or conflict detection at commit time (as in serializable snapshot isolation)."
  explanation: "The conceptual key is that row-level locks protect existing data; phantoms exploit the absence of data. A transaction that read 'all rows where status = pending' has implicitly made a claim about the complete set — but row locks only secure the members of that set at that moment, not the set's boundaries. Serializable isolation closes this gap by treating the predicate itself as a lockable resource, at the cost of reduced concurrency."
```

## Explainer

You already know from repeatable read isolation that a transaction can lock the specific rows it has read so that no other transaction can modify them mid-flight. This prevents dirty reads and non-repeatable reads — if you read a row once, you can read it again and get the same values. But repeatable read protects *existing rows*. It says nothing about rows that do not yet exist. A **phantom read** exploits exactly this gap: another transaction inserts a *new* row that matches your query's WHERE clause, and suddenly your second execution of the same query returns a row that was not there before.

Consider a concrete scenario. Transaction A runs `SELECT * FROM orders WHERE status = 'pending'` and gets back 50 rows. Meanwhile, Transaction B inserts a new order with `status = 'pending'` and commits. When Transaction A runs the same query again, it now gets 51 rows. The 51st row is the **phantom** — it appeared out of nowhere from A's perspective. None of the original 50 rows changed (repeatable read prevented that), but the result set itself grew. This is unsettling because Transaction A may have made decisions based on the assumption that there were exactly 50 pending orders.

The reason repeatable read cannot prevent phantoms is architectural. Row-level locks only apply to rows that have already been identified and read. You cannot lock a row that does not exist yet. To prevent phantoms, the database must lock the *predicate* — the condition `status = 'pending'` — so that no new row matching that condition can be inserted while the transaction holds the lock. This is what the **serializable** isolation level provides, often implemented through predicate locking, index-range locking, or serializable snapshot isolation.

Phantom reads matter most in transactions that perform aggregate calculations or make decisions based on the completeness of a result set. If a banking system sums all transactions for an account and then a new transaction sneaks in, the sum becomes stale. Understanding phantoms clarifies why serializable isolation exists and why it carries a performance cost — preventing phantoms requires locking not just data, but the *absence* of data that could appear.
