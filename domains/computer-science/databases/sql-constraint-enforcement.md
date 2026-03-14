---
id: sql-constraint-enforcement
title: 'SQL: Constraints (PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK, DEFAULT)'
domain: computer-science
course: databases
prerequisites:
- id: sql-table-creation-definition
  type: hard
builds-toward:
- primary-key-foreign-key-constraints
- functional-dependency-schema
tags:
- SQL
- constraint
- integrity
- validation
stage: formal-systems
status: draft
---

# SQL: Constraints (PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK, DEFAULT)

## Core Idea
Constraints enforce data integrity rules at the database level. PRIMARY KEY uniquely identifies rows. FOREIGN KEY enforces relationships between tables. UNIQUE prevents duplicate values. CHECK enforces domain constraints. DEFAULT assigns automatic values. Constraints prevent invalid data at the point of entry.

## How It's Best Learned
Design schemas with appropriate constraints, understand how constraints prevent invalid operations, and practice handling constraint violations in INSERT/UPDATE statements.
