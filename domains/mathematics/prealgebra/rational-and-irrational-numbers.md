---
id: rational-and-irrational-numbers
title: Rational and Irrational Numbers
domain: mathematics
course: prealgebra
prerequisites:
  - id: square-roots-intro
    type: hard
  - id: converting-fractions-decimals-percents
    type: hard
  - id: rational-numbers-operations
    type: soft
builds-toward:
  - radical-expressions-simplifying
  - completeness-axiom
tags: [real-numbers, irrational-numbers, decimals, square-roots, number-system]
stage: abstract-reasoning
status: validated
---

# Rational and Irrational Numbers

## Core Idea
A rational number is one that can be written as a fraction a/b of integers with b ≠ 0. In decimal form, every rational number either terminates (like 0.75) or repeats forever (like 0.333...). An irrational number is a real number that cannot be written as such a fraction, so its decimal never ends and never settles into a repeating block. Examples include √2, √3 and π. Rational and irrational numbers together make up the real numbers, which fill the whole number line.

## How It's Best Learned
Start by converting fractions to decimals with long division and noticing that the remainders must eventually repeat. Then approximate √2 by squaring guesses (1.4² = 1.96, 1.5² = 2.25) to show the digits keep going without a pattern. Place rational and irrational numbers on a number line together, and practice classifying numbers such as √16, √15, 0.121212... and 22/7.

## Common Misconceptions
- π equals 22/7 or 3.14. (Both are rational approximations; π itself is irrational, and 22/7 = 3.142857... differs from π = 3.14159... in the third decimal place.)
- Every square root is irrational. (The square root of a perfect square is a whole number, and the square root of a ratio of perfect squares is a fraction, so √16 = 4 and √(9/25) = 3/5 are rational.)
- A decimal that is long or looks random must be irrational. (Any decimal that eventually repeats is rational, however long its repeating block; 1/7 = 0.142857142857... is rational.)
- Multiplying two irrational numbers always gives an irrational number. (√2 × √2 = 2, which is rational.)

## Questions

```yaml
- question: "Which of these numbers is irrational?"
  type: multiple-choice
  options: ["√25", "0.272727...", "√7", "-4/9"]
  answer: 2
  explanation: "√25 = 5 is an integer, 0.272727... = 27/99 = 3/11 is a repeating decimal, and -4/9 is already a fraction of integers. 7 is not a perfect square, so √7 cannot be written as a fraction of integers and is irrational."

- question: "The number 22/7 is exactly equal to π."
  type: true-false
  answer: false
  explanation: "22/7 is a fraction of integers, so it is rational, while π is irrational. 22/7 = 3.142857... is a useful approximation, but π = 3.14159..., so the two differ starting in the third decimal place."

- question: "Between which two consecutive tenths does √2 lie? Show how you know."
  type: short-answer
  answer: "Between 1.4 and 1.5, because 1.4² = 1.96 < 2 and 1.5² = 2.25 > 2."
  explanation: "Squaring brackets the root. Since 1.96 < 2 < 2.25, the number whose square is 2 lies between 1.4 and 1.5. Repeating the process with hundredths (1.41² = 1.9881, 1.42² = 2.0164) narrows it further, and the digits never begin to repeat."

- question: "Write the repeating decimal 0.444... as a fraction."
  type: short-answer
  answer: "4/9"
  explanation: "Let x = 0.444.... Then 10x = 4.444.... Subtracting gives 9x = 4, so x = 4/9. Any repeating decimal can be converted this way, which is why repeating decimals are rational."
```

## Explainer

You already know many kinds of numbers: whole numbers, integers, fractions and decimals. All of these can be written as one integer divided by another nonzero integer. For example, 5 = 5/1, -3 = -3/1 and 0.75 = 3/4. Numbers that can be written this way are called rational, from the word "ratio."

Rational numbers have a recognizable decimal form. When you divide a by b with long division, each remainder is smaller than b, so there are only finitely many possible remainders. Either a remainder of 0 appears and the decimal stops, or some remainder comes back and the digits start repeating. That is why 3/8 = 0.375 terminates and 2/11 = 0.181818... repeats. The process also runs backward: a repeating decimal can be turned into a fraction. If x = 0.181818..., then 100x = 18.181818..., and subtracting gives 99x = 18, so x = 18/99 = 2/11.

Some numbers do not fit this pattern. Try to find √2. Since 1² = 1 and 2² = 4, it lies between 1 and 2. Since 1.4² = 1.96 and 1.5² = 2.25, it lies between 1.4 and 1.5. You can keep narrowing forever, getting 1.41421356..., and the digits never settle into a repeating block. The ancient Greeks proved that no fraction a/b, squared, gives exactly 2. Numbers like this are called irrational. Other examples are √3, √5, any square root of a whole number that is not a perfect square, and the circle constant π.

Rational and irrational numbers together form the real numbers. Every point on the number line is one or the other, never both. To place an irrational number, use rational approximations: √10 is a little more than 3 because 3² = 9, and π sits just to the right of 3.14.

Be careful with arithmetic rules. The sum of a rational number and an irrational number is always irrational, so 1 + √2 is irrational. But two irrational numbers can combine to give a rational one: √2 × √2 = 2, and (1 + √2) + (1 - √2) = 2. Classify each result by checking it, not by assuming.
