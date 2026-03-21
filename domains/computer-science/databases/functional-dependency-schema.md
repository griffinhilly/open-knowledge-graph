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

## Questions

```yaml
- question: "You examine a table of student enrollments and observe that, in the current dataset, every student_id value happens to correspond to exactly one department. Does this mean student_id → department is a functional dependency of the schema?"
  type: multiple-choice
  options:
    - "Yes — if the current data shows no violations, the FD holds"
    - "No — an FD is a constraint on all valid states of the relation, not just a pattern in current data; future insertions could violate it"
    - "Yes — functional dependencies are always derived from the data that exists in the table"
    - "It depends on whether student_id is the primary key"
  answer: 1
  explanation: "A functional dependency is a semantic constraint that must hold for ALL valid states of the table, including future insertions and updates — it is part of the schema design, not a description of current data. A table that currently shows no violations may simply not yet contain the row that would violate the constraint. FDs must be declared based on domain knowledge (e.g., business rules, real-world constraints), not inferred from observed data. This is the most common misconception about functional dependencies."

- question: "In a table with attributes {student_id, course_id, grade, student_name}, the functional dependencies are: student_id → student_name, and {student_id, course_id} → grade. What is the candidate key?"
  type: multiple-choice
  options:
    - "student_id, because it determines student_name"
    - "{student_id, course_id}, because it determines grade and student_name (transitively via student_id)"
    - "student_name, because names are unique"
    - "grade, because grades distinguish rows"
  answer: 1
  explanation: "A candidate key is a minimal superkey — a minimal set of attributes that determines all others. {student_id, course_id} determines grade directly, and determines student_name via student_id → student_name (transitivity). Neither student_id alone (doesn't determine grade) nor course_id alone (determines nothing) is sufficient. So {student_id, course_id} is the minimal set that determines everything — the candidate key. student_id is a partial key, not a full candidate key for this table."

- question: "A functional dependency A → B means that for any two rows in the table that have the same value in column A, they must also have the same value in column B."
  type: true-false
  answer: true
  explanation: "This is the precise definition of a functional dependency. If you see two rows with the same A value but different B values, the FD A → B is violated. This constraint captures the intuition that 'knowing A tells you B' — there is no ambiguity or choice involved. For example, student_id → student_name means two rows with the same student_id cannot have different student_names, because a student has exactly one name."

- question: "If the closure of attribute set X (written X⁺) equals the set of all attributes in the table, then X is guaranteed to be a candidate key."
  type: true-false
  answer: false
  explanation: "X⁺ = all attributes means X is a SUPERKEY — it determines everything. But a candidate key must also be MINIMAL: no proper subset of X can also determine all attributes. For example, if {A, B} determines all attributes but A alone also determines all attributes, then {A, B} is a superkey but not a candidate key (since A alone suffices). Computing closure tells you whether X is a superkey; checking minimality — by testing whether any proper subset of X is also a superkey — is the additional step needed to identify candidate keys."

- question: "What is the difference between a superkey and a candidate key, and why does the distinction matter for normalization?"
  type: short-answer
  answer: "A superkey is any set of attributes that functionally determines all other attributes. A candidate key is a minimal superkey — no proper subset of it is also a superkey. The distinction matters because normalization requires reasoning about what attributes depend on the WHOLE key versus only part of it; you can only detect partial dependencies (2NF violations) if you know which minimal subsets are keys."
  explanation: "If you use a superkey that is not minimal, you may incorrectly conclude that certain dependencies are 'on the whole key' when in fact they depend on only part of it. For example, if {A, B, C} is your primary key but A alone is also a superkey, then any attribute determined by A alone is only partially dependent on {A, B, C} — a 2NF violation. Finding true candidate keys (minimal superkeys) is what makes normalization analysis meaningful and reliable."
```

## Explainer

A **functional dependency** (FD) is a constraint on data: if you know the value of one set of attributes, you can determine the value of another. Written A → B, it means "for any two rows that agree on A, they must also agree on B." This is not a statement about a particular dataset — it is a rule about all possible valid states of the table. For example, in a student enrollment table, `student_id → student_name` says that a student ID always maps to the same name. Two rows with the same student_id cannot have different student_names. You already know from the relational model that primary keys uniquely identify rows; functional dependencies are the formal tool that explains why.

A **superkey** is any set of attributes that functionally determines all other attributes in the table — knowing the superkey values, you can determine the entire row. A **candidate key** is a minimal superkey: no proper subset of it is also a superkey. For example, if `{student_id, course_id}` determines every attribute in an enrollment table, and neither `student_id` alone nor `course_id` alone does, then `{student_id, course_id}` is a candidate key. The primary key you choose is one of the candidate keys. Finding candidate keys from a set of FDs is a mechanical process: compute the closure of every attribute subset (the set of all attributes it determines, following transitivity) and identify which minimal subsets determine everything.

FDs follow **Armstrong's axioms**, which let you derive new dependencies from known ones. **Reflexivity**: if B is a subset of A, then A → B (trivially). **Augmentation**: if A → B, then AC → BC. **Transitivity**: if A → B and B → C, then A → C. From these three, you can derive all implied FDs. The **closure** of an attribute set X (written X⁺) is the set of all attributes determined by X under the given FDs. Computing closures is how you systematically answer questions like "is this a candidate key?" or "does this FD follow from the others?"

The practical payoff is in normalization. Redundancy in a table arises when a non-key attribute depends on only part of the key (violating second normal form) or on another non-key attribute (violating third normal form). Functional dependencies make these problems precise and detectable. Instead of guessing whether a schema "feels" redundant, you list the FDs, compute candidate keys, and check whether every non-key attribute depends on the whole key and nothing but the key. This mechanical analysis is what guides decomposition into well-structured tables — the foundation of sound database design.
