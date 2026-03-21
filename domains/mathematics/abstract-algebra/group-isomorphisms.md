---
id: group-isomorphisms
title: Group Isomorphisms
domain: mathematics
course: abstract-algebra
prerequisites:
- id: group-homomorphisms
  type: hard
builds-toward:
- cosets-lagrange-theorem
- first-isomorphism-theorem-groups
tags:
- isomorphisms
- bijective
- structure-preserving
- equivalent-groups
stage: advanced
status: draft
---

# Group Isomorphisms

## Core Idea
A group isomorphism is a bijective homomorphism. Two groups are isomorphic if there exists an isomorphism between them, meaning they have identical algebraic structure. Isomorphic groups differ only in notation.

## Questions

```yaml
- question: "Consider ℤ₄ = {0,1,2,3} under addition mod 4, and the Klein four-group V₄ = {e,a,b,c} where every non-identity element satisfies x² = e. Both have order 4. Are they isomorphic?"
  type: multiple-choice
  options:
    - "Yes — any two groups of the same order are isomorphic by the classification theorem"
    - "No — ℤ₄ has an element of order 4, but V₄ has no element of order 4, and order of elements is a structural invariant preserved by any isomorphism"
    - "No — ℤ₄ is written additively and V₄ multiplicatively, so they cannot be compared"
    - "Yes — a bijection exists between any two sets of the same size, which is sufficient for isomorphism"
  answer: 1
  explanation: "Two isomorphic groups must have the same number of elements of each order — this is a structural invariant preserved by any isomorphism. In ℤ₄, the element 1 has order 4 (1+1+1+1 = 0 mod 4). In V₄, every non-identity element has order 2 (a²=e for all a≠e) — there is no element of order 4. Since any isomorphism φ: ℤ₄ → V₄ would have to send an order-4 element to an element of the same order, and V₄ has none, no such isomorphism can exist. The existence of a bijection between the underlying sets is necessary but not sufficient; the bijection must also preserve the group operation."

- question: "What does it mean to say two groups G and H are isomorphic?"
  type: multiple-choice
  options:
    - "G and H have the same number of elements"
    - "There exists a surjective group homomorphism from G to H"
    - "There exists a bijective map φ: G → H that preserves the group operation: φ(ab) = φ(a)φ(b) for all a,b ∈ G"
    - "G and H have the same generators and the same identity element"
  answer: 2
  explanation: "Isomorphism requires three things simultaneously: the map must be (1) a homomorphism (operation-preserving), (2) injective (one-to-one), and (3) surjective (onto). Same cardinality alone (option A) fails because ℤ₄ and V₄ have the same size but are not isomorphic. A surjective homomorphism alone (option B) fails because it might not be injective — for example, there is a surjective homomorphism from ℤ to ℤ/nℤ, but they are not isomorphic. Option D is not a definition. The bijective homomorphism condition captures the precise meaning: the two groups have identical algebraic structure, differing only in how their elements are named."

- question: "Any two cyclic groups of the same finite order are isomorphic to each other."
  type: true-false
  answer: true
  explanation: "This is a theorem: all cyclic groups of order n are isomorphic to ℤₙ (integers mod n under addition). If G and H are both cyclic of order n, let g generate G and h generate H. The map φ(gᵏ) = hᵏ is a well-defined bijection (since both groups have exactly n elements and cyclic structure is identical) and preserves the operation: φ(gʲ · gᵏ) = φ(gʲ⁺ᵏ) = hʲ⁺ᵏ = hʲ · hᵏ = φ(gʲ)φ(gᵏ). Every cyclic group of order n is 'the same' abstract group — only the names of the elements differ."

- question: "If G and H are isomorphic groups, and G is abelian (commutative), then H must also be abelian."
  type: true-false
  answer: true
  explanation: "Commutativity is a structural property preserved by isomorphism. If φ: G → H is an isomorphism and G is abelian, then for any x,y ∈ H, write x = φ(a) and y = φ(b) for unique a,b ∈ G. Then xy = φ(a)φ(b) = φ(ab) = φ(ba) = φ(b)φ(a) = yx, using the homomorphism property and the commutativity of G. So H is abelian. More generally, any property that can be stated purely in terms of the group operation — element orders, number of subgroups, solvability, nilpotency — is an isomorphism invariant and must be shared by isomorphic groups."

- question: "How would you prove that two groups of the same order are NOT isomorphic? Give a strategy and illustrate it with an example."
  type: short-answer
  answer: "To prove two groups are not isomorphic, find a structural invariant — a property preserved by any isomorphism — that differs between them. An isomorphism φ must map elements of order k to elements of order k (since |φ(g)| = |g|), preserve commutativity, and preserve the number of elements of each order. For example, to show ℤ₄ ≇ V₄: ℤ₄ has an element of order 4 (the generator), while V₄ has no element of order 4 (every non-identity element has order 2). Any isomorphism would have to map the order-4 element of ℤ₄ to an element of order 4 in V₄, but none exists. Contradiction — they cannot be isomorphic."
  explanation: "This strategy is how you distinguish non-isomorphic groups in practice: list the element orders, check commutativity, count subgroups, check for cyclic generators. Two groups are isomorphic only if they agree on ALL such invariants. If they disagree on even one, they are not isomorphic. Note that agreeing on all known invariants does not prove isomorphism — you must also exhibit the actual bijective homomorphism. Invariants are useful for ruling out isomorphism (disproofs); explicit construction is needed for proofs."
```

## Explainer

You've already studied **homomorphisms** — maps φ: G → H that preserve the group operation, meaning φ(ab) = φ(a)φ(b). A homomorphism is the group-theoretic notion of "structure-preserving map." An **isomorphism** is a homomorphism with one additional requirement: bijectivity. The map must be one-to-one (injective) and onto (surjective). When such a map exists, we write G ≅ H and say the groups are *isomorphic*.

The intuition is that isomorphic groups are the same group wearing different clothes. Consider the group of integers under addition modulo 4 ({0,1,2,3} with operation +₄) and the group of rotations of a square ({0°, 90°, 180°, 270°} with operation "followed by"). Both have order 4, both have a generator that cycles through all elements, and the structure of their Cayley tables is identical. The map φ(k) = rotation by 90k degrees is a bijective homomorphism — an isomorphism. In abstract algebra, these two groups are indistinguishable; any theorem proved for one holds for the other.

Not all groups of the same order are isomorphic. Consider two groups of order 4: **ℤ₄** (cyclic, with a single generator of order 4) and the **Klein four-group V₄** (where every non-identity element has order 2, i.e., a² = e for all a). These have the same size but different algebraic structure: ℤ₄ has an element of order 4, V₄ does not. No bijection between them can preserve the group operation, so V₄ ≇ ℤ₄. To prove two groups are *not* isomorphic, you find a structural invariant — a property preserved by any isomorphism, like the order of elements, the number of elements of each order, or commutativity — that differs between the two groups.

Isomorphisms are the equivalence relation of group theory: they tell you when two groups are "the same" at the level of abstract structure. The **First Isomorphism Theorem**, which you'll study next, makes this even more powerful by connecting isomorphisms to quotient groups — showing that every homomorphism "factors through" an isomorphism in a canonical way.
