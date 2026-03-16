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
stage: formal-systems
status: draft
---

# Multivalued Dependencies and Fourth Normal Form

## Core Idea
Multivalued dependencies occur when one column determines multiple independent set-valued attributes: if a course has independent lists of instructors and textbooks, storing all combinations creates redundancy and update anomalies. Fourth Normal Form (4NF) requires all non-trivial MVDs to also be functional dependencies. A relation in BCNF might still violate 4NF, requiring decomposition into separate relations.

## Explainer

You've seen how functional dependencies (A → B means each A value maps to exactly one B value) drive normalization through BCNF. But functional dependencies only capture single-valued relationships. A **multivalued dependency** (MVD) captures a different pattern: one attribute independently determines a *set* of values for another attribute. The notation is A →→ B, read "A multi-determines B." The classic example is a Course that has a set of Instructors and an independent set of Textbooks. Course →→ Instructor and Course →→ Textbook are both MVDs — each course is associated with multiple instructors and multiple textbooks, and these two sets are independent of each other.

The problem appears when you try to store both relationships in a single table. If course CS101 has instructors {Smith, Jones} and textbooks {Algorithms, Data Structures}, you must store all four combinations: (CS101, Smith, Algorithms), (CS101, Smith, Data Structures), (CS101, Jones, Algorithms), (CS101, Jones, Data Structures). This **cross-product explosion** is pure redundancy — adding a third instructor means adding two new rows (one per textbook), and forgetting a row creates a spurious association. These are exactly the kinds of update anomalies that normalization is designed to prevent, but BCNF cannot detect them because no functional dependency is violated. The key has no partial or transitive FD issues — the problem is that two independent facts are being multiplied together.

**Fourth Normal Form** (4NF) addresses this by requiring that for every non-trivial multivalued dependency A →→ B, A must be a superkey. Since Course is not a superkey of the three-column table (the key is {Course, Instructor, Textbook}), the MVD Course →→ Instructor violates 4NF. The fix is decomposition: split into (Course, Instructor) and (Course, Textbook). Now each fact is stored once, the cross-product redundancy vanishes, and adding a new instructor requires only one new row. The original data can be reconstructed by joining the two tables on Course.

A practical way to detect MVDs is to ask: "Are these two attributes independently associated with the key, or does knowing one tell you something about the other?" If instructors and textbooks are assigned independently — any instructor might use any textbook — you have independent MVDs and should decompose. If there's a real association (instructor Smith always uses Algorithms), that's a functional relationship, not an MVD, and the table structure is fine. Most real-world schemas reach 3NF or BCNF and stop, but MVD violations do arise in practice, particularly in systems that model entities with multiple independent multi-valued attributes like skills, certifications, or product features.
