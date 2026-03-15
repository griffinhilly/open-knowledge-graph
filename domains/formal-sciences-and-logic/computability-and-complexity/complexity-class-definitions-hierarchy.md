---
id: complexity-class-definitions-hierarchy
title: Complexity Classes and the Complexity Hierarchy
domain: formal-sciences-and-logic
course: computability-and-complexity
prerequisites:
- id: time-complexity-classes-formal
  type: hard
- id: space-complexity-classes-formal
  type: hard
- id: algorithm-analysis-big-o
  type: soft
- id: algorithm-complexity
  type: hard
builds-toward:
- p-versus-np
- polynomial-hierarchy
tags:
- complexity-classes
- hierarchy-theorem
- p-np-pspace
stage: advanced
status: draft
---

# Complexity Classes and the Complexity Hierarchy

## Core Idea
Complexity classes like P, NP, PSPACE, and EXPTIME group problems by the computational resources (time or space) required to solve them. The Hierarchy Theorem shows that these classes are strictly nested (e.g., P ⊆ NP ⊆ PSPACE ⊆ EXPTIME), with some containments proven and others (like P vs. NP) remaining famously open.

## How It's Best Learned
Study the hierarchy theorem proofs to understand how resource bounds create proper inclusions. Visualize complexity classes as concentric circles to internalize nestings.

## Common Misconceptions
- Confusing 'properly contained' with 'strictly separated by a provable gap.' Hierarchy theorems use resource separation, not problem difficulty.
- Assuming all inclusions are proven. P ⊆ NP is known; P = NP is open.
