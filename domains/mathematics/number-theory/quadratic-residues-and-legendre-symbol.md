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

## Questions

```yaml
- question: "Suppose (a/p) = −1 and (b/p) = −1 for a prime p. What is (ab/p)?"
  type: multiple-choice
  options:
    - "−1, because combining two non-residues produces another non-residue."
    - "0, because neither a nor b is a perfect square mod p."
    - "1, because the product of two quadratic non-residues is always a quadratic residue."
    - "It depends on the specific values of a and b; no general rule applies."
  answer: 2
  explanation: "By multiplicativity of the Legendre symbol, (ab/p) = (a/p)(b/p) = (−1)(−1) = 1. This is the analogue of multiplying two negative numbers: the result is positive (a quadratic residue). The same rule says two residues multiply to a residue (1 × 1 = 1), and a residue times a non-residue is a non-residue (1 × −1 = −1). Option A is the natural but wrong intuition — it reverses the algebraic fact. Multiplicativity is the Legendre symbol's most useful computational property."

- question: "Among the nonzero elements {1, 2, 3, ..., p−1} of ℤ/pℤ for an odd prime p, how many are quadratic residues?"
  type: multiple-choice
  options:
    - "p − 1, because every nonzero element has a square root in some extension field."
    - "(p − 1)/2, because the squaring map x ↦ x² is two-to-one: x and −x always yield the same square."
    - "(p + 1)/2, because we must count zero as a quadratic residue."
    - "It varies depending on the prime; no general formula exists."
  answer: 1
  explanation: "Among the p − 1 nonzero elements of ℤ/pℤ, exactly (p−1)/2 are quadratic residues and (p−1)/2 are non-residues. The reason is that the squaring map x ↦ x² hits each quadratic residue exactly twice: both x and −x (≡ p−x mod p) map to x². Since x ≠ −x for nonzero x in ℤ/pℤ (assuming p is an odd prime), the p−1 nonzero elements pair up into (p−1)/2 pairs with the same square, giving (p−1)/2 distinct quadratic residue values. Zero (p | a) is the special case where (a/p) = 0, not classified as a QR."

- question: "The product of a quadratic residue and a quadratic non-residue mod an odd prime p is always a quadratic non-residue."
  type: true-false
  answer: true
  explanation: "By multiplicativity of the Legendre symbol: if (a/p) = 1 and (b/p) = −1, then (ab/p) = (a/p)(b/p) = (1)(−1) = −1, so ab is a non-residue. This follows from the analogy with multiplication of signs: positive × negative = negative. The three cases are: QR × QR = QR, NR × NR = QR, QR × NR = NR. Knowing just the Legendre symbols of a and b fully determines the symbol of their product."

- question: "If x² ≡ a (mod p) has a solution and p ∤ a, then it has exactly one solution in {1, 2, ..., p−1}."
  type: true-false
  answer: false
  explanation: "When x² ≡ a (mod p) is solvable (a is a quadratic residue), it has exactly two solutions: if x₀ is one solution, then −x₀ ≡ p − x₀ (mod p) is the other, since (−x₀)² = x₀² ≡ a. These are distinct elements of ℤ/pℤ because x₀ ≠ −x₀ when p is an odd prime and p ∤ x₀. This two-to-one nature of the squaring map is exactly why only half of the nonzero elements are quadratic residues — each residue value is the image of exactly two inputs."

- question: "Explain why exactly half of the nonzero elements of ℤ/pℤ are quadratic residues, for an odd prime p."
  type: short-answer
  answer: "The squaring map x ↦ x² on the nonzero elements of ℤ/pℤ is exactly two-to-one: for each nonzero a, both x and −x satisfy x² ≡ a (mod p), and x ≠ −x since p is odd (x = −x would mean 2x ≡ 0, so p | x, contradicting x ≠ 0). Therefore the p−1 nonzero inputs pair up into (p−1)/2 pairs, each pair mapping to the same output. The image of the squaring map — the set of quadratic residues — has exactly (p−1)/2 elements, which is half of the nonzero elements."
  explanation: "The key is the pairing argument: every input x has a distinct partner −x with the same square. Since the inputs pair perfectly (no element is its own pair in ℤ/pℤ for odd p), the outputs are exactly half as many as the inputs. This same reasoning shows that every quadratic residue has exactly two square roots, while quadratic non-residues have none. The 2-to-1 structure of the squaring map is the fundamental fact underlying the entire theory of quadratic residues."
```

## Explainer

From modular arithmetic, you know that working mod p (for prime p) turns ℤ into the finite field ℤ/pℤ with exactly p elements. You've solved linear congruences ax ≡ b (mod p) by finding multiplicative inverses. Quadratic residues ask the next natural question: which elements of ℤ/pℤ are perfect squares? That is, for which values of a does x² ≡ a (mod p) have a solution?

Consider p = 7. The nonzero squares mod 7 are 1² = 1, 2² = 4, 3² = 2, 4² = 2, 5² = 4, 6² = 1 — so the **quadratic residues** mod 7 are {1, 2, 4}. The **quadratic non-residues** are {3, 5, 6}. Notice there are exactly 3 residues and 3 non-residues — half of the (p − 1) nonzero elements. This is always true: among the p − 1 nonzero elements of ℤ/pℤ, exactly (p − 1)/2 are quadratic residues. The reason is that the squaring map x ↦ x² is a 2-to-1 function: x and −x have the same square, so exactly half the nonzero values are hit.

The **Legendre symbol** (a/p) packages this information into a single number: it equals 1 if a is a QR mod p, −1 if a is a NR mod p, and 0 if p | a. The most powerful property is multiplicativity: (ab/p) = (a/p)(b/p). This means the product of two residues is a residue, the product of two non-residues is a residue, and the product of a residue and non-residue is a non-residue — exactly like the sign rules for multiplication of positive and negative numbers. Multiplicativity lets you factor the Legendre symbol just as you factor integers.

Computing the Legendre symbol efficiently relies on **Euler's criterion**: (a/p) ≡ a^((p−1)/2) (mod p). This connects directly to what you know from modular arithmetic — by Fermat's little theorem, a^(p−1) ≡ 1 (mod p) for a not divisible by p, so a^((p−1)/2) is a square root of 1, meaning it equals ±1. Euler's criterion says it equals +1 exactly when a is a QR. This gives a computable formula: to check whether 3 is a QR mod 11, compute 3^5 = 243 ≡ 1 (mod 11), so (3/11) = 1. Indeed, 5² = 25 ≡ 3 (mod 11) confirms it.

The theory of quadratic residues reaches its apex with the **law of quadratic reciprocity**, one of the most celebrated theorems in number theory: for odd primes p ≠ q, (p/q)(q/p) = (−1)^((p−1)/2 · (q−1)/2). This remarkable symmetry says that whether p is a square mod q is almost always equivalent to whether q is a square mod p, with a sign that depends only on whether p and q are both ≡ 3 (mod 4). Together with supplementary laws for (−1/p) and (2/p), reciprocity lets you evaluate any Legendre symbol by successive reduction — a computational method analogous to the Euclidean algorithm — without ever computing a large power.
