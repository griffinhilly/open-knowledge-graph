---
id: absolute-extrema-closed-interval
title: Absolute Extrema and the Closed Interval Method
domain: mathematics
course: calculus-1
prerequisites:
  - id: continuity-definition
    type: hard
  - id: first-derivative-test
    type: hard
  - id: intermediate-value-theorem
    type: soft
builds-toward:
  - optimization-problems
  - extreme-value-theorem-rigorous
tags: [calculus, extrema, extreme-value-theorem, critical-points, closed-interval-method]
stage: formal-systems
status: validated
---

# Absolute Extrema and the Closed Interval Method

## Core Idea
An absolute maximum of f on an interval is the largest value f takes anywhere on that interval, and an absolute minimum is the smallest. The Extreme Value Theorem guarantees that a function continuous on a closed interval [a, b] has both. Fermat's theorem says that an interior extremum can only occur where f'(x) = 0 or f'(x) does not exist. So the closed interval method is: find the critical numbers inside (a, b), evaluate f at them and at the endpoints a and b, and pick the largest and smallest values.

## How It's Best Learned
Sketch graphs on closed intervals and mark where the highest and lowest points occur, so students see that the answer can be at an endpoint or at a critical number. Show counterexamples that break each hypothesis of the Extreme Value Theorem (an open interval, a discontinuity). Then practice the method with a table of candidate x-values and their f-values.

## Common Misconceptions
- An absolute extremum must occur where f'(x) = 0. (It can also occur at an endpoint or where f' does not exist, as with f(x) = |x| at x = 0.)
- Every function has an absolute maximum and minimum on any interval. (The guarantee needs continuity and a closed, bounded interval; f(x) = x on (0, 1) has neither.)
- A local maximum is automatically the absolute maximum. (A local maximum is only the highest point nearby; an endpoint or another peak can be higher.)
- After finding critical numbers, the extreme values can be read off without evaluating f. (You must compare the actual f-values at every candidate.)

## Questions

```yaml
- question: "Find the absolute maximum value of f(x) = x³ - 3x on [0, 2]."
  type: multiple-choice
  options: ["-2", "0", "2", "8"]
  answer: 2
  explanation: "f'(x) = 3x² - 3 = 0 gives x = ±1, and only x = 1 lies in [0, 2]. The candidates are f(0) = 0, f(1) = -2 and f(2) = 2. The largest is 2, at the endpoint x = 2. The value -2 is the absolute minimum."

- question: "If f is continuous on [a, b], its absolute maximum on [a, b] must occur at a point where f'(x) = 0."
  type: true-false
  answer: false
  explanation: "The maximum can occur at an endpoint, or at an interior point where f' does not exist. In the previous question the maximum occurs at the endpoint x = 2, where f'(2) = 9 is not zero."

- question: "Give an example of a function on an interval that has no absolute maximum, and say which hypothesis of the Extreme Value Theorem fails."
  type: short-answer
  answer: "f(x) = x on the open interval (0, 1) has no absolute maximum; the interval is not closed."
  explanation: "The values of f get arbitrarily close to 1 but never reach it, because 1 is not in the domain. Other examples: f(x) = 1/x on (0, 1], which is unbounded, or a function with a jump discontinuity on a closed interval."

- question: "What are the candidates for absolute extrema of a continuous function f on [a, b]?"
  type: multiple-choice
  options:
    - "Only the points where f'(x) = 0"
    - "Only the endpoints a and b"
    - "The endpoints and the critical numbers of f in (a, b)"
    - "The inflection points of f"
  answer: 2
  explanation: "By Fermat's theorem, an interior extremum occurs only at a critical number, a point where f' is zero or undefined. The endpoints must be checked separately because Fermat's theorem does not apply there."
```

## Explainer

The first and second derivative tests find local extrema: points that are higher or lower than their immediate neighbors. Many problems ask a different question. What is the very largest or smallest value a function takes over a whole interval? These are the absolute, or global, extrema.

The first issue is whether they exist at all. On the open interval (0, 1), the function f(x) = x gets as close to 1 as you like but never reaches it, so it has no largest value. On [-1, 1], a function with a jump can also miss its highest point. The Extreme Value Theorem rules out these problems: if f is continuous on a closed interval [a, b], then f attains an absolute maximum and an absolute minimum somewhere in [a, b]. Both hypotheses matter. The theorem says the extremes exist; it does not say where they are.

To locate them, use Fermat's theorem: if f has a local extremum at an interior point c and f'(c) exists, then f'(c) = 0. An absolute extremum at an interior point is also a local one, so it must occur at a critical number, where f' is zero or undefined. The only other places to look are the endpoints, which Fermat's theorem does not cover. This gives the closed interval method.

1. Check that f is continuous on [a, b].
2. Find the critical numbers of f in (a, b).
3. Evaluate f at each critical number and at a and b.
4. The largest value is the absolute maximum; the smallest is the absolute minimum.

Example: f(x) = x³ - 3x on [0, 2]. Here f'(x) = 3x² - 3, which is zero at x = 1 and x = -1. Only x = 1 is in the interval. Evaluate: f(0) = 0, f(1) = 1 - 3 = -2 and f(2) = 8 - 6 = 2. The absolute maximum is 2, at x = 2, and the absolute minimum is -2, at x = 1. Notice that the maximum sits at an endpoint where the derivative is not zero.

The method does not require classifying critical numbers as maxima or minima. You compare the f-values directly. That makes it the backbone of optimization problems in which the variable is restricted to a closed interval, such as the side length of a box cut from a fixed sheet.
