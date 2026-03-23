---
id: making-change-transactions
title: Making Change in Simple Transactions
domain: mathematics
course: 2nd-grade
prerequisites:
- id: counting-money-simple
  type: hard
- id: making-change-simple
  type: hard
- id: subtraction-within-100
  type: hard
builds-toward:
- money-word-problems
tags:
- money
- change
- subtraction
stage: concrete-operations
status: validated
---

# Making Change in Simple Transactions

## Core Idea
Making change means finding the difference between the amount paid and the price. If an item costs 28¢ and you pay 50¢, the change is 22¢. This is subtraction applied to real situations.

## How It's Best Learned
Use play money and role-play transactions. Have students physically count up from the price to the amount paid ('start at 28, count up to 50'). Also solve with subtraction (50 - 28 = 22).

## Common Misconceptions
- Confusing change with the amount paid.
- Subtracting in the wrong direction (price - amount paid instead of amount paid - price).
- Not recognizing that coins can be exchanged for equivalent amounts.

## Questions

```yaml
- question: "An item costs 35¢. A customer pays with 50¢. The cashier hands back 35¢, saying 'that's what the item cost.' What error did the cashier make?"
  type: multiple-choice
  options:
    - "The cashier added the price and payment together instead of subtracting"
    - "The cashier confused the price with the amount of change — change is 50 − 35 = 15¢, not 35¢"
    - "The cashier subtracted in the wrong direction, computing 35 − 50 instead of 50 − 35"
    - "The cashier should only accept exact change to avoid this kind of error"
  answer: 1
  explanation: "The cashier made the classic error of confusing the price with the change. The price (35¢) is what the store keeps. The change is what the store returns — only the difference between what was paid (50¢) and what was owed (35¢). Change = 50 − 35 = 15¢. The customer paid 15¢ more than the item cost, so only 15¢ is returned, not 35¢."

- question: "Which equation correctly calculates the change when an item costs 42¢ and the customer pays 75¢?"
  type: multiple-choice
  options:
    - "42 + 75 = 117¢"
    - "42 − 75 = −33¢"
    - "75 − 42 = 33¢"
    - "75 + 42 = 117¢"
  answer: 2
  explanation: "Change = amount paid − price = 75 − 42 = 33¢. The direction is always payment minus price, because the customer paid more than the item costs and receives the excess back. Option B (42 − 75) subtracts in the wrong direction, giving a negative number — which tells you the customer didn't pay enough, the opposite situation. Change is always a positive number when the customer paid at least the price."

- question: "If you pay for a 28¢ item with a 50¢ coin, your change is 28¢."
  type: true-false
  answer: false
  explanation: "The change is 50 − 28 = 22¢, not 28¢. The confusion here is mixing up the price (28¢) with the amount of change. The price is what the store keeps. The change is only the excess — how much more you paid than the item costs. Since you paid 50¢ and owed 28¢, the store keeps 28¢ and returns 22¢. Checking: 28 + 22 = 50 ✓."

- question: "Counting up from the price to the amount paid gives the same answer as subtracting the price from the amount paid."
  type: true-false
  answer: true
  explanation: "Both strategies find the same difference — just by moving in opposite directions. Subtracting: 50 − 28 = 22¢. Counting up: start at 28, hop to 30 (+2), hop to 50 (+20), total = 22¢. They must give the same answer because change is defined as the difference between payment and price, and subtraction and counting up are two different ways to find that same difference."

- question: "An item costs 46¢ and the customer pays 60¢. Find the change using both strategies — subtraction and counting up — and explain why they give the same answer."
  type: short-answer
  answer: "Subtraction: 60 − 46 = 14¢. Counting up: start at 46, add 4 to reach 50 (a friendly ten), then add 10 to reach 60. Total added: 4 + 10 = 14¢. They give the same answer because both are finding the gap between 46 and 60 — the size of the difference. Subtraction computes it directly; counting up builds it by collecting hops. The difference between two numbers is the same no matter which direction you measure it from."
  explanation: "This dual-strategy understanding is the heart of making change. Many experienced cashiers count up naturally because hops to friendly tens are easier to track mentally. But the arithmetic is identical — both methods answer the question 'how far apart are these two amounts?' Knowing both strategies lets you choose whichever is easier for a given problem and gives you a way to check your answer."
```

## Explainer

You already know how to count collections of coins, and you can subtract numbers within 100. Making change is where those two skills meet in a real-world situation with a clear purpose: making sure a transaction is fair. When a customer pays more than an item costs, the store owes the customer the difference back.

The core question is always: **how much more than the price did the customer pay?** If something costs 28¢ and the customer hands over 50¢, the change is 50 − 28 = 22¢. The structure is always the same: price is what you owe, payment is what you hand over, and change is the difference. The direction matters — you subtract the price from the payment, not the other way around, because the customer is receiving money back, not paying more.

There are two strategies for finding change, and both are worth knowing. The first is **subtraction**: write the equation directly and calculate. The second is **counting up**: start at the price and add amounts until you reach what was paid. Starting at 28¢, you might count up 2¢ to reach 30¢, then 20¢ more to reach 50¢ — so the change is 2 + 20 = 22¢. Counting up is how many experienced cashiers reason through it mentally, and it connects naturally to your prior work on number lines and "how much more" situations.

A common trap is confusing the amount of change with the amount paid. If you pay 50¢, the change is not 50¢ — the store keeps 28¢ and returns only the rest. Another trap is subtracting in the wrong direction. Keeping the story clear — who paid, what was the price, who gets the difference back — prevents both errors. Every time you buy something and count your change, you're doing exactly this arithmetic in the real world.
