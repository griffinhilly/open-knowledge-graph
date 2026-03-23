---
id: logical-equivalence-intro
title: Logical Equivalence
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: truth-tables-introduction
    type: hard
  - id: converse-inverse-contrapositive-intro
    type: hard
  - id: biconditional-statements-intro
    type: soft
builds-toward:
  - logical-equivalence
  - logical-equivalence-propositional
  - logical-equivalences-intro
  - propositional-logic-introduction
tags: [equivalence, logic, truth-tables, tautology]
stage: abstract-reasoning
status: draft
---

# Logical Equivalence

## Core Idea
Two logical statements are logically equivalent if they have the same truth value in every possible situation — their truth tables produce identical output columns. The notation is P ≡ Q or P ⇔ Q. Key equivalences include: a conditional and its contrapositive (P → Q ≡ ¬Q → ¬P), double negation (¬¬P ≡ P), and De Morgan's Laws (¬(P ∧ Q) ≡ ¬P ∨ ¬Q). Logical equivalence lets you replace one statement with another in proofs and arguments, confident that the substitution preserves truth.

## How It's Best Learned
Have students build truth tables for pairs of statements and compare the output columns. If every row matches, the statements are equivalent. Start with obvious cases (¬¬P and P), then move to the conditional/contrapositive equivalence, then introduce De Morgan's Laws as a discovery exercise. Contrast with non-equivalences: P → Q and Q → P have different truth tables, proving they are not equivalent.

## Common Misconceptions
- Confusing logical equivalence with equality. Two equivalent statements are not the same statement — they are different expressions that happen to always agree in truth value.
- Thinking equivalence means the statements "look similar." P → Q and ¬P ∨ Q look completely different but are logically equivalent.
- Assuming equivalence can be checked with a few examples. You must verify all rows of the truth table, or use a known logical law, to establish equivalence.

## Questions

```yaml
- question: "Which of the following is logically equivalent to P → Q?"
  type: multiple-choice
  options:
    - "Q → P"
    - "¬P → ¬Q"
    - "¬P ∨ Q"
    - "P ∧ Q"
  answer: 2
  explanation: "The truth table for ¬P ∨ Q matches the truth table for P → Q in every row. When P is true, ¬P is false, so ¬P ∨ Q depends entirely on Q — matching P → Q. When P is false, ¬P is true, so ¬P ∨ Q is true — matching the vacuous truth of P → Q. Option A is the converse (not equivalent). Option B is the inverse (not equivalent). Option D is conjunction, which is false whenever either is false."

- question: "If two statements have the same truth value for three out of four rows in their truth tables but differ in one row, they are logically equivalent."
  type: true-false
  answer: false
  explanation: "Logical equivalence requires identical truth values in EVERY row. Even one row of disagreement means the statements are not equivalent. There exists a scenario — the one corresponding to the differing row — where one statement is true and the other is false. Equivalence is an all-or-nothing property."

- question: "Use De Morgan's Law to write an expression equivalent to ¬(P ∨ Q), and verify with a truth table."
  type: short-answer
  answer: "By De Morgan's Law, ¬(P ∨ Q) ≡ ¬P ∧ ¬Q. Verification: P=T,Q=T: ¬(T∨T)=¬T=F; ¬T∧¬T=F∧F=F. P=T,Q=F: ¬(T∨F)=¬T=F; ¬T∧¬F=F∧T=F. P=F,Q=T: ¬(F∨T)=¬T=F; ¬F∧¬T=T∧F=F. P=F,Q=F: ¬(F∨F)=¬F=T; ¬F∧¬F=T∧T=T. All rows match."
  explanation: "De Morgan's Laws are among the most useful equivalences in logic. ¬(P ∨ Q) ≡ ¬P ∧ ¬Q says 'not (P or Q)' is the same as 'not P and not Q.' The companion law is ¬(P ∧ Q) ≡ ¬P ∨ ¬Q. Negation distributes over connectives by swapping AND with OR."
```

## Explainer

You already know that a conditional and its contrapositive always have the same truth value. Logical equivalence is the general name for this relationship: two statements are logically equivalent when they agree in every possible scenario. No matter what truth values you assign to the variables, both statements come out the same — both true, or both false.

The simplest way to verify equivalence is to build truth tables for both statements and compare the final columns. If every row matches, the statements are equivalent. If even one row differs, they are not. This is a mechanical procedure — no cleverness required, just careful bookkeeping. For two variables, you check four rows. For three, eight rows. It scales, though it gets tedious for many variables.

Some equivalences are so fundamental that they have names and are used as building blocks. Double negation: ¬¬P ≡ P (negating a negation gives the original). Contrapositive: P → Q ≡ ¬Q → ¬P. Conditional as disjunction: P → Q ≡ ¬P ∨ Q (this one is surprising — "if P then Q" is equivalent to "not P or Q," which means a conditional is really a disguised OR statement). And De Morgan's Laws: ¬(P ∧ Q) ≡ ¬P ∨ ¬Q and ¬(P ∨ Q) ≡ ¬P ∧ ¬Q, which tell you how negation interacts with AND and OR.

The practical value of equivalences is substitution. In a proof or argument, you can replace any statement with a logically equivalent one without changing the truth of the overall argument. If you need to prove P → Q and find it difficult, you can instead prove ¬Q → ¬P (the contrapositive) or ¬P ∨ Q, whichever is easier. The equivalence guarantees that proving any one of them proves all of them.

Logical equivalence is closely related to the biconditional. In fact, P ≡ Q if and only if P ↔ Q is a tautology (true in every row). The biconditional asks "do P and Q have the same truth value in this particular case?" and logical equivalence asks "do they have the same truth value in every case?" Equivalence is the stronger claim — it is a biconditional that holds universally, not just in one scenario. This distinction will become important as you move into formal proof and the deeper study of propositional logic.
