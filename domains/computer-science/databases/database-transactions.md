---
id: database-transactions
title: Database Transactions
domain: computer-science
course: databases
prerequisites:
- id: sql-select-basics
  type: hard
- id: file-system-concepts
  type: soft
builds-toward:
- acid-properties
- concurrency-control-databases
- write-ahead-logging
tags:
- transactions
- COMMIT
- ROLLBACK
- BEGIN
- atomicity
- savepoint
stage: formal-systems
status: validated
---

# Database Transactions

## Core Idea
A transaction is a sequence of database operations treated as a single logical unit of work that either completes entirely (COMMIT) or is entirely undone (ROLLBACK), leaving no partial state visible. Transactions protect data integrity when systems fail midway through multi-step operations, such as a bank transfer that must debit one account and credit another atomically. The BEGIN/COMMIT/ROLLBACK commands delimit transaction boundaries; savepoints allow partial rollback to a named point within a transaction without abandoning the entire unit.

## How It's Best Learned
Simulate a bank transfer in two SQL statements inside a transaction, then deliberately cause an error or rollback between them to observe atomicity. Practice setting savepoints and rolling back to them.

## Common Misconceptions
- Auto-commit mode (default in many SQL clients) wraps every statement in its own transaction — multi-statement logic requires an explicit BEGIN.
- ROLLBACK does not undo DDL statements (CREATE TABLE, DROP TABLE) in most databases — DDL is auto-committed.
- Long-running transactions hold locks and consume resources; transactions should be kept as short as possible.

## Explainer

You already know SQL statements like SELECT, INSERT, UPDATE, and DELETE for manipulating data. A **transaction** wraps one or more of these statements into a single all-or-nothing unit. The core promise is **atomicity**: either every statement in the transaction succeeds and the changes become permanent, or none of them take effect. There is no state where half the work is done and half is not. This guarantee is what makes databases reliable for operations that involve multiple coordinated changes.

Consider the classic example of a bank transfer: you need to subtract $100 from Alice's account and add $100 to Bob's account. Without transactions, a crash between the two statements could leave Alice debited and Bob uncredited — the $100 vanishes. With a transaction, you write `BEGIN`, then the two UPDATE statements, then `COMMIT`. If anything goes wrong before COMMIT — a power failure, a constraint violation, an application error — the database performs a **ROLLBACK**, undoing all changes made since BEGIN. The money either moves completely or stays exactly where it was.

The `BEGIN` command starts a new transaction. Every statement after BEGIN is part of that transaction until you explicitly issue `COMMIT` (to make changes permanent) or `ROLLBACK` (to discard them). A subtlety to watch for: most SQL clients operate in **auto-commit mode** by default, meaning every individual statement is implicitly wrapped in its own transaction and committed immediately. If you want multi-statement atomicity, you must explicitly write BEGIN. **Savepoints** add finer-grained control within a transaction. `SAVEPOINT x` marks a named point, and `ROLLBACK TO x` undoes everything back to that point without abandoning the entire transaction. This is useful when you want to attempt an operation and gracefully recover if it fails, without losing earlier work in the same transaction.

Transactions are not free — they consume resources while active. An open transaction may hold locks on rows or tables, preventing other transactions from reading or modifying those rows. Long-running transactions can therefore cause other users' queries to queue up and wait, degrading system performance. The practical rule is to keep transactions as short as possible: do your computation outside the transaction, open it, perform the minimal set of database operations, and commit immediately. This discipline — combined with proper error handling to ensure every BEGIN is matched by either a COMMIT or a ROLLBACK — is foundational to writing reliable database applications.
