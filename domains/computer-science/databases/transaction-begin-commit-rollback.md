---
id: transaction-begin-commit-rollback
title: 'Transaction Control: BEGIN, COMMIT, ROLLBACK'
domain: computer-science
course: databases
prerequisites:
- id: database-transactions
  type: hard
builds-toward:
- transaction-savepoint-nested
- isolation-level-read-uncommitted
tags:
- transactions
- acid
- dml-control
stage: formal-systems
status: validated
---

# Transaction Control: BEGIN, COMMIT, ROLLBACK

## Core Idea
BEGIN starts a transaction, COMMIT finalizes changes, and ROLLBACK discards them. Together they provide explicit control over atomicity—either all changes succeed or none do.

## How It's Best Learned
Practice rolling back a DELETE in response to an error check, and verify that uncommitted changes are invisible to other sessions.

## Common Misconceptions
Uncommitted changes are visible only to the current session by default. Autocommit behavior (automatic COMMIT after each statement) varies by database and driver.

## Questions

```yaml
- question: "A developer runs UPDATE accounts SET balance = 0 WHERE id = 5 outside of an explicit BEGIN block. Immediately after, they realize this was a mistake. Can they issue ROLLBACK to undo it?"
  type: multiple-choice
  options:
    - "Yes — ROLLBACK always undoes the most recent statement"
    - "No — in autocommit mode, the UPDATE committed immediately and cannot be rolled back"
    - "Yes — databases keep a 24-hour undo log for all statements"
    - "Only if the UPDATE violated a constraint and the database rejected it"
  answer: 1
  explanation: "Outside an explicit BEGIN block, most databases operate in autocommit mode: each statement is its own transaction and commits immediately upon success. Once auto-committed, there is no ROLLBACK available — the change is durable and permanent. This is why working with critical data always requires explicit BEGIN/COMMIT boundaries, which give you a reversibility window before changes become permanent."

- question: "A bank transfer is wrapped in a single transaction: BEGIN; debit account A; credit account B; COMMIT. The credit operation fails due to a constraint violation. What happens?"
  type: multiple-choice
  options:
    - "The debit commits but the credit is lost — partial success is recorded"
    - "Both the debit and credit are rolled back, leaving the database exactly as before BEGIN"
    - "The database automatically retries the credit until it succeeds"
    - "The database enters a locked state pending administrator resolution"
  answer: 1
  explanation: "This is atomicity in action: a transaction either commits entirely or not at all. If any statement within the transaction fails (or if ROLLBACK is issued), all changes since BEGIN are discarded. The debit is not kept just because it succeeded — it exists in limbo until COMMIT. This all-or-nothing guarantee is exactly why the bank transfer pattern requires explicit transaction control."

- question: "Uncommitted changes made after BEGIN are visible to other database sessions, allowing them to read the latest in-progress data."
  type: true-false
  answer: false
  explanation: "Under default isolation levels, uncommitted changes are only visible to the session that made them. Other sessions see a consistent snapshot that excludes in-progress work. If other sessions could see uncommitted data, they might read values that get rolled back — this is called a 'dirty read' and is considered an isolation violation. Transaction isolation ensures that incomplete work stays invisible to the rest of the database until COMMIT makes it permanent."

- question: "ROLLBACK after an error within an explicit transaction undoes all changes since BEGIN, not just the single failing statement."
  type: true-false
  answer: true
  explanation: "ROLLBACK is not statement-scoped — it rolls back the entire transaction. All changes since the most recent BEGIN are discarded as a unit. If you want partial rollback (undo up to a specific point but keep earlier changes), you must use SAVEPOINTs to mark intermediate states. Without SAVEPOINTs, atomicity is all-or-nothing: either everything since BEGIN commits, or everything since BEGIN rolls back."

- question: "Explain why autocommit mode is a practical danger when working with critical data, and what the safer alternative is."
  type: short-answer
  answer: "In autocommit mode, every SQL statement becomes its own transaction and commits immediately upon success. This eliminates any window to review the effect and issue ROLLBACK if something is wrong. A mistaken DELETE or UPDATE cannot be undone — the change is durable the moment it completes. The safe alternative is explicit transaction control: issue BEGIN before any critical operations, perform the changes, inspect the result within the session (queries within the transaction see the uncommitted changes), and then COMMIT if everything looks correct — or ROLLBACK if anything is wrong. Explicit boundaries restore the reversibility that autocommit removes."
  explanation: "The danger is asymmetric: with autocommit, the cost of a mistake is permanent data loss; with explicit transactions, the cost of being overly cautious is just a few extra keystrokes. For this reason, professional database work almost always uses explicit BEGIN/COMMIT for any multi-statement operation involving writes."
```

## Explainer

You already understand that a database transaction is a logical unit of work that must either complete entirely or not at all — the atomicity guarantee from ACID. The three commands **BEGIN**, **COMMIT**, and **ROLLBACK** are how you exercise explicit control over that boundary. Without them, most database drivers operate in **autocommit mode**, where every individual SQL statement is its own transaction — it commits immediately upon completion. Explicit transaction control lets you group multiple statements into a single atomic unit.

The pattern is straightforward: `BEGIN` (or `START TRANSACTION` in some systems) opens a new transaction. Every subsequent INSERT, UPDATE, or DELETE is tentatively applied but not yet permanent. The changes exist in a kind of limbo — visible to your session but invisible to other connections. When you issue `COMMIT`, all changes since BEGIN are made durable and visible to everyone. If something goes wrong — a constraint violation, a business logic check that fails, or simply a mistake — `ROLLBACK` discards every change since BEGIN, leaving the database exactly as it was before the transaction started.

Consider a bank transfer: you need to debit one account and credit another. Without explicit transaction control, the debit might succeed but the credit might fail (due to a crash, constraint error, or network issue), leaving money missing from one account and not yet in the other. Wrapping both operations in a single transaction ensures atomicity: `BEGIN; UPDATE accounts SET balance = balance - 100 WHERE id = 1; UPDATE accounts SET balance = balance + 100 WHERE id = 2; COMMIT;`. If the second UPDATE fails, you call ROLLBACK and the first UPDATE is also undone. Neither change persists unless both succeed.

A practical subtlety is autocommit behavior. In PostgreSQL, each statement outside an explicit BEGIN block auto-commits. In MySQL with InnoDB, the same applies by default. Many application frameworks and database drivers also manage autocommit settings, sometimes turning it off by default and requiring explicit commits. If you run a DELETE and are puzzled that the rows are already gone before you typed COMMIT, autocommit is likely on. When working with critical data, always use explicit BEGIN/COMMIT boundaries so that you have a chance to ROLLBACK if something unexpected happens — once a statement auto-commits, there is no undoing it.
