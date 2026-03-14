---
id: np-completeness
title: NP-Completeness and Cook-Levin Theorem
domain: computer-science
course: theory-of-computation
prerequisites:
- id: nondeterministic-polynomial-time
  type: hard
tags:
- np-completeness
- cook-levin
- hardness
stage: abstract-reasoning
status: draft
---

# NP-Completeness and Cook-Levin Theorem

## Core Idea
A language is NP-complete if it is in NP and every language in NP reduces to it in polynomial time. The Cook-Levin theorem proves that boolean satisfiability (SAT) is NP-complete. NP-complete problems are presumed intractable; a polynomial-time algorithm for any NP-complete problem would imply P = NP.
