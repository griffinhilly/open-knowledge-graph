---
id: sylow-theorems
title: Sylow Theorems
domain: mathematics
course: abstract-algebra
prerequisites:
- id: class-equation
  type: hard
builds-toward:
- applications-sylow-theorems
tags:
- sylow-p-subgroup
- sylow-theorems
- p-groups
stage: advanced
status: validated
---

# Sylow Theorems

## Core Idea
For a finite group G of order pᵏm with gcd(p, m) = 1, Sylow's theorems assert the existence of p-Sylow subgroups of order pᵏ, that all such subgroups are conjugate, and that the number of p-Sylow subgroups divides m and is ≡ 1 (mod p).

## Questions

```yaml
- question: "A group G has order 15 = 3 · 5. What can the Sylow theorems tell you about the number of Sylow 3-subgroups (n₃)?"
  type: multiple-choice
  options:
    - "n₃ can be 1, 3, or 5, since any of these divide 15"
    - "n₃ must equal 1, since it must divide 5 and be ≡ 1 mod 3, leaving only n₃ = 1"
    - "n₃ can be 1 or 5, since both divide 15"
    - "n₃ is undetermined without knowing the specific group structure"
  answer: 1
  explanation: "The Third Sylow Theorem requires n₃ to satisfy two conditions simultaneously: n₃ divides m = 5 (so n₃ ∈ {1, 5}) AND n₃ ≡ 1 mod 3 (so n₃ ∈ {1, 4, 7, ...}). The only value satisfying both is n₃ = 1. Option (a) ignores the mod condition; option (c) checks divisibility but forgets the congruence condition. The two constraints together are what make the theorem powerful."

- question: "There is exactly one Sylow p-subgroup P of a finite group G. Which conclusion follows directly from this fact?"
  type: multiple-choice
  options:
    - "P is the center of G, since unique subgroups are always central"
    - "P is a normal subgroup of G"
    - "P is cyclic, since all Sylow subgroups of prime-power order are cyclic"
    - "P is the only subgroup of G of any order"
  answer: 1
  explanation: "By the Second Sylow Theorem, all Sylow p-subgroups are conjugate. If nₚ = 1, the unique subgroup P equals all of its conjugates — gPg⁻¹ = P for every g ∈ G. That is precisely the definition of a normal subgroup. Option (a) is not generally true; a unique Sylow subgroup need not be central. Option (c) is a separate question about the structure of P, not a consequence of uniqueness."

- question: "All Sylow p-subgroups of a finite group are isomorphic to each other."
  type: true-false
  answer: true
  explanation: "By the Second Sylow Theorem, all Sylow p-subgroups are conjugate: if P and Q are both Sylow p-subgroups, then Q = gPg⁻¹ for some g ∈ G. Conjugation is an isomorphism, so all Sylow p-subgroups are isomorphic. This is true regardless of how many there are — even if nₚ > 1, every Sylow p-subgroup has the same structure."

- question: "If nₚ > 1, the Sylow p-subgroups can rarely be isomorphic to each other, since they are distinct subgroups."
  type: true-false
  answer: false
  explanation: "Being distinct as subsets of G does not prevent isomorphism as groups. The Second Sylow Theorem says all Sylow p-subgroups are conjugate, and conjugation is an isomorphism. Multiple Sylow p-subgroups can coexist and still be isomorphic — they are different subgroups of G but have the same internal structure."

- question: "Why does nₚ = 1 imply that the unique Sylow p-subgroup is normal in G? Explain using the definition of normality and the Second Sylow Theorem."
  type: short-answer
  answer: "A subgroup P is normal in G if gPg⁻¹ = P for every g ∈ G. By the Second Sylow Theorem, any conjugate gPg⁻¹ is itself a Sylow p-subgroup. If nₚ = 1, there is only one Sylow p-subgroup — so gPg⁻¹ must equal P for every g. This is exactly normality. The uniqueness of P forces every conjugate to land back on P itself."
  explanation: "This argument is elegant because it requires no special properties of P — only the counting argument from the Third Sylow Theorem (which pins down nₚ = 1) combined with the conjugacy result from the Second Sylow Theorem. It is why Sylow analysis is used to find normal subgroups and prove simplicity or non-simplicity of groups."
```

## Explainer

You came to the Sylow theorems through the **class equation**, which used conjugacy classes to count elements and extract information about a group's structure. The Sylow theorems push this counting machinery much further — they are the main tool for classifying finite groups and proving that groups of certain orders cannot be simple.

Write |G| = pᵏm where p is prime and p does not divide m. A **Sylow p-subgroup** is a subgroup of G of order exactly pᵏ — the largest power of p that divides |G|. The **First Sylow Theorem** guarantees these always exist: for every prime p dividing |G|, at least one Sylow p-subgroup exists. This extends Cauchy's theorem (which gave elements of prime order) to subgroups of prime-power order.

The **Second Sylow Theorem** says all Sylow p-subgroups are conjugate to each other: if P and Q are both Sylow p-subgroups, then Q = gPg⁻¹ for some g ∈ G. This is remarkable — all Sylow p-subgroups are isomorphic (as they're conjugate) even if there are many of them. The **Third Sylow Theorem** pins down how many there are: if nₚ denotes the number of Sylow p-subgroups, then nₚ divides m and nₚ ≡ 1 (mod p). These two constraints together are often enough to pin down nₚ exactly.

The power of the Sylow theorems is in the applications. For a concrete example, suppose |G| = 12 = 2² · 3. The number of Sylow 3-subgroups satisfies n₃ | 4 and n₃ ≡ 1 mod 3, so n₃ ∈ {1, 4}. The number of Sylow 2-subgroups satisfies n₂ | 3 and n₂ ≡ 1 mod 2, so n₂ ∈ {1, 3}. If n₃ = 4, then there are 4 × 2 = 8 elements of order 3, leaving only 4 elements for two Sylow 2-subgroups of order 4 — but two distinct subgroups of order 4 would require at least 5 elements (they must share the identity). This forces n₂ = 1 when n₃ = 4. A **unique** Sylow subgroup (nₚ = 1) is automatically **normal** — it equals its own conjugates. This is how the Sylow theorems reveal normal subgroups and, ultimately, whether a group must be a direct product of smaller groups.
