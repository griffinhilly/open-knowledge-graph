---
id: compound-inequalities
title: Compound Inequalities
domain: mathematics
course: algebra-1
prerequisites:
  - id: solving-inequalities
    type: hard
  - id: one-step-inequalities
    type: hard
builds-toward:
  - absolute-value-inequalities
  - systems-of-inequalities
tags: [inequalities, compound, and, or, graphing]
stage: abstract-reasoning
status: validated
---

# Compound Inequalities

## Core Idea
A compound inequality combines two inequalities using "and" or "or." An "and" compound inequality (e.g., −3 < x < 7, or equivalently x > −3 AND x < 7) has solutions that satisfy both conditions simultaneously — the intersection. An "or" compound inequality (e.g., x < −2 OR x > 5) has solutions that satisfy at least one condition — the union. On a number line, "and" produces a segment between two values, while "or" produces two rays pointing outward. Compound inequalities model real-world constraints like temperature ranges, acceptable measurements, and eligibility criteria.

## How It's Best Learned
Solve each part of the compound inequality separately, then combine on a number line. For "and" inequalities, practice the shorthand notation (−3 < x < 7) and solving all three parts simultaneously. For "or" inequalities, emphasize that the solution is everything in either region. Use interval notation as an alternative representation. Test values to verify solutions.

## Common Misconceptions
- Confusing "and" with "or" — "and" narrows the solution, "or" widens it.
- Writing an "and" inequality as x > 7 AND x < −3, which has no solution (empty set), and not recognizing it as impossible.
- Solving −3 < 2x + 1 < 7 by only solving one side of the inequality.

## Questions

```yaml
- question: "A machine is safe to operate only when the temperature is above −5°C and below 40°C. Which compound inequality correctly represents the safe operating range?"
  type: multiple-choice
  options:
    - "T < −5 OR T > 40"
    - "T > −5 OR T < 40"
    - "T > −5 AND T < 40, equivalently written −5 < T < 40"
    - "T < −5 AND T > 40"
  answer: 2
  explanation: "Both conditions must hold simultaneously — the temperature must be above −5 AND below 40. This is an 'and' (intersection) compound inequality, graphed as a segment between the two endpoints. Option A represents the unsafe shutdown range. Option B uses 'or' which would mean 'any temperature except exactly −5 or exactly 40' — almost all temperatures. Option D is logically impossible (nothing is simultaneously less than −5 and greater than 40)."

- question: "Solving a compound 'and' inequality yields x > 8 AND x < 3. What is the solution set?"
  type: multiple-choice
  options:
    - "3 < x < 8"
    - "x < 3 OR x > 8"
    - "All real numbers"
    - "No solution (empty set)"
  answer: 3
  explanation: "No number can simultaneously be greater than 8 and less than 3. The 'and' requires both conditions to be true at once, but these two constraints are mutually exclusive — there is no overlap. This is an empty set. Option A reverses the direction of both inequalities into a valid range, which is a common error. Recognizing impossible 'and' constraints is a key skill; it reveals the underlying logic of intersection."

- question: "An 'or' compound inequality can have a solution set that includes every real number."
  type: true-false
  answer: true
  explanation: "If an 'or' inequality produces two overlapping or covering conditions — for example, x < 10 OR x > 2 — then every real number satisfies at least one condition (any number is either less than 10, or greater than 2, or both). The union can expand to cover the entire number line. This edge case illustrates that 'or' can only widen a solution set, never narrow it."

- question: "An 'and' compound inequality always has at least one solution."
  type: true-false
  answer: false
  explanation: "An 'and' compound inequality requires both conditions to hold simultaneously — which may be impossible. For example, x > 7 AND x < 3 has no solution because no number satisfies both constraints. The intersection of two non-overlapping ranges is the empty set. This is why solving each part of an 'and' compound inequality and checking whether the regions actually overlap is a necessary step."

- question: "Explain the difference between 'and' and 'or' compound inequalities in terms of what kind of solution set each produces."
  type: short-answer
  answer: "'And' means both conditions must be true simultaneously — the solution set is the intersection of the two individual solution sets. On a number line, this looks like a segment between two values (or is empty if the conditions conflict). 'Or' means at least one condition must be true — the solution set is the union of the two individual solution sets. On a number line, this typically looks like two outward-pointing rays with a gap in between (or all real numbers if the regions overlap)."
  explanation: "'And' narrows — it can only produce a solution set smaller than or equal to either individual inequality. 'Or' widens — it can only produce a solution set larger than or equal to either individual inequality. The logical connective determines the fundamental shape of the solution, which is why misreading 'and' as 'or' (or vice versa) produces a dramatically wrong answer, not just a minor error."
```

## Explainer

You already know how to solve a single inequality — you isolate the variable and flip the sign when multiplying or dividing by a negative. A **compound inequality** simply chains two of those constraints together and asks: when are both (or at least one) true at the same time?

The word "and" means **intersection**: both conditions must hold simultaneously. If a thermometer must read above 0°C but below 100°C to register liquid water, that is an "and" statement — 0 < T < 100. On a number line, this looks like a segment with two endpoints: you shade only the region between the two boundaries. When you solve a three-part inequality like −3 < 2x + 1 < 7, you are really solving two inequalities at once: 2x + 1 > −3 and 2x + 1 < 7. The efficient approach is to operate on all three parts simultaneously — subtract 1 from all three, then divide all three by 2 — keeping the variable trapped in the middle.

The word "or" means **union**: either condition is enough. If a machine shuts off when the temperature is too low (below −10°C) or too high (above 80°C), the shutdown condition is an "or" statement. On a number line, this produces two rays pointing outward from the two boundary values, with a gap in the middle. Note that an "or" solution set is always at least as large as an "and" solution set — it can never be narrower.

A useful sanity check: if an "and" compound inequality forces x to be simultaneously greater than 7 and less than 3, that is an **empty set** — no number satisfies both at once, and the solution is "no solution." Conversely, if an "or" compound inequality gives x < 10 or x > 2, you should recognize that every real number satisfies at least one condition, giving the solution "all real numbers." These edge cases reveal the underlying logic: "and" can collapse to nothing, and "or" can expand to everything.
