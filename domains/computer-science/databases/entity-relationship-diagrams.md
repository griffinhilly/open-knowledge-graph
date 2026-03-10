---
id: entity-relationship-diagrams
title: Entity-Relationship Diagrams
domain: computer-science
course: databases
prerequisites:
- id: relational-model-basics
  type: hard
builds-toward:
- database-schema-design
- primary-and-foreign-keys
tags:
- ER diagrams
- data modeling
- entities
- relationships
- cardinality
stage: formal-systems
status: draft
---

# Entity-Relationship Diagrams

## Core Idea
Entity-Relationship (ER) diagrams are a visual tool for modeling the conceptual structure of a database before implementation. Entities represent real-world objects (e.g., Student, Course), attributes describe their properties, and relationships capture how entities associate with one another. Cardinality annotations (one-to-one, one-to-many, many-to-many) specify how many instances of each entity can participate in a relationship. ER diagrams are later translated into relational schemas during logical design.

## How It's Best Learned
Model a familiar domain (e.g., a library system with Books, Members, and Loans) by drawing entities and relationships first, then convert to tables. Practice distinguishing weak entities, identifying keys, and resolving many-to-many relationships via junction tables.

## Common Misconceptions
- Attributes that look like relationships (storing a customer's city as a string vs. linking to a Cities table) are a common design error.
- Many-to-many relationships must be resolved into a junction (associative) table in the relational model — they cannot be represented directly.
