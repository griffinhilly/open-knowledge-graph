---
id: pattern-rules
title: Pattern Rules
domain: formal-sciences-and-logic
course: patterns-and-logic
prerequisites:
- id: number-patterns-logic
  type: hard
- id: recognizing-patterns
  type: hard
builds-toward:
- growing-patterns
- sequences-and-series-logic
- step-by-step-instructions
tags:
- patterns
- rules
- generalization
- algebra-readiness
stage: concrete-operations
status: validated
---

# Pattern Rules

## Core Idea
A pattern rule is a precise description of how a pattern works — the recipe that generates every element. Rules can describe what happens between consecutive terms ("add 3 each time") or connect each term to its position ("the term is 2 times its position number"). Being able to state a clear rule is the difference between noticing a pattern and truly understanding it. Rules make patterns useful: they let you predict any term, check membership, and communicate the pattern to someone who has never seen it.

## How It's Best Learned
Give students patterns and ask them to write the rule in their own words. Compare student descriptions for the same pattern — are they equivalent? Introduce the distinction between "term-to-term" rules (what you do to get from one term to the next) and "position" rules (how to find any term from its position number). Use T-charts with position numbers and term values. Have students create patterns from given rules and trade with classmates.

## Common Misconceptions
- Writing a rule that works for the first few terms but not all terms (e.g., "the numbers go up" instead of "add 4 each time").
- Confusing the starting number with the rule — "the pattern is 5, 8, 11, 14" is a list, not a rule. The rule is "start at 5, add 3."
- Thinking there is only one correct way to state a rule — "add 3 each time" and "each term is 3 more than the last" say the same thing.

## Questions

```yaml
- question: "Two students describe the same pattern (2, 5, 8, 11, 14). Student A says 'add 3 each time.' Student B says 'each term is 3 times its position minus 1.' Are both rules correct?"
  type: multiple-choice
  options:
    - "Only Student A is correct — you can see the +3 in the gaps"
    - "Only Student B is correct — position rules are always better"
    - "Both are correct — they describe the same pattern from different perspectives"
    - "Neither is correct — the rule is 'start at 2'"
  answer: 2
  explanation: "Both rules produce the same pattern. Student A gives a term-to-term rule (recursive): to get the next term, add 3 to the current one. Student B gives a position rule: term = 3 x position - 1 (position 1: 3(1)-1=2, position 2: 3(2)-1=5, etc.). Both are complete, correct descriptions of the same pattern. Having multiple valid descriptions is a strength, not a confusion."

- question: "Which is a complete pattern rule for the sequence 10, 8, 6, 4, 2?"
  type: multiple-choice
  options:
    - "'The numbers get smaller' — that tells you the direction"
    - "'Even numbers' — all the terms are even"
    - "'Start at 10, subtract 2 each time' — that gives the starting point and the operation"
    - "'The pattern is 10, 8, 6, 4, 2' — just list all the terms"
  answer: 2
  explanation: "A complete rule must tell you enough to generate every term. 'Start at 10, subtract 2 each time' does this: you get 10, then 8, then 6, and so on. 'The numbers get smaller' is too vague — many patterns get smaller. 'Even numbers' is an observation, not a rule (it does not specify which even numbers or in what order). Listing all terms is a description, not a rule — it does not tell you what comes next."

- question: "A pattern rule that says 'the numbers go up' is specific enough to identify a unique pattern."
  type: true-false
  answer: false
  explanation: "Infinitely many patterns have numbers that go up: 1, 2, 3, 4... and 1, 10, 100, 1000... and 2, 5, 8, 11... all go up. A useful rule must specify exactly how the numbers change — 'add 3 each time' or 'double each time' or 'each term is its position number squared.' Vague descriptions like 'going up' fail the test of being able to generate the specific pattern."

- question: "What is the difference between a term-to-term rule and a position rule, and why might you want both?"
  type: short-answer
  answer: "A term-to-term rule tells you how to get from one term to the next (e.g., 'add 5'). A position rule tells you how to find any term from its position number (e.g., 'the term is 5 times its position'). The term-to-term rule is easier to spot — you just look at the gaps. The position rule is more powerful — it lets you jump to the 100th term without listing all the ones before it. You want both because the term-to-term rule is easy to discover, and the position rule is efficient to use."
  explanation: "This distinction — recursive vs. explicit — is fundamental in mathematics. Term-to-term rules are recursive (each term depends on the previous one). Position rules are explicit (each term is computed independently). Much of algebra involves converting between these two forms, and students who understand both at the pattern level have a head start."
```

## Explainer

So far you have been recognizing and extending patterns. Now you are going to focus on the most important part: **stating the rule**. The rule is the engine of a pattern — the precise recipe that tells someone everything they need to generate the entire sequence.

There are two kinds of rules, and both are useful. A **term-to-term rule** tells you how to get from one element to the next. For the pattern 4, 7, 10, 13, the term-to-term rule is "add 3 each time." This rule is easy to spot: just look at the differences between consecutive terms (7-4=3, 10-7=3, 13-10=3). A **position rule** tells you how to find any element from its position number. For the same pattern, the position rule is "the term equals 3 times the position plus 1" (position 1: 3x1+1=4; position 2: 3x2+1=7; position 3: 3x3+1=10).

Why have two kinds of rules? Because they have different strengths. The term-to-term rule is easy to discover — you look at the jumps between neighbors. But to find the 50th term, you would need to compute all 49 terms before it. The position rule is harder to find, but once you have it, you can jump straight to any term: the 50th term is 3(50)+1 = 151. No listing required.

A good rule passes three tests. First, it generates every element of the pattern correctly. Second, it is specific enough that someone who has never seen the pattern can recreate it. Third, it does not include unnecessary details. "Start at 4, add 3 each time" passes all three. "The numbers go up" fails the second test — it is too vague. "4, 7, 10, 13, 16, 19, 22" fails the third — it is a list, not a rule. The habit of writing clear, precise rules is the beginning of thinking like a mathematician.
