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

## Explainer

You already know that **absolute value** measures distance from zero on the number line: |x| is always non-negative, regardless of the sign of x. Solving an absolute value equation asks a geometric question: for which values of x is the expression inside the absolute value bars exactly a certain distance from zero? The answer requires thinking in two directions. If |f(x)| = 5, then f(x) must be exactly 5 away from zero — either f(x) = 5 (positive direction) or f(x) = −5 (negative direction). This is the **case-splitting** technique, and it is the engine of every absolute value equation.

The systematic approach is: when you see |f(x)| = c, first check whether c is negative. If c < 0, stop immediately — absolute value is always non-negative, so the equation has no solutions. If c ≥ 0, write two separate equations: f(x) = c and f(x) = −c, then solve each using the equation-solving skills you already have (moving variables to one side, combining like terms, etc.). For example, |2x − 3| = 7 splits into 2x − 3 = 7, giving x = 5, and 2x − 3 = −7, giving x = −2. Both are valid solutions.

When both sides of the equation contain absolute values — like |f(x)| = |g(x)| — the same logic applies: either f(x) = g(x) or f(x) = −g(x). Two expressions have the same absolute value exactly when they are either equal or opposites. These equations typically produce up to two solutions and the algebra is straightforward once you recognize the two cases.

Always **check your solutions** in the original equation. Absolute value equations are one of the few places in algebra where algebraically derived solutions can turn out to be extraneous — not because you made an error, but because some algebraic manipulations (especially squaring both sides, if you use that approach) can introduce values that satisfy the manipulated equation but not the original. Substituting back into |f(x)| = c and verifying is fast and catches every spurious answer. This checking habit becomes even more critical when you move to absolute value inequalities, where the logic shifts from "exactly this distance from zero" to "closer than" or "farther than," and where forgetting the negative case entirely changes the solution set.
