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
status: validated
---
# Propositional Logic Foundations

## Core Idea
Propositional logic uses simple statements (propositions) that are either true or false, combined with logical operators (AND, OR, NOT, IF-THEN). These form the foundation for mathematical reasoning and are used to analyze arguments, determine truth values, and construct formal proofs.

## Questions

```yaml
- question: "Under the rule 'If a student passes the exam (P), then they receive credit (C),' a student fails the exam. What can we conclude about whether they receive credit?"
  type: multiple-choice
  options:
    - "Nothing — the implication P → C makes no claim when P is false"
    - "The student definitely does not receive credit, since they failed"
    - "The implication has been violated, since the outcome is uncertain"
    - "The student must receive credit, since the rule still applies"
  answer: 0
  explanation: "P → C is false only when P is true and C is false. When P is false (the student fails), the implication is vacuously true regardless of C — the conditional promise is simply never triggered. The student failing says nothing about whether they receive credit; perhaps they receive it on other grounds. This vacuous truth surprises beginners but follows directly from the truth table: a conditional that is never triggered cannot be violated."

- question: "Which of the following is logically equivalent to p → q?"
  type: multiple-choice
  options:
    - "¬p ∨ q"
    - "p ∧ ¬q"
    - "¬p → ¬q"
    - "q → p"
  answer: 0
  explanation: "p → q is false only when p is true and q is false. ¬p ∨ q is false only when ¬p is false (p is true) and q is false — exactly the same condition. They have identical truth tables and are therefore logically equivalent. Option C (¬p → ¬q) is the inverse of p → q — not equivalent. Option D (q → p) is the converse — not equivalent. Option B (p ∧ ¬q) is actually the negation of p → q, not the equivalence."

- question: "The statement 'If 2 + 2 = 5, then the moon is made of cheese' is a true proposition according to propositional logic."
  type: true-false
  answer: true
  explanation: "This is true — and deliberately counterintuitive. An implication p → q is false only when p is true and q is false. Here, p ('2 + 2 = 5') is false, so the entire implication is vacuously true regardless of q. The logical meaning of implication does not match the everyday meaning of 'if…then.' In formal logic, a false antecedent renders the conditional automatically true because no promise has been broken."

- question: "The contrapositive of p → q is ¬p → ¬q."
  type: true-false
  answer: false
  explanation: "False. The contrapositive of p → q is ¬q → ¬p (flip and negate both sides). It is logically equivalent to the original. The statement ¬p → ¬q is the inverse — a different statement that is not necessarily equivalent to p → q. A common error is to confuse the inverse with the contrapositive. Only the contrapositive preserves logical equivalence."

- question: "A classmate argues: 'Since p → q is false when p is true and q is false, it should also be false when p is false and q is false — after all, the conclusion still fails.' Explain why this reasoning is wrong."
  type: short-answer
  answer: "The implication p → q is a conditional promise: 'if p holds, then q must hold.' It is only violated when the premise is in force (p is true) and the conclusion fails (q is false). When p is false, the premise is never activated — no promise was made that applies to this situation. The truth value of q is then irrelevant. Logically, p → q is equivalent to ¬p ∨ q, which is true whenever p is false, regardless of q."
  explanation: "Vacuous truth is one of the hardest aspects of formal implication to accept intuitively. Everyday 'if…then' language often implies a causal relationship, but in propositional logic, implication is purely about truth values. The asymmetry — only one row is false — is what makes implication useful in formal proofs: you can freely use an implication whose antecedent is false without checking the conclusion."
```

## Explainer

A **proposition** is a declarative statement that is unambiguously either true or false — "The sky is blue," "7 is odd," "2 + 2 = 5." Questions, commands, and paradoxes such as "This sentence is false" are not propositions. The power of propositional logic is that once you assign truth values to atomic propositions, you can compute the truth value of any compound statement built from them using **logical connectives**: AND (∧), OR (∨), NOT (¬), IF-THEN (→), and IF-AND-ONLY-IF (↔). Each connective has a precise, non-negotiable meaning captured in a **truth table**.

AND (p ∧ q) is true only when both p and q are true. OR (p ∨ q) is true when at least one is true — this is *inclusive* or, not exclusive. NOT (¬p) flips the truth value. The most subtle connective is **implication** (p → q): it is false only when p is true and q is false. "If it rains, I bring an umbrella" is not falsified by sunny weather — on a dry day, the statement makes no claim at all. This *vacuous truth* surprises beginners, but follows from the definition: p → q is logically equivalent to (¬p ∨ q), which is clearly true whenever p is false.

Truth tables let you evaluate any compound statement systematically. With n propositional variables, there are 2ⁿ rows — one for every combination of truth values. A statement true in every row is a **tautology** (e.g., p ∨ ¬p — "either it's raining or it isn't"). A statement false in every row is a **contradiction** (e.g., p ∧ ¬p). Tautologies are especially important: they are logical guarantees, true regardless of what the variables represent.

Two statements are **logically equivalent** when they have identical truth tables — written p ≡ q. The most useful equivalences are De Morgan's Laws: ¬(p ∧ q) ≡ (¬p ∨ ¬q), and ¬(p ∨ q) ≡ (¬p ∧ ¬q). These let you push negations inward, transforming complex negations into workable form. Equally important is the **contrapositive**: (p → q) ≡ (¬q → ¬p). Since these are logically identical, you can always prove the contrapositive instead of the original implication — whichever is easier. Propositional logic is the bedrock of all formal mathematical reasoning: every proof, every theorem, every valid argument is ultimately grounded in these simple rules about truth values and connectives.
