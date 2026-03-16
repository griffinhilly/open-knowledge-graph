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

## Explainer

You already understand functional dependencies — the idea that one attribute uniquely determines another (e.g., student_id → student_name). Normalization uses functional dependencies to systematically restructure tables, eliminating redundancy that causes **anomalies**: situations where inserting, updating, or deleting data leads to inconsistencies. Each normal form addresses a specific type of redundancy, and each builds on the one before it.

**First Normal Form (1NF)** requires that every column holds a single, atomic value — no lists, sets, or nested tables within a cell. Consider a table where a student's courses are stored as a comma-separated string: "Math, Physics, CS". This violates 1NF because querying for all students in Physics requires string parsing, and adding or removing a course means editing a string rather than inserting or deleting a row. The fix is to ensure each cell contains exactly one value. Typically this means creating a separate row for each student-course pair, or better, splitting courses into a separate related table. Once your table is in 1NF, every value is independently addressable by SQL.

**Second Normal Form (2NF)** eliminates **partial dependencies** — attributes that depend on only part of a composite primary key. This only applies to tables with composite keys. Suppose a table has the composite key (student_id, course_id) and also contains student_name. Since student_name depends only on student_id (not on the full composite key), it is partially dependent. The consequence is redundancy: every time a student enrolls in another course, student_name is repeated. Update the name in one row but not another and you have an inconsistency. The fix is decomposition: move student_name into a separate Student table keyed by student_id alone, leaving the enrollment table with only attributes that depend on the full key (like grade or enrollment_date).

**Third Normal Form (3NF)** eliminates **transitive dependencies** — non-key attributes that depend on other non-key attributes rather than directly on the primary key. Suppose a table has key student_id with columns department and department_head. Here student_id → department and department → department_head, making department_head transitively dependent on student_id through department. The redundancy: every student in the same department stores the same department_head value. Change the department head and you must update every student row in that department. The fix is to create a Department table (department → department_head) and keep only the department foreign key in the Student table. After 3NF, every non-key attribute depends on "the key, the whole key, and nothing but the key" — the classic mnemonic that captures exactly what normalization through 3NF achieves.
