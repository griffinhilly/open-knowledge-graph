---
id: entity-relationship-model-weak-entities-isa
title: 'ER Model: Weak Entities and Specialization Hierarchies'
domain: computer-science
course: databases
prerequisites:
- id: entity-relationship-diagrams
  type: hard
builds-toward:
- er-to-relational-schema-conversion
tags:
- ER-model
- weak-entities
- specialization
- inheritance
- ISA
stage: formal-systems
status: draft
---

# ER Model: Weak Entities and Specialization Hierarchies

## Core Idea
The extended ER model includes weak entities (those requiring a strong entity for identity, like apartments within buildings) and specialization/generalization hierarchies (ISA relationships like Employee → FullTimeEmployee, PartTimeEmployee). These advanced constructs enable modeling of real-world structures with inheritance and dependency relationships that basic ER diagrams cannot express.

## Explainer

In basic ER modeling, every entity has its own primary key and can stand on its own. But real-world data is full of things that only make sense in the context of something else. An apartment number like "3B" is meaningless without knowing which building it belongs to — there could be dozens of apartment 3Bs across a city. A **weak entity** is one that cannot be uniquely identified by its own attributes alone. It depends on a related **strong entity** (called its **identifying owner**) for part of its identity. The weak entity has a **partial key** (also called a discriminator) — the attribute that distinguishes it *within* its owner. Apartment 3B in Building 7 is unique; the full key is the combination of the building's ID and the apartment's number.

In an ER diagram, weak entities are drawn with double-bordered rectangles and their identifying relationships with double-bordered diamonds. When you convert this to a relational schema, the weak entity's table includes the owner's primary key as part of its own composite primary key, along with a foreign key constraint back to the owner. If the strong entity is deleted, the weak entities should typically be deleted too — this maps naturally to ON DELETE CASCADE in SQL. Other classic examples include order line items (meaningless without their parent order), exam questions (identified by question number within a specific exam), and dependent family members (identified by name within an employee record).

**Specialization and generalization** (the ISA hierarchy) address a different modeling challenge: entities that share common attributes but also have distinct ones. Think of a university's "Person" entity that specializes into "Student" and "Faculty." Both have names and IDs (the shared superclass attributes), but students have GPAs and majors while faculty have salaries and tenure status. The ISA relationship is drawn as a triangle connecting the superclass to its subclasses. Specialization can be **disjoint** (a person is either a student or faculty, not both) or **overlapping** (a person could be both). It can also be **total** (every person must be one of the subclasses) or **partial** (some persons may not belong to any subclass).

When converting ISA hierarchies to relational tables, you have three standard strategies. First, you can create a separate table for each entity in the hierarchy — a Person table, a Student table, and a Faculty table — where the subclass tables reference the superclass via foreign key. This preserves the hierarchy cleanly but requires joins to reconstruct a full student record. Second, you can push all attributes into the subclass tables (no superclass table), which avoids joins but duplicates shared attributes and makes it hard to query across all people. Third, you can collapse everything into a single table with nullable columns for subclass-specific attributes and a type discriminator column. This is simple and avoids joins but wastes space and weakens constraints — you cannot enforce that a faculty member has a salary but a student does not. The right choice depends on your query patterns and how strict your integrity requirements are.
