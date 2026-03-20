---
id: three-digit-subtraction
title: Three-Digit Subtraction
domain: mathematics
course: 2nd-grade
prerequisites:
- id: subtraction-within-100
  type: hard
- id: three-digit-addition
  type: soft
- id: mental-math-add-subtract-hundreds
  type: soft
builds-toward:
- multi-digit-subtraction
- two-step-word-problems
tags:
- subtraction
- three-digit
- regrouping
- borrowing
stage: concrete-operations
status: validated
---

# Three-Digit Subtraction

## Core Idea
Subtracting three-digit numbers extends borrowing to three columns: subtract ones (borrow from tens if needed), subtract tens (borrow from hundreds if needed), then subtract hundreds. Some problems require borrowing across a zero — for example, 400 − 163 requires borrowing from the hundreds when the tens digit is zero. Checking answers by adding (result + subtrahend = minuend) reinforces the addition-subtraction relationship.

## How It's Best Learned
Spend extra time on the 'borrowing across zero' case using base-ten blocks. Have students use addition to check every subtraction answer. Estimation before computing ('about 240') helps catch large errors.

## Common Misconceptions
- Subtracting the smaller digit from the larger regardless of which is on top.
- Errors when borrowing across a zero in the tens place (e.g., in 400 − 163, forgetting that borrowing from the hundreds gives the tens 9, not 10).
- Not reducing the column borrowed from.

## Questions

```yaml
- question: "In solving 300 − 154, after borrowing from the hundreds because the tens digit is 0, what value should appear in the tens column before performing the tens subtraction?"
  type: multiple-choice
  options:
    - "10 — borrowing one hundred gives ten tens, and the tens column now holds 10"
    - "9 — after giving one of those tens to the ones column, the tens column holds 9"
    - "0 — the tens column started at 0 and nothing changed"
    - "1 — because exactly one ten was borrowed from the hundreds"
  answer: 1
  explanation: "Borrowing across a zero requires two steps. First, borrow from the hundreds: the hundreds drop by 1 and the tens gain 10. Second, borrow one of those tens for the ones column: the tens drop from 10 to 9, and the ones gain 10. The tens column ends up with 9, not 10. Students who skip the second step and leave 10 in the tens column get the wrong answer in the tens subtraction."

- question: "How can you verify that 783 − 248 = 535 is correct without redoing the subtraction?"
  type: multiple-choice
  options:
    - "Check that each digit in 535 is smaller than the corresponding digit in 783"
    - "Add 535 + 248 and confirm the result equals 783"
    - "Subtract 535 − 248 and check that the result is 0"
    - "Round both numbers to the nearest hundred and compare"
  answer: 1
  explanation: "Subtraction and addition are inverse operations — subtracting a number and then adding it back should return you to the original. So result + subtrahend = minuend is always true for a correct subtraction. Adding 535 + 248 = 783 confirms the answer. This strategy works for numbers of any size and reinforces the relationship between the two operations."

- question: "When solving a problem like 400 − 163, you can borrow directly from the tens column to handle the ones column because borrowing is always done from the column immediately to the left."
  type: true-false
  answer: false
  explanation: "When the tens digit is 0, there is nothing to borrow from the tens column. You must first borrow from the hundreds: hundreds decrease by 1 and tens gain 10. Then borrow one of those tens for the ones column, leaving the tens with 9. Blindly going to the adjacent column without checking whether it has anything to lend is the most common source of error in three-digit subtraction."

- question: "Adding your subtraction answer back to the number you subtracted should always equal the original starting number — this is a reliable check for any subtraction."
  type: true-false
  answer: true
  explanation: "Correct. If you computed A − B = C, then C + B must equal A. This is the inverse relationship between subtraction and addition. It works for any numbers regardless of size, and it catches almost all arithmetic errors including regrouping mistakes and column mix-ups. The check is most valuable precisely for the problems where errors are most likely — those involving borrowing."

- question: "Why does the tens digit become 9 (not 10) after borrowing across a zero in a problem like 500 − 247?"
  type: short-answer
  answer: "When you borrow from the hundreds, the tens column temporarily receives 10. But then you must immediately borrow one of those tens for the ones column. That removes one ten from the tens, leaving 10 − 1 = 9. Students who forget this second step write 10 in the tens column and then subtract incorrectly."
  explanation: "The two-step nature of borrowing across a zero is what makes it the trickiest case in three-digit subtraction. Step 1: borrow from hundreds (tens gets 10). Step 2: borrow from tens for ones (tens goes from 10 to 9, ones get 10). Writing it out explicitly — showing the tens as 9 after both steps — prevents the most common error."
```

## Explainer

Three-digit subtraction builds directly on what you already know about subtracting two-digit numbers. You start at the ones column, move to the tens, and finish with the hundreds — and whenever a column's top digit is smaller than the bottom digit, you **borrow** (also called **regrouping**) from the column to the left. The new piece is simply that you now have three columns instead of two.

The ordinary case — no borrowing needed — is straightforward. For 785 − 342, subtract each column: 5 − 2 = 3, 8 − 4 = 4, 7 − 3 = 4, giving 443. One-column borrowing works just like you practiced with two-digit numbers: if you can't subtract ones, borrow a ten from the tens place, making the ones digit 10 bigger and the tens digit 1 smaller. Then move left and finish the subtraction.

The genuinely new challenge in three-digit subtraction is **borrowing across a zero**. Consider 400 − 163. You need to subtract 3 from 0, so you want to borrow from the tens place — but the tens digit is also 0. There's nothing to borrow there. You have to go all the way to the hundreds first: borrow one hundred from the 4, making the hundreds 3 and giving 10 tens to the tens place. Now borrow one of those tens for the ones place: the tens digit drops from 10 to 9, and the ones become 10. Now you can subtract: 10 − 3 = 7, 9 − 6 = 3, 3 − 1 = 2, giving 237.

The most reliable way to check any subtraction is to add your answer back to the number you subtracted: 237 + 163 should equal 400. If it does, your subtraction was correct. This inverse relationship — subtraction undone by addition — is one of the most useful checking strategies in arithmetic, and it works for numbers of any size.
