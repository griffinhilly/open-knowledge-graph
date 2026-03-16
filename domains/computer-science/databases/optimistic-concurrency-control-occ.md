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

## Explainer

From your study of concurrency control and isolation levels, you know the core problem: multiple transactions running simultaneously can interfere with each other, producing anomalies like dirty reads, lost updates, and write skew. Lock-based concurrency control (the pessimistic approach) solves this by making transactions acquire locks before accessing data — if two transactions want the same row, one waits. This is safe but introduces blocking, deadlock risk, and reduced throughput when many transactions contend for the same data. **Optimistic concurrency control** takes the opposite bet: assume conflicts are rare, let every transaction proceed without locks, and check for conflicts only at commit time.

An OCC transaction runs in three phases. During the **read phase**, it reads data from the database and performs all its computations on a private workspace — a local copy of the data it needs. No locks are acquired and no other transaction is blocked. During the **validation phase** (at commit time), the system checks whether this transaction's reads and writes conflict with any other transaction that committed during the interval. Specifically, it verifies that no committed transaction wrote to data that this transaction read (which would mean it operated on stale data) and that no committed transaction read data that this transaction is about to overwrite (which could violate serializability). If validation passes, the **write phase** applies the transaction's changes to the actual database. If validation fails, the transaction is aborted and must be retried.

**Timestamp ordering** is a related optimistic technique. Each transaction receives a timestamp when it begins, and the system enforces that the final effect is equivalent to executing transactions in timestamp order. Every data item tracks the timestamp of the last transaction that read it and the last that wrote it. If a transaction tries to read a value that was already overwritten by a later-timestamped transaction, or tries to write a value that was already read by a later-timestamped one, the operation violates timestamp order and the transaction is aborted. Like OCC, this avoids locks entirely — conflicts are detected by comparing timestamps rather than by blocking.

The trade-off between optimistic and pessimistic approaches depends on your workload. OCC shines when conflicts are genuinely rare — in read-heavy workloads, analytics queries, or systems where transactions touch mostly disjoint data. Under high contention, however, OCC can degrade: many transactions reach the validation phase only to be aborted and retried, wasting the work they already did. In the worst case, livelock can occur where transactions repeatedly conflict and abort each other. Pessimistic locking is more predictable under contention because it forces waiting up front rather than wasting work. Modern databases like PostgreSQL use multiversion concurrency control (MVCC), which builds on these ideas by maintaining multiple versions of each row, allowing readers and writers to operate concurrently without blocking — a topic you will encounter next.
