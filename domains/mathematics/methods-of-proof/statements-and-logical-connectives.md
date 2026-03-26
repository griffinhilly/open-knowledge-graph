---
id: statements-and-logical-connectives
title: Statements and Logical Connectives
domain: mathematics
course: methods-of-proof
prerequisites: []
builds-toward:
- truth-tables
- logical-equivalences
tags:
- logic
- foundations
- statements
stage: formal-systems
status: validated
---

# Statements and Logical Connectives

## Core Idea
A logical statement is a declarative sentence that is either true or false, never both. Logical connectives—AND, OR, NOT, IF-THEN—combine simple statements into compound statements, allowing us to express complex logical relationships precisely. Mastering these connectives is the foundation for all formal reasoning.

## Questions

```yaml
- question: "What is the truth value of the statement: 'If the moon is made of cheese, then 2 + 2 = 5'?"
  type: multiple-choice
  options:
    - "True, because both parts are false and they cancel out"
    - "False, because the conclusion is false"
    - "True, because the hypothesis is false, making the implication vacuously true"
    - "Undefined, because neither part is a meaningful mathematical claim"
  answer: 2
  explanation: "A conditional P → Q is false ONLY when P is true and Q is false. Here P ('the moon is made of cheese') is false, so the implication is vacuously true — it made a promise only about what happens when P holds, and P never holds. The truth of Q is irrelevant."

- question: "Two students debate the meaning of 'P OR Q' in mathematics. Student A says it means exactly one of P or Q is true (but not both). Student B says it means at least one of P or Q is true (including the case where both are true). Which student is correct?"
  type: multiple-choice
  options:
    - "Student A — mathematical OR is exclusive, like everyday 'either/or'"
    - "Student B — mathematical OR is inclusive, true whenever at least one component is true"
    - "Both are correct — context determines which interpretation applies"
    - "Neither — OR is only defined when P and Q have opposite truth values"
  answer: 1
  explanation: "Mathematical disjunction (∨) is inclusive OR: P ∨ Q is true whenever at least one of P, Q is true, including the case where both are true. This differs from everyday English 'either/or,' which often implies exclusivity. Student A's version is called XOR (exclusive or) and is a different connective."

- question: "The sentence 'What is the square root of 9?' is a false statement because the answer is 3, not implied."
  type: true-false
  answer: false
  explanation: "This sentence is not a statement at all — it is a question. Statements are declarative sentences that have a definite truth value (true or false). Questions, commands, and exclamations are not statements and cannot be called true or false. Logic only operates on statements."

- question: "The conditional statement P → Q is logically equivalent to ¬P ∨ Q."
  type: true-false
  answer: true
  explanation: "This equivalence is fundamental: 'If P then Q' is false only when P is true and Q is false — the same conditions under which ¬P ∨ Q is false (¬P is false and Q is false). Checking all four truth-value combinations confirms they always agree. This equivalence is used to transform implications into disjunctions, which is often easier to reason about."

- question: "Explain why the statement 'If it is raining, then the ground is wet' can be TRUE on a sunny day when it is not raining and the ground is also dry."
  type: short-answer
  answer: "A conditional P → Q is vacuously true whenever P is false, regardless of Q's truth value. The statement makes a promise only about what happens when P (it is raining) holds — if it never rains, the promise is never violated."
  explanation: "Vacuous truth is one of the most counterintuitive features of material implication. The conditional is a guarantee: whenever rain occurs, wetness follows. On a dry, sunny day, the rain condition never activates, so there is no opportunity to violate the guarantee. This is not a trick — it reflects the logical structure of 'if-then' claims, which assert nothing about what happens when the hypothesis is false."
```

## Explainer

Mathematics is built on precise claims, and the first tool of precision is identifying what can be true or false. A **statement** (also called a **proposition**) is a declarative sentence with a definite truth value: "17 is prime" is true; "the square root of 4 is 3" is false. By contrast, "is 17 prime?" (a question) and "let x be a number" (a command) are not statements — they have no truth value. The discipline of logic begins by demanding that every sentence we reason about be a statement in this strict sense.

**Logical connectives** combine simple statements into compound ones. The **conjunction** "P AND Q" (written P ∧ Q) is true only when both P and Q are true simultaneously. The **disjunction** "P OR Q" (written P ∨ Q) is true when at least one is true — mathematical "or" is inclusive, unlike the everyday "either/or" which excludes the both-true case. The **negation** "NOT P" (written ¬P) flips the truth value: if P is "x > 5," then ¬P is "x ≤ 5." Each connective has a precise definition that a truth table captures exhaustively — listing every combination of truth values for the component statements and the resulting truth value of the compound.

The most important connective for mathematical reasoning is **implication**: "IF P THEN Q" (written P → Q). It asserts that whenever P is true, Q must also be true. Crucially, P → Q is false only when P is true but Q is false — a true hypothesis leading to a false conclusion is the only way to violate a conditional claim. When P is false, P → Q is **vacuously true** regardless of Q. This surprises newcomers: "If the moon is made of cheese, then 2 + 2 = 5" is logically true, because the hypothesis is false. The implication made a promise only about what happens when P holds — and P never holds.

These four connectives (AND, OR, NOT, IF-THEN) are enough to express any logical relationship precisely. Every mathematical theorem is ultimately a statement — often an implication — built from simpler components. The rules for manipulating these connectives (like the equivalence P → Q ≡ ¬P ∨ Q, or De Morgan's laws) let you transform statements while preserving truth, which is exactly what a mathematical proof does. Mastering the meaning of each connective, especially the surprising cases of vacuous truth and inclusive or, prevents the logical errors that invalidate proofs before they even begin.
