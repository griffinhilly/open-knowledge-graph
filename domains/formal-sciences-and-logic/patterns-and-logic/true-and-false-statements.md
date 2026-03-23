---
id: true-and-false-statements
title: True and False Statements
domain: formal-sciences-and-logic
course: patterns-and-logic
prerequisites:
- id: recognizing-patterns
  type: soft
builds-toward:
- if-then-statements
- negation-logic-intro
- and-or-everyday
- all-some-none
- propositional-logic-introduction
tags:
- logic
- truth
- statements
- foundational
stage: concrete-operations
status: draft
---

# True and False Statements

## Core Idea
A statement is a sentence that is either true or false — not both, and not neither. "Dogs have four legs" is a true statement. "The sun is cold" is a false statement. "Is it raining?" is not a statement (it is a question). "Wow!" is not a statement (it is an exclamation). Learning to distinguish statements from non-statements, and true statements from false ones, is the first step in logical thinking. Logic is built entirely on the idea that statements have definite truth values.

## How It's Best Learned
Give students a mix of sentences and ask them to sort into three piles: "true statement," "false statement," and "not a statement." Include questions, commands, exclamations, opinions, and clearly true/false factual claims. Discuss borderline cases: is "chocolate is the best flavor" a statement? (It is an opinion, not a factual claim with a definite truth value — introduce this subtlety gently.) Use everyday examples to make the concept tangible.

## Common Misconceptions
- Thinking a false statement is not a statement — false statements are still statements; they just happen to be false.
- Confusing statements with questions or commands — "Close the door" is a command, not something that can be true or false.
- Believing that statements must be true to count — the sentence "2 + 2 = 5" is a perfectly valid statement; it is just a false one.
- Thinking opinions are statements — "pizza is the best food" is subjective and does not have a definite truth value in logic.

## Questions

```yaml
- question: "Which of the following is a statement?"
  type: multiple-choice
  options:
    - "'What time is it?' — a question about time"
    - "'Please sit down' — a polite instruction"
    - "'7 is greater than 3' — a claim that is either true or false"
    - "'Hooray!' — an expression of excitement"
  answer: 2
  explanation: "A statement is a sentence that is either true or false. '7 is greater than 3' is a statement — it makes a claim that can be checked (and it happens to be true). A question asks for information, a command gives an instruction, and an exclamation expresses emotion. None of those are true or false, so none are statements in the logical sense."

- question: "The sentence '2 + 2 = 5' is not a statement because it is wrong."
  type: true-false
  answer: false
  explanation: "Being wrong does not disqualify a sentence from being a statement. '2 + 2 = 5' is a statement — it makes a definite claim that can be evaluated as true or false. It happens to be false. In logic, true statements and false statements are both statements. What matters is not whether the statement is correct, but whether it is the kind of sentence that CAN be true or false."

- question: "An opinion like 'chocolate ice cream is the best flavor' is a true-or-false statement."
  type: true-false
  answer: false
  explanation: "Opinions depend on personal preference and do not have a single definite truth value. 'Chocolate is the best flavor' is true for some people and false for others — logic requires that a statement be definitely one or the other, not a matter of perspective. Factual claims like 'chocolate ice cream contains cocoa' are statements because they can be verified."

- question: "Why is it important in logic that every statement must be either true or false, with no middle ground?"
  type: short-answer
  answer: "Because logical reasoning depends on being able to evaluate whether claims are true or false. If a statement could be 'sort of true' or 'maybe false,' you could not build reliable arguments from it. The true-or-false requirement — called the law of excluded middle — ensures that every logical operation (and, or, not, if-then) produces definite results. Without it, logical reasoning would have no solid foundation."
  explanation: "This principle is one of the three classical laws of logic (alongside the law of non-contradiction and the law of identity). While there are advanced logical systems that relax this requirement, classical logic — and the everyday reasoning students are learning — is built on the assumption that statements have definite truth values."
```

## Explainer

Before you can reason logically, you need to know what logic works with. The answer is **statements** — sentences that are either true or false. Not questions, not commands, not exclamations. Statements.

"The Earth orbits the Sun" is a statement — it is true. "Fish can fly" is a statement — it is false. "What is your name?" is NOT a statement — it is a question, and questions are neither true nor false. "Sit down, please" is NOT a statement — it is a command. "Wow, that is amazing!" is NOT a statement — it is an exclamation. The key test is: **can you say whether this sentence is true or false?** If yes, it is a statement. If no, it is not.

Here is something that surprises many students: **false statements are still statements**. The sentence "2 + 2 = 5" is wrong, but it is still a statement. It makes a clear claim that can be checked. It just happens to fail the check. In logic, being false is not a disqualification — it is a classification. Every statement has a **truth value**: true or false. That truth value is what logic operates on.

One tricky case: opinions. Is "pizza is the best food" a statement? In everyday conversation, people say "that is true!" But in logic, this sentence does not have a definite truth value — it depends on who you ask. Logic works with claims that can be objectively evaluated, like "pizza contains cheese" (true, usually) or "pizza was invented in the year 1000" (can be checked). Separating factual claims from opinions is part of learning to think logically.

This idea — that statements are true or false, and everything in logic starts from there — is the foundation of all the logical reasoning you will learn next. When you study "if-then" statements, "and" and "or," and negation, every one of those operations takes statements as input and produces statements as output. Getting clear on what a statement is will make everything else easier.
