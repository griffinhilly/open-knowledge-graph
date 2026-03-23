---
id: comparing-quantities-three-digit-2nd
title: Comparing and Ordering Three-Digit Quantities
domain: mathematics
course: 2nd-grade
prerequisites:
- id: comparing-three-digit-numbers
  type: hard
- id: place-value-whole-numbers
  type: hard
builds-toward:
- comparing-ordering-whole-numbers
tags:
- comparison
- ordering
- place-value
stage: concrete-operations
status: validated
---

# Comparing and Ordering Three-Digit Quantities

## Core Idea
When comparing three-digit numbers, look at the hundreds place first. If they're equal, look at the tens place; if still equal, look at the ones place. You can represent comparisons with symbols (<, >, =) or ordered lists (least to greatest).

## How It's Best Learned
Use base-ten blocks to visually compare quantities. Practice comparing numbers without blocks, verifying answers with blocks. Order sets of numbers and explain the reasoning.

## Common Misconceptions
- Comparing based on the count of digits rather than place value.
- Confusing which symbol means 'greater than' or 'less than'.
- Not checking all place values systematically.

## Questions

```yaml
- question: "A student compares 482 and 479 and concludes '479 is greater because 79 is greater than 82.' What error did the student make?"
  type: multiple-choice
  options:
    - "No error — comparing the last two digits is a valid method for three-digit numbers"
    - "The student compared the tens and ones digits while ignoring the hundreds; since both numbers have the same hundreds digit (4), you compare the tens: 8 > 7, so 482 > 479"
    - "The student should have compared the ones digits first, then moved left"
    - "The student should have added all the digits in each number before comparing"
  answer: 1
  explanation: "The correct method is left-to-right comparison: hundreds first, then tens (only if hundreds tie), then ones (only if tens also tie). Both numbers have 4 hundreds, so move to the tens: 8 tens vs. 7 tens — 8 wins, so 482 > 479. Comparing the two-digit endings (82 vs. 79) looks plausible because it gives the right answer here — but it breaks down with other numbers and misunderstands why place value works the way it does."

- question: "You need to order 523, 532, and 519 from least to greatest. What is the correct first step?"
  type: multiple-choice
  options:
    - "Compare the ones digits of all three numbers first, since they differ the most"
    - "Add all the digits of each number and compare the sums"
    - "Compare the hundreds digits; if equal, compare tens digits; if still equal, compare ones digits"
    - "Look for the largest individual digit anywhere in any of the numbers"
  answer: 2
  explanation: "Always start at the leftmost (most powerful) digit — the hundreds place. All three numbers have 5 hundreds, so move to the tens: 2 vs. 3 vs. 1. Ordering by tens gives 519 (1 ten) < 523 (2 tens) < 532 (3 tens). The ones digits never need to be compared here because the tens already differentiate all three. Starting at the ones digit (option A) would give a wrong ordering in many cases."

- question: "When comparing 347 and 291, it is necessary to look at the tens and ones digits to determine which number is greater."
  type: true-false
  answer: false
  explanation: "The hundreds digit is decisive: 3 hundreds vs. 2 hundreds — 3 wins, so 347 > 291 immediately. You never need to look at the tens or ones digits because no combination of tens and ones in a three-digit number can compensate for a deficit of one full hundred. (The maximum value of the tens and ones places combined is 99, which is less than 100.) You stop as soon as you find a differing digit, moving left to right."

- question: "The symbol < always points toward the smaller number in a comparison."
  type: true-false
  answer: true
  explanation: "The < and > symbols both 'open' toward the larger value, meaning the pointed tip aims at the smaller one. In 318 < 472, the tip of < points at 318 (the smaller number) and opens toward 472 (the larger). One memory trick: the symbol is like a hungry mouth that eats the bigger number — it always opens toward the greater value, with the tip pointing at the lesser."

- question: "Explain why you always start comparing at the hundreds place (leftmost digit) when comparing three-digit numbers. What would go wrong if you started with the ones place instead?"
  type: short-answer
  answer: "The hundreds place is the most powerful: a single hundred is worth more than any possible combination of tens and ones (the max is 9 tens + 9 ones = 99, which is less than 100). If one number has more hundreds than another, it is automatically greater — no other digits matter. Starting with the ones place gives the wrong result whenever the higher-place digits differ. For example, comparing 700 and 199 by ones digits gives 0 vs. 9, incorrectly suggesting 199 is greater."
  explanation: "Place value is a positional system where each position to the left is worth 10 times more than the position to the right. Comparison must proceed from most valuable to least valuable because the higher place will always override whatever the lower places say. This same logic extends to larger numbers: you always compare digits left to right, stopping the moment you find a position where the digits differ."
```

## Explainer

You already know how place value works: in a three-digit number like 352, the 3 stands for 3 hundreds (300), the 5 stands for 5 tens (50), and the 2 stands for 2 ones (2). Comparing two numbers is really asking: which one represents a bigger total? The smartest way to find out is to start with the most powerful digit — the **hundreds place** — because a single hundred is worth more than all nine tens and nine ones combined (100 > 99).

Here is the rule: **look left first**. Compare the hundreds digits of the two numbers. If one is larger, that number is greater — and you are done. You never even need to look at the tens or ones. For example, 472 vs. 318: 4 hundreds beats 3 hundreds, so 472 > 318, full stop. Only when the hundreds digits are *equal* do you need to move right and compare the tens digits. And only if the tens are also equal do you look at the ones.

The **symbols** <, >, and = are shorthand for this comparison. The symbol always "opens toward" the larger number — think of it as a hungry mouth eating the bigger meal. So 472 > 318 means "472 is greater than 318." You can flip it and write 318 < 472 — same relationship, different direction. When you need to **order** several numbers — say, from least to greatest — you apply this same left-to-right comparison repeatedly, like sorting a hand of cards by color first, then by value within each color. Start by sorting on hundreds, then break ties with tens, then with ones. The result is a line of numbers from smallest to largest, each one checked systematically against its neighbors.
