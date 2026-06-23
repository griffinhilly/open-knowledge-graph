---
id: group-representations
title: Group Representations
domain: mathematics
course: representation-theory
prerequisites:
- id: group-homomorphisms
  type: hard
- id: linear-transformations
  type: hard
- id: group-actions
  type: soft
builds-toward:
- matrix-representations
- equivalence-of-representations
- reducibility-and-irreducibility
tags:
- representation
- group-homomorphism
- general-linear-group
stage: expert
status: validated
---

# Group Representations

## Core Idea
A representation of a group G is a homomorphism ρ: G → GL(V), where GL(V) is the group of invertible linear transformations on a vector space V. This translates the abstract algebraic structure of a group into concrete linear algebra, where powerful matrix techniques become available. The dimension of V is called the degree of the representation.

## Questions

```yaml
- question: "A student defines a representation of a group G as any function ρ: G → GL(V). What critical condition is missing?"
  type: multiple-choice
  options:
    - "ρ must be injective"
    - "ρ must be a group homomorphism, i.e., ρ(gh) = ρ(g)ρ(h) for all g, h ∈ G"
    - "ρ must be surjective onto GL(V)"
    - "V must be finite-dimensional"
  answer: 1
  explanation: "A representation must preserve the group operation: ρ(gh) = ρ(g)ρ(h). Without this homomorphism condition, the map would assign matrices to group elements arbitrarily, losing all structural information. Injectivity is not required (the trivial representation sends every element to the identity matrix and is perfectly valid). Surjectivity is also not required, and V can be infinite-dimensional in general."

- question: "Every group has at least one representation."
  type: true-false
  answer: true
  explanation: "Every group has the trivial representation, which sends every group element to the identity matrix on a one-dimensional space: ρ(g) = 1 for all g ∈ G. This is clearly a homomorphism since ρ(gh) = 1 = 1·1 = ρ(g)ρ(h). While it carries no information about the group's structure, it is a valid representation. More interestingly, Cayley's theorem guarantees every group has a faithful (injective) representation via permutation matrices."

- question: "The trivial representation sends every group element to the identity transformation. Why is this still considered a legitimate representation despite conveying no structural information about G?"
  type: short-answer
  answer: "It satisfies the definition: it is a homomorphism from G to GL(V), since ρ(gh) = I = I·I = ρ(g)ρ(h) for all g, h ∈ G. Representations are defined by the homomorphism property, not by how much information they carry."
  explanation: "The trivial representation is the kernel-maximal extreme — its kernel is all of G. At the other extreme, a faithful representation has trivial kernel. Both are valid homomorphisms. The trivial representation plays a role analogous to the zero function in analysis: structurally degenerate but necessary for the theory to be clean (e.g., it appears as a summand in decompositions)."

- question: "If G is a finite group of order n, what is the degree of the representation obtained from the left regular action of G on the vector space with basis indexed by elements of G?"
  type: multiple-choice
  options:
    - "1"
    - "n − 1"
    - "n"
    - "n²"
  answer: 2
  explanation: "The left regular representation uses a vector space with one basis vector for each group element, so its dimension equals |G| = n. Each group element g acts by permuting the basis vectors via left multiplication: g·eₕ = e_{gh}. This gives an n-dimensional representation that is always faithful — distinct group elements produce distinct permutation matrices."
```

## Explainer

The central problem of group theory is understanding the structure of groups. One of the most powerful strategies for this is to represent abstract group elements as invertible linear maps on a vector space — that is, as matrices. A **representation** of a group G on a vector space V over a field F is a group homomorphism ρ: G → GL(V), where GL(V) denotes the group of all invertible linear transformations from V to itself. The homomorphism condition ρ(gh) = ρ(g)ρ(h) ensures that the group multiplication is faithfully reflected in matrix multiplication.

Why go through this translation? Because linear algebra is extraordinarily well-developed. We can diagonalize matrices, compute eigenvalues, take traces, and decompose spaces into direct sums. These operations have no direct analogues for abstract groups, but once we have a representation, we can apply all of linear algebra's machinery. A group that seemed opaque as a set with a binary operation becomes transparent when viewed through its action on a vector space.

The simplest example is the cyclic group ℤ/nℤ. A representation of this group on ℂ¹ is determined by where the generator 1 goes: it must map to a matrix (scalar) ζ with ζⁿ = 1, so ζ is an nth root of unity. Each root of unity gives a different one-dimensional representation. For a non-abelian example, the symmetric group S₃ has a two-dimensional representation where each permutation acts on ℝ² as a symmetry of an equilateral triangle — rotations and reflections become 2×2 matrices. This representation "sees" the geometric content of the group.

Two extreme cases frame the landscape. The **trivial representation** sends every element to the identity — it satisfies the homomorphism property vacuously but reveals nothing about G. The **regular representation** uses a vector space whose basis is indexed by the elements of G themselves, with each g ∈ G acting by permuting basis vectors. This representation is always faithful (injective) and contains every irreducible representation of G as a subrepresentation — a fact that makes it central to the structure theory you will develop in subsequent topics.
