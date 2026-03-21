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

## Questions

```yaml
- question: "A database serving a high-traffic e-commerce checkout processes many simultaneous transactions that all read and write the same popular inventory rows. Which concurrency control approach is likely to perform better, and why?"
  type: multiple-choice
  options:
    - "OCC, because it never blocks transactions and achieves maximum parallelism"
    - "Pessimistic locking, because high contention causes OCC aborts that waste all the work done since transaction start"
    - "OCC with timestamp ordering, because timestamps eliminate the need for retries"
    - "OCC, because the validation phase catches conflicts before they affect the database"
  answer: 1
  explanation: "OCC's advantage disappears under high contention. When many transactions touch the same rows, validation frequently fails — transactions are aborted after completing their entire read phase and computation, wasting all that work. Under high contention, pessimistic locking is preferable: it blocks conflicting transactions up front before they do wasted computation, and it doesn't risk livelock from repeated aborts. OCC shines in low-contention, read-heavy workloads where conflicts are genuinely rare."

- question: "In OCC's validation phase, a transaction T is about to commit. Under which condition should T be aborted?"
  type: multiple-choice
  options:
    - "Another transaction committed while T was in its read phase, regardless of what data was accessed"
    - "A committed transaction wrote to a data item that T read during its read phase"
    - "T's read phase lasted longer than a configured timeout threshold"
    - "T performed more write operations than read operations"
  answer: 1
  explanation: "T must be aborted if a committed transaction wrote to data that T read — meaning T's read is now stale and its computations were based on outdated values. This is the core conflict check: T's reads must remain valid relative to everything that committed during T's read phase. The other options are not OCC abort conditions: the mere existence of another committed transaction is not a conflict, timeouts are not a standard OCC mechanism, and the ratio of reads to writes is irrelevant."

- question: "In OCC, transactions that never access overlapping data will always commit without blocking, aborting, or wasting work."
  type: true-false
  answer: true
  explanation: "This is OCC's key advantage in low-contention workloads. If two transactions read and write completely disjoint data items, their validation phases will always pass — there is no conflict to detect. Neither transaction ever waits for the other. In workloads where most transactions are truly independent (e.g., analytics queries on different customer segments), OCC achieves high throughput with zero blocking overhead."

- question: "OCC always outperforms pessimistic locking because it eliminates blocking and allows transactions to proceed concurrently."
  type: true-false
  answer: false
  explanation: "OCC only outperforms pessimistic locking when conflicts are rare. Under high contention, OCC can perform worse: transactions complete their entire read phase and computation, then are aborted at validation, wasting all that work. In the worst case, a transaction may be aborted and retried repeatedly (livelock). Pessimistic locking blocks transactions earlier, before wasted work accumulates. The right choice depends entirely on the workload's contention level."

- question: "Describe the three phases of OCC and explain why conflicts detected at the validation phase can represent more wasted work than if pessimistic locking had blocked the transaction earlier."
  type: short-answer
  answer: "OCC has three phases: (1) Read phase — the transaction reads data into a private workspace and performs all computations, acquiring no locks; (2) Validation phase — at commit time, the system checks whether any committed transaction wrote to data this transaction read; (3) Write phase — if validation passes, changes are applied to the database. If validation fails, all work from the read phase is discarded and the transaction must restart from scratch. Pessimistic locking detects the conflict immediately when the second transaction tries to acquire the same lock, blocking it before it does any work on conflicting data. OCC allows both transactions to do all their work first, then discards one — making the wasted work proportional to the transaction's read phase duration."
  explanation: "This asymmetry — early blocking vs. late abort — is the fundamental tradeoff. OCC bets that validation will usually pass. When the bet fails in high-contention scenarios, the wasted computation can be substantial, especially for long-running read-heavy transactions."
```

## Explainer

From your study of concurrency control and isolation levels, you know the core problem: multiple transactions running simultaneously can interfere with each other, producing anomalies like dirty reads, lost updates, and write skew. Lock-based concurrency control (the pessimistic approach) solves this by making transactions acquire locks before accessing data — if two transactions want the same row, one waits. This is safe but introduces blocking, deadlock risk, and reduced throughput when many transactions contend for the same data. **Optimistic concurrency control** takes the opposite bet: assume conflicts are rare, let every transaction proceed without locks, and check for conflicts only at commit time.

An OCC transaction runs in three phases. During the **read phase**, it reads data from the database and performs all its computations on a private workspace — a local copy of the data it needs. No locks are acquired and no other transaction is blocked. During the **validation phase** (at commit time), the system checks whether this transaction's reads and writes conflict with any other transaction that committed during the interval. Specifically, it verifies that no committed transaction wrote to data that this transaction read (which would mean it operated on stale data) and that no committed transaction read data that this transaction is about to overwrite (which could violate serializability). If validation passes, the **write phase** applies the transaction's changes to the actual database. If validation fails, the transaction is aborted and must be retried.

**Timestamp ordering** is a related optimistic technique. Each transaction receives a timestamp when it begins, and the system enforces that the final effect is equivalent to executing transactions in timestamp order. Every data item tracks the timestamp of the last transaction that read it and the last that wrote it. If a transaction tries to read a value that was already overwritten by a later-timestamped transaction, or tries to write a value that was already read by a later-timestamped one, the operation violates timestamp order and the transaction is aborted. Like OCC, this avoids locks entirely — conflicts are detected by comparing timestamps rather than by blocking.

The trade-off between optimistic and pessimistic approaches depends on your workload. OCC shines when conflicts are genuinely rare — in read-heavy workloads, analytics queries, or systems where transactions touch mostly disjoint data. Under high contention, however, OCC can degrade: many transactions reach the validation phase only to be aborted and retried, wasting the work they already did. In the worst case, livelock can occur where transactions repeatedly conflict and abort each other. Pessimistic locking is more predictable under contention because it forces waiting up front rather than wasting work. Modern databases like PostgreSQL use multiversion concurrency control (MVCC), which builds on these ideas by maintaining multiple versions of each row, allowing readers and writers to operate concurrently without blocking — a topic you will encounter next.
