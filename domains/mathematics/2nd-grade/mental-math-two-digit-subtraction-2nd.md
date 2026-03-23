---
id: mental-math-two-digit-subtraction-2nd
title: Mental Math Strategies for Subtraction
domain: mathematics
course: 2nd-grade
prerequisites:
- id: subtraction-two-digit-regrouping-2nd
  type: soft
- id: mental-math-strategies-subtraction-1st
  type: hard
builds-toward:
- estimation-addition-subtraction-2nd
tags:
- mental-math
- subtraction
- strategies
- fluency
stage: concrete-operations
status: validated
---

# Mental Math Strategies for Subtraction

## Core Idea
Mental math strategies for subtraction include counting on, counting back, using tens, and relating subtraction to addition. For example, 45 - 18 can be solved by counting up from 18 to 45 (18 → 20 → 45 is 2 + 25 = 27).

## Questions

```yaml
- question: "To solve 53 − 28 mentally, Carlos thinks: 'I'll count up from 28 to 53. First I jump to 30 — that's 2. Then I jump to 50 — that's 20. Then I jump to 53 — that's 3. My answer is 25.' Is Carlos correct, and what strategy is he using?"
  type: multiple-choice
  options:
    - "Wrong — to subtract, you must count backward, not forward"
    - "Correct — he is using the counting-on strategy, turning the subtraction problem into a series of additions"
    - "Wrong — you cannot mix tens jumps and ones jumps in the same problem"
    - "Correct — but only because 28 happens to be close to a multiple of ten"
  answer: 1
  explanation: "Carlos is correct and his method is elegant. The counting-on strategy reframes 53 − 28 as 'what do I add to 28 to reach 53?' Each hop adds a friendly amount and targets a landmark number. 28 → 30 is +2, 30 → 50 is +20, 50 → 53 is +3. Total: 2 + 20 + 3 = 25. This works for any subtraction problem — not just when numbers are close to tens — and is often faster and more accurate than counting backward."

- question: "To solve 71 − 29 using the round-and-adjust strategy: you round 29 up to 30, compute 71 − 30 = 41, then..."
  type: multiple-choice
  options:
    - "Stop — 41 is the final answer"
    - "Subtract 1 more to get 40, because rounding up means adding more"
    - "Add 1 back to get 42, because you subtracted 1 too many when you used 30 instead of 29"
    - "Subtract 29 from 41 to double-check"
  answer: 2
  explanation: "When you round 29 up to 30, you are subtracting a larger number than the original problem asks for. 71 − 30 takes away one more than 71 − 29 does. To correct for this overshoot, you add 1 back: 41 + 1 = 42. The rule is: if you rounded UP (subtracted more than needed), ADD back the difference. If you had rounded DOWN (subtracted less than needed), you would subtract the difference."

- question: "In the counting-on strategy for subtraction, you count backward from the larger number to the smaller number."
  type: true-false
  answer: false
  explanation: "Counting on means starting at the smaller number and counting FORWARD (adding) to reach the larger number. For 45 − 18, you start at 18 and count up to 45 — you never subtract at all. This is the key insight: subtraction can be turned into addition. Counting backward from the larger number is a different strategy (counting back) that is only efficient when the number being subtracted is very small."

- question: "When using the round-and-adjust strategy, if you round the subtracted number UP before computing, you need to ADD back the difference to get the correct answer."
  type: true-false
  answer: true
  explanation: "If you subtract a number that is bigger than what the problem asks, your answer will be too small. You over-subtracted, so you compensate by adding back the extra. For example, 65 − 19: round 19 up to 20, compute 65 − 20 = 45, then add back 1 (because 20 is 1 more than 19), giving 46. The adjustment always corrects for the difference between the rounded number and the original."

- question: "Explain why the counting-on strategy turns a subtraction problem into an easier addition problem. Use 62 − 57 as your example."
  type: short-answer
  answer: "Subtraction asks 'how much is left after taking away?' but counting on asks the equivalent question 'how much do I need to add to get from the smaller number to the larger?' For 62 − 57, instead of trying to subtract 57 from 62, count up from 57 to 62: 57 → 60 is +3, 60 → 62 is +2. Total added: 5. So 62 − 57 = 5. The two numbers are close together, so only a few small hops are needed — far easier than borrowing or counting back 57 steps."
  explanation: "The key insight is that subtraction and addition are two sides of the same relationship: a − b = ? is the same question as b + ? = a. Counting on exploits the fact that small hops to landmark numbers are much easier to track mentally than large backward counts. This strategy is especially powerful when the two numbers are close together (small difference) or when one number is near a multiple of ten."
```

## Explainer

Mental subtraction feels harder than mental addition, but there is a secret: you do not have to subtract at all. You already know from your work on number relationships that subtraction and addition are inverses — 45 − 18 asks the same question as "what do I add to 18 to reach 45?" This reframe, called **counting on**, turns a subtraction problem into a more natural addition problem.

Here is counting on in action for 45 − 18. Start at 18. The nearest friendly ten is 20, so first add 2 to get there (18 → 20). Now jump by tens: 20 → 30 → 40 is two jumps of 10. One more jump of 5 lands on 45. Add up your jumps: 2 + 10 + 10 + 5 = 27. You never subtracted; you collected small additions. Each hop targeted a ten, which you can hold in memory easily.

The **use-tens strategy** works differently, but also leans on landmark numbers. To compute 45 − 18, round the number being subtracted to the nearest ten: 18 rounds up to 20. Subtracting 20 from 45 is easy: 25. But you subtracted 2 too many (you subtracted 20 instead of 18), so add them back: 25 + 2 = 27. This adjust-and-correct pattern — overshoot a friendly number, then compensate — is a theme that appears throughout arithmetic and algebra. The adjustment is always the difference between the rounded number and the original.

Choosing which strategy to use is itself a skill. Counting on works best when the two numbers are close together (e.g., 62 − 57 is 5 hops). Using-tens works best when one number is close to a multiple of ten (e.g., 71 − 29 rounds 29 to 30, subtract to get 41, add 1 back). With practice, you will start recognizing which approach fits a given problem in a few seconds — the hallmark of **number sense**, the ability to see numbers flexibly rather than mechanically.

