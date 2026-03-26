---
id: adding-subtracting-decimals
title: Adding and Subtracting Decimals
domain: mathematics
course: 5th-grade
prerequisites:
- id: decimal-place-value
  type: hard
- id: multi-digit-addition
  type: hard
- id: multi-digit-subtraction
  type: hard
- id: comparing-decimals
  type: soft
- id: reading-writing-decimals
  type: soft
builds-toward:
- multiplying-decimals
tags:
- decimals
- addition
- subtraction
- arithmetic
stage: concrete-operations
status: validated
---
# Adding and Subtracting Decimals

## Core Idea
Adding and subtracting decimals uses the same algorithms as whole numbers, with one critical rule: line up the decimal points (which means lining up the place values). 3.7 + 2.45 becomes 3.70 + 2.45 = 6.15 when you append a trailing zero to align the hundredths. The decimal point in the answer goes directly below the decimal points in the addends. This works because you are adding like units (tenths to tenths, hundredths to hundredths), just as with whole-number addition. Regrouping and borrowing work identically.

## How It's Best Learned
Start with money: $3.70 + $2.45 is natural and intuitive. Then generalize to non-money contexts. Use base-ten blocks or hundredths grids to model the addition physically. Emphasize lining up decimal points (not right-justifying the numbers as with whole numbers). Practice with addends of different lengths (some with more decimal places than others) to reinforce trailing-zero thinking.

## Common Misconceptions
- Right-aligning numbers instead of aligning decimal points (computing 3.7 + 2.45 as if it were 37 + 245).
- Forgetting to place the decimal point in the answer.
- Not appending trailing zeros to equalize decimal lengths before computing.

## Questions

```yaml
- question: "A student computes 3.7 + 2.45 by right-aligning the digits (stacking the 5 under the 7). What is wrong with this approach?"
  type: multiple-choice
  options:
    - "Nothing is wrong — right-aligning always works for addition."
    - "It adds tenths to hundredths instead of matching each place value to its equivalent."
    - "It produces an answer that is too small by exactly 1."
    - "It only fails when one number has more digits than the other."
  answer: 1
  explanation: "Right-aligning stacks the 5 (hundredths) under the 7 (tenths), treating them as the same place value. This is like adding dimes and pennies without converting. Aligning the decimal points ensures each column contains digits from the same place value."

- question: "Rewriting 3.7 as 3.70 before adding changes the value of the number, so you is expected to adjust your final answer to compensate."
  type: true-false
  answer: false
  explanation: "Appending a trailing zero after the decimal point does not change a number's value — 3.7 and 3.70 are identical. Trailing zeros to the right of the last significant decimal digit are placeholders that make the column structure explicit without altering the quantity."

- question: "Why does lining up decimal points work as the rule for decimal addition, rather than some other alignment strategy?"
  type: short-answer
  answer: "Lining up decimal points aligns every digit with its correct place value (tenths with tenths, hundredths with hundredths, etc.), so you are always adding like units — the same reason whole-number addition requires aligning ones with ones."
  explanation: "The decimal point marks the boundary between whole-number and fractional place values. Aligning the points automatically lines up all place values on both sides. Any other alignment would mix place values, producing a wrong answer for the same reason that adding 30 + 4 by right-aligning works but adding 3.0 + 0.4 by right-aligning would not."
```

## Explainer

You already know how to add and subtract multi-digit whole numbers by stacking them and working column by column. Adding decimals uses exactly the same process — the only change is how you line up the columns. For whole numbers, right-aligning puts ones under ones automatically. For decimals, the rule is: align the decimal points, not the right edges.

The reason comes down to place value. The decimal point marks the boundary between whole-number places (to its left) and fractional places (to its right). Aligning the decimal points ensures that tenths line up with tenths, hundredths with hundredths, and so on. If you right-align 3.7 and 2.45 like whole numbers, the 7 (tenths) lands above the 5 (hundredths), and you would be adding them as if they were the same unit — like adding dimes to pennies without converting first.

The practical fix is to append trailing zeros so both numbers have the same number of decimal places, then stack. Write 3.7 as 3.70 (its value is unchanged — 3.70 and 3.7 are identical), then stack with 2.45. Now the hundredths column has 0 and 5, the tenths column has 7 and 4, and the ones column has 3 and 2. Add exactly as with whole numbers: 3.70 + 2.45 = 6.15. The decimal point in the answer drops straight down from the decimal points in the addends.

Subtraction works identically. To compute 5.3 − 1.84, rewrite 5.3 as 5.30 and then borrow and subtract column by column: 5.30 − 1.84 = 3.46. The trailing zero just makes the hundredths column explicit so you can see there is a 0 to borrow against.

Money is the most natural context for this skill: you already know intuitively that $3.70 + $2.45 = $6.15. Recognizing that all decimal arithmetic is dollar-and-cents arithmetic in disguise gives you a built-in check — if a computation produces a wildly off answer, misaligned columns are usually the culprit.
