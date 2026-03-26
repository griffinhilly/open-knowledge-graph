---
id: factoring-completely
title: Factoring Completely
domain: mathematics
course: algebra-1
prerequisites:
  - id: factoring-gcf
    type: hard
  - id: factoring-trinomials
    type: hard
  - id: factoring-difference-of-squares
    type: hard
builds-toward:
  - solving-quadratics-by-factoring
  - rational-expressions-intro
tags: [factoring, complete, multi-step, polynomials]
stage: abstract-reasoning
status: validated
---

# Factoring Completely

## Core Idea
Factoring completely means writing a polynomial as a product of prime (unfactorable) factors. It often requires multiple steps: first factor out the GCF, then apply trinomial factoring or special patterns to what remains. For example, 3x³ − 12x = 3x(x² − 4) = 3x(x + 2)(x − 2). The process stops when no factor can be factored further. This is the culminating factoring skill — it integrates GCF, trinomials, difference of squares, and factor-by-grouping into a unified strategy. Solving quadratic equations by factoring requires the polynomial to be factored completely.

## How It's Best Learned
Teach a systematic decision tree: (1) Factor out the GCF first, always. (2) Count the terms — two terms: check for difference of squares or sum/difference of cubes; three terms: try trinomial factoring; four terms: try grouping. (3) Check each factor to see if it can be factored further. Practice with multi-step problems that require two or three techniques in sequence. Always verify by multiplying the factors back together.

## Common Misconceptions
- Skipping the GCF step and jumping to trinomial factoring (making the problem harder).
- Stopping too early (e.g., factoring 2x² − 8 as 2(x² − 4) but not continuing to 2(x + 2)(x − 2)).
- Not recognizing factor-by-grouping patterns in four-term expressions.

## Questions

```yaml
- question: "A student factors 4x³ − 16x and writes 4x(x² − 4), then stops. Which statement best describes this work?"
  type: multiple-choice
  options:
    - "It is fully factored — the polynomial is written as a product of simpler expressions"
    - "It is incorrect — the GCF should have been 2x, not 4x"
    - "It is incomplete — (x² − 4) is a difference of squares that can be factored further into (x + 2)(x − 2)"
    - "It is incomplete — the GCF was not factored out before the trinomial step"
  answer: 2
  explanation: "This is the classic 'stopping too early' error. 4x(x² − 4) is partially factored — the GCF was correctly identified and removed. But x² − 4 is a difference of squares: a² − b² = (a + b)(a − b), so x² − 4 = (x + 2)(x − 2). The fully factored form is 4x(x + 2)(x − 2). A polynomial is only factored completely when no individual factor can be factored further — you must check every factor at every step."

- question: "Which of the following expressions is fully factored?"
  type: multiple-choice
  options:
    - "3x(x² − 9)"
    - "(x + 3)(x² − 9)"
    - "3x(x + 3)(x − 3)"
    - "3x³ − 27x"
  answer: 2
  explanation: "Option C, 3x(x + 3)(x − 3), is the only fully factored form. Starting from 3x³ − 27x: factor out the GCF of 3x to get 3x(x² − 9). Then x² − 9 is a difference of squares that factors into (x + 3)(x − 3). Option A still has x² − 9 unfactored. Option B has (x² − 9) unfactored and the GCF wasn't addressed. Option D is the original unfactored expression."

- question: "When factoring a polynomial largely, you primarily need to check whether each resulting factor can be factored further if the original polynomial has four or more terms."
  type: true-false
  answer: false
  explanation: "You must inspect every factor at every step regardless of the original polynomial's term count. A two-term polynomial like 2x² − 8 first yields 2(x² − 4) after the GCF step, but x² − 4 is still a difference of squares that must be factored to (x + 2)(x − 2). The check 'can this factor be factored further?' applies universally — the number of terms in the original polynomial is irrelevant once you are past the initial step."

- question: "Factoring out the GCF as the first step in factoring completely typically simplifies the remaining factoring task."
  type: true-false
  answer: true
  explanation: "The GCF step is not just convention — it actively reduces the complexity of what follows. If you have 6x³ − 24x and skip the GCF, you face a cubic with no obvious pattern. Factor out 6x first and you get 6x(x² − 4) — a recognizable difference of squares. Similarly, pulling out a numeric GCF (like 3) can transform a trinomial with a large leading coefficient into one with leading coefficient 1, making the trinomial factoring step straightforward. GCF first is a strategic simplification, not a formality."

- question: "Explain why the strategy for factoring completely always begins with the GCF step, even when the GCF is just a number like 2 or 3. What would happen if you skipped this step?"
  type: short-answer
  answer: "Factoring out the GCF first reduces the degree and size of coefficients in the remaining expression, making subsequent steps much easier. If the GCF is a monomial like 3x, pulling it out converts a cubic into a quadratic; if it's just a number like 2, it simplifies the coefficients. Skipping the GCF forces you to work with larger, more complex expressions. For example, 2x² − 8 without the GCF step requires recognizing 2x² − 8 directly as a pattern, which is harder. After factoring out 2, you see x² − 4 — immediately a difference of squares. More importantly, skipping the GCF can hide the complete factored form entirely: you might successfully factor x² − 4 into (x + 2)(x − 2) but miss the factor of 2, leaving your answer incomplete."
  explanation: "The GCF step is strategic, not ceremonial. It applies to every polynomial (the GCF might be 1, in which case no simplification occurs, but you've confirmed that). Teaching GCF-first as a discipline prevents the most common factoring errors: working with unnecessarily large coefficients and leaving the GCF hidden inside a factor."
```

## Explainer

Factoring completely is what happens when all your individual factoring tools — GCF, trinomials, difference of squares — get combined into a single, disciplined process. The goal is to write a polynomial as a product where no individual factor can be broken down any further. Think of it like reducing a fraction to lowest terms: you are not done until every piece is truly irreducible.

The strategy always begins the same way: **factor out the greatest common factor (GCF) first**. This is not optional, and it is not a stylistic choice — it simplifies everything that follows. Suppose you have 3x³ − 12x. If you ignore the GCF and try to factor x³ − 4x directly, you face a cubic with no obvious pattern. But factoring out 3x first gives 3x(x² − 4), and now x² − 4 is a recognizable **difference of squares**: (x + 2)(x − 2). The full factored form is 3x(x + 2)(x − 2). Pulling the GCF first transforms a hard problem into an easier one.

After the GCF step, the number of remaining terms tells you what to try next. **Two terms**: look for a difference of squares (a² − b² = (a + b)(a − b)). **Three terms**: try trinomial factoring — find two numbers that multiply to the constant term and add to the middle coefficient (or use the ac-method when the leading coefficient is not 1). **Four terms**: try factor-by-grouping — split into two pairs, factor each pair, then factor out the common binomial. After each step, inspect every factor and ask: can this be factored further? A difference of squares inside a factor needs another application of the rule. A trinomial hiding inside a factor needs to be addressed before you stop.

The check is always the same: multiply your factors back together and verify you recover the original polynomial. This is not busywork — it catches errors from sign mistakes and missed steps, and it builds fluency with the distributive property in reverse. Factoring completely matters because many downstream skills depend on it: solving quadratic (and higher-degree) equations by setting factors equal to zero only works when the polynomial is fully factored; simplifying rational expressions requires you to cancel common factors; and finding zeros of polynomials is the foundation of graphing. The discipline of checking every factor and never stopping early is a habit that pays dividends throughout algebra.
