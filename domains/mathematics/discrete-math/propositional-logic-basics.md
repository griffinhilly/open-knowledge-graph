---
id: propositional-logic-basics
title: Propositional Logic Foundations
domain: mathematics
course: discrete-math
prerequisites:
- id: graph-theory-intro
  type: soft
builds-toward:
- logical-inference-and-rules
- logical-equivalences
tags:
- logic
- foundations
- discrete-math
stage: formal-systems
status: draft
---
# Propositional Logic Foundations

## Core Idea
Propositional logic uses simple statements (propositions) that are either true or false, combined with logical operators (AND, OR, NOT, IF-THEN). These form the foundation for mathematical reasoning and are used to analyze arguments, determine truth values, and construct formal proofs.

## Explainer

A **proposition** is a declarative statement that is unambiguously either true or false — "The sky is blue," "7 is odd," "2 + 2 = 5." Questions, commands, and paradoxes such as "This sentence is false" are not propositions. The power of propositional logic is that once you assign truth values to atomic propositions, you can compute the truth value of any compound statement built from them using **logical connectives**: AND (∧), OR (∨), NOT (¬), IF-THEN (→), and IF-AND-ONLY-IF (↔). Each connective has a precise, non-negotiable meaning captured in a **truth table**.

AND (p ∧ q) is true only when both p and q are true. OR (p ∨ q) is true when at least one is true — this is *inclusive* or, not exclusive. NOT (¬p) flips the truth value. The most subtle connective is **implication** (p → q): it is false only when p is true and q is false. "If it rains, I bring an umbrella" is not falsified by sunny weather — on a dry day, the statement makes no claim at all. This *vacuous truth* surprises beginners, but follows from the definition: p → q is logically equivalent to (¬p ∨ q), which is clearly true whenever p is false.

Truth tables let you evaluate any compound statement systematically. With n propositional variables, there are 2ⁿ rows — one for every combination of truth values. A statement true in every row is a **tautology** (e.g., p ∨ ¬p — "either it's raining or it isn't"). A statement false in every row is a **contradiction** (e.g., p ∧ ¬p). Tautologies are especially important: they are logical guarantees, true regardless of what the variables represent.

Two statements are **logically equivalent** when they have identical truth tables — written p ≡ q. The most useful equivalences are De Morgan's Laws: ¬(p ∧ q) ≡ (¬p ∨ ¬q), and ¬(p ∨ q) ≡ (¬p ∧ ¬q). These let you push negations inward, transforming complex negations into workable form. Equally important is the **contrapositive**: (p → q) ≡ (¬q → ¬p). Since these are logically identical, you can always prove the contrapositive instead of the original implication — whichever is easier. Propositional logic is the bedrock of all formal mathematical reasoning: every proof, every theorem, every valid argument is ultimately grounded in these simple rules about truth values and connectives.
