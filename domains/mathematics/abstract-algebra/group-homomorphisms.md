---
id: group-homomorphisms
title: Group Homomorphisms
domain: mathematics
course: abstract-algebra
prerequisites:
- id: group-basic-properties
  type: hard
builds-toward:
- group-isomorphisms
- cosets-lagrange-theorem
- normal-subgroups
tags:
- homomorphisms
- structure-preserving
- kernel
- image
stage: advanced
status: validated
---

# Group Homomorphisms

## Core Idea
A group homomorphism φ: G → H preserves the group operation: φ(ab) = φ(a)φ(b). The kernel ker(φ) = {a ∈ G : φ(a) = e} is a normal subgroup, and the image im(φ) is a subgroup of H. Homomorphisms reveal the underlying structure of groups.

## Questions

```yaml
- question: "Consider the homomorphism φ: ℤ → ℤ/6ℤ defined by φ(n) = n mod 6. What is the kernel of φ?"
  type: multiple-choice
  options:
    - "The set {0, 6} — the only integers that visibly 'look like' multiples of 6"
    - "The set {0, 1, 2, 3, 4, 5} — the elements of the codomain ℤ/6ℤ"
    - "The set of all integer multiples of 6: {…, −12, −6, 0, 6, 12, …}"
    - "The empty set — since φ maps ℤ into a finite group, nothing can map to the identity"
  answer: 2
  explanation: "The kernel consists of all elements of ℤ that map to 0 (the identity of ℤ/6ℤ under addition mod 6). These are exactly the integers divisible by 6: n mod 6 = 0 iff 6 | n. The kernel is an infinite subgroup — the entire lattice 6ℤ. Option B is the most common confusion: students mistake the image (the set of elements φ actually reaches in H, here all of ℤ/6ℤ) for the kernel (the set of elements in G that map to the identity)."

- question: "Suppose φ: G → H is a group homomorphism and g ∈ G has order 4 (meaning g⁴ = e_G but g² ≠ e_G). What must be true of the order of φ(g) in H?"
  type: multiple-choice
  options:
    - "The order of φ(g) must also be exactly 4"
    - "The order of φ(g) must divide 4, so it could be 1, 2, or 4"
    - "The order of φ(g) can be any positive integer"
    - "The order of φ(g) must be greater than 4 to compensate for the collapse"
  answer: 1
  explanation: "Homomorphisms preserve algebraic relations: φ(g⁴) = φ(g)⁴ = φ(e_G) = e_H. So φ(g)⁴ = e_H, meaning the order of φ(g) divides 4. The actual order could be 1 (φ(g) = e_H, the kernel case), 2, or 4 — any divisor of 4. It cannot exceed 4. Option A is the common misconception that homomorphisms preserve orders exactly; they preserve the relation g^n = e but allow the image to have smaller order (by mapping multiple elements to the same image)."

- question: "The kernel of any group homomorphism is always a normal subgroup of the domain group."
  type: true-false
  answer: true
  explanation: "Normality of the kernel follows directly from the homomorphism property. If k ∈ ker(φ), then for any g ∈ G: φ(gkg⁻¹) = φ(g)φ(k)φ(g⁻¹) = φ(g)·e_H·φ(g)⁻¹ = e_H. Therefore gkg⁻¹ ∈ ker(φ), which is exactly the definition of normality. This is not a coincidence — normality is precisely what allows the quotient group G/ker(φ) to be defined, leading to the First Isomorphism Theorem."

- question: "If a group homomorphism φ: G → H sends two different elements of G to the same element of H, then φ can rarely be a valid homomorphism."
  type: true-false
  answer: false
  explanation: "A homomorphism only needs to satisfy φ(ab) = φ(a)φ(b) — it does not need to be injective (one-to-one). Many valid homomorphisms are non-injective: the map φ(n) = n mod 6 sends infinitely many integers to the same residue class, yet is a perfectly valid homomorphism. Injectivity is an additional property (equivalent to ker(φ) = {e_G}), not a requirement for being a homomorphism. A homomorphism that is both injective and surjective is an isomorphism."

- question: "Why must the kernel of a group homomorphism be a normal subgroup, rather than merely any subgroup?"
  type: short-answer
  answer: "Normality is forced by the homomorphism property itself, not imposed as an extra condition. For any k in the kernel and any g in G, the calculation φ(gkg⁻¹) = φ(g)φ(k)φ(g⁻¹) = φ(g)·e_H·φ(g)⁻¹ = e_H shows that gkg⁻¹ is also in the kernel. This holds for all g, which is exactly the definition of a normal subgroup. Normality matters because it is precisely the condition needed to define the quotient group G/ker(φ), making the First Isomorphism Theorem (G/ker(φ) ≅ im(φ)) possible — the kernel's normality is what enables the quotient construction."
  explanation: "Conversely, every normal subgroup N ◁ G is the kernel of some homomorphism — namely the quotient map G → G/N. This gives a complete characterization: the kernels of group homomorphisms are exactly the normal subgroups."
```

## Explainer

A group homomorphism is a map that respects the group operation — if you combine two elements first and then map the result, you get the same answer as mapping each element individually and then combining. This structural respect is what makes homomorphisms powerful: they let you transport information from one group to another while preserving the algebraic relationships you care about. The defining equation φ(ab) = φ(a)φ(b) says that the map commutes with the operation.

From your study of group basic properties, you know a group has an identity element and every element has an inverse. The homomorphism property automatically preserves both: φ(e_G) = e_H (the identity maps to the identity), and φ(a⁻¹) = φ(a)⁻¹ (inverses map to inverses). These aren't additional requirements — they follow for free from the single defining equation. This is a recurring theme in algebra: a small structural requirement implies a cascade of consequences.

The two most important objects associated to a homomorphism are its **kernel** and its **image**. The kernel ker(φ) = {a ∈ G : φ(a) = e_H} is the set of elements that get "collapsed" to the identity in H. The image im(φ) is the subset of H that φ actually reaches. Both are subgroups — the kernel is a subgroup of G, and the image is a subgroup of H. The kernel has an extra property that the image lacks: it is a **normal subgroup**, meaning gker(φ)g⁻¹ = ker(φ) for every g ∈ G. This normality is not an accident; it is precisely what allows you to build a quotient group G/ker(φ) and identify it with the image.

To make this concrete: consider the map φ: ℤ → ℤ/nℤ that sends each integer to its remainder mod n. This is a homomorphism because φ(a + b) = (a + b) mod n = ((a mod n) + (b mod n)) mod n = φ(a) + φ(b). Its kernel is the set of multiples of n (those integers that map to 0), and its image is all of ℤ/nℤ. The homomorphism exactly encodes what modular arithmetic does to the integers. Recognizing the abstract homomorphism structure in this familiar operation is the moment the definition shifts from symbol-shuffling into genuine understanding — and prepares you for the First Isomorphism Theorem, which makes the G/ker(φ) ≅ im(φ) relationship precise.
