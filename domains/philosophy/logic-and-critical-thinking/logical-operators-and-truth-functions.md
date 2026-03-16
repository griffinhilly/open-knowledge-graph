---
id: logical-operators-and-truth-functions
title: Logical Operators and Truth Functions
domain: philosophy
course: logic-and-critical-thinking
prerequisites:
- id: propositional-logic-introduction
  type: soft
builds-toward:
- conditional-statements-and-material-conditional
- testing-validity-with-counterexamples
tags:
- logic
- operators
- truth-functions
- foundational
stage: abstract-reasoning
status: draft
---

# Logical Operators and Truth Functions

## Core Idea
The basic logical operators—conjunction (AND), disjunction (OR), and negation (NOT)—combine propositions into more complex statements. Each operator has precise truth conditions: AND is true only when both parts are true, OR is true when at least one part is true, and NOT reverses truth value. Understanding these operators is foundational to evaluating logical arguments.

## How It's Best Learned
Begin with simple two-proposition examples and truth tables for each operator. Show how they combine and interact. Use everyday language parallels, then formalize the notation.

## Common Misconceptions
Confusing English 'or' (often exclusive: 'you can have cake or ice cream') with logical OR (inclusive: at least one is true). Misplacing negation scope: 'not all birds fly' means 'some birds don't fly,' not 'no birds fly.'

## Explainer

From propositional logic, you know that propositions are the basic units—statements that are either true or false. Logical operators are the tools we use to build more complex statements from simpler ones. But unlike natural language connectives ("and," "or," "not"), logical operators have perfectly precise, fixed meanings defined entirely by their **truth tables**—tables that specify the output truth value for every possible combination of input truth values.

**Conjunction** (AND, written P ∧ Q) is true only when both P and Q are true. Think of it as requiring unanimous agreement: the compound sentence fails the moment either part fails. "It is raining AND cold" is false if it's raining but warm. This strictness is why AND is a powerful claim—satisfying it requires two conditions to hold at once. **Disjunction** (OR, written P ∨ Q) is true when at least one part is true. This is the key divergence from everyday English: when someone says "you can have cake or ice cream," they often mean exactly one. Logical OR is **inclusive**—it allows both. P ∨ Q is false only when both P and Q are false. This distinction matters in arguments: "the patient has disease A or disease B" does not rule out having both, and reasoning that treats OR as exclusive will produce errors.

**Negation** (NOT, written ¬P) simply flips the truth value. True becomes false; false becomes true. But scope matters enormously. "Not all politicians are corrupt" (¬∀x: corrupt(x)) means at least one isn't corrupt—it's compatible with most being corrupt. "All politicians are not corrupt" (∀x: ¬corrupt(x)) means none are. The negation sign works on what follows it, not on everything in sight. This is why careful attention to where NOT is placed changes the meaning entirely.

The power of truth tables is that they make validity mechanical. Once you express an argument in terms of P, Q, ¬, ∧, ∨, you can test every possible assignment of T and F to the variables. If the conclusion is true in every row where all premises are true, the argument is valid—no exceptions possible. This is how formal logic earns its rigor: not by telling you what's true about the world, but by guaranteeing that once you accept the premises, the conclusion is unavoidable. Mastering these three operators is the foundation from which all more complex logical analysis—including conditionals and quantifiers—is built.
