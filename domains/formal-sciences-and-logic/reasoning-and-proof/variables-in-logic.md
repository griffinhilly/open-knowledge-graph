---
id: variables-in-logic
title: Variables in Logic
domain: formal-sciences-and-logic
course: reasoning-and-proof
prerequisites:
  - id: what-is-an-argument
    type: hard
  - id: variable-expressions
    type: soft
builds-toward:
  - conditional-statements-formal
  - truth-tables-introduction
  - propositional-logic-introduction
tags: [variables, propositions, abstraction, logic]
stage: abstract-reasoning
status: validated
---

# Variables in Logic

## Core Idea
Just as algebra uses letters like x and y to stand for unknown numbers, logic uses letters like P and Q to stand for statements that can be true or false. Writing "If P, then Q" lets you study the structure of an argument without specifying what P and Q actually say. This abstraction is what makes logic powerful — a rule about "If P, then Q" applies to every argument with that shape, whether P means "it rains" or "the number is even." Variables in logic separate the form of reasoning from its content.

## How It's Best Learned
Begin with a concrete argument: "If it is raining, then the ground is wet." Label the parts: let P = "it is raining" and Q = "the ground is wet." Then show the same structure in a different context: P = "you study," Q = "you pass." The identical form "If P, then Q" captures both. Have students translate five different arguments into P-Q form and recognize they share a structure. Connect to algebraic variables: in algebra, x + x = 2x works for any number; in logic, "If P, then Q" works for any statements.

## Common Misconceptions
- Confusing logical variables (which stand for statements) with algebraic variables (which stand for numbers). P represents a whole statement like "it is Tuesday," not a number.
- Thinking the variable letters carry meaning. P and Q are arbitrary labels — you could use A and B or any other letters.
- Assuming a logical variable can be "partially true." In classical logic, each variable is either fully true or fully false.

## Questions

```yaml
- question: "In the statement 'If P, then Q,' what does the variable P represent?"
  type: multiple-choice
  options:
    - "A number we do not know yet"
    - "A statement that is either true or false"
    - "A question that needs an answer"
    - "The probability of an event"
  answer: 1
  explanation: "In logic, P is a propositional variable — it stands for a declarative statement with a definite truth value (true or false). This is different from algebraic variables, which represent numbers. P might stand for 'it is raining' or 'the number is prime' — any statement that is either true or false."

- question: "The logical statement 'If P, then Q' can only be used when P means 'it is raining' and Q means 'the ground is wet.'"
  type: true-false
  answer: false
  explanation: "That is one specific substitution, but the whole point of using variables is generality. 'If P, then Q' captures the structure of ANY if-then argument. P could mean 'you practice daily' and Q could mean 'you improve.' The form works regardless of what specific statements P and Q represent."

- question: "Translate this argument into variable form: 'If the battery is dead, then the car will not start. The battery is dead. Therefore, the car will not start.'"
  type: short-answer
  answer: "Let P = 'the battery is dead' and Q = 'the car will not start.' The argument is: If P, then Q. P. Therefore Q."
  explanation: "The translation strips away the specific content and reveals the logical skeleton. This skeleton — 'If P, then Q; P; therefore Q' — is a valid argument form called modus ponens. Any argument with this shape is valid, regardless of what P and Q represent. That is the power of working with variables."
```

## Explainer

In algebra, you learned to write x + 5 = 12 and solve for x. The letter x stands for an unknown number. Logic does something similar but with a different kind of object: instead of numbers, logical variables stand for statements. When you write P to mean "the sun is shining" or Q to mean "I will go for a walk," you are creating placeholders that let you talk about the structure of reasoning without getting caught up in the details.

Why bother? Because logical structure is what determines whether reasoning is valid. The argument "If it is raining, then the ground is wet; it is raining; therefore the ground is wet" has exactly the same structure as "If the number is even, then it is divisible by 2; the number is even; therefore it is divisible by 2." Both are instances of "If P, then Q; P; therefore Q." By working with variables, you study all arguments of this form simultaneously rather than analyzing each one individually.

The key difference from algebraic variables: in algebra, x represents a number and can take values like 3 or -7.5. In logic, P represents a complete statement and can take exactly two values — true or false. There is no "partially true" or "somewhat false" in classical logic. When you substitute a specific statement for P, that statement is either true or false, and the logical structure tells you what follows.

The letters you choose are arbitrary. P and Q are traditional, but you could use A and B, or S₁ and S₂, or any other labels. What matters is consistency: once you define P as "it is raining," you must use P for that same statement throughout the argument. This is the same discipline as algebra — once you say x = 3, you cannot later treat x as 5 within the same problem.

This abstraction is what turns logic from a collection of specific arguments into a general science of reasoning. Every rule you will learn — about conditionals, contrapositives, truth tables, and proofs — will be stated in terms of variables, and will therefore apply to every possible argument with the matching structure.
