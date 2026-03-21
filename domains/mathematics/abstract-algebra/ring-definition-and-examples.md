---
id: ring-definition-and-examples
title: Ring Definition and Examples
domain: mathematics
course: abstract-algebra
prerequisites:
- id: binary-operations-and-algebraic-structures
  type: hard
- id: group-definition-and-examples
  type: soft
builds-toward:
- ring-homomorphisms
- subrings-and-ideals
- polynomial-rings
tags:
- rings
- definitions
- examples
stage: advanced
status: draft
---

# Ring Definition and Examples

## Core Idea
A ring has two operations (addition and multiplication) where (R, +) is an abelian group and multiplication is associative with distributivity over addition. Rings can be commutative or not, with or without unity. Examples: integers, polynomials, matrices, Gaussian integers.

## Questions

```yaml
- question: "The set of even integers 2Z = {..., −4, −2, 0, 2, 4, ...} with ordinary addition and multiplication — which of the following is true?"
  type: multiple-choice
  options:
    - "2Z is a field — every nonzero even integer has a multiplicative inverse in 2Z"
    - "2Z is a ring with unity — the element 2 serves as the multiplicative identity"
    - "2Z is a ring without unity — all ring axioms are satisfied, but no multiplicative identity exists in 2Z"
    - "2Z is not a ring — it fails closure under multiplication since products of even integers are not always even"
  answer: 2
  explanation: "2Z satisfies all ring axioms: (2Z, +) is an abelian group (closed, associative, identity 0, inverses, commutative); multiplication is associative; distributivity holds. But there is *no multiplicative identity in 2Z* — no even integer e such that e·n = n for all even n. The integer 1 would work, but 1 ∉ 2Z. This makes 2Z a ring *without unity*. Option B is wrong: 2·4 = 8 ≠ 4, so 2 is not a multiplicative identity. Option D is wrong: 2×2 = 4 ∈ 2Z, so closure under multiplication holds — even integers are always even."

- question: "Which of the following is NOT required by the ring axioms?"
  type: multiple-choice
  options:
    - "Addition is commutative"
    - "Every element has an additive inverse"
    - "Multiplication is commutative"
    - "Multiplication distributes over addition from both sides"
  answer: 2
  explanation: "Commutativity of multiplication is *not* required by the ring axioms — only associativity and distributivity are required for multiplication. The set of 2×2 real matrices M₂(R) is the standard example: it is a ring (with all required axioms satisfied), but matrix multiplication is not commutative (AB ≠ BA in general). A ring where multiplication *is* commutative is specifically called a *commutative ring*. Options A, B, and D are all required: (R, +) must be an abelian group (commutativity of addition, A; additive inverses, B), and distributivity (D) is the key axiom linking the two operations."

- question: "In any ring R, the identity 0·a = 0 for all a ∈ R is a theorem that follows from the ring axioms — it does not need to be assumed as an additional axiom."
  type: true-false
  answer: true
  explanation: "True. Proof using only ring axioms: 0·a = (0 + 0)·a = 0·a + 0·a (by distributivity). Adding the additive inverse of 0·a to both sides (which exists since (R,+) is a group): 0 = 0·a. No additional assumptions are needed. This demonstrates the power of the axiom system — properties that seem obvious often fall out as theorems. The analogous result a·0 = 0 follows from the other distributive law. Zero always 'kills' multiplication, distinguishing the additive identity from any possible multiplicative identity."

- question: "Every ring must contain a multiplicative identity element (unity), just as every ring must contain an additive identity element (zero)."
  type: true-false
  answer: false
  explanation: "False. An additive identity (0) is required — (R, +) must be an abelian group, which mandates an identity element. But a multiplicative identity (1) is *not* required by the ring axioms. Rings possessing a multiplicative identity are called 'rings with unity' or 'unital rings'; those without are valid rings lacking this additional structure. The even integers 2Z are the canonical example: all ring axioms are satisfied, yet no even integer serves as a multiplicative identity. Many important algebraic structures are rings without unity."

- question: "What is a zero divisor in a ring, and why does the ring of integers Z contain no zero divisors?"
  type: short-answer
  answer: "A zero divisor is a nonzero element a in a ring R such that there exists a nonzero element b with ab = 0. In Z, if ab = 0 for integers a and b, then at least one must be zero — this is the fundamental property of integer multiplication. Z is therefore an integral domain (a commutative ring with unity and no zero divisors). By contrast, in Z/6Z, the elements 2 and 3 are both nonzero yet 2·3 = 6 ≡ 0 (mod 6), so both are zero divisors."
  explanation: "Zero divisors are what distinguish general rings from integral domains, and integral domains from fields. The absence of zero divisors enables cancellation: if ab = ac and a ≠ 0, then b = c (multiply both sides by a's inverse in the appropriate sense). This fails in Z/6Z: 2·3 = 2·0 (mod 6) but 3 ≠ 0. Understanding zero divisors is key to the algebraic hierarchy: fields (every nonzero element has a multiplicative inverse) ⊂ integral domains (no zero divisors, commutative, with unity) ⊂ commutative rings ⊂ rings."
```

## Explainer

You already understand **binary operations** and the **group axioms** — closure, associativity, identity, inverses. A ring extends this by adding a second operation and requiring the two operations to interact. Think of a ring as a structure where you can add, subtract (since additive inverses exist), and multiply — but division is not guaranteed. This makes rings a natural abstraction of the integers, where you can certainly add and multiply but dividing two integers rarely gives another integer.

Formally, a **ring** (R, +, ·) requires three things. First, (R, +) is an abelian group: addition is commutative and associative, there is an additive identity 0, and every element has an additive inverse. Second, multiplication is associative: (ab)c = a(bc) for all a, b, c. Third, multiplication distributes over addition from both sides: a(b+c) = ab + ac and (a+b)c = ac + bc. That's all. Multiplication does not need to be commutative, and there need not be a multiplicative identity (a "unity" or "1"). When commutativity holds we call it a **commutative ring**; when a unity exists we call it a **ring with unity** or **unital ring**.

The examples reveal the range of this definition. The integers Z are a commutative ring with unity — the prototypical example. Polynomials with real coefficients R[x] form another commutative ring with unity, where the unity is the constant polynomial 1. The set of 2×2 real matrices M₂(R) is a ring with unity (the identity matrix), but it is *not* commutative — matrix multiplication order matters. The **Gaussian integers** Z[i] = {a + bi : a, b ∈ Z} form a commutative ring with unity inside the complex numbers, which is useful for number theory. The set of even integers 2Z is a commutative ring *without* unity — there is no even number that acts as a multiplicative identity.

One subtlety: in a ring, 0·a = 0 for all a. This follows purely from the axioms without extra assumptions — it is a theorem, not an axiom. Proof: 0·a = (0+0)·a = 0·a + 0·a, and subtracting 0·a from both sides gives 0 = 0·a. This means the additive identity always "kills" multiplication, which distinguishes it from the multiplicative identity. A **zero divisor** is a nonzero element a where ab = 0 for some nonzero b — a phenomenon impossible in the integers but present in Z/6Z (where 2·3 = 0 mod 6). Rings without zero divisors are called **integral domains**, and they sit between general rings and fields in the hierarchy of algebraic structures you will study next.
