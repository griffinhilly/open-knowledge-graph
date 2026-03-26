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
stage: formal-systems
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

## Questions

```yaml
- question: "A student solves x/(x−2) = 2/(x−2) by multiplying both sides by (x−2), arriving at x = 2. What is the correct solution set?"
  type: multiple-choice
  options:
    - "{2} — x = 2 satisfies the simplified equation, so it is valid"
    - "All real numbers — the equation simplifies to a tautology"
    - "No solution — x = 2 makes both denominators zero and is excluded from the domain"
    - "The equation cannot be solved by this method"
  answer: 2
  explanation: "Multiplying both sides by (x−2) is only valid when x ≠ 2. The 'solution' x = 2 makes both original denominators zero — it is an extraneous solution produced by multiplying by zero. Since x = 2 is the only candidate and it is excluded from the domain, the equation has no solution. This is the most important check in solving rational equations."

- question: "Solving 1/(x+3) + 1/(x−3) = 2/(x²−9) yields x = ±3 after clearing fractions. A student reports both as solutions. What error did the student make?"
  type: multiple-choice
  options:
    - "The student used the wrong LCD; the correct LCD produces different solutions"
    - "No error — both ±3 satisfy the polynomial equation obtained after clearing fractions"
    - "Both x = 3 and x = −3 are extraneous; they make the original denominators zero"
    - "Only x = 3 is extraneous; x = −3 is a valid solution"
  answer: 2
  explanation: "x = 3 makes (x−3) = 0, and x = −3 makes (x+3) = 0; both also make x²−9 = 0. These are extraneous solutions — they appear because multiplying both sides by (x²−9) is invalid when x²−9 = 0. The polynomial equation may accept these values, but the original rational equation is undefined there. The equation has no solution."

- question: "An extraneous solution to a rational equation may satisfy the polynomial equation obtained after clearing fractions, yet be rejected as a solution to the original equation."
  type: true-false
  answer: true
  explanation: "Clearing fractions by multiplying by the LCD is only reversible when the LCD is nonzero. If a candidate solution makes the LCD equal zero, the multiplication step was invalid at that point — it was equivalent to multiplying by zero, which can create false solutions. The polynomial equation may produce that value as a root, but the original rational equation is undefined there, so it must be rejected."

- question: "Extraneous solutions to rational equations can generally be identified because they are negative numbers or zero."
  type: true-false
  answer: false
  explanation: "Extraneous solutions are not identified by their sign or magnitude. A solution is extraneous if and only if it makes at least one denominator in the original equation equal to zero. An extraneous solution can be any real number — positive, negative, or zero. The only reliable identification method is to substitute every candidate solution back into the original (unmodified) equation and check that it is defined and balanced."

- question: "Why can clearing fractions in a rational equation produce extraneous solutions, and what is the only reliable method to identify them?"
  type: short-answer
  answer: "Clearing fractions requires multiplying both sides by the LCD. If the LCD contains the variable, this step is only valid when the LCD is nonzero. A candidate solution that makes the LCD zero corresponds to a step where both sides were multiplied by zero — an irreversible operation that can introduce false solutions. The only reliable method is to substitute every candidate solution back into the original equation. Any value that makes a denominator zero, or that fails to balance the equation, must be rejected as extraneous."
  explanation: "The parallel with radical equations is useful: squaring both sides to clear a square root is also irreversible and also produces extraneous solutions. In both cases, the algebra can yield results that satisfy the transformed equation but not the original. Substitution back into the original is the universal check."
```

## Explainer

A **rational equation** is an equation that contains at least one fraction with a variable in the denominator, like 2/(x−3) + 1/x = 5/6. You know from your study of rational functions that the denominator cannot equal zero — that is where the function is undefined, where asymptotes or holes appear on the graph. Before you do anything else with a rational equation, identify the **domain restrictions**: every value of x that makes any denominator zero is automatically excluded from consideration. Write them down first and keep them visible.

The core strategy is to eliminate the fractions entirely by multiplying every term on both sides by the **LCD** (least common denominator) of all the denominators in the equation. If the denominators are x, (x−3), and 6, the LCD is 6x(x−3). Multiply every single term by 6x(x−3) and each fraction simplifies: the numerator remains, the denominator cancels. What you are left with is a polynomial equation — and at this point you can use all your quadratic-solving and factoring skills to find the solutions.

The dangerous consequence of this strategy is **extraneous solutions**. When you multiply both sides by an expression involving x, you are technically multiplying by zero when x equals a domain restriction. Multiplying both sides of an equation by zero is not a reversible step — it can create a "solution" that satisfies your simplified equation but not the original one. This is not a rare edge case; many textbook problems are deliberately constructed so that the algebraic work yields a root that is one of the excluded values. Always substitute every candidate solution back into the original equation. If plugging in x = 3 causes a division by zero anywhere, discard it as extraneous.

The same factoring skills you used to solve quadratics by factoring reappear here. After clearing fractions you often get a quadratic (or higher-degree polynomial) that requires factoring or the quadratic formula. The pattern is: identify restrictions → find LCD → multiply through → factor/solve → check every answer. This framework generalizes: radical equations (from your other prerequisite) follow the same check-for-extraneous logic, because squaring both sides is also an irreversible algebraic step that can introduce false solutions. In both cases, the algebra may produce results that are algebraically consistent but geometrically impossible, and only substitution back into the original equation reveals the truth.
