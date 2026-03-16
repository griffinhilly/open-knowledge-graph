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

## Explainer

You already know from studying concurrency control that databases offer a spectrum of isolation levels, each preventing an increasing set of anomalies. **SERIALIZABLE** sits at the top of that spectrum: it guarantees that the result of executing concurrent transactions is identical to some serial execution — as if the transactions ran one after another with no overlap at all. This means dirty reads, non-repeatable reads, and phantom reads are all impossible. The database might still execute transactions concurrently for performance, but it ensures the outcome is indistinguishable from a serial order.

How databases achieve this varies. Traditional implementations use **strict two-phase locking** (2PL): every transaction acquires locks before accessing data and holds all locks until it commits or aborts. For SERIALIZABLE, this includes **predicate locks** (also called range locks) that cover not just individual rows but entire ranges matching a query's WHERE clause, preventing phantom inserts. If transaction A reads "all orders where amount > 1000," a predicate lock prevents transaction B from inserting a new order with amount 1500 until A finishes. The downside is that aggressive locking increases the chance of **deadlocks** — situations where two transactions each wait for a lock the other holds — and reduces concurrency because transactions block each other more frequently.

Modern databases like PostgreSQL use a more sophisticated approach called **Serializable Snapshot Isolation** (SSI). Instead of blocking transactions with locks, SSI lets each transaction work on a consistent snapshot of the database (as in MVCC) and tracks dependencies between transactions. At commit time, the system checks whether the dependency graph contains a cycle — a pattern called a "dangerous structure" — that would make the execution non-serializable. If it detects one, it aborts one of the involved transactions, which the application must then retry. SSI achieves serializability with much less blocking than 2PL, making it practical for high-throughput systems.

The key practical consideration is **when to use SERIALIZABLE**. It is the right choice when your application's correctness depends on conditions that span multiple reads — for example, ensuring that a seat is not double-booked, or that an account balance never goes negative across concurrent withdrawals. In these cases, weaker isolation levels allow race conditions that produce incorrect results. The cost is that some transactions will be aborted and must be retried, so your application code must include retry logic. Many teams default to Read Committed for most operations and selectively escalate to SERIALIZABLE for the critical transactions where correctness cannot be compromised.
