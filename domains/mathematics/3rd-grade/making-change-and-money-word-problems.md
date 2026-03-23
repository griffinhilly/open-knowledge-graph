---
id: making-change-and-money-word-problems
title: Making Change and Money Word Problems
domain: mathematics
course: 3rd-grade
prerequisites:
- id: coins-and-their-values
  type: hard
- id: counting-money-simple
  type: hard
builds-toward:
- money-word-problems
tags:
- money
- real-world
- applications
stage: concrete-operations
status: validated
---

# Making Change and Money Word Problems

## Core Idea
Making change requires understanding coin values and computing the difference between a price and amount paid. For example, if an item costs 37¢ and you pay 50¢, the change is 50 − 37 = 13¢. Real and modeled shopping contexts apply arithmetic skills.

## Questions

```yaml
- question: "Marcus buys a pencil for 45¢ and pays with 2 quarters. How much change does he get?"
  type: multiple-choice
  options:
    - "5¢ — 50¢ minus 45¢"
    - "45¢ — the price of the pencil"
    - "95¢ — the price plus the amount paid"
    - "10¢ — subtracting the quarters from the price"
  answer: 0
  explanation: "Change = amount paid − price = 50¢ − 45¢ = 5¢. Two quarters = 50¢ (each quarter = 25¢). The price is 45¢. The subtraction is straightforward once you correctly identify both amounts. Option B confuses the price with the change; option C adds instead of subtracts; option D performs the subtraction backwards."

- question: "In the problem 'Lily buys stickers for 63¢ and pays with 3 quarters. How much change does she get?' — what is the unknown quantity?"
  type: multiple-choice
  options:
    - "The price of the stickers"
    - "The number of quarters Lily used"
    - "The amount of change she receives"
    - "The total value of 3 quarters"
  answer: 2
  explanation: "Identifying the unknown is the first step in solving any word problem. The price (63¢) is given. The number of quarters (3) is given. The total value of 3 quarters (75¢) can be calculated from given information. What the problem asks for — and what is not directly stated — is the change. Translating 'how much change' into 'amount paid minus price' is the key move: 75¢ − 63¢ = 12¢."

- question: "Counting up from the price to the amount paid gives a different answer than subtracting the price from the amount paid."
  type: true-false
  answer: false
  explanation: "Both methods measure the same gap between two numbers — they are mathematically identical. Counting up from 37¢ to 50¢ (add 3¢ to reach 40¢, add 10¢ to reach 50¢, total = 13¢) gives the same answer as 50 − 37 = 13. Counting up mirrors the physical action of making change at a register; subtraction is the arithmetic abstraction of the same operation. Same result, different mental approach."

- question: "To find the change owed, you subtract the price from the amount paid."
  type: true-false
  answer: true
  explanation: "Change = amount paid − price. If you pay more than the item costs, the difference comes back to you. This direction of subtraction matters: the amount paid is the larger number, and the price is subtracted from it. Reversing the subtraction (price − amount paid) would give a negative number, which signals you've set it up backwards."

- question: "Why is 'translating the situation into a calculation' the key skill in money word problems? Give an example of a translation step you would need to take."
  type: short-answer
  answer: "Word problems describe a real situation using language — your job is to convert that language into the numbers and operations needed to solve it. The arithmetic itself is often simple; the difficulty is identifying what is known, what is unknown, and which operation connects them. Example: 'Mia pays with 3 quarters' must be translated to '3 × 25¢ = 75¢ paid' before you can subtract the price."
  explanation: "Students often struggle with money word problems not because of the arithmetic but because they cannot extract the right numbers and operation from the sentence. The translation habit — pausing to name the price, name the amount paid, identify what's missing, then choose the operation — applies to all applied math, not just money. Every real-world math problem requires this interpretation step before any calculation begins."
```

## Explainer

You know the value of each coin and how to count a collection of money. Now you're applying those skills in a real transaction. When you buy something, two amounts meet: the **price** of the item and the **amount you pay**. If they match exactly, no change is needed. When you pay more than the price, the difference comes back to you as **change** — and computing that difference is the core skill here.

The calculation is subtraction: amount paid − price = change. If you pay 50¢ for something that costs 37¢, the change is 50 − 37 = 13¢. But there's a second strategy called **counting up** that many people find more natural at a register: start from the price (37¢) and count up to the amount paid (50¢). Add 3¢ to reach 40¢, then add 10¢ to reach 50¢. Total added: 13¢. Counting up is mathematically identical to subtraction — you're measuring the gap between two numbers — but the mental motion mirrors how change actually moves between hands.

Deciding *which coins* to return is its own mini-problem. To make 13¢ in change, the fewest coins is 1 dime + 3 pennies. You could also use 2 nickels + 3 pennies, but that's more coins for the same amount. The practical strategy: use the largest denominations that fit, working down to smaller ones for the remainder. This is the same left-to-right strategy you used for counting money, now run in reverse.

Word problems add a reading layer on top of the arithmetic. "Mia buys a notebook for 65¢ and pays with 3 quarters. How much change does she get?" You must first interpret "3 quarters" as 75¢, then compute 75 − 65 = 10¢. The arithmetic is simple; the real skill is **translating a situation into a calculation** — identifying what is known, what is unknown, and which operation connects them. This translation skill is the foundation of all applied math, and every money word problem is practice at it.
