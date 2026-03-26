---
id: arithmetic-sequences
title: Arithmetic Sequences
domain: mathematics
course: algebra-1
prerequisites:
- id: variable-expressions
  type: hard
- id: slope-concept
  type: soft
- id: writing-linear-equations
  type: soft
- id: arithmetic-patterns-3rd
  type: soft
- id: function-tables
  type: soft
- id: arithmetic-patterns-sequences-3rd
  type: soft
builds-toward:
- geometric-sequences
- arithmetic-sequences-and-series
- linear-functions
tags:
- sequences
- arithmetic
- common-difference
- patterns
stage: abstract-reasoning
status: validated
---
# Arithmetic Sequences

## Core Idea
An arithmetic sequence is a list of numbers where the difference between consecutive terms is constant. This constant is called the common difference (d). The sequence 3, 7, 11, 15, 19, ... has a common difference of 4. The nth term formula is aₙ = a₁ + (n − 1)d, where a₁ is the first term. Arithmetic sequences are discrete versions of linear functions — if you plot the term number against the term value, the points fall on a line with slope d and y-intercept a₁ − d. They appear in salary schedules, seating arrangements, and any context with a constant rate of change applied in steps.

## How It's Best Learned
Start with patterns: give sequences and ask students to find the common difference. Then use the formula to find specific terms (what is the 50th term?). Connect to linear equations: the common difference is the slope, and the first term determines the intercept. Practice finding d given two terms, writing the explicit formula, and determining whether a given number is in the sequence.

## Common Misconceptions
- Using n instead of (n − 1) in the formula (off by one error — the first term is a₁, not a₁ + d).
- Confusing arithmetic sequences with geometric sequences (adding vs. multiplying).
- Not recognizing negative common differences (decreasing sequences are still arithmetic).

## Questions

```yaml
- question: "The explicit formula for an arithmetic sequence is aₙ = a₁ + (n − 1)d. A student mistakenly writes aₙ = a₁ + nd instead. What specific error does this introduce?"
  type: multiple-choice
  options:
    - "The formula now calculates the sum of the sequence instead of a single term"
    - "The formula produces a result that is exactly d too large — it adds d one extra time, as if the first term had already had d added to it"
    - "The formula breaks down only for large values of n"
    - "The formula confuses the common difference with the first term"
  answer: 1
  explanation: "The (n − 1) exists because to reach the nth term you add d exactly (n − 1) times — the first term is reached with zero additions of d. Using nd instead adds d one extra time, producing a result that is always d larger than the correct answer. For example, in the sequence 3, 7, 11, 15... with a₁ = 3 and d = 4: the 3rd term should be 11. The correct formula gives 3 + (3−1)×4 = 11; the wrong formula gives 3 + 3×4 = 15 — that's the 4th term, not the 3rd."

- question: "You plot the terms of the arithmetic sequence 5, 8, 11, 14, 17, ... with term number n on the x-axis and term value on the y-axis. What does the graph look like, and what determines its slope?"
  type: multiple-choice
  options:
    - "A curved (parabolic) line, because the values keep increasing"
    - "Points falling on a straight line with slope 5, since a₁ = 5"
    - "Points falling on a straight line with slope 3, since the common difference d = 3"
    - "A scatter plot with no pattern, since sequences are discrete"
  answer: 2
  explanation: "Arithmetic sequences are discrete linear functions. When plotted, the points fall exactly on a straight line. The slope of that line is the common difference d — in this case, 3. The first term a₁ determines the y-intercept (specifically, the y-intercept of the underlying line is a₁ − d = 5 − 3 = 2). Option B is the classic confusion: a₁ is the value of the first term, not the slope. The rate of change between terms — which is what slope measures — is d."

- question: "A decreasing arithmetic sequence (where each term is smaller than the previous) is not truly arithmetic because the common difference is expected to be positive."
  type: true-false
  answer: false
  explanation: "A sequence is arithmetic if the difference between consecutive terms is constant — regardless of sign. A negative common difference (d < 0) produces a decreasing sequence that is perfectly arithmetic. For example, 20, 15, 10, 5, 0, −5, ... has d = −5 and is arithmetic. The formula aₙ = a₁ + (n − 1)d works exactly the same way; d being negative simply means the sequence decreases rather than increases."

- question: "An arithmetic sequence is a discrete version of a linear function: the common difference plays the same role as slope."
  type: true-false
  answer: true
  explanation: "The explicit formula aₙ = a₁ + (n − 1)d can be rewritten as aₙ = d·n + (a₁ − d), which is exactly slope-intercept form y = mx + b. The common difference d is the slope (the constant rate of change per step), and (a₁ − d) is the y-intercept. The only difference from a continuous linear function is that n is restricted to positive integers — you only hit discrete points on the line rather than every real x-value."

- question: "A job starts at a salary of $48,000 and increases by $3,000 every year. Explain why this is an arithmetic sequence and calculate the salary in the 6th year."
  type: short-answer
  answer: "This is arithmetic because the salary increases by a constant amount ($3,000) each year — that constant is the common difference d = 3,000. Using the explicit formula: a₆ = a₁ + (n − 1)d = 48,000 + (6 − 1)(3,000) = 48,000 + 15,000 = $63,000."
  explanation: "The key check for arithmetic sequences is whether the difference between any two consecutive terms is always the same. Here, year 1 to year 2 increases by $3,000, year 2 to year 3 increases by $3,000, and so on — constant difference, arithmetic sequence. The (n − 1) in the formula accounts for the fact that you add d five times to get from year 1 to year 6, not six times."
```

## Explainer

An arithmetic sequence is what you get when you apply a constant rate of change one step at a time. Consider a parking garage that charges $5 to enter and $3 for each hour. After 1 hour you've paid $8, after 2 hours $11, after 3 hours $14. Each term is exactly $3 more than the last — that $3 is the **common difference** d. The sequence 8, 11, 14, 17, 20, ... is arithmetic because the gap between consecutive terms never changes. You already know variable expressions; the sequence is really a rule: start at a₁ and keep adding d.

The explicit formula aₙ = a₁ + (n − 1)d lets you jump directly to any term without computing all the ones before it. The "(n − 1)" rather than "n" reflects a simple fact: to reach the nth term you add d exactly (n − 1) times, because the first term is reached with zero additions. For the parking garage, the 10th hour costs 8 + (10 − 1) × 3 = 8 + 27 = $35. Notice this formula is secretly a linear equation: rewrite it as aₙ = d · n + (a₁ − d). If you already know slope from graphing linear equations, you'll recognize d as the slope and (a₁ − d) as the y-intercept. The "term number" n plays the role of x, and the term value aₙ plays the role of y.

This connection to linear functions is the key insight. If you plot (n, aₙ) on a graph — term number on the horizontal axis, term value on the vertical — the points fall exactly on a straight line. The slope of that line is d, the common difference. Arithmetic sequences are discrete linear functions: instead of a continuous line through all real x-values, you only hit the integer points n = 1, 2, 3, .... This is why arithmetic sequences build toward linear functions: they're the same mathematical structure, just restricted to whole-number inputs.

You can also work backward. If you know two terms but not a₁ or d, you can find both. Suppose the 4th term is 19 and the 7th term is 31. The difference of 31 − 19 = 12 spans 3 steps (from n = 4 to n = 7), so d = 12/3 = 4. Then a₁ = 19 − (4 − 1) × 4 = 19 − 12 = 7. To check whether a specific number is in the sequence, solve aₙ = target for n and check whether the answer is a positive whole number. This algebraic thinking — using the formula as an equation to solve — is what connects sequences to the broader toolkit of algebra you've been building.
