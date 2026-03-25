---
id: first-isomorphism-theorem-groups
title: First Isomorphism Theorem for Groups
domain: mathematics
course: abstract-algebra
prerequisites:
- id: quotient-groups
  type: hard
- id: first-isomorphism-theorem-for-rings
  type: soft
builds-toward:
- second-isomorphism-theorem-groups
- third-isomorphism-theorem-groups
tags:
- isomorphism-theorem
- fundamental-theorem
- kernel
- image
stage: advanced
status: validated
---
# First Isomorphism Theorem for Groups

## Core Idea
If φ: G → H is a group homomorphism, then G/ker(φ) ≅ im(φ). This theorem connects quotient groups and images of homomorphisms.

## Questions

```yaml
- question: "A homomorphism φ: G → H has two elements g₁, g₂ ∈ G with φ(g₁) = φ(g₂). Which statement must be true?"
  type: multiple-choice
  options:
    - "Both g₁ and g₂ must be elements of the kernel"
    - "g₁g₂⁻¹ must be an element of the kernel"
    - "g₁ = g₂, since equal images imply equal preimages"
    - "The homomorphism must be the trivial map"
  answer: 1
  explanation: "If φ(g₁) = φ(g₂), then φ(g₁g₂⁻¹) = φ(g₁)φ(g₂)⁻¹ = e, so g₁g₂⁻¹ ∈ ker(φ). Option A is the classic misconception — g₁ and g₂ being in the kernel would mean φ(g₁) = φ(g₂) = e, but their images could be any element h ∈ H, not necessarily the identity. The kernel captures which elements are in the same coset (have the same image), not which elements map to the identity specifically."

- question: "The reduction-mod-3 map φ: ℤ → ℤ/3ℤ defined by φ(n) = n mod 3 has kernel 3ℤ. By the First Isomorphism Theorem, which group is isomorphic to ℤ/3ℤ (the image)?"
  type: multiple-choice
  options:
    - "ℤ itself, since φ maps from ℤ"
    - "3ℤ, since the kernel has the same order as the image"
    - "ℤ/3ℤ, since G/ker(φ) = ℤ/3ℤ ≅ im(φ) = ℤ/3ℤ"
    - "The theorem cannot apply because ℤ is infinite"
  answer: 2
  explanation: "The theorem states G/ker(φ) ≅ im(φ). Here G/ker(φ) = ℤ/3ℤ (three cosets: 3ℤ, 1+3ℤ, 2+3ℤ), and im(φ) = ℤ/3ℤ — they are the same group, so the isomorphism is immediate. Option B is wrong: the kernel 3ℤ is infinite, while the image has order 3. The theorem applies to all group homomorphisms, including those involving infinite groups."

- question: "If φ: G → H is a surjective homomorphism, then G/ker(φ) ≅ H."
  type: true-false
  answer: true
  explanation: "When φ is surjective, im(φ) = H, so the First Isomorphism Theorem gives G/ker(φ) ≅ im(φ) = H directly. Surjectivity is the special case where the image fills all of H. Even when φ is not surjective, the theorem still applies — G/ker(φ) ≅ im(φ) as a subgroup of H — but surjectivity makes the statement particularly clean."

- question: "The First Isomorphism Theorem implies that any two groups of the same finite order are isomorphic."
  type: true-false
  answer: false
  explanation: "This is a major misconception. The theorem says G/ker(φ) ≅ im(φ) for a specific homomorphism — it does not say anything about arbitrary groups of equal size. There are non-isomorphic groups of the same order: for example, ℤ/6ℤ and S₃ both have order 6 but are not isomorphic (one is abelian, the other is not). The theorem is a structural result about a given homomorphism, not a general statement about groups of the same cardinality."

- question: "Explain why the map φ̄: G/ker(φ) → im(φ) defined by φ̄(gK) = φ(g) is called 'well-defined,' and why this verification step is necessary."
  type: short-answer
  answer: "Well-defined means the output depends only on the coset gK, not on which representative g is chosen. If g' is another element in the same coset, then g' = gk for some k ∈ ker(φ), so φ(g') = φ(gk) = φ(g)φ(k) = φ(g)·e = φ(g). So both representatives give the same output. The verification is necessary because a coset has infinitely many representatives, and if different choices gave different outputs, φ̄ would not be a function at all. Well-definedness is exactly the statement that 'having the same image under φ' is the precise criterion for being in the same coset — and this is what makes the theorem work."
```

## Explainer

The First Isomorphism Theorem is one of the central structural results in group theory. It tells you that when a homomorphism φ: G → H cannot be injective — because multiple elements of G map to the same element of H — the "reason" for that collision is always the kernel. The **kernel** ker(φ) = {g ∈ G : φ(g) = e_H} is a normal subgroup of G, and it captures exactly the elements that get "crushed to the identity" by φ. Any two elements g₁ and g₂ with the same image — φ(g₁) = φ(g₂) — differ by a kernel element: g₂ = g₁k for some k ∈ ker(φ). So the kernel completely describes the collisions.

Your prerequisite knowledge of quotient groups is the key ingredient. The quotient group G/ker(φ) takes G and glues together everything that φ sends to the same place — creating one coset gK (where K = ker(φ)) for each "equivalence class" of elements sharing an image. The theorem says this collapsing operation produces a group genuinely isomorphic to the image im(φ) ≤ H. The isomorphism is the map φ̄: G/ker(φ) → im(φ) defined by φ̄(gK) = φ(g). This is well-defined precisely because any two representatives of gK have the same image under φ.

A concrete example makes this vivid. Let φ: ℤ → ℤ/3ℤ be the reduction-mod-3 map: φ(n) = n mod 3. The kernel is 3ℤ = {…, −6, −3, 0, 3, 6, …}, the multiples of 3. The quotient group ℤ/3ℤ on the left side of the isomorphism has three cosets: {3ℤ, 1+3ℤ, 2+3ℤ}. The image of φ is all of ℤ/3ℤ on the right. The theorem confirms these are isomorphic, and the isomorphism is immediate: coset k+3ℤ maps to k mod 3.

The deeper insight is a **dimension-like counting principle**. For finite groups, the theorem implies |G| = |ker(φ)| × |im(φ)|, since |G/ker(φ)| = |G|/|ker(φ)|. This is the group-theoretic analog of the rank-nullity theorem from linear algebra: the kernel (what collapses) and the image (what survives) together account for all of G. Every homomorphism factors as G surjecting onto G/ker(φ), followed by G/ker(φ) injecting isomorphically into H. The theorem makes this two-step factorization precise and universal — it applies to every group homomorphism, regardless of the specific groups involved.
