---
id: order-of-group-element
title: Order of a Group Element
domain: mathematics
course: abstract-algebra
prerequisites:
- id: cyclic-groups
  type: hard
builds-toward:
- cosets-and-lagrange-theorem
- sylow-theorems
tags:
- order
- elements
- properties
stage: advanced
status: validated
---

# Order of a Group Element

## Core Idea
The order of element a is the smallest positive integer n with a^n = e. Infinite order elements exist in infinite groups. The order divides |G| for finite groups; elements of order n generate cyclic subgroups of order n.

## How It's Best Learned
Compute orders in Z/nZ and symmetric groups. Verify that the set {e, a, a^2, ..., a^{n-1}} forms a cyclic subgroup of order n.

## Common Misconceptions
- Confusing the order of an element with the order of the group containing it.
- Assuming the order is always positive; we define it only for finite orders.

## Questions

```yaml
- question: "In ℤ/12ℤ (integers mod 12 under addition), what is the order of the element 4?"
  type: multiple-choice
  options:
    - "4, because 4 is the element itself"
    - "12, because the group has 12 elements and every element must traverse the whole group"
    - "3, because 4 + 4 + 4 = 12 ≡ 0 (mod 12) — three steps reach the identity"
    - "6, because the order of an element is always |G| divided by the element"
  answer: 2
  explanation: "The order of an element is the smallest positive integer n such that n copies of the element (under the group operation) equal the identity. In ℤ/12ℤ, we add: 4+4 = 8, 4+4+4 = 12 ≡ 0. Three steps reach 0, so ord(4) = 3. Note that option D reflects a common error — |G|/a is not a formula for element order. The correct relationship is that gcd(a, |G|) determines the order in cyclic groups: ord(4) = 12/gcd(4,12) = 12/4 = 3."

- question: "A group G has order 21. Which of the following element orders is IMPOSSIBLE in G?"
  type: multiple-choice
  options:
    - "1"
    - "3"
    - "6"
    - "7"
  answer: 2
  explanation: "By Lagrange's theorem, the order of any element must divide the order of the group. Since 21 = 3 × 7, the divisors of 21 are 1, 3, 7, and 21. The number 6 does not divide 21 (21/6 is not an integer), so no element of order 6 can exist in G. This is one of the most powerful applications of element order: without constructing G explicitly, we can rule out entire families of element orders just by factoring |G|."

- question: "If an element a has order n in a group G, then the set {e, a, a², ..., aⁿ⁻¹} forms a cyclic subgroup of G with exactly n elements."
  type: true-false
  answer: true
  explanation: "This is the fundamental structural consequence of element order. The powers of a are all distinct (if aⁱ = aʲ for i < j, then a^(j−i) = e, contradicting the minimality of n), so there are exactly n of them. They form a subgroup — closed under the group operation and containing inverses — isomorphic to ℤ/nℤ. So ord(a) simultaneously tells you how many steps before you cycle back and the size of the smallest subgroup containing a. These are the same thing."

- question: "In a group of order 20, it is possible for an element to have order 6."
  type: true-false
  answer: false
  explanation: "By Lagrange's theorem, the order of an element must divide the order of the group. Since 6 does not divide 20 (20 = 4 × 5; divisors are 1, 2, 4, 5, 10, 20), no element of order 6 can exist in any group of order 20. This constraint is absolute — it requires no knowledge of the group's specific structure, only its size."

- question: "Why does the order of an element in a finite group necessarily divide the order of the group? Trace the argument through subgroup theory."
  type: short-answer
  answer: "The powers of an element a of order n form a cyclic subgroup H = {e, a, a², ..., aⁿ⁻¹} of size n. By Lagrange's theorem, the size of any subgroup of a finite group G must divide |G|. Since |H| = n = ord(a), it follows that ord(a) divides |G|."
  explanation: "The chain of reasoning is: element order → size of generated cyclic subgroup → Lagrange's theorem → divisibility. Each step is tight: ord(a) = n exactly because the n powers are all distinct and aⁿ = e; those n elements form a genuine subgroup; and Lagrange proves any subgroup's size divides |G| by the coset partition argument. This means knowing |G| immediately constrains which orders are possible, making element order one of the primary tools for deducing group structure."
```

## Explainer

From cyclic groups, you already know that a single element a can generate an entire group by repeatedly applying the group operation: a, a², a³, and so on. The **order of an element** formalizes how long this process takes before you return to the identity. Formally, ord(a) is the smallest positive integer n such that aⁿ = e. If no such n exists, a has infinite order. Think of it as the "period" of a in the group — after n steps, you're back where you started.

Computing order is concrete and mechanical. In ℤ/12ℤ (integers mod 12 under addition), the element 4 has order 3, because 4+4+4 = 12 ≡ 0 (mod 12) — three steps to reach the identity. The element 5 has order 12, because gcd(5,12) = 1, so 5 generates the whole group before returning to 0. In the symmetric group S₃, a 3-cycle like (1 2 3) has order 3 (apply it three times and every element returns to its original position), while a transposition (1 2) has order 2. In general, the order of a k-cycle in Sₙ is k, and the order of a product of disjoint cycles is the least common multiple of their lengths.

A crucial structural fact: the powers {e, a, a², ..., aⁿ⁻¹} form a **cyclic subgroup** of order n. This subgroup is generated by a and is isomorphic to ℤ/nℤ. So the order of an element is simultaneously the size of the smallest subgroup containing it. This connects order to subgroup structure: every element carves out a cyclic subgroup whose size equals the element's order.

The deepest consequence is **Lagrange's theorem** (which you'll encounter next): the order of any subgroup divides the order of the group. Since ord(a) is the size of a subgroup, it follows that ord(a) divides |G| for any finite group G. This is a powerful constraint — it immediately rules out certain element orders. In a group of order 15, elements can only have orders 1, 3, 5, or 15. You can't have an element of order 4 in a group of size 15, because 4 does not divide 15. Order arithmetic is one of the main tools for deducing the structure of finite groups without constructing them explicitly.


