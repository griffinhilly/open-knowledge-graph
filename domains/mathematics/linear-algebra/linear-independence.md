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

## Explainer

Start with what you already know about vector spaces: they are sets closed under addition and scalar multiplication, and every element can be "moved around" by scaling. **Linear independence** asks a sharp question about a collection of vectors: is any one of them redundant? A vector is redundant if it can be written as a combination of the others — meaning it adds no new "direction" to the collection. Linear independence is exactly the property that none of them is redundant.

The formal definition encodes this idea elegantly. Write the equation c₁v₁ + c₂v₂ + ··· + cₖvₖ = 0 and ask: does it have a solution other than all cᵢ = 0? The trivial solution (all coefficients zero) always works, because the zero vector is always 0. If that is the *only* solution, the vectors are **linearly independent** — the only way to combine them to zero is to use nothing. If there is a nontrivial solution, say c₁ ≠ 0, you can solve: v₁ = −(c₂/c₁)v₂ − ··· − (cₖ/c₁)vₖ, showing v₁ is a combination of the others. That is **linear dependence**.

Geometrically, this is about dimension. Two vectors in the plane are linearly independent if they point in genuinely different directions — not just scaled versions of each other. Three vectors in 3D space are independent if none lies in the plane spanned by the other two. Dependence occurs whenever you have "too many" vectors relative to the space's dimension: three vectors in a plane must be dependent, because the plane is only two-dimensional. The connection to your prerequisite on scalar multiplication is direct: dependence always reduces to one vector being reachable from others by combinations of scaling and adding.

For matrices, the condition translates cleanly. The columns of an m × n matrix A are linearly independent if and only if the equation Ax = 0 has only the trivial solution x = 0 — meaning the kernel (null space) is just {0}. Equivalently, the rank of A equals n: all n columns are "active" in the sense that no column is a shadow of the others. This connection to rank makes independence testable by Gaussian elimination, which is how you will compute it in practice.
