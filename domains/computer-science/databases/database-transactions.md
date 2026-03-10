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
status: draft
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
