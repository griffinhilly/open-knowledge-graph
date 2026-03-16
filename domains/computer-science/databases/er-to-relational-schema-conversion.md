---
id: er-to-relational-schema-conversion
title: Converting ER Diagrams to Relational Schemas
domain: computer-science
course: databases
prerequisites:
- id: entity-relationship-diagram-advanced
  type: hard
- id: relational-model-basics
  type: hard
- id: primary-key-foreign-key-constraints
  type: hard
builds-toward:
- sql-table-creation-definition
- database-normalization-1nf-2nf
tags:
- mapping
- schema-design
- conversion
stage: formal-systems
status: draft
---

# Converting ER Diagrams to Relational Schemas

## Core Idea
Systematic rules convert each ER construct to relational tables: entity types become tables, attributes become columns, relationships become foreign keys or junction tables based on cardinality, weak entities create composite keys, and specialization hierarchies use either single tables with type discriminators or multiple related tables. Understanding these mappings ensures sound database design that properly represents requirements.

## Explainer

You already know how to draw ER diagrams with entities, attributes, and relationships, and you understand the relational model — tables with rows, columns, primary keys, and foreign keys. The conversion process is a systematic set of rules that translates every construct in an ER diagram into relational tables. Once you internalize these rules, you can mechanically convert any ER design into a working database schema.

The simplest rule handles **strong entities**: each entity type becomes a table, each attribute becomes a column, and the entity's key attribute becomes the primary key. An entity "Student" with attributes student_id, name, and email becomes a table `Student(student_id PK, name, email)`. **Multivalued attributes** cannot be stored in a single column (that would violate first normal form), so they get their own table with a foreign key back to the parent entity. A student with multiple phone numbers produces a separate `StudentPhone(student_id FK, phone)` table. **Composite attributes** are flattened — an "address" composed of street, city, and zip becomes three separate columns. **Derived attributes** (like age computed from birth_date) are typically omitted from the schema and calculated at query time.

**Relationships** are where cardinality drives the design. For a **one-to-many** relationship (one department has many employees), you add the primary key of the "one" side as a foreign key in the "many" side's table — `Employee` gets a `dept_id` foreign key pointing to `Department`. No separate table is needed. For a **many-to-many** relationship (students enroll in courses), neither side can hold the foreign key alone, so you create a **junction table** (also called an association or bridge table) containing the primary keys of both entities as foreign keys: `Enrollment(student_id FK, course_id FK)`. Together these form the junction table's composite primary key. Any attributes of the relationship itself (like enrollment_date or grade) become additional columns in the junction table. For **one-to-one** relationships, you place the foreign key on either side — typically the side with total participation, where every row must participate in the relationship.

**Weak entities** depend on a strong entity for identification. A "Dependent" identified by (employee_id, dependent_name) becomes a table whose primary key is the composite of the owning entity's key and the weak entity's partial key, with the owner's key also serving as a foreign key. **Specialization hierarchies** (like "Person" specialized into "Student" and "Faculty") offer three mapping strategies: a single table with a type discriminator column and nullable columns for subclass-specific attributes; separate tables for each subclass that include the superclass attributes; or a superclass table joined to subclass tables sharing the same primary key. The choice depends on query patterns — the single-table approach avoids joins but wastes space with nulls, while separate tables are cleaner when subclasses have many distinct attributes.
