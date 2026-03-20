---
id: rounding-to-nearest-hundred
title: Rounding to the Nearest Hundred
domain: mathematics
course: 3rd-grade
prerequisites:
- id: rounding-to-nearest-ten
  type: hard
- id: place-value-hundreds
  type: hard
builds-toward:
- rounding-whole-numbers
- estimation-strategies
- mental-math-add-subtract-hundreds
tags:
- rounding
- estimation
- place-value
- nearest-hundred
stage: concrete-operations
status: validated
---

# Rounding to the Nearest Hundred

## Core Idea
Rounding to the nearest hundred means replacing a number with the closest multiple of 100. Look at the tens digit: if it is 5 or more, round up; if it is 4 or fewer, round down. For example, 347 rounds to 300 and 682 rounds to 700. Rounding to hundreds is useful for estimating sums and differences of larger numbers.

## How It's Best Learned
Use number lines marked with hundreds to show where numbers fall. Have students name the two surrounding hundreds before deciding which is closer. Contrast with rounding to the nearest ten to solidify place-value understanding.

## Common Misconceptions
- Students look at the ones digit instead of the tens digit when rounding to the nearest hundred.
- 950 rounds to 1,000 (not 900), which surprises students who expect the hundreds digit to stay the same.

## Questions

```yaml
- question: "A student wants to round 463 to the nearest hundred. Which digit should they examine to make this decision?"
  type: multiple-choice
  options:
    - "The tens digit (6)"
    - "The ones digit (3)"
    - "The hundreds digit (4)"
    - "Both the ones and tens digits"
  answer: 0
  explanation: "When rounding to the nearest hundred, you examine the tens digit. The tens digit tells you which half of the hundred-interval the number falls in: tens digit 0–4 means the number is closer to the lower hundred, tens digit 5–9 means it's closer to the upper hundred. The ones digit is irrelevant for this decision. A very common error is examining the ones digit (as you would when rounding to the nearest ten) — in this case, that would give a wrong answer of 460 instead of 500."

- question: "A student rounds 350 to the nearest hundred. She says '300, because 50 is exactly in the middle — I'll round down to be safe.' What is the correct answer?"
  type: multiple-choice
  options:
    - "400 — the convention is to round up when the tens digit is exactly 5"
    - "300 — she is right that 50 is in the middle, so either answer is acceptable"
    - "350 — numbers exactly in the middle should not be rounded"
    - "400 — but only because the ones digit is 0"
  answer: 0
  explanation: "The standard rounding convention is: when the deciding digit is exactly 5, round up. So 350 rounds to 400, not 300. The student's reasoning ('in the middle so round down') reflects a natural instinct to be conservative, but it contradicts the mathematical convention. This convention exists so that rounding is consistent and predictable — 'round half up' is the standard rule taught at this level. The ones digit (option D) is not relevant to this decision."

- question: "When rounding 950 to the nearest hundred, the correct answer is 1,000, even though it crosses into a four-digit number."
  type: true-false
  answer: true
  explanation: "950 has a tens digit of 5, which means round up — increasing the hundreds digit by 1. The hundreds digit of 9 becomes 10, which carries over: 950 rounds to 1,000. This surprises many students who expect the answer to stay a three-digit number, but 1,000 is genuinely the closest multiple of 100 to 950. The number line confirms it: 950 is 50 away from 900 and 50 away from 1,000, and by convention ties round up."

- question: "To round a number to the nearest hundred, you examine the ones digit."
  type: true-false
  answer: false
  explanation: "To round to the nearest hundred, you examine the tens digit — the digit one place to the right of hundreds. Looking at the ones digit is the correct procedure when rounding to the nearest ten, not the nearest hundred. Each rounding level requires examining the digit immediately to the right of the target place: ones digit for rounding to tens, tens digit for rounding to hundreds. Confusing these levels is the most common error in place-value rounding."

- question: "A student rounds 847 by looking at the ones digit (7) and concludes the answer is 900. What mistake did they make, and what is the correct process?"
  type: short-answer
  answer: "The student looked at the ones digit instead of the tens digit. When rounding to the nearest hundred, the relevant digit is the tens digit, which tells you which half of the hundred-interval the number occupies. For 847, the tens digit is 4 (not 7). Since 4 < 5, the number is in the lower half of the 800–900 interval, so it rounds down to 800. The correct answer is 800, not 900. The procedure: identify the hundreds digit (8), look one place to the right (tens digit = 4), apply the rule (4 < 5, so keep the hundreds digit and write zeros), giving 800."
  explanation: "This error often comes from students applying the rule mechanically without tracking which place they are examining. A number line check (is 847 closer to 800 or 900?) confirms 800, since 847 is only 47 away from 800 but 53 away from 900."
```

## Explainer

Rounding to the nearest hundred is the same idea as rounding to the nearest ten — just one place-value level higher. From your earlier work with rounding to tens, you learned to look at the ones digit to decide whether to round the tens digit up or down. Now, to round to the nearest hundred, you look at the **tens digit** to decide whether to round the hundreds digit up or down.

The rule is the same: if the digit you're examining is 5 or more, round up; if it's 4 or less, round down. For 347, the tens digit is 4 — less than 5, so round down: 347 → 300. For 682, the tens digit is 8 — 5 or more, so round up: 682 → 700. After rounding, the tens and ones digits both become 0. The number lands exactly on a multiple of 100 because that's what "nearest hundred" means.

A number line is the best tool for building intuition here. Imagine a number line with 300 and 400 marked at either end. Where does 347 sit? It's closer to 300 than to 400 (only 47 away from 300, but 53 away from 400). So it rounds to 300. For any three-digit number, you can quickly estimate its position: the tens digit tells you which half of the hundred-interval you're in. Tens digit 0–4 means you're in the lower half (closer to the lower hundred). Tens digit 5–9 means you're in the upper half (closer to the higher hundred).

The trickiest case is when the tens digit is exactly 5, like 350. That number is exactly halfway between 300 and 400. The rounding convention — round up when the digit is 5 — gives you 400. Another surprise is rounding up through a century, like 950 → 1,000. Students expect the hundreds digit to change within the same century, but 950 is closer to 1,000 than to 900, so the number crosses into four digits. This is why the number line check is always more reliable than mechanical digit-watching alone.
