---
id: transaction-properties-acid
title: Transactions and ACID Properties
domain: computer-science
course: databases
prerequisites:
- id: sql-data-insertion-modification
  type: hard
builds-toward:
- concurrency-isolation-control
tags:
- transaction
- ACID
- atomicity
- consistency
- isolation
- durability
stage: formal-systems
status: draft
---

# Transactions and ACID Properties

## Core Idea
A transaction is a logical unit of work executing multiple SQL statements atomically. ACID properties guarantee: Atomicity (all-or-nothing), Consistency (valid state to valid state), Isolation (independent execution), Durability (permanent after commit). ACID ensures database reliability and correctness in multi-user environments.

## How It's Best Learned
Study concrete examples of ACID property violations and how they are prevented. Practice writing transaction code and understanding rollback scenarios. Compare different isolation levels and their consistency guarantees.

## Explainer

You already know how to insert, update, and delete data with individual SQL statements. But real-world operations often require multiple statements that must succeed or fail together. A bank transfer, for instance, debits one account and credits another — if the debit succeeds but the credit fails (say, due to a crash), money has vanished. A **transaction** wraps multiple statements into a single logical unit: either all of them take effect, or none of them do. You begin a transaction with `BEGIN`, execute your statements, and finalize with `COMMIT` (apply everything) or `ROLLBACK` (undo everything).

The **ACID properties** formalize what transactions guarantee. **Atomicity** means all-or-nothing: if any statement in the transaction fails or the system crashes mid-transaction, every change made so far is rolled back as if the transaction never started. The database achieves this by writing changes to a **write-ahead log** before modifying actual data pages — on crash recovery, it replays or undoes logged operations to restore a consistent state. **Consistency** means a transaction takes the database from one valid state to another, respecting all constraints (foreign keys, uniqueness, CHECK constraints). If a transaction would violate a constraint, it is aborted.

**Isolation** is the subtlest property: it determines how much of a transaction's in-progress work is visible to other concurrent transactions. Perfect isolation would mean every transaction runs as if it were the only one — but that would require serializing all access, destroying performance. In practice, databases offer **isolation levels** that trade consistency for concurrency. At READ COMMITTED (the default in PostgreSQL), a transaction sees only data committed before each statement executes. At SERIALIZABLE, the database guarantees results equivalent to running transactions one at a time, detecting and aborting conflicting ones. Lower isolation levels permit anomalies like dirty reads (seeing uncommitted data) or phantom reads (seeing new rows inserted by another transaction mid-query).

**Durability** means that once a transaction commits, its changes survive any subsequent failure — power loss, crash, disk error. The database ensures this by flushing the write-ahead log to stable storage before acknowledging the commit. Even if the server crashes immediately after, the committed data can be recovered from the log on restart. Together, the four ACID properties let you reason about database operations as if they were simple, sequential, and permanent — even when the reality involves concurrent users, network failures, and hardware faults. Understanding which property is doing the work in a given scenario is the foundation for the concurrency control and isolation topics that follow.
