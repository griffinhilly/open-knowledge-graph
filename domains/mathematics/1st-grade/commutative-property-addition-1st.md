---
id: commutative-property-addition-1st
title: Commutative Property of Addition
domain: mathematics
course: 1st-grade
prerequisites:
- id: addition-within-20
  type: hard
- id: properties-of-operations
  type: soft
builds-toward:
- addition-fact-families
- algebra-intro
tags:
- properties
- addition
stage: abstract-reasoning
status: draft
---

# Commutative Property of Addition

## Core Idea
The order of addends doesn't change the sum: 3 + 5 = 5 + 3 = 8. Recognizing this property reduces the number of facts to learn (if you know 3 + 5, you automatically know 5 + 3) and supports mental math strategies.

## Questions

```yaml
- question: "You know that 8 + 3 = 11. Without doing any new calculation, what does the commutative property immediately tell you?"
  type: multiple-choice
  options:
    - "3 + 8 = 11"
    - "8 − 3 = 5"
    - "11 − 8 = 3"
    - "3 + 3 = 6"
  answer: 0
  explanation: "The commutative property says switching the order of addends never changes the sum: 8 + 3 and 3 + 8 are the same fact. Subtraction facts like 8 − 3 are separate and are NOT given to you for free — subtraction is not commutative."

- question: "A student says: 'I know 4 + 7 = 11, but I still need to separately memorize 7 + 4 as a different fact.' What is wrong with this thinking?"
  type: multiple-choice
  options:
    - "The commutative property guarantees both expressions have the same sum, so knowing one gives you the other for free"
    - "Actually, 4 + 7 and 7 + 4 can give different answers depending on which number you count on from"
    - "The student is correct — they are different problems that require separate memory"
    - "You only need to memorize 7 + 4, not 4 + 7, because you should always start with the larger number"
  answer: 0
  explanation: "The commutative property means switching the order of addends never changes the sum. 4 + 7 and 7 + 4 are not two separate facts — they are one fact viewed from two directions. Knowing either one gives you the other automatically, which is why the property cuts memorization roughly in half."

- question: "The commutative property of addition means that 9 + 6 has the same sum as 6 + 9."
  type: true-false
  answer: true
  explanation: "Yes — this is exactly what the commutative property states. No matter which order you add the two numbers, the total is the same (15). The blocks don't change; only the direction you count them changes."

- question: "Because of the commutative property, you only need to memorize half as many addition facts AND half as many subtraction facts."
  type: true-false
  answer: false
  explanation: "The commutative property applies to addition, not subtraction. 9 − 3 = 6, but 3 − 9 is a different (negative) result — you cannot simply flip a subtraction problem. So the memorization shortcut applies only to addition facts, not subtraction facts."

- question: "Why does the commutative property cut the number of addition facts you need to memorize roughly in half?"
  type: short-answer
  answer: "Because every addition fact has a 'partner' fact with the same two numbers in the other order and the same sum. If you know 6 + 7 = 13, you automatically know 7 + 6 = 13 — you do not need to memorize them separately."
  explanation: "The commutative property means the sum depends only on which two numbers you add, not the order. Every pair of different addends (like 6 and 7) produces two equations (6+7 and 7+6) that share the same answer, so learning one teaches you both."
```

## Explainer

You already know how to add numbers within 20. Now here is a big insight: it doesn't matter which number you start with. If you have 3 red apples and 5 green apples, you have 8 apples total. But if you count the green ones first and then the red ones — 5 and then 3 more — you still get 8. The **commutative property of addition** says that switching the order of the two numbers you're adding never changes the answer.

Think about it with objects. Put 4 blocks on the left and 2 blocks on the right. Count them all: 6. Now move the groups — 2 on the left and 4 on the right. Count again: still 6. The blocks didn't disappear or multiply — you just looked at them from a different direction. The total is always 8 (or whatever the sum is), no matter which group you count first. This is what "commutative" means: you can **commute** (swap) the addends back and forth.

Here is why this is a superpower for learning addition facts. Suppose you already know that 7 + 3 = 10. The commutative property tells you, for free, that 3 + 7 = 10 too. You didn't have to memorize a separate fact — you got it automatically. This cuts the number of addition facts you need to memorize roughly in half. Every fact you learn comes with a partner: 6 + 4 gives you 4 + 6 as a bonus. When you see a new addition problem, always ask yourself: do I already know this one in the other order?

This property also helps you pick the easier path when adding mentally. If someone asks you to solve 2 + 9, you might not immediately know that one. But if you flip it to 9 + 2 — starting from 9 and counting up 2 — it becomes easy: 9, 10, 11. The commutative property lets you rearrange the problem to match your strongest strategies. You will keep using this idea all the way through school; it applies to bigger numbers and eventually to variables in algebra too. But the core idea is already here: order doesn't matter when you add.
