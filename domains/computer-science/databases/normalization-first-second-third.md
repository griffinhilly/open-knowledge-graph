---
id: normalization-first-second-third
title: Database Normalization (1NF, 2NF, 3NF)
domain: computer-science
course: databases
prerequisites:
- id: functional-dependency-schema
  type: hard
builds-toward:
- bcnf-higher-normalization
- denormalization-strategy
tags:
- normalization
- 1NF
- 2NF
- 3NF
- redundancy
stage: formal-systems
status: draft
---

# Database Normalization (1NF, 2NF, 3NF)

## Core Idea
Normalization is the process of organizing data to eliminate redundancy and improve integrity. First Normal Form (1NF) requires atomic attributes. Second Normal Form (2NF) eliminates partial dependencies on composite keys. Third Normal Form (3NF) eliminates transitive dependencies. Each higher form builds on the previous, reducing data anomalies.

## How It's Best Learned
Take denormalized schemas with redundancy and step through 1NF, 2NF, 3NF decomposition. Understand the problems each normal form solves: insertion/deletion/update anomalies and inconsistency.

## Questions

```yaml
- question: "A table has composite key (student_id, course_id) and includes columns: student_id, course_id, student_name, grade. Which normal form violation does this table have?"
  type: multiple-choice
  options:
    - "1NF violation — student_name is not an atomic value"
    - "2NF violation — student_name depends only on student_id, not the full composite key"
    - "3NF violation — student_name transitively depends on grade"
    - "No violation — the table is already in 3NF"
  answer: 1
  explanation: "student_name depends only on student_id (a partial key), not on the full composite key (student_id, course_id). This partial dependency is exactly what 2NF prohibits. The consequence: every time a student enrolls in a new course, student_name is repeated in a new row, and updating the name in one row but not others creates inconsistency. The fix is to move student_name into a separate Student table keyed by student_id alone. Note: grade depends on the full key (a specific student in a specific course) and is not a violation."

- question: "A table has primary key student_id and columns: student_id, department, department_head. The dependency chain is: student_id → department → department_head. What violation does this represent?"
  type: multiple-choice
  options:
    - "1NF violation — department_head is not atomic"
    - "2NF violation — department is a partial dependency on the primary key"
    - "3NF violation — department_head transitively depends on student_id through a non-key attribute (department)"
    - "No violation — transitive dependencies are permitted in normalized schemas"
  answer: 2
  explanation: "department_head depends on department (a non-key attribute), not directly on student_id (the primary key). This transitive chain — key → non-key → non-key — is what 3NF prohibits. The result: every student in the same department duplicates the department_head value; a single leadership change requires updating every such row. Note: option B is wrong because 2NF only addresses partial dependencies in composite keys, and student_id is a simple (single-column) key here — so the table is already in 2NF."

- question: "Second Normal Form (2NF) applies to any table with redundant data, regardless of whether its primary key is a single column or a composite key."
  type: true-false
  answer: false
  explanation: "2NF specifically addresses partial dependencies, which by definition can only exist when the primary key is composite (multi-column). A non-key attribute can only be partially dependent if it depends on *part* of a composite key. A table with a single-column primary key has no composite key to be partially dependent on — it is automatically in 2NF once it satisfies 1NF. Applying 2NF logic to single-key tables is a common misconception."

- question: "Decomposing a table to eliminate a transitive dependency (achieving 3NF) removes the update anomaly where changing one fact requires editing multiple rows."
  type: true-false
  answer: true
  explanation: "This is precisely the purpose of 3NF normalization. A transitive dependency means one value (e.g., department_head) is stored redundantly across many rows. If the department head changes, every row for students in that department must be updated — one update anomaly. Decomposition creates a Department table where department_head appears exactly once. Now a leadership change requires updating a single row, and the anomaly is eliminated."

- question: "Explain the difference between a partial dependency (2NF violation) and a transitive dependency (3NF violation), and describe the data anomaly each causes."
  type: short-answer
  answer: "A partial dependency occurs when a non-key attribute depends on only part of a composite primary key (e.g., student_name depends on student_id alone in a table keyed by student_id + course_id). Each new enrollment row repeats the student_name, and updating it inconsistently across rows creates conflicting data. A transitive dependency occurs when a non-key attribute depends on another non-key attribute rather than directly on the primary key (e.g., department_head depends on department, which depends on student_id). The same department_head value is repeated for every student in that department; changing the head requires updating all those rows. Both are eliminated by decomposition: move the dependent attributes into a new table where they depend directly on their own key."
  explanation: "The unifying principle of normalization through 3NF is the classic mnemonic: every non-key attribute must depend on 'the key, the whole key, and nothing but the key.' Partial dependencies violate 'the whole key'; transitive dependencies violate 'nothing but the key.' Each violation creates a specific kind of redundancy that leads to insertion, update, or deletion anomalies."
```

## Explainer

You already understand functional dependencies — the idea that one attribute uniquely determines another (e.g., student_id → student_name). Normalization uses functional dependencies to systematically restructure tables, eliminating redundancy that causes **anomalies**: situations where inserting, updating, or deleting data leads to inconsistencies. Each normal form addresses a specific type of redundancy, and each builds on the one before it.

**First Normal Form (1NF)** requires that every column holds a single, atomic value — no lists, sets, or nested tables within a cell. Consider a table where a student's courses are stored as a comma-separated string: "Math, Physics, CS". This violates 1NF because querying for all students in Physics requires string parsing, and adding or removing a course means editing a string rather than inserting or deleting a row. The fix is to ensure each cell contains exactly one value. Typically this means creating a separate row for each student-course pair, or better, splitting courses into a separate related table. Once your table is in 1NF, every value is independently addressable by SQL.

**Second Normal Form (2NF)** eliminates **partial dependencies** — attributes that depend on only part of a composite primary key. This only applies to tables with composite keys. Suppose a table has the composite key (student_id, course_id) and also contains student_name. Since student_name depends only on student_id (not on the full composite key), it is partially dependent. The consequence is redundancy: every time a student enrolls in another course, student_name is repeated. Update the name in one row but not another and you have an inconsistency. The fix is decomposition: move student_name into a separate Student table keyed by student_id alone, leaving the enrollment table with only attributes that depend on the full key (like grade or enrollment_date).

**Third Normal Form (3NF)** eliminates **transitive dependencies** — non-key attributes that depend on other non-key attributes rather than directly on the primary key. Suppose a table has key student_id with columns department and department_head. Here student_id → department and department → department_head, making department_head transitively dependent on student_id through department. The redundancy: every student in the same department stores the same department_head value. Change the department head and you must update every student row in that department. The fix is to create a Department table (department → department_head) and keep only the department foreign key in the Student table. After 3NF, every non-key attribute depends on "the key, the whole key, and nothing but the key" — the classic mnemonic that captures exactly what normalization through 3NF achieves.
