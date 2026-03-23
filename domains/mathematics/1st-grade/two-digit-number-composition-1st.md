---
id: two-digit-number-composition-1st
title: Composing and Decomposing Two-Digit Numbers
domain: mathematics
course: 1st-grade
prerequisites:
- id: tens-and-ones-base-ten
  type: hard
- id: place-value-tens-and-ones
  type: hard
builds-toward:
- two-digit-addition-no-regrouping
- two-digit-subtraction-with-regrouping
tags:
- place-value
- decomposition
stage: pre-formal
status: validated
---

# Composing and Decomposing Two-Digit Numbers

## Core Idea
The number 24 can be shown as 2 tens and 4 ones, or as 20 + 4, or with 24 objects. Composing means putting tens and ones together to make a number; decomposing means breaking a number apart. This flexibility is essential for addition and subtraction algorithms.

## Questions

```yaml
- question: "Which of the following correctly shows 63 broken into tens and ones?"
  type: multiple-choice
  options:
    - "60 tens and 3 ones"
    - "6 tens and 3 ones"
    - "6 tens and 30 ones"
    - "63 tens and 0 ones"
  answer: 1
  explanation: "The digit 6 in 63 is in the tens place, meaning 6 tens (which equals 60). The digit 3 is in the ones place, meaning 3 ones. So 63 = 6 tens + 3 ones = 60 + 3. Option A confuses the digit with the number of tens — the digit 6 means 6 tens, not 60 tens."

- question: "A student wants to add 32 + 25 by thinking about tens and ones separately. What should she do first?"
  type: multiple-choice
  options:
    - "Count up from 32 to 57 one number at a time"
    - "Decompose: 32 = 30 + 2 and 25 = 20 + 5, then add tens together and ones together"
    - "Guess an answer close to 50"
    - "Memorize that 32 + 25 = 57"
  answer: 1
  explanation: "Decomposing both numbers lets you add in parts: 30 + 20 = 50 (tens), and 2 + 5 = 7 (ones), so the total is 57. This is the power of decomposition — it turns one complicated addition into two easy ones. Counting one at a time works but is slow and error-prone."

- question: "The number 40 + 7 is the same as the number 47."
  type: true-false
  answer: true
  explanation: "40 + 7 = 47. This is exactly what decomposing means — breaking the number into its tens and ones parts. 40 is 4 tens, and 7 is 7 ones. Putting them together gives 47. The number hasn't changed; we just wrote it in a different form."

- question: "Decomposing a number into tens and ones changes its value."
  type: true-false
  answer: false
  explanation: "Decomposing only changes the form — how the number is written or thought about — not its value. 47 and '4 tens + 7 ones' and '40 + 7' all represent exactly the same amount. This flexibility of representation is the point: you can switch between forms to make calculation easier without changing what the number means."

- question: "How does breaking apart 24 and 13 into tens and ones make it easier to add them together?"
  type: short-answer
  answer: "You break 24 into 20 + 4 and 13 into 10 + 3. Then add the tens: 20 + 10 = 30. Add the ones: 4 + 3 = 7. Put them together: 37. Instead of one harder problem, you solve two easy ones."
  explanation: "This is the core payoff of place-value decomposition. Students who understand why it works can apply the strategy flexibly; students who only memorize a procedure may get lost when the numbers change slightly."
```

## Explainer

You already know that numbers are built from tens and ones — that's what place value taught you. Now you're learning to move fluidly between a number and its parts. When you look at 47, you can see it two ways at once: as the single number "forty-seven," or as 4 tens and 7 ones (which is 40 + 7). **Decomposing** a number means breaking it into those parts. **Composing** means building the number back up from parts.

Think of it like a box of crayons. A box of 36 crayons is one thing — but inside, there are 3 full packs of ten and 6 loose ones. The number 36 and "3 tens, 6 ones" describe exactly the same thing, just in different ways. Being able to switch between those views is the skill you're building.

This flexibility becomes powerful when you add and subtract. Suppose you want to add 24 + 13. Instead of counting all the way from 24, you can think: "24 is 20 + 4. 13 is 10 + 3. So the tens together are 30, and the ones together are 7, which makes 37." You decomposed both numbers, added the pieces, and composed the answer — without any complicated steps. That's the payoff of knowing your tens and ones cold.
