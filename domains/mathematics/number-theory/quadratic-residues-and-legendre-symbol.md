---
id: quadratic-residues-and-legendre-symbol
title: Quadratic Residues and the Legendre Symbol
domain: mathematics
course: number-theory
prerequisites:
- id: modular-arithmetic
  type: hard
builds-toward:
- euler-criterion
- law-of-quadratic-reciprocity
tags:
- quadratic-residues
- legendre-symbol
- modular-arithmetic
stage: advanced
status: draft
---

# Quadratic Residues and the Legendre Symbol

## Core Idea
An integer a is a quadratic residue modulo prime p if there exists x such that x² ≡ a (mod p). The Legendre symbol (a/p) ∈ {−1, 0, 1} compactly represents this; it satisfies multiplicativity and enables determining solvability of x² ≡ a (mod p).

## Explainer

From modular arithmetic, you know that working mod p (for prime p) turns ℤ into the finite field ℤ/pℤ with exactly p elements. You've solved linear congruences ax ≡ b (mod p) by finding multiplicative inverses. Quadratic residues ask the next natural question: which elements of ℤ/pℤ are perfect squares? That is, for which values of a does x² ≡ a (mod p) have a solution?

Consider p = 7. The nonzero squares mod 7 are 1² = 1, 2² = 4, 3² = 2, 4² = 2, 5² = 4, 6² = 1 — so the **quadratic residues** mod 7 are {1, 2, 4}. The **quadratic non-residues** are {3, 5, 6}. Notice there are exactly 3 residues and 3 non-residues — half of the (p − 1) nonzero elements. This is always true: among the p − 1 nonzero elements of ℤ/pℤ, exactly (p − 1)/2 are quadratic residues. The reason is that the squaring map x ↦ x² is a 2-to-1 function: x and −x have the same square, so exactly half the nonzero values are hit.

The **Legendre symbol** (a/p) packages this information into a single number: it equals 1 if a is a QR mod p, −1 if a is a NR mod p, and 0 if p | a. The most powerful property is multiplicativity: (ab/p) = (a/p)(b/p). This means the product of two residues is a residue, the product of two non-residues is a residue, and the product of a residue and non-residue is a non-residue — exactly like the sign rules for multiplication of positive and negative numbers. Multiplicativity lets you factor the Legendre symbol just as you factor integers.

Computing the Legendre symbol efficiently relies on **Euler's criterion**: (a/p) ≡ a^((p−1)/2) (mod p). This connects directly to what you know from modular arithmetic — by Fermat's little theorem, a^(p−1) ≡ 1 (mod p) for a not divisible by p, so a^((p−1)/2) is a square root of 1, meaning it equals ±1. Euler's criterion says it equals +1 exactly when a is a QR. This gives a computable formula: to check whether 3 is a QR mod 11, compute 3^5 = 243 ≡ 1 (mod 11), so (3/11) = 1. Indeed, 5² = 25 ≡ 3 (mod 11) confirms it.

The theory of quadratic residues reaches its apex with the **law of quadratic reciprocity**, one of the most celebrated theorems in number theory: for odd primes p ≠ q, (p/q)(q/p) = (−1)^((p−1)/2 · (q−1)/2). This remarkable symmetry says that whether p is a square mod q is almost always equivalent to whether q is a square mod p, with a sign that depends only on whether p and q are both ≡ 3 (mod 4). Together with supplementary laws for (−1/p) and (2/p), reciprocity lets you evaluate any Legendre symbol by successive reduction — a computational method analogous to the Euclidean algorithm — without ever computing a large power.
