---
id: sql-isolation-levels-anomalies
title: 'Transaction Isolation Levels: READ UNCOMMITTED to SERIALIZABLE'
domain: computer-science
course: databases
prerequisites:
- id: database-transactions
  type: hard
- id: transaction-properties-acid
  type: hard
- id: concurrency-control-databases
  type: hard
builds-toward:
- optimistic-concurrency-control-occ
- multiversion-concurrency-mvcc
tags:
- isolation-levels
- anomalies
- dirty-read
- phantom-read
- SERIALIZABLE
stage: formal-systems
status: draft
---

# Transaction Isolation Levels: READ UNCOMMITTED to SERIALIZABLE

## Core Idea
SQL isolation levels define how much concurrent transactions can interfere: READ UNCOMMITTED allows dirty reads, READ COMMITTED prevents dirty reads but allows non-repeatable reads, REPEATABLE READ prevents both but allows phantoms, and SERIALIZABLE provides complete isolation as if transactions ran sequentially. Higher isolation prevents more anomalies but reduces concurrency and throughput.
