---
id: multi-digit-addition
title: Multi-Digit Addition
domain: mathematics
course: 4th-grade
prerequisites:
- id: place-value-whole-numbers
  type: hard
- id: three-digit-addition
  type: soft
- id: two-digit-addition-with-regrouping
  type: soft
- id: two-step-word-problems
  type: soft
builds-toward:
- multi-digit-subtraction
- estimation-strategies
- adding-subtracting-decimals
tags:
- arithmetic
- addition
- place-value
stage: concrete-operations
status: validated
---
# Multi-Digit Addition

## Core Idea
Multi-digit addition extends single-digit addition by working place value by place value, starting from the ones. When the sum in any column exceeds 9, we "regroup" (carry) into the next place -- this is why understanding that 10 ones = 1 ten is essential. Students at this level add numbers up to the millions, managing multiple regroupings across columns. The standard algorithm is efficient, but it only makes sense when students understand that they are combining like units (ones with ones, tens with tens) and trading 10 of one unit for 1 of the next.

## How It's Best Learned
Start with base-ten blocks: physically combine ones, trade 10 ones for a ten-rod, combine ten-rods, trade 10 for a hundred-flat. Then transition to the written algorithm, linking each step back to what the blocks showed. Partial sums (adding each place separately, then combining) is a useful bridge strategy. Practice with real-world contexts -- combining distances, costs, populations -- reinforces meaning.

## Common Misconceptions
- Forgetting to carry when a column sums to 10 or more.
- Adding digits across different place values (misaligning columns).
- Carrying the wrong digit (writing the tens digit in the column and carrying the ones digit).

## Questions

```yaml
- question: "What is the sum of 3,846 + 2,975?"
  type: multiple-choice
  options: ["5,711", "6,711", "6,821", "6,811"]
  answer: 2
  explanation: "Starting from the ones: 6+5=11, write 1 carry 1; tens: 4+7+1=12, write 2 carry 1; hundreds: 8+9+1=18, write 8 carry 1; thousands: 3+2+1=6. Result: 6,821. A common error is forgetting one or more carries, which produces 6,811 or 6,711."

- question: "When adding 4,567 + 2,489, you can determine the thousands digit by computing 4 + 2 = 6 without checking for a carry from the hundreds column."
  type: true-false
  answer: false
  explanation: "Carries from lower columns can change a higher column's digit. Here: ones 7+9=16 (write 6, carry 1); tens 6+8+1=15 (write 5, carry 1); hundreds 5+4+1=10 (write 0, carry 1); thousands 4+2+1=7. The answer is 7,056, not 6,056. Never assume a column's digit is final until you check whether the column to its right generated a carry."

- question: "A school collected 1,248 cans in the first week and 976 in the second week. Explain how place-value alignment helps you find the correct total."
  type: short-answer
  answer: "Align 1,248 and 976 so ones are under ones, tens under tens, etc. Then add column by column from the right: 8+6=14 (write 4, carry 1); 4+7+1=12 (write 2, carry 1); 2+9+1=12 (write 2, carry 1); 1+0+1=2. Total: 2,224."
  explanation: "Alignment enforces the rule that only like units combine. Without it, you might add a tens digit to a ones digit, mixing units and producing a nonsense answer. The carries represent legitimate trading — 10 ones become 1 ten, 10 tens become 1 hundred — which is exactly what place value describes."
```

## Explainer

You already know two things that make multi-digit addition straightforward: how to add single-digit numbers, and how place value works (ones, tens, hundreds, thousands, and so on). Multi-digit addition is just those two ideas applied together. The central rule is that you can only combine like units — ones with ones, tens with tens, hundreds with hundreds. This is why you write numbers aligned by place value before adding.

Always start from the ones column and move left. When you add the ones, you might get a sum of 10 or more. You cannot write a two-digit number in a single column, so you write the ones digit in the column and "carry" the tens digit to the next column — this is regrouping. What you are really doing is trading 10 ones for 1 ten, the same trade you made physically with base-ten blocks when 10 unit cubes became a ten-rod.

The most common mistake is forgetting to include the carried digit in the next column. Think of a carry as an obligation: the moment you write it above a column, you must add it when you get there. A good habit is to write carry digits small above the column so they stay visible. The second most common mistake is misaligning columns — writing 976 so that its 9 lines up under the thousands digit of 1,248 instead of under the hundreds digit.

This algorithm scales to any number of digits without any new rules. Whether you are adding five-digit numbers or ten-digit numbers, each column works exactly like the ones column. That unlimited scalability is one of the most remarkable features of base-ten positional notation — the same simple procedure handles any size of number you could ever encounter.
