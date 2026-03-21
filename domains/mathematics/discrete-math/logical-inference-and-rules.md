---
id: logical-inference-and-rules
title: Logical Inference and Proof Rules
domain: mathematics
course: discrete-math
prerequisites:
- id: propositional-logic-basics
  type: hard
builds-toward:
- direct-proof-methods
- proof-by-contrapositive
tags:
- logic
- inference
- proofs
stage: formal-systems
status: draft
---

# Logical Inference and Proof Rules

## Core Idea
Inference rules allow us to deduce new true statements from known ones. Modus ponens, modus tollens, disjunctive syllogism, and hypothetical syllogism are fundamental rules that preserve truth. Understanding these rules enables rigorous logical reasoning in mathematics.

## How It's Best Learned
Practice applying inference rules to simple arguments first. Write out formal proofs using one inference rule per line, identifying the rule used and the statements involved.

## Common Misconceptions
- Confusing affirming the consequent with modus ponens. - Believing that a logical rule is valid just because it looks similar to a valid rule.

## Questions

```yaml
- question: "A scientist reasons: 'If this compound is toxic, lab animals will show symptoms. The animals showed symptoms. Therefore, the compound is toxic.' Which inference pattern is being applied?"
  type: multiple-choice
  options:
    - "Modus ponens — the scientist has P and P→Q, so concludes Q"
    - "Modus tollens — the scientist has ¬Q and P→Q, so concludes ¬P"
    - "Affirming the consequent — the scientist has P→Q and Q, so concludes P (invalid)"
    - "Disjunctive syllogism — the scientist is eliminating one disjunct"
  answer: 2
  explanation: "This is the classic invalid inference pattern: affirming the consequent. The form is P→Q, Q ∴ P. Even if the conditional is true ('toxicity causes symptoms'), the converse is not guaranteed — the animals might show symptoms for many reasons other than this compound. This looks superficially like modus ponens but runs in the wrong direction: modus ponens goes from antecedent to consequent (P, P→Q ∴ Q), while this goes from consequent back to antecedent, which is not truth-preserving."

- question: "You know 'If Alice is present, the meeting goes forward (A→M)' and 'If the meeting goes forward, the report is finalized (M→R).' Which rule lets you directly conclude 'If Alice is present, the report is finalized (A→R)'?"
  type: multiple-choice
  options:
    - "Modus ponens — applying the first conditional to a given premise"
    - "Modus tollens — taking the contrapositive of the chain"
    - "Hypothetical syllogism — chaining two conditionals P→Q and Q→R into P→R"
    - "Disjunctive syllogism — eliminating one option from a disjunction"
  answer: 2
  explanation: "Hypothetical syllogism is the transitivity rule for conditionals: from P→Q and Q→R, conclude P→R. It underlies multi-step proofs where you build a path from hypothesis to conclusion through intermediate steps — exactly what this scenario does with A→M and M→R to conclude A→R."

- question: "Modus tollens is essentially the contrapositive of modus ponens applied as an inference rule."
  type: true-false
  answer: true
  explanation: "Exactly right. Modus ponens says: P→Q, P ∴ Q. The contrapositive of P→Q is ¬Q→¬P, which is logically equivalent. Modus tollens applies that contrapositive: P→Q, ¬Q ∴ ¬P. If you know the conditional and you know the consequent is false, you can infer the antecedent is also false. The two rules are mirror images — both valid because contraposition preserves truth."

- question: "From 'If it rains, the game is cancelled (R→C)' and 'The game was cancelled (C)', you can validly conclude 'It rained (R)'."
  type: true-false
  answer: false
  explanation: "This is affirming the consequent, an invalid inference form. The game could have been cancelled for many reasons other than rain. P→Q being true does not make Q→P true. The valid inference from R→C and ¬C would be ¬R (modus tollens). But from R→C and C, no conclusion about R follows. The pattern looks persuasive because in everyday speech we often treat conditionals as biconditionals — but in logic, they are not."

- question: "Why is 'affirming the consequent' an invalid inference rule, even though it superficially resembles modus ponens?"
  type: short-answer
  answer: "Affirming the consequent has the form P→Q, Q ∴ P, which runs from consequent back to antecedent. This is invalid because P→Q allows Q to be true for reasons other than P — multiple different antecedents can produce the same consequent. Modus ponens (P→Q, P ∴ Q) is valid because starting from the sufficient condition and moving to its consequence preserves truth. Affirming the consequent reverses this direction through a one-way gate."
  explanation: "A conditional P→Q says P is sufficient for Q, not that P is the only way to get Q. Knowing Q is true doesn't tell you whether P caused it or something else did. Modus ponens works because it starts from the antecedent — the sufficient condition. Affirming the consequent tries to run the inference backwards, losing truth preservation in the process."
```

## Explainer

From your study of propositional logic, you know that compound statements are built from simpler ones using connectives like ∧, ∨, ¬, and →. Truth tables let you evaluate any statement given the truth values of its components. But proofs don't work by evaluating truth tables — they work by chaining together inference steps, each one guaranteed to preserve truth. **Inference rules** are the licensed moves of that game.

The most fundamental rule is **modus ponens**: if you know P → Q is true, and you know P is true, you can conclude Q is true. This matches ordinary reasoning — "If it rains, the ground gets wet; it is raining; therefore the ground is wet." Its partner is **modus tollens**: if P → Q and ¬Q, then ¬Q forces ¬P (the contrapositive). The key mistake to avoid is **affirming the consequent**: from P → Q and Q, you cannot conclude P. The ground might be wet because a pipe burst, not because it rained. That inference pattern is invalid — it does not preserve truth.

Two more rules complete the basic toolkit. **Disjunctive syllogism**: from P ∨ Q and ¬P, you may conclude Q. If you know one of two things is true and you rule out the first, the second must hold. **Hypothetical syllogism**: from P → Q and Q → R, you may chain them into P → R. This is the logical version of transitivity, and it underlies multi-step proofs where you build a path from hypothesis to conclusion through intermediate steps.

In practice, a formal proof is a numbered sequence of statements, where each statement is either a given premise or follows from earlier statements by a named inference rule. This discipline forces you to be explicit about *why* each step is valid, not just *that* it seems right. The payoff comes in the next topics — direct proof and proof by contrapositive — which are precisely modus ponens and modus tollens applied at the level of mathematical theorems. Every proof technique in mathematics is, at its core, a disciplined application of these inference rules.
