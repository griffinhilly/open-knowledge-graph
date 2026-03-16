---
id: transaction-savepoint-nested
title: 'Savepoints: Partial Rollback Within Transactions'
domain: computer-science
course: databases
prerequisites:
- id: transaction-begin-commit-rollback
  type: hard
tags:
- transactions
- rollback
- error-handling
stage: formal-systems
status: draft
---

# Savepoints: Partial Rollback Within Transactions

## Core Idea
Savepoints mark points within a transaction to which a ROLLBACK can be selective, allowing recovery from errors without losing all work in the transaction.

## How It's Best Learned
Create a multi-statement transaction with savepoints and practice rolling back to different points.

## Common Misconceptions
Savepoints do not commit data—only COMMIT finalizes changes. Rolled-back statements after a savepoint can be re-executed with different values.

## Explainer

From your work with BEGIN, COMMIT, and ROLLBACK, you know that a transaction groups multiple operations into an atomic unit — either everything succeeds and is committed, or everything is rolled back as if nothing happened. But what if your transaction contains ten steps, step seven fails, and you want to undo just step seven while keeping the first six? Without savepoints, your only option is to roll back the entire transaction and start over. **Savepoints** solve this by letting you place named bookmarks inside a transaction that you can roll back to selectively.

The syntax is straightforward: after beginning a transaction, you create a savepoint with `SAVEPOINT my_checkpoint`. You continue executing statements, and if something goes wrong, you issue `ROLLBACK TO SAVEPOINT my_checkpoint`. This undoes everything *after* that savepoint while preserving everything before it. You can then continue the transaction from that point — retrying the failed operation with different values, skipping it entirely, or taking an alternative path. Think of it like saving your progress in a video game: if you die in a tough section, you reload from the last save rather than restarting the entire game.

You can create **multiple savepoints** within a single transaction, effectively nesting recovery points. Imagine a batch import that processes records one at a time: you set a savepoint before each record, attempt the insert, and if a particular record violates a constraint, you roll back to its savepoint and log the failure without losing the successfully imported records. This pattern is essential in applications that process data in bulk where individual failures are expected and acceptable.

The critical thing to remember is that savepoints do **not** commit anything. All the work inside the transaction — including everything before your savepoints — remains uncommitted until you issue a final COMMIT. A savepoint is not a mini-transaction; it is a recovery marker within the larger transaction. If you ROLLBACK the entire transaction (without specifying a savepoint), everything is undone regardless of how many savepoints you set. Savepoints give you *finer-grained error recovery* within the transactional model you already understand, without breaking the atomicity guarantee that transactions provide.
