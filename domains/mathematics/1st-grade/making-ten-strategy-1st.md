---
id: making-ten-strategy-1st
title: Making Ten Strategy
domain: mathematics
course: 1st-grade
prerequisites:
- id: number-bonds-to-10
  type: hard
- id: addition-within-20
  type: hard
builds-toward:
- addition-fact-families
- place-value-tens-and-ones
tags:
- strategy
- mental-math
- decomposition
stage: pre-formal
status: validated
---

# Making Ten Strategy

## Core Idea
To solve 8 + 5, break 5 into 2 + 3. Then 8 + 2 = 10, and 10 + 3 = 13. Using 10 as a benchmark makes the problem simpler. This strategy relies on knowing number bonds to 10 and is a bridge to place-value understanding.

## Questions

```yaml
- question: "Using the make-ten strategy to solve 9 + 6, which number should you break apart, and into what parts?"
  type: multiple-choice
  options:
    - "Break the 9 into 5 + 4, then add 5 + 6 = 11, then add 4"
    - "Break the 6 into 1 + 5, since 9 needs 1 more to reach 10; then compute 10 + 5 = 15"
    - "Break the 6 into 3 + 3, add 9 + 3 = 12, then add 3 more"
    - "Break both numbers in half and add the halves separately"
  answer: 1
  explanation: "The make-ten strategy always asks: how much does the larger number need to reach 10? The 9 needs just 1 more. So you take 1 from the 6, giving you 9 + 1 = 10, with 5 left over. Then 10 + 5 = 15. You always break the smaller number into the exact piece the larger number needs, plus the remainder. Breaking the larger number (option A) or breaking randomly (option C) misses the point of the strategy."

- question: "Why is 10 a useful 'stepping stone' in the make-ten strategy?"
  type: multiple-choice
  options:
    - "Because 10 is the largest single-digit number"
    - "Because our number system is organized around tens, so adding to 10 is fast and easy"
    - "Because 10 is always exactly in the middle between any two numbers"
    - "Because you can split 10 evenly, which makes the math simpler"
  answer: 1
  explanation: "Ten is special because our whole number system is built in base ten — numbers are organized into groups of ten. Once you reach 10, you've completed one full group, and 10 + any single digit is immediately recognizable (10 + 6 = 16, 10 + 7 = 17). This is essentially thinking in place value: one ten and some ones. Ten is a 'friendly' number precisely because of how the number system works, not by coincidence."

- question: "In the make-ten strategy for 8 + 5, you break the 8 into smaller parts to reach 10."
  type: true-false
  answer: false
  explanation: "This is the most common mix-up. In 8 + 5, you always start with the LARGER number (8) and ask what it needs to reach 10 — that's 2. Then you break the SMALLER number (5) into 2 + 3. You give the 2 to the 8 (making 10), and the 3 is what's left. The larger number stays intact; the smaller number is broken apart. Breaking the larger number instead defeats the strategy."

- question: "The make-ten strategy works because adding any number to 10 is quick and easy in our base-ten number system."
  type: true-false
  answer: true
  explanation: "This captures the deep reason the strategy works. Our number system groups things by tens, so 10 + 3 = 13, 10 + 7 = 17, and so on are almost automatic — the tens digit is always 1 and the ones digit is the number you're adding. The make-ten strategy deliberately routes every addition problem through this easy step, turning hard problems (8 + 5) into easy ones (10 + 3). It's not a trick — it reflects the structure of the number system."

- question: "Using the example 7 + 5, explain the three steps of the make-ten strategy."
  type: short-answer
  answer: "Step 1: Find out how much 7 needs to reach 10 — it needs 3. Step 2: Break 5 into 3 + 2 (giving 3 to the 7). Step 3: Now you have 10 + 2 = 12."
  explanation: "The three steps are always: (1) find the 'gap' between the larger number and 10, (2) break the smaller number into that gap plus a remainder, and (3) add the remainder to 10. The strategy works because it uses known number bonds to 10 (7 + 3 = 10) to turn a harder calculation into an easy one (10 + 2 = 12)."
```

## Explainer

You already know your number bonds to 10 — the pairs of numbers that add up to exactly 10, like 6 + 4, 7 + 3, and 8 + 2. And you've practiced adding numbers within 20. Making ten is a strategy that combines both of those skills into a powerful shortcut: instead of counting all the way from 8 up to 13 in your head, you can use 10 as a stepping stone.

Here's how it works. Suppose you need to add 8 + 5. Ten is a friendly, easy number — you know what 10 looks like, and you know that 10 + anything is simple. So instead of adding 8 and 5 directly, you ask: how much does 8 need to become 10? It needs 2 more. So you "borrow" 2 from the 5, making 8 into 10. Now the 5 has become 3 (because you used 2 of it). The new problem is 10 + 3, which is easy: 13. You've used your number bond knowledge (8 + 2 = 10) to turn a tricky problem into a simple one.

The reason 10 is such a useful stopping point is that our number system is built around tens. Once you reach 10, you're starting a new group — the tens place. This is why adding to 10 feels natural and quick. When you know that 10 + 6 = 16, or 10 + 7 = 17, you're already thinking in place value: one ten and some ones. Making ten is practice for the way our whole number system is organized.

Try it with other problems: 9 + 4 (9 needs 1 more to reach 10, so take 1 from the 4, leaving 3; now you have 10 + 3 = 13). Or 7 + 6 (7 needs 3 more, take 3 from 6, leaving 3; 10 + 3 = 13). The strategy always has the same three steps: figure out what your bigger number needs to reach 10, break that amount off the smaller number, and then add what's left to 10. With practice, you won't need to think through all the steps — your brain will jump straight to the answer.
