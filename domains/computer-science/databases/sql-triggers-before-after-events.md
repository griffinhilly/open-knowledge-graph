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
