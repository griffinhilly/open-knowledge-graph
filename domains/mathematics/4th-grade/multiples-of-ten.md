---
id: multiples-of-ten
title: Multiplying by Multiples of Ten
domain: mathematics
course: 4th-grade
prerequisites:
  - id: place-value-whole-numbers
    type: hard
builds-toward:
  - multi-digit-multiplication
  - estimation-strategies
tags: [arithmetic, multiplication, place-value, patterns]
stage: concrete-operations
status: validated
---

# Multiplying by Multiples of Ten

## Core Idea
Multiplying by 10, 100, or 1,000 shifts every digit to a higher place value. 6 x 10 = 60 because 6 ones become 6 tens. This extends to multiples of ten: 30 x 40 = 1,200 because 3 x 4 = 12, then the two trailing zeros account for the tens x tens = hundreds relationship. Recognizing this pattern is critical for estimation, mental math, and understanding the partial products inside the multi-digit multiplication algorithm.

## How It's Best Learned
Use a place-value chart to show digits sliding left when multiplied by 10. Have students discover the "append zeros" pattern themselves through examples, then explain why it works using place value. Practice chains like 4 x 3, 4 x 30, 4 x 300, 40 x 300 to see the pattern generalize.

## Common Misconceptions
- Thinking "just add a zero" without understanding why, which breaks down with decimals later (0.5 x 10 is not 0.50).
- Miscounting zeros in products like 600 x 70.

## Questions

```yaml
- question: "A student calculates 0.5 × 10 by 'adding a zero' and writes the answer as 0.50. What is the correct answer, and why does the shortcut fail here?"
  type: multiple-choice
  options:
    - "0.50 — adding a zero is always the correct method for multiplying by 10"
    - "5 — the digit 5 shifts one place to the left, from tenths to ones"
    - "0.510 — you insert the zero after the 5 in the decimal"
    - "50 — any multiplication by 10 moves the answer past the decimal point"
  answer: 1
  explanation: "Multiplying by 10 is a place-value shift: every digit moves one column to the left. The 5 in the tenths place (0.5) shifts to the ones place, giving 5. 'Adding a zero' only mimics this shift for whole numbers — it fails with decimals because writing 0.50 doesn't actually change the value (0.5 = 0.50). Understanding the digit-shift principle, not the zero-appending shortcut, is what survives into decimal arithmetic."

- question: "What is 600 × 70?"
  type: multiple-choice
  options:
    - "4,200 — multiply 6 × 7, then add only the zeros from one factor"
    - "420 — multiply 6 × 7, keep one zero"
    - "42,000 — multiply 6 × 7 = 42, then add the three total trailing zeros"
    - "420,000 — count all digits, not just zeros"
  answer: 2
  explanation: "Strip the trailing zeros (two from 600, one from 70), multiply the remaining digits (6 × 7 = 42), then reattach all three zeros: 42,000. The zero-counting step is where errors cluster — be deliberate. Option A only adds zeros from one factor; option D overcounts by including non-zero digits."

- question: "When you multiply 4 × 300, the digit 4 effectively shifts two places to the left, producing 1,200."
  type: true-false
  answer: true
  explanation: "4 × 300 = 4 × (3 × 100). First 4 × 3 = 12, then 12 × 100 shifts every digit of 12 two places left: 1,200. The place-value shift model fully explains the result. The leading digits 1 and 2 have moved left twice relative to where 4 started."

- question: "The 'add a zero' shortcut for multiplying by 10 works for most type of number, including decimals."
  type: true-false
  answer: false
  explanation: "The shortcut works only for whole numbers. For decimals, 'adding a zero' to 0.5 gives 0.50, which equals 0.5 — unchanged. The actual operation is a place-value shift, and that shift must be performed correctly regardless of number type. Memorizing the shortcut without understanding why it works leaves students stranded when decimals appear."

- question: "Explain why the 'add a zero' shortcut works for whole numbers but fails for 0.5 × 10."
  type: short-answer
  answer: "For whole numbers, appending a zero shifts all digits one place to the left and fills the now-empty ones place with a zero placeholder — which is exactly what multiplying by 10 does. But for 0.5, the digit 5 is in the tenths place. Multiplying by 10 shifts it left to the ones place, giving 5. Writing '0.50' doesn't shift anything — it just adds a meaningless trailing zero. The digit-shift is the real operation; 'add a zero' is only a coincidental side-effect that works when the ones place was previously occupied."
  explanation: "The misconception is treating the shortcut as the rule instead of as a consequence of place-value shifting. Students who understand the underlying mechanism can handle any variant — decimals, large numbers, chains of multiples — without needing a separate rule for each case."
```

## Explainer

You already know place value — that the digit 6 means different things in 6, 60, and 600 depending on where it sits. Multiplying by a power of ten is precisely a **place-value shift**: every digit moves one column to the left for each factor of 10. When you compute 6 × 10, the 6 in the ones place becomes a 6 in the tens place, giving 60. When you compute 6 × 100, it shifts two places left, giving 600. The zeros you see in the answer aren't magic — they are placeholders that show how far the digits moved.

Now extend this to **multiples of ten**: numbers like 30, 40, 700, or 5,000. To multiply 4 × 30, think of it as 4 × (3 × 10). You can reorder: first multiply 4 × 3 = 12, then multiply 12 × 10 = 120. This works because multiplication is associative (you can group factors in any order). For 60 × 70: that's (6 × 10) × (7 × 10) = (6 × 7) × (10 × 10) = 42 × 100 = 4,200. The core multiplication gives you the leading digits; then you count the total zeros from both factors and append them.

A reliable procedure: (1) ignore all trailing zeros, (2) multiply the remaining digits, (3) count how many total zeros you stripped away, (4) reattach exactly that many zeros. For 600 × 70: strip zeros to get 6 × 7 = 42, count three total zeros (two from 600, one from 70), reattach to get 42,000. The zero-counting is where errors happen, so slow down there.

Understanding *why* this works — digit shifting, not formula memorizing — is crucial for what comes next. Multi-digit multiplication (like 46 × 38) is built out of exactly these partial products: 6 × 8, 6 × 30, 40 × 8, 40 × 30. Each of those is a multiples-of-ten calculation. And when you eventually multiply decimals (0.5 × 10), the place-value logic still applies — digits shift left — but you can't "add a zero" blindly, because 0.5 × 10 = 5, not 0.50. The understanding, not the shortcut, is what travels.
