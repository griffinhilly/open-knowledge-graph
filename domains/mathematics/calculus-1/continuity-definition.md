---
id: continuity-definition
title: Continuity Definition
domain: mathematics
course: calculus-1
prerequisites:
- id: limit-definition-intuitive
  type: hard
- id: one-sided-limits
  type: hard
- id: limit-laws
  type: soft
- id: piecewise-functions-graphing
  type: soft
builds-toward:
- intermediate-value-theorem
- limit-definition-of-derivative
tags:
- continuity
- limits
- functions
stage: formal-systems
status: validated
---
# Continuity Definition

## Core Idea
A function f is continuous at x = a if three conditions hold: f(a) is defined, lim(x->a) f(x) exists, and lim(x->a) f(x) = f(a). Informally, the graph has no break, jump, or hole at a. Continuity is important because continuous functions behave predictably: they satisfy the Intermediate Value Theorem, and most derivative and integral theorems require continuity.

## How It's Best Learned
Classify discontinuities as removable (hole), jump, or infinite (vertical asymptote) with examples of each. Practice checking the three conditions at specific points. Identify which standard functions are continuous on their domains (polynomials, rationals, trig, exponentials, logarithms).

## Common Misconceptions
- Believing a function is continuous just because it is defined at a (the limit must also match).
- Thinking continuity requires a formula (piecewise functions can be continuous).
- Assuming discontinuities are always obvious from the formula.

## Questions

```yaml
- question: "Define f(x) = (x²-4)/(x-2) for x ≠ 2, and f(2) = 5. What type of discontinuity does f have at x = 2?"
  type: multiple-choice
  options:
    - "Jump discontinuity"
    - "Infinite discontinuity"
    - "Removable discontinuity"
    - "None — f is continuous at x = 2"
  answer: 2
  explanation: "Factor: (x²-4)/(x-2) = (x+2)(x-2)/(x-2) = x+2 for x ≠ 2. So lim(x→2) f(x) = 4, which exists. But f(2) = 5 ≠ 4 — condition 3 fails. This is a removable discontinuity (a displaced point). If f(2) were redefined as 4, the discontinuity would be removed."

- question: "A function that is defined at every real number must be continuous at every real number."
  type: true-false
  answer: false
  explanation: "Being defined everywhere satisfies only condition 1. The limit must also exist (condition 2) and equal the function value (condition 3). For example, f(x) = 0 for x ≠ 0 and f(0) = 1 is defined everywhere, but at x = 0 the limit is 0 while f(0) = 1 — condition 3 fails, so f is discontinuous at 0."

- question: "State the three conditions for continuity at x = a, and describe geometrically what each one rules out."
  type: short-answer
  answer: "(1) f(a) is defined — rules out a hole (missing point). (2) lim(x→a) f(x) exists — rules out a jump (left and right limits disagree). (3) The limit equals f(a) — rules out a displaced point (limit exists but the function value is shifted away from it)."
  explanation: "Each condition targets exactly one type of discontinuity. Together they guarantee the graph passes through (a, f(a)) smoothly with no break of any kind. Violating exactly one condition identifies the discontinuity type precisely."
```

## Explainer

From your work with limits, you know that lim(x→a) f(x) describes what a function approaches near x = a — not necessarily what it equals there. Continuity is the formal condition that forces these two things to agree. Informally, a function is continuous at a point if you can draw its graph through that point without lifting your pencil. The formal definition makes "without lifting" precise.

There are exactly three conditions, and all three must hold simultaneously. First, f(a) must be defined — the function has an actual value at the point (no hole). Second, lim(x→a) f(x) must exist — the one-sided limits from the left and right agree on a single value (no jump). Third, that limit value must equal f(a) — the height the graph approaches must be exactly where the graph sits at the point (no displaced isolated point). Each condition rules out one distinct type of failure.

The corresponding discontinuity types map directly onto failed conditions. A removable discontinuity (a "hole") violates condition 1 or condition 3: either the function is undefined at a, or it is defined but at the wrong height. A jump discontinuity violates condition 2: the function approaches different values from the left and right. An infinite discontinuity also violates condition 2: the limit does not exist because the function blows up toward ±∞ near a vertical asymptote. Identifying which condition fails tells you which type of discontinuity you have.

The most important misconception to resist is thinking that "f(a) is defined" is sufficient for continuity. Many students see a formula that produces a value and assume continuity — but piecewise functions routinely have a well-defined value at a joining point while the surrounding pieces approach a completely different height. Always check all three conditions, not just the first.

Continuity matters throughout calculus because most theorems require it as a hypothesis. The Intermediate Value Theorem guarantees that a continuous function on [a, b] hits every value between f(a) and f(b) — this fails for functions with jumps. Differentiability requires continuity as a necessary condition. The Fundamental Theorem of Calculus assumes continuous integrands. Learning the precise three-condition definition now means you will understand why theorems are stated the way they are, not just how to apply them.
