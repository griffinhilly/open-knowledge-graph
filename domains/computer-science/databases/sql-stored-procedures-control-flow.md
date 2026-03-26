---
id: sql-stored-procedures-control-flow
title: 'Stored Procedures: Procedural Logic and Transaction Control'
domain: computer-science
course: databases
prerequisites:
- id: sql-data-retrieval-select
  type: hard
- id: database-transactions
  type: hard
builds-toward:
- sql-triggers-before-after-events
- acid-properties
tags:
- stored-procedures
- procedural
- BEGIN-COMMIT-ROLLBACK
stage: formal-systems
status: validated
---

# Stored Procedures: Procedural Logic and Transaction Control

## Core Idea
Stored procedures are SQL programs stored in the database that encapsulate business logic and enforce consistent behavior across applications. They support control flow (IF/ELSE, loops), variables, and error handling. Transaction control statements (BEGIN, COMMIT, ROLLBACK, SAVEPOINT) manage transaction boundaries, grouping multiple statements into atomic units that succeed completely or fail together.

## Questions

```yaml
- question: "A bank has a web app, a mobile app, and an internal admin tool — all of which need to transfer funds between accounts. What is the strongest argument for implementing the transfer logic as a stored procedure rather than in each application?"
  type: multiple-choice
  options:
    - "Stored procedures execute faster because they run closer to the data"
    - "Stored procedures guarantee that every transfer enforces the same rules regardless of which application calls the database"
    - "Stored procedures prevent SQL injection attacks more reliably than application code"
    - "Stored procedures automatically partition the workload across database servers"
  answer: 1
  explanation: "The core benefit of centralizing logic in a stored procedure is consistency and enforcement. If the transfer logic lives in each application, one app might have a bug, a different version, or be bypassed by someone running SQL directly. A stored procedure enforces the business rules at the database level — the single point of truth — regardless of who or what calls it. Performance is a secondary benefit; the enforcement guarantee is the primary justification."

- question: "Inside a stored procedure for a fund transfer, after debiting Account A, you set a SAVEPOINT. Then the credit to Account B fails. You execute ROLLBACK TO SAVEPOINT. What is the state of the transaction?"
  type: multiple-choice
  options:
    - "The entire transaction is rolled back — Account A's debit is also reversed"
    - "Only the failed credit attempt is rolled back; Account A's debit remains"
    - "The transaction is committed up to the savepoint — Account A's debit is permanent"
    - "SAVEPOINT has no effect when a statement fails; only full ROLLBACK works"
  answer: 1
  explanation: "ROLLBACK TO SAVEPOINT undoes all work done since the savepoint was set, but leaves work done before the savepoint intact within the transaction. The debit (done before the savepoint) is still pending; the failed credit (done after) is undone. Crucially, 'intact within the transaction' does not mean committed — the transaction is still open, and the debit has not been written permanently. A subsequent COMMIT or full ROLLBACK will determine the final state."

- question: "A stored procedure that wraps a fund transfer in BEGIN/COMMIT/ROLLBACK ensures that either both the debit and credit happen or neither happens."
  type: true-false
  answer: true
  explanation: "This is the atomicity guarantee of transaction control. BEGIN marks the start of the transaction; COMMIT makes all changes permanent only if every step succeeds; ROLLBACK undoes all changes if any step fails. By wrapping both operations in the same transaction boundary, the stored procedure ensures they are treated as a single atomic unit — the 'all or nothing' property of ACID transactions. Without this wrapper, a failure between debit and credit would leave the accounts in an inconsistent state."

- question: "Rolling back a transaction to a SAVEPOINT permanently commits most of the work done before the savepoint."
  type: true-false
  answer: false
  explanation: "ROLLBACK TO SAVEPOINT undoes work done after the savepoint but does not commit anything. The transaction is still open; work done before the savepoint is preserved within the transaction but has not been written to the database permanently. Only a COMMIT statement makes changes permanent. SAVEPOINT simply creates a partial-undo checkpoint within an ongoing transaction — it does not split the transaction into committed and uncommitted segments."

- question: "Why does putting business logic in a stored procedure provide stronger consistency guarantees than putting the same logic in application code, even if both implementations are correct?"
  type: short-answer
  answer: "Application code can be deployed inconsistently across multiple applications, can have version mismatches, or can be bypassed by anyone with direct database access. A stored procedure lives inside the database itself — it is the only path through which the operation executes, regardless of which application, user, or tool initiates the call. It also runs atomically inside the database engine, so network failures between application steps cannot leave the database in a half-updated state."
  explanation: "The key insight is that the database is the single source of truth, and stored procedures enforce rules at that level. Application-layer logic is contingent on every caller using the same version of the correct code — which is hard to guarantee in practice. By contrast, a stored procedure ensures that the rules are enforced at the point where data actually changes, making consistency a property of the database rather than a property of every application that talks to it."
```

## Explainer

You know how to write SELECT queries to retrieve data and you understand that transactions group operations into atomic units. But standard SQL is declarative — you say *what* you want, not *how* to do it step by step. **Stored procedures** bridge this gap by adding procedural logic directly inside the database. A stored procedure is a named block of code saved in the database that can declare variables, use IF/ELSE branching, loop with WHILE or FOR, handle errors with TRY/CATCH (or EXCEPTION blocks in PostgreSQL), and execute multiple SQL statements in sequence. You call it like a function: `CALL transfer_funds(account_from, account_to, amount)`.

The real power of stored procedures emerges when you combine procedural logic with **transaction control**. Consider a bank transfer: you must debit one account and credit another, and both must succeed or neither should. Inside a stored procedure, you wrap these operations in a transaction: `BEGIN` starts the transaction, `COMMIT` makes all changes permanent if everything succeeds, and `ROLLBACK` undoes everything if any step fails. **SAVEPOINT** adds finer granularity — you can mark intermediate points and roll back to them without aborting the entire transaction. The procedure can check conditions (is the balance sufficient?), branch on the result, and roll back with a meaningful error message if the business rule is violated.

Why put this logic in the database rather than in application code? Because the database is the single point of truth. If three different applications — a web app, a mobile app, and an internal admin tool — all need to transfer funds, embedding the logic in a stored procedure guarantees that every transfer follows the same rules. Application code can have bugs, can be deployed inconsistently, or can be bypassed entirely by someone running SQL directly. A stored procedure enforces the rules regardless of the caller. The tradeoff is that procedural SQL syntax is less ergonomic than Python or Java, and business logic embedded in the database can be harder to version-control and test. In practice, most systems use stored procedures selectively — for operations where atomicity, consistency, and centralized enforcement matter most.
