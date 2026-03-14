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
