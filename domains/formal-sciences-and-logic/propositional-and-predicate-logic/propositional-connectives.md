---
id: propositional-connectives
title: Propositional Connectives
domain: formal-sciences-and-logic
course: propositional-and-predicate-logic
prerequisites:
- id: propositional-syntax
  type: hard
builds-toward:
- propositional-semantics
- tautologies-and-contradictions
tags:
- connectives
- negation
- conjunction
- disjunction
- implication
- biconditional
- truth-functional
stage: formal-systems
status: draft
---

# Propositional Connectives

## Core Idea
The five standard propositional connectives — NOT (¬), AND (∧), OR (∨), IMPLIES (→), and IFF (↔) — are defined purely by their truth-functional behavior: the truth value of any compound formula is entirely determined by the truth values of its components. Each connective has a fixed truth table that serves as its semantic definition. Precedence conventions (¬ binds tightest, then ∧, then ∨, then →, then ↔) reduce the need for parentheses, but understanding this hierarchy is essential for correct parsing.

## How It's Best Learned
Build the truth table for each connective from scratch, then combine them to evaluate compound formulas step by step. Pay special attention to material implication (→), whose truth table surprises most beginners: a false antecedent makes the conditional true regardless of the consequent.

## Common Misconceptions
- Material implication (→) does not capture causation or temporal sequence — "if P then Q" is true whenever P is false, which feels counterintuitive but is logically consistent.
- Inclusive OR (∨) is true when both disjuncts are true, unlike the everyday "or" which often implies exclusivity.
- Precedence is a notational convention, not a logical fact — when in doubt, use parentheses.

## Explainer

From studying **propositional syntax** you know that formulas are built from atomic variables and connectives. Now we give those connectives their meanings — and the key idea is that meaning is **purely truth-functional**: the truth value of any compound formula is entirely determined by the truth values of its component formulas. There is no meaning "behind" the symbols, no causation, no time, no reference to content. Each connective is fully specified by a truth table.

**Negation** (¬P) flips truth to false and false to true — the simplest connective. **Conjunction** (P ∧ Q) is true only when both P and Q are true; it corresponds to "both." **Disjunction** (P ∨ Q) is true when at least one of P or Q is true — the inclusive "or." The logical OR differs from everyday English "or," which often carries an exclusive sense ("soup or salad" typically means one or the other, not both). The logical ∨ is satisfied by both P and Q being simultaneously true; keep this in mind when translating natural-language claims.

**Material implication** (P → Q) is the most counterintuitive connective. It is false only when P is true and Q is false — the one combination where a true premise yields a false conclusion. In all other cases, P → Q is true: when P is false (regardless of Q) and when Q is true (regardless of P). This feels wrong because natural language "if…then…" carries causal or temporal connotations. But material implication strips all of that away and says only: "it is not the case that P is true while Q is false." The statement "if the moon is made of cheese, then 2+2=5" is materially true, because the antecedent is false. This is the price of being purely truth-functional: the connective cannot track causation, only truth-value combinations. Learning to use P → Q correctly is the essential skill of this topic.

**Biconditional** (P ↔ Q) is true exactly when P and Q have the same truth value — both true or both false. It means "P if and only if Q." When writing logical equivalences, ↔ is the formal expression of "these formulas always agree." The **precedence hierarchy** — ¬ binds tightest, then ∧, then ∨, then →, then ↔ — is a notational convention that reduces parentheses. So P ∨ Q ∧ R is parsed as P ∨ (Q ∧ R) because ∧ binds before ∨. When in doubt, add parentheses; the grammar is more important than avoiding them.
