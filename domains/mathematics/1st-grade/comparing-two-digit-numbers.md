---
id: comparing-two-digit-numbers
title: Comparing Two-Digit Numbers
domain: mathematics
course: 1st-grade
prerequisites:
- id: place-value-tens-and-ones
  type: hard
builds-toward:
- ordering-numbers-to-20
tags:
- comparison
- inequalities
stage: pre-formal
status: validated
---

# Comparing Two-Digit Numbers

## Core Idea
Comparing two-digit numbers uses place value: compare tens first; if tens are equal, compare ones. The symbols <, >, and = express relationships between numbers precisely.

## Questions

```yaml
- question: "A student compares 73 and 69 by looking at the ones digits first: 3 < 9, so she concludes 69 > 73. What went wrong?"
  type: multiple-choice
  options:
    - "She should have compared the tens first; 7 tens > 6 tens, so 73 > 69"
    - "She should have added all digits: 7+3=10, 6+9=15, so 69 is larger"
    - "She was correct; 3 is less than 9, so 73 is smaller"
    - "The comparison doesn't work for numbers with different ones digits"
  answer: 0
  explanation: "Tens are compared first because the tens digit determines roughly how large a number is. 73 has 7 tens and 69 has only 6 tens — since 7 tens (70) is greater than 6 tens (60), we know 73 > 69 without even looking at the ones. The ones digit only matters when the tens digits are equal."

- question: "Two numbers both have 5 tens. One has 8 ones; the other has 2 ones. Which is greater?"
  type: multiple-choice
  options:
    - "The number with 2 ones, because 2 is the first ones digit you see and you compare left to right"
    - "The number with 8 ones, because when tens are equal, the ones digit decides"
    - "They are equal because they both have 5 tens"
    - "You cannot compare them without knowing the complete two-digit numbers"
  answer: 1
  explanation: "When the tens digits are equal, we move to the ones place to break the tie. 58 and 52 both have 5 tens — so we compare the ones: 8 ones > 2 ones, therefore 58 > 52. Option C is the classic trap: equal tens does not mean equal numbers."

- question: "When comparing 48 and 51, you should look at both the tens digit and the ones digit to determine which number is greater."
  type: true-false
  answer: false
  explanation: "Only the tens digits are needed here. 51 has 5 tens and 48 has only 4 tens — since 5 tens > 4 tens, 51 > 48 without any need to examine the ones digits. You only need the ones when the tens are equal."

- question: "In the number 67, the digit 6 represents a greater value than the digit 7."
  type: true-false
  answer: true
  explanation: "The digit 6 is in the tens place, meaning it represents 60. The digit 7 is in the ones place, meaning it represents 7. Even though 7 > 6 as raw digits, their place values reverse the comparison: 60 >> 7. This is exactly why we always compare tens first."

- question: "Explain why the tens digit is compared first when comparing two-digit numbers, rather than looking at both digits at once."
  type: short-answer
  answer: "The tens digit represents groups of ten, so it captures the bulk of each number's value. One group of ten (10) is always larger than any number of ones (at most 9), so whoever has more tens has the larger number — regardless of the ones. The ones digit is a tiebreaker that only matters when both numbers have the same number of tens."
  explanation: "Understanding this requires seeing digits as place-value quantities, not just symbols. 7 in the tens place means 70; 9 in the ones place means 9. 70 > 9, which is why the tens comparison dominates. Students who compare 'digit by digit' without this understanding often make errors on pairs like 73 vs. 69 or 81 vs. 97."
```

## Explainer

From your work on place value with tens and ones, you know that a two-digit number like 47 is not just a pair of digits side by side — it means 4 tens and 7 ones, which is 40 + 7 = 47. That understanding of what the digits *represent* is exactly the tool you need for comparing two-digit numbers. Comparison is really just asking: which number represents more?

Here is the key rule: **always look at the tens place first**. The tens digit tells you roughly how big the number is. If one number has more tens than another, it is bigger — no matter what the ones digits are. For example, 63 is greater than 59, because 6 tens is more than 5 tens. You do not even need to look at the 3 and 9. Six groups of ten beats five groups of ten every time.

The ones digit only matters when the tens digits are the same. If you have 47 and 43, both have 4 tens — so the tens cannot settle the comparison. Now you look at the ones: 7 ones vs. 3 ones. Since 7 is more than 3, the number 47 is greater than 43. Think of it like a footrace: if two runners are on the same lap, you look at how far around the track they are. But if they are on different laps, the lap number settles it first.

The symbols <, >, and = are just shorthand for these relationships. The **>** symbol points left toward the bigger number (47 > 43), the **<** symbol points right toward the bigger number (43 < 47), and **=** means both sides are exactly the same amount (45 = 45). A helpful memory trick: the open mouth of the symbol always faces the bigger number, like it wants to eat the larger amount. Practice reading comparison statements aloud — "47 is greater than 43," "43 is less than 47" — so the symbols feel connected to real meaning rather than arbitrary marks.
