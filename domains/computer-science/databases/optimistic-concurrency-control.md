---
id: optimistic-concurrency-control
title: 'Optimistic Concurrency Control: Version Numbers'
domain: computer-science
course: databases
prerequisites:
- id: lost-update-problem
  type: hard
tags:
- concurrency
- conflict-detection
- mvcc
stage: formal-systems
status: validated
---

# Optimistic Concurrency Control: Version Numbers

## Core Idea
Optimistic concurrency control avoids locks by versioning rows (timestamps or counters) and detecting conflicts at UPDATE time. If the version has changed since READ, the UPDATE is rejected.

## How It's Best Learned
Implement an UPDATE with a WHERE clause checking the current version, simulating an application-level conflict detection.

## Common Misconceptions
Optimistic control assumes conflicts are rare and works well with low contention. Under high contention, rollbacks and retries degrade performance.

## Questions

```yaml
- question: "Transaction T1 and T2 both read row id=42 at version=5. T1 updates the row first, bumping it to version=6. T2 then executes: UPDATE accounts SET balance=300, version=6 WHERE id=42 AND version=5. What happens?"
  type: multiple-choice
  options:
    - "T2's update succeeds and the balance is set to 300"
    - "T2's update matches zero rows — the conflict is detected and T2 must retry"
    - "T2 blocks, waiting for T1 to release a lock before proceeding"
    - "A deadlock is recorded and both transactions are rolled back"
  answer: 1
  explanation: "This is the core mechanism of OCC. T1 already changed the version from 5 to 6, so T2's WHERE clause (version=5) no longer matches. The update returns zero affected rows, signaling to the application that a concurrent modification occurred. T2 must re-read the current row (version 6) and recompute its update. No lock was held, no blocking occurred — the conflict was detected only at write time."

- question: "Which workload is most suited to optimistic concurrency control?"
  type: multiple-choice
  options:
    - "A high-frequency trading platform where many transactions update the same account balance per second"
    - "A content platform where millions of users each update only their own profile data"
    - "A ticket booking system during a flash sale where thousands of users compete for the last 10 seats"
    - "A bank transfer system where strict consistency is enforced across accounts"
  answer: 1
  explanation: "OCC excels when conflicts are rare — when transactions are unlikely to touch the same rows simultaneously. A platform where users update their own distinct profiles has very low contention: most transactions will never compete, so the overhead of locks is wasteful. The other options involve high contention (many transactions competing for the same rows), where OCC's retry storms would degrade performance relative to pessimistic locking."

- question: "In optimistic concurrency control, a transaction holds no locks during its read and processing phases."
  type: true-false
  answer: true
  explanation: "This is the defining characteristic of OCC. The transaction reads data, does its work, and only at commit time checks whether the data has changed (via the version number WHERE clause). No locks are acquired during reading — contrast this with pessimistic locking where a read lock is held from the moment of the read until commit. The lock-free read phase is why OCC performs well when contention is low."

- question: "Optimistic concurrency control prevents most data conflicts between concurrent transactions by detecting them before they can occur."
  type: true-false
  answer: false
  explanation: "OCC detects conflicts at write time — after they have already occurred — and responds by rejecting the update and requiring a retry. It does not prevent conflicts from happening; it detects and handles them after the fact. Pessimistic locking prevents conflicts by blocking concurrent access upfront. The tradeoff is that OCC's detection-after-the-fact is cheaper when conflicts are rare, but each detected conflict requires discarding work and retrying."

- question: "Why can optimistic concurrency control perform worse than pessimistic locking under high contention, even though OCC avoids lock overhead?"
  type: short-answer
  answer: "Under high contention, many transactions compete for the same rows, so a large fraction of OCC transactions will find that someone else modified the row before they committed. Each failed transaction must discard all its work, re-read the current data, redo the computation, and attempt the update again — only to potentially fail again. This retry storm means the system burns CPU and I/O on work that is repeatedly discarded. Pessimistic locking, by contrast, makes transactions wait in turn and then complete successfully — no work is wasted. The relative efficiency flips depending on whether wasted retries outweigh the cost of blocking waits."
  explanation: "The key insight is that OCC's efficiency advantage depends on the assumption that most transactions will succeed on their first try. When that assumption breaks down under contention, the retry cost dominates."
```

## Explainer

You know from studying the lost update problem that two transactions can silently overwrite each other's changes if nothing coordinates their access to the same row. The traditional solution is locking — grab a lock before reading, hold it until you commit, and block anyone else from touching the data. **Optimistic concurrency control** takes the opposite bet: instead of preventing conflicts upfront, it lets transactions proceed freely and checks for conflicts only at the moment of writing.

The mechanism relies on **version numbers** (or timestamps) attached to each row. When a transaction reads a row, it notes the current version — say, version 5. The transaction does its work locally without holding any locks. When it's ready to update, it issues something like `UPDATE accounts SET balance = 750, version = 6 WHERE id = 42 AND version = 5`. The `WHERE version = 5` clause is the critical check: if no other transaction has modified the row since our read, the version is still 5 and the update succeeds. If another transaction snuck in and changed the row (bumping it to version 6), our WHERE clause matches zero rows, and we know our read was stale. The application detects the zero-row update, discards its work, re-reads the current data, and retries.

The beauty of this approach is that the **common case is fast**. If conflicts are rare — which they are in most web applications where thousands of users rarely touch the same row at the same instant — transactions never block each other. There's no lock manager, no wait queues, and no deadlock risk. Readers never block writers, and writers never block readers. Compare this to pessimistic locking where every access acquires a lock, and transactions frequently wait in line even when no actual conflict would have occurred.

The tradeoff becomes painful under **high contention**. If many transactions compete for the same rows, optimistic control produces a storm of failed updates and retries. Each retry re-reads the data and attempts the update again, only to potentially fail again because yet another transaction beat it. Under extreme contention, the system can waste more work on retries than it saves by avoiding locks. This is why the choice between optimistic and pessimistic concurrency depends on your workload: optimistic for read-heavy, low-conflict scenarios (most web apps, content management systems); pessimistic for write-heavy, high-conflict scenarios (inventory systems during flash sales, financial trading platforms).
