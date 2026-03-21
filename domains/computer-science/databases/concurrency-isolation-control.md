---
id: concurrency-isolation-control
title: Concurrency Control and Isolation Levels
domain: computer-science
course: databases
prerequisites:
- id: transaction-properties-acid
  type: hard
tags:
- concurrency
- isolation
- locking
- MVCC
- serializability
stage: formal-systems
status: draft
---

# Concurrency Control and Isolation Levels

## Core Idea
Concurrency control ensures multiple concurrent transactions do not interfere with each other. Isolation levels define the degree of isolation: read uncommitted, read committed, repeatable read, serializable. Mechanisms include pessimistic locking (locks), optimistic locking (version checks), and multi-version concurrency control (MVCC). Choosing appropriate isolation is crucial for correctness and performance.

## How It's Best Learned
Trace execution of concurrent transactions at different isolation levels, identify phenomena (dirty reads, non-repeatable reads, phantoms), understand locking protocols, and analyze trade-offs between isolation strength and concurrency.

## Common Misconceptions
Higher isolation levels are not always better—they reduce concurrency. Serializable isolation can bottleneck performance. Most applications use read committed as a pragmatic balance.

## Questions

```yaml
- question: "A banking application processes transfers between accounts. Two concurrent transactions each read the same account balance, then both subtract the same amount, and both write back their result — causing the balance to only reflect one withdrawal instead of two. Which isolation level is the minimum required to prevent this anomaly?"
  type: multiple-choice
  options:
    - "Read Uncommitted — it prevents all dirty reads which cause this problem"
    - "Read Committed — it ensures both transactions see committed data before writing"
    - "Repeatable Read — it ensures a transaction's reads remain stable, preventing the lost update"
    - "Read Committed is sufficient; the application code should handle this with retry logic instead"
  answer: 2
  explanation: "This is a lost update anomaly, which requires at least Repeatable Read to prevent. At Read Committed, both transactions can read the same committed balance, compute their updates independently, and write back — one update is lost. Repeatable Read locks the row after the first read, forcing the second transaction to wait until the first commits. The application-retry answer (D) sidesteps isolation levels but does not address the root cause within the database."

- question: "Which anomaly can still occur at Repeatable Read isolation but is prevented by Serializable?"
  type: multiple-choice
  options:
    - "Dirty read — reading uncommitted data from another transaction"
    - "Non-repeatable read — a row changes between two reads within the same transaction"
    - "Phantom read — new rows matching a WHERE clause appear between two scans"
    - "Lost update — two transactions overwrite each other's changes"
  answer: 2
  explanation: "Phantom reads are the anomaly that Repeatable Read cannot prevent but Serializable does. Repeatable Read locks rows you have read, so existing rows cannot change — but it does not prevent other transactions from inserting new rows that match your query's WHERE clause. If you run the same range query twice, new rows may 'appear.' Serializable adds range locks (or predicate locks) to prevent this. Dirty reads and non-repeatable reads are both prevented by Repeatable Read."

- question: "Choosing Serializable isolation is always the safest and best-performing option because it prevents all anomalies."
  type: true-false
  answer: false
  explanation: "Serializable prevents all anomalies but imposes significant performance costs. It forces transactions to execute as if they ran one at a time, which can cause transactions to block waiting for locks, or to abort and retry when conflicts are detected. Under high concurrency, this dramatically reduces throughput. The right isolation level is the *weakest* one that still guarantees your application's correctness — for most read-heavy applications, Read Committed suffices and provides far better concurrency."

- question: "In a database using MVCC (multi-version concurrency control), a read query never blocks a concurrent write to the same row."
  type: true-false
  answer: true
  explanation: "MVCC maintains multiple versions of each row. A read query sees a consistent snapshot from the start of its transaction and reads the version of the row that existed at that snapshot time — it does not compete with a writer for the current version. This is the key advantage of MVCC: readers never block writers and writers never block readers. Only write-write conflicts cause blocking or aborts, which is why MVCC databases like PostgreSQL handle read-heavy workloads so efficiently."

- question: "Why is 'use the highest isolation level always' not good advice for production database applications?"
  type: short-answer
  answer: "Higher isolation levels reduce concurrency — they require holding locks longer or aborting conflicting transactions, which causes other transactions to wait or retry. Serializable isolation may be necessary for financial operations requiring full correctness, but for typical web applications (where most operations are reads), it would serialize all access and dramatically reduce throughput. The right choice is the weakest isolation level that still prevents the specific anomalies your application cannot tolerate."
  explanation: "The core insight is that isolation is a tradeoff, not a one-way scale where 'more is better.' Read Committed is the default in most production databases precisely because it prevents the most dangerous anomaly (dirty reads) while preserving high concurrency. Engineers must understand what anomalies each level prevents and which their application can tolerate, rather than defaulting to the strongest level out of caution."
```

## Explainer

You already know from ACID properties that the "I" — isolation — means each transaction should behave as if it were running alone, even when many transactions execute simultaneously. In practice, full isolation is expensive, so databases offer a spectrum of **isolation levels** that trade correctness guarantees for performance. Understanding this spectrum is essential for building applications that are both correct and responsive under concurrent load.

The SQL standard defines four isolation levels, each preventing an increasingly dangerous set of anomalies. **Read Uncommitted** is the weakest: a transaction can see uncommitted changes from other transactions (a **dirty read**). This is rarely used because reading data that might be rolled back leads to nonsensical results. **Read Committed** prevents dirty reads — you only see data that has been committed — but if you read the same row twice within your transaction, another committed transaction might have changed it in between, producing a **non-repeatable read**. **Repeatable Read** prevents both dirty and non-repeatable reads by ensuring that any row you read will not change for the duration of your transaction. However, new rows matching your query's conditions can still appear — these **phantom reads** occur when another transaction inserts rows that satisfy a WHERE clause you already evaluated. **Serializable** prevents all three anomalies, guaranteeing that the outcome is equivalent to running the transactions one at a time in some serial order.

Databases enforce these levels through different mechanisms. **Pessimistic locking** acquires locks on data before accessing it: shared locks for reads, exclusive locks for writes. A transaction holds its locks until it commits or rolls back, blocking other transactions that need conflicting access. This is simple but can cause **deadlocks** when two transactions each hold a lock the other needs. **Optimistic concurrency control** takes a different approach: transactions proceed without locks and check at commit time whether any conflicts occurred. If another transaction modified the same data, the committing transaction is rolled back and retried. **Multi-version concurrency control** (MVCC), used by PostgreSQL and many modern databases, keeps multiple versions of each row. Readers see a snapshot of the database as of their transaction's start time, so they never block writers and writers never block readers. This dramatically improves throughput for read-heavy workloads.

The practical choice of isolation level depends on your application's tolerance for anomalies. Most production applications default to **Read Committed** because it prevents the worst anomaly (dirty reads) while allowing high concurrency. Financial applications or inventory systems that must prevent double-spending or overselling may require Repeatable Read or Serializable. The key insight is that stronger isolation is not "better" in an absolute sense — it is a tradeoff. Serializable isolation may force transactions to wait or abort, reducing throughput. The right level is the weakest one that still guarantees your application's correctness requirements.
