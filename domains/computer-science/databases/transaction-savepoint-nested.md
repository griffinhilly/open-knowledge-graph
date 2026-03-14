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
