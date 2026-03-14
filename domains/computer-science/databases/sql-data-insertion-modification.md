---
id: sql-data-insertion-modification
title: 'SQL: INSERT, UPDATE, and DELETE (DML)'
domain: computer-science
course: databases
prerequisites:
- id: sql-table-creation-definition
  type: hard
builds-toward:
- transaction-properties-acid
tags:
- SQL
- DML
- INSERT
- UPDATE
- DELETE
- modification
stage: formal-systems
status: draft
---

# SQL: INSERT, UPDATE, and DELETE (DML)

## Core Idea
Data Manipulation Language (DML) modifies table contents. INSERT adds new rows, UPDATE changes existing row values, and DELETE removes rows. DML operations must respect constraints and are typically wrapped in transactions for consistency.

## How It's Best Learned
Practice INSERT with explicit column lists, multi-row inserts, and INSERT...SELECT. Practice UPDATE with WHERE conditions affecting multiple rows. Understand the importance of WHERE clauses to avoid accidental data loss.
