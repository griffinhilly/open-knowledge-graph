---
id: ruler-compass-constructions-algebraic
title: Ruler and Compass Constructions (Algebraic Proof)
domain: mathematics
course: abstract-algebra
prerequisites:
- id: fundamental-theorem-galois-theory
  type: hard
tags:
- geometric-construction
- constructible
- degree-2
- tower-of-fields
stage: advanced
status: draft
---

# Ruler and Compass Constructions (Algebraic Proof)

## Core Idea
A complex number is constructible by ruler and compass if and only if its minimal polynomial over Q has degree a power of 2. Consequently, angle trisection and cube duplication are impossible, and π is transcendental.

## Explainer

The Fundamental Theorem of Galois Theory, your prerequisite, gave you a dictionary between subfields of a field extension and subgroups of its Galois group. Ruler-and-compass constructibility is the spectacular application of that dictionary to classical geometry — it transforms the question "can I build this length with a ruler and compass?" into a purely algebraic question about polynomial degrees.

Here is the key translation. Each step of a ruler-and-compass construction involves either intersecting two lines, intersecting a line and a circle, or intersecting two circles. Lines have equations of degree 1; circles have degree 2. So each step introduces a new point whose coordinates satisfy a degree-2 polynomial over the field you already have — at worst, it adjoins a square root. This means every constructible number lies in a **tower of quadratic extensions**: Q ⊆ Q(α₁) ⊆ Q(α₁, α₂) ⊆ … where each step doubles the degree. By the tower law, the degree [Q(α₁, …, αₖ) : Q] = 2ᵏ, a power of 2.

The impossibility proofs flow directly from this. To **trisect 60°** you need to construct cos(20°), which satisfies the cubic 8x³ - 6x - 1 = 0. This polynomial is irreducible over Q (check: no rational roots), so [Q(cos 20°) : Q] = 3. Since 3 is not a power of 2, cos(20°) is not constructible, and neither is a 20° angle. To **duplicate the cube** you need ∛2, which satisfies x³ - 2 = 0, an irreducible cubic over Q, giving degree 3 — again impossible. These aren't failures of ingenuity; they are provable impossibilities embedded in the algebra.

The Galois perspective sharpens this further. A number α is constructible if and only if [Q(α) : Q] is a power of 2, which happens if and only if the Galois group of the splitting field of the minimal polynomial of α is a 2-group (all element orders are powers of 2). This is the Galois criterion: constructibility means your symmetry group is built entirely from ℤ/2ℤ pieces.

The case of **π** and **squaring the circle** goes one step further: π is transcendental (Lindemann, 1882), meaning it satisfies no polynomial with rational coefficients at all. No field tower of finite degree over Q can contain a transcendental number, so π is not constructible by an even more fundamental reason — it doesn't live in any algebraic extension of Q. This is the most dramatic application: two thousand years of geometric puzzles, resolved by asking what degree polynomial a number satisfies.
