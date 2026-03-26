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
- sql-constraint-enforcement
tags:
- triggers
- events
- automation
- before-after
- FOR-EACH-ROW
stage: formal-systems
status: validated
---

# Database Triggers and Automated Event Handling

## Core Idea
Triggers are database objects that automatically execute SQL code in response to DML events (INSERT, UPDATE, DELETE) on specific tables. BEFORE triggers execute before the event and can validate or modify data; AFTER triggers execute after and can update related tables or log changes. FOR EACH ROW triggers execute once per affected row, while statement-level triggers execute once per statement.

## Questions

```yaml
- question: "A database designer wants to ensure that whenever a new order is inserted, the order's total price is automatically rounded to two decimal places. Which trigger type is most appropriate?"
  type: multiple-choice
  options:
    - "AFTER INSERT FOR EACH ROW — it runs after the data is stored, so you can correct it"
    - "BEFORE INSERT FOR EACH ROW — it intercepts the data before writing and can modify NEW.total_price"
    - "AFTER INSERT FOR EACH STATEMENT — it handles all rows at once for efficiency"
    - "Either BEFORE or AFTER works identically for data modification"
  answer: 1
  explanation: "A BEFORE trigger fires before the row is written to disk and has access to NEW (the incoming data). This is the correct tool for transformation: you can directly modify NEW.total_price before it's stored. An AFTER trigger fires after the change is already committed to the table — at that point, modifying the data requires a separate UPDATE statement, which is slower and creates an additional trigger fire. BEFORE triggers are the idiomatic choice for validation and transformation."

- question: "A bulk UPDATE statement modifies 10,000 rows. How many times does a FOR EACH ROW trigger on that table execute, compared to a statement-level trigger?"
  type: multiple-choice
  options:
    - "Both execute exactly once, since it is one statement"
    - "The FOR EACH ROW trigger executes 10,000 times; the statement-level trigger executes once"
    - "The FOR EACH ROW trigger executes once; the statement-level trigger executes 10,000 times"
    - "Both execute 10,000 times for a bulk UPDATE"
  answer: 1
  explanation: "FOR EACH ROW triggers bind OLD and NEW to each affected row and fire for every row the statement touches — 10,000 times here. Statement-level triggers fire once per SQL statement regardless of rows affected. This difference has major performance implications: a FOR EACH ROW trigger that does expensive work (like writing to an audit table) will execute 10,000 times. For bulk operations where you only need to log that a batch occurred, a statement-level trigger is far more efficient."

- question: "An AFTER trigger can cause the data change that fired it to be rolled back."
  type: true-false
  answer: true
  explanation: "Although BEFORE triggers are the natural tool for cancellation (they can raise an error before the write occurs), AFTER triggers run inside the same transaction as the triggering statement. Raising an exception inside an AFTER trigger will roll back the entire transaction, including the data change. This is less common than using BEFORE for validation, but it is possible. Both trigger types run within the same transaction boundary."

- question: "Because triggers fire automatically regardless of which application modifies the data, they are the best place to enforce most business logic in a database application."
  type: true-false
  answer: false
  explanation: "Triggers are appropriate for cross-cutting concerns that must be enforced regardless of which application touches the data — audit logging, referential integrity, derived column maintenance. But placing general business logic in triggers creates serious maintainability problems: triggers fire invisibly, making debugging difficult. Trigger chains (one trigger firing another) can produce complex, opaque execution paths and even infinite loops. The standard guidance is to keep business logic in the application layer where it's visible and testable, using triggers only for concerns genuinely tied to the data layer."

- question: "Explain the key difference between what a BEFORE trigger and an AFTER trigger can accomplish, and give an example of an appropriate use case for each."
  type: short-answer
  answer: "A BEFORE trigger fires before the row is written to the table and can access and modify the NEW row — making it ideal for validation (reject the insert if a field is invalid) and transformation (normalize a phone number format, auto-set a created_at timestamp). An AFTER trigger fires after the change is successfully committed to the table — making it ideal for side effects like writing to an audit log, updating a summary counter in another table, or sending notifications. You cannot use an AFTER trigger to silently modify the data that was just written without issuing a separate UPDATE."
  explanation: "The timing determines capability: BEFORE = intercept and shape; AFTER = react and propagate. Mixing these up leads to either ineffective code (trying to validate after data is already written) or unnecessary complexity (issuing a corrective UPDATE in an AFTER trigger when a BEFORE trigger could have prevented the bad data in the first place)."
```

## Explainer

You already know how to write stored procedures — blocks of procedural SQL code that encapsulate logic on the server side. Triggers use that same procedural capability but with a crucial difference: they fire **automatically** in response to data changes, without any explicit call from the application. Think of a trigger as an event listener attached to a table. When someone inserts, updates, or deletes a row, the database checks whether any triggers are defined for that event and executes them as part of the same transaction.

The distinction between **BEFORE** and **AFTER** triggers determines when your code runs relative to the data change. A BEFORE trigger fires before the row is actually written to disk. This makes it ideal for **validation and transformation**: you can inspect the incoming data, reject it by raising an error, or silently modify it. For example, a BEFORE INSERT trigger might normalize a phone number format, enforce a business rule that application code forgot to check, or automatically set a `created_at` timestamp. Inside a BEFORE trigger, you have access to the `NEW` row (the data about to be written) and for updates, the `OLD` row (the data being replaced). An AFTER trigger fires after the change has been committed to the table. It's the right choice for **side effects**: logging the change to an audit table, updating a summary or materialized count in another table, or sending a notification. Since the data change has already succeeded, AFTER triggers can safely reference the final state of the row.

The second axis of trigger design is **row-level versus statement-level** execution. A `FOR EACH ROW` trigger fires once per affected row — if an UPDATE modifies 500 rows, the trigger executes 500 times, with `NEW` and `OLD` bound to each specific row. A statement-level trigger fires only once for the entire statement, regardless of how many rows are affected. Statement-level triggers are useful for actions that should happen once per operation (logging that a batch update occurred) rather than once per row, and they perform better when row-level granularity isn't needed.

Triggers are powerful but carry real risks. Because they fire invisibly, they can make debugging difficult — an INSERT that seems straightforward might cascade through multiple triggers, modifying other tables in ways that are hard to trace. **Trigger chains** (where one trigger's action fires another trigger) can create complex execution paths and even infinite loops if not carefully guarded. They also add overhead to every DML operation on the table, which matters for high-throughput workloads. The general guidance is to use triggers for cross-cutting concerns that must be enforced regardless of which application or query modifies the data (audit logging, referential actions, derived column maintenance), but to keep business logic in the application layer where it's more visible and testable.
