---
id: acid-properties
title: ACID Properties
domain: computer-science
course: databases
prerequisites:
- id: database-transactions
  type: hard
- id: sql-data-insertion-modification
  type: soft
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

## Questions

```yaml
- question: "A bank transfer transaction successfully debits $500 from Account A, but the database crashes before it can credit Account B. After the database restarts and recovers, what does atomicity guarantee?"
  type: multiple-choice
  options:
    - "The credit to Account B is completed during recovery, since the debit already occurred"
    - "The debit to Account A is rolled back, leaving both accounts in their pre-transaction state"
    - "The transaction is re-executed from the beginning automatically"
    - "The database flags Account A as overdrawn and waits for a human administrator to resolve it"
  answer: 1
  explanation: "Atomicity means all-or-nothing: if a transaction cannot complete fully, all of its partial changes are undone. The write-ahead log records the intended changes before they happen; on crash recovery, the database identifies uncommitted transactions and rolls them back. The debit to Account A is reversed, restoring both accounts to their pre-transaction state. This prevents a state where $500 simply vanishes from the system. The log — not a retry — is the mechanism."

- question: "Two concurrent transactions both read an account balance of $1,000 and each independently decide to withdraw $800, which would leave $200. Without isolation controls, what anomaly could occur, and which ACID property prevents it?"
  type: multiple-choice
  options:
    - "Both withdrawals succeed, leaving the balance at −$600; prevented by Consistency"
    - "Both withdrawals succeed, leaving the balance at −$600; prevented by Isolation"
    - "One withdrawal is lost entirely; prevented by Atomicity"
    - "The account is locked until both transactions complete; prevented by Durability"
  answer: 1
  explanation: "This is the classic lost-update / write-write conflict anomaly. Without isolation, both transactions read $1,000, both decide to proceed, and both commit a balance of $200 (1000 − 800) — or in a worse variant, one overwrite is lost entirely. Isolation prevents concurrent transactions from seeing or interfering with each other's intermediate states. At the SERIALIZABLE level, one transaction would see the other's committed debit and either fail the constraint check or be blocked. Atomicity ensures each transaction is all-or-nothing but does not protect against concurrent interference."

- question: "A database system can be fully ACID compliant and still produce incorrect data if the application code contains logic errors."
  type: true-false
  answer: true
  explanation: "ACID guarantees correct execution of what you ask the database to do — atomicity, consistency relative to schema constraints, isolation from other transactions, durability of commits. It cannot protect against application logic that is itself wrong. If code incorrectly calculates the transfer amount, or updates the wrong account ID, ACID will faithfully and durably commit the incorrect result. Consistency in ACID refers to schema invariants (foreign keys, CHECK constraints), not the semantic correctness of application logic."

- question: "'Consistency' in the ACID acronym means the same thing as 'consistency' in the CAP theorem — both ensure that most nodes in a distributed system see the same data at the same time."
  type: true-false
  answer: false
  explanation: "These are completely different concepts that share only a name. ACID consistency means a transaction must preserve all application-defined invariants declared in the schema (constraints, foreign keys, triggers) — it is about transitioning the database between valid states. CAP consistency (linearizability) means all distributed replicas appear as a single up-to-date copy — every read sees the most recent write. Confusing these is a common and consequential error when reasoning about distributed database tradeoffs."

- question: "Why do some distributed databases deliberately relax ACID guarantees, and which property is most commonly relaxed first?"
  type: short-answer
  answer: "Enforcing full ACID requires coordination mechanisms — write-ahead logging, locking protocols, two-phase commit across nodes — that add significant latency and reduce throughput, especially in distributed systems where network communication is slow and unreliable. Isolation is most commonly relaxed first: SQL defines four isolation levels (READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE) of increasing strictness. Most production databases default to READ COMMITTED or REPEATABLE READ rather than full SERIALIZABLE isolation, accepting specific anomalies (dirty reads, non-repeatable reads, phantoms) in exchange for higher concurrency. Durability is rarely relaxed in traditional RDBMS; some NoSQL systems relax it too by using in-memory storage or eventual persistence."
  explanation: "The CAP theorem formalizes a version of this tradeoff: in the presence of network partitions, a distributed system must choose between consistency and availability. Systems like Cassandra and DynamoDB prioritize availability over strong consistency, implementing 'eventual consistency' instead. This is a practical engineering tradeoff, not a flaw — choosing the right consistency model requires understanding the workload's tolerance for stale reads and conflicting writes."
```

## Explainer

You already understand that a database transaction groups multiple operations into a single logical unit — a bank transfer that debits one account and credits another, for example. ACID describes the four guarantees a database must provide for transactions to behave reliably, even in the face of crashes, concurrent access, and hardware failures. Each letter names a specific promise, and understanding the mechanisms behind each one reveals why databases are engineered the way they are.

**Atomicity** means a transaction is all-or-nothing. If a bank transfer debits $500 from Account A but crashes before crediting Account B, atomicity guarantees the debit is rolled back — the database never ends up in a state where money simply vanished. Databases achieve this using a **write-ahead log** (WAL): before modifying any data page, the database first writes a log record describing the intended change. On crash recovery, the database replays committed transactions from the log and undoes uncommitted ones. The log is the source of truth for what happened, and it is what makes rollback possible.

**Consistency** means a transaction must transition the database from one valid state to another, respecting all declared constraints — primary keys, foreign keys, CHECK constraints, unique constraints, and triggers. If your schema says an account balance cannot be negative, any transaction that would create a negative balance is rejected. This is sometimes the most misunderstood ACID property because "consistency" means something different in distributed systems (the C in CAP theorem refers to linearizability, an entirely different concept). In ACID, consistency is about application-level invariants enforced by the schema.

**Isolation** ensures that concurrent transactions do not interfere with each other. Without isolation, one transaction might read half-written data from another, producing phantom results or lost updates. Full isolation (the SERIALIZABLE level) makes concurrent transactions behave as though they ran one at a time. But serializable execution is expensive — it requires extensive locking or validation — so SQL defines weaker isolation levels (READ COMMITTED, REPEATABLE READ) that trade some isolation guarantees for better throughput. Understanding which anomalies each level permits (dirty reads, non-repeatable reads, phantom reads) is essential for choosing the right level for a workload.

**Durability** guarantees that once a transaction commits, its effects survive any subsequent failure — power loss, OS crash, disk failure. The WAL again plays a central role: a transaction is not considered committed until its log records are flushed to stable storage. Even if the in-memory data pages are lost in a crash, the database can reconstruct committed state from the log. Replication and backups extend durability guarantees beyond single-machine failures. Together, these four properties form the contract that makes relational databases trustworthy for financial systems, medical records, and any application where data correctness is non-negotiable.
