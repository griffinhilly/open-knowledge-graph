---
id: sql-constraint-types-domain-check
title: 'Constraint Types: Domain, Check, Unique, and Key Constraints'
domain: computer-science
course: databases
prerequisites:
- id: sql-table-creation-definition
  type: hard
builds-toward:
- referential-integrity-cascading-actions
- sql-constraint-enforcement
tags:
- constraints
- integrity
- domain
- check
- unique
stage: formal-systems
status: draft
---

# Constraint Types: Domain, Check, Unique, and Key Constraints

## Core Idea
Databases support multiple constraint types to maintain data integrity: domain constraints restrict column values to appropriate types and ranges, check constraints enforce logical conditions on column values, unique constraints prevent duplicate non-null values, and key constraints uniquely identify rows. The DBMS automatically enforces these constraints, rejecting invalid data before it enters the database.
