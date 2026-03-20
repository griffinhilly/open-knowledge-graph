---
id: rounding-to-nearest-ten
title: Rounding to the Nearest Ten
domain: mathematics
course: 3rd-grade
prerequisites:
- id: place-value-hundreds
  type: hard
- id: number-line-to-1000
  type: soft
builds-toward:
- rounding-to-nearest-hundred
- estimation-strategies
- rounding-whole-numbers
tags:
- rounding
- estimation
- place-value
- nearest-ten
stage: concrete-operations
status: validated
---

# Rounding to the Nearest Ten

## Core Idea
Rounding to the nearest ten means replacing a number with the closest multiple of 10. For example, 47 rounds to 50 because 47 is closer to 50 than to 40. The rule: look at the ones digit — if it is 5 or more, round up; if it is 4 or fewer, round down. Numbers ending in exactly 5 round up by convention.

## How It's Best Learned
Open number lines showing two neighboring tens with the target number placed between them make rounding visual. Students mark the number and identify which ten it is closer to. Avoid introducing the rule before the concept.

## Common Misconceptions
- Students sometimes round down when the ones digit is 5 (should round up).
- Rounding 95 to the nearest ten produces 100, not 90 — students may be surprised the digit in the tens place changes.

## Questions

```yaml
- question: "A student is rounding 95 to the nearest ten. She reasons: 'the tens digit is 9, so I keep the tens digit and change the ones digit to 0 — the answer is 90.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — 90 is the correct answer"
    - "She should round to 100 because the ones digit is 5, so she rounds up, which carries into the hundreds place"
    - "She should always round to the lower ten when the tens digit is 9"
    - "95 cannot be rounded because it ends in 5"
  answer: 1
  explanation: "Rounding means finding the closest multiple of 10. On a number line, 95 sits exactly halfway between 90 and 100. By convention, when a number is exactly halfway, we round up — so 95 rounds to 100. Mechanically: the ones digit is 5, so round up. 'Rounding up' from 95 means the ones digit becomes 0 and the tens digit increases by 1 — but 9 tens + 1 = 10 tens, which carries into the hundreds place, giving 100. The tens digit does change in this case."

- question: "A student rounds every number in this list to the nearest ten: 23, 45, 78, 51, 95. Which numbers round to 50?"
  type: multiple-choice
  options:
    - "45 only"
    - "45 and 51"
    - "45, 51, and 23"
    - "51 only"
  answer: 1
  explanation: "45 rounds up to 50 (ones digit is 5, round up). 51 rounds down to 50 (ones digit is 1, less than 5, so round down to the lower ten, which is 50). 23 rounds to 20 (ones digit 3, round down). 78 rounds to 80 (ones digit 8, round up). 95 rounds to 100 (ones digit 5, round up — carries into hundreds). So both 45 and 51 round to 50."

- question: "The rule 'if the ones digit is 5 or more, round up' is just a trick teachers invented — it has no mathematical reason behind it."
  type: true-false
  answer: false
  explanation: "The rule follows directly from measuring distance on the number line. Any number with a ones digit of 5–9 is at least halfway from the lower ten to the upper ten, meaning the upper ten is as close or closer. The ones digit tells you exactly how far you've traveled past the lower ten: a ones digit of 5 means exactly halfway (round up by convention); 6–9 means past halfway (upper ten is closer). The rule is a shortcut for this distance logic, not an arbitrary convention."

- question: "47 is closer to 50 than to 40 on the number line."
  type: true-false
  answer: true
  explanation: "47 is 7 units above 40 and only 3 units below 50. Since 3 < 7, 47 is closer to 50 — so it rounds up to 50. The ones digit of 7 confirms this: any ones digit of 5 or more means the number is at least halfway to the upper ten, so the upper ten is closer."

- question: "Why does looking at the ones digit tell you which ten to round to?"
  type: short-answer
  answer: "The ones digit tells you how far the number has traveled past the lower ten. If the ones digit is 0–4, you haven't reached the halfway point (5), so the lower ten is closer and you round down. If the ones digit is 5–9, you're at or past the halfway point, so the upper ten is as close or closer and you round up. The ones digit is a shortcut for measuring distance between two neighboring tens."
  explanation: "Understanding the ones digit as a distance measure — not just a digit to look up in a rule — is what lets students handle edge cases like 95 correctly. Rather than memorizing exceptions, they can reason: 95 is 5 past 90 and only 5 below 100 — equidistant, so by convention round up to 100."
```

## Explainer

Rounding is about choosing the best approximate value for a number when you do not need or want an exact answer. Every whole number lives between two neighboring multiples of ten. The number 47, for example, sits between 40 and 50. Rounding to the nearest ten means picking whichever of those two neighbors is closer. Because 47 is 7 away from 40 but only 3 away from 50, it is closer to 50 — so it rounds to 50. Your prerequisite knowledge of the **number line** makes this visual: place 47 on a number line with 40 on the left and 50 on the right, and you can see it is nearer the right.

The ones digit is your shortcut for making that distance judgment without actually measuring. The ones digit tells you how far you have traveled *past* the lower ten. A ones digit of 0, 1, 2, 3, or 4 means you are less than halfway to the next ten — so the lower ten is closer, and you round down. A ones digit of 5, 6, 7, 8, or 9 means you are at least halfway — so the upper ten is closer (or equally close), and you round up. The rule "5 and above round up" is not arbitrary; it follows directly from measuring distance.

Place value — your main prerequisite — is what the rounding result is built from. When you round 47 to 50, you are changing the ones digit to 0 and increasing the tens digit by 1. When you round 43 to 40, you are changing the ones digit to 0 and keeping the tens digit the same. The tens digit is the only digit that matters in the result; all smaller digits become zero. This is exactly what "rounding to the nearest ten" means: you are replacing a precise number with the closest number that has a zero in the ones place.

One edge case deserves attention: what happens when rounding causes the tens digit to change in an unexpected way? Consider 95. The ones digit is 5, so you round up. But up from 95 is not 100 — wait, actually it is. 95 rounded up to the nearest ten is 100, not 90. The tens digit becomes 10, which carries over into a new hundreds digit. This surprises students, but the number line confirms it: 95 is exactly halfway between 90 and 100, and by convention we choose the upper neighbor. The same carry mechanism you know from addition applies here too.

