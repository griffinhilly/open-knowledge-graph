---
id: optimistic-concurrency-control-occ
title: Optimistic Concurrency Control and Timestamp Ordering
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
- id: sql-isolation-levels-anomalies
  type: hard
builds-toward:
- multiversion-concurrency-mvcc
- snapshot-isolation-write-skew
tags:
- OCC
- optimistic
- timestamp-ordering
- validation
stage: formal-systems
status: draft
---

# Optimistic Concurrency Control and Timestamp Ordering

## Core Idea
Optimistic Concurrency Control assumes conflicts are rare and validates transactions at commit time rather than blocking. Each transaction operates on local versions; at commit, the system checks if its reads/writes conflict with committed transactions. Timestamp ordering assigns each transaction a logical position; transactions commit only if operations respect timestamp order. OCC aborts transactions on conflicts but avoids blocking when no conflicts exist.
