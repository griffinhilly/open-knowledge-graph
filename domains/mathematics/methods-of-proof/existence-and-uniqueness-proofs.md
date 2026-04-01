---
id: existence-and-uniqueness-proofs
title: Existence and Uniqueness Proofs
domain: mathematics
course: methods-of-proof
prerequisites:
- id: predicates-and-quantifiers
  type: hard
- id: proof-structure-terminology
  type: soft
tags:
- proof
- existence
- uniqueness
stage: formal-systems
status: validated
---

# Existence and Uniqueness Proofs

## Core Idea
To prove existence ('There exists x such that P(x)'), we construct or describe a specific x satisfying P. To prove uniqueness, we show that if both x and y satisfy P, then x = y. Combined in 'There exists a unique solution', these two components establish both presence and singularity, a powerful form of proof.

## Questions

```yaml
- question: "To prove that a real number x satisfying x² + x − 6 = 0 exists, a student names x = 2 and stops. What is missing from this proof?"
  type: multiple-choice
  options:
    - "Nothing — naming a specific value is sufficient for an existence proof"
    - "A uniqueness argument showing no other value satisfies the equation"
    - "Verification that x = 2 actually satisfies x² + x − 6 = 0"
    - "A proof by contradiction ruling out all other candidates"
  answer: 2
  explanation: "Naming a witness is the right strategy for an existence proof, but naming alone is not sufficient — you must verify that the named object actually satisfies the predicate. The student should confirm: 2² + 2 − 6 = 0. ✓ Without this verification, you've only made a claim. The act of checking is the proof."

- question: "To prove that the solution to Ax = b (for an invertible matrix A) is unique, which strategy is correct?"
  type: multiple-choice
  options:
    - "Show that the formula x = A⁻¹b gives a specific answer — this establishes uniqueness"
    - "Assume x and y are both solutions, then derive x = y using properties of A"
    - "Show that A⁻¹ exists — invertibility alone implies the solution must be unique"
    - "Prove that no other value satisfies Ax = b by checking every possible vector"
  answer: 1
  explanation: "The standard uniqueness proof strategy is 'assume two, show they're equal': suppose Ax = b and Ay = b, then A(x − y) = 0. Since A is invertible, x − y = 0, so x = y. Option A (showing the formula gives a specific answer) establishes existence, not uniqueness — it finds at least one solution but doesn't prove there can't be others. The uniqueness proof must begin by assuming two solutions might exist and then deriving they are equal."

- question: "A uniqueness proof should begin by assuming that there is only one solution to the problem being proved."
  type: true-false
  answer: false
  explanation: "This is the key misconception about uniqueness proofs. You do not assume uniqueness — you prove it. The standard technique begins by assuming the opposite: suppose x and y are both solutions (possibly equal, possibly not). Then you derive x = y. If any two solutions must be equal, the solution is unique. Starting by assuming uniqueness would be circular; the proof works precisely because it makes no such assumption upfront."

- question: "A proof that establishes existence automatically establishes uniqueness — if you can construct a specific object, it is expected to be the main one."
  type: true-false
  answer: false
  explanation: "Existence and uniqueness are entirely independent. Existence says 'at least one solution exists'; uniqueness says 'at most one solution exists.' A construction can yield one of many possible solutions. For example, x² = 4 has two real solutions (x = 2 and x = −2) — existence is trivial, but uniqueness fails. You can construct x = 2 without that being the only solution. This is why existence-and-uniqueness proofs require both components separately."

- question: "Why does mathematics care about proving both existence and uniqueness, rather than just finding a solution?"
  type: short-answer
  answer: "Existence tells you the problem is not vacuous — there is something to find. Uniqueness tells you the solution is well-defined — it makes sense to speak of 'the' solution rather than 'a' solution. Together they justify computing a specific answer and trusting it is the only right one. Without uniqueness, a solution you compute might be one of many, and a different computation could yield a different, equally valid answer."
  explanation: "Consider Ax = b: if A is not invertible, there may be zero solutions (inconsistent) or infinitely many (underdetermined). Existence rules out the first case; uniqueness rules out the second. Only when both hold can you trust that 'solve Ax = b' has a single definitive answer. In physics, a differential equation modeling a physical system should have a unique solution given initial conditions — otherwise the theory fails to make unique predictions."
```

## Explainer

From your study of predicates and quantifiers, you know the difference between ∃x P(x) (there exists something satisfying P) and the stronger claim ∃!x P(x) (there exists exactly one thing satisfying P). Existence-and-uniqueness proofs are the standard technique for establishing this stronger claim. They always split into two parts — and understanding why each part is necessary is the first step.

**Existence** is proven by exhibiting a witness: you name a specific object and verify it satisfies P. This can be done by direct construction ("let x = ..."), by algorithm ("apply this procedure to obtain x"), or by a non-constructive argument ("one of these finitely many cases must satisfy P"). The key rule is that you must actually check that your candidate works — naming it is not enough. If you want to prove that there exists an integer x with x² = 4, you name x = 2 and verify 2² = 4. The verification is the proof.

**Uniqueness** is proven by the "assume two, show they're equal" strategy: suppose both x and y satisfy P(x) and P(y), then derive x = y. This is logically tight: if any two solutions must be equal, there can be at most one. For example, to prove that the additive identity in any group is unique, suppose both e and e′ satisfy the identity axiom. Then e = e · e′ = e′, so e = e′. The proof never assumes there is only one identity — it *proves* it by showing any two must coincide. You can also establish uniqueness by contradiction: assume x ≠ y both satisfy P, then derive an impossibility.

In practice, you will often see these proofs arise in differential equations (does a given initial value problem have a unique solution?), linear algebra (does Ax = b have a unique solution?), and optimization (is there a unique minimum?). The structure is always the same: existence tells you the problem is not vacuous, uniqueness tells you the solution is well-defined. Together they justify computing *the* solution rather than merely *a* solution — a distinction that matters whenever you need to trust that your answer is the only right one.
