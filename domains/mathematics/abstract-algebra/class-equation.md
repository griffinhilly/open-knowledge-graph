---
id: class-equation
title: The Class Equation
domain: mathematics
course: abstract-algebra
prerequisites:
- id: orbit-stabilizer-theorem
  type: hard
builds-toward:
- sylow-theorems
tags:
- conjugacy
- conjugacy-class
- class-equation
- center
stage: advanced
status: draft
---

# The Class Equation

## Core Idea
For a finite group G under conjugation, |G| = |Z(G)| + Σ |Cᵢ|, where the sum is over conjugacy classes of size > 1. This equation relates the center and conjugacy classes of the group.

## Explainer

The class equation is really just the orbit-stabilizer theorem in disguise — applied to the specific group action of conjugation. Recall that any group G acts on itself by conjugation: g sends x to gxg⁻¹. From your prerequisite work on the orbit-stabilizer theorem, you know that orbits partition the set G, and that |Orbit(x)| = |G| / |Stabilizer(x)|. The **conjugacy class** of x is precisely its orbit under conjugation — the set of all elements of the form gxg⁻¹. So the group decomposes into disjoint conjugacy classes, and the orbit-stabilizer theorem tells you the size of each one.

Now consider two extreme cases. If x lies in the **center** Z(G) — the set of elements that commute with everything — then gxg⁻¹ = x for all g, so the conjugacy class of x contains only x itself (size 1). If x does not lie in the center, its conjugacy class has size greater than 1. Since conjugacy classes partition G, we can write |G| as a sum over all classes: the singleton classes contribute |Z(G)| (one element each), and the remaining classes each contribute some size greater than 1.

This gives the class equation: |G| = |Z(G)| + Σ |G| / |C_G(xᵢ)|, where the sum runs over one representative xᵢ from each non-central conjugacy class, and **C_G(xᵢ)** is the centralizer of xᵢ (the stabilizer under conjugation). Written in terms of conjugacy class sizes: |G| = |Z(G)| + Σ |Cᵢ|. Every term divides |G| by the orbit-stabilizer theorem, which makes this equation a powerful divisibility constraint.

The payoff is algebraic: the class equation forces structural results about groups of prime power order. If |G| = pⁿ, then every conjugacy class size divides pⁿ and hence is a power of p. Each non-central term in the sum is divisible by p, and |G| is divisible by p, so |Z(G)| must also be divisible by p. This means p-groups always have non-trivial centers — a fact that seeds the Sylow theorems and the classification of groups of small order. The class equation is the bridge between the orbit-stabilizer machinery and the structure theory of finite groups.
