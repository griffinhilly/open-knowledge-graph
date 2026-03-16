---
id: the-class-equation
title: The Class Equation
domain: mathematics
course: abstract-algebra
prerequisites:
- id: orbit-stabilizer-theorem
  type: hard
builds-toward:
- sylow-theorems
tags:
- class-equation
- conjugacy
- center
stage: advanced
status: draft
---

# The Class Equation

## Core Idea
The class equation states |G| = |Z(G)| + Σ |C_i| where the sum is over non-central conjugacy classes. Conjugacy classes partition G; elements in Z(G) form singletons. The class equation is essential for analyzing p-groups and proving Sylow theorems.

## Explainer

The **class equation** is a precise bookkeeping identity that comes directly from the orbit-stabilizer theorem you've already learned, applied to a specific group action: conjugation. When a group G acts on itself by conjugation — the action g · x = gxg⁻¹ — the orbits are exactly the **conjugacy classes**. The conjugacy class of an element x is the set of all elements of the form gxg⁻¹ as g ranges over G. Two elements in the same conjugacy class are "conjugate" — related by an internal symmetry of the group.

By the orbit-stabilizer theorem, the size of the orbit of x (its conjugacy class) equals |G| divided by the size of the stabilizer of x under conjugation. The stabilizer of x is {g ∈ G : gxg⁻¹ = x} = {g ∈ G : gx = xg}, which is exactly the set of elements that commute with x — called the **centralizer** of x, written C_G(x). So |conjugacy class of x| = |G|/|C_G(x)|.

Now partition G by its conjugacy classes. Elements in the **center** Z(G) — those that commute with everything — form conjugacy classes of size 1: gxg⁻¹ = x for all g. All other elements belong to classes of size ≥ 2. Summing the sizes of all conjugacy classes gives |G|, yielding the class equation: **|G| = |Z(G)| + Σ |G|/|C_G(xᵢ)|**, where the sum runs over one representative xᵢ from each non-central conjugacy class.

The class equation's power shows immediately in the theory of p-groups (groups of order pⁿ for a prime p). Every term in the class equation is divisible by p (since each non-central class size divides |G| = pⁿ and is greater than 1, it must be divisible by p). Since |G| is divisible by p and all the non-central terms are divisible by p, it follows that |Z(G)| is divisible by p — so Z(G) is nontrivial. This means every p-group has a nontrivial center, a fact that bootstraps into the proof that groups of order p² are abelian and ultimately into the full Sylow theory.
