---
id: solving-absolute-value-equations-review
title: Solving Absolute Value Equations Review
domain: mathematics
course: algebra-2
prerequisites:
  - id: absolute-value
    type: hard
  - id: equations-variables-both-sides
    type: hard
builds-toward:
  - quadratic-inequalities
tags: [absolute-value, equations, review]
stage: abstract-reasoning
status: validated
---

# Solving Absolute Value Equations Review

## Core Idea
An absolute value equation |f(x)| = c (where c >= 0) is solved by considering two cases: f(x) = c or f(x) = -c. If c < 0, there is no solution. For equations like |f(x)| = |g(x)|, solve f(x) = g(x) and f(x) = -g(x). This review reinforces the case-splitting technique and prepares students for more complex equations and inequalities in Algebra 2.

## How It's Best Learned
Revisit the definition of absolute value as distance from zero. Solve progressively harder equations: |x| = 5, |2x - 3| = 7, |x + 1| = |3x - 5|. Always check solutions in the original equation. Graph y = |f(x)| and y = c to visualize solutions as intersection points.

## Common Misconceptions
- Forgetting the negative case (only solving f(x) = c and missing f(x) = -c).
- Not checking for extraneous solutions, especially when the equation has been manipulated.
- Thinking |x| = -3 has solutions (absolute value is never negative).

## Questions

```yaml
- question: "Solve |2x + 4| = 6. Which answer correctly identifies ALL solutions?"
  type: multiple-choice
  options:
    - "x = 1 only — solving 2x + 4 = 6"
    - "x = 1 and x = −5 — solving both 2x + 4 = 6 and 2x + 4 = −6"
    - "x = −5 only — since the expression must be negative inside the bars"
    - "No solution — the right side must first be rewritten before splitting"
  answer: 1
  explanation: "Case-splitting gives two equations: 2x + 4 = 6 → x = 1, and 2x + 4 = −6 → x = −5. Both satisfy the original equation when checked. The most common error is solving only the positive case and missing x = −5 entirely."

- question: "A student encounters |3x − 1| = −4. What is the correct conclusion?"
  type: multiple-choice
  options:
    - "x = −1 (solving 3x − 1 = −4)"
    - "x = 5/3 and x = −1 (splitting into both cases)"
    - "There is no solution because an absolute value cannot equal a negative number"
    - "x = 5/3 (solving 3x − 1 = 4)"
  answer: 2
  explanation: "Absolute value is always non-negative, so |3x − 1| ≥ 0 for every real x. The equation |3x − 1| = −4 asks when a non-negative quantity equals a negative number — which is never. Stop immediately when c < 0; no case-splitting is needed."

- question: "The equation |x − 5| = 3 has exactly one solution, x = 8."
  type: true-false
  answer: false
  explanation: "Case-splitting gives two equations: x − 5 = 3 → x = 8, and x − 5 = −3 → x = 2. Both values satisfy |x − 5| = 3. Forgetting the negative case is the single most common error in absolute value equations — it always produces two solutions (when c > 0) unless the two cases coincidentally give the same answer."

- question: "When solving |f(x)| = |g(x)|, the correct approach is to set up two cases: f(x) = g(x) and f(x) = −g(x)."
  type: true-false
  answer: true
  explanation: "Two expressions have equal absolute values when they are equal or when they are opposites — exactly these two cases. This is the natural extension of the single-sided case: |expression| = c becomes expression = c or expression = −c, and when both sides have absolute values, the same logic applies to the relationship between f(x) and g(x)."

- question: "Why is it necessary to check solutions back in the original absolute value equation, and what type of error are you guarding against?"
  type: short-answer
  answer: "Checking guards against extraneous solutions — values that satisfy an algebraically manipulated form of the equation but not the original. Extraneous solutions can arise from operations like squaring both sides (sometimes used as an alternative method), which can introduce values that weren't present in the original. Substituting each candidate solution back into |f(x)| = c and verifying the equation holds is the only reliable way to confirm every solution is genuine."
  explanation: "Absolute value equations are one of the few contexts where algebraically correct steps can introduce spurious answers. The habit of checking solutions — fast and reliable — becomes even more critical when moving to absolute value inequalities, where forgetting to verify can silently produce an incorrect solution set."
```

## Explainer

You already know that **absolute value** measures distance from zero on the number line: |x| is always non-negative, regardless of the sign of x. Solving an absolute value equation asks a geometric question: for which values of x is the expression inside the absolute value bars exactly a certain distance from zero? The answer requires thinking in two directions. If |f(x)| = 5, then f(x) must be exactly 5 away from zero — either f(x) = 5 (positive direction) or f(x) = −5 (negative direction). This is the **case-splitting** technique, and it is the engine of every absolute value equation.

The systematic approach is: when you see |f(x)| = c, first check whether c is negative. If c < 0, stop immediately — absolute value is always non-negative, so the equation has no solutions. If c ≥ 0, write two separate equations: f(x) = c and f(x) = −c, then solve each using the equation-solving skills you already have (moving variables to one side, combining like terms, etc.). For example, |2x − 3| = 7 splits into 2x − 3 = 7, giving x = 5, and 2x − 3 = −7, giving x = −2. Both are valid solutions.

When both sides of the equation contain absolute values — like |f(x)| = |g(x)| — the same logic applies: either f(x) = g(x) or f(x) = −g(x). Two expressions have the same absolute value exactly when they are either equal or opposites. These equations typically produce up to two solutions and the algebra is straightforward once you recognize the two cases.

Always **check your solutions** in the original equation. Absolute value equations are one of the few places in algebra where algebraically derived solutions can turn out to be extraneous — not because you made an error, but because some algebraic manipulations (especially squaring both sides, if you use that approach) can introduce values that satisfy the manipulated equation but not the original. Substituting back into |f(x)| = c and verifying is fast and catches every spurious answer. This checking habit becomes even more critical when you move to absolute value inequalities, where the logic shifts from "exactly this distance from zero" to "closer than" or "farther than," and where forgetting the negative case entirely changes the solution set.
