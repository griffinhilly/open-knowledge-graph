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

## Explainer

From your study of propositional logic, you know that compound statements are built from simpler ones using connectives like ∧, ∨, ¬, and →. Truth tables let you evaluate any statement given the truth values of its components. But proofs don't work by evaluating truth tables — they work by chaining together inference steps, each one guaranteed to preserve truth. **Inference rules** are the licensed moves of that game.

The most fundamental rule is **modus ponens**: if you know P → Q is true, and you know P is true, you can conclude Q is true. This matches ordinary reasoning — "If it rains, the ground gets wet; it is raining; therefore the ground is wet." Its partner is **modus tollens**: if P → Q and ¬Q, then ¬Q forces ¬P (the contrapositive). The key mistake to avoid is **affirming the consequent**: from P → Q and Q, you cannot conclude P. The ground might be wet because a pipe burst, not because it rained. That inference pattern is invalid — it does not preserve truth.

Two more rules complete the basic toolkit. **Disjunctive syllogism**: from P ∨ Q and ¬P, you may conclude Q. If you know one of two things is true and you rule out the first, the second must hold. **Hypothetical syllogism**: from P → Q and Q → R, you may chain them into P → R. This is the logical version of transitivity, and it underlies multi-step proofs where you build a path from hypothesis to conclusion through intermediate steps.

In practice, a formal proof is a numbered sequence of statements, where each statement is either a given premise or follows from earlier statements by a named inference rule. This discipline forces you to be explicit about *why* each step is valid, not just *that* it seems right. The payoff comes in the next topics — direct proof and proof by contrapositive — which are precisely modus ponens and modus tollens applied at the level of mathematical theorems. Every proof technique in mathematics is, at its core, a disciplined application of these inference rules.
