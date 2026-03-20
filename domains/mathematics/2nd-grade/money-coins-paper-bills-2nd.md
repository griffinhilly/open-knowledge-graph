---
id: money-coins-paper-bills-2nd
title: Counting Coins and Paper Bills
domain: mathematics
course: 2nd-grade
prerequisites:
- id: counting-coins-and-bills
  type: hard
- id: coins-and-their-values
  type: soft
builds-toward:
- making-change-2nd
tags:
- money
- coins
- bills
stage: concrete-operations
status: draft
---

# Counting Coins and Paper Bills

## Core Idea
Coins (pennies, nickels, dimes, quarters) and bills (ones, fives, tens) have different values. Count coins starting with the largest value first for efficiency: quarters, dimes, nickels, pennies.

## Questions

```yaml
- question: "A student has 2 quarters, 1 dime, and 4 pennies. Which counting approach will reach the correct total most efficiently?"
  type: multiple-choice
  options:
    - "Start with the 4 pennies (1, 2, 3, 4), add the dime (14), then add each quarter (39, 64 cents)"
    - "Start with the 2 quarters (25, 50), then add the dime (60), then add the pennies (61, 62, 63, 64 cents)"
    - "Count all coins simultaneously by grouping them into sets of 10"
    - "It doesn't matter — all counting orders take the same number of steps and reach the same answer"
  answer: 1
  explanation: "Starting with the largest denomination (quarters: 25, 50) then working down to the dime (60) then pennies (61, 62, 63, 64) minimizes counting steps and reaches the correct total of 64 cents. Starting with pennies forces counting by ones from the very beginning — many more steps and more opportunities for error. The 'largest first' strategy works because high-value coins cover more ground per step."

- question: "Which of the following coin combinations does NOT equal 25 cents?"
  type: multiple-choice
  options:
    - "1 quarter"
    - "5 nickels"
    - "2 dimes and 1 nickel"
    - "4 nickels and 4 pennies"
  answer: 3
  explanation: "4 nickels = 20 cents, plus 4 pennies = 4 cents, totaling 24 cents — one cent short of 25. The other three all equal 25 cents: 1 quarter = 25¢; 5 nickels = 5×5 = 25¢; 2 dimes + 1 nickel = 20+5 = 25¢. This question illustrates coin equivalence — many different combinations can represent the same value, which is the key idea behind making change."

- question: "When counting a mixed collection of coins, starting with the highest-value coins (quarters before dimes before nickels before pennies) leads to fewer counting steps."
  type: true-false
  answer: true
  explanation: "Each quarter covers 25 cents in one counting step; each penny covers only 1 cent per step. Starting with high-value coins means you count up in large jumps first, covering most of the total quickly. Starting with pennies means counting by ones all the way before adding any large coins — many more steps, more time, and more chances for error."

- question: "A dime is worth more than a nickel because it is physically larger."
  type: true-false
  answer: false
  explanation: "A dime is actually smaller in physical size than a nickel, yet it is worth twice as much (10 cents vs. 5 cents). Coin values are assigned by convention, not determined by size or weight. This trips up many learners who expect larger coins to be worth more. Knowing coin values requires memorization — you cannot infer them from appearance."

- question: "Why is it more efficient to count coins starting with the largest denomination? What would happen if you started with pennies instead when counting 1 quarter, 2 dimes, and 3 pennies?"
  type: short-answer
  answer: "Largest-first: 25 (quarter), 35, 45 (dimes), 46, 47, 48 (pennies) — the large jumps happen first, and only 3 slow penny-steps remain at the end. Pennies-first: 1, 2, 3 (pennies), 13 (dime), 23 (dime), 48 (quarter) — same number of steps here, but for larger collections the difference grows. Starting with pennies leaves you counting by ones while high-value coins sit unused, making it harder to hold the running total in mind."
  explanation: "The 'largest first' strategy reduces cognitive load by front-loading the big jumps. You cover most of the total in a few steps, leaving only a small remainder to count by ones. It also mirrors efficient mental addition — experienced counters instinctively start with the biggest pieces because it mirrors how place value works (hundreds before tens before ones)."
```

## Explainer

Money is a real-world application of everything you know about counting and number values. Each coin and bill is simply a physical token that stands for a number of cents or dollars. A **penny** equals 1 cent, a **nickel** equals 5 cents, a **dime** equals 10 cents, and a **quarter** equals 25 cents. Paper **bills** work the same way at the dollar level: a one-dollar bill = 100 cents, a five = 500 cents, a ten = 1,000 cents. Knowing these values by heart is the starting point for everything else in money math.

The most efficient way to count a mixed collection of coins is to **sort by value and start with the largest**. If you have 1 quarter, 2 dimes, 1 nickel, and 3 pennies, begin at 25, count on by 10s (35, 45), then by 5s (50), then by 1s (51, 52, 53). You arrive at 53 cents without losing track. Starting with pennies would force you to count 1 by 1 all the way, making errors more likely. The "largest first" strategy works because it minimizes the number of counting steps.

The same logic applies to bills. If you have a ten, two fives, and three ones, start at 10, count on 5 (15), 5 (20), 1 (21), 1 (22), 1 (23): twenty-three dollars. Notice this is the same as adding: 10 + 5 + 5 + 1 + 1 + 1 = 23. Counting money is just addition with named values instead of abstract numbers.

One key idea is that different combinations can represent the **same total**. Two dimes and a nickel equal a quarter; five nickels equal a quarter; ten pennies equal a dime. Recognizing these equivalences lets you make change — swapping one combination for another of equal value. This skill builds directly toward making change, where you figure out what coins to give back so that the amount paid plus the change equals the price.
