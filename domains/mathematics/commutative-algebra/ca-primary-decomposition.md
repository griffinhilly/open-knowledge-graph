---
id: ca-primary-decomposition
title: Primary Decomposition
domain: mathematics
course: commutative-algebra
prerequisites:
- id: ca-noetherian-rings
  type: hard
- id: maximal-prime-ideals
  type: hard
builds-toward:
- ca-associated-primes
tags:
- primary-ideal
- primary-decomposition
- lasker-noether
- irredundant
stage: expert
status: validated
---

# Primary Decomposition

## Core Idea
A primary ideal Q in a ring R is one where ab ∈ Q implies a ∈ Q or bⁿ ∈ Q for some n — the radical √Q is prime, and Q is "concentrated" at √Q. The Lasker-Noether theorem states that in a Noetherian ring, every ideal decomposes as a finite intersection of primary ideals. This is the algebraic generalization of unique prime factorization of integers to ideals in higher-dimensional rings.

## Questions

```yaml
- question: "In ℤ, the ideal (12) decomposes as (4) ∩ (3). Which statement correctly describes this decomposition?"
  type: multiple-choice
  options:
    - "(4) is primary with radical (2) and (3) is primary with radical (3), giving an irredundant primary decomposition of (12)"
    - "(4) and (3) are both prime ideals, so this is a prime decomposition"
    - "(12) = (4) · (3) is a product decomposition, not an intersection"
    - "This decomposition is redundant because (4) ⊇ (3)"
  answer: 0
  explanation: "The ideal (4) = (2²) is primary: if ab ∈ (4), then 4 | ab; if 4 ∤ a, then 2 ∤ a (since we need a²... actually) — more precisely, (4) is (2)-primary because √(4) = (2) is prime, and (4) satisfies the primary condition. The ideal (3) is prime (hence primary with radical (3)). The intersection (4) ∩ (3) = (12) because lcm(4,3) = 12. This is irredundant: neither component contains the other. In ℤ, primary decomposition corresponds to the prime-power factorization of integers."

- question: "Which of the following is the correct analog of primary decomposition in ℤ?"
  type: multiple-choice
  options:
    - "Factoring n into a product of primes: n = p₁^{a₁} ··· pₖ^{aₖ}"
    - "Writing (n) as an intersection of prime-power ideals: (n) = (p₁^{a₁}) ∩ ··· ∩ (pₖ^{aₖ})"
    - "Writing n as a sum of prime numbers (Goldbach's conjecture)"
    - "Factoring the ideal (n) into a product of prime ideals"
  answer: 1
  explanation: "For n = p₁^{a₁} ··· pₖ^{aₖ}, the ideal (n) decomposes as (p₁^{a₁}) ∩ ··· ∩ (pₖ^{aₖ}). Each (pᵢ^{aᵢ}) is (pᵢ)-primary. This is an irredundant primary decomposition. Note the distinction between intersection and product: in ℤ, (p₁^{a₁}) ∩ ··· ∩ (pₖ^{aₖ}) = (p₁^{a₁}) ··· (pₖ^{aₖ}) when the primes are distinct, but in general rings, the intersection and product of ideals differ."

- question: "In a Noetherian ring, every ideal has a primary decomposition."
  type: true-false
  answer: true
  explanation: "This is the Lasker-Noether theorem, the fundamental existence result for primary decomposition. Lasker proved it for polynomial rings in 1905, and Noether generalized it to all Noetherian rings in 1921. The proof uses the Noetherian property to show that every ideal is a finite intersection of irreducible ideals, and every irreducible ideal in a Noetherian ring is primary. The decomposition may not be unique, but the associated primes and their primary components (for minimal primes) are unique."

- question: "The primary decomposition of an ideal in a Noetherian ring is always unique."
  type: true-false
  answer: false
  explanation: "While the associated primes (the radicals of the primary components) are uniquely determined, and the primary components corresponding to minimal associated primes are unique, the primary components corresponding to embedded (non-minimal) primes may not be unique. For example, in k[x,y], the ideal (x², xy) has associated primes (x) and (x,y), and the (x,y)-primary component can vary. The first uniqueness theorem says the set of associated primes is unique; the second says minimal primary components are unique."

- question: "Explain the difference between a prime ideal and a primary ideal, and why primary ideals are the 'right' building blocks for ideal decomposition."
  type: short-answer
  answer: "A prime ideal P satisfies: ab ∈ P implies a ∈ P or b ∈ P. A primary ideal Q satisfies the weaker condition: ab ∈ Q implies a ∈ Q or bⁿ ∈ Q for some n. Equivalently, Q is primary if every zero-divisor in R/Q is nilpotent. The radical √Q is always prime, and Q is 'concentrated at' this prime. Primary ideals are the right building blocks because prime ideals alone are too restrictive — the ideal (4) in ℤ is not prime but is (2)-primary, and (12) = (4) ∩ (3) requires the non-prime component (4)."
  explanation: "Primary ideals relate to prime ideals as prime powers relate to primes in ℤ. The 'defect' of Q from being prime — that b might not be in Q when ab ∈ Q — is controlled: some power of b must be in Q. This means the zero-divisors in R/Q are all nilpotent (they become zero when raised to a high enough power), which is a manageable kind of 'non-primeness.' Without primary ideals, you cannot decompose ideals like (x², xy) in k[x,y], which require embedded components."
```

## Explainer

Unique factorization of integers — 12 = 2² × 3 — is really a statement about ideals: (12) = (4) ∩ (3), where (4) is (2)-primary and (3) is (3)-primary. **Primary decomposition** generalizes this to ideals in any Noetherian ring. An ideal Q is **primary** if ab ∈ Q implies a ∈ Q or bⁿ ∈ Q for some positive integer n. The radical √Q (the set of elements with some power in Q) is always a prime ideal P, and we say Q is **P-primary**. Informally, a primary ideal is "concentrated at a single prime" — its deviation from being prime is controlled, consisting only of nilpotent elements in R/Q.

The **Lasker-Noether theorem** asserts that in a Noetherian ring, every ideal I can be written as a finite intersection I = Q₁ ∩ ··· ∩ Qₙ of primary ideals. The decomposition is called **irredundant** if no Qᵢ can be removed without changing the intersection. In an irredundant decomposition, the prime ideals Pᵢ = √Qᵢ are called the **associated primes** of I. The first uniqueness theorem says the set {P₁, ..., Pₙ} is uniquely determined by I (independent of the decomposition). The second uniqueness theorem says that Qᵢ is uniquely determined when Pᵢ is a minimal associated prime.

The distinction between **minimal** and **embedded** associated primes is geometrically significant. Consider the ideal I = (x², xy) in k[x,y]. Its primary decomposition is (x) ∩ (x², y) = (x) ∩ (x², xy, y^n) for any n ≥ 1 — the (x,y)-primary component is not unique. The minimal prime (x) corresponds to the line x = 0; the embedded prime (x,y) corresponds to the origin, which is a "special point" on that line where extra vanishing occurs. Embedded primes detect subtle geometric features — thickened points, non-reduced structure, singularities.

Primary decomposition connects to many other parts of commutative algebra. The associated primes of an ideal determine where localization is trivial versus non-trivial. The Noetherian hypothesis is essential — non-Noetherian rings can have ideals without primary decomposition. The theory extends to modules (primary decomposition of submodules), which is the framework needed for the deeper theory of associated primes and support of modules.
