---
id: injections-surjections-bijections-classification
title: Injections, Surjections, and Bijections
domain: formal-sciences-and-logic
course: set-theory
prerequisites:
- id: functions-and-mappings-formal
  type: hard
builds-toward:
- cardinality-and-equinumerosity
tags:
- injective
- surjective
- bijective
- one-to-one
- onto
stage: formal-systems
status: validated
---

# Injections, Surjections, and Bijections

## Core Idea
An injection preserves distinctness: f(a) = f(b) implies a = b. A surjection covers the codomain: every b ∈ B equals f(a) for some a. A bijection is both injective and surjective, establishing a perfect one-to-one correspondence. Bijections are invertible and preserve cardinality across sets.

## How It's Best Learned
Use definitions directly to prove properties. For example, f(x) = 2x on ℝ is bijective; f(x) = x² on ℝ is neither injective nor surjective, but becomes bijective when restricted to [0,∞) → [0,∞). Construct counterexamples to distinguish the concepts.

## Common Misconceptions
- Confusing 'onto' (surjective) with 'one-to-one' (injective). - Thinking a function must be defined by a formula; what matters is the assignment rule. - Assuming bijections exist only between finite sets (false; bijections exist between infinite sets of equal cardinality).

## Questions

```yaml
- question: "The function f: ℝ → ℝ defined by f(x) = x² is neither injective nor surjective. If we restrict the domain and codomain to [0, ∞) → [0, ∞), what changes?"
  type: multiple-choice
  options:
    - "It becomes injective but not surjective — negative outputs are excluded but the function is still many-to-one for some inputs"
    - "It becomes surjective but not injective — the codomain now matches the range, but two inputs can still share an output"
    - "It becomes bijective — distinct non-negative inputs produce distinct outputs, and every non-negative real has a square root"
    - "It remains neither — the formula f(x) = x² is fundamentally non-bijective regardless of domain"
  answer: 2
  explanation: "On all of ℝ, f(x) = x² fails injectivity (3 and -3 both map to 9) and surjectivity (negative numbers have no preimage). Restricting to [0,∞) → [0,∞) fixes both: non-negative inputs are all distinct after squaring (injectivity), and every non-negative real number b has a square root √b in the domain (surjectivity). This illustrates that injectivity and surjectivity are properties of a function together with its domain and codomain — changing either can change the classification."

- question: "What does exhibiting a bijection between two infinite sets prove about those sets?"
  type: multiple-choice
  options:
    - "That the two sets are identical — they contain exactly the same elements"
    - "That the two sets have the same cardinality — the same 'size' in a precise mathematical sense"
    - "That one set is a subset of the other"
    - "Nothing useful — bijections only apply to finite sets where elements can be counted"
  answer: 1
  explanation: "A bijection is a perfect one-to-one correspondence: every element of A pairs with exactly one element of B, and vice versa. This is the formal definition of 'same size' for sets — two sets have the same cardinality if and only if there exists a bijection between them. For finite sets this matches ordinary counting. For infinite sets it produces surprising results: f(n) = 2n is a bijection from ℕ to the even naturals, proving they have the same cardinality even though the evens seem like 'half' of the naturals."

- question: "The function f(n) = 2n from the natural numbers ℕ to the even natural numbers is a bijection, which proves that the even natural numbers and all natural numbers have the same cardinality."
  type: true-false
  answer: true
  explanation: "f(n) = 2n is injective (if 2m = 2n then m = n) and surjective onto the even naturals (every even number 2k equals f(k)). So it is a bijection. The existence of this bijection means ℕ and the even naturals are equinumerous — they have the same cardinality, both ℵ₀. This seems paradoxical because the evens are a proper subset of ℕ, yet they're the 'same size.' This counterintuitive result is a defining feature of infinite sets and one of the reasons bijection-based cardinality is so important in set theory."

- question: "Whether a function is surjective depends only on its defining formula, not on what codomain is specified."
  type: true-false
  answer: false
  explanation: "Surjectivity requires that every element of the codomain is the image of some element in the domain. The codomain is part of the definition of the function — change it and you can change whether the function is surjective. f(x) = x² with codomain ℝ is not surjective (negative numbers are never outputs). The same formula with codomain [0,∞) is surjective (every non-negative real is a square). A function's classification as surjective, injective, or bijective always depends on both its domain and its codomain, not the formula alone."

- question: "Explain in your own words why a bijection between sets A and B is called a 'same size' certificate: why does the existence of a bijection prove the sets have the same number of elements?"
  type: short-answer
  answer: "A bijection pairs each element of A with exactly one element of B, and each element of B with exactly one element of A — no element is left unmatched on either side. This is exactly what 'same number' means: you can count them together simultaneously. For finite sets, this matches ordinary counting. For infinite sets, bijections extend the idea of 'same size' to cases where we can't literally count: if you can establish a perfect pairing, the sets are equinumerous by definition, regardless of how the elements are described."
  explanation: "This is why Cantor's bijection-based cardinality theory is so powerful. It lets us compare the sizes of infinite sets without counting. Two sets have the same cardinality if and only if a bijection exists between them. Sets with no bijection to ℕ (like ℝ) are 'uncountably infinite' and strictly larger. The bijection is the formal machinery that makes 'same size' precise and computable for any sets, finite or infinite."
```

## Explainer

You already know that a **function** assigns to each element of a domain exactly one element of a codomain. The three classifications — injection, surjection, bijection — are about two different ways a function can "behave well" with respect to that assignment. Think of a function as an arrow diagram: each element on the left points to exactly one element on the right. The question is what patterns those arrows can form.

An **injection** (or one-to-one function) means no two elements on the left share the same target: every arrow lands in a distinct spot. Formally, f(a) = f(b) implies a = b. The contrapositive is equally useful: if a ≠ b, then f(a) ≠ f(b). A good mental image is that injections "spread out" — the domain can fit inside the codomain without collisions. The function f(x) = 2x from ℤ to ℤ is injective: different integers get sent to different even integers. The function f(x) = x² on ℝ is not injective because 3 and −3 both map to 9.

A **surjection** (or onto function) means every element on the right is hit by at least one arrow — nothing in the codomain is left uncovered. Formally, for every b in the codomain, there exists some a in the domain with f(a) = b. The function f(x) = x³ from ℝ to ℝ is surjective because every real number has a real cube root. But f(x) = x² from ℝ to ℝ is not surjective because negative numbers have no preimage. Notice that injectivity and surjectivity are independent: a function can have either, both, or neither. The codomain matters — f(x) = x² restricted to [0,∞) → [0,∞) becomes surjective.

A **bijection** achieves both simultaneously: it is a perfect one-to-one correspondence between domain and codomain. Every element on the left pairs with exactly one element on the right, and vice versa. Bijections are the "same size" certificates for sets — if you can exhibit a bijection between A and B, you have proven they have the same cardinality. This is profound: the bijection f(n) = 2n from ℕ to the even natural numbers proves the evens and the naturals are the same size, even though the evens seem "smaller." Bijections are also precisely the invertible functions: if f is a bijection, there is a unique function f⁻¹ that undoes it. This connection between bijections and invertibility will be central when you study cardinality, permutations, and group theory.
