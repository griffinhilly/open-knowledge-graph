---
id: burnsides-theorem
title: Burnside's Theorem
domain: mathematics
course: representation-theory
prerequisites:
- id: character-theory
  type: hard
builds-toward: []
tags:
- burnside
- pq-theorem
- solvability
- character-degree
stage: expert
status: validated
---

# Burnside's Theorem

## Core Idea
Burnside's pᵃqᵇ theorem states that every group of order pᵃqᵇ (for primes p, q) is solvable. The proof, remarkably, uses representation theory — specifically, the fact that a character of degree d evaluated at an element whose conjugacy class has size coprime to d must be zero or have absolute value d. This was one of the first major applications of character theory to pure group theory, demonstrating that representation-theoretic methods can prove statements with no obvious connection to linear algebra.

## Questions

```yaml
- question: "Burnside's theorem states that groups of order pᵃqᵇ are solvable. Why can't this be proved by purely group-theoretic methods (without representation theory)?"
  type: multiple-choice
  options:
    - "It has been proved by purely group-theoretic methods — the representation-theoretic proof was just the first one found"
    - "No purely group-theoretic proof is known; the character-theoretic argument remains essential"
    - "It can be proved using Sylow theorems alone"
    - "The theorem is actually false without the representation-theoretic hypothesis"
  answer: 0
  explanation: "A purely group-theoretic proof was eventually found by Goldschmidt (1970) and simplified by others, but it is significantly more complex than Burnside's character-theoretic proof. For decades after Burnside's 1904 proof, no alternative was known. The representation-theoretic proof remains the standard one taught in algebra courses because of its elegance and the insight it provides into why character theory is powerful."

- question: "The key lemma in Burnside's proof states: if χ is an irreducible character of degree d and g is an element whose conjugacy class has size coprime to d, then |χ(g)| = d or χ(g) = 0. This uses the fact that χ(g)/d is an algebraic integer."
  type: true-false
  answer: true
  explanation: "The argument shows that χ(g)/d is both an algebraic integer (using the column orthogonality relations and the coprimality condition) and has absolute value at most 1 (since χ(g) is a sum of d roots of unity). An algebraic integer of absolute value ≤ 1 that is also a root-of-unity sum must be 0 or have absolute value exactly 1, giving |χ(g)| = 0 or d. This number-theoretic constraint is what forces the group to be solvable."

- question: "A group of order 12 = 2² · 3 is solvable by Burnside's theorem. Name one group of order 12 and verify it is solvable."
  type: short-answer
  answer: "A₄ (the alternating group on 4 elements) has order 12. Its normal subgroup V₄ = {e, (12)(34), (13)(24), (14)(23)} is the Klein 4-group, with A₄/V₄ ≅ ℤ/3ℤ. Both V₄ and ℤ/3ℤ are abelian, so A₄ has an abelian normal series: {e} ◁ V₄ ◁ A₄, confirming solvability."
  explanation: "Every group of order pᵃqᵇ is solvable, so this includes groups of order 12 = 2²·3, order 24 = 2³·3, order 100 = 2²·5², etc. The smallest non-solvable group is A₅ of order 60 = 2²·3·5, which involves three prime factors — just beyond the reach of Burnside's theorem."
```

## Explainer

Burnside's theorem (1904) is one of the crown jewels of character theory. It states: **every group of order pᵃqᵇ, where p and q are primes, is solvable** — meaning it can be built up from abelian groups through a series of normal subgroup extensions. The remarkable feature is not the result itself (which had been conjectured on empirical grounds) but the method of proof: it uses character theory in an essential way, deploying representation-theoretic tools to prove a statement about abstract group structure.

The proof hinges on a lemma about characters and conjugacy class sizes. Suppose χ is an irreducible character of degree d and g ∈ G has a conjugacy class of size m, where gcd(d, m) = 1. Then χ(g)/d is an algebraic integer (this follows from the column orthogonality relations and the coprimality condition via a Bezout identity argument). But χ(g) is a sum of d roots of unity, so |χ(g)| ≤ d, meaning |χ(g)/d| ≤ 1. An algebraic integer with all conjugates of absolute value ≤ 1 is either zero or a root of unity with absolute value 1. Therefore |χ(g)| = 0 or |χ(g)| = d.

The conclusion |χ(g)| = d forces χ(g) = d · (root of unity), which means ρ(g) is a scalar matrix — so g lies in the center of ρ(G). Using this, Burnside shows that a group of order pᵃqᵇ always has a nontrivial proper normal subgroup (by finding a conjugacy class whose size is a prime power and applying the lemma). Induction on |G| then gives solvability.

This theorem illustrates a paradigm that recurs throughout algebra: **representation-theoretic methods can prove results about groups that seem inaccessible by direct group-theoretic arguments**. The interplay between the number-theoretic properties of characters (algebraic integers, roots of unity) and the combinatorial structure of the group (conjugacy class sizes, subgroup lattice) creates leverage that purely combinatorial arguments lack. The Feit-Thompson theorem (1963) — all groups of odd order are solvable — extends this paradigm to its most spectacular conclusion, using character theory and modular representation theory in a 255-page proof.
