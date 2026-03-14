---
id: linear-independence
title: Linear Independence and Linear Dependence
domain: mathematics
course: linear-algebra
prerequisites:
- id: vector-spaces-definition
  type: hard
- id: scalar-multiplication
  type: hard
builds-toward:
- basis-definition
- span-spanning-set
tags:
- linear independence
- dependence
- vectors
stage: formal-systems
status: draft
---

# Linear Independence and Linear Dependence

## Core Idea
Vectors v₁, ..., vₖ are linearly independent if c₁v₁ + ... + cₖvₖ = 0 implies all c_i = 0. They are linearly dependent if a non-trivial combination equals zero. Independence means no vector is a combination of others. For matrices: columns are independent iff rank equals the number of columns.
