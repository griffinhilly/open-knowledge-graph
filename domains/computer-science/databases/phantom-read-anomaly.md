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

## Explainer

You already know from repeatable read isolation that a transaction can lock the specific rows it has read so that no other transaction can modify them mid-flight. This prevents dirty reads and non-repeatable reads — if you read a row once, you can read it again and get the same values. But repeatable read protects *existing rows*. It says nothing about rows that do not yet exist. A **phantom read** exploits exactly this gap: another transaction inserts a *new* row that matches your query's WHERE clause, and suddenly your second execution of the same query returns a row that was not there before.

Consider a concrete scenario. Transaction A runs `SELECT * FROM orders WHERE status = 'pending'` and gets back 50 rows. Meanwhile, Transaction B inserts a new order with `status = 'pending'` and commits. When Transaction A runs the same query again, it now gets 51 rows. The 51st row is the **phantom** — it appeared out of nowhere from A's perspective. None of the original 50 rows changed (repeatable read prevented that), but the result set itself grew. This is unsettling because Transaction A may have made decisions based on the assumption that there were exactly 50 pending orders.

The reason repeatable read cannot prevent phantoms is architectural. Row-level locks only apply to rows that have already been identified and read. You cannot lock a row that does not exist yet. To prevent phantoms, the database must lock the *predicate* — the condition `status = 'pending'` — so that no new row matching that condition can be inserted while the transaction holds the lock. This is what the **serializable** isolation level provides, often implemented through predicate locking, index-range locking, or serializable snapshot isolation.

Phantom reads matter most in transactions that perform aggregate calculations or make decisions based on the completeness of a result set. If a banking system sums all transactions for an account and then a new transaction sneaks in, the sum becomes stale. Understanding phantoms clarifies why serializable isolation exists and why it carries a performance cost — preventing phantoms requires locking not just data, but the *absence* of data that could appear.
