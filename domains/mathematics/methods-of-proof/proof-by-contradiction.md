---
id: proof-by-contradiction
title: Proof by Contradiction
domain: mathematics
course: methods-of-proof
prerequisites:
- id: negation-of-quantified-statements
  type: hard
- id: proof-structure-terminology
  type: hard
- id: proving-by-contradiction
  type: soft
builds-toward:
- proof-by-cases-exhaustion
tags:
- proof
- contradiction
- reductio-ad-absurdum
stage: formal-systems
status: validated
---
# Proof by Contradiction

## Core Idea
In a proof by contradiction, we assume the negation of our goal and derive a contradiction (a statement that is both true and false). Since the assumption leads to an absurdity, the original statement must be true. This technique works for any statement, not just conditionals, making it versatile for goals that resist direct proof.

## Questions

```yaml
- question: "You want to prove 'if A then B.' In setting up a proof by contradiction, what should you assume?"
  type: multiple-choice
  options:
    - "Assume ¬A (the hypothesis is false)"
    - "Assume ¬B (the conclusion is false)"
    - "Assume A ∧ ¬B (the hypothesis is true and the conclusion is false)"
    - "Assume ¬A ∧ ¬B (both hypothesis and conclusion are false)"
  answer: 2
  explanation: "To prove 'if A then B' by contradiction, you assume the negation of the entire conditional. The negation of 'if A then B' is 'A and not-B' — not simply ¬B. Assuming only ¬B is a common error that proves something weaker or creates a circular argument. The proof then derives a contradiction from A ∧ ¬B, establishing that this combination is impossible, and therefore 'if A then B' must hold."

- question: "In the classic proof that √2 is irrational, the contradiction reached is:"
  type: multiple-choice
  options:
    - "√2 turns out to equal a specific rational number, contradicting the assumption it was irrational"
    - "The denominator q turns out to equal zero, making the fraction undefined"
    - "Both p and q must be even, contradicting the assumption that p/q was in lowest terms"
    - "p² = 2q² has no integer solutions, directly contradicting the assumption"
  answer: 2
  explanation: "The proof assumes √2 = p/q in lowest terms (no common factors), then shows p must be even (so p = 2k), substitutes to get q² = 2k², which forces q to also be even. But if both p and q are even, they share the factor 2 — directly contradicting the assumption that p/q was already in lowest terms. This contradiction discharges the assumption, establishing that √2 cannot be rational."

- question: "In a proof by contradiction, the contradiction derived should take the explicit form of a statement P being asserted both true and false simultaneously (P ∧ ¬P)."
  type: true-false
  answer: false
  explanation: "The contradiction can be any statement already known to be false — not just an explicit P ∧ ¬P. It might be a violation of a previously proven theorem, a consequence like 0 = 1, or a derived result that contradicts a known fact (like 'both p and q are even' contradicting 'p/q is in lowest terms'). The only requirement is that the derived statement is demonstrably impossible, given what was already established before the proof began."

- question: "A proof by contradiction can establish that an object exists without constructing or exhibiting the object explicitly."
  type: true-false
  answer: true
  explanation: "This is what makes contradiction proofs non-constructive. The proof of √2's irrationality, for example, proves a negative — that no rational number equals √2 — without building anything. Existential claims can also be proven this way: assume the object does not exist, derive a contradiction, conclude it must exist. The proof demonstrates truth by eliminating the alternative, not by exhibiting a positive construction. This is what distinguishes contradiction proofs from direct proofs."

- question: "Why must you negate the *entire* goal when setting up a proof by contradiction, and what goes wrong if you only negate part of it?"
  type: short-answer
  answer: "You must negate the entire goal because the proof works by showing the negation leads to a contradiction — if you only negate part of the goal, you are assuming something different from 'the goal is false,' so any contradiction you derive doesn't establish the full original statement. For a conditional 'if A then B,' negating only B assumes 'not-B' without assuming A, which means contradictions you reach might depend on the absence of A rather than on A ∧ ¬B — proving a weaker or different result."
  explanation: "Logical hygiene here is essential. The proof's validity depends on the chain: (negation of goal) → contradiction → goal is true. If the negation is incomplete or incorrect, the chain breaks. Partial negations lead to proofs that feel valid but actually establish something other than the intended claim — a subtle error that can be difficult to spot after the fact."
```

## Explainer

Proof by contradiction is one of the most powerful proof strategies because it makes no assumption about what form the proof must take — only about what would follow if you were wrong. From your prerequisites on negation and proof structure, you know that every statement P has a negation ¬P, and that exactly one of them is true in classical logic. The contradiction strategy exploits this: assume ¬P is true, then derive a statement that is both provably true and provably false. Since a contradiction is impossible, the assumption ¬P must be what is wrong — so P must be true. This is **reductio ad absurdum**: reduction to absurdity.

The classic example is proving √2 is irrational. Assume the negation: √2 = p/q for integers p, q with no common factor (in lowest terms). Then p² = 2q², so p² is even, so p must be even (since odd² is always odd), so p = 2k for some integer k. Substituting: 4k² = 2q², so q² = 2k², so q is also even. But now both p and q are even — they share the factor 2 — contradicting the assumption that p/q is in lowest terms. The assumption led to a contradiction, so √2 cannot be rational. Notice that the proof constructs nothing; it works entirely by showing the alternative is impossible.

This non-constructive character is what distinguishes contradiction from direct proof. A **direct proof** builds the conclusion from the hypotheses step by step, producing a positive construction. A proof by contradiction establishes that the opposite is incompatible with what is already known. The technique is especially effective when the conclusion is a negation ("there is no largest prime"), when negating the conclusion gives you powerful structural information to work with (as "√2 is rational" gives you a fraction to manipulate), or when no direct route to the conclusion is visible.

Precise **logical hygiene** is essential. You must negate the entire goal, not a convenient subset of it. If the goal is "if A then B," the negation is "A and not-B" — not simply "not-B." After assuming the negation, you pursue any contradiction, anywhere it leads. The contradiction does not have to be an explicit P ∧ ¬P; it can be any statement already known to be false (like 0 = 1, or a previously proven theorem being violated). Once the contradiction is derived, the assumed negation is discharged and the original statement is established. The proof is complete.
