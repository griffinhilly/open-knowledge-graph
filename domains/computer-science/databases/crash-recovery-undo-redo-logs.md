---
id: crash-recovery-undo-redo-logs
title: 'Crash Recovery: Undo and Redo Logging'
domain: computer-science
course: databases
prerequisites:
- id: write-ahead-logging-protocol-durability
  type: hard
- id: transaction-properties-acid
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
status: draft
---

# Crash Recovery: Undo and Redo Logging

## Core Idea
Recovery algorithms use undo and redo logs to restore consistency after crashes. Undo logging records old values for backwards roll of uncommitted transactions; redo logging records new values for forwards replay of committed transactions. ARIES (Algorithm for Recovery and Isolation Exploiting Semantics) combines both: it redoes committed work, then undoes incomplete transactions. This approach minimizes recovery time and avoids re-executing long transactions.

## Explainer

You already know from write-ahead logging that every change must be recorded in a log before it reaches the database on disk. The reason is simple: crashes can happen at any moment — between writing one page and the next, between logging a change and applying it, even mid-commit. The database must be able to reconstruct a consistent state from whatever survived on disk. The question is: what exactly should the log record, and how does recovery use those records?

**Undo logging** records the old value before each modification. If a transaction writes attribute A from value 5 to value 8, the undo log entry says "A was 5." The rule is that the actual database page must be written to disk before the transaction commits. If the system crashes before commit, recovery scans the log backward and restores every modified value to its old state — rolling back incomplete work. The advantage is straightforward recovery; the disadvantage is that every dirty page must be forced to disk before commit, which can be slow for transactions that touch many pages.

**Redo logging** takes the opposite approach: it records the new value. The undo log entry for the same operation would say "A becomes 8." Here the rule is reversed — the database pages must not be written to disk until after the transaction commits and the commit record is in the log. If the system crashes after commit but before pages were written, recovery replays the log forward, applying the new values. If the crash happens before commit, there is nothing to redo because the pages were never modified on disk. Redo logging allows lazy page writes (buffering changes in memory), but it means uncommitted changes never reach disk, which can limit buffer management flexibility.

**ARIES** (Algorithm for Recovery and Isolation Exploiting Semantics), used by most production databases, combines both strategies into **undo/redo logging**. Each log entry records both the old and new value. Pages can be flushed to disk at any time — before or after commit — giving the buffer manager maximum flexibility. Recovery proceeds in three phases: an **analysis pass** scans the log to determine which transactions were active at crash time and which pages might be dirty; a **redo pass** replays all logged changes from the most recent checkpoint forward to restore the database to its exact pre-crash state (including uncommitted changes that had been flushed); and an **undo pass** rolls back any transaction that was still active at crash time by applying the old values in reverse order. This "redo everything, then undo losers" approach is elegant because it separates two concerns: first bring the physical state up to date, then enforce transactional consistency on top of it.
