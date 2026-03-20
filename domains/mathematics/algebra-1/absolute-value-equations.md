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

## Questions

```yaml
- question: "A student solving |3x + 6| − 4 = 8 immediately writes: 3x + 6 = 12 and 3x + 6 = −12. What error did they make?"
  type: multiple-choice
  options:
    - "They set up the wrong pair of cases — they should use +8 and −8, not +12 and −12"
    - "They failed to isolate the absolute value first; they should add 4 to both sides to get |3x + 6| = 12 before splitting"
    - "They should only write one case, since the equation has a unique solution"
    - "There is no error; this setup correctly leads to the right answers"
  answer: 1
  explanation: "The rule is to isolate the absolute value expression before splitting into cases. With |3x + 6| − 4 = 8, the −4 is outside the bars. Splitting immediately — as if the equation were |3x + 6| = 8 — gives the wrong right-hand side. You must first add 4 to both sides to get |3x + 6| = 12, and only then write 3x + 6 = 12 and 3x + 6 = −12. The student's equations happen to use ±12 but for the wrong reason — they derived it by folding in the 4, which is precisely the procedure they should have done explicitly."

- question: "What is the solution to |x − 5| = −3?"
  type: multiple-choice
  options:
    - "x = 2 and x = 8"
    - "x = 8 only"
    - "No solution — absolute value cannot equal a negative number"
    - "x = −2 and x = −8"
  answer: 2
  explanation: "Absolute value measures distance from zero, and distance is never negative. For any value of x, |x − 5| ≥ 0 always. No number can be −3 units from zero, so there is no solution. You don't need to split into cases — you should recognize immediately that the right side is negative and conclude no solution exists. This saves work and builds the mathematical instinct that absolute value equations with negative right-hand sides are always unsolvable."

- question: "If the right side of an absolute value equation equals zero, there is no solution."
  type: true-false
  answer: false
  explanation: "When |expression| = 0, there is exactly one solution: the value that makes the expression equal to zero. For example, |x + 2| = 0 has the solution x = −2. Zero is not negative — absolute value can equal zero when the expression inside evaluates to zero. The 'no solution' rule only applies when the right side is strictly negative. Confusing |expression| = 0 with |expression| = negative is a subtle but consequential error."

- question: "To correctly solve |5x − 2| + 3 = 11, you must subtract 3 from both sides before splitting into two cases."
  type: true-false
  answer: true
  explanation: "The +3 is outside the absolute value bars, so it must be removed before the two-case split. Subtracting 3 from both sides gives |5x − 2| = 8, which then splits into 5x − 2 = 8 and 5x − 2 = −8. If you split too early with the +3 still present, you get the wrong right-hand side values (±11 instead of ±8) and both solutions will be incorrect. 'Isolate first, split second' is the non-negotiable order of operations."

- question: "Explain why solving |2x − 3| = 7 requires two separate equations rather than one, connecting your explanation to the definition of absolute value as distance."
  type: short-answer
  answer: "Absolute value measures distance from zero on the number line. The equation |2x − 3| = 7 asks: for what values of x is the expression (2x − 3) exactly 7 units from zero? Two numbers are 7 units from zero: +7 and −7. Therefore the expression inside can equal either +7 or −7, producing two equations: 2x − 3 = 7 (giving x = 5) and 2x − 3 = −7 (giving x = −2). Considering only one case misses half the solutions by ignoring the symmetry of distance around zero."
  explanation: "The two-case technique is not an arbitrary algebraic rule — it follows directly from what absolute value means. Because distance has two directions (positive and negative from zero), any equation setting a distance equal to a positive number has two candidate expressions. This 'case analysis' thinking — identifying a condition with two possibilities and solving each — is a pattern that transfers to piecewise functions, inequalities, and proof techniques encountered throughout later mathematics."
```

## Explainer

You already know that absolute value measures distance from zero on the number line — that is the key to understanding these equations. When you see |2x − 3| = 7, the question is: what values make the expression inside the bars exactly 7 units away from zero? There are always two numbers that are 7 units from zero: positive 7 and negative 7. So the expression inside can equal either 7 or −7. That is the entire logic of the **two-case split**: |expression| = k becomes expression = k or expression = −k.

The critical first step is always to **isolate the absolute value** before splitting. Suppose you have |2x − 3| + 5 = 12. You cannot split immediately — the +5 is outside the bars. Subtract 5 from both sides first to get |2x − 3| = 7, and only then write your two equations: 2x − 3 = 7 and 2x − 3 = −7. Solving the first gives x = 5; solving the second gives x = −2. Both are valid solutions, and you can check: |2(5) − 3| = |7| = 7 ✓ and |2(−2) − 3| = |−7| = 7 ✓.

What happens when the right side is negative, like |x + 1| = −4? Absolute value measures distance, and distance is never negative. No matter what x is, |x + 1| ≥ 0 always. So there are **no solutions** — you do not even need to split into cases. Recognizing this immediately saves work and builds sound mathematical instinct.

This technique — splitting into cases based on what makes an expression positive or negative — is a pattern you will use far beyond absolute value. It appears in piecewise functions, inequalities, and eventually in analyzing cases in proofs. The absolute value equation is your first systematic encounter with **case analysis**: identifying the condition that determines which branch of a problem applies, solving each branch independently, and combining the results. That thinking skill transfers directly to more advanced mathematics.
