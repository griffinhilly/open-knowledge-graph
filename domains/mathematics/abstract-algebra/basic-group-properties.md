---
id: basic-group-properties
title: Basic Group Properties
domain: mathematics
course: abstract-algebra
prerequisites:
- id: group-definition-and-examples
  type: hard
builds-toward:
- subgroups-and-subgroup-test
- cosets-and-lagrange-theorem
tags:
- groups
- properties
- proofs
stage: advanced
status: validated
---

# Basic Group Properties

## Core Idea
Basic group properties include uniqueness of identity and inverses, cancellation laws, and (ab)^{-1} = b^{-1}a^{-1}. These follow directly from axioms and are used throughout group theory. Proofs are brief but build essential intuition.

## Questions

```yaml
- question: "In a group G, which expression correctly gives the inverse of the product ab?"
  type: multiple-choice
  options:
    - "a⁻¹b⁻¹ — inverses of the individual elements in the same order"
    - "b⁻¹a⁻¹ — inverses of the individual elements in reversed order"
    - "b·a — elements in reversed order, uninverted"
    - "(ab)⁻¹ cannot be simplified further without knowing the specific group"
  answer: 1
  explanation: "The socks-and-shoes rule states (ab)⁻¹ = b⁻¹a⁻¹ — the order reverses when taking the inverse of a product. You can verify directly: (ab)(b⁻¹a⁻¹) = a(bb⁻¹)a⁻¹ = a·e·a⁻¹ = aa⁻¹ = e. Option A is the most common error — students apply inverses element-by-element without reversing order, forgetting that non-commutative groups require the reversal. In an abelian (commutative) group, a⁻¹b⁻¹ = b⁻¹a⁻¹ happens to give the same result, but the correct general formula always reverses."

- question: "In a group G, suppose ab = ac for elements a, b, c ∈ G. What can you conclude, and why?"
  type: multiple-choice
  options:
    - "Nothing — cancellation requires the group to be commutative (abelian)"
    - "a = e — only the identity can appear on both sides this way"
    - "b = c — left cancellation holds because every group element has an inverse"
    - "b and c must both equal a⁻¹"
  answer: 2
  explanation: "Left cancellation holds in every group: multiply both sides on the left by a⁻¹ to get a⁻¹(ab) = a⁻¹(ac), then (a⁻¹a)b = (a⁻¹a)c by associativity, so e·b = e·c, therefore b = c. Crucially, this proof uses both the existence of inverses (a⁻¹ exists) and associativity — it does not require commutativity. In a monoid (associative with identity but no guaranteed inverses), cancellation may fail. Option A is the most tempting distractor: students confuse commutativity with cancellability."

- question: "A group can have two distinct identity elements, as long as each satisfies the identity axiom independently."
  type: true-false
  answer: false
  explanation: "The uniqueness of the identity is a theorem, not an additional axiom. If e and e' are both identities, then e = e·e' (because e' is an identity) = e' (because e is an identity). The two supposed identities are forced to be the same element. This brief proof is important: it shows the group axioms are not redundant — they constrain the structure enough to rule out multiple identities without explicitly requiring uniqueness."

- question: "The cancellation law (if ab = ac then b = c) holds in any algebraic structure with a binary operation and an identity element, even without guaranteed inverses."
  type: true-false
  answer: false
  explanation: "Cancellation requires the existence of inverses, not just an identity. The proof multiplies both sides by a⁻¹, which only works if a⁻¹ exists. In a monoid (associative binary operation with identity, but no guaranteed inverses), cancellation can fail. For example, in the monoid of integers under multiplication, 0·3 = 0·5 but 3 ≠ 5, yet 0 has no multiplicative inverse. Groups guarantee inverses for all elements, which is what makes cancellation universally valid."

- question: "Why is it necessary to prove that the identity element of a group is unique, rather than simply assuming uniqueness from the axiom that states an identity exists?"
  type: short-answer
  answer: "The group axiom only states that at least one identity element exists — it says nothing about whether there could be more than one. Without a proof, it would be logically possible that different identities exist satisfying the axiom independently. The proof forces any two identities to be equal using only associativity and the identity property itself: if e and e' are both identities, then e = e·e' = e'. The axioms are sufficient to derive uniqueness, so adding it as a separate assumption would be redundant — but ignoring the proof would leave an unverified gap."
  explanation: "This same reasoning applies to inverse uniqueness: the axiom guarantees at least one inverse per element, but you must prove no element has two distinct inverses. These uniqueness proofs are not mere formalities — they establish that the algebraic structure is well-defined, with a single canonical identity and a single canonical inverse for each element, which every subsequent theorem in group theory depends on."
```

## Explainer

You already know the four group axioms: closure, associativity, existence of an identity, and existence of inverses. What you may not yet realize is that the axioms leave open a silent question — what if a group has *two* different identities? Or what if an element has *two* different inverses? Basic group properties are the proofs that rule this out, and they follow from the axioms alone through surprisingly short arguments.

**Uniqueness of the identity** is proved by assuming e and e' are both identities and watching them collapse: e = e · e' = e'. The first equality holds because e' is an identity (so anything times e' equals that thing), and the second holds because e is an identity. Two identities are forced to be the same element. **Uniqueness of inverses** follows the same logic: if b and c are both inverses of a, then b = b·e = b·(a·c) = (b·a)·c = e·c = c. The associativity axiom is the key engine driving both proofs.

The **cancellation laws** say that if ab = ac then b = c (left cancellation), and if ba = ca then b = c (right cancellation). The proof is immediate: multiply both sides on the left by a⁻¹. These feel obvious because you're used to real number arithmetic, but they are not trivial — they require the existence of inverses guaranteed by the axioms. Note that in a group, left and right cancellation both hold, but in weaker algebraic structures (like monoids, which lack guaranteed inverses) they may not.

The **socks-and-shoes rule** (ab)⁻¹ = b⁻¹a⁻¹ captures the order-reversal that happens when inverting a product. To undo the act of putting on socks *then* shoes, you must remove the shoes *first*, then the socks — the reversal is forced. Algebraically, you verify this by checking that (ab)(b⁻¹a⁻¹) = a(bb⁻¹)a⁻¹ = a·e·a⁻¹ = e. The pattern generalizes: (a₁a₂···aₙ)⁻¹ = aₙ⁻¹···a₂⁻¹a₁⁻¹. These properties are used so constantly in group theory that they quickly become automatic, but the first time you write out each proof you see the full logical weight the axioms are bearing.
