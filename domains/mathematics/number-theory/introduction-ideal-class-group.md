---
id: introduction-ideal-class-group
title: Introduction to the Ideal Class Group
domain: mathematics
course: number-theory
prerequisites:
- id: failure-unique-factorization
  type: hard
- id: subrings-and-ideals
  type: hard
tags:
- ideal-class-group
- algebraic-number-theory
stage: advanced
status: draft
---

# Introduction to the Ideal Class Group

## Core Idea
The ideal class group measures how far a number ring departs from unique factorization. In rings of algebraic integers where elements may not factor uniquely, ideals always factor uniquely into prime ideals. Two ideals are equivalent if they differ by multiplication by a principal ideal. The class group is the quotient of fractional ideals by principal ideals, and its order—the class number h(K)—equals 1 precisely when the ring is a principal ideal domain with unique factorization. Computing class numbers reveals the arithmetic complexity of number fields and connects to deep results in algebraic number theory.

## How It's Best Learned
Work through ℤ[√−5], where 6 = 2 · 3 = (1+√−5)(1−√−5) shows factorization failure. Then verify that ideal factorization restores uniqueness and compute that h = 2, making the class group ℤ/2ℤ.

## Common Misconceptions
The class group is not about individual elements failing to factor—it is about the global structure of ideals. Students sometimes think unique factorization fails "everywhere" when h > 1, but many elements still factor uniquely; it is the exceptions that the class group quantifies.

