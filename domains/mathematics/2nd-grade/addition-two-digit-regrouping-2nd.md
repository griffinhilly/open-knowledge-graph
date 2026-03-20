---
id: addition-two-digit-regrouping-2nd
title: Two-Digit Addition With Regrouping
domain: mathematics
course: 2nd-grade
prerequisites:
- id: two-digit-addition-no-regrouping-2nd
  type: hard
- id: regrouping-addition-trading-ones-for-tens
  type: hard
builds-toward:
- addition-three-digit-numbers-2nd
tags:
- addition
- two-digit
- regrouping
- carrying
stage: concrete-operations
status: draft
---

# Two-Digit Addition With Regrouping

## Core Idea
When ones sum to 10 or more, regroup 10 ones as 1 ten. In 27 + 15: ones sum to 12 (regroup as 1 ten + 2 ones), then add tens (2 + 1 + 1 = 4 tens), yielding 42. Regrouping preserves place value.

## Questions

```yaml
- question: "A student solves 38 + 47. In the ones column, they get 8 + 7 = 15 and write '15' in the ones place. What should they do instead?"
  type: multiple-choice
  options:
    - "Writing 15 is correct — the ones column can hold any sum"
    - "Write 5 in the ones place and carry 1 to the tens column, because 15 ones = 1 ten and 5 ones"
    - "Add only 5 and drop the 1 entirely"
    - "Start over using a different method"
  answer: 1
  explanation: "The ones place can only hold a single digit (0–9). When the ones sum is 15, that's really 1 ten + 5 ones. You write the 5 in the ones place and carry the 1 ten over to the tens column, where it will be added with the other tens. Writing '15' in the ones column is a place-value error — it misrepresents the number."

- question: "When you 'carry' a 1 to the tens column during addition, what does that 1 actually represent?"
  type: multiple-choice
  options:
    - "One leftover one that wasn't needed"
    - "One ten — because 10 ones were traded for 1 ten"
    - "A correction for an addition mistake"
    - "One hundred, because you're moving to the next column"
  answer: 1
  explanation: "The carried digit is always 1 ten, not 1 one. When the ones sum reaches 10 or more, you've accumulated enough ones to form a complete ten. Trading 10 ones for 1 ten is an equal exchange — nothing is added or removed — and that 1 ten gets placed in the tens column. Understanding what the carried digit represents is what makes regrouping make sense rather than just being a mysterious rule."

- question: "Regrouping in addition does not change the total — it just reorganizes the same amount in a different way."
  type: true-false
  answer: true
  explanation: "Regrouping is an equal trade: 10 ones and 1 ten are exactly the same value. When you carry, you're converting between equivalent forms of the same number, not adding anything extra. The total remains the same — only the representation changes."

- question: "When you carry a digit to the tens column, the total you are calculating gets larger because you are adding an extra number."
  type: true-false
  answer: false
  explanation: "Carrying does not increase the total. The carried 1 represents a ten that was already part of the ones sum — it is being moved to the correct column, not added from outside the problem. Regrouping is a reorganization, not an addition."

- question: "Explain in your own words why you 'carry' when adding two-digit numbers. What does the carried number actually represent?"
  type: short-answer
  answer: "You carry because the ones column can only hold a single digit. When the ones sum reaches 10 or more, you have made a full ten. The carried '1' represents that one ten, which gets moved to the tens column to be counted with the other tens. It's like trading 10 pennies for 1 dime — the value is the same."
  explanation: "The key is understanding that the carried digit is not a bonus — it is part of the ones sum, just reorganized into its correct place-value column. This same logic extends to every column in addition: whenever a column's sum reaches 10, you trade 10 of that unit for 1 of the next larger unit and carry it left."
```

## Explainer

You already know how to add two-digit numbers when the ones column stays under 10 — add ones to ones, tens to tens, and you're done. But what happens when the ones column produces a sum of 10 or more? That's exactly what regrouping solves.

Think of it using what you know about place value: the ones place can only hold a single digit (0–9). When your ones sum reaches 10, you've actually made a brand-new ten — so you trade those 10 ones for 1 ten and carry it over to the tens column. This is sometimes called **carrying**, and it's just another way of saying: "I've accumulated enough ones to fill a tens cup, so I'll move it over."

Take 27 + 15 as an example. Start with the ones: 7 + 5 = 12. Since 12 is bigger than 9, you can't write "12" in the ones column — there's only room for one digit. Instead, you write the 2 in the ones place and carry the 1 (which stands for 1 ten) up to the tens column. Now the tens column reads 2 + 1 + 1 (the carried ten) = 4. So the answer is 42.

The key insight is that regrouping doesn't change the total — it just reorganizes how the total is expressed. 12 ones is exactly the same amount as 1 ten and 2 ones; you're not adding or removing anything. Every time you carry, you're simply converting between equivalent forms. This same idea — trading 10 of a smaller unit for 1 of the next unit up — will power every column of addition you'll ever do, from three-digit numbers all the way to millions.
