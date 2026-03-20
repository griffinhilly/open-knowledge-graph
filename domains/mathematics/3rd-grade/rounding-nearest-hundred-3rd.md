---
id: rounding-nearest-hundred-3rd
title: Rounding to the Nearest Hundred
domain: mathematics
course: 3rd-grade
prerequisites:
- id: rounding-nearest-ten-3rd
  type: hard
builds-toward:
- estimation-multiplication-division
tags:
- rounding
- place-value
- number-sense
stage: concrete-operations
status: draft
---

# Rounding to the Nearest Hundred

## Core Idea
Rounding to the nearest hundred replaces a number with the closest multiple of 100. The tens digit determines rounding: 0–4 round down, 5–9 round up. For example, 247 rounds to 200 and 267 rounds to 300.

## Questions

```yaml
- question: "A student rounds 349 to the nearest hundred by looking at the 9 in the ones place and deciding to round up to 400. What error did they make?"
  type: multiple-choice
  options:
    - "9 is indeed the largest digit, so rounding up to 400 is correct"
    - "When rounding to the nearest hundred, you look at the tens digit (4), not the ones digit. Since 4 is in the range 0–4, 349 rounds DOWN to 300"
    - "349 rounds to 400 because it is an odd number"
    - "The student should have averaged 300 and 400 to get 350"
  answer: 1
  explanation: "The ones digit is irrelevant when rounding to the nearest hundred. Only the tens digit determines rounding direction, because the tens digit tells you whether the leftover (tens + ones) is above or below the halfway point of 50. In 349, the tens digit is 4, so the leftover (49) is less than 50 — round down to 300. Even though the ones digit is 9, 49 < 50, so the answer stays at 300."

- question: "Which digit do you examine when rounding a number to the nearest hundred?"
  type: multiple-choice
  options:
    - "The ones digit, because it shows the smallest unit of the number"
    - "The tens digit, because it determines whether the leftover amount is above or below the 50-unit halfway point between two hundreds"
    - "The hundreds digit, because you are rounding to hundreds"
    - "The largest digit in the number"
  answer: 1
  explanation: "The tens digit is the decision-maker. It represents the most significant part of the 'leftover' below the hundreds place. A tens digit of 5 or more means the leftover is at least 50 (closer to the next hundred); a tens digit of 4 or less means it's below 50 (closer to the current hundred). The ones digit can add at most 9, which cannot push a 4-tens leftover past 50 (40 + 9 = 49 < 50)."

- question: "The ones digit is irrelevant when rounding to the nearest hundred — only the tens digit determines which hundred a number rounds to."
  type: true-false
  answer: true
  explanation: "Correct. The tens digit tells you whether the combined leftover (tens + ones) is above or below 50. Even at its maximum, a ones digit of 9 with a tens digit of 4 gives a leftover of 49 — still below 50. So no matter what the ones digit is, a tens digit of 0–4 always means round down and 5–9 always means round up. The ones digit cannot change the outcome."

- question: "Rounding 350 to the nearest hundred gives 300, because the hundreds digit is 3."
  type: true-false
  answer: false
  explanation: "The hundreds digit tells you which hundred you are near — it does not determine rounding direction. To round 350, look at the tens digit: it is 5. Since 5 ≥ 5, round UP to 400. The hundreds digit (3) shows your current position; the tens digit (5) tells you which direction to go. Confusing these roles is the most common error when learning to round to hundreds."

- question: "Explain why the tens digit — not the ones digit — determines which hundred a number rounds to."
  type: short-answer
  answer: "When rounding to the nearest hundred, you are asking whether the leftover (everything below the hundreds place) is closer to 0 or to 100. That leftover ranges from 00 to 99, with 50 as the halfway point. The tens digit determines which side of 50 you are on: a tens digit of 5 or more means the leftover is at least 50 (round up); a tens digit of 4 or less means it is below 50 (round down). The ones digit adds at most 9, which cannot push a 4-tens leftover across the 50 threshold."
  explanation: "This is the same rule used for rounding to the nearest ten, just shifted one place to the left — instead of asking 'is the ones digit ≥ 5?', you ask 'is the tens digit ≥ 5?' The underlying logic is identical: you are looking at the digit that represents the 'halfway point' of the interval you're rounding within."
```

## Explainer

You already know how to round to the nearest ten — you look at the ones digit to decide whether to round up or down. Rounding to the nearest hundred works by the exact same rule, just shifted one place to the left: now you look at the **tens digit** to decide, and the result is always a multiple of 100 (…100, 200, 300, 400, …).

Think of the multiples of 100 as "landmarks" on the number line. Every three-digit number lives between two of these landmarks. For example, 247 lives between 200 and 300. To decide which landmark is closer, look at the tens digit of 247, which is 4. The rule: tens digit 0–4 means you're closer to the lower hundred (round down to 200); tens digit 5–9 means you're closer to the upper hundred (round up to 300). So 247 → 200, and 267 → 300.

Why the tens digit? Because the tens and ones together form a two-digit number between 00 and 99, and you're asking whether that part is closer to 00 (round down) or to 100 (round up). The halfway point is 50. If the tens digit is 5 or more, the leftover part is 50 or above — closer to the next hundred. If the tens digit is 4 or less, the leftover is below 50 — closer to the current hundred. The ones digit doesn't matter because even 99 doesn't push you over the halfway point once the tens digit is only 4 (49 < 50).

Rounding to the nearest hundred is one of the first tools you'll use for **estimation** in multiplication and division. When you need to estimate 4 × 247, rounding 247 to 200 turns it into 4 × 200 = 800 — a fact you can compute in your head. The rounder the numbers, the easier the mental math. That's the real payoff: rounding is not just about approximation for its own sake, it's a strategy that makes hard problems manageable.
