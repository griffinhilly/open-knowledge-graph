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
status: validated
---

# Formal Logic and Propositional Calculus

## Core Idea
Propositional logic formalizes reasoning with statements that are either true or false. Logical operators (AND, OR, NOT, conditional, biconditional) combine propositions into compound statements. Truth tables systematically determine the truth value of any logical expression.

## How It's Best Learned
Build truth tables for increasingly complex formulas. Identify logical equivalences and laws (De Morgan's, distributive, associative). Recognize common patterns like tautologies and contradictions.

## Common Misconceptions
The conditional 'if P then Q' is true when P is false (vacuous truth)—this confuses many. Biconditional requires both directions to be true, not just one.

## Questions

```yaml
- question: "For which combination of truth values is the conditional P → Q false?"
  type: multiple-choice
  options:
    - "P is false and Q is false"
    - "P is false and Q is true"
    - "P is true and Q is false"
    - "P is true and Q is true"
  answer: 2
  explanation: "P → Q is false only when the hypothesis P is true but the conclusion Q is false — a promise was made (P is true) but broken (Q is false). All other cases make the conditional true: when P is false, the conditional makes no claim about what happens, so it cannot be violated (vacuous truth). Many students intuitively expect P → Q to be false when P is false ('nothing was guaranteed'), but this is wrong — a conditional with a false hypothesis is automatically true in classical logic."

- question: "You know that 'If it rained last night, the sidewalk is wet' is true. You walk outside and see that the sidewalk IS wet. What can you logically conclude?"
  type: multiple-choice
  options:
    - "It rained last night — the wet sidewalk confirms the conditional"
    - "Nothing about whether it rained — the wet sidewalk is consistent with rain, but also with other causes"
    - "It definitely did not rain — the conditional only runs one way"
    - "The conditional must be false — sidewalks can be wet without rain"
  answer: 1
  explanation: "This tests the fallacy of affirming the consequent: P → Q and Q being true does NOT allow you to conclude P. The sidewalk could be wet because of rain, a sprinkler, someone washing it, morning dew, etc. The conditional only licenses the inference from P (it rained) to Q (wet sidewalk), not from Q back to P. The valid inference in the other direction is the contrapositive: if the sidewalk is NOT wet, then it did NOT rain (¬Q → ¬P). This is why modus ponens (from P → Q and P, conclude Q) is valid, but affirming the consequent is not."

- question: "In classical propositional logic, the statement 'If 2 + 2 = 5, then the moon is made of cheese' is TRUE."
  type: true-false
  answer: true
  explanation: "This is the famous vacuous truth. P → Q is false only when P is true and Q is false. Here, P ('2 + 2 = 5') is false, so the conditional cannot be violated — it is automatically true regardless of Q. This feels counterintuitive because we expect the content of P and Q to matter. But in classical logic, the conditional only makes a claim about what happens when P holds. When P is false, no claim is made, so no claim can be falsified. Vacuous truth is not a bug but a feature: it ensures conditionals with impossible hypotheses are always true, which is essential for mathematical reasoning."

- question: "In propositional logic, 'P OR Q' is true primarily when exactly one of P or Q is true — not when both are true."
  type: true-false
  answer: false
  explanation: "Propositional logic uses inclusive or: P ∨ Q is true whenever at least one of P or Q is true, including when both are true. It is false only when both P and Q are false. Exclusive or (XOR), which requires exactly one to be true, is a separate connective that must be explicitly constructed from the basic ones. The confusion between inclusive and exclusive or is extremely common and leads to incorrect truth table entries. In ordinary English, 'or' is sometimes exclusive ('you can have cake or pie'), but in logic the default is always inclusive."

- question: "Why is the conditional P → Q vacuously true when P is false? Use a concrete example to explain the logic."
  type: short-answer
  answer: "The conditional P → Q makes a conditional promise: 'whenever P holds, Q will hold.' If P never holds (P is false), the promise is never tested and therefore cannot be broken. Example: 'If you score 100% on every exam, you will get an A.' If you do not score 100% on every exam, this promise says nothing — it is not violated. In classical logic, the only way to falsify a conditional is to have P true while Q is false — the premise is satisfied but the conclusion fails. A false premise means the condition that would activate the promise never occurs."
  explanation: "Vacuous truth preserves the logical behavior that conditionals need for mathematical reasoning. In proofs, we often want statements like 'For all x, if x is an even prime greater than 2, then x is divisible by 7' to be true — because there are no even primes greater than 2, the condition is never triggered and the statement is vacuously true. This allows universal statements to be true without requiring any instances to exist. The alternative — making conditionals with false hypotheses false — would collapse mathematical logic."
```

## Explainer

You already know the conditional (if P then Q) and the biconditional (P if and only if Q) from your prerequisite work. Propositional logic now gives you the complete toolkit: a formal language where every statement has a definite truth value and every compound statement's truth value is fully determined by the truth values of its parts. A **proposition** is any declarative statement that is either true or false — "It is raining" qualifies; "Is it raining?" does not. Variables like P and Q stand in for propositions, and **logical connectives** combine them: negation (¬P, "not P"), conjunction (P ∧ Q, "P and Q"), disjunction (P ∨ Q, "P or Q"), the conditional (P → Q), and the biconditional (P ↔ Q).

A **truth table** is the mechanical tool for determining the truth value of any compound statement across all possible combinations of its variables. For n variables, the table has 2ⁿ rows. The connectives you need to memorize: ¬P flips truth value; P ∧ Q is true only when both are true; P ∨ Q is false only when both are false (inclusive or); P → Q is false only when P is true and Q is false. That last rule — the conditional is true whenever its hypothesis is false — is the famous **vacuous truth**. "If 2 + 2 = 5, then the moon is made of cheese" is a true statement in classical logic, because the hypothesis is false and the conditional makes no claim about what happens when its premise fails.

Two statements are **logically equivalent** when they have identical truth tables. The most important equivalences to know are **De Morgan's laws**: ¬(P ∧ Q) ≡ (¬P ∨ ¬Q) and ¬(P ∨ Q) ≡ (¬P ∧ ¬Q). These let you push negations inward. The contrapositive equivalence — P → Q ≡ ¬Q → ¬P — is equally important: proving the contrapositive is one of the standard proof strategies you will use immediately in the next course.

A **tautology** is a formula that is true in every row of its truth table: P ∨ ¬P is the simplest example. A **contradiction** is false in every row: P ∧ ¬P. Tautologies represent logical laws that hold regardless of the facts; contradictions represent impossible combinations. Recognizing whether an argument's conclusion follows necessarily from its premises — formal validity — is exactly the problem propositional logic was designed to solve, and truth tables give you a decision procedure: check whether every row where all premises are true also has the conclusion true.
