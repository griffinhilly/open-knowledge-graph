---
id: database-normalization-1nf-2nf
title: First and Second Normal Forms
domain: computer-science
course: databases
prerequisites:
- id: functional-dependencies
  type: hard
- id: entity-relationship-diagrams
  type: soft
builds-toward:
- database-normalization-3nf-bcnf
- database-schema-design
tags:
- normalization
- 1NF
- 2NF
- data anomalies
- redundancy
- partial dependency
stage: formal-systems
status: validated
---

# First and Second Normal Forms

## Core Idea
Normalization is the process of organizing a relational schema to eliminate data redundancy and update anomalies by decomposing tables based on functional dependencies. First Normal Form (1NF) requires each attribute to contain only atomic, indivisible values with no repeating groups or arrays in a cell. Second Normal Form (2NF) builds on 1NF by requiring that every non-key attribute be fully functionally dependent on the entire primary key — eliminating partial dependencies where a non-key attribute depends on only part of a composite key.

## How It's Best Learned
Start with a deliberately denormalized flat-file table (e.g., an order form with customer info repeated on every line item) and trace the anomalies. Decompose step-by-step to 1NF then 2NF, noting which anomalies each step eliminates.

## Common Misconceptions
- 1NF is violated by storing comma-separated lists in a single column — each value must be atomic.
- 2NF only matters when the primary key is composite; tables with a single-column primary key are automatically in 2NF.
- Normalization is not always the right choice — performance-sensitive read-heavy workloads sometimes deliberately denormalize.
