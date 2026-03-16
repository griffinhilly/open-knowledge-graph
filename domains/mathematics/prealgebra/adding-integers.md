---
id: adding-integers
title: Adding Integers
domain: mathematics
course: prealgebra
prerequisites:
  - id: integers-and-number-line
    type: hard
  - id: absolute-value
    type: soft
builds-toward:
  - subtracting-integers
  - combining-like-terms
  - one-step-equations
tags: [integers, addition, operations]
stage: abstract-reasoning
status: validated
---

# Adding Integers

## Core Idea
Adding integers extends whole-number addition to include negative numbers. When both integers have the same sign, you add their absolute values and keep the shared sign. When they have different signs, you subtract the smaller absolute value from the larger and take the sign of the number with the greater absolute value. On the number line, adding a positive number means moving right, and adding a negative number means moving left. This skill is used constantly in algebra when combining terms, solving equations, and working with polynomials.

## How It's Best Learned
Begin with number line hops — physically showing that 3 + (−5) means start at 3, move 5 left, land at −2. Use integer chips (positive/negative pairs that cancel) as a second model. Once students have intuition, formalize the two rules (same sign, different sign). Drill with a mix of positive-positive, negative-negative, and mixed-sign problems.

## Common Misconceptions
- Students may apply whole-number addition and ignore signs, writing (−3) + (−4) = 7 instead of −7.
- Confusion between "adding a negative" and subtraction — they are the same operation, but students don't always see that yet.
- When adding numbers of different signs, students sometimes subtract but pick the wrong sign for the result.

## Questions

```yaml
- question: "What is (-7) + 3?"
  type: multiple-choice
  options: ["-10", "-4", "4", "10"]
  answer: 1
  explanation: "The two numbers have different signs, so we subtract the smaller absolute value from the larger: 7 - 3 = 4. The number with the greater absolute value is -7, so the result is negative: -4."

- question: "(-4) + (-6) = -2"
  type: true-false
  answer: false
  explanation: "Both numbers are negative (same sign), so you add their absolute values (4 + 6 = 10) and keep the negative sign: (-4) + (-6) = -10, not -2. The error of getting -2 comes from subtracting the smaller from the larger, which only applies when the signs are different."

- question: "Why is adding a negative number the same as subtracting a positive number?"
  type: short-answer
  answer: "Adding a negative number moves you left on the number line by the same amount that subtracting a positive would — both operations reduce the total by the same magnitude."
  explanation: "On the number line, addition always means movement in the direction of the number's sign. Adding +5 moves right 5 units; adding -5 moves left 5 units. Subtracting 5 also moves left 5 units. Both produce identical results, which is why a + (-b) = a - b."
```

## Explainer

The key to adding integers is the number line. Every integer lives at a specific location, and every addition is a movement. When you compute 3 + (-5), you start at 3 and move 5 steps to the left (because -5 is negative, pointing left). You land at -2. This physical picture makes the rules feel inevitable rather than arbitrary.

Two rules cover every case. When both integers share the same sign — like (-4) + (-6) — you are moving in the same direction both times, so you combine their distances: 4 + 6 = 10 steps, and since both moves went left, the answer is -10. When the integers have different signs — like (-7) + 3 — you are first moving in one direction, then partially backtracking. The net result is the difference of the distances (7 - 3 = 4) in the direction of whichever had the longer journey. Since -7 had the greater absolute value, the result is negative: -4.

The most common error is applying the "different sign" rule (subtract) when both signs are actually the same. For example, some students compute (-4) + (-6) as -2 by subtracting — but both numbers are negative, so you should be adding their magnitudes to get -10. Always check the signs first: are they the same or different?

Absolute value, which you already know, gives this rule a precise name: the absolute value of an integer is its distance from zero. The rules are really just: (same signs) add the distances and keep the sign; (different signs) find the difference of the distances and use the sign of the farther one. These two rules will carry you through algebra, combining like terms, and solving equations.

