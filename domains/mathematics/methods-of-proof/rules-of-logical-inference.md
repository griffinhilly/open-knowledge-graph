---
id: rules-of-logical-inference
title: Rules of Logical Inference
domain: mathematics
course: methods-of-proof
prerequisites:
- id: conditional-implication-statements
  type: hard
- id: tautologies-and-contradictions-classification
  type: soft
builds-toward:
- modus-ponens-and-modus-tollens
- proving-by-direct-method
tags:
- logic
- inference
- deduction
- validity
stage: formal-systems
status: draft
---

# Rules of Logical Inference

## Core Idea
Rules of inference are patterns of reasoning that guarantee a true conclusion when applied to true premises. They preserve truth: if the premises are true, the conclusion must be true. These rules form the foundation of valid deductive proof.

## How It's Best Learned
Learn a few key rules deeply (modus ponens, modus tollens, hypothetical syllogism) rather than trying to memorize many. Understand why each rule works using truth tables or logical intuition.

## Common Misconceptions
- Confusing valid reasoning with true conclusions (validity requires true premises).
- Applying rules backwards (e.g., affirming the consequent).
- Assuming common-sense reasoning is logically valid.

## Explainer

A **rule of inference** is a template for constructing valid arguments. You know from your study of conditional statements that "P → Q" means "if P then Q," and you know what it means for a statement to be a tautology — true under every truth assignment. Rules of inference are exactly those argument forms whose logical structure guarantees truth-preservation: whenever the premises are true, the conclusion must be true. That guarantee is what makes a proof valid, as opposed to merely persuasive.

The most important rule is **modus ponens**: from P and P → Q, conclude Q. In natural language: "It is raining" and "If it rains, the ground gets wet" together imply "The ground gets wet." Verify this with a truth table — the only row where both premises are true forces Q to be true. **Modus tollens** runs the same conditional in reverse: from ¬Q and P → Q, conclude ¬P. If the ground is dry, and rain would wet it, then it hasn't rained. Notice what is not valid: from Q and P → Q, you cannot conclude P. That error is called **affirming the consequent** — it is the classic confusion between "if P then Q" and "if Q then P."

**Hypothetical syllogism** chains conditionals: from P → Q and Q → R, conclude P → R. This is transitivity of implication, and it is what allows multi-step proofs — each step passes the truth forward until you reach the desired conclusion. **Disjunctive syllogism** handles or-statements: from P ∨ Q and ¬P, conclude Q. If at least one of P, Q is true and P is false, Q must be true. This is the logical engine behind proof by cases and proof by elimination.

The overarching principle is **validity vs. truth**. An argument is valid if the conclusion follows necessarily from the premises — regardless of whether the premises are actually true. "All fish can fly; salmon are fish; therefore salmon can fly" is valid (the structure is correct) but unsound (a premise is false). In mathematics, where the axioms are stipulated to be true, validity and soundness coincide — but the distinction reminds you to check both the logical structure of your proof and the truth of your starting assumptions. Rules of inference give you the structural half; your domain knowledge gives you the truth half.
