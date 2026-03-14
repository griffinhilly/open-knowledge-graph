---
id: primary-key-foreign-key-constraints
title: Primary Keys and Foreign Key Relationships
domain: computer-science
course: databases
prerequisites:
- id: sql-constraint-enforcement
  type: hard
- id: entity-relationship-conceptual-design
  type: soft
builds-toward:
- functional-dependency-schema
tags:
- primary key
- foreign key
- referential integrity
- relationships
stage: formal-systems
status: draft
---

# Primary Keys and Foreign Key Relationships

## Core Idea
A primary key uniquely identifies each row in a table and cannot contain NULL values. A foreign key in one table references the primary key in another table, establishing relationships and enforcing referential integrity. Together they implement database relationships and prevent orphaned records.

## How It's Best Learned
Design multi-table schemas with primary and foreign keys, understand ON DELETE/UPDATE actions (CASCADE, SET NULL, RESTRICT), and practice enforcing referential integrity constraints.
