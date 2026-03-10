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
status: draft
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
