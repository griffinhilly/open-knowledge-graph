---
id: solving-rational-equations
title: Solving Rational Equations
domain: mathematics
course: algebra-2
prerequisites:
- id: rational-functions-and-asymptotes
  type: hard
- id: solving-quadratics-by-factoring
  type: hard
- id: graphing-rational-functions
  type: soft
- id: solving-radical-equations
  type: soft
builds-toward: []
tags:
- rational-equations
- LCD
- extraneous-solutions
stage: abstract-reasoning
status: validated
---
# Solving Rational Equations

## Core Idea
A rational equation contains one or more rational expressions. To solve: (1) find the LCD of all denominators, (2) multiply both sides by the LCD to clear fractions, (3) solve the resulting polynomial equation, (4) check for extraneous solutions (values that make any original denominator zero). Extraneous solutions are common because multiplying by an expression containing the variable can introduce them.

## How It's Best Learned
Start with simple equations (one fraction equals another). Progress to equations with three or more terms requiring an LCD. Emphasize identifying domain restrictions before solving. Always check solutions against the original equation. Connect to work/rate problems and mixture problems for applications.

## Common Misconceptions
- Forgetting to check for extraneous solutions (the most critical step).
- Finding the LCD incorrectly.
- Only multiplying some terms by the LCD instead of every term.
- Confusing solving rational equations (clear fractions, find x) with simplifying rational expressions (combine, but no equation to solve).

## Explainer

A **rational equation** is an equation that contains at least one fraction with a variable in the denominator, like 2/(x−3) + 1/x = 5/6. You know from your study of rational functions that the denominator cannot equal zero — that is where the function is undefined, where asymptotes or holes appear on the graph. Before you do anything else with a rational equation, identify the **domain restrictions**: every value of x that makes any denominator zero is automatically excluded from consideration. Write them down first and keep them visible.

The core strategy is to eliminate the fractions entirely by multiplying every term on both sides by the **LCD** (least common denominator) of all the denominators in the equation. If the denominators are x, (x−3), and 6, the LCD is 6x(x−3). Multiply every single term by 6x(x−3) and each fraction simplifies: the numerator remains, the denominator cancels. What you are left with is a polynomial equation — and at this point you can use all your quadratic-solving and factoring skills to find the solutions.

The dangerous consequence of this strategy is **extraneous solutions**. When you multiply both sides by an expression involving x, you are technically multiplying by zero when x equals a domain restriction. Multiplying both sides of an equation by zero is not a reversible step — it can create a "solution" that satisfies your simplified equation but not the original one. This is not a rare edge case; many textbook problems are deliberately constructed so that the algebraic work yields a root that is one of the excluded values. Always substitute every candidate solution back into the original equation. If plugging in x = 3 causes a division by zero anywhere, discard it as extraneous.

The same factoring skills you used to solve quadratics by factoring reappear here. After clearing fractions you often get a quadratic (or higher-degree polynomial) that requires factoring or the quadratic formula. The pattern is: identify restrictions → find LCD → multiply through → factor/solve → check every answer. This framework generalizes: radical equations (from your other prerequisite) follow the same check-for-extraneous logic, because squaring both sides is also an irreversible algebraic step that can introduce false solutions. In both cases, the algebra may produce results that are algebraically consistent but geometrically impossible, and only substitution back into the original equation reveals the truth.
