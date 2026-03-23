---
id: snapshot-isolation-write-skew
title: Snapshot Isolation and Write Skew Anomalies
domain: computer-science
course: databases
prerequisites:
- id: multiversion-concurrency-mvcc
  type: hard
- id: sql-isolation-levels-anomalies
  type: hard
tags:
- snapshot-isolation
- write-skew
- anomaly
- SI
- phantom
stage: formal-systems
status: validated
---

# Snapshot Isolation and Write Skew Anomalies

## Core Idea
Snapshot Isolation provides each transaction with a consistent database snapshot, preventing dirty, non-repeatable, and phantom reads. However, SI allows write skew anomalies where two transactions both read versions satisfying a constraint, make changes, and commit without noticing their combined effect violates the constraint (e.g., both doctors see the other on call, both go off). This anomaly cannot occur under SERIALIZABLE but is rare in practice.

## Questions

```yaml
- question: "Under snapshot isolation, two transactions T1 and T2 both run concurrently. T1 reads rows X and Y and writes row X; T2 reads rows X and Y and writes row Y. A constraint requires that X + Y > 0. Both T1 and T2 read X=5, Y=5 and each sets their respective row to -3. What happens?"
  type: multiple-choice
  options:
    - "Both commits succeed; the constraint X + Y > 0 is violated (write skew)"
    - "One transaction is aborted because both wrote to overlapping rows"
    - "Both transactions are aborted because SI detects the constraint violation"
    - "T1 succeeds and T2 is aborted because T2 started later"
  answer: 0
  explanation: "This is textbook write skew. T1 writes only row X and T2 writes only row Y — their *writes* do not overlap. SI's first-committer-wins rule only aborts a transaction if it writes to a row already modified by a committed concurrent transaction. Since the writes are to different rows, neither triggers the conflict detector. Both commit successfully, setting X=-3, Y=-3, which violates X + Y > 0. The constraint violation is invisible to SI because it emerges from the *combination* of writes that each appeared safe individually."

- question: "A developer wants to prevent write skew in a snapshot-isolated database without upgrading to SERIALIZABLE. What technique can they use at the application level?"
  type: multiple-choice
  options:
    - "Use INSERT ... ON CONFLICT to deduplicate writes"
    - "Wrap all reads in SELECT FOR UPDATE to acquire write locks on read rows"
    - "Use ROLLBACK SAVEPOINT after each read to create checkpoints"
    - "Set the transaction isolation level to READ COMMITTED for the affected transactions"
  answer: 1
  explanation: "SELECT FOR UPDATE acquires a write lock on the rows read, even though you're not yet writing them. This converts the read dependency into a write conflict that SI's first-committer-wins rule *can* detect. If T1 and T2 both SELECT FOR UPDATE on the rows they read, whichever transaction commits second will find those rows locked by the first, and will be aborted. The other options do not address the root cause: ON CONFLICT handles duplicate inserts (not read-write cycles), SAVEPOINT doesn't prevent concurrent commits, and READ COMMITTED offers weaker — not stronger — isolation."

- question: "Snapshot isolation's first-committer-wins rule prevents write skew anomalies."
  type: true-false
  answer: false
  explanation: "First-committer-wins prevents *lost updates* — the case where two transactions both write to the *same* row and the second silently overwrites the first's change. Write skew is different: the two transactions write to *different* rows, so no write-write conflict is detected. The anomaly arises because each transaction's individual write is safe, but their combined effect violates a constraint that both read simultaneously. First-committer-wins doesn't fire because the writes don't overlap. Preventing write skew requires either SERIALIZABLE isolation or explicit locking (SELECT FOR UPDATE)."

- question: "Write skew can occur even when two concurrent transactions never write to the same database row."
  type: true-false
  answer: true
  explanation: "This is the defining characteristic of write skew — it occurs precisely because the conflicting writes are to *different* rows. Both transactions read an overlapping set of rows, each makes a decision based on what it sees, and each writes to a distinct row. The violation emerges only when both writes are combined. The on-call doctor example illustrates this: Doctor A updates her own row, Doctor B updates his own row, and neither write conflicts with the other — yet together they leave zero doctors on call, violating the invariant."

- question: "Why does snapshot isolation fail to prevent write skew, even though it prevents lost updates, non-repeatable reads, and phantom reads?"
  type: short-answer
  answer: "SI prevents anomalies that arise from a transaction observing *another transaction's writes* (dirty reads, non-repeatable reads, phantoms) and prevents *same-row* write-write conflicts via first-committer-wins. Write skew, however, involves a *read-write dependency across different rows*: each transaction's read set overlaps with the other's write set, but not vice versa. SI has no mechanism to detect this 'anti-dependency' cycle. Each transaction sees a consistent snapshot, each write appears locally valid, and the conflict is only visible when both committed states are combined — which SI never checks."
  explanation: "The core issue is that SI tracks which rows transactions *write* (to enforce first-committer-wins) but does not track which rows transactions *read*. The serialization anomaly in write skew requires detecting that T1's write to row X conflicts with T2's read of row X (and vice versa). Serializable Snapshot Isolation (SSI), as implemented in PostgreSQL, adds this read tracking to detect and abort transactions involved in such cycles."
```

## Explainer

You already understand how MVCC works — each transaction sees a consistent snapshot of the database as of its start time, reading committed versions without blocking other writers. And you know that isolation levels define which anomalies a system permits. **Snapshot isolation** (SI) sits between REPEATABLE READ and SERIALIZABLE in strength: it prevents dirty reads, non-repeatable reads, and even phantom reads, because every read within the transaction returns data from the same fixed snapshot. Two concurrent transactions can both read and write without blocking each other, which makes SI attractive for performance.

The catch is **write skew**, an anomaly unique to snapshot isolation. Write skew occurs when two transactions each read an overlapping set of rows, make decisions based on what they read, and write to different rows — but their combined writes violate a constraint that held when each transaction read. The classic example involves two on-call doctors. A hospital rule says at least one doctor must remain on call. Doctor A and Doctor B both check the schedule at the same time, both see the other is on call, and both submit a request to go off call. Under snapshot isolation, each transaction sees the other doctor still on call (because neither has committed yet), so each concludes the constraint is satisfied. Both commit successfully, and now zero doctors are on call — violating the invariant.

The key insight is that write skew cannot happen if both transactions write to the same row. SI uses a **first-committer-wins** rule: if two transactions modify the same row, the second one to commit is aborted. This prevents lost updates. But write skew involves writing to *different* rows (Doctor A updates her own row, Doctor B updates his), so the conflict detection never fires. The transactions' writes do not overlap, even though their reads do, and the constraint violation emerges only from the combination.

Defending against write skew requires either upgrading to true SERIALIZABLE isolation (which detects these dependency cycles and aborts one transaction) or using application-level locking. A common workaround is to use SELECT FOR UPDATE on the rows you read, which forces a write lock even though you are only reading — effectively converting the read dependency into a write conflict that SI can detect. Some systems, like PostgreSQL's Serializable Snapshot Isolation (SSI), extend SI with dependency tracking to automatically detect and prevent write skew without requiring explicit locks.
