---
id: database-design-phases
title: 'Database Design Process: Conceptual, Logical, and Physical'
domain: computer-science
course: databases
prerequisites:
- id: database-systems-introduction
  type: hard
- id: relational-model-basics
  type: hard
builds-toward:
- entity-relationship-diagram-advanced
- database-schema-design
tags:
- design
- methodology
- phases
- requirements
stage: formal-systems
status: draft
---

# Database Design Process: Conceptual, Logical, and Physical

## Core Idea
Database design proceeds through three phases: (1) Conceptual design models business requirements using ER diagrams without implementation details, (2) Logical design translates the conceptual model to relational tables with keys and constraints, and (3) Physical design optimizes for performance through indexing, partitioning, and storage structure decisions. Each phase has distinct objectives and techniques.

## Explainer

You already understand what a relational database is — tables with rows and columns, linked by keys. But how do you go from a business problem ("we need to track customer orders") to a working schema? The answer is a structured three-phase design process, where each phase operates at a different level of abstraction. Skipping phases or collapsing them together is the most common source of poorly designed databases, because it mixes "what do we need to represent?" with "how do we store it efficiently?" before either question is fully answered.

**Conceptual design** is the first phase, and it is deliberately technology-independent. You work with stakeholders to identify the key entities (customers, orders, products), their attributes (customer name, order date, product price), and the relationships between them (a customer places many orders; an order contains many products). The primary tool here is the **Entity-Relationship (ER) diagram**, which visually maps these entities and their connections. At this stage, you do not think about data types, primary keys, or table structures — you think about the real-world things and their relationships. The goal is a model that a business stakeholder can look at and say "yes, that captures what we need."

**Logical design** translates the conceptual model into relational structures. Each entity becomes a table, each attribute becomes a column, and relationships become foreign keys or junction tables. This is where you assign primary keys, define constraints (NOT NULL, UNIQUE), and apply normalization rules to eliminate redundancy. A many-to-many relationship between Orders and Products, for example, becomes a junction table (often called OrderItems) with foreign keys to both. The logical model is specific to the relational model but still independent of any particular database system — you are defining the schema's structure and integrity rules, not its physical implementation.

**Physical design** is where performance enters the picture. You choose specific data types (VARCHAR(255) vs TEXT), create indexes on columns that appear in WHERE clauses and JOIN conditions, decide on partitioning strategies for large tables, and configure storage parameters. Physical design decisions depend heavily on the actual query workload: a table that is read frequently but rarely updated benefits from multiple indexes, while a write-heavy logging table might use minimal indexing. The three phases flow naturally from abstract to concrete — each one takes the output of the previous phase as input and adds a layer of implementation detail. When requirements change, you revisit the appropriate phase: a new business entity goes back to conceptual design, a new relationship constraint to logical design, and a slow query to physical design.
