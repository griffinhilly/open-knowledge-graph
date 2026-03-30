---
id: fundamental-theorem-of-galois-theory
title: Fundamental Theorem of Galois Theory
domain: mathematics
course: abstract-algebra
prerequisites:
- id: galois-groups
  type: hard
- id: normal-subgroups
  type: soft
builds-toward:
- insolvability-of-the-quintic
tags:
- galois-theory
- correspondence
- fundamental
stage: expert
status: validated
---

# Fundamental Theorem of Galois Theory

## Core Idea
For Galois extension F/K, there is a bijection between intermediate fields E (K ⊆ E ⊆ F) and subgroups H of Gal(F/K), given by H ↔ F^H (the fixed field). Subgroups are normal iff corresponding fields are Galois extensions. The correspondence reverses inclusion.

## Questions

```yaml
- question: "Let Gal(F/K) have a large subgroup H containing most of the group's automorphisms. What does the Galois correspondence predict about the fixed field F^H?"
  type: multiple-choice
  options:
    - "F^H is large, close to F itself, because a large subgroup fixes many elements"
    - "F^H is small, close to K, because many automorphisms must simultaneously fix an element for it to be in F^H"
    - "F^H has the same cardinality as H, reflecting the bijective nature of the correspondence"
    - "The size of F^H cannot be predicted without knowing which specific automorphisms H contains"
  answer: 1
  explanation: "The Galois correspondence reverses inclusion: a larger subgroup corresponds to a smaller fixed field. For an element to be in F^H, it must be fixed by every automorphism in H. The more automorphisms in H, the fewer elements can satisfy all their constraints simultaneously, making F^H smaller. Conversely, a small H places fewer constraints, allowing more elements to be fixed. This reversal is confirmed by the degree-index relation: [Gal(F/K):H] = [F^H:K]."

- question: "An intermediate field E (with K ⊆ E ⊆ F) is not itself a Galois extension of K. What does the Fundamental Theorem tell you about the subgroup of Gal(F/K) corresponding to E?"
  type: multiple-choice
  options:
    - "The corresponding subgroup is trivial — only the identity fixes E"
    - "The corresponding subgroup is not normal in Gal(F/K)"
    - "The corresponding subgroup equals all of Gal(F/K)"
    - "The corresponding subgroup does not exist — non-Galois intermediate fields fall outside the bijection"
  answer: 1
  explanation: "The Fundamental Theorem establishes a bijection between ALL intermediate fields and ALL subgroups — including non-Galois intermediate fields and non-normal subgroups. The theorem also states that E is a Galois extension of K if and only if its corresponding subgroup is normal in Gal(F/K). Contrapositively: if E/K is not Galois, the corresponding subgroup is not normal. Every intermediate field corresponds to exactly one subgroup; the Galois/non-Galois distinction tracks the normal/non-normal distinction."

- question: "The Galois correspondence reverses inclusion: if H₁ ⊆ H₂ are subgroups of Gal(F/K), then F^(H₂) ⊆ F^(H₁)."
  type: true-false
  answer: true
  explanation: "If H₂ contains H₁ (H₁ ⊆ H₂), then H₂ imposes more constraints — every element of F^(H₂) must be fixed by all of H₂, which includes all of H₁ and more. So F^(H₂) ⊆ F^(H₁): the fixed field of the larger subgroup is contained in the fixed field of the smaller subgroup. Inclusion reverses. This is consistent with the degree-index relation: [F^(H₁):K] = [Gal(F/K):H₁] ≥ [Gal(F/K):H₂] = [F^(H₂):K]."

- question: "The question of whether a polynomial is solvable by radicals reduces, via the Galois correspondence, to whether its Galois group is abelian."
  type: true-false
  answer: false
  explanation: "Solvability by radicals corresponds to whether the Galois group is *solvable* — a broader class than abelian. A group is solvable if it has a composition series where each successive quotient is abelian, but the group itself need not be abelian. Abelian groups are solvable (since every subgroup of an abelian group is normal and quotients are abelian), but solvability extends further. The quintic has Galois group S₅, which is not solvable — not merely because it is non-abelian, but specifically because it has no such composition series."

- question: "Explain why the Galois correspondence reverses inclusion — why does a larger subgroup of Gal(F/K) correspond to a smaller fixed field?"
  type: short-answer
  answer: "For an element x ∈ F to belong to the fixed field F^H, it must satisfy σ(x) = x for every automorphism σ in H. The larger H is, the more simultaneous constraints x must satisfy, and the fewer elements can satisfy all of them — so a large H leaves few elements fixed, giving a small F^H. Conversely, a small H places fewer constraints, and more elements can satisfy them all, yielding a large F^H. The correspondence reverses inclusion because 'fixed by everything in H' becomes a stricter condition as H grows."
  explanation: "This reversal is confirmed algebraically: [Gal(F/K):H] = [F^H:K]. A large subgroup H has small index in Gal(F/K), corresponding to a small extension degree [F^H:K], meaning F^H is close to K. The index-degree equality is the quantitative version of the qualitative inclusion-reversal argument, and it underlies the correspondence's power as a tool for translating field questions into group questions."
```

## Explainer

The Fundamental Theorem of Galois Theory is a dictionary that translates field-theoretic questions into group-theoretic ones and back. You already know that a Galois group Gal(F/K) is the group of all field automorphisms of F that fix K pointwise — every element permutes the roots of the minimal polynomial while leaving the base field unchanged. The Fundamental Theorem reveals that this group encodes the complete structure of every intermediate field between K and F.

The correspondence works like this: for each subgroup H of Gal(F/K), define its **fixed field** F^H as the set of all elements of F that every automorphism in H leaves unchanged. This fixed field is an intermediate field sitting between K and F. Conversely, for each intermediate field E, you get the subgroup of Gal(F/K) consisting of all automorphisms that fix E. The theorem says these two operations — taking fixed fields and taking fixing subgroups — are inverses of each other, establishing a perfect bijection.

The most striking feature of this bijection is that it **reverses inclusion**: a larger subgroup corresponds to a smaller intermediate field, and vice versa. Think about why: if H is big (many automorphisms must all fix an element), then very few elements of F are fixed, so F^H is small. If H is small (fewer constraints), more elements can satisfy them, making F^H large. This reversal is not accidental — it mirrors the way index and degree are related: [Gal(F/K) : H] = [F^H : K].

The theorem also captures the qualitative difference between "nice" and "arbitrary" intermediate fields via normal subgroups. Recall from your study of normal subgroups that H is normal in G when it is closed under conjugation — gHg⁻¹ = H for all g in G. In the Galois correspondence, H is a normal subgroup of Gal(F/K) if and only if F^H is itself a Galois extension of K. In this case, the quotient group Gal(F/K)/H is isomorphic to Gal(F^H/K). This is the engine behind the theory of solvable equations: the question of whether a polynomial's roots can be expressed in radicals reduces to whether the Galois group has a particular chain of normal subgroups — a **composition series** through solvable groups. The field/subgroup dictionary converts a geometric question about fields into a purely algebraic question about group structure.
