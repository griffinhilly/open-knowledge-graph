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
