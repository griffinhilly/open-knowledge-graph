---
id: acid-properties
title: ACID Properties
domain: computer-science
course: databases
prerequisites:
- id: database-transactions
  type: hard
builds-toward:
- concurrency-control-databases
- write-ahead-logging
- nosql-concepts
tags:
- ACID
- atomicity
- consistency
- isolation
- durability
- transaction guarantees
stage: formal-systems
status: draft
---

# ACID Properties

## Core Idea
ACID is an acronym for four properties that guarantee reliable transaction processing: Atomicity (all-or-nothing execution — a failure mid-transaction rolls back all changes), Consistency (a transaction brings the database from one valid state to another, preserving all defined invariants), Isolation (concurrent transactions execute without interfering, as if serialized), and Durability (committed transactions survive crashes and power loss). Enforcing full ACID requires logging, locking, and recovery protocols that add overhead, which is why some distributed systems deliberately relax these guarantees.

## How It's Best Learned
Work through scenarios that would violate each property: crash mid-transfer (atomicity), violate a constraint mid-transaction (consistency), read uncommitted data (isolation), lose a commit after crash (durability). Understand what mechanisms prevent each failure.

## Common Misconceptions
- Consistency in ACID refers to application-defined invariants (foreign keys, CHECK constraints), not linearizability — it is distinct from the 'C' in CAP theorem.
- Isolation is not binary; SQL defines four isolation levels (READ UNCOMMITTED through SERIALIZABLE) with different tradeoffs.
- ACID compliance does not prevent all data bugs — application logic errors still cause inconsistency even in fully ACID systems.
