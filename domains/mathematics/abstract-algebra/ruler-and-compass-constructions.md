---
id: ruler-and-compass-constructions
title: Ruler and Compass Constructions
domain: mathematics
course: abstract-algebra
prerequisites:
- id: field-extensions
  type: hard
- id: galois-groups
  type: soft
tags:
- constructions
- compass
- ruler
- quadratic-extensions
stage: advanced
status: draft
---

# Ruler and Compass Constructions

## Core Idea
A length is constructible with ruler and compass iff it lies in a field extension Q(α₁, ..., αₙ) where each [Q(α₁, ..., αᵢ) : Q(α₁, ..., αᵢ₋₁)] = 2. This proves angle trisection and cube doubling are impossible: they require non-power-of-2 degree extensions. The theory uses Galois extensions of degree 2^k.

## Explainer

You know from field extensions that adjoining an element α to a field F creates a new field F(α), and the degree [F(α) : F] measures how many dimensions the extension adds. The key connection here is geometric: every ruler-and-compass step — drawing a line between two points, drawing a circle centered at one point and passing through another, finding their intersections — corresponds algebraically to solving a linear or quadratic equation. Linear equations keep you in the same field; quadratic equations adjoin a square root, adding a degree-2 extension. This means each construction step can at most double the degree of the field over ℚ.

The **constructibility criterion** follows: a length is constructible if and only if it lives in a field you can reach by a tower of quadratic extensions, Q ⊂ F₁ ⊂ F₂ ⊂ ... ⊂ Fₙ, where each step has degree 2. By the tower law you already know, [Fₙ : Q] = 2ⁿ for some n. So any constructible number has degree over ℚ equal to a power of 2. This is the gatekeeper: if a number requires a field extension whose degree is *not* a power of 2, it cannot be constructed.

Now the famous impossibility results fall out cleanly. **Doubling the cube** means constructing ∛2 — a root of x³ - 2, which is irreducible over ℚ. The degree [Q(∛2) : Q] = 3, which is not a power of 2. Impossible. **Trisecting a 60° angle** means constructing cos(20°), a root of 8x³ - 6x - 1, again irreducible of degree 3. Impossible. The impossibility is not about ingenuity or complexity — no sequence of compass-and-straightedge moves, no matter how clever, can escape the algebraic constraint that each step only adjoins square roots.

**Squaring the circle** (constructing √π) is also impossible, but for a deeper reason: π is transcendental, meaning it satisfies no polynomial with rational coefficients at all. It is not merely in a "wrong-degree" extension — it is outside the entire algebraic hierarchy. Contrast this with regular polygons: a regular n-gon is constructible if and only if n = 2^k · p₁ · p₂ · ... · pₘ where each pᵢ is a distinct **Fermat prime** (primes of the form 2^(2^k) + 1). Gauss proved this at age 19 by showing constructibility of a regular n-gon is equivalent to the Galois group of the n-th cyclotomic field being a 2-group. The field extension framework transforms ancient geometric puzzles into questions you can answer with algebra.
