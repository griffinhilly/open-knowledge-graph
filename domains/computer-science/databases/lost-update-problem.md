---
id: lost-update-problem
title: 'Lost Update Problem: Overwriting Concurrent Writes'
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
builds-toward:
- optimistic-concurrency-control
- pessimistic-concurrency-control
tags:
- concurrency
- data-integrity
- write-conflicts
stage: formal-systems
status: validated
---

# Lost Update Problem: Overwriting Concurrent Writes

## Core Idea
A lost update occurs when two transactions read the same row, modify it independently, and write back their versions in sequence—the first write is overwritten by the second.

## How It's Best Learned
Simulate two concurrent sessions reading a balance, incrementing it, and writing it back to observe the first increment disappearing.

## Common Misconceptions
Lost updates can occur even under READ COMMITTED isolation if explicit locking is not used. Row-level locks prevent this only if the lock is held until COMMIT.

## Questions

```yaml
- question: "A bank account holds $500. Transaction A reads $500 and plans to write $600 (adding $100). Transaction B reads $500 and plans to write $700 (adding $200). A commits first, then B commits. What is the final balance?"
  type: multiple-choice
  options:
    - "$800 — both deposits are applied"
    - "$700 — B's write silently overwrites A's $600, losing A's $100 deposit"
    - "$600 — A's write is preserved and B's is rejected because A committed first"
    - "$500 — both writes are rolled back because a conflict was detected"
  answer: 1
  explanation: "This is a classic lost update. B read $500 before A committed, so B's write is based on the original value. When B writes $700, it overwrites A's $600 — A's $100 deposit is permanently lost. The correct balance should be $800. Option C (B rejected) would require pessimistic locking that was never acquired. Option D (both rolled back) would require a detection mechanism like optimistic concurrency control with versioning."

- question: "Which of the following correctly prevents the lost update problem in a concurrent database system?"
  type: multiple-choice
  options:
    - "Using the READ COMMITTED isolation level, which is the default in many databases"
    - "Wrapping each transaction in a BEGIN/COMMIT block"
    - "Using SELECT ... FOR UPDATE to lock the row at read time, held until COMMIT"
    - "Using READ UNCOMMITTED isolation for faster performance"
  answer: 2
  explanation: "SELECT ... FOR UPDATE acquires a row-level exclusive lock when reading, preventing any other transaction from reading or modifying the row until the lock is released at COMMIT. This serializes access to the row, eliminating the race condition. Option A is the key misconception: READ COMMITTED prevents dirty reads but does NOT prevent lost updates — both transactions can still read the same committed value and race to write. Options B and D provide no protection against lost updates."

- question: "READ COMMITTED isolation level prevents the lost update problem in most database systems."
  type: true-false
  answer: false
  explanation: "READ COMMITTED only guarantees that you read committed (not dirty) data — it does not prevent two transactions from reading the same committed value and then both writing over it. In the classic scenario, both transactions commit their reads before either writes, so both reads are of committed data, yet the lost update still occurs. Preventing lost updates requires either explicit row locking (SELECT ... FOR UPDATE), optimistic concurrency control with version checking, or a higher isolation level like REPEATABLE READ in databases that detect write conflicts."

- question: "Optimistic concurrency control prevents lost updates by rejecting a write if the underlying row has changed since it was read, typically using a version number or timestamp."
  type: true-false
  answer: true
  explanation: "Optimistic concurrency control (OCC) proceeds without locks: each transaction reads freely, but at write time compares the current row version to the version it read. If they differ, another transaction has intervened and the write is rejected (the transaction must retry). This prevents the lost update without blocking concurrent reads, making it efficient when conflicts are rare. The tradeoff: under high conflict rates, many retries occur, making pessimistic locking more practical."

- question: "Why is the lost update problem particularly hard to detect through testing individual transactions? Why does it only emerge from concurrent execution?"
  type: short-answer
  answer: "Each transaction in isolation behaves correctly: read the balance, add the deposit, write the new total. There is no bug within any single transaction's logic. The error only emerges from the interleaving of two transactions: both read the same value before either writes, so each overwrites the other's result without any violation of internal logic. Unit tests of individual transactions will always pass. The bug is a property of the schedule (the ordering of operations across transactions), not of any single transaction."
  explanation: "This is what makes concurrency bugs in databases especially dangerous: they are invisible to standard testing but can cause silent data corruption at scale. The lost update is detectable only through integration tests that run multiple concurrent sessions simultaneously, or through careful reasoning about transaction schedules. Systems under low load may never trigger the race condition, then it appears suddenly under production traffic."
```

## Explainer

You know from concurrency control that databases allow multiple transactions to execute simultaneously for performance, and that this concurrency creates the possibility of interference between transactions. The **lost update problem** is one of the most intuitive concurrency hazards: two transactions both read the same row, each computes a new value based on what it read, and both write back their results — but the second write silently overwrites the first, making it as if the first transaction never happened.

Here is a concrete example. A bank account has a balance of $1,000. Transaction A reads the balance ($1,000) and adds $200, planning to write $1,200. Meanwhile, Transaction B also reads the balance ($1,000) and adds $300, planning to write $1,300. If A writes first ($1,200) and then B writes ($1,300), the final balance is $1,300 — Transaction A's $200 deposit has vanished. The correct final balance should be $1,500. Both transactions operated on stale data because neither knew about the other's in-progress modification. This is the "lost update": A's write is overwritten and its effect is permanently lost.

The lost update is dangerous precisely because each transaction in isolation behaves correctly. A reads the balance, adds $200, writes the new total — perfectly reasonable. B does the same with $300. The error only emerges from their interleaving, making it hard to detect through testing individual transactions. Importantly, the default isolation level in many databases (**READ COMMITTED**) does not prevent this problem. READ COMMITTED only guarantees you read committed data — it does not prevent two transactions from reading the same committed value and then both writing over it.

There are several ways to prevent lost updates. **Pessimistic locking** uses `SELECT ... FOR UPDATE` to lock the row when reading it, preventing any other transaction from reading or modifying it until the lock is released at COMMIT. This serializes access to the row and eliminates the race condition, but reduces concurrency. **Optimistic concurrency control** takes a different approach: allow both transactions to proceed, but detect the conflict at write time — typically by checking a version number or timestamp. If the row has changed since you read it, your write is rejected and you must retry. Some databases also offer **REPEATABLE READ** or **SERIALIZABLE** isolation levels that detect and abort conflicting concurrent modifications automatically. The right solution depends on how frequently conflicts occur — pessimistic locking is safer but slower; optimistic approaches allow more concurrency when conflicts are rare.
