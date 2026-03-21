---
id: isolation-level-serializable
title: 'Isolation Level: SERIALIZABLE'
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
tags:
- isolation
- concurrency
- strongest-level
stage: formal-systems
status: draft
---

# Isolation Level: SERIALIZABLE

## Core Idea
SERIALIZABLE is the highest isolation level; it prevents all anomalies (dirty reads, non-repeatable reads, phantom reads) by effectively serializing transactions, though at a performance cost.

## Questions

```yaml
- question: "A banking application runs two concurrent transactions: T1 sums the balances of all accounts, and T2 deposits money into one account. Under SERIALIZABLE isolation, which outcome is possible?"
  type: multiple-choice
  options:
    - "T1 reads the same account's balance both before and after T2's deposit within a single scan"
    - "T2's deposit appears in some but not all of T1's reads of that account"
    - "The result is identical to T1 completing entirely before T2, or T2 completing entirely before T1"
    - "T1 and T2 freely interleave since SERIALIZABLE only prevents dirty reads"
  answer: 2
  explanation: "SERIALIZABLE guarantees that the result of concurrent execution is indistinguishable from some serial execution. T1 will see either all of T2's changes or none — as if they ran one after the other. Options A and B describe phantoms and non-repeatable reads that SERIALIZABLE specifically prevents. Option D confuses SERIALIZABLE with READ COMMITTED, the weakest level that prevents only dirty reads."

- question: "PostgreSQL implements SERIALIZABLE using Serializable Snapshot Isolation (SSI) rather than strict two-phase locking (2PL). What is the key operational difference?"
  type: multiple-choice
  options:
    - "SSI prevents more anomalies than strict 2PL, including dirty writes that 2PL cannot prevent"
    - "SSI lets transactions work concurrently on snapshots and aborts conflicting transactions at commit time rather than blocking them with locks"
    - "SSI only applies to read-only transactions; 2PL handles transactions that write"
    - "SSI requires explicit LOCK TABLE statements in application code, while 2PL acquires locks automatically"
  answer: 1
  explanation: "The core difference is blocking vs. abort-and-retry. Strict 2PL blocks one transaction while another holds a conflicting lock, reducing parallelism. SSI lets all transactions run on consistent snapshots, tracks dependency patterns between them, and aborts any transaction whose execution pattern creates a cycle that would make the result non-serializable. Applications must include retry logic for aborted transactions. Both approaches achieve the same correctness guarantee but with different performance characteristics."

- question: "Under SERIALIZABLE isolation, some transactions may be aborted mid-execution and require application-level retry logic to handle."
  type: true-false
  answer: true
  explanation: "This is the practical cost of SERIALIZABLE. SSI-based implementations (like PostgreSQL) abort transactions when they detect a 'dangerous structure' — a dependency cycle indicating non-serializability. The aborted transaction must be retried. Strict 2PL avoids aborts (using blocking instead) but can deadlock, which also requires retry. Applications targeting SERIALIZABLE must be designed to retry on serialization failures."

- question: "SERIALIZABLE isolation guarantees that concurrent transactions execute in the exact chronological order they were submitted to the database."
  type: true-false
  answer: false
  explanation: "SERIALIZABLE guarantees equivalence to *some* serial order — not necessarily the order of submission. The database chooses (or discovers) a valid serial ordering that matches what actually happened. In SSI, concurrent transactions may partially overlap in time; the guarantee is that the resulting data state looks as though they ran one at a time in some order. The actual submission order is irrelevant to serializability."

- question: "Explain why 'equivalent to a serial execution' is different from 'executed serially,' and why this distinction matters for a high-throughput database."
  type: short-answer
  answer: "Executing transactions serially — one at a time with no overlap — would eliminate all concurrency anomalies but also eliminate concurrency itself, giving the throughput of a single-threaded system. 'Equivalent to a serial execution' means the database can still run transactions concurrently (lapping each other in time), as long as the final committed state is identical to what some serial order would produce. This preserves correctness while allowing the parallelism needed for performance. SSI achieves this by detecting dangerous interleavings and aborting them rather than preventing all overlap."
  explanation: "The distinction is between the *outcome* of execution (which must look serial) and the *process* of execution (which can be concurrent). High-throughput databases like PostgreSQL serve thousands of transactions per second — true serial execution would create a bottleneck. SERIALIZABLE at the outcome level preserves correctness guarantees that applications depend on (no phantom reads, no write skew) while still allowing the database engine to schedule transactions with substantial overlap."
```

## Explainer

You already know from studying concurrency control that databases offer a spectrum of isolation levels, each preventing an increasing set of anomalies. **SERIALIZABLE** sits at the top of that spectrum: it guarantees that the result of executing concurrent transactions is identical to some serial execution — as if the transactions ran one after another with no overlap at all. This means dirty reads, non-repeatable reads, and phantom reads are all impossible. The database might still execute transactions concurrently for performance, but it ensures the outcome is indistinguishable from a serial order.

How databases achieve this varies. Traditional implementations use **strict two-phase locking** (2PL): every transaction acquires locks before accessing data and holds all locks until it commits or aborts. For SERIALIZABLE, this includes **predicate locks** (also called range locks) that cover not just individual rows but entire ranges matching a query's WHERE clause, preventing phantom inserts. If transaction A reads "all orders where amount > 1000," a predicate lock prevents transaction B from inserting a new order with amount 1500 until A finishes. The downside is that aggressive locking increases the chance of **deadlocks** — situations where two transactions each wait for a lock the other holds — and reduces concurrency because transactions block each other more frequently.

Modern databases like PostgreSQL use a more sophisticated approach called **Serializable Snapshot Isolation** (SSI). Instead of blocking transactions with locks, SSI lets each transaction work on a consistent snapshot of the database (as in MVCC) and tracks dependencies between transactions. At commit time, the system checks whether the dependency graph contains a cycle — a pattern called a "dangerous structure" — that would make the execution non-serializable. If it detects one, it aborts one of the involved transactions, which the application must then retry. SSI achieves serializability with much less blocking than 2PL, making it practical for high-throughput systems.

The key practical consideration is **when to use SERIALIZABLE**. It is the right choice when your application's correctness depends on conditions that span multiple reads — for example, ensuring that a seat is not double-booked, or that an account balance never goes negative across concurrent withdrawals. In these cases, weaker isolation levels allow race conditions that produce incorrect results. The cost is that some transactions will be aborted and must be retried, so your application code must include retry logic. Many teams default to Read Committed for most operations and selectively escalate to SERIALIZABLE for the critical transactions where correctness cannot be compromised.
