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

## Explainer

You already know how to round to the nearest ten — you look at the ones digit to decide whether to round up or down. Rounding to the nearest hundred works by the exact same rule, just shifted one place to the left: now you look at the **tens digit** to decide, and the result is always a multiple of 100 (…100, 200, 300, 400, …).

Think of the multiples of 100 as "landmarks" on the number line. Every three-digit number lives between two of these landmarks. For example, 247 lives between 200 and 300. To decide which landmark is closer, look at the tens digit of 247, which is 4. The rule: tens digit 0–4 means you're closer to the lower hundred (round down to 200); tens digit 5–9 means you're closer to the upper hundred (round up to 300). So 247 → 200, and 267 → 300.

Why the tens digit? Because the tens and ones together form a two-digit number between 00 and 99, and you're asking whether that part is closer to 00 (round down) or to 100 (round up). The halfway point is 50. If the tens digit is 5 or more, the leftover part is 50 or above — closer to the next hundred. If the tens digit is 4 or less, the leftover is below 50 — closer to the current hundred. The ones digit doesn't matter because even 99 doesn't push you over the halfway point once the tens digit is only 4 (49 < 50).

Rounding to the nearest hundred is one of the first tools you'll use for **estimation** in multiplication and division. When you need to estimate 4 × 247, rounding 247 to 200 turns it into 4 × 200 = 800 — a fact you can compute in your head. The rounder the numbers, the easier the mental math. That's the real payoff: rounding is not just about approximation for its own sake, it's a strategy that makes hard problems manageable.
