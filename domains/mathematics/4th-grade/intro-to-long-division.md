---
id: intro-to-long-division
title: Introduction to Long Division
domain: mathematics
course: 4th-grade
prerequisites:
- id: multi-digit-multiplication
  type: hard
- id: multi-digit-subtraction
  type: hard
- id: place-value-whole-numbers
  type: hard
- id: division-as-grouping
  type: soft
- id: division-facts-within-100
  type: soft
- id: division-word-problems
  type: soft
- id: multiplication-division-relationship
  type: soft
builds-toward:
- dividing-decimals
- factors-and-multiples
tags:
- arithmetic
- division
- algorithms
stage: concrete-operations
status: validated
---
# Introduction to Long Division

## Core Idea
Long division is a procedure for dividing a multi-digit number by a one- or two-digit divisor, finding both the quotient and remainder. The algorithm works place by place from left to right: at each step you ask "how many groups of the divisor fit into this portion of the dividend?", multiply, subtract, and bring down the next digit. Division is the inverse of multiplication, so every division step can be checked by multiplying the quotient by the divisor and adding the remainder. At fourth grade, students focus on dividing up to four-digit dividends by one-digit divisors, with remainders.

## How It's Best Learned
Begin with concrete sharing situations: distribute 156 items equally among 4 groups. Use base-ten blocks to physically partition hundreds, tens, and ones. Transition to partial quotients (subtracting manageable chunks) before introducing the standard long division algorithm. Emphasizing the "divide, multiply, subtract, bring down" cycle as a repeated loop helps students see the algorithm as systematic rather than arbitrary.

## Common Misconceptions
- Not knowing where to start (which digit to divide first).
- Forgetting to bring down the next digit.
- Writing a 0 in the quotient when the divisor does not fit into the current portion -- students skip the place instead.
- Remainders larger than the divisor (indicating the quotient digit is too small).

## Questions

```yaml
- question: "When dividing 156 ÷ 4 using long division, you divide 15 by 4 and get 3 with remainder 3. What is the correct next step?"
  type: multiple-choice
  options: ["Write 3 as the final remainder and stop", "Bring down the 6 to make 36, then divide 36 ÷ 4", "Start the problem over with a different estimate", "Divide 3 ÷ 4 and record 0 in the quotient"]
  answer: 1
  explanation: "After dividing and subtracting at the tens place, you bring down the next digit (6) to join the remainder (3), forming 36. Then ask how many times 4 goes into 36 (9 times). This is the 'bring down' step in the divide–multiply–subtract–bring down cycle."

- question: "A remainder can be larger than the divisor."
  type: true-false
  answer: false
  explanation: "If the remainder is larger than the divisor, the quotient digit is too small — at least one more group could have been taken out. The remainder must always be less than the divisor; this is the check that confirms the quotient digit is correct."

- question: "How can you verify that your long division answer is correct?"
  type: short-answer
  answer: "Multiply the quotient by the divisor, then add the remainder. The result should equal the original dividend."
  explanation: "Division and multiplication are inverse operations. If 156 ÷ 4 = 39 with no remainder, then 39 × 4 must equal 156. With a remainder r, the check is: quotient × divisor + remainder = dividend. This catches both quotient errors and arithmetic slips."
```

## Explainer

Division answers the question: how many equal groups can I make? If you have 156 stickers to share equally among 4 friends, how many does each get? Long division is the systematic procedure for answering this when the numbers are too large to solve in your head.

The algorithm works from left to right, one place value at a time. Start with the leftmost digit: "How many times does 4 go into 1?" Zero times — so look at the first two digits together: "How many times does 4 go into 15?" Three times (3 × 4 = 12), with 3 left over. Write 3 in the quotient above the 5. Subtract 12 from 15 to get 3, then bring down the next digit (6) to make 36. Now ask: "How many times does 4 go into 36?" Nine times exactly (9 × 4 = 36). Write 9. The answer is 39.

The loop you repeat at every step is: **divide → multiply → subtract → bring down**. That is the entire algorithm. The "bring down" step is where students most often make mistakes — if the divisor does not fit into the current partial dividend, you must write a 0 in the quotient and bring down the next digit anyway. Skipping that 0 shifts every remaining digit and produces a wrong answer.

One rule keeps you on track: the remainder at each step must always be smaller than the divisor. If your remainder is equal to or larger than the divisor, your quotient digit was too small — try the next higher digit and redo the subtraction.

You can always verify your answer by multiplying back: quotient × divisor + remainder = dividend. If 156 ÷ 4 = 39, then 39 × 4 = 156. This check connects division back to multiplication and makes errors immediately visible.
