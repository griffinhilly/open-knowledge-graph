---
id: factors-and-multiples
title: Factors and Multiples
domain: mathematics
course: 4th-grade
prerequisites:
- id: multi-digit-multiplication
  type: hard
- id: intro-to-long-division
  type: soft
- id: repeated-addition-to-multiplication
  type: soft
- id: arithmetic-patterns-3rd
  type: soft
- id: multiples-of-a-number
  type: soft
builds-toward:
- prime-and-composite-numbers
- equivalent-fractions
- adding-fractions-unlike-denominators
tags:
- number-theory
- multiplication
- division
- factors
stage: concrete-operations
status: validated
---
# Factors and Multiples

## Core Idea
A factor of a number divides it evenly (no remainder). A multiple of a number is the result of multiplying it by a whole number. These are two sides of the same relationship: 4 is a factor of 20, and 20 is a multiple of 4. Finding all factor pairs of a number (e.g., 24: 1x24, 2x12, 3x8, 4x6) and recognizing multiples in skip-counting patterns are foundational skills. Factors and multiples underpin fraction equivalence, simplification, finding common denominators, and later work with greatest common factor and least common multiple.

## How It's Best Learned
Use arrays: a number's factor pairs correspond to the different rectangles you can make with that many tiles. Students systematically find all factor pairs by testing divisors from 1 upward, stopping when pairs start repeating. Practice identifying whether one number is a factor or multiple of another. Use Venn diagrams to find common factors or common multiples of two numbers.

## Common Misconceptions
- Confusing factors and multiples (thinking factors are larger than the number, or multiples are smaller).
- Missing factor pairs by not checking systematically (skipping divisors).
- Forgetting that 1 and the number itself are always factors.

## Questions

```yaml
- question: "Is the following statement true, partially true, or false: '5 is a factor of 35, and 35 is a multiple of 5'?"
  type: multiple-choice
  options:
    - "False — a number can only be one or the other, not both"
    - "Partially true — 35 is a multiple of 5, but 5 cannot be a factor because it is smaller than 35"
    - "True — both statements describe the same multiplication relationship from different directions"
    - "Partially true — 5 is a factor of 35, but 35 is too large to be a multiple of 5"
  answer: 2
  explanation: "Both statements are simultaneously and completely true. Because 5 × 7 = 35, we know that 5 is a factor of 35 (it divides evenly into 35) AND that 35 is a multiple of 5 (it results from multiplying 5 by a whole number). Factors and multiples are two sides of the same multiplication relationship, not competing labels."

- question: "A student claims that the factors of 15 include the number 30 because 30 is related to 15 by multiplication. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — 30 is indeed a factor of 15"
    - "Factors of a number must be less than or equal to the number, and 30 is larger than 15"
    - "30 is only a factor if it divides into 15 with no remainder, and 30 × 0.5 = 15 counts"
    - "Factors only include odd numbers"
  answer: 1
  explanation: "A factor of a number must divide into it evenly — and a factor is always less than or equal to the original number. 30 does not divide into 15 evenly (15 ÷ 30 = 0.5, which is not a whole number), so 30 is not a factor of 15. 30 is actually a multiple of 15. The common misconception is thinking factors can be larger than the number they divide; they cannot."

- question: "Since factors come from multiplication, the factors of a number can sometimes be larger than the number itself."
  type: true-false
  answer: false
  explanation: "Factors must divide into the number evenly, which means every factor is less than or equal to the number. A factor of n is a whole number that divides n with no remainder — this automatically means it cannot exceed n. The only way a × b = n with a > n would require b to be less than 1, which is not a whole number. Multiples, not factors, grow larger than the original number."

- question: "The number 6 is simultaneously a factor of 6 and the smallest positive multiple of 6."
  type: true-false
  answer: true
  explanation: "Every number is a factor of itself (n × 1 = n, so n divides n evenly) and is also its own smallest positive multiple (n × 1 = n). The number sits at the top of its own factor list and at the bottom of its own multiple list. This is not a special case — it applies to every positive whole number."

- question: "A classmate says '12 is a factor of 3 because 3 goes into 12.' What is the error, and what is the correct relationship between 3 and 12?"
  type: short-answer
  answer: "The error is a common confusion of direction. '3 goes into 12' means 3 divides 12 evenly — so 3 is a factor of 12, not the other way around. 12 is a multiple of 3 (because 3 × 4 = 12). The classmate has the labels reversed: the smaller number (3) is the factor, and the larger number (12) is the multiple."
  explanation: "A reliable memory tool: factors are smaller (or equal), multiples are larger (or equal). Because 3 × 4 = 12, we say '3 is a factor of 12' and '12 is a multiple of 3.' The phrase '3 goes into 12' is a division way of expressing the same fact — and the number doing the dividing (3) is the factor."
```

## Explainer

You have already worked with multiples — the endless chain of products you get by multiplying a number by 1, 2, 3, and so on. Now you are going to look at the same multiplication relationship from the opposite direction. While a **multiple** asks "what do I get by multiplying this number by something?", a **factor** asks "what numbers multiply together to make this number?" They are two sides of one coin: because 4 × 6 = 24, you simultaneously know that 4 and 6 are factors of 24, and that 24 is a multiple of both 4 and 6.

A systematic way to find all the factors of a number is to hunt for **factor pairs** — pairs of whole numbers whose product equals your target. For 24, start at 1 and work upward: 1 × 24 = 24 ✓, 2 × 12 = 24 ✓, 3 × 8 = 24 ✓, 4 × 6 = 24 ✓, and 5 doesn't divide 24 evenly. When you try 6, you'd get 6 × 4 — a pair you've already found, just switched. That repeated pair signals you're done. The complete factor list of 24 is: 1, 2, 3, 4, 6, 8, 12, 24. You can visualize each pair as a different rectangular arrangement of 24 tiles — a 1×24 strip, a 2×12 rectangle, a 3×8 rectangle, and a 4×6 rectangle.

A one-sentence check prevents the most common confusion: **a factor is always ≤ the original number; a multiple is always ≥ the original number**. The factors of 24 are all at most 24. The multiples of 24 start at 24 and climb without end. The number itself sits in both lists: 24 is a factor of itself (24 × 1 = 24) and it is its own smallest positive multiple (24 × 1 = 24).

Factors and multiples are not just abstract number exercises — they are the engine behind fraction arithmetic. To add fractions with unlike denominators, you need a **common multiple** of those denominators. To simplify a fraction to lowest terms, you need a **common factor** of the numerator and denominator. Every fraction problem you encounter from here forward draws on exactly the skills you are building now.
