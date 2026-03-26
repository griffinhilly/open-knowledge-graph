---
id: solving-inequalities
title: Solving Multi-Step Inequalities
domain: mathematics
course: algebra-1
prerequisites:
  - id: one-step-inequalities
    type: hard
  - id: solving-multi-step-equations
    type: hard
builds-toward:
  - compound-inequalities
  - absolute-value-inequalities
  - systems-of-inequalities
tags: [inequalities, solving, graphing, number-line]
stage: abstract-reasoning
status: validated
---

# Solving Multi-Step Inequalities

## Core Idea
Multi-step inequalities are solved using the same techniques as multi-step equations — distribute, combine like terms, use inverse operations — with the added rule that multiplying or dividing both sides by a negative number reverses the inequality sign. The solution is a range of values, graphed on a number line with open or closed circles and shading. For example, −3x + 7 > 1 becomes −3x > −6, then x < 2 (sign flipped because of division by −3). Inequalities model real-world constraints: budgets, speed limits, minimum requirements.

## How It's Best Learned
Solve the corresponding equation first to find the boundary value, then determine the direction of the inequality by testing a point. This reinforces the equation-inequality connection. Practice the sign-flip rule extensively with dedicated exercises. Graph every solution on a number line and verify by substituting a value from the solution region into the original inequality.

## Common Misconceptions
- Forgetting to flip the inequality when multiplying or dividing by a negative (the most common error in all of inequality solving).
- Confusing open and closed circles (open for strict <, >, closed for <=, >=).
- Thinking the solution must be a single number rather than a range.

## Questions

```yaml
- question: "A student solves −2x > 8 and gets x > −4. What error did the student make?"
  type: multiple-choice
  options:
    - "The student moved the constant to the wrong side"
    - "The student divided both sides by −2 but forgot to flip the inequality sign, so the correct answer is x < −4"
    - "The student made an arithmetic error; the correct answer is x > −16"
    - "No error — x > −4 is the correct solution"
  answer: 1
  explanation: "Dividing both sides by −2 requires flipping the inequality: −2x > 8 becomes x < −4 (not x > −4). The sign reversal happens because dividing by a negative flips the number line ordering — what was greater becomes lesser. The student correctly performed the division but forgot the sign flip, which is the most common error in inequality solving."

- question: "Solve −3x + 7 > 1. Which of the following is the correct solution?"
  type: multiple-choice
  options:
    - "x > 2"
    - "x < 2"
    - "x > −2"
    - "x < −2"
  answer: 1
  explanation: "Subtract 7 from both sides: −3x > −6. Divide both sides by −3 — and flip the sign: x < 2. The flip occurs because we divided by a negative number. Verify: x = 0 gives −3(0) + 7 = 7 > 1 ✓ (0 is in the solution set x < 2). x = 3 gives −3(3) + 7 = −2, and −2 > 1 is false ✓ (3 is correctly excluded)."

- question: "The solution to a linear inequality with one variable is always a range of values (an interval on the number line), never a single number."
  type: true-false
  answer: true
  explanation: "An inequality like x < 2 describes infinitely many values — all real numbers less than 2. Unlike an equation (which has a single solution point), an inequality defines a region. Graphically, this is represented with shading extending in one direction from a boundary value. Thinking the answer 'should be a number' is a common error that comes from confusing inequalities with equations."

- question: "You should flip the inequality sign whenever you subtract a positive number from both sides of an inequality."
  type: true-false
  answer: false
  explanation: "The sign only flips when you multiply or divide both sides by a negative number. Adding or subtracting any number (positive or negative) from both sides preserves the direction of the inequality. For example, x + 3 > 7 → x > 4 (subtracting 3, no flip). Only multiplication and division by negatives cause the flip, because they reverse the ordering relationship on the number line."

- question: "Explain why multiplying or dividing both sides of an inequality by a negative number reverses the inequality sign. Use a numeric example to illustrate."
  type: short-answer
  answer: "Multiplying by a negative flips the number line — larger numbers become smaller and vice versa. Example: 3 > 1 is true. Multiply both sides by −1: −3 and −1. Now −3 < −1, so the relationship reverses. The same logic applies when solving: dividing by −3 flips every comparison."
  explanation: "The flip is not an arbitrary rule — it follows directly from how negative numbers reorder the number line. Positive multiplication preserves order (if a > b and c > 0, then ac > bc). Negative multiplication reverses it (if a > b and c < 0, then ac < bc). Understanding the reason makes the rule memorable and prevents forgetting it under exam pressure."
```

## Explainer

Solving a multi-step inequality is almost identical to solving a multi-step equation — you isolate the variable using the same inverse-operation strategy you learned with equations. The key insight is that an inequality doesn't give you a single answer; it describes an entire region of values that satisfy a condition. Think of it as asking: "For which values of x is this statement true?" The answer is always an interval or ray on the number line, not just one point.

The mechanics mirror equation-solving closely. Take −3x + 7 > 1. Subtract 7 from both sides: −3x > −6. Now divide both sides by −3 — and here is the one new rule. **Dividing or multiplying both sides of an inequality by a negative number reverses the direction of the inequality sign.** This happens because multiplying by −1 flips the number line: what was larger becomes smaller. So −3x > −6 becomes x < 2. The inequality flipped from > to <.

Why does the flip happen? Imagine the true inequality 3 > 1. Multiply both sides by −1 and you get −3 and −1. On the number line, −3 is to the *left* of −1, meaning −3 < −1. The relationship reversed. This same logic applies whenever a negative factor appears. A reliable strategy: solve the corresponding equation first to find the **boundary value** (x = 2 here), then test one point on each side to determine which region satisfies the original inequality.

The solution x < 2 is graphed on a number line with an open circle at 2 (the boundary is not included because the inequality is strict) and shading extending to the left. Had the inequality been ≤ instead of <, the circle would be closed. This graphical representation communicates the full solution set at a glance. Verify your answer: pick x = 0 (inside the solution region): −3(0) + 7 = 7 > 1 ✓. Pick x = 3 (outside): −3(3) + 7 = −2, and −2 > 1 is false ✓. Both checks confirm the solution.
