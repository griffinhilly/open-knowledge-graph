---
id: integers-and-number-line
title: Integers and the Number Line
domain: mathematics
course: prealgebra
prerequisites:
- id: place-value-whole-numbers
  type: soft
- id: decimal-place-value
  type: soft
- id: comparing-ordering-whole-numbers
  type: soft
builds-toward:
  - absolute-value
  - adding-integers
  - subtracting-integers
tags: [integers, number-line, negative-numbers]
stage: abstract-reasoning
status: validated
---

# Integers and the Number Line

## Core Idea
Integers extend the whole numbers to include negative numbers and zero. The number line is a visual model that places every integer at an equal spacing, with negative numbers to the left of zero and positive numbers to the right. Understanding integers is foundational because they appear everywhere in real life — temperatures below zero, debts, elevations below sea level — and they are the gateway to all of algebra. The number line also introduces the idea that numbers have both magnitude (how far from zero) and direction (positive or negative), a concept that will eventually generalize to vectors and coordinate planes.

## How It's Best Learned
Start with concrete contexts students already understand: thermometers, bank accounts, floors above and below ground level. Have students physically place integers on a number line, emphasizing symmetry around zero. Use comparison exercises (which is greater, -3 or -7?) to build intuition before any operations.

## Common Misconceptions
- Students often think -7 is greater than -3 because 7 > 3. Reinforce that further left on the number line means smaller.
- Some students believe zero is not an integer or confuse it with "nothing" rather than a specific location on the number line.
- Students may think negative numbers are only used in math class and have no real-world meaning.

## Questions

```yaml
- question: "Which of the following correctly orders the integers from least to greatest?"
  type: multiple-choice
  options: ["-8, -3, 0, 2", "2, 0, -3, -8", "-3, -8, 0, 2", "0, -3, -8, 2"]
  answer: 0
  explanation: "On the number line, further left means smaller. -8 is leftmost (smallest), then -3, then 0, then 2 (greatest). The other options reverse or scramble this order."

- question: "-7 is greater than -3 because 7 is greater than 3."
  type: true-false
  answer: false
  explanation: "On the number line, -7 is further left than -3, which means -7 is smaller, not greater. A larger absolute value in the negative direction indicates a smaller number — think of debt: owing $7 is worse than owing $3."

- question: "A thermometer reads -5°C in the morning and 3°C in the afternoon. How many degrees did the temperature rise?"
  type: short-answer
  answer: "8 degrees"
  explanation: "From -5 to 3 is a change of 3 - (-5) = 3 + 5 = 8 degrees. On the number line, this is a move of 8 units to the right. Subtracting a negative is the same as adding its positive counterpart."
```

## Explainer

The whole numbers you learned first (0, 1, 2, 3, ...) describe quantities that can only grow. But many real situations involve values that fall below zero: a thermometer reads −10°C, a bank account shows −$50 (overdrawn), an elevator descends to floor −2 (below ground level). Integers extend the whole numbers by including all these negative counterparts, so that every positive number has an opposite.

The number line makes this visual. Zero sits at the center. Positive integers extend infinitely to the right, negative integers extend infinitely to the left, and every integer occupies a unique, equally-spaced point. The number line encodes the rule for ordering: a number further to the right is always greater. This means −3 is greater than −7, because −3 sits to the right of −7 on the line — even though 7 > 3 in the positive direction. Students often get this backwards: the bigger the absolute value, the further from zero, but "further left" means smaller, not bigger.

Each positive integer and its negative counterpart are called opposites, and they are equidistant from zero in opposite directions. The opposite of 5 is −5; the opposite of −5 is 5. Zero is its own opposite. This symmetry is foundational — when you later study absolute value, you will be measuring that exact distance from zero.

Zero itself is an integer, but it is neither positive nor negative. It is the additive identity: adding zero to any integer leaves it unchanged. Students sometimes treat zero as a non-number or as belonging to neither side, but it is a full member of the integers with its own specific location on the number line.

The number line also gives you a concrete model for operations you will learn next. Adding a positive number moves you to the right; adding a negative number moves you to the left. This directional interpretation makes integer arithmetic far more intuitive than any memorized sign rule — you are simply tracking movement along a line.
