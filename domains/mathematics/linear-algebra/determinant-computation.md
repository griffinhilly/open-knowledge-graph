---
id: determinant-computation
title: Computing Determinants
domain: mathematics
course: linear-algebra
prerequisites:
- id: matrices-definition
  type: hard
builds-toward:
- determinant-properties
- cramers-rule
- eigenvalues-eigenvectors
tags:
- determinants
- computation
- algorithms
stage: formal-systems
status: draft
---

# Computing Determinants

## Core Idea
The determinant of an n × n matrix is a scalar with geometric meaning (signed volume of the parallelepiped spanned by columns). For 2×2: det([a b; c d]) = ad − bc. For larger matrices, use cofactor expansion C_ij = (−1)^{i+j} M_ij or row reduction. det(A) = 0 iff A is singular.
