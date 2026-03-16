---
id: domain-and-range
title: Domain and Range
domain: mathematics
course: precalculus
prerequisites:
  - id: function-notation-review
    type: hard
builds-toward:
  - inverse-functions-review
  - rational-functions-asymptotes-review
tags: [functions, domain, range]
stage: formal-systems
status: validated
---

# Domain and Range

## Core Idea
The domain of a function is the set of all valid inputs; the range is the set of all possible outputs. Identifying domain and range is the first step in understanding any function's behavior, because it tells you where the function lives and what values it can produce. Restrictions typically arise from division by zero, square roots of negatives, and logarithms of non-positives.

## How It's Best Learned
Practice finding domains algebraically (set denominators not equal to zero, radicands greater than or equal to zero) and visually from graphs. Use interval notation consistently. For range, graphical methods are often easier than algebraic ones.

## Common Misconceptions
- Assuming every function has domain all real numbers.
- Confusing domain restrictions with the function being undefined vs. just not yet encountered.
- Writing domain/range as a single value instead of a set or interval.

## Explainer

From function notation, you know that f(x) is a rule: you feed in an input x, and the function returns an output f(x). The **domain** is the complete set of inputs you are allowed to feed in — all the x-values where the rule actually works. The **range** is the complete set of outputs the function actually produces — all the values f(x) can take. Together they describe where a function lives.

Most domain restrictions come from three operations that fail on certain inputs. First, division by zero is undefined, so any x that makes a denominator zero is excluded: f(x) = 1/(x − 3) is undefined at x = 3, giving domain (−∞, 3) ∪ (3, ∞). Second, even roots of negatives are not real numbers, so the radicand must be non-negative: g(x) = √(x − 2) requires x − 2 ≥ 0, giving domain [2, ∞). Third, logarithms require positive inputs: h(x) = ln(x + 1) requires x + 1 > 0, giving domain (−1, ∞). To find the domain algebraically, identify which of these three situations applies, set up the corresponding inequality or exclusion, and express the result in interval notation.

Range is harder to find algebraically than domain, because you need to determine which outputs are actually reachable — not just which inputs are valid. Graphically, the range is every y-value the graph touches. Algebraically, one strategy is to write y = f(x) and solve for x in terms of y; the y-values for which a real solution exists form the range. For example, y = x² gives x = ±√y, which has a real solution only when y ≥ 0, so range = [0, ∞).

Compare two functions to see how domain and range can differ despite looking similar: f(x) = x² has domain all reals (you can square anything) and range [0, ∞) (squares are never negative). Its "inverse" f(x) = √x has domain [0, ∞) (you cannot take a square root of a negative) and range [0, ∞) (square roots are never negative). Same range, very different domain. Keeping these sets distinct — and always expressing them as sets or intervals, not single values — is the foundation for analyzing any function's behavior in the topics ahead.
