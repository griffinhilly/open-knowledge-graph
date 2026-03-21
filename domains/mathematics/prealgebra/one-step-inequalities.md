---
id: one-step-inequalities
title: One-Step Inequalities
domain: mathematics
course: prealgebra
prerequisites:
- id: one-step-equations
  type: hard
- id: integers-and-number-line
  type: hard
- id: comparing-and-ordering-integers
  type: soft
builds-toward:
- solving-inequalities
- compound-inequalities
tags:
- inequalities
- solving
- number-line
- graphing
stage: abstract-reasoning
status: validated
---
# One-Step Inequalities

## Core Idea
An inequality uses symbols (<, >, <=, >=) to show that one expression is less than, greater than, or not equal to another. Solving a one-step inequality uses the same inverse operations as solving a one-step equation, with one critical exception: when you multiply or divide both sides by a negative number, you must reverse the inequality sign. The solution to an inequality is not a single number but a set of numbers, represented on a number line with a ray. For example, x + 3 > 7 gives x > 4, meaning every number greater than 4 is a solution.

## How It's Best Learned
Start by connecting to equations — solve x + 3 = 7 to get x = 4, then ask "what if x + 3 needs to be greater than 7?" Test specific values to verify the solution. Teach number line graphing with open vs. closed circles (strict vs. inclusive). Introduce the sign-flip rule with a concrete example: if 2 < 5, then −2 > −5 (multiplying by −1 reverses the order). Test the sign-flip with substitution.

## Common Misconceptions
- Forgetting to flip the inequality when multiplying or dividing by a negative number.
- Using the wrong type of circle on the number line (open for <= or closed for <).
- Shading the number line in the wrong direction — check by substituting a value from the shaded region.

## Questions

```yaml
- question: "Solve: −4x ≥ 20. What is the correct solution?"
  type: multiple-choice
  options:
    - "x ≥ −5"
    - "x ≤ −5"
    - "x ≥ 5"
    - "x ≤ 5"
  answer: 1
  explanation: "Dividing both sides by −4 requires flipping the inequality sign: ≥ becomes ≤. So −4x ≥ 20 becomes x ≤ −5. Verify: try x = −6 (satisfies x ≤ −5): −4(−6) = 24 ≥ 20 ✓. Try x = −4 (does not satisfy x ≤ −5): −4(−4) = 16 ≥ 20? No ✗. The most common error is forgetting to flip the sign, producing the wrong answer x ≥ −5."

- question: "Which number line graph correctly represents the solution to x + 5 < 9?"
  type: multiple-choice
  options:
    - "Closed circle at 4, shaded to the right"
    - "Open circle at 4, shaded to the right"
    - "Open circle at 4, shaded to the left"
    - "Closed circle at 14, shaded to the left"
  answer: 2
  explanation: "Solving: x + 5 < 9 → x < 4. The solution is all numbers less than 4, which means shading to the left of 4. The inequality is strict (< not ≤), so 4 itself is NOT included — use an open circle. A closed circle would incorrectly include 4; shading to the right would represent x > 4, the opposite of the correct solution."

- question: "When solving an inequality, multiplying both sides by a negative number does not change the direction of the inequality sign."
  type: true-false
  answer: false
  explanation: "Multiplying or dividing both sides by a negative number always reverses the inequality direction. The reason: multiplying by −1 reflects all numbers across zero on the number line, reversing their order. For example, 2 < 5, but multiplying both by −1 gives −2 > −5. Since inequalities describe left-right order on the number line, this reflection flips every 'greater than' to 'less than' and vice versa. This rule has no counterpart in equations and is the single most common error when solving inequalities."

- question: "The solution to an inequality like x − 3 > 7 is a set of infinitely many numbers, not a single value."
  type: true-false
  answer: true
  explanation: "Solving x − 3 > 7 gives x > 10. Every number greater than 10 satisfies this — 10.001, 11, 100, 1,000,000, and infinitely many others. This is a fundamental difference from equations: x − 3 = 7 has exactly one solution (x = 10), while x − 3 > 7 describes an infinite range. The solution is represented as a ray on the number line (starting at an open circle at 10, shading right), not a single point."

- question: "Explain why the inequality sign must reverse when you multiply or divide both sides by a negative number. Use the number line to justify your answer."
  type: short-answer
  answer: "On the number line, multiplying every number by −1 is a reflection across zero: positives become negatives and vice versa. This reflection reverses the ordering of all numbers — what was to the right is now to the left. For example, 3 is to the right of 1 (3 > 1), but after multiplying by −1, −3 is to the left of −1 (−3 < −1). Since inequalities describe this left-right ordering, the reflection flips every 'greater than' into 'less than' and vice versa. Failing to flip produces an inequality satisfied by all the wrong values."
  explanation: "A concrete check reinforces this: start with 2 < 10, multiply both sides by −2: you get −4 and −20. Is −4 < −20? No — −4 > −20. The sign had to flip. Substitution checks like this are the best safeguard against sign-flip errors when solving inequalities."
```

## Explainer

You already know how to solve one-step equations like x + 3 = 7 by applying an inverse operation to both sides: subtract 3 from both sides to get x = 4. Inequalities work almost exactly the same way — the only difference is that instead of one precise answer, you get an entire set of answers, and you use inequality symbols (< less than, > greater than, ≤ less than or equal, ≥ greater than or equal) to describe which values qualify. For x + 3 > 7, subtract 3 from both sides to get x > 4. Every number greater than 4 is a solution — not just 5, but also 4.1, 100, or 1,000,000.

The number line becomes your new best tool for displaying these solution sets. You learned on the integers-and-number-line that numbers increase to the right and decrease to the left. For x > 4, draw a **open circle** at 4 (to show 4 itself is not included) and shade all numbers to the right. For x ≥ 4, use a **closed (filled) circle** to show 4 is included. The open/closed circle distinction corresponds directly to the strict vs. inclusive inequality symbols: < and > exclude the endpoint, ≤ and ≥ include it. If you're ever unsure about the direction of shading, substitute a test value — pick any number from the shaded side and check that it satisfies the original inequality.

There is one critical rule that has no counterpart in equations: **when you multiply or divide both sides by a negative number, the inequality sign flips direction**. Here's the geometric reason. On the number line, multiplying by −1 reflects every point across zero: 2 maps to −2, 5 maps to −5. This reflection reverses the ordering of all numbers. Since 2 < 5 on the original line, after the reflection −2 > −5. Whenever you apply this reflection (by multiplying or dividing by a negative), all the "greater than" relationships become "less than" and vice versa. A concrete example: to solve −3x < 12, divide both sides by −3. Because you're dividing by a negative, flip the sign: x > −4.

You can always verify a solution by substituting a specific number. For x > −4, try x = 0: does −3(0) < 12? Yes, 0 < 12 ✓. Try x = −5: does −3(−5) < 12? That's 15 < 12, which is false ✗. So x = −5 correctly falls outside the solution set x > −4. This substitution check is your safeguard against sign-flip errors and direction-of-shading mistakes — two numbers, one inside and one outside the solution, catch both types of error at once.
