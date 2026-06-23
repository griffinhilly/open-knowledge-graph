---
id: place-value-whole-numbers
title: Place Value for Whole Numbers
domain: mathematics
course: 4th-grade
prerequisites:
  - id: skip-counting-by-10s-fluency
    type: soft
  - id: tens-and-ones-base-ten
    type: hard
builds-toward:
  - rounding-whole-numbers
  - comparing-ordering-whole-numbers
  - multi-digit-addition
  - multi-digit-subtraction
tags: [number-sense, place-value, arithmetic]
stage: concrete-operations
status: validated
---

# Place Value for Whole Numbers

## Core Idea

Our number system is positional -- the value of a digit depends on its position. The digit 3 means 3 ones, 30, 300, or 3,000 depending on where it sits. Each position is worth 10 times the position to its right. A student who understands place value can decompose numbers (4,527 = 4,000 + 500 + 20 + 7), compare multi-digit numbers by examining digits left to right, and understand why our standard algorithms for addition and subtraction work.

## How It's Best Learned

Use base-ten blocks or bundling sticks to make the grouping-by-tens structure physical. Have students compose and decompose numbers using expanded form. Place value charts help, but the physical trading (10 ones for 1 ten-rod, 10 ten-rods for 1 hundred-flat) is what builds real understanding. Extend to thousands and beyond once the pattern is clear.

## Common Misconceptions

- Treating digits independently rather than positionally (reading 305 as "thirty-five" because the zero is ignored).
- Not understanding that a zero in a position means "none of that unit" but still holds the place.

## Questions

```yaml
- question: "In the number 3,052, what does the digit 0 represent?"
  type: multiple-choice
  options: ["Zero tens — none of that unit, but the place is still held", "Nothing — it can be removed to give 352", "Zero ones", "A placeholder that makes the 3 worth more"]
  answer: 0
  explanation: "The 0 sits in the tens position, meaning there are zero tens. Without it, 352 is a completely different number (three hundred fifty-two vs. three thousand fifty-two). The zero is not decorative — it pushes the 3 and 5 into the correct positions."

- question: "The number 405 can be rewritten as 45 because the zero contributes no value."
  type: true-false
  answer: false
  explanation: "The zero in 405 occupies the tens place. Removing it collapses the number to 45 (forty-five), which is entirely different from 405 (four hundred five). The zero means 'zero tens' — it contributes no quantity of its own, but it holds the place so the 4 remains in the hundreds position."

- question: "Write 2,306 in expanded form."
  type: short-answer
  answer: "2,000 + 300 + 6"
  explanation: "Each digit is multiplied by the value of its position: 2 is in the thousands place (2,000), 3 is in the hundreds place (300), 0 is in the tens place (0 tens, so nothing added), and 6 is in the ones place (6). The expanded form makes the positional value of each digit explicit."
```

## Explainer

Our number system is called a **positional** or **place-value** system. Unlike Roman numerals, where X always means 10 regardless of where it appears, our system gives each digit a value that depends entirely on its position. The digit 3 alone tells you almost nothing — but once you know it sits in the hundreds place, you know it represents 300.

The organizing principle is simple: each position to the left is worth exactly ten times the position to its right. Ones × 10 = tens. Tens × 10 = hundreds. Hundreds × 10 = thousands. This is why we call it base-ten. When you write a number like 4,527, you are really writing a sum in disguise: 4,000 + 500 + 20 + 7. This "expanded form" makes the positional values visible.

The trickiest part for most students is the zero. A zero in a position doesn't mean "this place doesn't exist" — it means "there are zero of that unit here, and the place must still be held." In 305, the zero in the tens position is load-bearing: without it, the number collapses to 35. The zero is a placeholder that pushes the 3 into the hundreds column where it belongs.

Understanding place value is what makes arithmetic algorithms work. When you add two multi-digit numbers by "lining them up," you are aligning same-valued positions so you can add ones to ones and tens to tens. When you "carry" a 1, you are exchanging 10 smaller units for 1 of the next larger unit — the same trade you can make physically with base-ten blocks. Every standard algorithm for addition, subtraction, multiplication, and division is secretly a series of place-value manipulations.
