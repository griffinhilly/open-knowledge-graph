---
id: subtraction-within-20
title: Subtraction Within 20
domain: mathematics
course: 1st-grade
prerequisites:
- id: subtraction-within-10
  type: hard
- id: number-line-0-to-20
  type: soft
builds-toward:
- addition-subtraction-relationship
- addition-subtraction-word-problems
tags:
- subtraction
- arithmetic
stage: pre-formal
status: validated
---

# Subtraction Within 20

## Core Idea
Subtracting with minuends to 20 uses strategies including counting back, counting up, and relating to known addition facts. Understanding that subtraction 'undoes' addition is crucial.

## How It's Best Learned
Use ten frames, number lines, and physical objects. Model both 'take away' and 'how many more' contexts. Connect explicitly to addition facts.

## Common Misconceptions
- Counting back incorrectly (counting the starting number).
- Not recognizing the relationship between subtraction and addition (8-3 and 3+5).

## Questions

```yaml
- question: "A student solves 13 − 8 by counting: '13, 12, 11, 10, 9, 8' and writes the answer as 6. What went wrong?"
  type: multiple-choice
  options:
    - "The student used the wrong strategy — they should have drawn a ten frame"
    - "The student counted the starting number (13) as one of the steps; counting back from 13 means the first step lands on 12, not 13"
    - "The student subtracted in the wrong direction — you should always count forward"
    - "The student stopped too early; they should have counted back 9 steps"
  answer: 1
  explanation: "The classic counting-back error is including the starting number in the count. Counting back 8 from 13 means: 12 (one), 11 (two), 10 (three), 9 (four), 8 (five), 7 (six), 6 (seven), 5 (eight). The answer is 5. Starting the count at '13' means you've only actually subtracted 5, not 6."

- question: "Which of the following correctly shows that subtraction and addition are inverse operations?"
  type: multiple-choice
  options:
    - "15 − 8 = 7 because 7 + 9 = 16"
    - "15 − 8 = 7 because 8 + 7 = 15"
    - "15 − 8 = 7 because 15 − 7 = 8, and 7 is smaller"
    - "15 − 8 = 7 because 10 − 3 = 7 and 10 is close to 15"
  answer: 1
  explanation: "The 'think-addition' strategy works because every subtraction fact is secretly an addition fact. 15 − 8 = 7 because 8 and 7 are the two parts that make 15. If you know 8 + 7 = 15, you instantly know both 15 − 8 = 7 and 15 − 7 = 8. This inverse relationship is the key insight of this topic."

- question: "The phrase 'subtraction undoes addition' means that if you know 6 + 9 = 15, you can use that fact to immediately find 15 − 9 without counting."
  type: true-false
  answer: true
  explanation: "Yes — this is exactly the think-addition strategy. 6 + 9 = 15 means 15 − 9 = 6 and 15 − 6 = 9. The addition fact and the two subtraction facts are all part of the same fact family. Knowing any one of them gives you the others instantly, which is why connecting subtraction to addition is so powerful."

- question: "Counting back is typically the most reliable strategy for subtraction within 20."
  type: true-false
  answer: false
  explanation: "Counting back is error-prone (it's easy to miscount the starting number) and slow when the numbers are far apart. The think-addition strategy, make-ten strategy, and count-up strategy are all often faster and more accurate. For example, 17 − 9 is much easier solved by 'what plus 9 makes 17?' (answer: 8) or by counting up from 9 to 17 (8 steps), rather than counting back 9 steps from 17."

- question: "Why can subtraction mean both 'take away' and 'how far between two numbers'? Give an example of each interpretation for 13 − 8."
  type: short-answer
  answer: "Take-away: Start with 13 objects, remove 8, and 5 remain. Distance: Start at 8 and count up to 13 — the gap between them is 5 steps. Both give the same answer (5) because subtraction measures the difference between two numbers, whether you think of it as removing or as comparing."
  explanation: "Understanding that subtraction has two interpretations unlocks two different solving strategies. 'Take away' naturally leads to counting back. 'How far between?' naturally leads to counting up (or think-addition). Choosing the right interpretation for a given context makes the calculation easier — for instance, 13 − 12 is much easier to solve by counting up (just 1 step) than by counting back 12 steps."
```

## Explainer

You already know how to subtract within 10 — taking away small numbers from numbers up to 10. Subtracting within 20 extends that skill, but the key leap isn't just using bigger numbers: it's discovering smarter strategies that make the work much easier.

The most powerful strategy is called **think-addition** (or "think of the missing addend"). Instead of counting backward from 13 to find 13 − 8, you ask yourself: "8 plus *what* makes 13?" If you know that 8 + 5 = 13, then 13 − 8 = 5. Subtraction and addition are two sides of the same coin — this is what the Core Idea means when it says subtraction "undoes" addition. Every subtraction fact is secretly an addition fact waiting to be used.

A **ten frame** makes this visual. Think of 13 as a full row of 10 plus 3 more. To subtract 5, you first take the 3 from the bottom row, and then take 2 more from the ten — leaving 8. This "make ten" thinking breaks bigger subtractions into two smaller ones you already know. For 15 − 6: take 5 to get to 10, then take 1 more, leaving 9. You're using the structure of 10 as a stepping stone.

**Counting up** is another efficient approach. Instead of counting backward from 17 to find 17 − 9, you start at 9 and count up: "10, 11, 12, 13, 14, 15, 16, 17" — that's 8 steps. You arrive at the answer 8 by adding forward rather than subtracting backward. This is especially useful when the two numbers are close together (like 15 − 12), where counting up takes very few steps.

The big picture is this: subtraction isn't just "take away." Sometimes it means "how many more does one number have than another?" and sometimes it means "how far is it between two numbers?" Depending on which way you think about it, a different strategy becomes easiest. Having several strategies — think-addition, make-ten, count up, count back — lets you pick the right tool for each problem.
