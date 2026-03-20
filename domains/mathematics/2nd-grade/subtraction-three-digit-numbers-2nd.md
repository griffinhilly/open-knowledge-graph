---
id: subtraction-three-digit-numbers-2nd
title: Three-Digit Subtraction
domain: mathematics
course: 2nd-grade
prerequisites:
- id: subtraction-two-digit-regrouping-2nd
  type: hard
- id: place-value-hundreds-2nd
  type: hard
builds-toward:
- addition-subtraction-word-problems
tags:
- subtraction
- three-digit
- regrouping
stage: concrete-operations
status: draft
---

# Three-Digit Subtraction

## Core Idea
Three-digit subtraction applies regrouping principles across place values. Students subtract ones, tens, and hundreds in sequence, regrouping from tens to ones or from hundreds to tens as needed.

## Questions

```yaml
- question: "A student is solving 503 − 267. They look at the ones: 3 − 7. They need to borrow, but the tens digit is 0. What should they do?"
  type: multiple-choice
  options:
    - "Write 0 in the ones place and skip borrowing — it can't be done"
    - "Borrow from the hundreds place to put a ten in the tens place, then borrow from tens to get ones"
    - "Subtract 7 − 3 instead and write 4 in the ones place"
    - "Change 503 to 500 to make it easier, then adjust the answer"
  answer: 1
  explanation: "When the tens digit is 0, you can't borrow from it directly — there's nothing there. Instead, borrow from the hundreds place: the hundreds digit decreases by 1, and 1 hundred becomes 10 tens. Now there's a 10 in the tens column. Then borrow from tens as normal: 1 ten becomes 10 ones, tens column becomes 9. This 'double borrow' is the hardest part of three-digit subtraction, but it follows the same logic: equal trades all the way down."

- question: "In which order do you work through the columns when doing three-digit subtraction?"
  type: multiple-choice
  options:
    - "Left to right: hundreds, then tens, then ones"
    - "Right to left: ones, then tens, then hundreds"
    - "It doesn't matter — columns can be done in any order"
    - "Always start with the largest column first"
  answer: 1
  explanation: "You must work right to left because borrowing flows leftward. When the ones column needs more, it borrows from the tens column — so the tens column must be adjusted before you subtract there. If you subtracted the tens first and then borrowed from them for the ones, you'd be borrowing from a column you already calculated. Right to left is the only order that keeps the bookkeeping consistent."

- question: "When you borrow a ten during three-digit subtraction, you are making an equal trade — 1 ten is exactly the same value as 10 ones."
  type: true-false
  answer: true
  explanation: "Borrowing is just renaming the same value in different units. One ten equals ten ones — breaking it down doesn't change the total, just like breaking a $10 bill into ten $1 bills leaves you with the same amount of money. This is why borrowing never changes the value you're subtracting from, only how it's expressed."

- question: "In three-digit subtraction, you can only regroup once per problem because the ones column can only borrow one time."
  type: true-false
  answer: false
  explanation: "You may need to regroup in both the ones column (borrowing from tens) and the tens column (borrowing from hundreds), depending on the numbers. Some problems, like those with zeros in the middle, require a 'chain' of borrowing across two columns. Each borrow is an independent equal trade."

- question: "A student asks: 'If I borrow from a column, doesn't that make the number I'm subtracting from smaller, so I get a smaller answer?' How would you explain why borrowing doesn't change the answer?"
  type: short-answer
  answer: "Borrowing doesn't change the total value — it just reorganizes how it's expressed. When you borrow 1 ten to get 10 extra ones, the tens digit goes down by 1 but the ones digit goes up by 10. The net change is zero: −10 + 10 = 0. It's like breaking a $10 bill into ten $1 bills — you have exactly the same amount, just in different denominations."
  explanation: "The confusion arises because students see a digit decrease and worry the number got smaller. But every borrow is an equal trade: you take from one column and give to the next. The original number's total value is preserved throughout the regrouping. This same principle is why regrouping in addition doesn't change the total — reorganizing between columns is always value-neutral."
```

## Explainer

You already know how to subtract two-digit numbers with regrouping — borrowing a ten when the ones column doesn't have enough. Three-digit subtraction is the same idea, just extended one column further to the left, into the hundreds place.

Here's the process: work from right to left, one column at a time. Start at the **ones** column. If the top number is smaller than the bottom, you can't subtract yet — you need to **regroup** (borrow) from the tens column. One ten comes over and becomes 10 extra ones, letting you subtract. Then move to the **tens** column. Again, if the top is smaller than the bottom (and remember, if you just borrowed from tens, its digit is already one smaller), regroup from the hundreds column. One hundred becomes 10 extra tens. Finally, subtract in the **hundreds** column.

For example: 435 − 178. Ones: 5 − 8, can't do it. Borrow from tens. Now ones: 15 − 8 = 7. Tens: 2 (after borrowing) − 7, can't do it. Borrow from hundreds. Tens: 12 − 7 = 5. Hundreds: 3 (after borrowing) − 1 = 2. Answer: 257.

The key insight is that regrouping never changes the *value* you're working with — it just reorganizes how it's expressed. One ten really is the same as ten ones; one hundred really is the same as ten tens. Every time you borrow, you're making an equal trade, like breaking a ten-dollar bill into ten ones. The number you're subtracting from hasn't gotten smaller; you've just restructured it so the subtraction can proceed column by column. Keep track of each borrow carefully, and the process becomes reliable — even for the hardest cases like subtracting from numbers with zeros in the middle.
