---
id: de-morgans-laws
title: De Morgan's Laws
domain: mathematics
course: methods-of-proof
prerequisites:
- id: logical-equivalences
  type: hard
builds-toward:
- proof-structure-and-terminology
tags:
- equivalence
- negation
- logic
stage: formal-systems
status: validated
---

# De Morgan's Laws

## Core Idea
De Morgan's Laws state that ¬(p ∧ q) ≡ ¬p ∨ ¬q and ¬(p ∨ q) ≡ ¬p ∧ ¬q. These laws describe how negation distributes over AND and OR, essential for manipulating logical expressions.

## Questions

```yaml
- question: "A security system unlocks only when both a key AND a fingerprint are provided. A technician says: 'If the door fails to open, then the key must be wrong AND the fingerprint must be wrong.' According to De Morgan's first law, what is the correct negation?"
  type: multiple-choice
  options:
    - "The key is wrong AND the fingerprint is wrong (technician is correct)"
    - "The key is wrong OR the fingerprint is wrong (the failure of a conjunction is a disjunction of failures)"
    - "Neither the key nor the fingerprint is required"
    - "The key is wrong OR the fingerprint is correct"
  answer: 1
  explanation: "De Morgan's first law: ¬(p ∧ q) ≡ ¬p ∨ ¬q. The door fails when it is NOT the case that both conditions hold — meaning at least one condition fails. The technician's error is keeping AND after negation; De Morgan's says the connective must flip to OR."

- question: "Which of the following correctly applies De Morgan's Laws to simplify ¬(A ∨ B ∨ C)?"
  type: multiple-choice
  options:
    - "¬A ∨ ¬B ∨ ¬C"
    - "¬A ∧ ¬B ∨ ¬C"
    - "¬A ∧ ¬B ∧ ¬C"
    - "¬(A ∧ B ∧ C)"
  answer: 2
  explanation: "By iterated application of De Morgan's second law (¬(p ∨ q) ≡ ¬p ∧ ¬q), negating a disjunction of any length produces a conjunction of all the negated components. Each OR flips to AND, and each variable gets negated. Mixing ∨ and ∧ in the result (option B) would be incorrect."

- question: "¬(p ∧ q) is logically equivalent to ¬p ∧ ¬q — negation distributes over AND while leaving the connective unchanged."
  type: true-false
  answer: false
  explanation: "This is the most common De Morgan's error. Negation does not pass through a connective unchanged: ¬(p ∧ q) ≡ ¬p ∨ ¬q. The connective flips from AND to OR. Verify with p = T, q = F: ¬(T ∧ F) = ¬F = T, but ¬T ∧ ¬F = F ∧ T = F. The two expressions differ."

- question: "De Morgan's Laws apply to set theory as well as propositional logic: the complement of an intersection equals the union of the complements, and the complement of a union equals the intersection of the complements."
  type: true-false
  answer: true
  explanation: "The set-theoretic versions (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ and (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ follow directly from the logical laws by treating 'x ∈ A' as a proposition. This correspondence (∧ ↔ ∩, ∨ ↔ ∪, ¬ ↔ complement) is one of the deepest structural parallels in mathematics."

- question: "Explain why ¬(p ∧ q) cannot equal ¬p ∧ ¬q, using specific truth values for p and q to show where the two expressions produce different results."
  type: short-answer
  answer: "Let p = T, q = F. Then ¬(p ∧ q) = ¬(T ∧ F) = ¬F = T, but ¬p ∧ ¬q = F ∧ T = F. The expressions disagree, so they are not equivalent."
  explanation: "When p is true and q is false, the conjunction p ∧ q is false, so its negation is true. But negating each component and conjoining gives F ∧ T = F. This single counterexample refutes the claimed equivalence. The correct form, ¬p ∨ ¬q = F ∨ T = T, matches the left side — confirming De Morgan's actual law."
```

## Explainer

From your study of logical equivalences, you know that two statements are equivalent when they have identical truth tables. De Morgan's Laws are perhaps the most useful equivalences in all of logic — they tell you exactly what happens when you push a negation sign inside a compound statement. The rule is: **negation flips AND to OR and OR to AND**. These two laws are simple to state but surprisingly powerful in practice.

The first law, ¬(p ∧ q) ≡ ¬p ∨ ¬q, says: "not (both p and q)" means "either not-p or not-q." Think of it concretely. Suppose a lock opens only when *both* a key and a code are correct. If the lock fails to open, then either the key was wrong *or* the code was wrong (or both). The failure of a conjunction is a disjunction of failures. The second law, ¬(p ∨ q) ≡ ¬p ∧ ¬q, says: "not (p or q)" means "not-p and not-q." If a door won't open when pushed *or* pulled, then it blocks both pushing *and* pulling. The negation of a disjunction is a conjunction of negations.

Both laws are easily verified with truth tables — a technique from your logical equivalences prerequisite. For any combination of truth values of p and q (TT, TF, FT, FF), the left and right sides of each law always match. But the laws are more useful as *algebraic tools* than as truth table exercises. When writing proofs, you often encounter complex negated statements and need to "expand" them into a usable form. De Morgan's Laws provide the algebra for doing so: ¬(A ∧ B ∧ C) = ¬A ∨ ¬B ∨ ¬C, and ¬(A ∨ B ∨ C) = ¬A ∧ ¬B ∧ ¬C by iterated application.

The laws extend naturally to sets: if A and B are subsets of a universal set U, then (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ and (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ. These are the set-theoretic De Morgan's Laws, and they follow directly from the logical versions by translating "x ∈ A" as a proposition. This connection between logical connectives and set operations (∧ ↔ ∩, ∨ ↔ ∪, ¬ ↔ complement) is one of the deepest unifying patterns in mathematics, and De Morgan's Laws sit at the center of it.
