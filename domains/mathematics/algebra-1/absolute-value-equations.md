---
id: absolute-value-equations
title: Absolute Value Equations
domain: mathematics
course: algebra-1
prerequisites:
  - id: absolute-value
    type: hard
  - id: solving-multi-step-equations
    type: hard
builds-toward:
  - absolute-value-inequalities
  - piecewise-functions
tags: [absolute-value, equations, solving, two-cases]
stage: abstract-reasoning
status: validated
---

# Absolute Value Equations

## Core Idea
An absolute value equation like |2x − 3| = 7 asks: what values of x make the expression inside the bars exactly 7 units from zero? Since both 7 and −7 are 7 units from zero, this splits into two cases: 2x − 3 = 7 (giving x = 5) and 2x − 3 = −7 (giving x = −2). Always isolate the absolute value expression first before splitting into cases. If the absolute value equals a negative number (like |x + 1| = −4), there is no solution because absolute value cannot be negative. This topic deepens understanding of absolute value as distance and introduces the important algebraic technique of case analysis.

## How It's Best Learned
Emphasize the distance interpretation: |expression| = k means the expression is k units from zero, which gives two directions. Always isolate the absolute value first, then split into two equations. Check both solutions in the original equation to catch extraneous solutions (which can arise in more complex absolute value equations). Use a number line to visualize both solutions.

## Common Misconceptions
- Forgetting to consider the negative case (finding only one solution instead of two).
- Not isolating the absolute value before splitting: solving |2x − 3| + 5 = 12 by writing 2x − 3 + 5 = 12 or 2x − 3 + 5 = −12.
- Thinking |x| = −4 has a solution (it does not).

## Explainer

You already know that absolute value measures distance from zero on the number line — that is the key to understanding these equations. When you see |2x − 3| = 7, the question is: what values make the expression inside the bars exactly 7 units away from zero? There are always two numbers that are 7 units from zero: positive 7 and negative 7. So the expression inside can equal either 7 or −7. That is the entire logic of the **two-case split**: |expression| = k becomes expression = k or expression = −k.

The critical first step is always to **isolate the absolute value** before splitting. Suppose you have |2x − 3| + 5 = 12. You cannot split immediately — the +5 is outside the bars. Subtract 5 from both sides first to get |2x − 3| = 7, and only then write your two equations: 2x − 3 = 7 and 2x − 3 = −7. Solving the first gives x = 5; solving the second gives x = −2. Both are valid solutions, and you can check: |2(5) − 3| = |7| = 7 ✓ and |2(−2) − 3| = |−7| = 7 ✓.

What happens when the right side is negative, like |x + 1| = −4? Absolute value measures distance, and distance is never negative. No matter what x is, |x + 1| ≥ 0 always. So there are **no solutions** — you do not even need to split into cases. Recognizing this immediately saves work and builds sound mathematical instinct.

This technique — splitting into cases based on what makes an expression positive or negative — is a pattern you will use far beyond absolute value. It appears in piecewise functions, inequalities, and eventually in analyzing cases in proofs. The absolute value equation is your first systematic encounter with **case analysis**: identifying the condition that determines which branch of a problem applies, solving each branch independently, and combining the results. That thinking skill transfers directly to more advanced mathematics.
