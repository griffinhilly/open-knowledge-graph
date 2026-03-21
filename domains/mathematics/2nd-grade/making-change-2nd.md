---
id: making-change-2nd
title: Making Change
domain: mathematics
course: 2nd-grade
prerequisites:
- id: coins-and-their-values
  type: hard
- id: counting-money-simple
  type: hard
builds-toward:
- money-word-problems
tags:
- money
- change
- subtraction
- transactions
stage: concrete-operations
status: draft
---

# Making Change

## Core Idea
Making change means returning money after a transaction. If a purchase costs 15¢ and the customer pays 25¢, change is 10¢. Finding change involves subtracting cost from amount paid, a practical application of subtraction.

## Questions

```yaml
- question: "A pencil costs 23¢ and you pay with a quarter (25¢). Student A subtracts: 25 − 23 = 2, so 2¢ change. Student B counts up from 23¢: '24¢, 25¢' — two pennies. Which approach is correct?"
  type: multiple-choice
  options:
    - "Only Student A — subtraction is the only correct method for making change"
    - "Only Student B — counting up is the only method cashiers should use"
    - "Both students are correct; subtraction and counting up are two strategies for the same calculation"
    - "Neither — you need to count all the coins in your hand to find the change"
  answer: 2
  explanation: "Both methods work and reach the same answer (2¢) because they are two ways of computing the same thing: the difference between what was paid and what was owed. Subtraction computes it directly. Counting up reframes it as 'how much more is needed to get from 23¢ to 25¢?' Both are valid, and counting up is often faster with physical coins because you can stop as soon as you reach the amount paid."

- question: "An item costs 37¢ and the customer pays with two quarters (50¢). Which combination gives correct change using the fewest coins?"
  type: multiple-choice
  options:
    - "13 pennies"
    - "1 dime and 3 pennies"
    - "2 nickels and 3 pennies"
    - "1 nickel and 8 pennies"
  answer: 1
  explanation: "Change is 50 − 37 = 13¢. The fewest coins: 1 dime (10¢) + 3 pennies (3¢) = 4 coins. Counting up from 37¢ naturally leads here: 'go to 40¢ (3 pennies), then to 50¢ (1 dime)' — 4 coins total. The 13-penny option uses the right total but the most coins. Using fewest coins is the practical goal because it is easier to count and verify, and it's what cashiers and vending machines aim for."

- question: "The only correct way to calculate change is to write out the subtraction problem (amount paid minus cost) before deciding which coins to return."
  type: true-false
  answer: false
  explanation: "Counting up from the price to the amount paid is a completely valid — and often faster — strategy. Starting at the cost and adding coins until you reach the amount paid gives the exact same answer as subtraction, without needing paper or mental arithmetic. In real transactions, cashiers often count up by instinct: 'Your total is 83¢, you gave me a dollar — 84, 85, 90, one dollar' (2 pennies, 1 nickel, 1 dime = 17¢ change). The counting-up method also naturally produces the fewest coins."

- question: "Change equals the amount paid minus the cost of the item."
  type: true-false
  answer: true
  explanation: "This is the core equation: change = amount paid − cost. If an item costs 15¢ and you pay 25¢, change = 25 − 15 = 10¢. This is always true regardless of which calculation strategy you use. Counting up from 15¢ to 25¢ also gives 10¢ — it is the same calculation approached from a different direction (addition instead of subtraction), but the relationship is always amount paid − cost = change."

- question: "How does counting up from the price help you give back change in fewer coins? Walk through the example of an item costing 47¢ when the customer pays with a dollar."
  type: short-answer
  answer: "Counting up naturally guides you toward friendly numbers (multiples of 5 and 10), which minimizes coins. Starting at 47¢: add 3 pennies to reach 50¢, then 2 quarters to reach $1.00. Total change: 3 pennies + 2 quarters = 53¢ in 5 coins. A direct subtraction gives $1.00 − $0.47 = 53¢, but doesn't tell you which coins to use. Counting up to the next 5¢ or 10¢ increment first naturally finds the efficient coin combination."
  explanation: "The counting-up strategy works because it exploits the structure of our coin system — values are at 1¢, 5¢, 10¢, 25¢, 50¢, $1.00. Moving to the nearest 'friendly' value (next multiple of 5 or 10) with small coins, then jumping with larger coins, minimizes the count. This is the same reasoning as rounding to a friendly number when estimating — you work toward round targets to keep the math simple and the coin count low."
```

## Explainer

You already know the values of coins — a quarter is 25¢, a dime is 10¢, a nickel is 5¢, a penny is 1¢ — and how to count up a collection of coins to find a total. Making change uses both those skills together in a real-world transaction: someone pays more than something costs, and the cashier returns the difference.

The core calculation is subtraction. If a pencil costs 17¢ and you pay with a quarter (25¢), the change is 25 − 17 = 8¢. But in real life, people rarely calculate change by doing the subtraction on paper. Instead, they **count up** from the price to the amount paid. Starting at 17¢, you might say: "18¢ (one penny), 19¢, 20¢ (another penny and a nickel), 25¢ (a nickel)." That gives you 3 pennies and 1 nickel — which is 8¢. Counting up is often easier because you're working with physical coins that have specific values, and you can stop as soon as you reach the amount paid.

There's a strategy that makes this even smoother: use **fewest coins**. If change is 8¢, you could hand back 8 pennies — but a nickel and 3 pennies is much easier for everyone. Think of it as building to a nice number: go to the next 5¢ or 10¢ first, then keep going to the total paid. This is exactly the same thinking as rounding to a friendly number when you estimate.

The key question to ask yourself in any change problem is: "How much MORE does the customer need to go from the price to what they paid?" That reframes subtraction as an addition problem — and addition is often easier to think through with coins. Change = amount paid − price. Both ways of thinking lead to the same answer.
