---
id: two-digit-addition-with-regrouping
title: Two-Digit Addition with Regrouping
domain: mathematics
course: 2nd-grade
prerequisites:
- id: two-digit-addition-no-regrouping
  type: hard
- id: place-value-tens-and-ones
  type: hard
- id: regrouping-addition-trading-ones-for-tens
  type: hard
builds-toward:
- addition-within-100
- three-digit-addition
- multi-digit-addition
tags:
- addition
- regrouping
- carrying
- place-value
stage: concrete-operations
status: validated
---

# Two-Digit Addition with Regrouping

## Core Idea
When adding two-digit numbers, the ones column may sum to 10 or more. When this happens, we regroup — trading 10 ones for 1 ten and carrying that ten to the tens column. For example, 47 + 35 requires regrouping because 7 + 5 = 12 ones, so we write 2 ones and carry 1 ten. Understanding place value is essential: the carry represents a full group of ten.

## How It's Best Learned
Use base-ten blocks to physically trade 10 unit cubes for a tens rod before moving to the written algorithm. Have students predict whether regrouping will be needed (ones digits sum ≥ 10) before computing. Practice with open number lines alongside the standard algorithm so students understand what is happening, not just the procedure.

## Common Misconceptions
- Forgetting to add the carried ten to the tens column.
- Writing both digits of the ones sum (e.g., writing '12' in the ones place instead of regrouping).
- Believing regrouping changes the total value — emphasize that 12 ones = 1 ten and 2 ones.

## Questions

```yaml
- question: "A student adds 38 + 47 and writes '15' in the ones place because 8 + 7 = 15. What should she do instead?"
  type: multiple-choice
  options:
    - "Write 1 in the ones place and carry the 5 to the tens column"
    - "Write 5 in the ones place and carry the 1 ten to the tens column"
    - "Start over and add the tens column first"
    - "Round both numbers to the nearest 10 before adding"
  answer: 1
  explanation: "When the ones column sums to 10 or more, you must regroup: trade 10 ones for 1 ten. 8 + 7 = 15 ones — that's 1 ten and 5 ones. Write the 5 in the ones place (the remaining ones), and carry the 1 ten to the tens column. Writing '15' in the ones place is the classic error: the ones place can only hold a single digit. The regrouped ten must move to the tens column because that's where tens belong."

- question: "When you carry the '1' to the tens column during regrouping, what does that 1 represent?"
  type: multiple-choice
  options:
    - "One extra one that was left over from the ones column"
    - "One ten, formed by trading 10 ones — it belongs in the tens column"
    - "A placeholder so the tens column is not empty"
    - "The first digit of the ones-column sum"
  answer: 1
  explanation: "The carried '1' represents one ten — a full group of 10. When the ones column sums to 10 or more, you can trade 10 ones for 1 ten (because that's what a ten is). That new ten gets recorded in the tens column. Students often think of it as 'just a 1,' but understanding it as 1 ten explains why it goes to the tens column and why it must be added there — it's the same unit as the other tens."

- question: "Regrouping during addition changes the total value of the sum — the carried 1 adds extra to the answer."
  type: true-false
  answer: false
  explanation: "This is the central misconception about regrouping. Regrouping does NOT change the total value — it only renames it. 12 ones and 1 ten + 2 ones represent the exact same amount; you have simply reorganized how they're expressed to fit the place-value system. The carried 1 is not extra — it came from the ones column. Nothing is added or removed. Base-ten blocks make this visible: trading 10 unit cubes for a tens rod doesn't change how many you have."

- question: "You can predict whether regrouping will be needed by checking if the ones digits of both numbers sum to 10 or more."
  type: true-false
  answer: true
  explanation: "Regrouping is triggered exactly when the ones-column sum reaches 10 or more, because 10 ones can be traded for 1 ten. If the ones digits sum to 9 or less, no trading is needed and the result fits directly in the ones place. Developing the habit of previewing this before computing — 'do the ones digits together reach 10?' — deepens understanding of what regrouping is about and helps catch errors before they happen."

- question: "Explain what it means to 'regroup' in addition and why it doesn't change the total."
  type: short-answer
  answer: "Regrouping means trading 10 ones for 1 ten when the ones column adds up to 10 or more. The total doesn't change because 10 ones and 1 ten are the same amount — just expressed differently. For example, in 47 + 35, the ones give 12, which is renamed as 1 ten and 2 ones. The 2 stays in the ones place; the 1 ten is added to the tens column. The value is preserved; only the representation changes."
  explanation: "The key insight is that regrouping is renaming, not changing. Our number system is built on groups of 10, so whenever a column accumulates 10 or more of its unit, you can always trade them up: 10 ones become 1 ten, 10 tens become 1 hundred. This trade is completely value-neutral. The total quantity stays the same; only how it's expressed in place-value form changes. This is why carrying always produces a correct answer — you're reorganizing the total, not altering it."
```

## Explainer

You already know how to add two-digit numbers when the ones column stays below 10 — you simply add ones to ones, then tens to tens. Regrouping is what happens when the ones column "overflows." The key idea comes directly from your knowledge of **place value**: our number system groups things in tens. When you have 10 or more ones, you can always trade them for a ten, because that's what tens *are*.

Here's the core example. Add 47 + 35. Start with the ones: 7 + 5 = 12. But "12 ones" can't stay in the ones place — there's only room for a single digit there. So you **regroup**: trade 10 of those 12 ones for 1 ten, keeping 2 ones in the ones place. Write the 2 ones in the ones column and carry the new ten up to the tens column as a small "1." Now add the tens: 4 + 3 + 1 (the carried ten) = 8 tens. The answer is 82.

What makes regrouping work — and what students often miss — is that *nothing is being added or removed*. You're only **renaming** the same quantity. 12 ones and 1 ten + 2 ones are exactly the same amount, just as a dozen eggs is 12 eggs regardless of how they're arranged. The total value is preserved; only the representation changes. This is why base-ten blocks are so helpful: when you physically trade 10 unit cubes for a tens rod, you can see and feel that the total amount hasn't changed.

Before computing, you can predict whether regrouping will be needed: if the ones digits sum to 10 or more, you'll regroup. 6 + 7 = 13 (regroup), 8 + 5 = 13 (regroup), 3 + 4 = 7 (no regroup). Building this habit of previewing a problem helps you stay alert during computation. Every multi-digit addition you encounter in later grades — with hundreds, thousands, and beyond — applies exactly this same principle, column by column, moving from right to left.
