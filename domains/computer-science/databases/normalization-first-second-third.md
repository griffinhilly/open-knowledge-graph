---
id: normalization-first-second-third
title: Database Normalization (1NF, 2NF, 3NF)
domain: computer-science
course: databases
prerequisites:
- id: functional-dependency-schema
  type: hard
builds-toward:
- bcnf-higher-normalization
- denormalization-strategy
tags:
- normalization
- 1NF
- 2NF
- 3NF
- redundancy
stage: formal-systems
status: draft
---

# Database Normalization (1NF, 2NF, 3NF)

## Core Idea
Normalization is the process of organizing data to eliminate redundancy and improve integrity. First Normal Form (1NF) requires atomic attributes. Second Normal Form (2NF) eliminates partial dependencies on composite keys. Third Normal Form (3NF) eliminates transitive dependencies. Each higher form builds on the previous, reducing data anomalies.

## How It's Best Learned
Take denormalized schemas with redundancy and step through 1NF, 2NF, 3NF decomposition. Understand the problems each normal form solves: insertion/deletion/update anomalies and inconsistency.
