---
id: truth-tables-intro
title: Truth Tables and Truth Conditions
domain: mathematics
course: methods-of-proof
prerequisites:
- id: statements-and-logical-connectives
  type: hard
builds-toward:
- logical-equivalences-intro
- conditional-and-biconditional-statements
tags:
- logic
- truth-values
- systematic-reasoning
stage: formal-systems
status: draft
---

# Truth Tables and Truth Conditions

## Core Idea
A truth table systematically lists all possible truth value assignments for a statement's components and shows the resulting truth value. Truth tables provide a mechanical, exhaustive method for determining when compound statements are true or false under all possible conditions, eliminating ambiguity from logical reasoning.

## Questions

```yaml
- question: "The statement 'If it is raining, then the ground is wet' (P → Q) — in which scenario is this conditional FALSE?"
  type: multiple-choice
  options:
    - "It is raining and the ground is wet"
    - "It is not raining and the ground is not wet"
    - "It is raining and the ground is not wet"
    - "It is not raining and the ground is wet"
  answer: 2
  explanation: "A conditional P → Q is false in exactly one case: when P is true and Q is false — the conditional 'breaks its promise.' If it is raining (P is true) but the ground is not wet (Q is false), the statement is falsified. All other combinations make the conditional true: when P is false, the conditional cannot be falsified regardless of Q, because no promise was made. Rows B and D have a false antecedent, making the conditional vacuously true."

- question: "A truth table analysis of an argument shows that in one row where all premises are true, the conclusion is false. What does this tell you about the argument?"
  type: multiple-choice
  options:
    - "The argument is valid — one counterexample row is not enough to defeat it"
    - "The argument is invalid — there exists a possible scenario where the premises hold but the conclusion fails"
    - "The argument is unsound, but soundness is different from validity"
    - "The truth table must contain an error, because valid arguments cannot have such rows"
  answer: 1
  explanation: "Validity requires that every row making all premises true also makes the conclusion true. A single row where the premises are all true and the conclusion is false is a logical counterexample — proof that the argument is invalid. Validity is all-or-nothing: if even one such row exists, the argument fails. This mechanical test is the power of truth tables — they make validity checking exhaustive and error-free."

- question: "If the antecedent P in a conditional P → Q is false, then the conditional is true regardless of Q's truth value."
  type: true-false
  answer: true
  explanation: "This is the 'vacuous truth' principle. A conditional makes a promise: 'if P, then Q.' If P never happens (P is false), the promise is never tested and cannot be broken. Logically, a false premise makes the conditional true under both Q = true and Q = false. This seems counterintuitive but is the only consistent rule — if false antecedents made conditionals false, then 'if 2 + 2 = 5, then pigs can fly' would be false, which would undermine mathematical theorems stated in conditional form."

- question: "A tautology is a statement that is true whenever all of its component propositions are true."
  type: true-false
  answer: false
  explanation: "A tautology is a statement that is true under ALL possible truth value assignments — including rows where some components are false. For example, P ∨ ¬P is a tautology: it is true whether P is true or false. The statement in this question describes only partial coverage. Many statements are true when all components are true but false in other rows — those are not tautologies. A tautology must be true in every single row of its truth table."

- question: "Why is a conditional P → Q defined as true when P is false? Explain the 'broken promise' reasoning and why this seemingly strange rule is logically essential."
  type: short-answer
  answer: "The conditional P → Q is a promise: 'if P occurs, then Q will follow.' The only way to break this promise is for P to be true (the triggering condition occurred) and Q to be false (the promised outcome didn't happen). When P is false, the triggering condition never occurred, so the promise was never tested and cannot be broken — making the conditional vacuously true. This rule is logically essential because mathematical theorems often take the form 'if X, then Y' where the hypothesis X may be false for many objects. If false hypotheses made conditionals false, entire bodies of mathematical results would collapse."
  explanation: "Students often think 'false implies anything' is arbitrary. But it follows from defining falsity as 'breaking the promise.' A conditional that is never tested cannot be said to have been broken. This is also why P → Q is logically equivalent to ¬P ∨ Q — either the antecedent fails (promise never triggered) or the consequent holds (promise kept)."
```

## Explainer

You know that logical connectives like AND (∧), OR (∨), NOT (¬), and the conditional (→) have meanings in ordinary language. But ordinary language is imprecise: "or" can mean "one or the other but not both" or "at least one of them," and "if…then" carries causal implications that formal logic strips away. A **truth table** makes these meanings completely precise by exhaustively listing every possible combination of truth values and specifying the output for each combination according to a fixed rule.

The construction is mechanical. A compound statement with n atomic components has 2ⁿ possible truth value assignments — two choices (true or false) per component. You write one row per assignment, then evaluate the compound statement in each row using the definitions of the connectives. For ¬P: flip the truth value. For P ∧ Q: true only when both are true. For P ∨ Q: true when at least one is true. For P → Q: false only when P is true and Q is false — the conditional "breaks its promise" only in that case. For P ↔ Q: true when both have the same truth value. Each connective has a fixed, completely mechanical rule with no room for interpretation.

The power of truth tables goes beyond evaluating a single statement. A **tautology** is a statement that is true in every row — it is logically necessary regardless of the truth values of its components. De Morgan's laws (¬(P ∧ Q) ≡ ¬P ∨ ¬Q) and the equivalence between P → Q and ¬P ∨ Q are tautologies you can verify by checking that no row makes them false. A **contradiction** is false in every row. Two statements are **logically equivalent** when their truth tables match column-for-column under identical inputs — this is a mechanical test for equivalence that requires no insight or intuition.

Truth tables also provide a formal criterion for **validity** of an argument. An argument is valid when every row that makes all the premises true also makes the conclusion true — there is no possible assignment of truth values that satisfies the premises but falsifies the conclusion. This is how you verify that modus ponens is valid and how you expose that affirming the consequent is invalid: there exist rows where P → Q and Q are both true but P is false, showing the argument can fail. Validity is a purely structural guarantee about the relationship between premises and conclusion, independent of whether the premises are actually true.
