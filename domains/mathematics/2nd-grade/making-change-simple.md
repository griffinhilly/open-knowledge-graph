---
id: making-change-simple
title: Making Change
domain: mathematics
course: 2nd-grade
prerequisites:
- id: dollars-and-cents-notation
  type: hard
- id: subtraction-within-100
  type: hard
- id: counting-money-simple
  type: hard
- id: understanding-money-value
  type: hard
builds-toward:
- money-word-problems
tags:
- money
- change
- subtraction
- real-world
stage: concrete-operations
status: validated
---

# Making Change

## Core Idea
Change is the amount of money returned when you pay more than the price. To find change, subtract the price from the amount paid. For example, if an item costs 63¢ and you pay with a dollar (100¢), the change is 100 − 63 = 37¢. The 'count-up' strategy — counting from the price up to the amount paid — mirrors what cashiers do and avoids subtraction with borrowing for many problems.

## How It's Best Learned
Act out store scenarios with play money. Teach both the subtraction method and the count-up method, and let students choose. Limit prices to whole cents and amounts paid to single dollar bills initially. Gradually increase complexity to two-dollar amounts.

## Common Misconceptions
- Subtracting the paid amount from the price (reversing the subtraction).
- Forgetting to account for the cents column when the price has cents.
- Giving change in the fewest coins without checking correctness first.

## Questions

```yaml
- question: "An eraser costs 78¢ and you pay with a $1 bill. What is the correct way to find the change?"
  type: multiple-choice
  options:
    - "Subtract $1.00 from 78¢ to find the difference"
    - "Subtract 78¢ from 100¢ to get 22¢ change"
    - "Add 78¢ and 100¢ together"
    - "The change is always the same as the cost of the item"
  answer: 1
  explanation: "Change is what you get back after paying, so you subtract the price FROM the amount paid: 100¢ − 78¢ = 22¢. Option A reverses the subtraction — subtracting a larger amount from a smaller one doesn't make sense in this context and gives a negative result. You always subtract in the direction from 'what you paid' down to 'what it costs.'"

- question: "A book costs 63¢. You pay with $1. Using the count-up method, which sequence correctly finds the change?"
  type: multiple-choice
  options:
    - "Start at 100¢ and count down to 63¢, counting each cent"
    - "Start at 63¢, add 7¢ to reach 70¢, then add 30¢ to reach 100¢ — total added is 37¢"
    - "Start at 63¢ and subtract 1¢ at a time until you reach 0"
    - "Add 63 + 100 and divide by 2"
  answer: 1
  explanation: "The count-up method starts at the price and counts forward to the amount paid, adding in convenient chunks. From 63¢: add 7¢ to reach 70¢, then add 30¢ to reach 100¢. The total added (7 + 30 = 37¢) is the change. This mirrors what cashiers do naturally and avoids borrowing in subtraction. Both the subtraction method and the count-up method give the same answer."

- question: "You can check your change calculation by adding the change back to the price — if the total equals the amount you paid, your answer is correct."
  type: true-false
  answer: true
  explanation: "This is the standard verification method. If an item costs 63¢ and you calculated 37¢ change, check: 63 + 37 = 100¢ = $1. The check works because subtraction and addition are inverse operations. If change + price = amount paid, the subtraction was done correctly."

- question: "If an item costs 45¢ and you pay with $1, you find the change by subtracting $1.00 from 45¢."
  type: true-false
  answer: false
  explanation: "This reverses the subtraction. You subtract the price FROM the amount paid: 100¢ − 45¢ = 55¢. Subtracting the paid amount from the price (45 − 100) gives a negative number, which doesn't make sense for change. Change is always what's 'left over' after the price is covered — you start with the larger number (what you paid) and subtract the smaller one (the price)."

- question: "How can you check whether your change calculation is correct?"
  type: short-answer
  answer: "Add the change back to the price. If the sum equals the amount you paid, the answer is correct. For example: price 63¢ + change 37¢ = 100¢ = $1 paid. ✓"
  explanation: "Change is calculated by subtraction, and subtraction can always be verified by the inverse operation — addition. This check catches both computational errors and direction errors (accidentally subtracting the wrong way). Making the habit of checking every change calculation builds accuracy and reinforces the relationship between addition and subtraction."
```

## Explainer

Imagine you're buying a pencil that costs 63 cents and you hand the cashier a dollar bill. The cashier owes you back the difference — the amount left over after paying the price. That leftover amount is called **change**. Making change is just subtraction in a real-world context: start with what you paid, subtract what the item cost, and the result is what comes back to you.

The straightforward method is to subtract: 100¢ − 63¢ = 37¢. You already know how to subtract within 100, so you can apply that skill directly here. The challenge is keeping track of units — cents are cents, and you need to line up the numbers carefully. When you write it out as a subtraction problem, 100 − 63, the answer is 37, so the change is 37 cents.

There's a second method that many cashiers use naturally: **counting up**. Instead of subtracting, you start at the price and count up to the amount paid. From 63 cents, you might think: "63… add 7 cents to get 70, add 30 cents to get a dollar." The total you added — 7 + 30 = 37 cents — is the change. This method avoids borrowing and feels more natural when you're actually handling coins. Both methods give the same answer; which one you use depends on the numbers.

One mistake to watch for: never subtract the amount paid from the price (63 − 100 doesn't make sense here). Change always flows from the amount paid down to the price, because you gave more than was owed. You can check your work by adding the change back to the price — if you get the amount paid, you're right. 63 + 37 = 100. ✓ This idea of checking subtraction with addition is a habit that will serve you in every math context.
