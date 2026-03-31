---
id: ca-going-up-going-down
title: Going Up and Going Down Theorems
domain: mathematics
course: commutative-algebra
prerequisites:
- id: ca-integral-extensions
  type: hard
- id: ca-prime-and-maximal-ideals
  type: hard
- id: ca-krull-dimension
  type: soft
builds-toward:
- ca-valuation-rings
tags:
- going-up
- going-down
- lying-over
- incomparability
- integral-extension
- flat-morphism
stage: expert
status: validated
---

# Going Up and Going Down Theorems

## Core Idea
The going up and going down theorems describe how prime ideal chains in a ring R extend to prime ideal chains in an extension ring S. The lying-over theorem says that for an integral extension R ⊆ S, every prime of R is the contraction of some prime of S. Going up (Cohen-Seidenberg) says chains of primes in R can be lifted to chains in S preserving containment. Going down requires additional hypotheses (R integrally closed, or the extension being flat) and guarantees chains can be extended downward. These theorems are the algebraic engine behind dimension-theoretic arguments in algebraic geometry.

## Questions

```yaml
- question: "Which of the following is required for the going down theorem to hold for an integral extension R ⊆ S?"
  type: multiple-choice
  options:
    - "S is a finitely generated R-module"
    - "R is integrally closed and S is a domain"
    - "S is Noetherian"
    - "R is a local ring"
  answer: 1
  explanation: "The going down theorem for integral extensions requires R to be an integrally closed domain and S to be a domain. Without these hypotheses, going down can fail. For example, Z ⊆ Z[i] satisfies going down because Z is integrally closed. But the integral extension Z[√5] over Z[2√5] can fail going down when the base is not integrally closed."

- question: "If R ⊆ S is an integral extension and P is a prime of R, then there exists a prime Q of S with Q ∩ R = P."
  type: true-false
  answer: true
  explanation: "This is the lying-over theorem. The proof goes through the localization: R_P ⊆ S_P is still integral, and the maximal ideal of R_P contracts from some prime of S_P. Pulling back gives Q lying over P. Lying-over is the starting point; going up and going down extend it to chains."

- question: "Let k be a field and consider the integral extension k[x^2] ⊆ k[x]. The prime (x^2 - 1) of k[x^2] has the prime (x - 1) lying over it. What other prime of k[x] lies over (x^2 - 1)?"
  type: short-answer
  answer: "(x + 1), since x^2 - 1 = (x - 1)(x + 1) and (x + 1) ∩ k[x^2] = (x^2 - 1)."
  explanation: "In k[x], the ideal (x^2 - 1) of k[x^2] generates (x-1)(x+1), which lies in both (x-1) and (x+1). The incomparability theorem guarantees these two primes lying over (x^2-1) are not comparable by inclusion, consistent with both being maximal in k[x]."

- question: "The going up theorem holds for any integral extension of commutative rings (no extra hypotheses beyond integrality)."
  type: true-false
  answer: true
  explanation: "Going up is unconditional for integral extensions: given R ⊆ S integral and primes P ⊆ P' of R with Q lying over P, there exists Q' ⊇ Q lying over P'. This is the Cohen-Seidenberg going up theorem. Going DOWN is the one that requires extra hypotheses (integrally closed base, or flatness)."

- question: "Explain the geometric meaning of the going up theorem in terms of morphisms of varieties."
  type: short-answer
  answer: "An integral extension R ⊆ S corresponds to a finite surjective morphism f: Spec S → Spec R. Going up says the map f is closed: it maps closed sets to closed sets. Chains of subvarieties in the base can be lifted to the total space."
  explanation: "Algebraically, going up says prime chains lift through integral extensions. Geometrically, finite morphisms (those corresponding to integral extensions) are closed maps. The lying-over theorem says f is surjective. Going up gives closedness. Going down (when it holds) gives an 'open-like' property: the map preserves generization."
```

## Explainer

The **going up** and **going down** theorems, due to Cohen and Seidenberg, describe how the prime ideal structure of a ring relates to that of an integral extension. Given a ring extension R ⊆ S, every prime ideal Q of S **contracts** to a prime ideal Q ∩ R of R. The fundamental question is the converse: given primes in R, can we find primes in S lying over them? And can we do this compatibly with chains?

The **lying-over theorem** is the starting point: if R ⊆ S is an integral extension and P is a prime ideal of R, then there exists a prime Q of S with Q ∩ R = P. The **incomparability theorem** adds that distinct primes of S lying over the same prime of R are incomparable under inclusion. Together, these say the map Spec S → Spec R is surjective and the fibers have no containments. The **going up theorem** extends this to chains: if P_1 ⊆ P_2 are primes of R and Q_1 lies over P_1, then there exists Q_2 ⊇ Q_1 lying over P_2. Going up holds for any integral extension without additional hypotheses.

The **going down theorem** is more delicate. It states: if R ⊆ S is an integral extension with R an integrally closed domain and S a domain, and if P_1 ⊇ P_2 are primes of R with Q_1 lying over P_1, then there exists Q_2 ⊆ Q_1 lying over P_2. The hypothesis that R is integrally closed is essential -- without it, going down can fail. There is an alternative route to going down that bypasses integrality entirely: if R → S is a **flat** ring homomorphism, then going down holds. Flatness-based going down is used extensively in algebraic geometry, where flat morphisms are the algebraic counterpart of "continuously varying fibers."

The consequences for dimension theory are immediate. Going up implies that dim(S) ≥ dim(R) for integral extensions (chains in R lift to chains of at least the same length in S). When going down also holds, the dimensions are equal for integral extensions of domains. Combined with Noether normalization (every finitely generated k-algebra is integral over a polynomial subring), these theorems prove that the Krull dimension of a finitely generated k-algebra equals its transcendence degree over k -- one of the foundational results connecting algebra to geometry.
