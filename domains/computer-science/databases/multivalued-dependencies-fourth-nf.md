---
id: multivalued-dependencies-fourth-nf
title: Multivalued Dependencies and Fourth Normal Form
domain: computer-science
course: databases
prerequisites:
- id: database-normalization-3nf-bcnf
  type: hard
- id: functional-dependencies
  type: hard
builds-toward:
- join-dependencies-fifth-nf
tags:
- 4NF
- multivalued-dependencies
- MVD
- normalization
stage: advanced
status: validated
---

# Multivalued Dependencies and Fourth Normal Form

## Core Idea
Multivalued dependencies occur when one column determines multiple independent set-valued attributes: if a course has independent lists of instructors and textbooks, storing all combinations creates redundancy and update anomalies. Fourth Normal Form (4NF) requires all non-trivial MVDs to also be functional dependencies. A relation in BCNF might still violate 4NF, requiring decomposition into separate relations.

## Questions

```yaml
- question: "A table has schema (Course, Instructor, Textbook). Course CS101 has instructors {Smith, Jones} and textbooks {Algorithms, Data Structures}. How many rows must this table contain for CS101?"
  type: multiple-choice
  options:
    - "2 rows — one per instructor, with textbook nullable"
    - "2 rows — one per textbook, with instructor nullable"
    - "4 rows — every instructor-textbook combination must appear"
    - "3 rows — one for the course plus one per instructor and one per textbook"
  answer: 2
  explanation: "Because instructors and textbooks are independently associated with the course (not with each other), the table must store every combination to avoid implying false associations. With 2 instructors and 2 textbooks, that's 2×2 = 4 rows. This cross-product explosion is caused by storing two independent multivalued dependencies in a single relation. 4NF decomposition eliminates this: split into (Course, Instructor) with 2 rows and (Course, Textbook) with 2 rows."

- question: "A table with schema (Employee, Skill, Language) is in BCNF. You notice that an employee's skills and languages are assigned independently. What should you do?"
  type: multiple-choice
  options:
    - "Nothing — BCNF is the highest practically relevant normal form"
    - "Decompose into (Employee, Skill) and (Employee, Language) to achieve 4NF"
    - "Add a foreign key linking Skill to Language to establish a functional dependency"
    - "Combine Skill and Language into a single composite attribute"
  answer: 1
  explanation: "Independent multivalued dependencies (Employee →→ Skill and Employee →→ Language) cause cross-product redundancy that BCNF cannot detect — BCNF only addresses functional dependencies. The fix is decomposition into two relations, each recording one independent fact. Adding a foreign key (option C) would create a false dependency that doesn't exist. Option A is wrong because BCNF is insufficient when independent MVDs are present."

- question: "A relation that is in BCNF cannot have update anomalies."
  type: true-false
  answer: false
  explanation: "BCNF eliminates anomalies caused by functional dependencies, but multivalued dependencies create a different kind of anomaly that BCNF cannot detect. In a table with independent MVDs (like Course-Instructor-Textbook), adding a new instructor requires adding one row per textbook — an update anomaly driven by the cross-product structure. Only 4NF addresses this. BCNF is necessary but not sufficient for eliminating all redundancy-based anomalies."

- question: "The multivalued dependency A →→ B means that for each value of A, the set of B values is determined by A alone, independently of other attributes in the relation."
  type: true-false
  answer: true
  explanation: "This is the definition of an MVD: A →→ B means the set of B values associated with a given A value is independent of the other attributes. In the Course-Instructor-Textbook example, Course →→ Instructor means the set of instructors for CS101 is determined by the course alone, not by which textbook is also in the row. This independence causes the cross-product explosion — the sets for A →→ B and A →→ C must be listed in every combination."

- question: "Explain why BCNF normalization is insufficient to eliminate all redundancy caused by multivalued dependencies, using a concrete example."
  type: short-answer
  answer: "BCNF only catches violations caused by functional dependencies (where a non-key attribute determines another). In a relation like (Course, Instructor, Textbook), the key is {Course, Instructor, Textbook} and no non-key determines another — no FD is violated, so BCNF is satisfied. But if CS101 has 3 instructors and 4 textbooks independently, the table must store 12 rows. Adding a new textbook means adding 3 rows (one per instructor) — a redundancy-driven update anomaly that BCNF misses entirely because it stems from independent MVDs, not FDs."
  explanation: "The conceptual gap is that BCNF addresses single-valued facts (one value per key), while MVDs address multi-valued facts (sets per key). When two independent multi-valued facts share a table, they multiply. 4NF catches this by requiring every non-trivial MVD's determinant to be a superkey, and decomposition separates the independent facts into tables where each row represents exactly one association."
```

## Explainer

You've seen how functional dependencies (A → B means each A value maps to exactly one B value) drive normalization through BCNF. But functional dependencies only capture single-valued relationships. A **multivalued dependency** (MVD) captures a different pattern: one attribute independently determines a *set* of values for another attribute. The notation is A →→ B, read "A multi-determines B." The classic example is a Course that has a set of Instructors and an independent set of Textbooks. Course →→ Instructor and Course →→ Textbook are both MVDs — each course is associated with multiple instructors and multiple textbooks, and these two sets are independent of each other.

The problem appears when you try to store both relationships in a single table. If course CS101 has instructors {Smith, Jones} and textbooks {Algorithms, Data Structures}, you must store all four combinations: (CS101, Smith, Algorithms), (CS101, Smith, Data Structures), (CS101, Jones, Algorithms), (CS101, Jones, Data Structures). This **cross-product explosion** is pure redundancy — adding a third instructor means adding two new rows (one per textbook), and forgetting a row creates a spurious association. These are exactly the kinds of update anomalies that normalization is designed to prevent, but BCNF cannot detect them because no functional dependency is violated. The key has no partial or transitive FD issues — the problem is that two independent facts are being multiplied together.

**Fourth Normal Form** (4NF) addresses this by requiring that for every non-trivial multivalued dependency A →→ B, A must be a superkey. Since Course is not a superkey of the three-column table (the key is {Course, Instructor, Textbook}), the MVD Course →→ Instructor violates 4NF. The fix is decomposition: split into (Course, Instructor) and (Course, Textbook). Now each fact is stored once, the cross-product redundancy vanishes, and adding a new instructor requires only one new row. The original data can be reconstructed by joining the two tables on Course.

A practical way to detect MVDs is to ask: "Are these two attributes independently associated with the key, or does knowing one tell you something about the other?" If instructors and textbooks are assigned independently — any instructor might use any textbook — you have independent MVDs and should decompose. If there's a real association (instructor Smith always uses Algorithms), that's a functional relationship, not an MVD, and the table structure is fine. Most real-world schemas reach 3NF or BCNF and stop, but MVD violations do arise in practice, particularly in systems that model entities with multiple independent multi-valued attributes like skills, certifications, or product features.
