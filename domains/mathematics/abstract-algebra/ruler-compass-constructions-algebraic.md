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
status: validated
---

# Ruler and Compass Constructions (Algebraic Proof)

## Core Idea
A complex number is constructible by ruler and compass if and only if its minimal polynomial over Q has degree a power of 2. Consequently, angle trisection and cube duplication are impossible, and π is transcendental.

## Questions

```yaml
- question: "A student claims that angle trisection is merely very difficult — that a sufficiently clever construction sequence could succeed where all previous attempts have failed. The algebraic proof in this topic establishes that:"
  type: multiple-choice
  options:
    - "Current construction methods are inefficient but not impossible; better algorithms could in principle work"
    - "Trisecting 60° requires constructing cos(20°), whose minimal polynomial over Q is an irreducible cubic of degree 3 — since 3 is not a power of 2, this is provably impossible, not merely unachieved"
    - "Trisection is impossible only for 60°; other angles could be trisected with the right approach"
    - "The impossibility is geometric rather than algebraic; new geometric axioms could in principle allow trisection"
  answer: 1
  explanation: "The impossibility is not a statement about the limits of human ingenuity — it is a provable algebraic fact. Each ruler-and-compass step introduces at most a quadratic field extension (degree 2). By the tower law, any constructible number lies in a tower of quadratic extensions, so its degree over Q must be a power of 2. The minimal polynomial of cos(20°) is 8x³ - 6x - 1, which is irreducible over Q, giving degree 3 — not a power of 2. No sequence of ruler-and-compass steps can bridge this gap, regardless of cleverness, because the degree obstruction is absolute. The student's framing treats it as an engineering challenge; the mathematics shows it is a structural impossibility."

- question: "Why does the transcendence of π immediately imply that squaring the circle is impossible, even before applying the power-of-2 degree criterion?"
  type: multiple-choice
  options:
    - "π is irrational, and ruler-and-compass constructions can only produce rational lengths"
    - "π is transcendental — it satisfies no polynomial with rational coefficients — so it cannot appear in any algebraic extension of Q at all, including any tower of quadratic extensions"
    - "π is larger than all constructible numbers, which are bounded by the initial unit length"
    - "Squaring the circle requires the ratio π to appear as a coefficient, and coefficients must be constructible"
  answer: 1
  explanation: "The power-of-2 degree criterion applies to algebraic numbers (those satisfying some polynomial over Q). π is transcendental: it satisfies no such polynomial. Therefore π cannot lie in any finite algebraic extension of Q — it is not reachable by any tower of field extensions, quadratic or otherwise. This is a strictly stronger obstruction than having the 'wrong' degree. The set of constructible numbers is a subset of algebraic numbers; transcendentals are excluded a priori, before any degree calculation. Option A is wrong because ruler-and-compass constructions can produce irrational lengths (e.g., √2) — irrationality is not the obstruction."

- question: "A real number is constructible by ruler and compass if and only if it lies in a tower of quadratic field extensions over Q, meaning its degree over Q must be a power of 2."
  type: true-false
  answer: true
  explanation: "This is the fundamental theorem connecting ruler-and-compass geometry to field theory. Each construction step (line-line, line-circle, or circle-circle intersection) produces a new point whose coordinates satisfy a degree-at-most-2 polynomial over the current field — at worst, it adjoins a square root. Starting from Q, after k steps the total field degree is a product of 1s and 2s (by the tower law), hence a power of 2. The converse also holds: any number whose degree over Q is 2ᵏ lies in a tower of k quadratic extensions, each step realizable as a construction. Constructibility is exactly the condition [Q(α):Q] = 2ᵏ for some non-negative integer k."

- question: "The cube root of 2 is not constructible because it is irrational — ruler-and-compass constructions cannot produce irrational lengths."
  type: true-false
  answer: false
  explanation: "Ruler-and-compass constructions can and do produce irrational lengths: √2 (diagonal of a unit square), √3 (height of an equilateral triangle), the golden ratio, and infinitely many others are all constructible because they have degree 2 over Q — a power of 2. The obstruction for ∛2 is not irrationality but algebraic degree: ∛2 satisfies x³ - 2 = 0, an irreducible cubic over Q (no rational roots by the rational root theorem), giving [Q(∛2):Q] = 3. Since 3 is not a power of 2, ∛2 is not constructible. The relevant criterion is always the degree of the minimal polynomial over Q, not whether the number is rational or irrational."

- question: "Explain why each step of a ruler-and-compass construction extends the current field by at most a degree-2 extension, and why this implies any constructible number's minimal polynomial degree must be a power of 2."
  type: short-answer
  answer: "Every construction step produces new points as intersections of two lines (degree-1 equations), a line and a circle (degree 2), or two circles (degree 2). In all cases, the new coordinates satisfy a polynomial of degree at most 2 over the current field — at worst, they require adjoining a square root. Starting from Q, after k steps you have Q(α₁, …, αₖ) where each αᵢ has degree 1 or 2 over the previous field. By the tower law, [Q(α₁, …, αₖ):Q] = ∏[Q(α₁,…,αᵢ):Q(α₁,…,αᵢ₋₁)], and each factor is 1 or 2. A product of 1s and 2s is a power of 2. Any constructible number lies in such a tower, so its minimal polynomial degree — which divides the tower degree — must also be a power of 2."
  explanation: "This algebraic translation is the key mechanism that makes impossibility results provable. The geometric question 'can I reach this point with ruler and compass?' becomes the purely algebraic question 'does this point's minimal polynomial have degree a power of 2?' No geometric ingenuity can circumvent this because the degree constraint follows from the structure of the operations themselves — not from the particular construction tried. The two classical impossibilities (cube duplication, angle trisection) both produce degree-3 minimal polynomials, placing them permanently outside the constructible numbers regardless of what construction strategy is attempted."
```

