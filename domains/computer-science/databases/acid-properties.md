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
status: validated
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

## Explainer

You already understand that a database transaction groups multiple operations into a single logical unit — a bank transfer that debits one account and credits another, for example. ACID describes the four guarantees a database must provide for transactions to behave reliably, even in the face of crashes, concurrent access, and hardware failures. Each letter names a specific promise, and understanding the mechanisms behind each one reveals why databases are engineered the way they are.

**Atomicity** means a transaction is all-or-nothing. If a bank transfer debits $500 from Account A but crashes before crediting Account B, atomicity guarantees the debit is rolled back — the database never ends up in a state where money simply vanished. Databases achieve this using a **write-ahead log** (WAL): before modifying any data page, the database first writes a log record describing the intended change. On crash recovery, the database replays committed transactions from the log and undoes uncommitted ones. The log is the source of truth for what happened, and it is what makes rollback possible.

**Consistency** means a transaction must transition the database from one valid state to another, respecting all declared constraints — primary keys, foreign keys, CHECK constraints, unique constraints, and triggers. If your schema says an account balance cannot be negative, any transaction that would create a negative balance is rejected. This is sometimes the most misunderstood ACID property because "consistency" means something different in distributed systems (the C in CAP theorem refers to linearizability, an entirely different concept). In ACID, consistency is about application-level invariants enforced by the schema.

**Isolation** ensures that concurrent transactions do not interfere with each other. Without isolation, one transaction might read half-written data from another, producing phantom results or lost updates. Full isolation (the SERIALIZABLE level) makes concurrent transactions behave as though they ran one at a time. But serializable execution is expensive — it requires extensive locking or validation — so SQL defines weaker isolation levels (READ COMMITTED, REPEATABLE READ) that trade some isolation guarantees for better throughput. Understanding which anomalies each level permits (dirty reads, non-repeatable reads, phantom reads) is essential for choosing the right level for a workload.

**Durability** guarantees that once a transaction commits, its effects survive any subsequent failure — power loss, OS crash, disk failure. The WAL again plays a central role: a transaction is not considered committed until its log records are flushed to stable storage. Even if the in-memory data pages are lost in a crash, the database can reconstruct committed state from the log. Replication and backups extend durability guarantees beyond single-machine failures. Together, these four properties form the contract that makes relational databases trustworthy for financial systems, medical records, and any application where data correctness is non-negotiable.
