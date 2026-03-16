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

## Explainer

Normalization is a disciplined process for structuring relational tables to avoid redundancy and the data anomalies that come with it. You already understand functional dependencies — the idea that one set of attributes uniquely determines another. Normalization uses functional dependencies as the diagnostic tool: wherever you find a dependency that violates a normal form's rules, you decompose the table to fix it.

Consider a flat table tracking student course enrollments: StudentID, StudentName, CourseID, CourseName, InstructorName. If a student takes three courses, their name is stored three times. If you update the student's name in one row but not the others, you have an **update anomaly**. If you delete the student's last enrollment, you lose the student's name entirely — a **deletion anomaly**. If you want to record a new student who hasn't enrolled yet, you can't without a CourseID — an **insertion anomaly**. These anomalies are the symptoms that normalization cures.

**First Normal Form (1NF)** requires that every cell contains a single, atomic value — no lists, no sets, no repeating groups. A table that stores a student's courses as "CS101, CS102, CS103" in one cell violates 1NF. The fix is to create separate rows: one per student-course pair. This seems basic, but it is the foundation everything else builds on. Without atomic values, you cannot write reliable queries (how do you JOIN on a comma-separated list?) or enforce constraints (how do you set a foreign key on one item in a list?).

**Second Normal Form (2NF)** eliminates **partial dependencies** — situations where a non-key attribute depends on only part of a composite primary key. In our enrollment table with composite key (StudentID, CourseID), StudentName depends only on StudentID and CourseName depends only on CourseID. These are partial dependencies: the non-key attributes don't need the full key to be determined. The fix is to decompose into three tables: Students(StudentID, StudentName), Courses(CourseID, CourseName, InstructorName), and Enrollments(StudentID, CourseID). Now each fact is stored exactly once, eliminating the update anomalies. Note that 2NF only applies when the primary key is composite — a table with a single-column primary key cannot have partial dependencies and is automatically in 2NF.
