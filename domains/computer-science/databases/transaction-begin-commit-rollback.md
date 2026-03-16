---
id: transaction-begin-commit-rollback
title: 'Transaction Control: BEGIN, COMMIT, ROLLBACK'
domain: computer-science
course: databases
prerequisites:
- id: database-transactions
  type: hard
builds-toward:
- transaction-savepoint-nested
- isolation-level-read-uncommitted
tags:
- transactions
- acid
- dml-control
stage: formal-systems
status: draft
---

# Transaction Control: BEGIN, COMMIT, ROLLBACK

## Core Idea
BEGIN starts a transaction, COMMIT finalizes changes, and ROLLBACK discards them. Together they provide explicit control over atomicity—either all changes succeed or none do.

## How It's Best Learned
Practice rolling back a DELETE in response to an error check, and verify that uncommitted changes are invisible to other sessions.

## Common Misconceptions
Uncommitted changes are visible only to the current session by default. Autocommit behavior (automatic COMMIT after each statement) varies by database and driver.

## Explainer

You already understand that a database transaction is a logical unit of work that must either complete entirely or not at all — the atomicity guarantee from ACID. The three commands **BEGIN**, **COMMIT**, and **ROLLBACK** are how you exercise explicit control over that boundary. Without them, most database drivers operate in **autocommit mode**, where every individual SQL statement is its own transaction — it commits immediately upon completion. Explicit transaction control lets you group multiple statements into a single atomic unit.

The pattern is straightforward: `BEGIN` (or `START TRANSACTION` in some systems) opens a new transaction. Every subsequent INSERT, UPDATE, or DELETE is tentatively applied but not yet permanent. The changes exist in a kind of limbo — visible to your session but invisible to other connections. When you issue `COMMIT`, all changes since BEGIN are made durable and visible to everyone. If something goes wrong — a constraint violation, a business logic check that fails, or simply a mistake — `ROLLBACK` discards every change since BEGIN, leaving the database exactly as it was before the transaction started.

Consider a bank transfer: you need to debit one account and credit another. Without explicit transaction control, the debit might succeed but the credit might fail (due to a crash, constraint error, or network issue), leaving money missing from one account and not yet in the other. Wrapping both operations in a single transaction ensures atomicity: `BEGIN; UPDATE accounts SET balance = balance - 100 WHERE id = 1; UPDATE accounts SET balance = balance + 100 WHERE id = 2; COMMIT;`. If the second UPDATE fails, you call ROLLBACK and the first UPDATE is also undone. Neither change persists unless both succeed.

A practical subtlety is autocommit behavior. In PostgreSQL, each statement outside an explicit BEGIN block auto-commits. In MySQL with InnoDB, the same applies by default. Many application frameworks and database drivers also manage autocommit settings, sometimes turning it off by default and requiring explicit commits. If you run a DELETE and are puzzled that the rows are already gone before you typed COMMIT, autocommit is likely on. When working with critical data, always use explicit BEGIN/COMMIT boundaries so that you have a chance to ROLLBACK if something unexpected happens — once a statement auto-commits, there is no undoing it.
