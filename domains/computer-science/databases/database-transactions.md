---
id: database-transactions
title: Database Transactions
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
- id: file-system-concepts
  type: soft
builds-toward:
- acid-properties
- concurrency-control-databases
- write-ahead-logging
tags:
- transactions
- COMMIT
- ROLLBACK
- BEGIN
- atomicity
- savepoint
stage: formal-systems
status: validated
---

# Database Transactions

## Core Idea
A transaction is a sequence of database operations treated as a single logical unit of work that either completes entirely (COMMIT) or is entirely undone (ROLLBACK), leaving no partial state visible. Transactions protect data integrity when systems fail midway through multi-step operations, such as a bank transfer that must debit one account and credit another atomically. The BEGIN/COMMIT/ROLLBACK commands delimit transaction boundaries; savepoints allow partial rollback to a named point within a transaction without abandoning the entire unit.

## How It's Best Learned
Simulate a bank transfer in two SQL statements inside a transaction, then deliberately cause an error or rollback between them to observe atomicity. Practice setting savepoints and rolling back to them.

## Common Misconceptions
- Auto-commit mode (default in many SQL clients) wraps every statement in its own transaction — multi-statement logic requires an explicit BEGIN.
- ROLLBACK does not undo DDL statements (CREATE TABLE, DROP TABLE) in most databases — DDL is auto-committed.
- Long-running transactions hold locks and consume resources; transactions should be kept as short as possible.

## Questions

```yaml
- question: "A banking application runs two UPDATE statements to transfer money: first debiting Alice's account, then crediting Bob's. There is no explicit transaction — the database is in auto-commit mode. A server crash occurs between the two statements. What is the outcome?"
  type: multiple-choice
  options:
    - "Both statements are rolled back automatically because the operation was incomplete"
    - "Alice's account is debited but Bob's is never credited — the $100 is lost"
    - "The database retries both statements when the server restarts"
    - "The credit to Bob is applied when the server restarts, completing the transfer"
  answer: 1
  explanation: "In auto-commit mode, each statement is its own independent transaction. The first UPDATE (debit) committed immediately and is permanent. The second UPDATE (credit) never ran due to the crash and there is no transaction to roll back. The result is a partial state: money leaves Alice's account but never arrives in Bob's. This is precisely the problem transactions solve. Without an explicit BEGIN wrapping both statements, atomicity across multiple operations does not exist."

- question: "A developer wraps two UPDATE statements in a transaction with BEGIN, but the application crashes before the COMMIT is issued. What does the database do?"
  type: multiple-choice
  options:
    - "Commits the changes that completed successfully before the crash"
    - "Leaves the database in a partial state until the developer manually cleans it up"
    - "Automatically rolls back all changes made since BEGIN, restoring the original state"
    - "Commits the changes on the next successful connection to the database"
  answer: 2
  explanation: "Transaction atomicity guarantees that if anything goes wrong before COMMIT — a crash, a constraint violation, an application error — the database rolls back all changes made since BEGIN. This is the core promise: there is no partial state. The changes either fully complete and commit, or they are entirely undone. The 'all or nothing' guarantee is what makes multi-step database operations reliable in the presence of failures."

- question: "Issuing ROLLBACK inside a transaction undoes all changes made since the corresponding BEGIN."
  type: true-false
  answer: true
  explanation: "ROLLBACK discards all modifications made to the database since the transaction began with BEGIN, restoring the database to its state at that point. This is the complement of COMMIT, which makes changes permanent. The undo capability is what gives transactions their recovery power — if any step of a multi-statement operation fails, ROLLBACK returns the database to a known-good state, leaving no partial effects."

- question: "In most relational databases, a ROLLBACK issued inside a transaction will undo a CREATE TABLE or DROP TABLE statement that was executed within that transaction."
  type: true-false
  answer: false
  explanation: "Most databases (including PostgreSQL exceptions aside, and notably MySQL/Oracle) auto-commit DDL statements — CREATE TABLE, DROP TABLE, ALTER TABLE — immediately regardless of transaction boundaries. This means DDL cannot be rolled back by a subsequent ROLLBACK in most systems. PostgreSQL is an exception and does support transactional DDL. This is an important practical trap: if you run DROP TABLE inside what you think is a safe transaction, you may discover the DDL committed immediately and cannot be undone."

- question: "What specific problem does transaction atomicity solve, and what is the concrete consequence of running multi-step database operations without it?"
  type: short-answer
  answer: "Atomicity ensures that a sequence of database operations either all succeed and commit, or all fail and are rolled back — no partial state can exist. Without it, a failure midway through a multi-step operation (like a bank transfer) leaves the database in an inconsistent state: one change persists while the corresponding change does not, violating the real-world invariant the operations were meant to maintain."
  explanation: "The bank transfer example makes this concrete: subtract from Alice, add to Bob must be atomic — both happen or neither does. Without a transaction wrapping both, a crash between the two statements permanently corrupts the data. The database has no way to know the two operations were related. Transactions provide that relationship: the BEGIN announces 'these operations belong together,' and the atomicity guarantee enforces it."
```

## Explainer

You already know SQL statements like SELECT, INSERT, UPDATE, and DELETE for manipulating data. A **transaction** wraps one or more of these statements into a single all-or-nothing unit. The core promise is **atomicity**: either every statement in the transaction succeeds and the changes become permanent, or none of them take effect. There is no state where half the work is done and half is not. This guarantee is what makes databases reliable for operations that involve multiple coordinated changes.

Consider the classic example of a bank transfer: you need to subtract $100 from Alice's account and add $100 to Bob's account. Without transactions, a crash between the two statements could leave Alice debited and Bob uncredited — the $100 vanishes. With a transaction, you write `BEGIN`, then the two UPDATE statements, then `COMMIT`. If anything goes wrong before COMMIT — a power failure, a constraint violation, an application error — the database performs a **ROLLBACK**, undoing all changes made since BEGIN. The money either moves completely or stays exactly where it was.

The `BEGIN` command starts a new transaction. Every statement after BEGIN is part of that transaction until you explicitly issue `COMMIT` (to make changes permanent) or `ROLLBACK` (to discard them). A subtlety to watch for: most SQL clients operate in **auto-commit mode** by default, meaning every individual statement is implicitly wrapped in its own transaction and committed immediately. If you want multi-statement atomicity, you must explicitly write BEGIN. **Savepoints** add finer-grained control within a transaction. `SAVEPOINT x` marks a named point, and `ROLLBACK TO x` undoes everything back to that point without abandoning the entire transaction. This is useful when you want to attempt an operation and gracefully recover if it fails, without losing earlier work in the same transaction.

Transactions are not free — they consume resources while active. An open transaction may hold locks on rows or tables, preventing other transactions from reading or modifying those rows. Long-running transactions can therefore cause other users' queries to queue up and wait, degrading system performance. The practical rule is to keep transactions as short as possible: do your computation outside the transaction, open it, perform the minimal set of database operations, and commit immediately. This discipline — combined with proper error handling to ensure every BEGIN is matched by either a COMMIT or a ROLLBACK — is foundational to writing reliable database applications.
