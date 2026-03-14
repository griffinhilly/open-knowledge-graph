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
