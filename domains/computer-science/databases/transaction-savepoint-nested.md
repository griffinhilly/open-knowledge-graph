---
id: transaction-savepoint-nested
title: 'Savepoints: Partial Rollback Within Transactions'
domain: computer-science
course: databases
prerequisites:
- id: database-transactions
  type: hard
tags:
- transactions
- rollback
- error-handling
stage: formal-systems
status: validated
---

# Savepoints: Partial Rollback Within Transactions

## Core Idea
Savepoints mark points within a transaction to which a ROLLBACK can be selective, allowing recovery from errors without losing all work in the transaction.

## How It's Best Learned
Create a multi-statement transaction with savepoints and practice rolling back to different points.

## Common Misconceptions
Savepoints do not commit data—only COMMIT finalizes changes. Rolled-back statements after a savepoint can be re-executed with different values.

## Questions

```yaml
- question: "A transaction executes 10 INSERT statements, then sets a savepoint, then attempts an 11th INSERT that violates a constraint. The application issues ROLLBACK TO SAVEPOINT. What is the state of the database after this command?"
  type: multiple-choice
  options:
    - "The first 10 inserts are committed and the 11th is discarded"
    - "All 11 inserts are rolled back, returning to the state before the transaction began"
    - "The first 10 inserts are preserved within the transaction (still uncommitted), the 11th is undone"
    - "The 11th insert is retried automatically with the constraint relaxed"
  answer: 2
  explanation: "ROLLBACK TO SAVEPOINT undoes everything *after* the savepoint while preserving work done before it — but 'preserving' means it remains inside the open transaction, not committed. The first 10 inserts are intact and will be committed when the transaction issues COMMIT. Option A is the most common misconception: it conflates 'preserved by rollback-to-savepoint' with 'committed.' Nothing is persisted to disk until the final COMMIT; the savepoint only controls what portion of the transaction's in-progress work is undone."

- question: "A batch import transaction sets a savepoint before each of 100 record inserts. Records 1–50 succeed; record 51 fails a constraint, so the application rolls back to that record's savepoint and logs the error; records 52–100 succeed. The transaction then issues COMMIT. What happens?"
  type: multiple-choice
  options:
    - "Only records 52–100 are committed, because rolling back to a savepoint discards all prior work"
    - "Records 1–50 and 52–100 are committed; record 51's failed insert is not"
    - "Nothing is committed — the ROLLBACK TO SAVEPOINT invalidated the entire transaction"
    - "All 100 records are committed because savepoints do not affect COMMIT behavior"
  answer: 1
  explanation: "Savepoints enable exactly this pattern: fine-grained error recovery within a transaction. Rolling back to a savepoint only undoes the work done after that specific savepoint — records 1–50 remain intact in the transaction. After the rollback-to-savepoint and logging, the application continues processing records 52–100, all within the same transaction. The final COMMIT writes records 1–50 and 52–100. This is the key value proposition of savepoints: handle expected individual failures without sacrificing successfully processed records."

- question: "Rolling back to a savepoint commits most changes made before that savepoint, making them permanent in the database."
  type: true-false
  answer: false
  explanation: "This is the most dangerous misconception about savepoints. A savepoint is a recovery marker, not a commit point. ROLLBACK TO SAVEPOINT undoes work after the savepoint but leaves work before it in an uncommitted state within the still-open transaction. Only a COMMIT can write data permanently. If the entire transaction is later rolled back — or the connection drops before COMMIT — even the work 'preserved' by the savepoint is lost. Developers who mistake savepoints for mini-commits may believe their data is safely stored when it is actually still vulnerable."

- question: "After rolling back to a savepoint, the application can re-execute the failed operation with corrected values and continue the transaction normally."
  type: true-false
  answer: true
  explanation: "This is precisely what makes savepoints useful. After ROLLBACK TO SAVEPOINT, the transaction is still open at the state as of that savepoint. The application can examine the error, correct the input (different values, skip the record, log and continue), and then issue new SQL statements within the same transaction. The savepoint essentially lets you say 'try this risky operation; if it fails, undo it and take an alternative path, all without abandoning everything else.' This error-recovery loop within a single transaction is impossible without savepoints."

- question: "What is the fundamental difference between a savepoint and a COMMIT, and why does this distinction matter when designing bulk-processing transactions?"
  type: short-answer
  answer: "A COMMIT permanently writes all uncommitted changes to the database and ends the transaction. A savepoint creates a named marker inside a transaction that enables partial rollback — undoing work done after that point without touching work done before it — but commits nothing. The transaction remains open and all data remains uncommitted until COMMIT. For bulk processing, this means savepoints let you skip or log bad records without losing good ones, but the entire batch remains at risk until the final COMMIT. If the process crashes after setting savepoints but before COMMIT, all work is lost."
  explanation: "A common design mistake is to use savepoints assuming that passing a savepoint means the preceding work is 'safe.' It is safe from partial rollback, but not from a full transaction rollback, connection failure, or crash. If durability is required for each successfully processed record, you need intermediate COMMITs (separate transactions per record or per batch), not savepoints. Savepoints optimize for the case where you want to handle individual failures gracefully within a single atomic unit — they do not substitute for the durability guarantee that only COMMIT provides."
```

## Explainer

From your work with BEGIN, COMMIT, and ROLLBACK, you know that a transaction groups multiple operations into an atomic unit — either everything succeeds and is committed, or everything is rolled back as if nothing happened. But what if your transaction contains ten steps, step seven fails, and you want to undo just step seven while keeping the first six? Without savepoints, your only option is to roll back the entire transaction and start over. **Savepoints** solve this by letting you place named bookmarks inside a transaction that you can roll back to selectively.

The syntax is straightforward: after beginning a transaction, you create a savepoint with `SAVEPOINT my_checkpoint`. You continue executing statements, and if something goes wrong, you issue `ROLLBACK TO SAVEPOINT my_checkpoint`. This undoes everything *after* that savepoint while preserving everything before it. You can then continue the transaction from that point — retrying the failed operation with different values, skipping it entirely, or taking an alternative path. Think of it like saving your progress in a video game: if you die in a tough section, you reload from the last save rather than restarting the entire game.

You can create **multiple savepoints** within a single transaction, effectively nesting recovery points. Imagine a batch import that processes records one at a time: you set a savepoint before each record, attempt the insert, and if a particular record violates a constraint, you roll back to its savepoint and log the failure without losing the successfully imported records. This pattern is essential in applications that process data in bulk where individual failures are expected and acceptable.

The critical thing to remember is that savepoints do **not** commit anything. All the work inside the transaction — including everything before your savepoints — remains uncommitted until you issue a final COMMIT. A savepoint is not a mini-transaction; it is a recovery marker within the larger transaction. If you ROLLBACK the entire transaction (without specifying a savepoint), everything is undone regardless of how many savepoints you set. Savepoints give you *finer-grained error recovery* within the transactional model you already understand, without breaking the atomicity guarantee that transactions provide.
