---
id: gaussian-integers
title: Gaussian Integers
domain: mathematics
course: number-theory
prerequisites:
- id: algebraic-integers
  type: hard
builds-toward:
- norm-algebraic-number-fields
tags:
- gaussian-integers
- complex-integers
- unique-factorization
stage: advanced
status: validated
---

# Gaussian Integers

## Core Idea
The Gaussian integers ℤ[i] = {a + bi : a,b ∈ ℤ} form a unique factorization domain with norm N(a+bi) = a^2 + b^2. Gaussian primes include rational primes p ≡ 3 (mod 4) and factors a±bi of primes p ≡ 1 (mod 4), elegantly explaining two-square representations.

## Questions

```yaml
- question: "Why is 2 + i a Gaussian prime?"
  type: multiple-choice
  options:
    - "Its real and imaginary parts share no common integer factors"
    - "Its norm N(2+i) = 5 is a rational prime, so it cannot factor further in ℤ[i]"
    - "It lies on the Gaussian unit circle and is therefore irreducible"
    - "It corresponds to the prime 2 in ℤ, which remains prime in all extensions"
  answer: 1
  explanation: "The key tool is the multiplicativity of the norm: N(αβ) = N(α)N(β). If 2+i = βγ in ℤ[i], then N(2+i) = N(β)N(γ), i.e., 5 = N(β)N(γ). Since 5 is a rational prime, the only factorizations in ℕ are 1×5 and 5×1. An element with norm 1 is a unit, so this means one factor is a unit — making 2+i irreducible (a Gaussian prime). The same argument applies to any Gaussian integer whose norm is a rational prime."

- question: "A student argues that the rational prime p = 7 must remain prime in ℤ[i] because '7 cannot be split into two pieces.' What is the correct analysis?"
  type: multiple-choice
  options:
    - "The student is right; 7 is prime in ℤ and therefore prime in every ring containing ℤ"
    - "The student reaches the right conclusion for the wrong reason; 7 remains prime in ℤ[i] specifically because 7 ≡ 3 (mod 4)"
    - "The student is wrong; 7 splits in ℤ[i] as a product of two conjugate Gaussian primes"
    - "The student is wrong; 7 ramifies in ℤ[i] like the prime 2"
  answer: 1
  explanation: "The correct conclusion is that 7 remains prime (inert) in ℤ[i], but the reason is the mod 4 classification: a rational prime p remains prime in ℤ[i] if and only if p ≡ 3 (mod 4). Since 7 ≡ 3 (mod 4), it stays prime. The reason this works is Fermat's theorem on sums of squares: p ≡ 3 (mod 4) cannot be written as a² + b² = N(a+bi), so p cannot be a norm of a non-unit Gaussian integer, hence it cannot split. The student's informal argument doesn't capture this; a prime like 5 ≡ 1 (mod 4) splits as 5 = (2+i)(2-i) even though '5 cannot be split into two pieces' by ordinary integers."

- question: "The norm function N(a+bi) = a² + b² satisfies N(αβ) = N(α)N(β) for all Gaussian integers α and β."
  type: true-false
  answer: true
  explanation: "Multiplicativity of the norm is the engine of Gaussian integer factorization theory. Because N(αβ) = N(α)N(β), any factorization in ℤ[i] produces a corresponding factorization of norms in ℤ. This means divisibility and primality questions in ℤ[i] can be partially reduced to ordinary integer arithmetic. In particular, an element with prime norm must be a Gaussian prime, because the only way to factor its norm in ℤ would require one factor to be 1 (a unit)."

- question: "Every rational prime remains prime in ℤ[i] because ℤ[i] contains ℤ as a subring, and divisibility is preserved under ring extensions."
  type: true-false
  answer: false
  explanation: "This is false. Rational primes fall into three categories in ℤ[i]: primes p ≡ 3 (mod 4) remain prime (inert); primes p ≡ 1 (mod 4) split into a product of two distinct Gaussian primes — for example, 5 = (2+i)(2−i); and p = 2 ramifies as 2 = −i(1+i)². Being prime in a subring does not guarantee primality in an extension ring; it is a property that must be checked in the new ring."

- question: "Why does the behavior of rational primes in ℤ[i] depend on their residue mod 4, and what role does the norm play in proving this?"
  type: short-answer
  answer: "A rational prime p splits in ℤ[i] precisely when it can be written as a sum of two squares, p = a² + b² = N(a+bi). Fermat's theorem on sums of squares says this is possible if and only if p ≡ 1 (mod 4) (or p = 2). The norm's multiplicativity is what connects splitting to sums of squares: if p = (a+bi)(a−bi), then N(p) = p² = N(a+bi)·N(a−bi) = (a²+b²)², forcing a²+b² = p. Primes ≡ 3 (mod 4) cannot be expressed as sums of two squares, so they cannot split."
  explanation: "This is the payoff of the Gaussian integer machinery: a 2,000-year-old number theory result (Fermat's two-square theorem) becomes a corollary of unique factorization in ℤ[i]. The mod 4 condition emerges from quadratic reciprocity and properties of the Legendre symbol, but in ℤ[i] its geometric meaning is clear: whether p = a² + b² has a solution is exactly whether p factors as a norm in ℤ[i]."
```

