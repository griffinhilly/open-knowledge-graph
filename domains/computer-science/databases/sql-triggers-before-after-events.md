---
id: sql-triggers-before-after-events
title: Database Triggers and Automated Event Handling
domain: computer-science
course: databases
prerequisites:
- id: sql-data-insertion-modification
  type: hard
- id: sql-stored-procedures-control-flow
  type: hard
builds-toward:
- database-schema-design
- sql-constraint-types-domain-check
tags:
- triggers
- events
- automation
- before-after
- FOR-EACH-ROW
stage: formal-systems
status: draft
---

# Database Triggers and Automated Event Handling

## Core Idea
Triggers are database objects that automatically execute SQL code in response to DML events (INSERT, UPDATE, DELETE) on specific tables. BEFORE triggers execute before the event and can validate or modify data; AFTER triggers execute after and can update related tables or log changes. FOR EACH ROW triggers execute once per affected row, while statement-level triggers execute once per statement.

## Explainer

You already know how to write stored procedures — blocks of procedural SQL code that encapsulate logic on the server side. Triggers use that same procedural capability but with a crucial difference: they fire **automatically** in response to data changes, without any explicit call from the application. Think of a trigger as an event listener attached to a table. When someone inserts, updates, or deletes a row, the database checks whether any triggers are defined for that event and executes them as part of the same transaction.

The distinction between **BEFORE** and **AFTER** triggers determines when your code runs relative to the data change. A BEFORE trigger fires before the row is actually written to disk. This makes it ideal for **validation and transformation**: you can inspect the incoming data, reject it by raising an error, or silently modify it. For example, a BEFORE INSERT trigger might normalize a phone number format, enforce a business rule that application code forgot to check, or automatically set a `created_at` timestamp. Inside a BEFORE trigger, you have access to the `NEW` row (the data about to be written) and for updates, the `OLD` row (the data being replaced). An AFTER trigger fires after the change has been committed to the table. It's the right choice for **side effects**: logging the change to an audit table, updating a summary or materialized count in another table, or sending a notification. Since the data change has already succeeded, AFTER triggers can safely reference the final state of the row.

The second axis of trigger design is **row-level versus statement-level** execution. A `FOR EACH ROW` trigger fires once per affected row — if an UPDATE modifies 500 rows, the trigger executes 500 times, with `NEW` and `OLD` bound to each specific row. A statement-level trigger fires only once for the entire statement, regardless of how many rows are affected. Statement-level triggers are useful for actions that should happen once per operation (logging that a batch update occurred) rather than once per row, and they perform better when row-level granularity isn't needed.

Triggers are powerful but carry real risks. Because they fire invisibly, they can make debugging difficult — an INSERT that seems straightforward might cascade through multiple triggers, modifying other tables in ways that are hard to trace. **Trigger chains** (where one trigger's action fires another trigger) can create complex execution paths and even infinite loops if not carefully guarded. They also add overhead to every DML operation on the table, which matters for high-throughput workloads. The general guidance is to use triggers for cross-cutting concerns that must be enforced regardless of which application or query modifies the data (audit logging, referential actions, derived column maintenance), but to keep business logic in the application layer where it's more visible and testable.
