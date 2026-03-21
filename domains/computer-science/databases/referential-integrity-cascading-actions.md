---
id: referential-integrity-cascading-actions
title: Referential Integrity and Cascading Delete/Update Actions
domain: computer-science
course: databases
prerequisites:
- id: primary-key-foreign-key-constraints
  type: hard
- id: sql-constraint-types-domain-check
  type: hard
builds-toward:
- database-schema-design
- sql-constraint-enforcement
tags:
- referential-integrity
- foreign-keys
- cascading
- actions
stage: formal-systems
status: draft
---

# Referential Integrity and Cascading Delete/Update Actions

## Core Idea
Referential integrity ensures that foreign key values correspond to existing primary key values in referenced tables. Cascading actions define what happens when referenced rows are modified: CASCADE automatically updates/deletes dependent rows, SET NULL sets foreign keys to null, SET DEFAULT uses default values, and RESTRICT prevents the operation if dependent rows exist. Choosing the right action prevents orphaned records and maintains consistency.

## Questions

```yaml
- question: "A university database has a `students` table and an `enrollments` table with a foreign key referencing students. After a student withdraws, an administrator deletes the student's record. The university wants to keep enrollment records for institutional history, but with the student reference cleared. Which ON DELETE action achieves this?"
  type: multiple-choice
  options:
    - "CASCADE — deletes the student and automatically removes all their enrollment records"
    - "SET NULL — keeps enrollment records but sets the student_id foreign key to NULL"
    - "RESTRICT — prevents the delete until all enrollment records are removed manually"
    - "SET DEFAULT — replaces the student_id with a placeholder value defined at table creation"
  answer: 1
  explanation: "SET NULL keeps the child rows (enrollment records) while clearing the foreign key that points to the now-deleted student. This is appropriate for 'association' relationships where the child has independent value. CASCADE would destroy the enrollment records entirely — the wrong outcome here. RESTRICT would block the delete, forcing manual cleanup. SET DEFAULT works only if a meaningful default was defined."

- question: "A developer applies ON DELETE CASCADE to every foreign key in a schema 'to avoid constraint violation errors.' They then delete a single top-level department record. What is the most dangerous likely consequence?"
  type: multiple-choice
  options:
    - "The delete will fail because cascading across multiple tables is not permitted"
    - "Child rows (employees, projects, budgets) will be automatically deleted, potentially removing far more data than the developer intended"
    - "The foreign key constraints will be silently ignored for the operation"
    - "Child rows will be preserved and their foreign keys set to NULL automatically"
  answer: 1
  explanation: "CASCADE propagates deletes automatically through every table that references the deleted row, and through tables that reference those tables, and so on. A single top-level delete can silently cascade through the entire dependency chain, removing large amounts of data with no confirmation prompt. The database is doing exactly what was configured — the danger is that the developer did not think through all downstream effects. This is why 'default to RESTRICT and use CASCADE only when you can articulate why automatic deletion is the correct business behavior' is the safer practice."

- question: "Referential integrity enforcement applies only when you delete rows from a parent table — not during INSERT or UPDATE operations on the child table."
  type: true-false
  answer: false
  explanation: "Referential integrity is enforced in both directions. When you INSERT a row into a child table with a foreign key value that does not exist in the parent table, the database rejects the INSERT. Similarly, an UPDATE that changes a child row's foreign key to a non-existent parent value is rejected. ON DELETE and ON UPDATE cascading actions address modifications to the *parent* table, but the database also continuously checks that child rows never reference non-existent parents."

- question: "Using ON DELETE CASCADE is most appropriate when child rows have no meaningful existence independent of their parent — for example, order line items that belong to a specific order."
  type: true-false
  answer: true
  explanation: "This is the 'composition' relationship pattern: the child is part of the parent and has no reason to exist on its own. If you delete an order, its line items should go with it — keeping orphaned line items would be meaningless. By contrast, for 'association' relationships (like students enrolled in courses), both sides have independent existence and CASCADE would be destructive. The relationship semantics determine the right cascading action."

- question: "Explain the difference between a 'composition' relationship and an 'association' relationship in database design, and give one example of each showing why they call for different ON DELETE actions."
  type: short-answer
  answer: "A composition relationship is one where the child has no meaningful existence without the parent — the child is a part of the parent. Example: order line items belong to an order; delete the order, and CASCADE-deleting the line items is correct because orphaned line items are meaningless. An association relationship is one where both sides have independent existence. Example: students and courses — a student enrolls in a course, but both exist independently. Deleting a course should not delete the students, and deleting a student should probably use SET NULL or RESTRICT on enrollment records, not CASCADE."
  explanation: "The composition vs. association distinction comes from object-oriented modeling (UML) and directly maps to the right cascading behavior. The key test: if the parent disappears, does the child still make sense on its own? If yes, use RESTRICT or SET NULL. If no, CASCADE may be appropriate — but only after explicitly reasoning through all the consequences."
```

## Explainer

You already know that foreign keys link rows in one table to rows in another, creating relationships that mirror real-world connections — an order belongs to a customer, a comment belongs to a post. **Referential integrity** is the guarantee that these links never point to nothing. If a foreign key in the `orders` table references `customer_id = 42`, then a row with `id = 42` must actually exist in the `customers` table. The database enforces this on every INSERT and UPDATE that touches a foreign key column, rejecting any operation that would create a dangling reference.

The interesting question is what happens when you go the other direction: what if you try to DELETE customer 42, who has 15 orders? Or UPDATE their primary key? This is where **cascading actions** come in. When you define a foreign key constraint, you specify an `ON DELETE` and `ON UPDATE` action that tells the database how to handle modifications to the referenced row. The options form a spectrum from most automatic to most restrictive.

**CASCADE** is the most aggressive option: deleting customer 42 automatically deletes all 15 of their orders. Updating the customer's primary key automatically updates the foreign key in every related order. This is convenient but dangerous — a single DELETE can ripple through many tables, removing far more data than you might expect. **SET NULL** takes a gentler approach: instead of deleting the orders, it sets their `customer_id` to NULL, effectively orphaning them in a controlled way. This works well when the child rows have independent value — you might want to keep order records even after removing a customer. **SET DEFAULT** works similarly but uses a predefined default value instead of NULL. **RESTRICT** (and its close cousin NO ACTION) is the safest choice: it simply blocks the DELETE or UPDATE if any dependent rows exist, forcing you to deal with the children first.

Choosing the right action depends on the relationship's semantics. For composition relationships where children have no meaning without their parent (like line items on an order), CASCADE makes sense — delete the order, delete its items. For association relationships where both sides have independent existence (like students enrolled in courses), RESTRICT or SET NULL is usually safer. A common mistake is applying CASCADE everywhere for convenience, then discovering that deleting one row triggers a chain reaction across half the database. The safest practice is to default to RESTRICT, switching to CASCADE only when you can articulate why automatic deletion is the correct business behavior.
