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

## Questions

```yaml
- question: "A table has composite primary key (StudentID, CourseID) and includes the attribute InstructorEmail, which depends only on CourseID. This violates which normal form?"
  type: multiple-choice
  options:
    - "First Normal Form — because InstructorEmail may contain non-atomic values"
    - "Second Normal Form — because InstructorEmail has a partial dependency on the key"
    - "Third Normal Form — because InstructorEmail depends on a non-key attribute"
    - "No normal form is violated — a non-key attribute may depend on any part of the key"
  answer: 1
  explanation: "InstructorEmail depends only on CourseID, not on the full composite key (StudentID, CourseID). This is a partial dependency — the defining violation of 2NF. The fix is to move InstructorEmail to a separate Courses table where CourseID is the sole primary key, so each instructor's email is stored once. If left in the enrollment table, updating an instructor's email requires updating every row for that course — a classic update anomaly."

- question: "In a flat enrollment table, a student's only course enrollment is deleted to record a withdrawal. As a side effect, the student's name and contact information are also lost. This is an example of:"
  type: multiple-choice
  options:
    - "An update anomaly — the same data exists in multiple places and only one copy was updated"
    - "An insertion anomaly — new data cannot be inserted without providing unrelated information"
    - "A deletion anomaly — deleting one fact unintentionally destroys another unrelated fact"
    - "A 1NF violation — the row contained multiple values in a single column"
  answer: 2
  explanation: "A deletion anomaly occurs when removing one logical fact (the enrollment) inadvertently destroys another (the student's identity information), because both facts are entangled in the same row. This is a direct consequence of redundant storage — the student's name is only recorded via their enrollments, not in a dedicated Students table. Normalization to 2NF resolves this by separating student data from enrollment data so each fact lives in exactly one place."

- question: "A table with a single-column primary key can still violate Second Normal Form if non-key attributes depend on only part of that key."
  type: true-false
  answer: false
  explanation: "Partial dependencies — the 2NF violation — can only exist when the primary key is composite (two or more columns). A partial dependency means a non-key attribute depends on a proper subset of the key. With a single-column key, there are no proper subsets, so partial dependencies are structurally impossible. Tables with single-column primary keys are automatically in 2NF, though they can still violate 3NF if a non-key attribute depends on another non-key attribute."

- question: "Storing a student's enrolled courses as 'CS101, CS202, CS303' in a single column violates First Normal Form."
  type: true-false
  answer: true
  explanation: "1NF requires each cell to contain exactly one atomic, indivisible value. A comma-separated list in a single column stores multiple values as a single string, violating atomicity. This makes the data very difficult to work with: you cannot JOIN on individual courses, cannot set foreign key constraints on individual values, and queries require string-splitting logic. The fix is to create one row per student-course combination, where each cell holds a single CourseID."

- question: "What is a partial dependency, and why does it cause update anomalies in a database table?"
  type: short-answer
  answer: "A partial dependency occurs when a non-key attribute depends on only part of a composite primary key rather than the entire key. For example, if CourseName depends only on CourseID in a table with key (StudentID, CourseID), CourseName is stored redundantly in every row for that course. An update anomaly results: if the course name changes, every row containing that CourseID must be updated individually. If even one row is missed, the database contains conflicting values for the same fact — an inconsistency that normalization is designed to prevent."
  explanation: "The deeper issue is that partial dependencies encode two independent facts in one row: facts about the enrollment relationship AND facts about the course itself. 2NF separates these by decomposing the table so each fact lives in exactly one place. This 'one fact, one place' principle is why normalization eliminates anomalies: there is no longer a second copy to forget to update, no enrollment row to delete that takes course information with it."
```

## Explainer

Normalization is a disciplined process for structuring relational tables to avoid redundancy and the data anomalies that come with it. You already understand functional dependencies — the idea that one set of attributes uniquely determines another. Normalization uses functional dependencies as the diagnostic tool: wherever you find a dependency that violates a normal form's rules, you decompose the table to fix it.

Consider a flat table tracking student course enrollments: StudentID, StudentName, CourseID, CourseName, InstructorName. If a student takes three courses, their name is stored three times. If you update the student's name in one row but not the others, you have an **update anomaly**. If you delete the student's last enrollment, you lose the student's name entirely — a **deletion anomaly**. If you want to record a new student who hasn't enrolled yet, you can't without a CourseID — an **insertion anomaly**. These anomalies are the symptoms that normalization cures.

**First Normal Form (1NF)** requires that every cell contains a single, atomic value — no lists, no sets, no repeating groups. A table that stores a student's courses as "CS101, CS102, CS103" in one cell violates 1NF. The fix is to create separate rows: one per student-course pair. This seems basic, but it is the foundation everything else builds on. Without atomic values, you cannot write reliable queries (how do you JOIN on a comma-separated list?) or enforce constraints (how do you set a foreign key on one item in a list?).

**Second Normal Form (2NF)** eliminates **partial dependencies** — situations where a non-key attribute depends on only part of a composite primary key. In our enrollment table with composite key (StudentID, CourseID), StudentName depends only on StudentID and CourseName depends only on CourseID. These are partial dependencies: the non-key attributes don't need the full key to be determined. The fix is to decompose into three tables: Students(StudentID, StudentName), Courses(CourseID, CourseName, InstructorName), and Enrollments(StudentID, CourseID). Now each fact is stored exactly once, eliminating the update anomalies. Note that 2NF only applies when the primary key is composite — a table with a single-column primary key cannot have partial dependencies and is automatically in 2NF.
