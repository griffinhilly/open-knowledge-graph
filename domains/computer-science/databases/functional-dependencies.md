---
id: functional-dependencies
title: Functional Dependencies
domain: computer-science
course: databases
prerequisites:
- id: relational-model-basics
  type: hard
- id: primary-and-foreign-keys
  type: hard
- id: binary-relations
  type: soft
- id: logical-equivalence
  type: soft
- id: relations-properties-and-types
  type: soft
builds-toward:
- database-normalization-1nf-2nf
- database-normalization-3nf-bcnf
tags:
- functional dependencies
- keys
- candidate keys
- Armstrong's axioms
- normalization theory
stage: formal-systems
status: validated
---

# Functional Dependencies

## Core Idea
A functional dependency X → Y means the value of attribute set X uniquely determines the value of Y: any two tuples agreeing on X must agree on Y. Functional dependencies formalize the concept of a key — K is a superkey if K determines all attributes, and a candidate key if no proper subset of K also determines all attributes. Armstrong's axioms (reflexivity, augmentation, transitivity) form a sound and complete inference system for deriving all logical consequences of a given set of FDs.

## How It's Best Learned
Given a sample table with data anomalies (insertion, update, deletion), identify the functional dependencies that caused them. Practice computing attribute closures under a set of FDs to find all candidate keys.

## Common Misconceptions
- A functional dependency is a data constraint, not a causal relationship — it must hold for all possible instances, not just the current data.
- The left-hand side of an FD can be a set of multiple attributes.
- Having two tuples that happen to agree on X and Y in the current data does not prove X → Y — the FD must hold for all future data too.

## Questions

```yaml
- question: "A database table currently has the property that every row with ZipCode = '90210' also has City = 'Beverly Hills.' What can you conclude about the functional dependency ZipCode → City?"
  type: multiple-choice
  options:
    - "ZipCode → City holds — the data proves it"
    - "ZipCode → City may or may not hold — the current data is consistent with it, but an FD must hold for all possible future data"
    - "ZipCode → City definitely holds, because zip codes and cities have a one-to-one relationship"
    - "ZipCode → City holds only if ZipCode is the primary key"
  answer: 1
  explanation: "An FD is a constraint on all possible valid data, not an observation about current data. Today's table may happen to be consistent with ZipCode → City, but this proves nothing — someone could insert a new zip code with a different city, violating the constraint if it were declared. The FD is a design decision: you are declaring that your schema requires this relationship to always hold. Observing it in current data is necessary but not sufficient evidence that the FD is intended as a constraint."

- question: "In a student table, the FD StudentID → Name holds. A data-entry error creates two rows with the same StudentID but different Names. What is true?"
  type: multiple-choice
  options:
    - "The FD no longer holds — functional dependencies can change as data changes"
    - "The FD is violated — the data is inconsistent with the declared constraint"
    - "The FD still holds for all other rows, so the table is partially valid"
    - "This situation is impossible if StudentID is a primary key, so no FD is violated"
  answer: 1
  explanation: "If StudentID → Name is declared as an FD, then any two rows agreeing on StudentID must agree on Name — without exception. Two rows with the same StudentID and different Names violate this constraint. The FD is a declarative assertion about all valid states of the database; a violation means the data is in an invalid state. This is exactly the kind of anomaly that normalization prevents: the FD makes explicit what the data model requires, so violations can be detected and prevented."

- question: "A functional dependency X → Y means that knowing X causes Y to take a particular value in some physical or logical sense."
  type: true-false
  answer: false
  explanation: "False. An FD is a data constraint, not a causal relationship. X → Y means only that in any valid instance of the relation, two tuples agreeing on X must agree on Y. It says nothing about why — there is no causal mechanism implied. ZipCode → City holds in a postal database not because zip codes physically cause cities to exist, but because the data model declares that the postal system assigns each zip code to exactly one city. Confusing constraint with causation leads to errors in schema design."

- question: "A candidate key is a minimal superkey: it determines all attributes of the relation, and no proper subset of it also determines all attributes."
  type: true-false
  answer: true
  explanation: "True. A superkey K satisfies K → (all attributes). A candidate key is a superkey with no redundant attributes — remove any single attribute from it and it no longer determines everything. In practice, computing candidate keys requires finding the closure K⁺ under the given FDs: if K⁺ equals all attributes, K is a superkey; if no proper subset of K has this property, K is a candidate key. Primary keys are chosen from among the candidate keys."

- question: "Why does the distinction between 'an FD appearing to hold in current data' versus 'an FD declared as a design constraint' matter for database design?"
  type: short-answer
  answer: "Because normalization decisions are based on FDs as constraints, not as observations. If you declare ZipCode → City and store City in a table keyed by something else, you create redundancy — every row with that zip code repeats the city name. This causes update anomalies (changing the city requires updating many rows) and insertion anomalies (you can't record a new zip/city pair without a full row). If the FD only appears to hold currently, normalizing based on it may split the table incorrectly when future data violates the assumed dependency."
  explanation: "The practical consequence: before declaring an FD, you must verify it reflects a real-world constraint — not just a coincidence in today's data. An FD like EmployeeID → Department might appear in data today but might not be a true constraint (an employee could be reassigned). Treating a coincidence as an FD and normalizing around it produces a schema that cannot represent future valid states of the world. FDs must be grounded in domain knowledge, not data mining."
```

## Explainer

You already understand that a relational table consists of rows (tuples) and columns (attributes), and that primary keys uniquely identify each row. A **functional dependency** (FD) formalizes what "uniquely determines" means at a deeper level. The notation X → Y says: whenever two rows have the same values for the attributes in X, they must also have the same values for the attributes in Y. For example, in a student table, StudentID → Name means that knowing the StudentID is sufficient to determine the Name — no two rows with the same StudentID can have different Names. This is exactly the constraint that a primary key enforces, but FDs generalize the idea to any set of attributes, not just the designated key.

FDs are not observations about the current data — they are **constraints about all possible valid data**. If you look at a table today and see that every row with the same ZipCode has the same City, that is suggestive but not proof of ZipCode → City. The FD is a design decision: you are declaring that your data model requires this relationship to always hold. This distinction matters because normalization theory uses FDs to detect and eliminate redundancy. If ZipCode → City holds and you store City alongside ZipCode in a table that has a different primary key, then City is redundantly repeated wherever the same ZipCode appears — creating update anomalies (change the city name in one row but not another) and insertion anomalies (cannot record a new ZipCode-City pair without a full row).

**Armstrong's axioms** give you a mechanical way to reason about FDs. **Reflexivity**: if Y is a subset of X, then X → Y (trivially true). **Augmentation**: if X → Y, then XZ → YZ for any attribute set Z. **Transitivity**: if X → Y and Y → Z, then X → Z. These three axioms are **sound** (they never derive a false FD) and **complete** (they can derive every FD that logically follows from a given set). In practice, you use them through the **attribute closure** algorithm: given a set of attributes X, compute X⁺ — everything X determines — by repeatedly applying the FDs until no new attributes are added. If X⁺ contains all attributes of the relation, then X is a **superkey**. If no proper subset of X also has this property, X is a **candidate key**.

Understanding FDs is the gateway to normalization. When you decompose a table into smaller tables to eliminate redundancy (moving toward 2NF, 3NF, or BCNF), you are really asking: which FDs cause which anomalies, and how can we split the table so that every non-trivial FD has a superkey on its left-hand side? The FDs are the map; normalization is the journey they guide.
