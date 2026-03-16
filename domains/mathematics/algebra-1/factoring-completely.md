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

## Explainer

Factoring completely is what happens when all your individual factoring tools — GCF, trinomials, difference of squares — get combined into a single, disciplined process. The goal is to write a polynomial as a product where no individual factor can be broken down any further. Think of it like reducing a fraction to lowest terms: you are not done until every piece is truly irreducible.

The strategy always begins the same way: **factor out the greatest common factor (GCF) first**. This is not optional, and it is not a stylistic choice — it simplifies everything that follows. Suppose you have 3x³ − 12x. If you ignore the GCF and try to factor x³ − 4x directly, you face a cubic with no obvious pattern. But factoring out 3x first gives 3x(x² − 4), and now x² − 4 is a recognizable **difference of squares**: (x + 2)(x − 2). The full factored form is 3x(x + 2)(x − 2). Pulling the GCF first transforms a hard problem into an easier one.

After the GCF step, the number of remaining terms tells you what to try next. **Two terms**: look for a difference of squares (a² − b² = (a + b)(a − b)). **Three terms**: try trinomial factoring — find two numbers that multiply to the constant term and add to the middle coefficient (or use the ac-method when the leading coefficient is not 1). **Four terms**: try factor-by-grouping — split into two pairs, factor each pair, then factor out the common binomial. After each step, inspect every factor and ask: can this be factored further? A difference of squares inside a factor needs another application of the rule. A trinomial hiding inside a factor needs to be addressed before you stop.

The check is always the same: multiply your factors back together and verify you recover the original polynomial. This is not busywork — it catches errors from sign mistakes and missed steps, and it builds fluency with the distributive property in reverse. Factoring completely matters because many downstream skills depend on it: solving quadratic (and higher-degree) equations by setting factors equal to zero only works when the polynomial is fully factored; simplifying rational expressions requires you to cancel common factors; and finding zeros of polynomials is the foundation of graphing. The discipline of checking every factor and never stopping early is a habit that pays dividends throughout algebra.
