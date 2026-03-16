---
id: pessimistic-concurrency-control
title: 'Pessimistic Concurrency Control: Locking'
domain: computer-science
course: databases
prerequisites:
- id: lost-update-problem
  type: hard
tags:
- concurrency
- locking
- locks
stage: formal-systems
status: draft
---

# Pessimistic Concurrency Control: Locking

## Core Idea
Pessimistic concurrency control acquires locks on rows before reading or modifying them. Locks are held until commit, ensuring no other transaction can interfere.

## How It's Best Learned
Use SELECT...FOR UPDATE to lock rows, observe how other sessions block, and commit to release locks.

## Common Misconceptions
Locks are held until COMMIT, not after the UPDATE statement finishes. Deadlocks can occur if two transactions lock resources in different orders.

## Explainer

When multiple transactions access the same data concurrently, things can go wrong — you already saw this with the **lost update problem**, where two transactions read and write the same row and one silently overwrites the other's changes. Pessimistic concurrency control is the straightforward solution: before you touch a row, you lock it. While you hold the lock, nobody else can modify that row. It is called "pessimistic" because it assumes conflicts are likely and prevents them upfront, rather than detecting them after the fact.

In practice, most relational databases implement this through **shared locks** and **exclusive locks**. A shared lock (read lock) allows multiple transactions to read the same row simultaneously — reads do not conflict with each other. An exclusive lock (write lock) gives one transaction sole access to a row for modification, blocking both readers and writers. When you execute `SELECT ... FOR UPDATE`, you are explicitly requesting an exclusive lock on the returned rows. Other transactions that try to read or modify those same rows will block — they wait, paused, until you commit or roll back and release your locks.

The critical detail is *when* locks are released. Under the standard **two-phase locking** protocol, a transaction acquires all the locks it needs (the growing phase) and releases them only at commit or abort (the shrinking phase). This means a lock acquired early in a long transaction is held for the entire duration, even if the row is not touched again. This guarantees serializability — the result is equivalent to running transactions one at a time — but it also means long transactions can block other work for extended periods.

The main danger of pessimistic locking is **deadlock**: transaction A locks row 1 and waits for row 2, while transaction B locks row 2 and waits for row 1. Neither can proceed. Databases handle this with deadlock detection — periodically checking for cycles in the wait graph and aborting one transaction to break the cycle. You can minimize deadlocks by always acquiring locks in a consistent order (e.g., by primary key) and keeping transactions as short as possible. The tradeoff is clear: pessimistic control gives you strong correctness guarantees at the cost of reduced concurrency and the risk of blocking. For workloads where conflicts are frequent and correctness is paramount — such as financial transfers or inventory updates — that tradeoff is well worth it.
