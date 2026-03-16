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
status: validated
---

# Entity-Relationship Diagrams

## Core Idea
Entity-Relationship (ER) diagrams are a visual tool for modeling the conceptual structure of a database before implementation. Entities represent real-world objects (e.g., Student, Course), attributes describe their properties, and relationships capture how entities associate with one another. Cardinality annotations (one-to-one, one-to-many, many-to-many) specify how many instances of each entity can participate in a relationship. ER diagrams are later translated into relational schemas during logical design.

## How It's Best Learned
Model a familiar domain (e.g., a library system with Books, Members, and Loans) by drawing entities and relationships first, then convert to tables. Practice distinguishing weak entities, identifying keys, and resolving many-to-many relationships via junction tables.

## Common Misconceptions
- Attributes that look like relationships (storing a customer's city as a string vs. linking to a Cities table) are a common design error.
- Many-to-many relationships must be resolved into a junction (associative) table in the relational model — they cannot be represented directly.

## Explainer

Before you write any SQL or create any tables, you need a way to think about the structure of your data at a conceptual level. **Entity-Relationship (ER) diagrams** provide that thinking tool. They let you map out what things exist in your domain, what properties those things have, and how they relate to each other — all before committing to any particular database implementation. You already understand the relational model's tables, rows, and columns; ER diagrams operate one level above that, capturing the real-world structure that tables will eventually represent.

An **entity** is any distinct "thing" you need to track — a Student, a Course, an Order, a Product. Each entity has **attributes**: a Student might have a student_id, name, and enrollment_date. One attribute (or combination) serves as the **primary key**, uniquely identifying each instance. Entities are drawn as rectangles, attributes as ovals connected to their entity. A **relationship** describes how entities associate: a Student *enrolls in* a Course, an Employee *works for* a Department. Relationships are drawn as diamonds connecting the relevant entity rectangles.

The most important annotation on a relationship is its **cardinality** — how many instances of each entity can participate. A Department *has* many Employees, but each Employee *belongs to* one Department: that is a **one-to-many** (1:N) relationship. A Student can enroll in many Courses, and a Course can have many Students: that is a **many-to-many** (M:N) relationship. One-to-one (1:1) relationships are rarer but occur when two entities have a strict pairing, like an Employee and their single Parking Permit. Cardinality determines how the ER diagram translates to tables: one-to-many relationships are implemented with a foreign key on the "many" side, while many-to-many relationships require a separate **junction table** (also called an associative or bridge table) that holds foreign keys to both entities.

Translating an ER diagram into a relational schema is a methodical process. Each entity becomes a table. Each attribute becomes a column. Each one-to-many relationship adds a foreign key column to the "many" side table. Each many-to-many relationship becomes its own table with two foreign key columns (and potentially additional attributes — for example, an Enrollment junction table between Student and Course might include a grade and enrollment_date). **Weak entities** — entities that cannot be uniquely identified without their parent's key (like a Room that is only unique within a Building) — become tables whose primary key includes the parent's foreign key. Practicing this translation on familiar domains — a library with books, members, and loans; an online store with customers, orders, and products — builds the skill of moving fluidly between conceptual models and physical schemas.
