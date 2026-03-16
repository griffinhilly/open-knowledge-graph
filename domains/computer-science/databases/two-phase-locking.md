---
id: two-phase-locking
title: Two-Phase Locking
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
- id: mutex-and-locks
  type: soft
- id: semaphores
  type: soft
builds-toward:
- database-deadlocks
tags:
- two-phase locking
- 2PL
- shared lock
- exclusive lock
- serializability
- strict 2PL
stage: formal-systems
status: validated
---

# Two-Phase Locking

## Core Idea
Two-Phase Locking (2PL) is a concurrency control protocol that guarantees serializability: in the growing phase, a transaction may acquire locks but not release any; in the shrinking phase, it may release locks but not acquire new ones. Shared (read) locks allow concurrent reading; exclusive (write) locks block all other access. Strict 2PL (the common variant) holds all locks until commit, preventing cascading aborts where one transaction's rollback forces others to roll back. 2PL is provably correct for serializability but does not prevent deadlocks.

## How It's Best Learned
Draw lock timelines for two concurrent transactions and determine whether their interleaving is serializable under 2PL. Work through examples that would deadlock and contrast with timestamp-based or optimistic approaches.

## Common Misconceptions
- 2PL guarantees serializability but not deadlock-freedom — deadlock detection or prevention must be handled separately.
- Releasing a lock before commit (violating the shrinking phase rule) can produce non-serializable schedules.
- Row-level locking vs. table-level locking is an implementation detail orthogonal to the 2PL protocol itself.

## Explainer

From your study of concurrency control, you know the core problem: multiple transactions running simultaneously can interfere with each other, producing results that no serial (one-at-a-time) execution would produce. The gold standard for correctness is **serializability** — the guarantee that the concurrent execution is equivalent to *some* serial ordering of the same transactions. Two-Phase Locking is the most widely used protocol for achieving this guarantee, and its elegance lies in a single, simple rule about when locks can be acquired and released.

The protocol divides each transaction's lifetime into two phases. During the **growing phase**, the transaction acquires whatever locks it needs — shared locks for reading, exclusive locks for writing — but may not release any lock it holds. During the **shrinking phase**, the transaction may release locks but may not acquire any new ones. That's it. This one constraint — never acquire after releasing — is sufficient to guarantee serializability. The intuition is that if a transaction releases a lock and then tries to acquire another, a different transaction could slip in between, creating an interleaving that has no serial equivalent. By forbidding this pattern, 2PL ensures that all transactions' lock acquisitions form a consistent ordering.

In practice, most databases use **Strict 2PL**, which strengthens the protocol by holding all locks until the transaction commits or aborts. Basic 2PL allows releasing locks during the shrinking phase before commit, but this creates a problem: if transaction T1 releases a lock, T2 reads the unlocked data, and then T1 aborts, T2 has read data that was never actually committed. T2 must now also abort — a **cascading abort** that can ripple through many transactions. Strict 2PL eliminates this entirely by keeping locks held until commit, at the cost of holding resources longer. This is why you sometimes see transactions blocking while waiting for another transaction to finish.

The major limitation of 2PL is **deadlock**. If transaction T1 holds a lock on row A and waits for a lock on row B, while T2 holds B and waits for A, neither can proceed. 2PL guarantees serializability but says nothing about deadlock. Databases handle this with separate mechanisms: **deadlock detection** (periodically checking for cycles in the wait-for graph and aborting one transaction to break the cycle) or **deadlock prevention** (using transaction timestamps to decide who waits and who aborts). Understanding that serializability and deadlock-freedom are orthogonal concerns — and that 2PL solves only the first — is essential for reasoning about concurrent database behavior.
