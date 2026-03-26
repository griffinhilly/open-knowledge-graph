---
id: two-phase-locking
title: Two-Phase Locking
domain: computer-science
course: databases
prerequisites:
- id: concurrency-control-databases
  type: hard
- id: mutual-exclusion-and-locks
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

## Questions

```yaml
- question: "Transaction T1 holds an exclusive lock on row A and requests a lock on row B. Transaction T2 holds an exclusive lock on row B and requests a lock on row A. Under 2PL, what happens?"
  type: multiple-choice
  options:
    - "2PL automatically detects the circular wait and aborts the lower-priority transaction"
    - "Both transactions block indefinitely — a deadlock that 2PL itself does not resolve"
    - "2PL prevents this scenario by requiring transactions to acquire all locks before starting"
    - "T1 is forced to release its lock on A to make progress, then reacquire it later"
  answer: 1
  explanation: "2PL guarantees serializability, not deadlock-freedom. In this scenario, T1 waits for B while holding A, and T2 waits for A while holding B — a classic circular wait. Neither can proceed without the other releasing, so they block indefinitely. Deadlock resolution (detection via wait-for graphs, or prevention via timestamp ordering) is handled by a separate mechanism, not by the 2PL protocol itself. Option C describes a different protocol (predeclaring all locks) that 2PL does not require."

- question: "A transaction using 2PL acquires a shared lock on row X, reads the data, then releases the shared lock on row X. Later in the same transaction, it needs to acquire a shared lock on row Y. Why does this violate 2PL?"
  type: multiple-choice
  options:
    - "Shared locks cannot be released before exclusive locks in any 2PL implementation"
    - "Releasing the lock on X starts the shrinking phase, so no new lock — including on Y — can be acquired"
    - "Row-level locking in 2PL requires all locks to be acquired before any data is read"
    - "Shared locks on different rows are mutually exclusive and cannot both be held"
  answer: 1
  explanation: "2PL's core rule is: once any lock is released, the transaction enters the shrinking phase and may not acquire any further locks. Releasing the lock on X, even though X is done with, immediately ends the growing phase. Attempting to acquire a new lock on Y afterward violates the protocol and can produce non-serializable schedules. This is also why Strict 2PL holds all locks until commit — not just to avoid cascading aborts, but to prevent transactions from accidentally entering the shrinking phase too early."

- question: "Under Strict 2PL, holding all locks until commit or abort prevents cascading aborts."
  type: true-false
  answer: true
  explanation: "True. Basic 2PL allows releasing locks before commit (during the shrinking phase), which creates a risk: if T1 releases a lock and T2 reads the now-unlocked data, then T1 aborts, T2 has read data that was never committed. T2 must also abort — and if T3 read T2's data, T3 must abort too. Strict 2PL prevents this by ensuring that no transaction can read data from T1 until T1 has committed, since T1 holds its locks until then."

- question: "Two-Phase Locking guarantees that deadlocks will seldom occur between transactions in a correctly implemented database."
  type: true-false
  answer: false
  explanation: "False. 2PL guarantees serializability — that the concurrent execution is equivalent to some serial ordering — but says nothing about deadlocks. Deadlocks are a separate phenomenon caused by circular lock-wait dependencies, which can happen under any locking protocol. Databases handle deadlocks through separate mechanisms: deadlock detection (checking for cycles in the wait-for graph and aborting a victim) or deadlock prevention (using timestamps to impose a global ordering on lock acquisition)."

- question: "Why does the 2PL rule — never acquire a lock after releasing one — guarantee serializability?"
  type: short-answer
  answer: "If a transaction releases a lock and then acquires a new one, another transaction could slip in between: reading the just-released data and producing an interleaving with no equivalent serial ordering. The 2PL rule prevents this by ensuring that each transaction's lock-acquisition window is contiguous and closed. The growing phase establishes a consistent 'claim' on all relevant data; the shrinking phase releases those claims. Because no transaction can acquire a new claim after beginning to release, the partial ordering of transactions induced by their lock conflicts is always acyclic — which is equivalent to the existence of a serializable ordering."
  explanation: "More precisely, 2PL ensures that the lock points (the moment a transaction transitions from growing to shrinking) can be used to construct a serial order that the concurrent schedule is equivalent to. This proof relies on the fact that if T1's lock point precedes T2's, then T1 holds all its locks when T2's shrinking phase begins, preventing any interleaving that would violate the T1-before-T2 order."
```

## Explainer

From your study of concurrency control, you know the core problem: multiple transactions running simultaneously can interfere with each other, producing results that no serial (one-at-a-time) execution would produce. The gold standard for correctness is **serializability** — the guarantee that the concurrent execution is equivalent to *some* serial ordering of the same transactions. Two-Phase Locking is the most widely used protocol for achieving this guarantee, and its elegance lies in a single, simple rule about when locks can be acquired and released.

The protocol divides each transaction's lifetime into two phases. During the **growing phase**, the transaction acquires whatever locks it needs — shared locks for reading, exclusive locks for writing — but may not release any lock it holds. During the **shrinking phase**, the transaction may release locks but may not acquire any new ones. That's it. This one constraint — never acquire after releasing — is sufficient to guarantee serializability. The intuition is that if a transaction releases a lock and then tries to acquire another, a different transaction could slip in between, creating an interleaving that has no serial equivalent. By forbidding this pattern, 2PL ensures that all transactions' lock acquisitions form a consistent ordering.

In practice, most databases use **Strict 2PL**, which strengthens the protocol by holding all locks until the transaction commits or aborts. Basic 2PL allows releasing locks during the shrinking phase before commit, but this creates a problem: if transaction T1 releases a lock, T2 reads the unlocked data, and then T1 aborts, T2 has read data that was never actually committed. T2 must now also abort — a **cascading abort** that can ripple through many transactions. Strict 2PL eliminates this entirely by keeping locks held until commit, at the cost of holding resources longer. This is why you sometimes see transactions blocking while waiting for another transaction to finish.

The major limitation of 2PL is **deadlock**. If transaction T1 holds a lock on row A and waits for a lock on row B, while T2 holds B and waits for A, neither can proceed. 2PL guarantees serializability but says nothing about deadlock. Databases handle this with separate mechanisms: **deadlock detection** (periodically checking for cycles in the wait-for graph and aborting one transaction to break the cycle) or **deadlock prevention** (using transaction timestamps to decide who waits and who aborts). Understanding that serializability and deadlock-freedom are orthogonal concerns — and that 2PL solves only the first — is essential for reasoning about concurrent database behavior.
