---
id: number-patterns-logic
title: Number Patterns
domain: formal-sciences-and-logic
course: patterns-and-logic
prerequisites:
- id: extending-patterns-logic
  type: hard
- id: arithmetic-patterns-3rd
  type: soft
- id: skip-counting-patterns-3rd
  type: soft
builds-toward:
- pattern-rules
- growing-patterns
tags:
- patterns
- numbers
- sequences
- arithmetic
stage: concrete-operations
status: validated
---

# Number Patterns

## Core Idea
Number patterns are sequences of numbers that follow a rule. The rule might be additive (add 4 each time: 3, 7, 11, 15), subtractive (subtract 2: 20, 18, 16, 14), multiplicative (double each time: 2, 4, 8, 16), or involve other operations. Identifying the rule behind a number pattern requires looking at the relationship between consecutive terms. Number patterns connect arithmetic skills to logical reasoning — instead of just computing, you are detecting structure.

## How It's Best Learned
Present sequences and ask students to find the rule before extending. Start with constant-difference patterns (add 5, subtract 3) before introducing constant-ratio patterns (multiply by 2). Use number lines to visualize the jumps between terms. Have students create their own number patterns and challenge classmates to find the rule. Include patterns that start at different points but follow the same rule (e.g., 1, 4, 7, 10 and 2, 5, 8, 11 both add 3).

## Common Misconceptions
- Only looking at the first gap between terms and assuming it continues (e.g., seeing 2, 4 and assuming "add 2" when the pattern is actually "multiply by 2" — which gives 2, 4, 8, 16, not 2, 4, 6, 8).
- Confusing the starting number with the rule — the rule is about the relationship between terms, not the first number.
- Thinking all number patterns must increase — patterns can decrease (subtract) or stay the same in interesting ways.

## Questions

```yaml
- question: "What is the rule for this pattern: 100, 90, 80, 70, 60?"
  type: multiple-choice
  options:
    - "Multiply by 10 each time"
    - "Subtract 10 each time"
    - "Divide by 10 each time"
    - "Add 10 each time"
  answer: 1
  explanation: "Each term is 10 less than the one before it: 100 - 10 = 90, 90 - 10 = 80, and so on. The rule is 'subtract 10 each time.' This is a decreasing pattern — not all patterns go up. The constant difference (10) between consecutive terms is the signature of an additive (or in this case, subtractive) pattern."

- question: "Two patterns both have 4 as their second term: Pattern A is 2, 4, 6, 8, 10 and Pattern B is 2, 4, 8, 16, 32. Why do they produce completely different sequences despite starting the same way?"
  type: multiple-choice
  options:
    - "They use different starting numbers"
    - "Pattern A adds 2 each time while Pattern B multiplies by 2 each time — different rules produce different sequences even from the same start"
    - "Pattern B has an error after the 4"
    - "Both patterns actually produce the same sequence"
  answer: 1
  explanation: "Pattern A follows the rule 'add 2' (differences are constant: 2, 2, 2, 2). Pattern B follows the rule 'multiply by 2' (each term is double the previous one). They share the first two terms (2, 4) by coincidence, but the rules are fundamentally different. This is why identifying the rule — not just the next term — matters: the same starting terms can lead to wildly different patterns."

- question: "Every number pattern must increase — the numbers must get bigger each time."
  type: true-false
  answer: false
  explanation: "Patterns can decrease (subtract each time: 50, 45, 40, 35), stay constant (5, 5, 5, 5), or alternate (1, 3, 1, 3). The defining feature of a pattern is a predictable rule, not the direction of change. Decreasing patterns are just as valid and important as increasing ones."

- question: "Explain why the rule of a number pattern is more useful than just knowing the next term."
  type: short-answer
  answer: "The rule lets you find any term in the pattern without listing them all. If you only know the next term, you can extend one step. But if you know the rule (for example, 'add 7 each time, starting at 3'), you can find the 100th term, check whether a specific number belongs to the pattern, and explain why the pattern works. The rule is the complete description; a single next term is just one data point."
  explanation: "This is the transition from arithmetic to algebraic thinking. Knowing the rule 'add 7, start at 3' is equivalent to the formula 3 + 7n (which students will encounter later). The rule generalizes — it answers every possible question about the pattern, not just 'what comes next?'"
```

## Explainer

You have worked with patterns made of shapes and colors. Now you are going to focus on **number patterns** — sequences where the elements are numbers and the rule involves arithmetic.

The simplest number patterns have a **constant difference**: you add (or subtract) the same amount each time. The pattern 5, 8, 11, 14, 17 adds 3 each time. The pattern 30, 25, 20, 15 subtracts 5 each time. To find the rule, look at the gaps between consecutive terms: 8 - 5 = 3, 11 - 8 = 3, 14 - 11 = 3. If the gaps are all the same, you have found a constant-difference rule. This is the same structure as skip-counting, which you have already practiced.

Some number patterns use multiplication instead of addition. The pattern 3, 6, 12, 24 doubles each time (multiply by 2). The gaps between terms are 3, 6, 12 — they are not constant. Instead, each term is a constant *multiple* of the previous one. These patterns grow much faster than additive ones. A pattern that adds 3 each time reaches 30 after 10 steps. A pattern that multiplies by 3 each time reaches 59,049 after 10 steps. The type of rule — additive versus multiplicative — completely determines how the pattern behaves.

Here is a powerful idea: two patterns can share the same first few terms but follow different rules. The sequences 2, 4, 6, 8 and 2, 4, 8, 16 both start with 2, 4 — but the first adds 2, while the second multiplies by 2. After just a few more terms, they look completely different. This is why stating the **rule** matters more than listing a few terms. The rule is the complete recipe for the pattern; a few terms are just a sample.

Number patterns are where arithmetic meets logic. You are not just computing — you are detecting a hidden structure, testing whether your rule holds for every term, and using it to predict terms you have never seen. This is the same reasoning process scientists use when they spot a trend in data and ask, "What rule explains this?"
