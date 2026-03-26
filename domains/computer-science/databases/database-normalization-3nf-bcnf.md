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

## Questions

```yaml
- question: "A relation R(Student, Course, Instructor) has two FDs: {Student, Course} → Instructor and Instructor → Course. This schema is in 3NF but not BCNF. Why?"
  type: multiple-choice
  options:
    - "Because it has a transitive dependency between Student and Course through Instructor"
    - "Because Instructor → Course violates BCNF (Instructor is not a superkey), but 3NF permits it since Course is part of a candidate key"
    - "Because the primary key spans three attributes rather than one"
    - "Because Course appears on the right side of two different functional dependencies"
  answer: 1
  explanation: "BCNF requires that for every non-trivial FD X → Y, X must be a superkey. Here Instructor → Course violates BCNF because Instructor alone is not a superkey. However, 3NF's 'candidate key escape clause' permits this: the right-hand side, Course, is part of the candidate key {Student, Course}. 3NF allows the violation when Y is prime (part of some candidate key); BCNF does not. This is exactly the scenario — overlapping candidate keys — where 3NF and BCNF diverge."

- question: "A designer finds that decomposing a schema to BCNF loses some functional dependencies as enforceable single-table constraints. What is the standard practical recommendation?"
  type: multiple-choice
  options:
    - "Always use BCNF; lost dependencies can be ignored since they are captured in the data redundancy"
    - "Use 3NF synthesis instead — it guarantees both lossless-join decomposition and dependency preservation"
    - "Fall back to 2NF to avoid the decomposition problem"
    - "Use BCNF and recreate lost dependencies using application-layer triggers"
  answer: 1
  explanation: "3NF synthesis (based on a minimal cover) guarantees two properties: lossless-join decomposition (original data can be reconstructed by joining) and dependency preservation (all FDs remain enforceable as single-table constraints). BCNF eliminates more FD-based redundancy but may require cross-table joins to enforce some constraints. The standard advice is: normalize to 3NF first, then evaluate whether remaining anomalies justify the added cost of BCNF. Dependency preservation matters for practical integrity enforcement."

- question: "Every BCNF schema is automatically in 3NF."
  type: true-false
  answer: true
  explanation: "BCNF is strictly stronger than 3NF, so any schema satisfying BCNF trivially satisfies 3NF. BCNF requires that every non-trivial FD X → Y has X as a superkey — no exceptions. 3NF relaxes this with the candidate key escape clause. Since BCNF has no escape clause, it rules out every schema that violates 3NF and more. The inclusion chain is BCNF ⊂ 3NF ⊂ 2NF ⊂ 1NF (where ⊂ means strictly stronger condition on schemas)."

- question: "BCNF decomposition generally preserves most functional dependencies as enforceable single-table constraints."
  type: true-false
  answer: false
  explanation: "This is a critical practical limitation of BCNF. When a relation with overlapping candidate keys is decomposed to BCNF, some FDs may span multiple tables in the result — they can only be checked by joining tables, which is expensive. The example R(Student, Course, Instructor) with Instructor → Course: after BCNF decomposition, enforcing Instructor → Course requires a join. 3NF avoids this by preserving dependencies in individual tables. This trade-off is why 3NF is often preferred despite permitting some residual anomalies."

- question: "Why does the distinction between 3NF and BCNF only arise when a relation has multiple overlapping candidate keys?"
  type: short-answer
  answer: "The only difference is 3NF's candidate key escape clause: a non-trivial FD X → Y with X not a superkey is permitted if Y is part of some candidate key (Y is 'prime'). For this escape clause to activate, there must be a non-superkey X that determines a prime attribute Y. This requires Y to be part of one candidate key but not the universal superkey — which only happens when there are multiple candidate keys that overlap. With a single candidate key, every prime attribute is part of that one key, and any X that determines it would itself be a superkey. No multiple overlapping keys ⟹ no scenario where 3NF and BCNF differ."
  explanation: "Concretely: if a relation has candidate keys CK1 and CK2 that share some attributes, a non-superkey X could determine an attribute that is prime in CK1 but not in CK2. The 3NF escape clause lets this pass; BCNF does not. This is exactly the structure in the Student-Course-Instructor example: {Student, Course} and {Student, Instructor} are both candidate keys, and Instructor determines Course (prime in the first key)."
```

## Explainer

Building on your understanding of 1NF and 2NF, you know that normalization progressively eliminates different kinds of redundancy by restructuring relations. Second Normal Form removed partial dependencies — attributes that depend on only part of a composite key. **Third Normal Form** (3NF) targets the next source of redundancy: **transitive dependencies**. A transitive dependency occurs when a non-key attribute determines another non-key attribute. For example, in a table (StudentID, DepartmentID, DepartmentName), the primary key StudentID determines DepartmentID, and DepartmentID determines DepartmentName. So StudentID → DepartmentName is transitive through DepartmentID. Every time a student is added to the same department, DepartmentName is redundantly stored.

To achieve 3NF, decompose the relation so that every non-key attribute depends directly on the key and nothing but the key. In the example, split into (StudentID, DepartmentID) and (DepartmentID, DepartmentName). Now DepartmentName is stored once per department, not once per student. The formal rule for 3NF says: for every non-trivial functional dependency X → Y, either X is a superkey or Y is part of some candidate key. That second condition — the "candidate key escape clause" — is what distinguishes 3NF from BCNF.

**Boyce-Codd Normal Form** removes that escape clause entirely. BCNF requires that for every non-trivial functional dependency X → Y, X must be a superkey — no exceptions. This means BCNF eliminates all redundancy that arises from functional dependencies. The difference between 3NF and BCNF only matters when a relation has multiple overlapping candidate keys. If a relation has a single candidate key (the common case), then 3NF and BCNF are equivalent. The classic example where they diverge involves a relation like (Student, Course, Instructor) where Instructor → Course but {Student, Course} is the key. 3NF allows this because Course is part of a candidate key, but BCNF does not because Instructor is not a superkey.

The practical tension is between **eliminating redundancy** (BCNF) and **preserving dependencies** (3NF). BCNF decomposition always produces a lossless join — you can reconstruct the original data by joining the decomposed tables. But it may not preserve all functional dependencies as single-table constraints. 3NF decomposition guarantees both: lossless join and dependency preservation. This is why the synthesis algorithm (based on minimal covers) produces 3NF schemas that can enforce all constraints locally, while BCNF decomposition may require cross-table checks. In practice, start by normalizing to 3NF, then evaluate whether the remaining anomalies (if any) justify the cost of moving to BCNF.
