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
status: validated
---

# Transactions and ACID Properties

## Core Idea
A transaction is a logical unit of work executing multiple SQL statements atomically. ACID properties guarantee: Atomicity (all-or-nothing), Consistency (valid state to valid state), Isolation (independent execution), Durability (permanent after commit). ACID ensures database reliability and correctness in multi-user environments.

## How It's Best Learned
Study concrete examples of ACID property violations and how they are prevented. Practice writing transaction code and understanding rollback scenarios. Compare different isolation levels and their consistency guarantees.

## Questions

```yaml
- question: "A database crash occurs midway through a transaction that has debited one bank account but not yet credited the other. When the server restarts, what happens to the partial changes?"
  type: multiple-choice
  options:
    - "The debit is permanent because it executed before the crash; the missing credit is flagged for manual correction"
    - "The entire transaction is rolled back to its pre-transaction state, as if neither operation had occurred"
    - "The database prompts an administrator to decide whether to complete or undo the transaction"
    - "The credit is automatically retried until it succeeds"
  answer: 1
  explanation: "This is Atomicity: all-or-nothing. The database uses a write-ahead log to record changes before they affect actual data pages. On crash recovery, the system finds the incomplete transaction in the log (no COMMIT entry) and rolls back all its changes — the debited account is restored to its original balance. This is precisely why Atomicity exists: the scenario in option A (money disappearing) would be a catastrophic failure. 'Partial execution' is never the outcome; the database either commits fully or undoes fully."

- question: "Two users simultaneously read an account balance of $500, then both attempt to withdraw $400. Without sufficient isolation, what problem could occur?"
  type: multiple-choice
  options:
    - "Neither withdrawal would succeed, because the database detects the conflict automatically"
    - "Both withdrawals could succeed, leaving a balance of -$300 — a consistency violation"
    - "The second withdrawal would automatically wait until the first completed"
    - "This scenario is impossible; the database serializes all requests by default"
  answer: 1
  explanation: "This is the classic 'lost update' problem caused by insufficient isolation. Without proper isolation, both transactions read $500, both verify $500 ≥ $400, and both write $100 as the new balance — meaning $800 was withdrawn but only $400 was deducted. This violates Consistency and illustrates why Isolation matters: each transaction must see a consistent view of the data, not the in-progress state of concurrent transactions. Higher isolation levels prevent this by locking rows or using snapshot isolation."

- question: "The SERIALIZABLE isolation level guarantees that transactions will execute one at a time, in strict sequence, with no physical parallelism."
  type: true-false
  answer: false
  explanation: "SERIALIZABLE guarantees that the *results* are equivalent to some serial execution — it does not mean transactions actually run one at a time. The database uses techniques like snapshot isolation, MVCC, or locking to allow physical concurrency while ensuring the logical outcome matches a serial run. The distinction matters because truly sequential execution would destroy performance; SERIALIZABLE is achievable with acceptable performance by detecting and aborting conflicting transactions rather than preventing all concurrency. The guarantee is about observable outcomes, not physical execution order."

- question: "Durability means that if a transaction commits successfully, its changes will survive even if the database server crashes one second later."
  type: true-false
  answer: true
  explanation: "This is the precise guarantee Durability provides. By flushing the write-ahead log to stable storage before acknowledging the COMMIT to the client, the database ensures committed changes can be recovered even from a complete server failure. An uncommitted transaction that is lost in a crash is fine — Atomicity handles that via rollback. Losing a committed transaction would be a Durability violation. This is why databases force a synchronous disk flush on commit: it is slower, but it is what makes the guarantee possible."

- question: "Explain why Isolation is described as the 'subtlest' ACID property and what tradeoff it forces database designers to navigate."
  type: short-answer
  answer: "Atomicity, Consistency, and Durability are essentially binary: transactions either commit fully or they don't; constraints either hold or the transaction aborts; committed data either survives failure or it doesn't. Isolation is a spectrum. Perfect isolation means every transaction runs as if it is the only one — but serializing all access destroys performance in multi-user systems. Databases offer multiple isolation levels (READ COMMITTED, REPEATABLE READ, SERIALIZABLE) that progressively trade away anomaly prevention for concurrency. Choosing the right level requires understanding which anomalies the application can tolerate."
  explanation: "The key insight is that the other three ACID properties are achieved or not achieved; isolation is calibrated to match workload requirements. A financial system processing transfers likely requires SERIALIZABLE to prevent lost updates. A social media feed might tolerate READ COMMITTED, accepting slightly stale reads in exchange for higher throughput. This tradeoff is fundamental to database design, which is why isolation levels exist as a concept — there is no single right answer, only a range of consistency-performance tradeoffs appropriate to different use cases."
```

## Explainer

You already know how to insert, update, and delete data with individual SQL statements. But real-world operations often require multiple statements that must succeed or fail together. A bank transfer, for instance, debits one account and credits another — if the debit succeeds but the credit fails (say, due to a crash), money has vanished. A **transaction** wraps multiple statements into a single logical unit: either all of them take effect, or none of them do. You begin a transaction with `BEGIN`, execute your statements, and finalize with `COMMIT` (apply everything) or `ROLLBACK` (undo everything).

The **ACID properties** formalize what transactions guarantee. **Atomicity** means all-or-nothing: if any statement in the transaction fails or the system crashes mid-transaction, every change made so far is rolled back as if the transaction never started. The database achieves this by writing changes to a **write-ahead log** before modifying actual data pages — on crash recovery, it replays or undoes logged operations to restore a consistent state. **Consistency** means a transaction takes the database from one valid state to another, respecting all constraints (foreign keys, uniqueness, CHECK constraints). If a transaction would violate a constraint, it is aborted.

**Isolation** is the subtlest property: it determines how much of a transaction's in-progress work is visible to other concurrent transactions. Perfect isolation would mean every transaction runs as if it were the only one — but that would require serializing all access, destroying performance. In practice, databases offer **isolation levels** that trade consistency for concurrency. At READ COMMITTED (the default in PostgreSQL), a transaction sees only data committed before each statement executes. At SERIALIZABLE, the database guarantees results equivalent to running transactions one at a time, detecting and aborting conflicting ones. Lower isolation levels permit anomalies like dirty reads (seeing uncommitted data) or phantom reads (seeing new rows inserted by another transaction mid-query).

**Durability** means that once a transaction commits, its changes survive any subsequent failure — power loss, crash, disk error. The database ensures this by flushing the write-ahead log to stable storage before acknowledging the commit. Even if the server crashes immediately after, the committed data can be recovered from the log on restart. Together, the four ACID properties let you reason about database operations as if they were simple, sequential, and permanent — even when the reality involves concurrent users, network failures, and hardware faults. Understanding which property is doing the work in a given scenario is the foundation for the concurrency control and isolation topics that follow.
