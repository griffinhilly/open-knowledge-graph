---
id: dirty-read-anomaly
title: 'Dirty Read Anomaly: Reading Uncommitted Changes'
domain: computer-science
course: databases
prerequisites:
- id: isolation-level-read-uncommitted
  type: hard
tags:
- concurrency
- anomalies
- isolation-problems
stage: formal-systems
status: draft
---

# Dirty Read Anomaly: Reading Uncommitted Changes

## Core Idea
A dirty read occurs when a transaction reads data written by another uncommitted transaction. If the writing transaction rolls back, the reading transaction has consumed invalid data.

## Explainer

You understand from studying the Read Uncommitted isolation level that it allows a transaction to see changes made by other transactions before those transactions commit. A **dirty read** is the specific anomaly this creates — and understanding why it's dangerous requires tracing through what happens when things go wrong.

Consider a banking scenario. Transaction A transfers $500 from Account X (balance: $1000) to Account Y, first debiting X to $500. Before A commits, Transaction B reads Account X's balance and sees $500. Now suppose Transaction A encounters an error and rolls back — Account X returns to $1000. But Transaction B has already acted on the $500 figure. If B was generating a bank statement, it shows the wrong balance. If B was checking whether to approve a loan, it made its decision on data that never actually existed in any committed state of the database. This is the core problem: B read **uncommitted, tentative data** that the database later erased.

The term "dirty" comes from the idea that uncommitted writes are "dirty" — they are provisional changes that may or may not become permanent. A committed write is "clean" because it has passed the point of no return. When you allow dirty reads, you're letting transactions base their logic on data that might vanish. The danger isn't just seeing a wrong number once; it's that the reading transaction might make further writes or decisions based on that phantom value, propagating the error outward in ways that are hard to trace.

Dirty reads are prevented by requiring transactions to only see **committed** data — which is exactly what the Read Committed isolation level guarantees, typically by using shared locks on reads or maintaining separate committed and uncommitted versions of each row. The reason Read Uncommitted exists at all, despite this risk, is performance: skipping the locking or versioning overhead makes reads faster. In practice, it's only safe for approximate queries where exact correctness doesn't matter — things like rough row counts or dashboard estimates where being slightly wrong is acceptable. For anything involving business logic, financial calculations, or data integrity, dirty reads are unacceptable.
