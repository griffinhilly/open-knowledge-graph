---
id: diagonalization
title: Diagonalization
domain: mathematics
course: linear-algebra
prerequisites:
- id: eigenvalues-and-eigenvectors
  type: hard
- id: basis-and-dimension
  type: hard
builds-toward:
- least-squares-approximation
tags:
- diagonalization
- similarity
- powers
- exponentials
stage: formal-systems
status: draft
---

# Diagonalization

## Core Idea
Matrix A is diagonalizable if A = PDP⁻¹ where D is diagonal and P's columns are eigenvectors of A. Diagonalization simplifies computation: Aⁿ = PDⁿP⁻¹. An n × n matrix is diagonalizable iff it has n linearly independent eigenvectors, guaranteed if all eigenvalues are distinct.
