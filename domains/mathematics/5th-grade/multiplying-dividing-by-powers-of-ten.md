---
id: multiplying-dividing-by-powers-of-ten
title: Multiplying and Dividing by Powers of Ten
domain: mathematics
course: 5th-grade
prerequisites:
  - id: powers-of-ten
    type: hard
  - id: decimal-place-value
    type: hard
builds-toward:
  - multiplying-decimals
  - dividing-decimals
  - converting-metric-units
tags: [place-value, decimals, exponents, operations]
stage: concrete-operations
status: validated
---

# Multiplying and Dividing by Powers of Ten

## Core Idea
Multiplying by a power of ten shifts the decimal point to the right (making the number larger), and dividing by a power of ten shifts it to the left (making the number smaller). The number of places shifted equals the exponent. So 3.47 x 100 = 347 (shift right 2 places) and 3.47 / 10 = 0.347 (shift left 1 place). This is a direct consequence of place value: each shift moves every digit into the next-higher (or next-lower) position. This skill is fundamental for decimal operations, metric conversions, and scientific notation.

## How It's Best Learned
Use a place-value chart with a fixed decimal point and slide the digits left or right to show multiplication or division by 10, 100, 1000. This visual makes it clear that the digits move, not the decimal point (though the practical shortcut is to "move the decimal point"). Practice chains: start with 4.5, multiply by 10, multiply by 10 again, then divide by 100 to return. Connect to metric conversions (meters to centimeters is x100).

## Common Misconceptions
- Moving the decimal point the wrong direction.
- "Appending zeros" without understanding (works for whole numbers but not for decimals: 4.5 x 10 is 45, not 4.50).
- Confusing the number of places to shift with the number itself (multiplying by 100 shifts 2 places, not 100 places).

## Questions

```yaml
- question: "What is 4.7 × 100?"
  type: multiple-choice
  options:
    - "4.700"
    - "47"
    - "470"
    - "0.047"
  answer: 2
  explanation: "Multiplying by 100 = 10² shifts every digit two places to the left. The 4 moves from the ones place to the hundreds place, and the 7 moves from the tenths place to the tens place: the result is 470. Option B (47) is only one shift — that would be 4.7 × 10. Option A (4.700) adds zeros after the decimal but keeps the value identical to 4.7, which is the 'appending zeros' error. Option D is what dividing by 100 gives, not multiplying."

- question: "A student calculates 36.5 ÷ 10 and writes 36.50. What error did the student make?"
  type: multiple-choice
  options:
    - "No error — 36.50 is correct because you append a zero when dividing by 10"
    - "The student shifted the digits the wrong direction: dividing by 10 shifts digits right, giving 3.65"
    - "The student should have shifted digits left, giving 365"
    - "You cannot divide a decimal by 10"
  answer: 1
  explanation: "Dividing by 10 shifts every digit one place to the RIGHT (toward smaller place values): 36.5 ÷ 10 = 3.65. The 3 moves from tens to ones, the 6 from ones to tenths, the 5 from tenths to hundredths. The student confused dividing (shifts right, makes smaller) with multiplying (shifts left, makes larger). Writing 36.50 doesn't change the value at all — it still equals 36.5."

- question: "When you multiply a number by 10, each digit moves one place to the left in the place-value chart."
  type: true-false
  answer: true
  explanation: "Multiplying by 10 makes every digit worth 10 times as much, which means each digit moves into the next-higher position: ones become tens, tens become hundreds, tenths become ones. This leftward shift is why the product is larger. The decimal point itself is a fixed marker — it's the digits that move relative to it."

- question: "Multiplying any number by a power of ten generally produces a larger result."
  type: true-false
  answer: false
  explanation: "This only holds when multiplying by powers of ten greater than 1 (10, 100, 1000...). Multiplying by 10⁰ = 1 leaves the number unchanged. And dividing by a power of ten (which is multiplying by a negative power, like 10⁻¹) makes the number smaller. The correct rule: multiplying by 10ⁿ where n > 0 shifts digits left (larger); dividing by 10ⁿ shifts digits right (smaller)."

- question: "Explain why 4.5 × 10 = 45, not 4.50. What is wrong with the idea of 'just adding a zero'?"
  type: short-answer
  answer: "Adding a zero after the decimal (4.50) doesn't change the value — 4.5 and 4.50 are the same number. The correct operation is to shift each digit one place left: the 4 moves from the ones place to the tens place, and the 5 moves from the tenths place to the ones place. The result is 45. The 'add a zero' shortcut only works for whole numbers (like 5 × 10 = 50) because appending a zero there does shift every digit left. For decimals, you must actually move the digits — not append."
  explanation: "The 'add a zero' rule is a memorized shortcut that breaks down with decimals. Understanding that digits shift position (and why) prevents this error. 4.5 has a 4 in the ones place and a 5 in the tenths place. Multiplying by 10 promotes each digit one place: 4 → tens, 5 → ones. Result: 45. Writing 4.50 leaves the digit positions unchanged and gives the same value as 4.5."
```

## Explainer

You've already learned that our number system is built on **place value**: each position in a number is worth exactly 10 times the position to its right. The ones place is worth 1, the tens place is worth 10, the hundreds place is worth 100, and so on. Moving to the right works the same way in reverse — tenths are worth 1/10, hundredths are worth 1/100. Multiplying or dividing by a power of ten is simply the act of shifting every digit into the next-higher or next-lower position, and the number of positions shifted equals the **exponent** of 10 you're multiplying or dividing by.

When you **multiply by 10**, every digit becomes worth 10 times as much, which means each digit moves one position to the left. The 3 that was in the ones place (worth 3) now sits in the tens place (worth 30). When you multiply by 100 = 10², every digit shifts two places left. When you multiply by 1,000 = 10³, every digit shifts three places left. The digit values themselves don't change — their position does, and position is what determines value in our number system.

**Dividing by a power of ten** is the exact reverse: every digit shifts to the right. Dividing by 10 moves each digit one place right, making it worth one-tenth as much. So 347 ÷ 10 = 34.7: the 3 drops from hundreds to tens, the 4 drops from tens to ones, and the 7 drops from ones to tenths. The decimal point is just a marker that separates the whole-number part from the fractional part — it doesn't actually move. What moves are the digits relative to that fixed marker. The "move the decimal point" shortcut works, but understanding why it works — digits shifting positions — is what prevents errors and builds flexibility.

This skill connects directly to **metric conversions**, because the metric system is built on powers of ten. Converting 3.47 meters to centimeters means multiplying by 100 (there are 100 cm in 1 m): 3.47 × 100 = 347 cm. Converting 5,200 millimeters to meters means dividing by 1,000: 5,200 ÷ 1,000 = 5.2 m. Every time you see a metric prefix (kilo-, centi-, milli-), you're seeing a power of ten written as a word. Fluency with this skill makes unit conversion a matter of identifying the right power of ten and shifting — no formula required.
