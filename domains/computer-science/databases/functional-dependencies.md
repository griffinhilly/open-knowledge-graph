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

## Explainer

You already understand that a relational table consists of rows (tuples) and columns (attributes), and that primary keys uniquely identify each row. A **functional dependency** (FD) formalizes what "uniquely determines" means at a deeper level. The notation X → Y says: whenever two rows have the same values for the attributes in X, they must also have the same values for the attributes in Y. For example, in a student table, StudentID → Name means that knowing the StudentID is sufficient to determine the Name — no two rows with the same StudentID can have different Names. This is exactly the constraint that a primary key enforces, but FDs generalize the idea to any set of attributes, not just the designated key.

FDs are not observations about the current data — they are **constraints about all possible valid data**. If you look at a table today and see that every row with the same ZipCode has the same City, that is suggestive but not proof of ZipCode → City. The FD is a design decision: you are declaring that your data model requires this relationship to always hold. This distinction matters because normalization theory uses FDs to detect and eliminate redundancy. If ZipCode → City holds and you store City alongside ZipCode in a table that has a different primary key, then City is redundantly repeated wherever the same ZipCode appears — creating update anomalies (change the city name in one row but not another) and insertion anomalies (cannot record a new ZipCode-City pair without a full row).

**Armstrong's axioms** give you a mechanical way to reason about FDs. **Reflexivity**: if Y is a subset of X, then X → Y (trivially true). **Augmentation**: if X → Y, then XZ → YZ for any attribute set Z. **Transitivity**: if X → Y and Y → Z, then X → Z. These three axioms are **sound** (they never derive a false FD) and **complete** (they can derive every FD that logically follows from a given set). In practice, you use them through the **attribute closure** algorithm: given a set of attributes X, compute X⁺ — everything X determines — by repeatedly applying the FDs until no new attributes are added. If X⁺ contains all attributes of the relation, then X is a **superkey**. If no proper subset of X also has this property, X is a **candidate key**.

Understanding FDs is the gateway to normalization. When you decompose a table into smaller tables to eliminate redundancy (moving toward 2NF, 3NF, or BCNF), you are really asking: which FDs cause which anomalies, and how can we split the table so that every non-trivial FD has a superkey on its left-hand side? The FDs are the map; normalization is the journey they guide.
