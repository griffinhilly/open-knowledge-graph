---
id: addition-strategies-counting-on
title: 'Addition Strategy: Counting On'
domain: mathematics
course: 1st-grade
prerequisites:
- id: addition-within-20
  type: hard
- id: number-line-0-to-20
  type: soft
builds-toward:
- mental-math-add-subtract-tens
- addition-fact-families
tags:
- strategy
- mental-math
- addition
stage: pre-formal
status: draft
---

# Addition Strategy: Counting On

## Core Idea
Instead of counting from 1, students start at the first number and count on from there. To solve 7 + 3, say '7' then count '8, 9, 10' on fingers or using a number line. This is faster and more efficient than starting from 1 each time.

## How It's Best Learned
Model on a number line and with fingers. Use small totals first (5 + 2) then expand. Have students verbalize: 'Start at 5, count 6, 7.' Repeat until automatic.

## Common Misconceptions
- Counting the starting number again (counting 7, 8, 9, 10 instead of starting at 7).
- Using this strategy only with a number line; real objects and fingers work too.
- Thinking this is slower; it actually builds automaticity.

## Questions

```yaml
- question: "A student solves 7 + 3 by counting: '7, 8, 9' and writes 9 as her answer. What error did she make?"
  type: multiple-choice
  options:
    - "She started at the wrong number; she should have started at 3"
    - "She counted 7 as her first step rather than holding it, so she only moved 2 steps instead of 3"
    - "The counting-on strategy doesn't work when the first number is larger than the second"
    - "She should have counted backward from 10 instead"
  answer: 1
  explanation: "Counting on requires holding the first number in mind and counting ON from it — not saying it aloud as a step. The student said '7' as step 1, then '8, 9' for two more steps, counting only 2 steps total instead of 3. The correct approach: hold 7, then count '8' (step 1), '9' (step 2), '10' (step 3). The answer is 10, not 9. This off-by-one error is the most common mistake with counting on."

- question: "To solve 3 + 8 most efficiently using the counting-on strategy, where should you start?"
  type: multiple-choice
  options:
    - "Start at 3 and count on 8 steps: 4, 5, 6, 7, 8, 9, 10, 11"
    - "Start at 8 and count on 3 steps: 9, 10, 11"
    - "Count all numbers from 1 to 11"
    - "Start at 3 and count on 3 steps, since both numbers are in the problem"
  answer: 1
  explanation: "Because addition is commutative (3 + 8 = 8 + 3), you can always start from the larger number. Starting at 8 and counting on just 3 steps (9, 10, 11) reaches the answer in 3 counts. Starting at 3 and counting on 8 steps reaches the same answer in 8 counts — correct, but more than twice as slow. Always starting from the larger number makes counting on as efficient as possible."

- question: "When using counting-on to solve 5 + 4, you should say '5' aloud as the first counting step."
  type: true-false
  answer: false
  explanation: "The key rule of counting on is to hold the first number in your mind without counting it, then count on from there. Saying '5' as the first step means you start at 4 and end at 8 instead of 9. The correct method: hold 5, then say '6' (step 1), '7' (step 2), '8' (step 3), '9' (step 4). The last number said — 9 — is the answer."

- question: "The counting-on strategy is more efficient than counting all because it skips the steps from 1 up to the starting number."
  type: true-false
  answer: true
  explanation: "Counting all starts from 1 every time, requiring as many steps as the total sum. For 7 + 3, counting all means counting 10 numbers (1 through 10). Counting on skips the first 7 steps by holding 7 in mind and counting only the 3 remaining steps (8, 9, 10). This efficiency advantage grows with larger starting numbers."

- question: "Why should you always start the counting-on strategy from the larger of the two numbers, even if the problem writes the smaller number first?"
  type: short-answer
  answer: "Because addition is commutative — the order of the numbers doesn't change the sum. Starting from the larger number reduces the counting steps needed to just the smaller number's worth, making the strategy faster. For 2 + 9, starting at 9 requires only 2 counting steps (10, 11) instead of 9 steps if you started at 2."
  explanation: "The commutative property makes this swap valid: 2 + 9 = 9 + 2 = 11 regardless of order. Recognizing this and always using the larger number as the starting point is what separates an efficient counter-on from one who takes the long route. This habit also builds toward mental math fluency by training students to find the most efficient path through every addition problem."
```

## Explainer

You know how to add numbers within 20, and you may have been using a counting-all strategy: for 7 + 3, starting at 1 and counting up to 10. That works every time — but it's slow. You count all 10 numbers just to reach an answer you could get in 3 steps. **Counting on** is the first big leap in addition efficiency: instead of starting from scratch each time, you start *at* the first number and count forward from there.

Here is how it works for 7 + 3. Hold 7 in your mind (or point to 7 on the number line). Now count on three more steps: 8, 9, 10. Stop. The last number you said — 10 — is the answer. You didn't count the 7 again; you started after it, counting only the steps you still needed. This is the essential rule: **hold the first number, count the second number**. Fingers, a number line, or mental tracking all work for keeping count of how many steps you've taken.

The most common mistake is including the starting number in your count — saying "7, 8, 9, 10" and thinking you counted 4 steps when you only added 3. The starting number is already in your head; you are adding to it, not counting it. Say "8" on the first step, not "7." Holding up a finger each time you say a new number can help: when you finish, count the fingers — the number of fingers should match the second number in the problem.

There is also a smarter habit to build: **always start from the bigger number**. For 2 + 8, don't count on 8 steps from 2 — instead, start at 8 and count on just 2 steps: 9, 10. Same answer, much less work. This connects to something you already know: addition numbers can switch places (2 + 8 = 8 + 2) without changing the sum. Counting on from the larger number turns every addition problem into the easiest version of itself.
