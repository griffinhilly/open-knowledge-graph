---
id: input-output-tables
title: Input-Output Tables
domain: mathematics
course: 4th-grade
prerequisites:
  - id: multi-digit-multiplication
    type: soft
  - id: multi-digit-addition
    type: soft
builds-toward:
  - patterns-and-sequences
  - number-patterns-and-relationships
  - writing-numerical-expressions
tags: [algebra-readiness, patterns, functions]
stage: concrete-operations
status: validated
---

# Input-Output Tables

## Core Idea
An input-output table shows a consistent rule applied to each input to produce an output. Given inputs of 2, 5, 8 and outputs of 6, 15, 24, the rule is "multiply by 3." Students learn to identify the rule from given pairs, complete missing values, and express the rule in words. This is early function thinking -- the idea that a rule maps each input to exactly one output -- which is foundational for algebra. Input-output tables also reinforce arithmetic fluency as students test different operations to discover the pattern.

## How It's Best Learned
Start with single-operation rules (add 7, multiply by 4) and advance to two-step rules (multiply by 2 then add 1). Have students create their own input-output tables for classmates to solve. Use "function machines" as a metaphor: a number goes in, the machine applies the rule, a number comes out. Practice identifying rules from completed tables, then generating tables from stated rules.

## Common Misconceptions
- Assuming the rule is always addition.
- Looking only at the difference between input and output rather than the multiplicative relationship.
- Confusing two-step rules (thinking "times 2 plus 1" is the same as "times 3").

## Questions

```yaml
- question: "An input-output table shows: input 3 → output 10, input 5 → output 16, input 7 → output 22. What is the rule?"
  type: multiple-choice
  options:
    - "Multiply by 3, then add 1"
    - "Add 7"
    - "Multiply by 2, then add 4"
    - "Multiply by 5, then subtract 5"
  answer: 0
  explanation: "Test 'multiply by 3, then add 1': 3 × 3 + 1 = 10 ✓; 5 × 3 + 1 = 16 ✓; 7 × 3 + 1 = 22 ✓. Rule confirmed. 'Add 7' works for the first pair (3 + 7 = 10) but fails for the second (5 + 7 = 12, not 16). This is exactly why you must test at least two pairs before trusting a rule — one matching pair is often coincidental."

- question: "A table shows: input 2 → output 10, input 4 → output 20, input 6 → output 30. A student says the rule is 'add 8.' Why is this wrong?"
  type: multiple-choice
  options:
    - "The rule is 'add 10' — the student made an arithmetic error"
    - "The rule is 'multiply by 5' — the student only checked one pair and missed the multiplicative pattern"
    - "The student is right — adding 8 to each input gives the correct outputs"
    - "The rule is 'add 8 then add 2' — a two-step additive rule"
  answer: 1
  explanation: "'Add 8' seems to work for the first pair (2 + 8 = 10), but fails immediately for the second (4 + 8 = 12, not 20). The correct rule is 'multiply by 5.' The common error is looking only at the difference between input and output for one pair, rather than checking consistency and testing multiplicative relationships. Always check the ratio (output ÷ input) as well as the difference (output − input)."

- question: "When finding the rule for an input-output table, testing your guess against at least two input-output pairs is necessary to confirm the rule."
  type: true-false
  answer: true
  explanation: "One pair is never enough. Many different rules can match a single pair: for input 3, output 10, both 'add 7' and 'multiply by 3 then add 1' work. A second pair eliminates most false candidates. A rule must hold for every pair in the table without exception. Testing two or more pairs dramatically increases confidence and catches rules that only coincidentally match the first pair."

- question: "If the rule for an input-output table is 'multiply by 4,' then an input of 6 could produce different outputs on different tables using the same rule."
  type: true-false
  answer: false
  explanation: "This is the fundamental property of a function (and an input-output table): a consistent rule maps each input to exactly one output, always. If the rule is 'multiply by 4,' input 6 always produces output 24 — no exceptions, no variation. An input-output 'rule' that sometimes gives different outputs isn't a rule at all. This consistency is what makes the rule useful and what distinguishes a function from a random pairing."

- question: "An input-output table shows: input 3 → output 11, input 6 → output 20. A student guesses the rule is 'multiply by 3, then add 2.' Verify whether this is correct."
  type: short-answer
  answer: "Test pair 1: 3 × 3 + 2 = 11 ✓. Test pair 2: 6 × 3 + 2 = 20 ✓. Both pairs confirm the rule. 'Multiply by 3, then add 2' is correct."
  explanation: "Always substitute both known pairs. A single pair could fit many rules; multiple pairs narrow it to one consistent rule. Notice that input 3 → output 11 could also fit 'add 8,' but 'add 8' fails for input 6 (6 + 8 = 14, not 20). The two-step rule 'multiply by 3 then add 2' is the only simple rule that satisfies both pairs — and that is your confirmation."
```

## Explainer

An input-output table is built around a single hidden rule. Every input goes through the same rule to produce its output — no exceptions. Your job is to discover the rule from the given pairs, and then use it to fill in the missing values. Think of it as a **function machine**: a number drops in the top, the machine does something to it, and a result comes out the bottom. The machine never changes its behavior.

Start by looking at the relationship between one input and its output. Try the four operations. If the input is 5 and the output is 20, ask: did we add 15? Multiply by 4? These are both possible. Test your guess on a second pair to confirm. If input 3 gives output 12, "add 15" fails (3 + 15 = 18, not 12), but "multiply by 4" works (3 × 4 = 12). Always verify your rule with at least two pairs before using it to complete the table.

Multiplicative rules are easier to miss than additive ones because students naturally look at the difference between input and output first. Develop the habit of also testing: "Is the output a fixed multiple of the input?" For a table where inputs are 2, 4, 6 and outputs are 10, 20, 30, the difference between input and output varies (8, 16, 24), but the ratio is constant (5, 5, 5) — the rule is "multiply by 5." Always check both additive and multiplicative possibilities.

Two-step rules — like "multiply by 3 then add 2" — appear when neither simple operation works alone. Input 4, output 14: 4 × 3 = 12, then 12 + 2 = 14. Input 6, output 20: 6 × 3 = 18, then 18 + 2 = 20. When a single operation doesn't fit, look for a pattern in the remainders after removing the multiplicative component. Input-output tables are your first formal encounter with the idea that a rule maps each input to **exactly one** output — a concept that will be called a function when you reach algebra.
