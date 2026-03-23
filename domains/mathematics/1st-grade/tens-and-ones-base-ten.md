---
id: tens-and-ones-base-ten
title: Tens and Ones Place Value
domain: mathematics
course: 1st-grade
prerequisites:
- id: place-value-tens-and-ones
  type: hard
- id: number-bonds-to-10
  type: soft
builds-toward:
- place-value-whole-numbers
- three-digit-number-forms
tags:
- place-value
- base-ten
- decomposition
stage: pre-formal
status: validated
---

# Tens and Ones Place Value

## Core Idea
In the number 17, the 1 represents one ten (10), and the 7 represents seven ones. Understanding this structure is crucial for multi-digit addition, subtraction, and later multiplication. Numbers are composed of groups of ten and leftover ones.

## How It's Best Learned
Use base-ten blocks or bundles of ten sticks with loose ones. Bundle objects to show 'this is one ten' vs. 'these are ten ones.' Repeatedly model and let students physically create two-digit numbers.

## Common Misconceptions
- Seeing digits as separate (the 1 and 7 in 17 are just two numbers, not one ten and seven ones).
- Not understanding that 10 ones equals 1 ten; they're the same quantity in different forms.
- Thinking place value is only about position, not about actual quantities.

## Questions

```yaml
- question: "In the number 35, what is the value of the digit 3?"
  type: multiple-choice
  options:
    - "3 — it just means three"
    - "30 — it represents three tens"
    - "300 — it represents three hundreds"
    - "The value depends on which digit comes next"
  answer: 1
  explanation: "The 3 in 35 is in the tens place, so it means three tens, which equals 30. The digit 3 by itself means 'three,' but its position in a number is what determines its actual value. This is the heart of place value: the same digit means different amounts depending on where it sits in the number."

- question: "A student says: '17 is made of the numbers 1 and 7, so it equals 1 + 7 = 8.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — 17 is indeed 1 plus 7"
    - "The 1 represents one ten (10), not just one, so 17 = 10 + 7 = 17"
    - "You should multiply: 1 × 7 = 7"
    - "The order of digits doesn't matter in addition"
  answer: 1
  explanation: "The student is treating each digit as its face value and ignoring position. The 1 in 17 is in the tens place, so it represents one ten (the value 10), not just the number 1. The correct decomposition is 17 = 10 + 7. This is the classic misconception: seeing digits as isolated numbers rather than as place-value representations."

- question: "In the number 71, the digit 7 has a smaller value than the digit 7 in the number 17."
  type: true-false
  answer: false
  explanation: "The 7 in 71 is in the tens place, giving it a value of 70. The 7 in 17 is in the ones place, giving it a value of 7. So the 7 in 71 is actually ten times larger. This illustrates why position matters so much — the same digit 7 can represent 7 or 70 or 700 depending on its place in the number."

- question: "Ten individual unit blocks can be traded for one ten-rod without changing the total amount."
  type: true-false
  answer: true
  explanation: "Ten ones and one ten represent exactly the same quantity — they are just packaged differently. A ten-rod is literally made of ten units fused together. This equivalence (10 ones = 1 ten) is the core mechanical insight that makes regrouping in addition and subtraction possible. Understanding that you can trade between forms without changing the total is what makes borrowing and carrying make sense."

- question: "Why does the position of a digit in a number matter? Why isn't the digit 3 always just worth 3?"
  type: short-answer
  answer: "In our base-ten system, each position has a different value. The ones place is worth 1, the tens place is worth 10, and the hundreds place is worth 100. A digit in any position is multiplied by that position's value. So 3 in the ones place = 3, but 3 in the tens place = 30, and 3 in the hundreds place = 300. Without position mattering, numbers like 35 and 53 would be the same, which they clearly are not."
  explanation: "This is the fundamental principle of positional notation, the system that underlies all of our arithmetic. Understanding it converts numbers from memorized symbols into meaningful structures that can be decomposed, compared, and operated on with understanding."
```

## Explainer

When you learned number bonds to 10, you discovered that 10 ones can be grouped into a single bundle. **Place value** takes that idea and turns it into the organizing principle of our entire number system. In the number 17, the digit 1 does not mean "one" — it means **one ten**, which is a bundle of ten ones. The digit 7 means seven separate ones. So 17 is really 10 + 7, two quantities combined into one compact symbol.

The position of a digit is what gives it meaning. A digit in the **ones place** tells how many loose units there are. A digit in the **tens place** tells how many groups of ten there are. This is why the number 71 is so different from 17, even though both use the same digits — in 71, the 7 is in the tens place (seven groups of ten = 70) and the 1 is in the ones place (one unit). Position, not just the digit itself, carries the meaning.

Base-ten blocks make this concrete: a long "ten-rod" represents one group of ten, and small unit cubes represent ones. To build 34 with blocks, you would take 3 ten-rods and 4 unit cubes. You could also make 34 with 34 individual cubes — same quantity, different form. The key insight is that **ten ones and one ten are identical in value**, just packaged differently. Being able to repackage numbers this way is exactly what you'll need for addition and subtraction with regrouping.

Every two-digit number from 10 to 99 follows this structure: a tens digit and a ones digit. Even the teen numbers, which can feel irregular, fit the pattern — 13 is one ten and three ones, 19 is one ten and nine ones. Seeing every two-digit number as a tens-part plus a ones-part transforms arithmetic from memorizing answers into understanding structure.
