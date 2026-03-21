---
id: archimedean-property
title: The Archimedean Property
domain: mathematics
course: real-analysis
prerequisites:
- id: ordered-field-axioms
  type: hard
- id: supremum-and-infimum
  type: hard
builds-toward:
- density-of-rationals
tags:
- archimedean
- properties
- infinite
stage: advanced
status: draft
---

# The Archimedean Property

## Core Idea
The Archimedean Property states that for any positive real numbers a and b, there exists a natural number n such that na > b. This means no element is infinitely large relative to another, and it implies that the natural numbers are unbounded above in ℝ. It is a consequence of the completeness axiom.

## Questions

```yaml
- question: "A student argues: 'The Archimedean Property must be added as a separate axiom when defining ℝ, because the completeness axiom only guarantees that bounded sets have suprema — it says nothing about whether infinitely large elements exist.' What is wrong with this argument?"
  type: multiple-choice
  options:
    - "The student is correct — completeness and the Archimedean Property are logically independent"
    - "The Archimedean Property is already built into the definition of the natural numbers, so it requires no axiom at all"
    - "The Archimedean Property is a theorem: the assumption that ℕ is bounded above in ℝ leads to a contradiction via the least upper bound property"
    - "Completeness only applies to Cauchy sequences, not to properties of the natural numbers"
  answer: 2
  explanation: "The Archimedean Property is a theorem, not an axiom — it follows from the completeness of ℝ (the least upper bound property). If ℕ were bounded above, it would have a supremum M by completeness. But then some n ∈ ℕ exceeds M − 1, so n + 1 > M, contradicting M being an upper bound. Therefore ℕ is unbounded, which is precisely the Archimedean Property. The student's error is treating completeness as too weak to imply it — completeness is exactly what rules out infinitely large elements."

- question: "In an ε-δ proof, you need to find N ∈ ℕ such that 1/N < ε for an arbitrary ε > 0. Which fact from the Archimedean Property directly guarantees this choice is always possible?"
  type: multiple-choice
  options:
    - "The natural numbers are a subset of the real numbers"
    - "For any positive real ε, there exists n ∈ ℕ with n > 1/ε, so 1/n < ε"
    - "The sequence 1/n is bounded below by 0"
    - "ℝ is an ordered field, so division is always well-defined"
  answer: 1
  explanation: "The Archimedean Property (with a = 1, b = 1/ε) guarantees there exists n ∈ ℕ with n·1 > 1/ε, i.e., n > 1/ε, which gives 1/n < ε. This is the corollary used in virtually every ε-N argument. Options A and C are true but do not imply the existence of such N. Option D guarantees 1/ε is well-defined as a real number but not that a natural number exceeds it — that requires the Archimedean Property."

- question: "The Archimedean Property must be included as an explicit axiom when defining the real numbers, because the completeness axiom alone does not prevent ℝ from containing infinitely large elements."
  type: true-false
  answer: false
  explanation: "The Archimedean Property is a theorem proved from completeness, not an additional axiom. The proof: if ℕ were bounded above in ℝ, completeness would give it a supremum M. But then some n > M − 1, so n + 1 > M, contradicting M being an upper bound. Ordered fields that lack the Archimedean Property (containing infinitely large elements) are therefore necessarily incomplete — they violate the least upper bound property. Completeness is sufficient to rule out infinite elements."

- question: "In any ordered field that fails the Archimedean Property, there must exist a positive element smaller than 1/n for every natural number n."
  type: true-false
  answer: true
  explanation: "If a field contains an infinitely large element b (one larger than every natural number), then 1/b is a positive element smaller than 1/n for every n ∈ ℕ — a positive infinitesimal. The two pathologies are dual: the existence of an infinitely large element implies the existence of a positive infinitesimal (its reciprocal), and vice versa. This is precisely what the Archimedean Property rules out on both ends: no element is infinitely large relative to 1, and no positive element is smaller than all terms of the sequence 1/n."

- question: "Why is the Archimedean Property called a theorem rather than an axiom of the real numbers? Sketch the argument that proves it from completeness."
  type: short-answer
  answer: "It is a theorem because it can be derived from the completeness axiom (least upper bound property) without being assumed independently. Proof sketch: Suppose, for contradiction, that ℕ is bounded above in ℝ. By completeness, ℕ has a supremum M. Since M − 1 < M is not an upper bound, there exists n ∈ ℕ with n > M − 1, so n + 1 > M. But n + 1 ∈ ℕ, contradicting M being an upper bound. Therefore ℕ has no upper bound in ℝ — which is exactly the Archimedean Property (taking a = 1)."
  explanation: "Distinguishing axioms from theorems matters because it reveals the logical structure of the real numbers. Only one completeness axiom is needed; the Archimedean Property comes for free. Ordered fields that lack completeness (like certain non-Archimedean fields) show that completeness is genuinely doing the work — remove it and infinitely large elements become possible. The proof is also a template for other arguments: assume a supremum exists, then construct an element that exceeds it, deriving a contradiction."
```

## Explainer

From your study of ordered field axioms, you know that ℝ is an ordered field — addition and multiplication interact with the ordering in the standard ways. But the ordered field axioms alone do not rule out exotic behavior. There exist ordered fields containing elements larger than every natural number — so-called **infinitely large** elements — and elements positive yet smaller than 1/n for every natural number n — **infinitesimal** elements. The rational numbers ℝ and ℚ do not contain such elements, but other ordered fields do. The Archimedean Property is precisely the statement that rules them out.

The property says: given any two positive reals a and b, you can always "reach" b by taking enough copies of a. Formally, there exists n ∈ ℕ with na > b. Think of a as a unit of measurement and b as a distance to cover. No matter how tiny your unit, repeated application eventually surpasses any fixed distance. This is the intuition behind the statement "you can measure any length with a ruler, given enough patience." An ordered field lacking this property would have an element b so large that no multiple of 1 ever exceeds it — b would be genuinely infinite.

The Archimedean Property is not an axiom of ℝ — it is a **theorem**, proved from the completeness of ℝ (the least upper bound property you studied as the supremum axiom). The argument is clean: suppose ℕ were bounded above in ℝ. Then by completeness, ℕ has a supremum, call it M. Since M − 1 < M is not an upper bound, some natural number n satisfies n > M − 1, so n + 1 > M. But n + 1 ∈ ℕ, contradicting M being an upper bound. Therefore ℕ has no upper bound in ℝ, which is exactly the Archimedean Property with a = 1.

Two important corollaries follow immediately. First, for any ε > 0 there exists n ∈ ℕ with 1/n < ε — the sequence 1/n can be made arbitrarily small. This is used constantly in analysis to construct approximations. Second, for any real x there exists an integer n with n > x — the integers are cofinal in ℝ. Together, these two facts undergird nearly every ε-N argument you will write: you choose N large enough so that 1/N < ε, and this choice is always available precisely because of the Archimedean Property.
