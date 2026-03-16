---
id: formal-logic-propositions
title: Formal Logic and Propositional Calculus
domain: mathematics
course: discrete-math
prerequisites:
- id: conditional-and-biconditional
  type: hard
builds-toward:
- predicates-quantifiers-discrete
- mathematical-proof-strategies
tags:
- logic
- propositional
- truth-tables
stage: formal-systems
status: draft
---

# Formal Logic and Propositional Calculus

## Core Idea
Propositional logic formalizes reasoning with statements that are either true or false. Logical operators (AND, OR, NOT, conditional, biconditional) combine propositions into compound statements. Truth tables systematically determine the truth value of any logical expression.

## How It's Best Learned
Build truth tables for increasingly complex formulas. Identify logical equivalences and laws (De Morgan's, distributive, associative). Recognize common patterns like tautologies and contradictions.

## Common Misconceptions
The conditional 'if P then Q' is true when P is false (vacuous truth)—this confuses many. Biconditional requires both directions to be true, not just one.

## Explainer

You already know the conditional (if P then Q) and the biconditional (P if and only if Q) from your prerequisite work. Propositional logic now gives you the complete toolkit: a formal language where every statement has a definite truth value and every compound statement's truth value is fully determined by the truth values of its parts. A **proposition** is any declarative statement that is either true or false — "It is raining" qualifies; "Is it raining?" does not. Variables like P and Q stand in for propositions, and **logical connectives** combine them: negation (¬P, "not P"), conjunction (P ∧ Q, "P and Q"), disjunction (P ∨ Q, "P or Q"), the conditional (P → Q), and the biconditional (P ↔ Q).

A **truth table** is the mechanical tool for determining the truth value of any compound statement across all possible combinations of its variables. For n variables, the table has 2ⁿ rows. The connectives you need to memorize: ¬P flips truth value; P ∧ Q is true only when both are true; P ∨ Q is false only when both are false (inclusive or); P → Q is false only when P is true and Q is false. That last rule — the conditional is true whenever its hypothesis is false — is the famous **vacuous truth**. "If 2 + 2 = 5, then the moon is made of cheese" is a true statement in classical logic, because the hypothesis is false and the conditional makes no claim about what happens when its premise fails.

Two statements are **logically equivalent** when they have identical truth tables. The most important equivalences to know are **De Morgan's laws**: ¬(P ∧ Q) ≡ (¬P ∨ ¬Q) and ¬(P ∨ Q) ≡ (¬P ∧ ¬Q). These let you push negations inward. The contrapositive equivalence — P → Q ≡ ¬Q → ¬P — is equally important: proving the contrapositive is one of the standard proof strategies you will use immediately in the next course.

A **tautology** is a formula that is true in every row of its truth table: P ∨ ¬P is the simplest example. A **contradiction** is false in every row: P ∧ ¬P. Tautologies represent logical laws that hold regardless of the facts; contradictions represent impossible combinations. Recognizing whether an argument's conclusion follows necessarily from its premises — formal validity — is exactly the problem propositional logic was designed to solve, and truth tables give you a decision procedure: check whether every row where all premises are true also has the conclusion true.