## Explainer

The Fundamental Theorem of Galois Theory, your prerequisite, gave you a dictionary between subfields of a field extension and subgroups of its Galois group. Ruler-and-compass constructibility is the spectacular application of that dictionary to classical geometry — it transforms the question "can I build this length with a ruler and compass?" into a purely algebraic question about polynomial degrees.

Here is the key translation. Each step of a ruler-and-compass construction involves either intersecting two lines, intersecting a line and a circle, or intersecting two circles. Lines have equations of degree 1; circles have degree 2. So each step introduces a new point whose coordinates satisfy a degree-2 polynomial over the field you already have — at worst, it adjoins a square root. This means every constructible number lies in a **tower of quadratic extensions**: Q ⊆ Q(α₁) ⊆ Q(α₁, α₂) ⊆ … where each step doubles the degree. By the tower law, the degree [Q(α₁, …, αₖ) : Q] = 2ᵏ, a power of 2.

The impossibility proofs flow directly from this. To **trisect 60°** you need to construct cos(20°), which satisfies the cubic 8x³ - 6x - 1 = 0. This polynomial is irreducible over Q (check: no rational roots), so [Q(cos 20°) : Q] = 3. Since 3 is not a power of 2, cos(20°) is not constructible, and neither is a 20° angle. To **duplicate the cube** you need ∛2, which satisfies x³ - 2 = 0, an irreducible cubic over Q, giving degree 3 — again impossible. These aren't failures of ingenuity; they are provable impossibilities embedded in the algebra.

The Galois perspective sharpens this further. A number α is constructible if and only if [Q(α) : Q] is a power of 2, which happens if and only if the Galois group of the splitting field of the minimal polynomial of α is a 2-group (all element orders are powers of 2). This is the Galois criterion: constructibility means your symmetry group is built entirely from ℤ/2ℤ pieces.

The case of **π** and **squaring the circle** goes one step further: π is transcendental (Lindemann, 1882), meaning it satisfies no polynomial with rational coefficients at all. No field tower of finite degree over Q can contain a transcendental number, so π is not constructible by an even more fundamental reason — it doesn't live in any algebraic extension of Q. This is the most dramatic application: two thousand years of geometric puzzles, resolved by asking what degree polynomial a number satisfies.
