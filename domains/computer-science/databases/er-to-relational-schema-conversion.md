---
id: er-to-relational-schema-conversion
title: Converting ER Diagrams to Relational Schemas
domain: computer-science
course: databases
prerequisites:
- id: entity-relationship-model-weak-entities-isa
  type: hard
- id: relational-data-model
  type: hard
- id: primary-and-foreign-keys
  type: hard
builds-toward:
- sql-table-creation-definition
- database-normalization-1nf-2nf
tags:
- mapping
- schema-design
- conversion
stage: formal-systems
status: validated
---

# Converting ER Diagrams to Relational Schemas

## Core Idea
Systematic rules convert each ER construct to relational tables: entity types become tables, attributes become columns, relationships become foreign keys or junction tables based on cardinality, weak entities create composite keys, and specialization hierarchies use either single tables with type discriminators or multiple related tables. Understanding these mappings ensures sound database design that properly represents requirements.

## Questions

```yaml
- question: "A university ER diagram has a many-to-many relationship between Student and Course, with an enrollment date as a relationship attribute. Which relational schema correctly represents this?"
  type: multiple-choice
  options:
    - "Add a course_id foreign key to the Student table and store enrollment_date there"
    - "Add a student_id foreign key to the Course table and store enrollment_date there"
    - "Create a junction table Enrollment(student_id FK, course_id FK, enrollment_date) with a composite primary key"
    - "Store both student_id and course_id as a comma-separated list in a single Enrollment column"
  answer: 2
  explanation: "Many-to-many relationships require a junction table because neither side can hold the other's foreign key without duplicating rows. The junction table's composite primary key (student_id, course_id) uniquely identifies each pairing, and relationship attributes like enrollment_date become additional columns. Options A and B each force one side to repeat rows for every pairing, violating relational design. Option D violates first normal form — you cannot store multiple values in one cell."

- question: "A Student entity has a 'phones' attribute that can hold multiple phone numbers. How should this be mapped to a relational schema?"
  type: multiple-choice
  options:
    - "Add a phones column to the Student table storing all numbers separated by commas"
    - "Create a separate StudentPhone(student_id FK, phone) table"
    - "Add phone1, phone2, phone3 columns to Student to accommodate up to three numbers"
    - "Omit phone numbers entirely — multivalued attributes cannot be represented relationally"
  answer: 1
  explanation: "Multivalued attributes require their own table with a foreign key back to the parent entity. Storing all values in one cell (option A) or in fixed columns (option C) both violate first normal form, making it impossible to cleanly query for a specific phone number or handle an arbitrary number of phones. Option D is wrong — the separate table approach is exactly how multivalued attributes are handled."

- question: "A one-to-many relationship between Department and Employee is correctly represented by adding a dept_id foreign key to the Employee table, with no separate junction table required."
  type: true-false
  answer: true
  explanation: "For a 1:N relationship, the 'many' side holds the foreign key. Each Employee row stores a dept_id referencing one Department row, while many Employee rows can reference the same Department — exactly the 1:N semantics. Junction tables are needed only for M:N relationships, where neither side can hold the other's key without repeating rows. Creating a junction table for a 1:N relationship is unnecessary complexity."

- question: "When converting a specialization hierarchy (e.g., Person → Student, Faculty) to a relational schema, the main correct approach is to create a separate table for each entity type in the hierarchy."
  type: true-false
  answer: false
  explanation: "There are three valid strategies: (1) a single table with a type discriminator column and nullable subclass attributes; (2) separate tables for each subclass that include all superclass attributes; or (3) a superclass table joined to subclass tables via shared primary key. Each has tradeoffs — single-table avoids joins but wastes space with nulls; separate joined tables are cleaner when subclasses have many distinct attributes. The right choice depends on query patterns and schema requirements."

- question: "Explain the difference between how a one-to-many and a many-to-many relationship are represented in a relational schema, and why this difference is necessary."
  type: short-answer
  answer: "In a 1:N relationship, the 'many' side's table gets a foreign key column pointing to the 'one' side's primary key — no new table needed. In an M:N relationship, neither side can hold the other's key without repeating rows, so a junction table is created with foreign keys to both sides, forming a composite primary key. The difference is necessary because the relational model stores one value per cell: a cell cannot hold a list of IDs."
  explanation: "The relational model's fundamental constraint — one atomic value per cell — is why M:N needs a junction table. If a student can enroll in many courses, you can't store all course IDs in one Student row cell (that's a non-atomic value). And you can't store all student IDs in one Course cell. The junction table represents every pairing as its own row, which is the only way to handle arbitrary M:N relationships without violating 1NF or duplicating data."
```

## Explainer

You already know how to draw ER diagrams with entities, attributes, and relationships, and you understand the relational model — tables with rows, columns, primary keys, and foreign keys. The conversion process is a systematic set of rules that translates every construct in an ER diagram into relational tables. Once you internalize these rules, you can mechanically convert any ER design into a working database schema.

The simplest rule handles **strong entities**: each entity type becomes a table, each attribute becomes a column, and the entity's key attribute becomes the primary key. An entity "Student" with attributes student_id, name, and email becomes a table `Student(student_id PK, name, email)`. **Multivalued attributes** cannot be stored in a single column (that would violate first normal form), so they get their own table with a foreign key back to the parent entity. A student with multiple phone numbers produces a separate `StudentPhone(student_id FK, phone)` table. **Composite attributes** are flattened — an "address" composed of street, city, and zip becomes three separate columns. **Derived attributes** (like age computed from birth_date) are typically omitted from the schema and calculated at query time.

**Relationships** are where cardinality drives the design. For a **one-to-many** relationship (one department has many employees), you add the primary key of the "one" side as a foreign key in the "many" side's table — `Employee` gets a `dept_id` foreign key pointing to `Department`. No separate table is needed. For a **many-to-many** relationship (students enroll in courses), neither side can hold the foreign key alone, so you create a **junction table** (also called an association or bridge table) containing the primary keys of both entities as foreign keys: `Enrollment(student_id FK, course_id FK)`. Together these form the junction table's composite primary key. Any attributes of the relationship itself (like enrollment_date or grade) become additional columns in the junction table. For **one-to-one** relationships, you place the foreign key on either side — typically the side with total participation, where every row must participate in the relationship.

**Weak entities** depend on a strong entity for identification. A "Dependent" identified by (employee_id, dependent_name) becomes a table whose primary key is the composite of the owning entity's key and the weak entity's partial key, with the owner's key also serving as a foreign key. **Specialization hierarchies** (like "Person" specialized into "Student" and "Faculty") offer three mapping strategies: a single table with a type discriminator column and nullable columns for subclass-specific attributes; separate tables for each subclass that include the superclass attributes; or a superclass table joined to subclass tables sharing the same primary key. The choice depends on query patterns — the single-table approach avoids joins but wastes space with nulls, while separate tables are cleaner when subclasses have many distinct attributes.
