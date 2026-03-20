---
id: comparing-decimals
title: Comparing and Ordering Decimals
domain: mathematics
course: 5th-grade
prerequisites:
- id: decimal-place-value
  type: hard
- id: comparing-ordering-whole-numbers
  type: soft
- id: comparing-fractions
  type: soft
- id: relating-fractions-and-decimals
  type: soft
- id: reading-writing-decimals
  type: soft
builds-toward:
- rounding-decimals
- adding-subtracting-decimals
tags:
- decimals
- comparison
- number-sense
stage: concrete-operations
status: validated
---
# Comparing and Ordering Decimals

## Core Idea
Comparing decimals uses the same left-to-right, place-by-place strategy as comparing whole numbers, but students must resist the temptation to judge by the number of digits. 0.5 > 0.38 because 5 tenths > 3 tenths, even though 38 > 5 as whole numbers. Appending trailing zeros (rewriting 0.5 as 0.50) can make comparisons clearer by aligning place values. Students should be able to compare any two decimals through thousandths using <, >, and =, and order sets of decimals from least to greatest or greatest to least.

## How It's Best Learned
Use place-value charts side by side, comparing digit by digit from left to right. 10x10 grids (hundredths grids) make the comparison visual. Practice with carefully chosen pairs: same whole-number part but different decimal parts, different lengths, trailing zeros. Always connect back to the meaning: "5 tenths versus 3 tenths and 8 hundredths."

## Common Misconceptions
- Thinking longer decimals are always larger (0.125 > 0.9 because 125 > 9).
- Thinking shorter decimals are always larger (the opposite error, overgeneralizing that "fewer places means bigger").
- Not recognizing that trailing zeros do not change value (0.50 = 0.5).

## Questions

```yaml
- question: "Which decimal is greater: 0.4 or 0.35?"
  type: multiple-choice
  options:
    - "0.35 — because 35 is greater than 4"
    - "0.4 — because 4 tenths is greater than 3 tenths"
    - "They are equal — both have digits in the tenths and hundredths places"
    - "0.35 — because it has more decimal digits"
  answer: 1
  explanation: "Compare digit by digit from left to right. Both numbers have 0 in the ones place (tied). In the tenths place, 0.4 has a 4 and 0.35 has a 3. Since 4 tenths > 3 tenths, 0.4 is larger — the comparison is decided right there, before we even look at the hundredths. Option A is the classic mistake: treating the decimal digits as a whole number (35 > 4) and ignoring place value."

- question: "A student argues: '0.125 must be bigger than 0.9 because 125 is much greater than 9.' How do you respond?"
  type: multiple-choice
  options:
    - "The student is correct — 125 > 9, so 0.125 > 0.9"
    - "The student is wrong — 0.9 is greater because 9 tenths > 1 tenth, and the comparison ends at the tenths place"
    - "You need to find a common denominator before you can compare"
    - "They are equal because both are less than 1"
  answer: 1
  explanation: "The student is applying the 'longer means bigger' misconception. Compare by place value: in the tenths place, 0.9 has 9 and 0.125 has 1. Since 9 tenths > 1 tenth, 0.9 is larger immediately. Rewriting both with trailing zeros confirms: 0.900 vs. 0.125 — 900 thousandths vs. 125 thousandths. The number of decimal digits is irrelevant; only the place value of the first differing digit determines which is larger."

- question: "A decimal with more digits after the decimal point is always greater than a decimal with fewer digits."
  type: true-false
  answer: false
  explanation: "This is one of the two most common decimal misconceptions. 0.9 has one decimal place; 0.125 has three. Yet 0.9 > 0.125, because 9 tenths > 1 tenth. The number of digits after the decimal point tells you the smallest place value represented, not the size of the number. Only the leftmost differing digit determines which decimal is larger."

- question: "Rewriting 0.5 as 0.50 changes the value of the number."
  type: true-false
  answer: false
  explanation: "Trailing zeros after the last nonzero decimal digit do not change the value. 0.50 means '50 hundredths,' and 50 hundredths = 5 tenths = 0.5. The value is identical. Appending trailing zeros is a useful technique for comparing decimals because it aligns place values and makes the comparison look like a whole-number comparison (e.g., 0.50 vs. 0.38 becomes '50 hundredths vs. 38 hundredths')."

- question: "Why can't you compare decimals simply by treating all the digits after the decimal point as a whole number (e.g., concluding that 0.125 > 0.9 because 125 > 9)?"
  type: short-answer
  answer: "Because the digits after the decimal point represent different place values (tenths, hundredths, thousandths), not a single number. 0.9 means 9 tenths, and 0.125 means 1 tenth + 2 hundredths + 5 thousandths. The first decimal digit represents tenths for both, so you compare those first. Comparing '125 vs. 9' ignores place value entirely — it is like comparing the number 125 to 9 when you should be comparing 900 thousandths to 125 thousandths."
  explanation: "The left-to-right, place-by-place strategy works because each position has a fixed, decreasing value (tenths > hundredths > thousandths). Once you find the first place where the digits differ, the comparison is decided — everything to the right is irrelevant, just as when comparing 847 and 823 you know 847 > 823 as soon as you see the tens digits (4 > 2)."
```

## Explainer

You've learned how the decimal place-value system works — tenths, hundredths, thousandths extending the whole-number system to the right of the decimal point — and you know how to read and write decimals. You've also compared whole numbers before. Comparing decimals uses the exact same strategy as comparing whole numbers: start from the leftmost digit and work right until you find a place where the digits differ.

The algorithm is: align the decimal points, then compare digit by digit from left to right. For 0.5 and 0.38, the tenths digits are 5 vs. 3. Since 5 > 3, we know 0.5 > 0.38 immediately — the hundredths digit of 0.38 is irrelevant because the comparison was already decided at the tenths place. A useful technique is **appending trailing zeros**: rewrite 0.5 as 0.50 so both numbers have digits in the same place-value positions. Now the comparison reads "50 hundredths versus 38 hundredths," which looks exactly like comparing 50 and 38 as whole numbers. The trailing zero doesn't change the value, but it makes the alignment visible and explicit.

The most seductive mistake is judging by digit count: "0.125 has three decimal places, so it must be bigger than 0.9 which has only one." This reverses the truth. Rewrite 0.9 as 0.900 — that's 900 thousandths versus 125 thousandths. The connection to your prerequisite on fractions and decimals makes this concrete: 0.9 = 9/10 and 0.125 = 125/1000. Converting to a common denominator (thousandths) gives 900/1000 vs. 125/1000 — 0.9 is clearly larger. The number of digits after the decimal point tells you nothing about size on its own; only the place-value of the leading differing digit matters.

Ordering a set of decimals from least to greatest follows the same logic extended to multiple numbers: compare whole-number parts first (any decimal ≥ 1 is greater than any decimal < 1), then tenths, then hundredths, and so on until all ties are broken. Numbers that differ only in trailing zeros are equal (0.50 = 0.500 = 0.5). Fluency here supports every operation with decimals that follows — adding, subtracting, rounding, multiplying — because all of them depend on understanding what the digits in each place actually represent.
