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
status: validated
---

# ER Model: Weak Entities and Specialization Hierarchies

## Core Idea
The extended ER model includes weak entities (those requiring a strong entity for identity, like apartments within buildings) and specialization/generalization hierarchies (ISA relationships like Employee → FullTimeEmployee, PartTimeEmployee). These advanced constructs enable modeling of real-world structures with inheritance and dependency relationships that basic ER diagrams cannot express.

## Questions

```yaml
- question: "A database models course sections, where each section is identified by a number (1, 2, 3) unique only within a specific course. How should this be modeled?"
  type: multiple-choice
  options:
    - "Section as a regular entity with section number as its primary key"
    - "Section as a weak entity with section number as its partial key and Course as its identifying owner"
    - "Section as a weak entity with course ID as its primary key"
    - "Section as an attribute of the Course entity"
  answer: 1
  explanation: "Section numbers are only unique within a course — 'Section 2' of CS101 differs from 'Section 2' of MATH201. This is the classic weak entity pattern: Section cannot be identified by its own attributes alone. Its partial key (section number) combined with the owner's primary key (course ID) forms its full identity. Option A is wrong because numbers collide across courses. Option C is wrong because it misidentifies which key belongs to the weak entity. Option D loses the ability to record section-specific data like enrollment or instructor."

- question: "A university models Person with subclasses Student and Faculty. Queries almost always access only Student-specific attributes for one subclass at a time. Which ISA mapping strategy minimizes joins for these queries?"
  type: multiple-choice
  options:
    - "Separate tables for Person, Student, and Faculty — Student references Person via foreign key"
    - "One table per subclass only, with shared Person attributes duplicated in each"
    - "A single combined table with a type discriminator and nullable columns for subclass attributes"
    - "All three strategies produce equivalent join costs for this query pattern"
  answer: 1
  explanation: "When queries focus on one subclass at a time, having a separate Student table avoids the overhead of scanning a large combined table. The single-table approach (C) avoids joins but wastes space on nulls and weakens constraints. The subclass-only approach (B) avoids joins but duplicates shared attributes and makes cross-subclass queries expensive. Option A (separate tables) requires a join to reconstruct a full person record but is efficient when queries target subclass-specific attributes."

- question: "When a weak entity's identifying strong entity is deleted, the weak entities it owns should also be deleted."
  type: true-false
  answer: true
  explanation: "This follows directly from the semantics of weak entities. A weak entity depends on its identifying owner for its very existence and identity — an apartment record in a demolished building has no meaning. In SQL, this is implemented with ON DELETE CASCADE on the foreign key linking the weak entity to its owner. Allowing the strong entity to be deleted while leaving weak entities behind would create orphaned records with broken identity, violating the dependency that motivated the weak entity model."

- question: "In an ISA hierarchy, 'total' specialization means that every subclass entity must belong to every superclass."
  type: true-false
  answer: false
  explanation: "This conflates two independent dimensions of ISA constraints. 'Total' specialization means every superclass entity must belong to at least one subclass — every Person must be either a Student or Faculty (or both, if overlapping). It says nothing about subclass entities and superclasses. 'Disjoint' vs 'overlapping' governs whether an entity can belong to multiple subclasses simultaneously. Total/partial controls coverage of the superclass; disjoint/overlapping controls overlap among subclasses. These are orthogonal properties."

- question: "Why does a weak entity use a partial key rather than its own full primary key?"
  type: short-answer
  answer: "A weak entity lacks attributes that can uniquely identify its instances across all contexts — its partial key is only unique within the scope of its identifying owner. Apartment '3B' is not globally unique, but 'Building 7, Apartment 3B' is. The full primary key in a relational schema must therefore be a composite of its partial key and the owner's primary key. This composite key also encodes the real-world dependency: the apartment's identity is inherently tied to the building."
  explanation: "Assigning a surrogate key (like a sequential ID) would technically avoid collisions but would hide the natural dependency relationship and make the schema harder to understand. The partial key concept captures a genuine ontological fact: these entities exist and have meaning only relative to their owners."
```

## Explainer

In basic ER modeling, every entity has its own primary key and can stand on its own. But real-world data is full of things that only make sense in the context of something else. An apartment number like "3B" is meaningless without knowing which building it belongs to — there could be dozens of apartment 3Bs across a city. A **weak entity** is one that cannot be uniquely identified by its own attributes alone. It depends on a related **strong entity** (called its **identifying owner**) for part of its identity. The weak entity has a **partial key** (also called a discriminator) — the attribute that distinguishes it *within* its owner. Apartment 3B in Building 7 is unique; the full key is the combination of the building's ID and the apartment's number.

In an ER diagram, weak entities are drawn with double-bordered rectangles and their identifying relationships with double-bordered diamonds. When you convert this to a relational schema, the weak entity's table includes the owner's primary key as part of its own composite primary key, along with a foreign key constraint back to the owner. If the strong entity is deleted, the weak entities should typically be deleted too — this maps naturally to ON DELETE CASCADE in SQL. Other classic examples include order line items (meaningless without their parent order), exam questions (identified by question number within a specific exam), and dependent family members (identified by name within an employee record).

**Specialization and generalization** (the ISA hierarchy) address a different modeling challenge: entities that share common attributes but also have distinct ones. Think of a university's "Person" entity that specializes into "Student" and "Faculty." Both have names and IDs (the shared superclass attributes), but students have GPAs and majors while faculty have salaries and tenure status. The ISA relationship is drawn as a triangle connecting the superclass to its subclasses. Specialization can be **disjoint** (a person is either a student or faculty, not both) or **overlapping** (a person could be both). It can also be **total** (every person must be one of the subclasses) or **partial** (some persons may not belong to any subclass).

When converting ISA hierarchies to relational tables, you have three standard strategies. First, you can create a separate table for each entity in the hierarchy — a Person table, a Student table, and a Faculty table — where the subclass tables reference the superclass via foreign key. This preserves the hierarchy cleanly but requires joins to reconstruct a full student record. Second, you can push all attributes into the subclass tables (no superclass table), which avoids joins but duplicates shared attributes and makes it hard to query across all people. Third, you can collapse everything into a single table with nullable columns for subclass-specific attributes and a type discriminator column. This is simple and avoids joins but wastes space and weakens constraints — you cannot enforce that a faculty member has a salary but a student does not. The right choice depends on your query patterns and how strict your integrity requirements are.
