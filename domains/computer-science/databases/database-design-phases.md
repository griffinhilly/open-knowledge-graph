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
status: validated
---

# Database Design Process: Conceptual, Logical, and Physical

## Core Idea
Database design proceeds through three phases: (1) Conceptual design models business requirements using ER diagrams without implementation details, (2) Logical design translates the conceptual model to relational tables with keys and constraints, and (3) Physical design optimizes for performance through indexing, partitioning, and storage structure decisions. Each phase has distinct objectives and techniques.

## Questions

```yaml
- question: "A developer building a new system immediately starts defining table names, column data types, and indexes. Which phase is being skipped, and what is the most likely consequence?"
  type: multiple-choice
  options:
    - "Physical design is being skipped; performance will suffer because indexes are absent"
    - "Conceptual design is being skipped; the schema may not accurately reflect business requirements"
    - "Logical design is being skipped; the database will lack proper primary and foreign keys"
    - "Nothing significant is skipped; jumping to tables is an acceptable shortcut for experienced developers"
  answer: 1
  explanation: "Jumping directly to tables and columns collapses conceptual and physical concerns before anyone has validated what entities and relationships actually need to be represented. The conceptual phase exists precisely to separate 'what must we model?' from 'how do we store it?' — without it, implementation intuitions drive schema design instead of business requirements."

- question: "A business stakeholder reviews a document and says 'Yes, this captures exactly what we need.' In which design phase is this stakeholder feedback most meaningful?"
  type: multiple-choice
  options:
    - "Physical design — the stakeholder is confirming that storage and indexing choices are correct"
    - "Logical design — the stakeholder is approving the table schema and normalization decisions"
    - "Conceptual design — the stakeholder is validating the entity-relationship model"
    - "All phases equally — stakeholders should review and approve every design artifact"
  answer: 2
  explanation: "Conceptual design intentionally produces technology-independent ER diagrams that business stakeholders can read without knowing anything about relational databases. This is the phase where you confirm that the model reflects real-world entities and relationships correctly. Logical and physical artifacts are increasingly technical and are validated by the engineering team, not business stakeholders."

- question: "The physical design phase is where primary keys and foreign keys are defined, and normalization rules are applied to eliminate redundancy."
  type: true-false
  answer: false
  explanation: "Defining primary keys, foreign keys, and applying normalization are logical design activities. The logical phase translates the conceptual model into relational structures while remaining independent of any specific database system. Physical design comes after: it chooses data types, creates indexes, and configures partitioning and storage — decisions driven by the actual query workload."

- question: "When a new business entity must be added to an existing database, the change should be traced back to the conceptual design phase before modifying the schema."
  type: true-false
  answer: true
  explanation: "A new entity is a requirements-level change — it affects what needs to be represented, which is the domain of conceptual design. Starting from conceptual ensures the entity's attributes and relationships are fully understood before they are translated into tables (logical phase) and optimized (physical phase). Skipping straight to schema changes risks missing relationships or creating an entity that doesn't align with the overall data model."

- question: "Why does the three-phase design process separate conceptual, logical, and physical concerns rather than addressing them all at once?"
  type: short-answer
  answer: "Each phase answers a fundamentally different question at a different level of abstraction: conceptual asks 'what does the business need to represent?', logical asks 'how should that be structured as relational tables with integrity constraints?', and physical asks 'how should those tables be stored and indexed for performance?' Mixing the phases causes implementation details to constrain requirements modeling before requirements are fully understood, leading to schemas that fit one technical approach but don't accurately capture the underlying domain."
  explanation: "The separation-of-concerns principle is the key design insight. Business stakeholders can review ER diagrams without knowing SQL; database designers can normalize without worrying about query performance; and DBAs can optimize physical layout without reopening what entities need to exist. When requirements change, the three-phase structure also tells you exactly which layer to revisit: a new entity goes to conceptual, a new constraint to logical, a slow query to physical."
```

## Explainer

You already understand what a relational database is — tables with rows and columns, linked by keys. But how do you go from a business problem ("we need to track customer orders") to a working schema? The answer is a structured three-phase design process, where each phase operates at a different level of abstraction. Skipping phases or collapsing them together is the most common source of poorly designed databases, because it mixes "what do we need to represent?" with "how do we store it efficiently?" before either question is fully answered.

**Conceptual design** is the first phase, and it is deliberately technology-independent. You work with stakeholders to identify the key entities (customers, orders, products), their attributes (customer name, order date, product price), and the relationships between them (a customer places many orders; an order contains many products). The primary tool here is the **Entity-Relationship (ER) diagram**, which visually maps these entities and their connections. At this stage, you do not think about data types, primary keys, or table structures — you think about the real-world things and their relationships. The goal is a model that a business stakeholder can look at and say "yes, that captures what we need."

**Logical design** translates the conceptual model into relational structures. Each entity becomes a table, each attribute becomes a column, and relationships become foreign keys or junction tables. This is where you assign primary keys, define constraints (NOT NULL, UNIQUE), and apply normalization rules to eliminate redundancy. A many-to-many relationship between Orders and Products, for example, becomes a junction table (often called OrderItems) with foreign keys to both. The logical model is specific to the relational model but still independent of any particular database system — you are defining the schema's structure and integrity rules, not its physical implementation.

**Physical design** is where performance enters the picture. You choose specific data types (VARCHAR(255) vs TEXT), create indexes on columns that appear in WHERE clauses and JOIN conditions, decide on partitioning strategies for large tables, and configure storage parameters. Physical design decisions depend heavily on the actual query workload: a table that is read frequently but rarely updated benefits from multiple indexes, while a write-heavy logging table might use minimal indexing. The three phases flow naturally from abstract to concrete — each one takes the output of the previous phase as input and adds a layer of implementation detail. When requirements change, you revisit the appropriate phase: a new business entity goes back to conceptual design, a new relationship constraint to logical design, and a slow query to physical design.
