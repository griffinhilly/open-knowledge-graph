---
id: rounding-nearest-ten-3rd
title: Rounding to the Nearest Ten
domain: mathematics
course: 3rd-grade
prerequisites:
- id: place-value-whole-numbers
  type: hard
builds-toward:
- rounding-nearest-hundred-3rd
- estimation-multiplication-division
tags:
- rounding
- place-value
- number-sense
stage: concrete-operations
status: draft
---

# Rounding to the Nearest Ten

## Core Idea
Rounding to the nearest ten replaces a number with the closest multiple of 10. Numbers ending in 0–4 round down; 5–9 round up. A number line visually shows which ten is nearest: 34 is closer to 30, but 37 is closer to 40.

## Questions

```yaml
- question: "A student rounds 75 to 70, reasoning that '7 is the tens digit so 75 stays near 70.' What is the error?"
  type: multiple-choice
  options:
    - "The student should have looked at the tens digit, not the ones digit"
    - "When the ones digit is exactly 5, the convention is to round UP — so 75 rounds to 80, not 70"
    - "75 is exactly halfway, so there is no correct answer"
    - "The student should have rounded 75 to the nearest hundred instead"
  answer: 1
  explanation: "The ones digit of 75 is 5. The convention for a ones digit of 5 is always to round UP to the higher ten — this is a human convention, not a mathematical necessity, because 5 sits exactly halfway. So 75 rounds to 80. The tens digit tells you where you are; the ones digit tells you which direction to go. The student confused these roles."

- question: "What does the ones digit '3' in the number 53 tell you when rounding to the nearest ten?"
  type: multiple-choice
  options:
    - "53 rounds up to 60 because 3 is odd"
    - "53 rounds down to 50 because the ones digit 3 is in the range 0–4"
    - "53 rounds down to 50 because the tens digit is 5"
    - "53 rounds up to 60 because there are 5 tens"
  answer: 1
  explanation: "The ones digit is the only decision-maker when rounding to the nearest ten. A ones digit of 3 falls in the range 0–4, which means 53 is closer to 50 than to 60 (only 3 steps away from 50, and 7 steps from 60). Options C and D confuse the role of the tens digit — the tens digit tells you which ten you are near, but the ones digit tells you which direction to round."

- question: "A number's ones digit — and only the ones digit — determines whether you round up or down when rounding to the nearest ten."
  type: true-false
  answer: true
  explanation: "Correct. When rounding to the nearest ten, the tens digit tells you which two multiples of ten the number falls between, but the ones digit is the sole decision-maker for direction. Ones digits 0–4 → round down (stay at the lower ten); ones digits 5–9 → round up (go to the higher ten). No other digit is consulted."

- question: "When a number's ones digit is exactly 5, there is no single correct answer because the number is perfectly halfway between two tens."
  type: true-false
  answer: false
  explanation: "By mathematical convention, a ones digit of 5 always rounds UP to the higher ten. This is a convention — a human decision made for consistency — not a logical necessity, because the number is indeed equidistant. But the rule is fixed: 35 → 40, 45 → 50, 75 → 80. Knowing it is a convention (not a law of nature) helps you remember it without wondering why."

- question: "Explain how you would use a number line to decide whether 63 rounds to 60 or 70."
  type: short-answer
  answer: "On a number line, mark the multiples of ten: 60 and 70. Place 63 between them. Count the distance: 63 is 3 steps from 60 and 7 steps from 70. Since 63 is closer to 60, it rounds down to 60. This matches the rule: ones digit 3 is in the range 0–4, so round down."
  explanation: "The number line makes the concept visual — rounding asks 'which ten is nearest?' and the answer is literally the shorter distance. The ones digit rule is just a shortcut for what the number line shows directly: ones digits 0–4 place the number in the lower half of the gap (closer to the bottom ten); ones digits 5–9 place it in the upper half (closer or equal to the top ten)."
```

## Explainer

You already understand place value — that a number like 47 is made of 4 tens and 7 ones. Rounding uses that structure to replace a precise number with a nearby "round" number that is easier to work with. When you round to the nearest ten, you are asking: "Is this number closer to the ten below it or the ten above it?"

Picture a number line with the multiples of 10 marked: 30, 40, 50, and so on. Every other number lives between two of these markers. The number 34 sits between 30 and 40. Is it closer to 30 or 40? It is 4 steps away from 30 and 6 steps away from 40 — so it rounds down to 30. The number 37 is 7 steps from 30 and only 3 steps from 40 — so it rounds up to 40. The **ones digit** tells you which ten is closer: ones digits 0–4 mean round down (stay at the lower ten), ones digits 5–9 mean round up (go to the higher ten).

The rule for 5 is a convention worth knowing: when the ones digit is exactly 5, the number sits perfectly halfway between two tens. Mathematicians chose to round up in this case — it is a decision, not a mathematical necessity. So 35 rounds to 40, and 45 rounds to 50.

To round any number in your head: look only at the ones digit, ignore everything else. If the ones digit is 0, 1, 2, 3, or 4, replace it with 0 (round down). If it is 5, 6, 7, 8, or 9, add 1 to the tens digit and replace the ones with 0 (round up). So 73 → 70, and 78 → 80. This skill is the direct foundation for estimating multiplication and division, which you will use immediately in the next topic.
