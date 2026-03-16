---
id: database-normalization-3nf-bcnf
title: Third Normal Form and BCNF
domain: computer-science
course: databases
prerequisites:
- id: database-normalization-1nf-2nf
  type: hard
builds-toward:
- database-schema-design
tags:
- normalization
- 3NF
- BCNF
- transitive dependency
- decomposition
- lossless join
stage: formal-systems
status: validated
---

# Third Normal Form and BCNF

## Core Idea
Third Normal Form (3NF) eliminates transitive dependencies — situations where a non-key attribute depends on another non-key attribute rather than directly on the primary key. Boyce-Codd Normal Form (BCNF) is a strictly stronger version requiring that for every non-trivial functional dependency X → Y, X must be a superkey; it handles anomalies arising from overlapping candidate keys that 3NF permits. BCNF always eliminates all FD-based redundancy but may lose dependency preservation, while 3NF guarantees both lossless-join decomposition and dependency preservation.

## How It's Best Learned
Work through examples where 3NF and BCNF differ — schemas with multiple overlapping candidate keys. Decompose to BCNF and then verify whether all original FDs are still directly enforceable.

## Common Misconceptions
- Every BCNF schema is in 3NF, but not every 3NF schema is in BCNF — BCNF is strictly stronger.
- BCNF decomposition may not preserve all functional dependencies, which is why 3NF is sometimes preferred in practice.
- Higher normal forms (4NF, 5NF) address multi-valued and join dependencies beyond what functional dependencies capture.

## Explainer

Building on your understanding of 1NF and 2NF, you know that normalization progressively eliminates different kinds of redundancy by restructuring relations. Second Normal Form removed partial dependencies — attributes that depend on only part of a composite key. **Third Normal Form** (3NF) targets the next source of redundancy: **transitive dependencies**. A transitive dependency occurs when a non-key attribute determines another non-key attribute. For example, in a table (StudentID, DepartmentID, DepartmentName), the primary key StudentID determines DepartmentID, and DepartmentID determines DepartmentName. So StudentID → DepartmentName is transitive through DepartmentID. Every time a student is added to the same department, DepartmentName is redundantly stored.

To achieve 3NF, decompose the relation so that every non-key attribute depends directly on the key and nothing but the key. In the example, split into (StudentID, DepartmentID) and (DepartmentID, DepartmentName). Now DepartmentName is stored once per department, not once per student. The formal rule for 3NF says: for every non-trivial functional dependency X → Y, either X is a superkey or Y is part of some candidate key. That second condition — the "candidate key escape clause" — is what distinguishes 3NF from BCNF.

**Boyce-Codd Normal Form** removes that escape clause entirely. BCNF requires that for every non-trivial functional dependency X → Y, X must be a superkey — no exceptions. This means BCNF eliminates all redundancy that arises from functional dependencies. The difference between 3NF and BCNF only matters when a relation has multiple overlapping candidate keys. If a relation has a single candidate key (the common case), then 3NF and BCNF are equivalent. The classic example where they diverge involves a relation like (Student, Course, Instructor) where Instructor → Course but {Student, Course} is the key. 3NF allows this because Course is part of a candidate key, but BCNF does not because Instructor is not a superkey.

The practical tension is between **eliminating redundancy** (BCNF) and **preserving dependencies** (3NF). BCNF decomposition always produces a lossless join — you can reconstruct the original data by joining the decomposed tables. But it may not preserve all functional dependencies as single-table constraints. 3NF decomposition guarantees both: lossless join and dependency preservation. This is why the synthesis algorithm (based on minimal covers) produces 3NF schemas that can enforce all constraints locally, while BCNF decomposition may require cross-table checks. In practice, start by normalizing to 3NF, then evaluate whether the remaining anomalies (if any) justify the cost of moving to BCNF.
