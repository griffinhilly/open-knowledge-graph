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
- sql-triggers-and-events
- transaction-properties-acid
tags:
- stored-procedures
- procedural
- BEGIN-COMMIT-ROLLBACK
stage: formal-systems
status: draft
---

# Stored Procedures: Procedural Logic and Transaction Control

## Core Idea
Stored procedures are SQL programs stored in the database that encapsulate business logic and enforce consistent behavior across applications. They support control flow (IF/ELSE, loops), variables, and error handling. Transaction control statements (BEGIN, COMMIT, ROLLBACK, SAVEPOINT) manage transaction boundaries, grouping multiple statements into atomic units that succeed completely or fail together.

## Explainer

You know how to write SELECT queries to retrieve data and you understand that transactions group operations into atomic units. But standard SQL is declarative — you say *what* you want, not *how* to do it step by step. **Stored procedures** bridge this gap by adding procedural logic directly inside the database. A stored procedure is a named block of code saved in the database that can declare variables, use IF/ELSE branching, loop with WHILE or FOR, handle errors with TRY/CATCH (or EXCEPTION blocks in PostgreSQL), and execute multiple SQL statements in sequence. You call it like a function: `CALL transfer_funds(account_from, account_to, amount)`.

The real power of stored procedures emerges when you combine procedural logic with **transaction control**. Consider a bank transfer: you must debit one account and credit another, and both must succeed or neither should. Inside a stored procedure, you wrap these operations in a transaction: `BEGIN` starts the transaction, `COMMIT` makes all changes permanent if everything succeeds, and `ROLLBACK` undoes everything if any step fails. **SAVEPOINT** adds finer granularity — you can mark intermediate points and roll back to them without aborting the entire transaction. The procedure can check conditions (is the balance sufficient?), branch on the result, and roll back with a meaningful error message if the business rule is violated.

Why put this logic in the database rather than in application code? Because the database is the single point of truth. If three different applications — a web app, a mobile app, and an internal admin tool — all need to transfer funds, embedding the logic in a stored procedure guarantees that every transfer follows the same rules. Application code can have bugs, can be deployed inconsistently, or can be bypassed entirely by someone running SQL directly. A stored procedure enforces the rules regardless of the caller. The tradeoff is that procedural SQL syntax is less ergonomic than Python or Java, and business logic embedded in the database can be harder to version-control and test. In practice, most systems use stored procedures selectively — for operations where atomicity, consistency, and centralized enforcement matter most.
