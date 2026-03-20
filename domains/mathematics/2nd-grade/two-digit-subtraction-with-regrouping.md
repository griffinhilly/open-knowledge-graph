---
id: two-digit-subtraction-with-regrouping
title: Two-Digit Subtraction with Regrouping
domain: mathematics
course: 2nd-grade
prerequisites:
- id: two-digit-addition-with-regrouping
  type: soft
- id: subtraction-within-20
  type: hard
- id: place-value-tens-and-ones
  type: hard
builds-toward:
- subtraction-within-100
- three-digit-subtraction
- multi-digit-subtraction
tags:
- subtraction
- regrouping
- borrowing
- place-value
stage: concrete-operations
status: validated
---

# Two-Digit Subtraction with Regrouping

## Core Idea
When the ones digit we are subtracting is larger than the ones digit we are subtracting from, we need to regroup — trading 1 ten for 10 ones. For example, 53 − 27 requires regrouping in the ones column because 3 < 7: we borrow a ten, making the ones 13, and the tens column becomes 4. The total value of the number does not change; we are just representing it differently.

## How It's Best Learned
Start with base-ten blocks to show physically breaking apart a tens rod into 10 ones. Use the 'can I subtract?' check on the ones column as a decision-making habit. Compare with the counting-up strategy (counting up from 27 to 53 on a number line) so students see multiple valid methods.

## Common Misconceptions
- Subtracting the smaller digit from the larger regardless of position (e.g., computing 53 − 27 as 34 by doing 7 − 3 in ones).
- Forgetting to reduce the tens column after regrouping.
- Confusing regrouping in subtraction with regrouping in addition.

## Questions

```yaml
- question: "A student computes 63 − 28 and gets 45, writing '8 − 3 = 5' in the ones column and '6 − 2 = 4' in the tens column. What error did they make?"
  type: multiple-choice
  options:
    - "They subtracted the bottom digit from the top digit in the ones column regardless of which was larger"
    - "They forgot to carry a value into the tens column"
    - "They subtracted in the wrong order — tens before ones"
    - "They made an arithmetic error in the tens column"
  answer: 0
  explanation: "The student swapped the subtraction in the ones column: instead of computing 3 − 8 (which requires regrouping), they computed 8 − 3 = 5. This 'subtract the smaller from the larger' error is the most common mistake in two-digit subtraction. The correct approach is to recognize that 3 < 8, regroup (trade 1 ten for 10 ones), then compute 13 − 8 = 5 in ones and 5 − 2 = 3 in tens, giving 35."

- question: "In the problem 53 − 27, after regrouping the tens column changes from 5 tens to 4 tens. Why?"
  type: multiple-choice
  options:
    - "You traded 1 ten for 10 ones so the ones column has enough to subtract from, leaving one fewer ten"
    - "You subtracted 1 from the tens column as the first step of finding the answer"
    - "The tens digit decreases whenever the ones digit in the subtrahend is larger"
    - "It is a procedural step with no connection to the value of the number"
  answer: 0
  explanation: "Regrouping means making an exchange: 1 ten is traded for 10 ones. The 53 is re-expressed as 4 tens and 13 ones — still the same total value, just represented differently. This exchange is why the tens column shows one fewer ten after regrouping. Understanding the exchange (not just the procedure) helps students catch the most common post-regrouping error: forgetting to reduce the tens digit before subtracting in the tens column."

- question: "After regrouping in a subtraction problem, the total value of the number you started with has not changed — only how it is represented has changed."
  type: true-false
  answer: true
  explanation: "Regrouping is an exchange, not a removal: 1 ten becomes 10 ones, so 53 becomes '4 tens + 13 ones,' which still equals 53. The total is preserved. This is why regrouping works: it rearranges the same quantity into a form that allows digit-by-digit subtraction. Students who don't grasp this sometimes think they are 'taking' something from the number, which can lead to confusion about why the tens digit must be updated."

- question: "When solving a two-digit subtraction problem with regrouping, you should check the tens column first to decide whether regrouping is needed."
  type: true-false
  answer: false
  explanation: "Always check the ones column first. Regrouping is triggered by a ones-column problem (the bottom ones digit is larger than the top ones digit), not by anything in the tens column. The useful habit is: before subtracting ones, ask 'Can I subtract?' If yes, proceed. If no, regroup first — borrow a ten, update the tens digit, then subtract. Checking the tens column first leads students to start subtracting there prematurely or to miss the need for regrouping entirely."

- question: "Explain why regrouping (borrowing a ten) does not change the total value of the number, even though it changes the digits."
  type: short-answer
  answer: "Regrouping is an exchange based on the fact that 1 ten equals exactly 10 ones. When we regroup, we break apart one ten and add 10 to the ones column — the quantity is rearranged but not changed. For example, 53 can be expressed as 5 tens and 3 ones, or as 4 tens and 13 ones. Both representations equal 53. This is the same principle underlying place value: different combinations of tens and ones can represent the same total."
  explanation: "This understanding is what separates students who genuinely grasp regrouping from those who have only memorized the steps. If a student knows WHY the tens digit drops by 1, they will remember to update it — and they won't confuse regrouping in subtraction with regrouping in addition (where 10 ones bundle into a new ten, going the other direction)."
```

## Explainer

You already know place value — that a two-digit number like 53 is made of 5 tens and 3 ones. You also know how to subtract within 20. **Regrouping** (sometimes called borrowing) is what happens when those two skills meet a problem they cannot handle separately: there are not enough ones to subtract from.

Consider 53 − 27. Start with the ones column: can you subtract 7 from 3? No, because 3 is too small. So you **regroup** — you trade one of the tens for 10 ones. The 5 tens becomes 4 tens, and the 3 ones becomes 13 ones. Now you can subtract: 13 − 7 = 6 in the ones place. Then subtract the tens: 4 − 2 = 2. The answer is 26. Crucially, the total value of 53 never changed — you just re-expressed it as 4 tens and 13 ones instead of 5 tens and 3 ones.

This mirrors what you learned in addition with regrouping, but in reverse. In addition, 10 or more ones bundled up into a new ten. In subtraction, a ten unbundles into 10 ones when you need them. The place-value structure allows both kinds of exchange because 1 ten always equals 10 ones exactly.

A useful habit: before subtracting, look at the ones column first. Ask "can I subtract?" If yes, proceed. If no, regroup first, then subtract. After regrouping, always update the tens digit — it drops by 1 — before continuing to the tens column. Forgetting that update is the most common error in the whole procedure.

