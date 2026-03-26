---
id: dirichlet-series-and-l-functions
title: Dirichlet Series and L-Functions
domain: mathematics
course: number-theory
prerequisites:
- id: riemann-zeta-function-intro
  type: soft
builds-toward:
- primes-arithmetic-progressions
tags:
- dirichlet-series
- l-functions
- analytic-number-theory
stage: advanced
status: validated
---

# Dirichlet Series and L-Functions

## Core Idea
Dirichlet L-functions L(s, χ) = Σ χ(n)/n^s generalize the Riemann zeta function for Dirichlet characters χ. They satisfy functional equations and have Euler products, enabling study of primes in arithmetic progressions and other structured subsets of integers.

## Questions

```yaml
- question: "To prove there are infinitely many primes congruent to 1 mod 5, Dirichlet needed to establish a key analytic fact about the L-functions for characters mod 5. What is that fact?"
  type: multiple-choice
  options:
    - "Each L(s, χ) has a simple pole at s = 1, just like the Riemann zeta function"
    - "L(1, χ) ≠ 0 for every non-principal character χ mod 5"
    - "The Euler product for L(s, χ) converges for all complex s"
    - "Each L(s, χ) satisfies the Riemann Hypothesis"
  answer: 1
  explanation: "The proof uses a logarithmic sum over primes: the sum of χ(p)/p over primes p diverges if L(1, χ) = 0. By orthogonality of characters, summing over all characters mod q isolates the contribution from primes in the specific residue class a mod q. If any L(1, χ) = 0 for a non-principal χ, the sum collapses and fails to diverge, contradicting the known divergence of the sum over primes in any valid residue class. So non-vanishing of L(1, χ) is not just helpful — it is the precise analytic input the proof requires."

- question: "A Dirichlet L-function L(s, χ) has an Euler product factored over primes because of a specific property of the character χ. Which property is responsible?"
  type: multiple-choice
  options:
    - "χ is periodic mod q"
    - "χ takes values that are roots of unity"
    - "χ is completely multiplicative: χ(mn) = χ(m)χ(n) for all m, n"
    - "χ vanishes on integers sharing a common factor with q"
  answer: 2
  explanation: "The Euler product for L(s, χ) = Σ χ(n)/n^s exists precisely because χ is completely multiplicative. When χ(mn) = χ(m)χ(n) always, the Dirichlet series factors prime by prime, giving L(s, χ) = Π_p (1 − χ(p)p^{-s})^{-1}, just as ζ(s) factors when a(n) = 1. Periodicity ensures the character is determined by residues mod q, and vanishing on integers sharing a factor with q is necessary for the character to be well-defined, but neither of these gives the Euler product — complete multiplicativity does."

- question: "The Generalized Riemann Hypothesis (GRH) asserts that all non-trivial zeros of any Dirichlet L-function L(s, χ) lie on the critical line Re(s) = 1/2."
  type: true-false
  answer: true
  explanation: "GRH directly extends the Riemann Hypothesis — which concerns ζ(s) — to all Dirichlet L-functions. Just as the Riemann Hypothesis asserts that the non-trivial zeros of ζ(s) lie on Re(s) = 1/2, GRH makes the same assertion for each L(s, χ). Most sharp estimates in analytic number theory about primes in arithmetic progressions — error terms, explicit bounds — would become dramatically better if GRH were proved. It remains one of the central open problems in mathematics."

- question: "Dirichlet's proof that nearly every arithmetic progression a, a+q, a+2q, … with gcd(a, q) = 1 contains infinitely many primes can be completed using primarily the algebraic properties of Dirichlet characters, without any complex analysis."
  type: true-false
  answer: false
  explanation: "The algebraic structure — character orthogonality, Euler products — sets up the machinery, but the critical step is showing L(1, χ) ≠ 0 for all non-principal characters, and this requires complex analysis. The principal character's L-function has a pole at s = 1 (it behaves like ζ(s) with finitely many factors removed), and non-vanishing of the non-principal L-functions at s = 1 is a genuinely analytic result. Elementary proofs of special cases exist, but Dirichlet's general theorem requires analysis."

- question: "Explain why character orthogonality is the key mechanism that allows Dirichlet L-functions to 'isolate' primes in a specific residue class, and why non-vanishing of L(1, χ) is the crucial step in the proof."
  type: short-answer
  answer: "The orthogonality of Dirichlet characters mod q means that the sum Σ_χ χ(a)^{-1} χ(n) over all characters is φ(q) if n ≡ a (mod q) and gcd(n, q) = 1, and 0 otherwise. This acts as an indicator function for the residue class. When you sum log L(s, χ) over all characters and apply orthogonality, the contributions from primes not in the target class cancel, and only primes ≡ a (mod q) survive — their contribution diverges as s → 1⁺. If any L(1, χ) = 0 for a non-principal χ, that term would collapse rather than diverge, destroying the argument. So L(1, χ) ≠ 0 is not a technical detail but the analytic foundation the entire selection mechanism rests on."
  explanation: "The deep insight is that L-functions provide a 'lens' that can focus on structured subsets of primes by encoding residue information in the character. The Euler product connects this to primes directly, and the analytic behavior at s = 1 controls whether the lens successfully sees infinitely many primes in the target class."
```

## Explainer

From the Riemann zeta function you already know that ζ(s) = Σ 1/n^s encodes deep arithmetic information, particularly about primes, via its Euler product ζ(s) = Π (1 − p^−s)^−1. A **Dirichlet series** is any series of the form Σ a(n)/n^s, and the zeta function is simply the case where a(n) = 1 for all n. The key insight of analytic number theory is to replace the constant sequence 1 with a richer arithmetic function — one that "sees" structure in the integers that 1 cannot detect.

A **Dirichlet character** χ mod q is a completely multiplicative, periodic function on the integers that is zero on integers sharing a common factor with q, and otherwise takes values that are roots of unity. The **principal character** χ₀ just assigns 1 to integers coprime to q and 0 otherwise, making L(s, χ₀) essentially ζ(s) with finitely many factors removed. Non-principal characters are the interesting ones: they "color" residues mod q differently, and the L-function L(s, χ) = Σ χ(n)/n^s becomes a weighted zeta function that selectively picks up integers according to their residue class. Because χ is completely multiplicative, L(s, χ) also factors into an Euler product L(s, χ) = Π_p (1 − χ(p)p^−s)^−1, one factor per prime.

The reason Dirichlet introduced these objects was to prove that every arithmetic progression a, a+q, a+2q, … with gcd(a, q) = 1 contains infinitely many primes — a statement you cannot prove by the same direct argument used for primes overall. The key is to show L(1, χ) ≠ 0 for all non-principal characters, which requires complex analysis. Think of it as follows: if you take a formal "average" of L(s, χ) over all characters mod q, the multiplicativity and orthogonality of characters cause most prime contributions to cancel — except for primes in the specific residue class a mod q. Showing these L-functions are nonzero at s = 1 is the heart of Dirichlet's theorem.

Like the Riemann zeta function, L-functions satisfy **functional equations** that relate L(s, χ) to L(1 − s, χ̄) (where χ̄ is the conjugate character), allowing analytic continuation to the whole complex plane. The analogue of the Riemann Hypothesis — that the non-trivial zeros of L(s, χ) all lie on the line Re(s) = 1/2 — is known as the **Generalized Riemann Hypothesis** (GRH), and most of analytic number theory would become considerably sharper if it were proved. Every result you will encounter about primes in arithmetic progressions and residue structure ultimately traces back to the non-vanishing and zero distribution of these L-functions.
