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
