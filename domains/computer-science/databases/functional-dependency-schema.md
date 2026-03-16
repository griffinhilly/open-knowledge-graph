---
id: functional-dependency-schema
title: Functional Dependencies and Database Design
domain: computer-science
course: databases
prerequisites:
- id: relational-data-model
  type: hard
- id: primary-key-foreign-key-constraints
  type: soft
builds-toward:
- normalization-first-second-third
tags:
- functional dependency
- FD
- candidate key
- superkey
stage: formal-systems
status: draft
---

# Functional Dependencies and Database Design

## Core Idea
A functional dependency (FD) is a constraint stating that if two rows have the same value in attribute A, they must have the same value in attribute B (written A → B). Functional dependencies identify candidate keys and guide normalization. Understanding FDs is essential for eliminating data redundancy.

## How It's Best Learned
Identify functional dependencies in real-world scenarios, determine candidate keys from FD sets, and use FD analysis to guide schema design toward higher normal forms.

## Explainer

A **functional dependency** (FD) is a constraint on data: if you know the value of one set of attributes, you can determine the value of another. Written A → B, it means "for any two rows that agree on A, they must also agree on B." This is not a statement about a particular dataset — it is a rule about all possible valid states of the table. For example, in a student enrollment table, `student_id → student_name` says that a student ID always maps to the same name. Two rows with the same student_id cannot have different student_names. You already know from the relational model that primary keys uniquely identify rows; functional dependencies are the formal tool that explains why.

A **superkey** is any set of attributes that functionally determines all other attributes in the table — knowing the superkey values, you can determine the entire row. A **candidate key** is a minimal superkey: no proper subset of it is also a superkey. For example, if `{student_id, course_id}` determines every attribute in an enrollment table, and neither `student_id` alone nor `course_id` alone does, then `{student_id, course_id}` is a candidate key. The primary key you choose is one of the candidate keys. Finding candidate keys from a set of FDs is a mechanical process: compute the closure of every attribute subset (the set of all attributes it determines, following transitivity) and identify which minimal subsets determine everything.

FDs follow **Armstrong's axioms**, which let you derive new dependencies from known ones. **Reflexivity**: if B is a subset of A, then A → B (trivially). **Augmentation**: if A → B, then AC → BC. **Transitivity**: if A → B and B → C, then A → C. From these three, you can derive all implied FDs. The **closure** of an attribute set X (written X⁺) is the set of all attributes determined by X under the given FDs. Computing closures is how you systematically answer questions like "is this a candidate key?" or "does this FD follow from the others?"

The practical payoff is in normalization. Redundancy in a table arises when a non-key attribute depends on only part of the key (violating second normal form) or on another non-key attribute (violating third normal form). Functional dependencies make these problems precise and detectable. Instead of guessing whether a schema "feels" redundant, you list the FDs, compute candidate keys, and check whether every non-key attribute depends on the whole key and nothing but the key. This mechanical analysis is what guides decomposition into well-structured tables — the foundation of sound database design.
