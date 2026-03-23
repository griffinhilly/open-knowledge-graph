---
id: proving-by-cases
title: Proving by Cases and Exhaustion
domain: mathematics
course: methods-of-proof
prerequisites:
- id: proving-by-direct-method
  type: hard
builds-toward:
- vacuous-truth-and-trivial-cases
tags:
- proof
- cases
- exhaustion
- disjunction
stage: formal-systems
status: validated
---

# Proving by Cases and Exhaustion

## Core Idea
To prove a statement P, divide the domain or hypothesis into mutually exclusive and exhaustive cases, then prove P in each case. If P holds in all cases, it holds in general. This method is used when a direct proof is unwieldy or when the proof naturally breaks into distinct scenarios.

## How It's Best Learned
Identify when a statement naturally breaks into cases (e.g., integer parity, modular arithmetic). Ensure all cases are covered and are mutually exclusive.

## Common Misconceptions
- Forgetting to cover all cases.
- Allowing cases to overlap without recognizing it.
- Assuming one case 'represents' the others without proving all.

## Questions

```yaml
- question: "A student wants to prove a statement about all real numbers using proof by cases. They split into: (i) x > 0, (ii) x < 0. Is this proof complete?"
  type: multiple-choice
  options:
    - "Yes — positive and negative reals cover all reals"
    - "No — the cases are not mutually exclusive"
    - "No — the case x = 0 is missing, making the proof non-exhaustive"
    - "No — you need at least four cases for a proof by cases to be valid"
  answer: 2
  explanation: "The cases x > 0 and x < 0 are mutually exclusive (they cannot both be true), but they are not exhaustive — they omit x = 0. Since 0 is a real number, the proof has a gap and is incomplete. A proof by cases fails the moment any element of the domain is not covered by at least one case. The requirement is exhaustiveness, not a minimum number of cases — two cases are fine if they truly cover everything."

- question: "A proof of 'P holds for all integers' is conducted in two cases: n is even and n is odd. Within the even case, the prover writes n = 2k and uses that fact. What is the structural advantage of having the case assumption?"
  type: multiple-choice
  options:
    - "It allows the prover to assume the conclusion P is true inside the case"
    - "It supplies an additional hypothesis — the concrete form n = 2k — that would not be available in a general direct proof"
    - "It eliminates the need to prove the odd case separately"
    - "It converts the proof into a proof by contradiction"
  answer: 1
  explanation: "Within a case, you know not just the original hypothesis but also the case condition itself — here, that n is even, which means n = 2k for some integer k. That concrete algebraic form is often exactly what enables the sub-proof: it unlocks arithmetic manipulations that are unavailable when n is an arbitrary integer. This is the real power of case-splitting: each case provides extra fuel for its own sub-argument. Options A and C misstate the structure — you still prove P separately in each case, and the case assumption never lets you assume the conclusion."

- question: "In a proof by cases, it is acceptable for the cases to overlap — i.e., some elements can belong to more than one case."
  type: true-false
  answer: true
  explanation: "Cases must be exhaustive (collectively cover the whole domain) but need not be mutually exclusive. If an element falls under multiple cases, it just means you prove the statement for that element in two different ways — both proofs are valid and the conclusion still holds. For example, dividing integers into {n ≡ 0 mod 6}, {n ≡ 1 mod 6}, ..., {n ≡ 5 mod 6} is fine even though you could have used just even/odd. The danger is missing cases, not having too many."

- question: "If you prove a statement for positive integers and separately prove it for even integers, you have proven the statement for all non-negative integers."
  type: true-false
  answer: false
  explanation: "Positive integers and even integers are not an exhaustive partition of the non-negative integers. Positive integers cover {1, 2, 3, ...} and even integers cover {0, 2, 4, ...}. Together they miss only nothing... wait — actually they do cover all non-negative integers (0 is even, and all positive integers are covered). But the better point is: the cases must be explicitly shown to collectively cover the domain. Proving for positive integers and for even integers is redundant in places and the case split is not the natural exhaustive partition. More concretely, if you tried the analogous trick for all integers — proving for positive and for even — you'd miss negative odd integers entirely."

- question: "Why does the proof-by-cases technique succeed when a direct proof would be unwieldy or impossible?"
  type: short-answer
  answer: "Because within each case, you gain the case assumption as an additional hypothesis that restricts which elements you're reasoning about. A direct proof must handle all elements simultaneously without that extra information. When a statement has different 'reasons' for being true in different parts of the domain, no single chain of reasoning covers all of them — but separate proofs, each empowered by their case's specific assumption, can each succeed."
  explanation: "The logical mechanism is a disjunction: if you know (P₁ ∨ P₂ ∨ ... ∨ Pₙ) covers the domain, and you show Q follows from each Pᵢ separately, then Q holds everywhere. The cases create sub-problems with stronger starting assumptions, and the reassembly is guaranteed by logical disjunction. This is why integer parity proofs are so natural for this technique — every integer is either even or odd, and each form gives you a concrete substitution that drives the algebra."
```

## Explainer

You already know how to construct a direct proof: assume the hypothesis, then derive the conclusion through a chain of valid inference steps. But sometimes the path from hypothesis to conclusion is not a single straight line — the hypothesis splits into distinct scenarios that require different reasoning. **Proof by cases** is the technique for handling this: divide, conquer each piece separately, then reassemble.

The logical foundation is simple. Suppose you know that at least one of P₁, P₂, ..., Pₙ is true (the cases cover all possibilities), and you can prove Q from each Pᵢ individually. Then Q must be true. In symbols: if (P₁ ∨ P₂ ∨ ··· ∨ Pₙ) and (Pᵢ → Q for each i), then Q. The strength of the method is that within each case, you can use the case assumption as an additional hypothesis — an assumption not available in a general direct proof. That added assumption often makes what was intractable become straightforward.

The most important structural requirement is **exhaustiveness**: your cases must collectively cover the entire domain. If you prove a statement for even integers and odd integers separately, you have covered all integers — because every integer is either even or odd. But if you prove something for positive reals and negative reals and forget zero, your proof has a gap. Overlapping cases are fine (you can have more cases than necessary), but missing cases are fatal. Common natural case splits arise from: parity (even/odd), sign (positive/negative/zero), inequalities (x < 1, x = 1, x > 1), divisibility classes, and whether a particular element is in a set or not.

Consider proving that n² + n is always even for any integer n. A direct proof without cases is possible but feels awkward. With cases: if n is even, write n = 2k, then n² + n = 4k² + 2k = 2(2k² + k), which is even. If n is odd, write n = 2k + 1, then n² + n = (2k+1)² + (2k+1) = 4k² + 4k + 1 + 2k + 1 = 4k² + 6k + 2 = 2(2k² + 3k + 1), which is even. Both cases give even results; the cases are exhaustive; the proof is complete. The case structure does not just organize the proof — it actively enables each sub-proof by supplying the concrete form of n.
