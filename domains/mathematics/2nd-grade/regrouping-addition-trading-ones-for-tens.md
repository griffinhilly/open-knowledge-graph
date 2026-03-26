---
id: regrouping-addition-trading-ones-for-tens
title: 'Regrouping in Addition: Trading Ones for Tens'
domain: mathematics
course: 2nd-grade
prerequisites:
- id: addition-within-20
  type: hard
- id: place-value-tens-and-ones
  type: hard
builds-toward:
- two-digit-addition-with-regrouping
- three-digit-addition-with-regrouping
tags:
- regrouping
- place-value
- addition
stage: concrete-operations
status: validated
---

# Regrouping in Addition: Trading Ones for Tens

## Core Idea
Regrouping is the process of combining ten individual ones into one ten. When adding, if you have 10 or more ones, you bundle them into a new ten and record the leftover ones. For example, 17 ones becomes 1 ten and 7 ones.

## How It's Best Learned
Use bundles of ten sticks or base-ten blocks to physically show this trading. Have students practice bundling 10 ones repeatedly until the concept is automatic.

## Common Misconceptions
- Misunderstanding what the regrouped ten represents.
- Writing the regrouped number in the wrong place.
- Forgetting to add the regrouped ten.

## Questions

```yaml
- question: "When solving 47 + 35, a student correctly gets 12 in the ones column, writes 2 in the ones place, and carries a '1' to the tens column. What does that carried '1' actually represent?"
  type: multiple-choice
  options:
    - "The digit 1, written as a reminder symbol so the student doesn't forget"
    - "A new ten created by bundling 10 of the 12 ones together"
    - "The number of tens that were already in 47"
    - "The difference between 12 ones and the 2 that was written down"
  answer: 1
  explanation: "The carried '1' is not a notation trick or a reminder — it represents a real ten. When you add 7 + 5 = 12, you have 12 loose ones. You bundle 10 of them into one rod (a ten), leaving 2 singles. That bundle is a real ten that must be counted in the tens column. This is why forgetting to add the carried ten is such a costly error: you literally lose a whole ten from your answer."

- question: "A student adds 56 + 37. She adds the ones: 6 + 7 = 13. She writes '1' in the tens column and '3' in the ones column, then adds the tens as 5 + 3 = 8, ignoring the carried digit. Her answer is 83. What is correct?"
  type: multiple-choice
  options:
    - "83 is correct — the carried digit just marks the ones column answer"
    - "The correct answer is 93; she forgot to add the carried ten to the tens column (5 + 3 + 1 = 9)"
    - "The correct answer is 103; she should have carried a 1 to the hundreds column too"
    - "The correct answer is 83; carrying only applies when the ones sum exceeds 15"
  answer: 1
  explanation: "The student correctly identified that she needed to carry, but then forgot to add the carried ten when computing the tens column. The tens column should be 5 + 3 + 1 (carried) = 9, giving 93, not 83. This is the 'forgetting to add the regrouped ten' error — the carried digit is a real ten that must participate in the tens-column addition."

- question: "The digit you carry in addition represents a real ten, not just a notation symbol."
  type: true-false
  answer: true
  explanation: "The carry is a physical trade: you exchanged 10 loose ones for one bundled ten, and that ten must now be added in the tens column. Thinking of it as 'just a little 1 you write on top' leads to forgetting it or writing it in the wrong place. Understanding that the carry is a real quantity — a ten you just created — is the conceptual anchor that makes regrouping reliable."

- question: "You mainly need to carry (regroup) when the ones column sum is exactly 10."
  type: true-false
  answer: false
  explanation: "You carry whenever the ones column sum is 10 or more — that is, when you have 10, 11, 12, 13, 14, 15, 16, 17, or 18 ones (the maximum possible when adding two single digits). Any time you have 10 or more ones, you can bundle 10 of them into a new ten, write the remainder in the ones place, and carry the ten. The threshold is '10 or more,' not 'exactly 10.'"

- question: "When you add 8 + 5 in the ones column and write '3, carry 1,' where does that carried '1' come from and why does it belong in the tens column?"
  type: short-answer
  answer: "8 + 5 = 13 ones. You bundle 10 of those ones into a single ten (that's the carry), and 3 ones are left over (that's the digit in the ones place). The ten you just created belongs in the tens column because the tens column tracks groups of ten — and you now have a new group of ten that must be counted there."
  explanation: "This is the place value logic underneath regrouping. The ones column can only hold the count of individual ones (0–9). When you exceed 9, you must trade up: 10 ones become 1 ten, which moves to the tens column. Carrying records this trade in writing. Students who see regrouping as a procedure ('write the smaller digit, carry the bigger one') without this conceptual grounding tend to make positional errors."
```

## Explainer

You already understand place value: the tens place and the ones place. A number like 34 means 3 tens and 4 ones — not "thirty-four random dots," but a specific, organized structure. You also know addition facts up to 20. Regrouping is what happens when those two ideas collide: you're adding ones, and you end up with more than 9 of them.

Think about base-ten blocks. You have a pile of individual unit cubes (ones) and a pile of rods (each rod = 10 cubes bundled together). When you add 8 ones to 5 ones, you get 13 ones. But 13 loose cubes is messy and hard to compare with other numbers. So you **trade** 10 of those cubes for a single rod: now you have 1 rod and 3 cubes — that's 1 ten and 3 ones, or 13. This physical swap is exactly what the written "carry" notation records.

Here's what it looks like in a problem: 28 + 35. You add the ones column: 8 + 5 = 13. You can't write "13" in the ones place — that would put a 1 in the wrong column. Instead, you write the 3 in the ones place (the leftover after trading) and **carry** the 1 to the tens column (the new ten you just created). Then you add the tens: 1 + 2 + 3 = 6 tens. The answer is 63.

The "1" you carry is not just a reminder symbol — it represents a real ten that you created by bundling up 10 ones. This is why the "forgetting to add the regrouped ten" mistake is so costly: you literally lose a ten from your answer. Every time you carry, picture yourself handing that bundled rod to the tens column. Regrouping is not a trick — it's the place value system doing exactly what it was designed to do: keep ones with ones and tens with tens so big numbers stay organized.
