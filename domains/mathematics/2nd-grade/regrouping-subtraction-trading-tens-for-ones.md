---
id: regrouping-subtraction-trading-tens-for-ones
title: 'Regrouping in Subtraction: Trading Tens for Ones'
domain: mathematics
course: 2nd-grade
prerequisites:
- id: subtraction-within-20
  type: hard
- id: place-value-tens-and-ones
  type: hard
builds-toward:
- two-digit-subtraction-with-regrouping
- three-digit-subtraction-with-regrouping
tags:
- regrouping
- subtraction
- place-value
stage: concrete-operations
status: validated
---

# Regrouping in Subtraction: Trading Tens for Ones

## Core Idea
When subtracting and the ones digit of the top number is smaller than the ones digit of the bottom number, you trade one ten for ten ones. This gives you enough ones to subtract. For example, to solve 32 - 17, regroup 32 as 2 tens and 12 ones, then subtract.

## How It's Best Learned
Use base-ten blocks to show trading one ten-rod for ten unit cubes. Model the process step-by-step with multiple examples before expecting independence.

## Common Misconceptions
- Subtracting the smaller ones digit from the larger instead of regrouping.
- Regrouping but forgetting to reduce the tens place.
- Confusing this with addition regrouping.

## Questions

```yaml
- question: "To solve 43 − 18, you need to regroup. After the trade, how should the top number be represented in the written problem?"
  type: multiple-choice
  options:
    - "3 tens and 13 ones — one ten was traded for ten ones, and the tens digit reduced from 4 to 3"
    - "4 tens and 13 ones — you add ten to the ones but keep the tens digit the same"
    - "3 tens and 3 ones — you reduce both digits by one when you regroup"
    - "5 tens and 3 ones — you borrow by adding to the tens digit"
  answer: 0
  explanation: "43 starts as 4 tens and 3 ones. Since 3 < 8 (you can't subtract 8 ones from 3 ones), you trade one ten for ten ones: 4 tens → 3 tens, and 3 ones → 13 ones. The tens digit MUST drop from 4 to 3 to reflect the trade. Option B is the most common error — students add the ten to the ones column but forget to reduce the tens digit, as if the ten appeared from nowhere instead of being traded from the tens column."

- question: "Emma solves 52 − 27. In the ones column, she writes '7 − 2 = 5' (subtracting the top from the bottom since 2 < 7). In the tens column she writes '5 − 2 = 3,' and gets 35. What error did Emma make?"
  type: multiple-choice
  options:
    - "She should have subtracted the tens column first, then the ones"
    - "She subtracted the smaller digit from the larger in the ones place instead of regrouping — she flipped the subtraction so the answer would be positive"
    - "She used the wrong fact: 7 − 2 = 5 is correct, so her error must be in the tens"
    - "She regrouped correctly but forgot to update the tens digit"
  answer: 1
  explanation: "When the top ones digit (2) is smaller than the bottom ones digit (7), you cannot simply subtract in either direction and get the right answer. The correct approach is regrouping: trade a ten to get 12 ones, then compute 12 − 7 = 5 ones and 4 − 2 = 2 tens, giving 25. Emma flipped the subtraction (doing 7 − 2 instead of regrouping to do 12 − 7) — a common error that always produces wrong answers. The correct answer is 25, not 35."

- question: "When you regroup in a subtraction problem by trading one ten for ten ones, the total value of the top number changes."
  type: true-false
  answer: false
  explanation: "Regrouping is a reorganization, not a change in value. The number 32 written as '3 tens and 2 ones' represents the same quantity as '2 tens and 12 ones' — both equal 32. You are simply changing *how the number is grouped* within the place value columns, not changing the number itself. Understanding this is essential: if the value changed, subtraction wouldn't work correctly. The trade is just a bookkeeping move to create enough ones to subtract from."

- question: "After trading one ten for ten ones in a subtraction problem, you must reduce the tens digit in the written problem by 1."
  type: true-false
  answer: true
  explanation: "This step is required and is the most commonly forgotten part of regrouping. If you start with 3 tens and trade one away, you now have 2 tens — the written digit must change from 3 to 2. Skipping this step is the most common source of error: students correctly add 10 to the ones column but leave the tens digit unchanged, as if the ten came from nowhere. In written form, you cross out the original tens digit and write the reduced digit above it."

- question: "Explain in your own words what happens when you 'regroup' in a subtraction problem. Why doesn't regrouping change the value of the number?"
  type: short-answer
  answer: "Regrouping means trading one unit from a higher place value column for ten units in the next lower column — specifically, trading one ten for ten ones. The value stays the same because ten ones equals one ten; you're exchanging equivalents, not adding or removing anything. For example, 43 regroups to 3 tens and 13 ones, which still equals 43. The purpose is to create enough ones to subtract from when the ones digit in the top number is smaller than the ones digit being subtracted."
  explanation: "The concept that regrouping preserves value is the foundation for why the procedure works. If students understand this, they also understand why the tens digit must be reduced (you spent one of those tens), why you get exactly 10 extra ones (not 5 or 9 — because one ten = ten ones), and why the same logic scales to three-digit subtraction. Students who just follow steps without this understanding often forget to reduce the tens digit or apply the procedure incorrectly in new situations."
```

## Explainer

You know that every two-digit number is made of tens and ones. The number 32, for example, is 3 tens and 2 ones — think of it as three ten-sticks and two single cubes in base-ten blocks. This place value understanding is exactly what you'll use when subtraction runs into a problem.

Here's the problem: try to subtract 32 − 17. In the ones column, you need to subtract 7 from 2, but 2 is smaller than 7 — you don't have enough ones. This is where **regrouping** comes in. You trade one of your ten-sticks for ten unit cubes. Now instead of 3 tens and 2 ones, you have 2 tens and 12 ones. The total is still 32 — you haven't changed the number, just reorganized how it's grouped. Now you can subtract: 12 − 7 = 5 ones, and 2 − 1 = 1 ten. The answer is 15.

The crucial step that beginners forget is updating the tens place after the trade. You started with 3 tens, traded one away, so you now have 2 tens — the written digit in the tens column must change from 3 to 2. Skipping this step is the most common source of error. In written form, you cross out the 3 and write a small 2 above it, and write a small 1 next to the 2 in the ones column to show you now have 12 ones.

**Regrouping** in subtraction (sometimes called "borrowing") is the mirror image of regrouping in addition, where you carried a ten when ones added up past 9. Both operations are really about the structure of our number system: numbers are organized by powers of 10, and any time you need to move between columns, you exchange at a rate of 10 to 1. Understanding why the trade works — not just following the steps — is what lets you apply this to three-digit subtraction and beyond.
