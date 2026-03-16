---
id: snapshot-isolation-write-skew
title: Snapshot Isolation and Write Skew Anomalies
domain: computer-science
course: databases
prerequisites:
- id: multiversion-concurrency-mvcc
  type: hard
- id: sql-isolation-levels-anomalies
  type: hard
tags:
- snapshot-isolation
- write-skew
- anomaly
- SI
- phantom
stage: formal-systems
status: draft
---

# Snapshot Isolation and Write Skew Anomalies

## Core Idea
Snapshot Isolation provides each transaction with a consistent database snapshot, preventing dirty, non-repeatable, and phantom reads. However, SI allows write skew anomalies where two transactions both read versions satisfying a constraint, make changes, and commit without noticing their combined effect violates the constraint (e.g., both doctors see the other on call, both go off). This anomaly cannot occur under SERIALIZABLE but is rare in practice.

## Explainer

You already understand how MVCC works — each transaction sees a consistent snapshot of the database as of its start time, reading committed versions without blocking other writers. And you know that isolation levels define which anomalies a system permits. **Snapshot isolation** (SI) sits between REPEATABLE READ and SERIALIZABLE in strength: it prevents dirty reads, non-repeatable reads, and even phantom reads, because every read within the transaction returns data from the same fixed snapshot. Two concurrent transactions can both read and write without blocking each other, which makes SI attractive for performance.

The catch is **write skew**, an anomaly unique to snapshot isolation. Write skew occurs when two transactions each read an overlapping set of rows, make decisions based on what they read, and write to different rows — but their combined writes violate a constraint that held when each transaction read. The classic example involves two on-call doctors. A hospital rule says at least one doctor must remain on call. Doctor A and Doctor B both check the schedule at the same time, both see the other is on call, and both submit a request to go off call. Under snapshot isolation, each transaction sees the other doctor still on call (because neither has committed yet), so each concludes the constraint is satisfied. Both commit successfully, and now zero doctors are on call — violating the invariant.

The key insight is that write skew cannot happen if both transactions write to the same row. SI uses a **first-committer-wins** rule: if two transactions modify the same row, the second one to commit is aborted. This prevents lost updates. But write skew involves writing to *different* rows (Doctor A updates her own row, Doctor B updates his), so the conflict detection never fires. The transactions' writes do not overlap, even though their reads do, and the constraint violation emerges only from the combination.

Defending against write skew requires either upgrading to true SERIALIZABLE isolation (which detects these dependency cycles and aborts one transaction) or using application-level locking. A common workaround is to use SELECT FOR UPDATE on the rows you read, which forces a write lock even though you are only reading — effectively converting the read dependency into a write conflict that SI can detect. Some systems, like PostgreSQL's Serializable Snapshot Isolation (SSI), extend SI with dependency tracking to automatically detect and prevent write skew without requiring explicit locks.
