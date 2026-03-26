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

## Questions

```yaml
- question: "What is the domain of f(x) = √(x + 3) / (x − 1)?"
  type: multiple-choice
  options:
    - "All real numbers"
    - "x ≥ −3, written [−3, ∞)"
    - "x ≥ −3 and x ≠ 1, written [−3, 1) ∪ (1, ∞)"
    - "x > 0"
  answer: 2
  explanation: "Two restrictions apply simultaneously. The square root requires x + 3 ≥ 0, giving x ≥ −3. The denominator requires x − 1 ≠ 0, excluding x = 1. Both must hold: the domain is all x ≥ −3 except x = 1. Option B misses the denominator restriction; Option A assumes all inputs are valid; Option D ignores both restrictions. When multiple constraints exist, every one of them must be satisfied."

- question: "A student claims the range of f(x) = x² is all real numbers because 'x can be any real number.' What error has the student made?"
  type: multiple-choice
  options:
    - "None — x² does produce all real numbers as outputs"
    - "The student has confused the domain with the range — x can be any real number (the domain), but x² is never negative (the range is [0, ∞))"
    - "The student correctly identified the domain but should express it in interval notation"
    - "The student is wrong because x cannot equal 0"
  answer: 1
  explanation: "The student described the domain (inputs: any real number) but called it the range. The range is the set of actual output values. Since squaring any real number — positive, negative, or zero — always produces a non-negative result, the range is [0, ∞). Negative numbers are simply unreachable outputs. This is the core distinction: domain is where the function accepts inputs; range is where its outputs actually land."

- question: "The range of f(x) = x² is most real numbers."
  type: true-false
  answer: false
  explanation: "The domain of f(x) = x² is all real numbers (any real input can be squared), but the range is only [0, ∞). Squaring any real number — whether positive, negative, or zero — always yields a non-negative result. There is no input x such that x² < 0, so negative numbers are not in the range. This is a common confusion: a function with an unrestricted domain can still have a restricted range."

- question: "To find the range of a function algebraically, one strategy is to write y = f(x), solve for x in terms of y, and determine which values of y allow a real solution for x."
  type: true-false
  answer: true
  explanation: "This is the standard algebraic method for finding range. For y = x², solving gives x = ±√y, which has a real solution only when y ≥ 0, confirming range = [0, ∞). The strategy works because you are asking: 'which output values y are actually achievable?' — i.e., which y allow a valid input x to exist. When this algebraic approach is cumbersome, graphical inspection (reading all y-values from the graph) is often easier."

- question: "Explain why finding the range of a function is generally more difficult than finding its domain."
  type: short-answer
  answer: "Finding the domain requires identifying which inputs cause the function to fail — division by zero, square roots of negatives, or logarithms of non-positives — which reduces to setting up simple inequalities or exclusions. Finding the range requires determining which outputs the function actually produces across all valid inputs. There is no simple algebraic check analogous to 'set denominator ≠ 0': you must reason about the function's behavior as a whole, either by analyzing the formula algebraically (solving y = f(x) for x and asking which y allow a real solution) or by reading all y-values from a graph. The range depends on the function's specific structure, not just which inputs are forbidden."
  explanation: "Domain restrictions come from a short list of operations that fail on specific inputs — easily checked by inspection. Range requires understanding what the function actually does to its inputs across the entire domain. For example, f(x) = x² has domain all reals (no failures) but range [0, ∞) — you can only discover this by observing that squaring always yields non-negative results, which requires understanding the function's behavior, not just its failure modes."
```

## Explainer

From function notation, you know that f(x) is a rule: you feed in an input x, and the function returns an output f(x). The **domain** is the complete set of inputs you are allowed to feed in — all the x-values where the rule actually works. The **range** is the complete set of outputs the function actually produces — all the values f(x) can take. Together they describe where a function lives.

Most domain restrictions come from three operations that fail on certain inputs. First, division by zero is undefined, so any x that makes a denominator zero is excluded: f(x) = 1/(x − 3) is undefined at x = 3, giving domain (−∞, 3) ∪ (3, ∞). Second, even roots of negatives are not real numbers, so the radicand must be non-negative: g(x) = √(x − 2) requires x − 2 ≥ 0, giving domain [2, ∞). Third, logarithms require positive inputs: h(x) = ln(x + 1) requires x + 1 > 0, giving domain (−1, ∞). To find the domain algebraically, identify which of these three situations applies, set up the corresponding inequality or exclusion, and express the result in interval notation.

Range is harder to find algebraically than domain, because you need to determine which outputs are actually reachable — not just which inputs are valid. Graphically, the range is every y-value the graph touches. Algebraically, one strategy is to write y = f(x) and solve for x in terms of y; the y-values for which a real solution exists form the range. For example, y = x² gives x = ±√y, which has a real solution only when y ≥ 0, so range = [0, ∞).

Compare two functions to see how domain and range can differ despite looking similar: f(x) = x² has domain all reals (you can square anything) and range [0, ∞) (squares are never negative). Its "inverse" f(x) = √x has domain [0, ∞) (you cannot take a square root of a negative) and range [0, ∞) (square roots are never negative). Same range, very different domain. Keeping these sets distinct — and always expressing them as sets or intervals, not single values — is the foundation for analyzing any function's behavior in the topics ahead.
