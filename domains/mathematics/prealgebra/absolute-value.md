---
id: absolute-value
title: Absolute Value
domain: mathematics
course: prealgebra
prerequisites:
- id: integers-and-number-line
  type: hard
- id: comparing-and-ordering-integers
  type: soft
- id: opposites-and-additive-inverses
  type: soft
builds-toward:
- absolute-value-equations
- absolute-value-inequalities
tags:
- absolute-value
- integers
- distance
stage: abstract-reasoning
status: validated
---
# Absolute Value

## Core Idea
The absolute value of a number is its distance from zero on the number line, regardless of direction. It answers the question "how far?" without caring about "which way?" For example, both -5 and 5 are five units from zero, so |−5| = |5| = 5. Absolute value is always non-negative. This concept is important because distance and magnitude come up constantly in mathematics and science — you cannot have a negative distance. It also lays the groundwork for absolute value equations and inequalities in algebra.

## How It's Best Learned
Use the number line heavily. Have students count spaces from zero for various integers. Emphasize the language of "distance from zero" rather than "just drop the negative sign," because the latter rule fails when students encounter expressions like |3 − 8| and need to evaluate inside first. Practice with both single numbers and simple expressions inside the bars.

## Common Misconceptions
- Students treat absolute value as "make it positive," which leads to errors when the input is an expression (e.g., |x| when x is already positive, or |a − b|).
- Some students think |−3| = −3 because they see the negative sign and don't process the bars.
- Confusing absolute value with "opposite" — the absolute value of a positive number is not its opposite.

## Questions

```yaml
- question: "What is |3 − 8|?"
  type: multiple-choice
  options:
    - "−5"
    - "5"
    - "11"
    - "−11"
  answer: 1
  explanation: "Evaluate the expression inside first: 3 − 8 = −5. Then take the absolute value (distance from zero): |−5| = 5. The most common error is to 'drop the negative sign' on the 3 or 8 before subtracting, which gives the wrong answer. The bars act like parentheses — everything inside is computed first."

- question: "If x = −6, what is |x + 2|?"
  type: multiple-choice
  options:
    - "8"
    - "−4"
    - "4"
    - "−8"
  answer: 2
  explanation: "Substitute x = −6 and evaluate inside first: −6 + 2 = −4. Then take the absolute value: |−4| = 4. Option A (8) comes from incorrectly treating |x| as 6 before adding 2. Option B keeps the negative sign, which is wrong because absolute value is always non-negative. The key rule: evaluate the expression inside the bars completely, then report the distance from zero."

- question: "For any two real numbers a and b, |a − b| = |b − a|."
  type: true-false
  answer: true
  explanation: "Absolute value measures distance on the number line, and distance is symmetric — the distance from a to b is the same as the distance from b to a. Algebraically, b − a = −(a − b), and |−(a − b)| = |a − b| since absolute value ignores the sign. This is why order doesn't matter when computing distance between two numbers."

- question: "If x is a positive number, then |x − 15| = x − 15."
  type: true-false
  answer: false
  explanation: "This is only true when x ≥ 15. When x is positive but less than 15 — say x = 4 — then x − 15 = −11, and |x − 15| = |−11| = 11, not −11. Absolute value depends on whether the expression inside is non-negative, not on whether x itself is positive. A positive x does not guarantee a non-negative expression inside the bars."

- question: "Why is 'just drop the negative sign' a dangerous shortcut for evaluating absolute value?"
  type: short-answer
  answer: "The shortcut only works when the input is a bare negative number like |−5|. It fails on expressions like |3 − 8|, where you must evaluate the expression first (getting −5) before taking the distance. 'Dropping the negative sign' on 3 or 8 individually gives the wrong answer. Absolute value means distance from zero of the entire expression inside the bars — not a piecewise operation on individual terms."
  explanation: "The shortcut encourages students to act on the negative sign before computing, but absolute value applies to the final result inside the bars. |3 − 8| ≠ 3 + 8. The correct process is: evaluate inside completely, identify the result, then ask how far that result is from zero. This matters especially for expressions with variables, like |a − b|, where you cannot determine the sign without knowing the values."
```

## Explainer

You have already worked with the **number line** and learned about **opposites**: −5 is the opposite of 5, and they sit on opposite sides of zero at equal distances. Absolute value captures exactly that distance. The **absolute value** of a number is simply how far it is from zero on the number line, measured as a non-negative quantity. Because distance is never negative, absolute value is never negative either. Both 5 and −5 are five steps from zero, so |5| = 5 and |−5| = 5.

Think of it this way: the number line has two directions, positive and negative, but distance does not care about direction — it only cares about magnitude. If you ask "how far is −7 from zero?", the answer is 7, not −7. The bars |  | are asking that same question. Everything inside the bars gets evaluated first (like parentheses), and then you report the distance. So |3 − 8| means first compute 3 − 8 = −5, then take the distance: |−5| = 5. This is why "just drop the negative sign" is a dangerous shortcut — it works on bare numbers like |−5|, but fails on expressions.

The **formal definition** makes this precise: |x| = x when x ≥ 0, and |x| = −x when x < 0. At first, writing |x| = −x looks strange — it seems to say absolute value is negative. But when x is negative, −x is positive (the negative of a negative is positive), so the formula gives the right answer. For example, if x = −5, then |x| = −(−5) = 5. This piecewise definition is exactly what you will use when you solve absolute value equations later, because you will split into two cases based on whether the inside is positive or negative.

Absolute value is foundational because **distance** is one of the most universal concepts in mathematics. The distance between any two numbers a and b on the number line is |a − b| — regardless of which is larger. Distance between −3 and 7 is |−3 − 7| = |−10| = 10, or equivalently |7 − (−3)| = |10| = 10. Order does not matter. This single idea — absolute value as distance — will reappear in geometry (distance formulas), analysis (how close two quantities are), and statistics (measuring error). Every time you measure how far apart two things are, you are using the concept you learned here.