## Explainer

From algebraic integers, you know that ℤ[i] is the ring of integers of ℚ(i) — the "integral" elements of the field of Gaussian rationals. The Gaussian integers look like the ordinary integers ℤ but spread out over the complex plane on a square grid. The unit circle in ℤ[i] contains only four elements — 1, −1, i, −i — corresponding to the four units. Just as in ℤ, units are the invertible elements, and factorization is only unique "up to units."

The key to factorization in ℤ[i] is the **norm**: N(a + bi) = a² + b² = (a + bi)(a − bi). The crucial property is multiplicativity — N(αβ) = N(α)N(β). This turns the problem of factorization in ℤ[i] into a problem about ordinary integers, because if α factors as βγ then N(α) = N(β)N(γ) in ℤ. In particular, an element with prime norm must be a **Gaussian prime** (irreducible in ℤ[i]). For example, 2 + i has norm 5, which is a rational prime, so 2 + i is a Gaussian prime.

The fate of rational primes in ℤ[i] falls into three cases that depend on their residue mod 4. A prime **p ≡ 3 (mod 4)** remains prime — it is still irreducible in ℤ[i]. Geometrically, there is no way to write p = a² + b² as a sum of two squares when p ≡ 3 (mod 4). A prime **p ≡ 1 (mod 4)** splits: it factors as p = (a + bi)(a − bi) where a² + b² = p — and Fermat's theorem on sums of squares guarantees this factorization exists. The prime **p = 2** is special: 2 = −i(1 + i)², so 2 ramifies (its Gaussian factor repeats). This tripartite classification is the prototype for how primes "split, remain inert, or ramify" in general number fields.

The payoff of all this machinery is **Fermat's two-square theorem**: a positive integer n is expressible as a sum of two squares n = a² + b² if and only if every prime factor of n of the form 4k + 3 appears to an even power. The proof flows directly from unique factorization in ℤ[i]. Writing n as a norm N(a + bi) = a² + b² is exactly asking for n to factor in ℤ[i], and unique factorization tells you exactly when that is possible. A 2,000-year-old theorem about sums of squares becomes a routine consequence of the algebraic structure.

The reason ℤ[i] is particularly tractable is that it is a **Euclidean domain**: you can perform division with remainder using the norm as the "size" function. Specifically, given α, β ∈ ℤ[i] with β ≠ 0, you can always find γ, ρ ∈ ℤ[i] with α = βγ + ρ and N(ρ) < N(β). This geometric fact — that every complex number lies within distance 1/√2 < 1 of some Gaussian integer — is the reason Euclid's algorithm works in ℤ[i], and it is what ultimately guarantees unique factorization. Not every ring of algebraic integers enjoys this property, making ℤ[i] an especially clean model to master before tackling more complex number fields.
