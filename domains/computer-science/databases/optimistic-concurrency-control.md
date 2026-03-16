---
id: optimistic-concurrency-control
title: 'Optimistic Concurrency Control: Version Numbers'
domain: computer-science
course: databases
prerequisites:
- id: lost-update-problem
  type: hard
tags:
- concurrency
- conflict-detection
- mvcc
stage: formal-systems
status: draft
---

# Optimistic Concurrency Control: Version Numbers

## Core Idea
Optimistic concurrency control avoids locks by versioning rows (timestamps or counters) and detecting conflicts at UPDATE time. If the version has changed since READ, the UPDATE is rejected.

## How It's Best Learned
Implement an UPDATE with a WHERE clause checking the current version, simulating an application-level conflict detection.

## Common Misconceptions
Optimistic control assumes conflicts are rare and works well with low contention. Under high contention, rollbacks and retries degrade performance.

## Explainer

You know from studying the lost update problem that two transactions can silently overwrite each other's changes if nothing coordinates their access to the same row. The traditional solution is locking — grab a lock before reading, hold it until you commit, and block anyone else from touching the data. **Optimistic concurrency control** takes the opposite bet: instead of preventing conflicts upfront, it lets transactions proceed freely and checks for conflicts only at the moment of writing.

The mechanism relies on **version numbers** (or timestamps) attached to each row. When a transaction reads a row, it notes the current version — say, version 5. The transaction does its work locally without holding any locks. When it's ready to update, it issues something like `UPDATE accounts SET balance = 750, version = 6 WHERE id = 42 AND version = 5`. The `WHERE version = 5` clause is the critical check: if no other transaction has modified the row since our read, the version is still 5 and the update succeeds. If another transaction snuck in and changed the row (bumping it to version 6), our WHERE clause matches zero rows, and we know our read was stale. The application detects the zero-row update, discards its work, re-reads the current data, and retries.

The beauty of this approach is that the **common case is fast**. If conflicts are rare — which they are in most web applications where thousands of users rarely touch the same row at the same instant — transactions never block each other. There's no lock manager, no wait queues, and no deadlock risk. Readers never block writers, and writers never block readers. Compare this to pessimistic locking where every access acquires a lock, and transactions frequently wait in line even when no actual conflict would have occurred.

The tradeoff becomes painful under **high contention**. If many transactions compete for the same rows, optimistic control produces a storm of failed updates and retries. Each retry re-reads the data and attempts the update again, only to potentially fail again because yet another transaction beat it. Under extreme contention, the system can waste more work on retries than it saves by avoiding locks. This is why the choice between optimistic and pessimistic concurrency depends on your workload: optimistic for read-heavy, low-conflict scenarios (most web apps, content management systems); pessimistic for write-heavy, high-conflict scenarios (inventory systems during flash sales, financial trading platforms).
