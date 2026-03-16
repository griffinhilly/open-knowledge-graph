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
status: draft
---

# Lost Update Problem: Overwriting Concurrent Writes

## Core Idea
A lost update occurs when two transactions read the same row, modify it independently, and write back their versions in sequence—the first write is overwritten by the second.

## How It's Best Learned
Simulate two concurrent sessions reading a balance, incrementing it, and writing it back to observe the first increment disappearing.

## Common Misconceptions
Lost updates can occur even under READ COMMITTED isolation if explicit locking is not used. Row-level locks prevent this only if the lock is held until COMMIT.

## Explainer

You know from concurrency control that databases allow multiple transactions to execute simultaneously for performance, and that this concurrency creates the possibility of interference between transactions. The **lost update problem** is one of the most intuitive concurrency hazards: two transactions both read the same row, each computes a new value based on what it read, and both write back their results — but the second write silently overwrites the first, making it as if the first transaction never happened.

Here is a concrete example. A bank account has a balance of $1,000. Transaction A reads the balance ($1,000) and adds $200, planning to write $1,200. Meanwhile, Transaction B also reads the balance ($1,000) and adds $300, planning to write $1,300. If A writes first ($1,200) and then B writes ($1,300), the final balance is $1,300 — Transaction A's $200 deposit has vanished. The correct final balance should be $1,500. Both transactions operated on stale data because neither knew about the other's in-progress modification. This is the "lost update": A's write is overwritten and its effect is permanently lost.

The lost update is dangerous precisely because each transaction in isolation behaves correctly. A reads the balance, adds $200, writes the new total — perfectly reasonable. B does the same with $300. The error only emerges from their interleaving, making it hard to detect through testing individual transactions. Importantly, the default isolation level in many databases (**READ COMMITTED**) does not prevent this problem. READ COMMITTED only guarantees you read committed data — it does not prevent two transactions from reading the same committed value and then both writing over it.

There are several ways to prevent lost updates. **Pessimistic locking** uses `SELECT ... FOR UPDATE` to lock the row when reading it, preventing any other transaction from reading or modifying it until the lock is released at COMMIT. This serializes access to the row and eliminates the race condition, but reduces concurrency. **Optimistic concurrency control** takes a different approach: allow both transactions to proceed, but detect the conflict at write time — typically by checking a version number or timestamp. If the row has changed since you read it, your write is rejected and you must retry. Some databases also offer **REPEATABLE READ** or **SERIALIZABLE** isolation levels that detect and abort conflicting concurrent modifications automatically. The right solution depends on how frequently conflicts occur — pessimistic locking is safer but slower; optimistic approaches allow more concurrency when conflicts are rare.
