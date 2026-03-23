---
id: first-isomorphism-theorem-for-groups
title: First Isomorphism Theorem for Groups
domain: mathematics
course: abstract-algebra
prerequisites:
- id: quotient-groups
  type: hard
- id: group-isomorphisms
  type: hard
builds-toward:
- second-and-third-isomorphism-theorems
tags:
- isomorphism-theorems
- fundamental
- structure
stage: advanced
status: validated
---

# First Isomorphism Theorem for Groups

## Core Idea
If φ: G → H is a homomorphism, then G/ker(φ) ≅ im(φ). Every homomorphism factors through a quotient by its kernel. This fundamental theorem connects quotient groups to isomorphisms and reveals homomorphism structure.

## Questions

```yaml
- question: "A surjective homomorphism φ: ℤ → ℤ/6ℤ has kernel 6ℤ. What does the First Isomorphism Theorem conclude?"
  type: multiple-choice
  options:
    - "ℤ ≅ ℤ/6ℤ, since φ is surjective"
    - "ker(φ) ≅ im(φ), so 6ℤ ≅ ℤ/6ℤ"
    - "ℤ/6ℤ ≅ ℤ/6ℤ — the quotient of ℤ by its kernel is isomorphic to the image"
    - "The theorem does not apply because ℤ is infinite"
  answer: 2
  explanation: "The theorem states G/ker(φ) ≅ im(φ). With G = ℤ, ker(φ) = 6ℤ, and im(φ) = ℤ/6ℤ (surjective), we get ℤ/6ℤ ≅ ℤ/6ℤ. This confirms that ℤ/6ℤ arises canonically as a quotient of ℤ. Option A is the key misconception: surjectivity alone does not give G ≅ H — only G/ker(φ) ≅ im(φ). The theorem does not require G to be finite."

- question: "To prove that the rotation group of a square is isomorphic to ℤ/4ℤ, the most powerful application of the First Isomorphism Theorem is to:"
  type: multiple-choice
  options:
    - "Show both groups have 4 elements and are abelian"
    - "Find a surjective homomorphism φ: ℤ → (rotation group) and verify its kernel is 4ℤ"
    - "Directly construct a bijection and check it preserves the group operation"
    - "Apply the theorem to the identity homomorphism φ(g) = g on the rotation group"
  answer: 1
  explanation: "The standard strategy: find a surjective homomorphism φ from a known group (ℤ) onto the target, then the theorem gives ℤ/ker(φ) ≅ target. Since the rotation group has order 4, the kernel of φ will be 4ℤ, giving ℤ/4ℤ ≅ rotation group. Option A is insufficient — same size and commutativity don't determine the isomorphism class. Option C works but bypasses the theorem's power. Option D is circular and produces a trivial conclusion."

- question: "If φ: G → H is a homomorphism with trivial kernel, then G ≅ H."
  type: true-false
  answer: false
  explanation: "Trivial kernel means φ is injective, so the First Isomorphism Theorem gives G ≅ im(φ). But im(φ) may be a proper subgroup of H — you only get G ≅ H if φ is also surjective. For example, the inclusion φ: ℤ → ℚ has trivial kernel, but ℤ ≇ ℚ. The theorem precisely identifies G with its image, not with all of H."

- question: "The First Isomorphism Theorem guarantees that quotienting G by ker(φ) always produces a group isomorphic to the image of φ, for any homomorphism φ."
  type: true-false
  answer: true
  explanation: "This is the precise statement: G/ker(φ) ≅ im(φ) for any homomorphism φ: G → H. The induced map φ̄(gK) = φ(g) is well-defined (coset representatives don't matter), injective (different cosets map to different images), surjective onto im(φ), and a homomorphism. No additional conditions are required — the result holds universally."

- question: "Why does forming the quotient G/ker(φ) make the induced map φ̄ injective, even when the original homomorphism φ is not injective?"
  type: short-answer
  answer: "φ fails to be injective because distinct elements g and g' can map to the same image — this happens exactly when g'g⁻¹ ∈ ker(φ), meaning g and g' lie in the same coset of ker(φ). Forming G/ker(φ) declares such elements equivalent: g and g' become the same coset gK = g'K. The induced map φ̄ sends each coset to its common image under φ. If φ̄(gK) = φ̄(g'K), then φ(g) = φ(g'), so g'g⁻¹ ∈ ker(φ), so gK = g'K — proving injectivity."
  explanation: "The kernel records exactly what φ 'collapses' — all elements φ cannot distinguish. Quotienting by the kernel merges everything that φ already merged, removing the precise obstruction to injectivity. The quotient group is built to match the information content of φ."
```

## Explainer

You already know two things: how to build quotient groups G/N by collapsing a normal subgroup N into a single identity element, and what it means for two groups to be isomorphic — a structure-preserving bijection between them. The First Isomorphism Theorem is the statement that these two ideas are secretly the same thing. Every homomorphism is, at its core, a quotient map followed by a relabeling.

Here is the key insight. When φ: G → H is a homomorphism, it sends every element of ker(φ) to the identity in H. So φ cannot distinguish between g and gk if k ∈ ker(φ) — they map to the same place. This means φ is really "seeing" the **cosets** of ker(φ), not the individual elements of G. The quotient group G/ker(φ) is precisely the structure you get when you declare "g and gk are the same thing." The theorem says that once you pass to that quotient, the induced map φ̄: G/ker(φ) → im(φ), defined by φ̄(gK) = φ(g), is an isomorphism — it is now bijective and still a homomorphism.

The factoring picture makes this vivid. The original map φ: G → H factors as G → G/ker(φ) → im(φ) → H, where the first arrow is the quotient map (collapsing), the middle arrow is the isomorphism φ̄, and the last arrow is the inclusion of im(φ) into H. The hard part of the proof is checking that φ̄ is well-defined (the coset representative doesn't matter), injective (different cosets map to different images), surjective onto im(φ) (clear from definition), and a homomorphism (inherited from φ). Each step follows directly from the definition of kernel and coset multiplication.

The theorem has an important corollary you will use constantly: if φ is surjective, then im(φ) = H, so G/ker(φ) ≅ H. This is the standard way to prove two groups are isomorphic — find a surjective homomorphism from one to the other, then compute the kernel. For example, the map ℝ → ℝ/ℤ (real numbers mod 1) shows ℝ/ℤ is isomorphic to the circle group. The map ℤ → ℤ/nℤ shows integers mod n are a quotient of the integers. In each case, the First Isomorphism Theorem tells you exactly which quotient gives the target group.
