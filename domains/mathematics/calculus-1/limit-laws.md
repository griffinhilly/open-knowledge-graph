---
id: limit-laws
title: Limit Laws
domain: mathematics
course: calculus-1
prerequisites:
  - id: limit-definition-intuitive
    type: hard
builds-toward:
  - continuity-definition
  - squeeze-theorem
  - limits-at-infinity
tags: [limits, laws, computation]
stage: formal-systems
status: validated
---

# Limit Laws

## Core Idea
Limit laws are rules that allow you to compute limits algebraically by breaking complex expressions into simpler pieces. If lim f(x) = L and lim g(x) = M, then lim(f + g) = L + M, lim(f * g) = L * M, lim(f/g) = L/M (when M is not 0), and lim(f^n) = L^n. These laws formalize the intuition that the limit of a combination equals the combination of limits, and they are the workhorse tools for evaluating limits without tables or graphs.

## How It's Best Learned
State each law, verify with examples, then practice applying them to compute limits of polynomial and rational functions. Show that for polynomials, limits can be found by direct substitution (a consequence of the limit laws). Emphasize the cases where the laws do not directly apply (0/0 indeterminate forms).

## Common Misconceptions
- Applying the quotient law when the denominator's limit is zero (this requires further analysis, not the quotient law).
- Assuming all limit laws hold for infinite limits (some do, some produce indeterminate forms).
- Believing limit laws are definitions rather than consequences of the precise limit definition.

## Explainer

When you first learned about limits, you built intuition: the limit of f(x) as x → a is the value f(x) approaches as x gets close to a. That intuition is powerful but it leaves a practical question unanswered: how do you actually *compute* a limit for a complicated expression? **Limit laws** answer this by giving you a toolkit for breaking a complex limit into smaller, manageable pieces — much like order of operations lets you evaluate arithmetic by breaking it into steps.

The core laws say that limits distribute across the basic operations. If lim f(x) = L and lim g(x) = M (as x → a), then: the limit of f + g is L + M, the limit of f · g is L · M, and the limit of f/g is L/M — provided M ≠ 0. There is also a power law: the limit of [f(x)]ⁿ is Lⁿ. These are not definitions or conventions; they are theorems that follow from the precise epsilon-delta definition of a limit. The idea behind each law is the same: if you can get f as close to L as you like, and g as close to M as you like, then their sum (or product) gets as close to L + M (or L · M) as you like.

The most immediate application is **direct substitution for polynomials**. Every polynomial p(x) satisfies lim_{x→a} p(x) = p(a). Why? Because a polynomial is just sums and products of constants and powers of x, and by the limit laws, you can push the limit through every sum and product until you are evaluating limits of the form lim x = a and lim c = c — both of which are obvious from the definition. This makes evaluating polynomial limits trivial: just plug in. Rational functions work the same way whenever the denominator is not zero at the point.

The limit laws break down at exactly one point: the **quotient law fails when M = 0**. If lim g(x) = 0, you cannot conclude anything from L/M because division by zero is undefined — and the limiting behavior can be anything: the limit might be finite (0/0 indeterminate form requiring algebraic simplification), infinite (one-sided vertical asymptote), or genuinely nonexistent. This is the boundary where limit laws end and more specialized techniques — factoring and canceling, L'Hôpital's rule, conjugate multiplication — take over. Recognizing when you are in the 0/0 or ∞/∞ regime, and knowing that the limit laws alone cannot resolve it, is as important as knowing what the laws do say.
