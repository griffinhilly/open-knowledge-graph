---
id: crash-recovery-undo-redo-logs
title: 'Crash Recovery: Undo and Redo Logging'
domain: computer-science
course: databases
prerequisites:
- id: write-ahead-logging
  type: hard
- id: acid-properties
  type: hard
builds-toward:
- checkpoint-fuzzy-recovery
tags:
- recovery
- undo
- redo
- ARIES
- crash
stage: formal-systems
status: validated
---

# Crash Recovery: Undo and Redo Logging

## Core Idea
Recovery algorithms use undo and redo logs to restore consistency after crashes. Undo logging records old values for backwards roll of uncommitted transactions; redo logging records new values for forwards replay of committed transactions. ARIES (Algorithm for Recovery and Isolation Exploiting Semantics) combines both: it redoes committed work, then undoes incomplete transactions. This approach minimizes recovery time and avoids re-executing long transactions.

## Questions

```yaml
- question: "A transaction uses REDO logging to change page A from value 5 to value 8. The system writes the commit record to the log, but crashes before flushing page A to disk. What happens during recovery?"
  type: multiple-choice
  options:
    - "Recovery rolls back the transaction because the page was never written to disk before the crash"
    - "Recovery replays the redo log entry forward, writing value 8 to page A to restore the committed state"
    - "Recovery scans backward and restores A to value 5 using the old value stored in the log"
    - "Recovery cannot restore this transaction because the page was not on disk at crash time"
  answer: 1
  explanation: "Redo logging records the *new* value (8). Recovery's job after a commit is to replay the log forward, applying all new values to bring the database up to the committed state — regardless of whether the pages were on disk at crash time. This is the defining rule of redo logging: pages may not be written to disk until after commit, so recovery knows that any committed transaction needs its changes applied. Option C describes undo logging (old values, backward scan), which is the opposite approach."

- question: "During ARIES recovery after a crash, the analysis pass identifies two transactions: T1 (committed, with some dirty pages flushed to disk) and T2 (uncommitted, also with dirty pages flushed). In the redo pass, which logged changes are replayed?"
  type: multiple-choice
  options:
    - "Only T1's changes — T2 was uncommitted and should never be redone"
    - "Only T2's changes — T2's pages on disk are wrong and must be overwritten first"
    - "Both T1's and T2's logged changes are redone to restore the exact pre-crash disk state; then the undo pass rolls back T2"
    - "Neither — ARIES always starts recovery from a clean checkpoint and redoes nothing before the checkpoint"
  answer: 2
  explanation: "ARIES's key insight is to separate physical and transactional recovery into two phases. The redo pass brings the database to the exact state it was in at the moment of crash — including uncommitted changes that had been flushed to disk. Only after this physical restoration does the undo pass enforce transactional consistency by rolling back uncommitted transactions. Skipping T2 in the redo pass would leave the disk in a mixed state that makes the undo pass impossible to execute correctly. 'Redo everything, then undo losers' is the phrase to remember."

- question: "Undo logging requires all dirty pages to be written to disk *before* a transaction commits, while redo logging requires that dirty pages *not* be written to disk until after the commit record is in the log."
  type: true-false
  answer: true
  explanation: "This is the defining constraint of each approach. Undo logging must write pages before commit because recovery scans backward and needs the old values to be superseded by what's actually on disk — if the crash happened before commit, rollback restores old values. Redo logging must hold pages until after commit because recovery replays the log forward — if the crash happened before commit, no committed state exists to replay, so no rollback is needed. The two rules are exact opposites, reflecting the opposite directions of recovery."

- question: "In ARIES, the redo pass only replays changes from committed transactions, since replaying uncommitted changes would violate transaction isolation."
  type: true-false
  answer: false
  explanation: "This is the most common misconception about ARIES. The redo pass replays ALL logged changes — committed and uncommitted — to bring the physical disk state to exactly what it was at the moment of the crash. ARIES's buffer manager may flush uncommitted dirty pages to disk at any time, so after a crash the disk may contain a mix of committed and uncommitted work. The redo pass restores this exact state; the undo pass then cleanly rolls back uncommitted transactions. Isolation is enforced by the undo pass, not by filtering the redo pass."

- question: "Why does ARIES redo *all* changes — including those from uncommitted transactions — before undoing anything, rather than simply replaying only committed work and skipping uncommitted changes?"
  type: short-answer
  answer: "Because ARIES allows the buffer manager to flush dirty pages to disk at any time — before or after commit. After a crash, the disk may contain partial writes from uncommitted transactions that were flushed. The redo pass must replay all logged changes to bring the disk to the exact pre-crash state, because only from that exact state can the undo pass cleanly reverse uncommitted work. If the redo pass skipped uncommitted changes, the disk would be in a mixed, inconsistent state where the undo pass could not determine what was actually written and what was not."
  explanation: "The elegance of ARIES is that it separates two concerns: 'make the physical state consistent with the log' (redo everything) and 'enforce transactional atomicity' (undo uncommitted work). Conflating these — trying to filter the redo pass for committed-only changes — would require the recovery algorithm to know which pages correspond to which transactions before it has restored the log state, creating a circular dependency."
```

## Explainer

You already know from write-ahead logging that every change must be recorded in a log before it reaches the database on disk. The reason is simple: crashes can happen at any moment — between writing one page and the next, between logging a change and applying it, even mid-commit. The database must be able to reconstruct a consistent state from whatever survived on disk. The question is: what exactly should the log record, and how does recovery use those records?

**Undo logging** records the old value before each modification. If a transaction writes attribute A from value 5 to value 8, the undo log entry says "A was 5." The rule is that the actual database page must be written to disk before the transaction commits. If the system crashes before commit, recovery scans the log backward and restores every modified value to its old state — rolling back incomplete work. The advantage is straightforward recovery; the disadvantage is that every dirty page must be forced to disk before commit, which can be slow for transactions that touch many pages.

**Redo logging** takes the opposite approach: it records the new value. The undo log entry for the same operation would say "A becomes 8." Here the rule is reversed — the database pages must not be written to disk until after the transaction commits and the commit record is in the log. If the system crashes after commit but before pages were written, recovery replays the log forward, applying the new values. If the crash happens before commit, there is nothing to redo because the pages were never modified on disk. Redo logging allows lazy page writes (buffering changes in memory), but it means uncommitted changes never reach disk, which can limit buffer management flexibility.

**ARIES** (Algorithm for Recovery and Isolation Exploiting Semantics), used by most production databases, combines both strategies into **undo/redo logging**. Each log entry records both the old and new value. Pages can be flushed to disk at any time — before or after commit — giving the buffer manager maximum flexibility. Recovery proceeds in three phases: an **analysis pass** scans the log to determine which transactions were active at crash time and which pages might be dirty; a **redo pass** replays all logged changes from the most recent checkpoint forward to restore the database to its exact pre-crash state (including uncommitted changes that had been flushed); and an **undo pass** rolls back any transaction that was still active at crash time by applying the old values in reverse order. This "redo everything, then undo losers" approach is elegant because it separates two concerns: first bring the physical state up to date, then enforce transactional consistency on top of it.
