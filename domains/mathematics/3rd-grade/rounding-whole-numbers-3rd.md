---
id: rounding-whole-numbers-3rd
title: Rounding to the Nearest Ten and Hundred
domain: mathematics
course: 3rd-grade
prerequisites:
- id: place-value-three-digits-3rd
  type: hard
builds-toward:
- estimation-products-3rd
tags:
- rounding
- tens
- hundreds
stage: concrete-operations
status: validated
---

# Rounding to the Nearest Ten and Hundred

## Core Idea
To round to the nearest ten, look at the ones digit: if 5 or more, round up; if less than 5, round down. To round to the nearest hundred, look at the tens digit. Number lines help visualize rounding.

## How It's Best Learned
Use number lines to see which ten or hundred is closest. Practice with many examples.

## Common Misconceptions
Using wrong rules; confusing 'round up' with 'make larger'; not understanding rounding's purpose.

## Questions

```yaml
- question: "To round 362 to the nearest hundred, which digit do you examine, and why?"
  type: multiple-choice
  options:
    - "The tens digit (6) — it tells you which half of the 300–400 interval 362 falls in"
    - "The ones digit (2) — it tells you the exact distance from the nearest hundred"
    - "The hundreds digit (3) — that is the place you are rounding to"
    - "Both the ones and tens digits — you need both to determine distance"
  answer: 0
  explanation: "When rounding to the nearest hundred, you look at the tens digit — the digit immediately to the right of the place you are rounding to. The tens digit acts as a dividing line: 0–4 means the number is in the lower half of the interval (closer to the lower hundred), 5–9 means it's in the upper half (closer to the higher hundred). For 362, the tens digit is 6, which is ≥ 5, so round up to 400. Examining the ones digit or the hundreds digit gives you no useful information about which hundred is closest."

- question: "A student says 'round up means make the number bigger.' Is this always true?"
  type: multiple-choice
  options:
    - "No — 'round up' means increase the rounding digit by 1 and replace digits to the right with zeros; the result is always the higher benchmark, which is larger than the original only if you were already past the midpoint"
    - "Yes — rounding always produces a number larger than the original"
    - "No — rounding always produces a number smaller than the original"
    - "Yes — but only when the digit being examined is odd"
  answer: 0
  explanation: "The term 'round up' refers to increasing the rounding place's digit by 1, not to the absolute result being larger than the original. When you 'round up,' the result is always the higher benchmark (e.g., 362 rounds up to 400, which is larger). But when you 'round down,' the result is the lower benchmark, which is smaller than the original. The confusion arises from the phrase 'round up' sounding like 'make bigger' — but it specifically means move to the upper benchmark, which happens when the number is in the upper half of the interval."

- question: "Rounding 47 to the nearest ten gives 50 because 47 is closer to 50 than to 40 on a number line."
  type: true-false
  answer: true
  explanation: "47 is 7 units away from 40 and only 3 units away from 50 — it is genuinely closer to 50. The 'look at the ones digit' rule confirms this: ones digit 7 ≥ 5, so round up to 50. The number line view and the digit rule always agree; the number line makes the reason visible, while the digit rule is a quick shortcut."

- question: "When rounding to the nearest ten, you examine the tens digit to decide whether to round up or down."
  type: true-false
  answer: false
  explanation: "When rounding to the nearest ten, you examine the ones digit — the digit one place to the right of the tens. The ones digit tells you which side of the ten-interval you're on. If it's 0–4, you're closer to the lower ten (round down); if it's 5–9, you're closer to the upper ten (round up). Examining the tens digit is the correct move when rounding to the nearest hundred, not the nearest ten. Confusing these is the most common procedural error in place-value rounding."

- question: "Why is a number line a more reliable tool for understanding rounding than memorizing the 'if the digit is 5 or more, round up' rule?"
  type: short-answer
  answer: "A number line makes rounding concrete: it shows rounding as a question of physical distance — which benchmark is this number closest to? The digit rule is a shortcut that works because the tens digit (for example) tells you which half of the hundred-interval the number is in, which determines the closer hundred. But students who only memorize the rule sometimes apply it mechanically — examining the wrong digit, or forgetting what 'round up' means. The number line lets you check any answer by asking: is this result actually the closer benchmark? It also makes the special case of ties (e.g., 350 is equidistant from 300 and 400) visible as a genuine ambiguity resolved by convention, rather than a mystery."
  explanation: "Understanding rounding as distance also helps students extend the concept correctly: the same logic applies whether you're rounding to the nearest ten, hundred, thousand, or any other place — always find the two surrounding benchmarks and ask which is closer."
```

## Explainer

Rounding is a way of replacing an exact number with a nearby, simpler number. You already understand place value for three-digit numbers — that gives you exactly the tool you need. Rounding to the nearest ten means finding the closest multiple of 10. Rounding to the nearest hundred means finding the closest multiple of 100. The goal is always the same: which "round" number is this closest to?

A **number line** makes rounding visual. To round 47 to the nearest ten, place it on a number line between 40 and 50. Is 47 closer to 40 or to 50? It's 7 away from 40 and only 3 away from 50, so it rounds to 50. To round 43, place it between 40 and 50 — it's 3 away from 40 and 7 away from 50, so it rounds to 40. The number line reveals that rounding is really about distance, not about following a rule blindly.

The standard rule — "look at the digit to the right of the place you're rounding to" — is a shortcut for the distance question. When rounding to the nearest ten, look at the **ones digit**. If it's 0–4, the number is closer to the lower ten, so round down. If it's 5–9, the number is closer (or tied) to the upper ten, so round up. When rounding to the nearest hundred, look at the **tens digit** the same way. For example, to round 362 to the nearest hundred: the tens digit is 6, which is ≥ 5, so round up to 400.

"Round up" means increase the target digit by one and replace all digits to the right with zeros — it doesn't always make the number larger in an absolute sense, but it moves toward the higher benchmark. "Round down" means keep the target digit the same and replace digits to the right with zeros. Rounding is useful whenever you need an estimate rather than an exact answer: about how many students are in the school? About how far is the drive? Estimation with rounded numbers lets you do quick mental math and check whether exact answers are in the right ballpark.
