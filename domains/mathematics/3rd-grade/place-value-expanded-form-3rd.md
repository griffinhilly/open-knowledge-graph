---
id: place-value-expanded-form-3rd
title: Place Value and Expanded Form
domain: mathematics
course: 3rd-grade
prerequisites:
- id: place-value-three-digits-3rd
  type: hard
builds-toward:
- place-value
tags:
- place-value
- expanded-form
- numbers
stage: concrete-operations
status: validated
---

# Place Value and Expanded Form

## Core Idea
Three-digit numbers can be written in expanded form to show the value of each digit. For example, 234 = 200 + 30 + 4. This makes clear that the 2 represents 200, not just 2.

## Questions

```yaml
- question: "What is the value of the digit 5 in the number 532?"
  type: multiple-choice
  options:
    - "5, because 5 is the digit itself"
    - "50, because 5 is in the tens place"
    - "500, because 5 is in the hundreds place"
    - "5,000, because it is the leading digit"
  answer: 2
  explanation: "In 532, the 5 is in the hundreds place, so its value is 5 × 100 = 500. The digit 5 looks the same everywhere, but its position determines what it is worth. Position is everything in a place value system. If the 5 were in the tens place (as in 253), it would be worth 50; in the ones place (as in 235), it would be worth just 5. Expanded form makes this visible: 532 = 500 + 30 + 2."

- question: "What is the correct expanded form of 305, and what does the zero in the tens place tell you?"
  type: multiple-choice
  options:
    - "300 + 50 + 0 — the zero holds the ones place and 5 is in the tens place"
    - "300 + 0 + 5 — the zero means there are no tens; the 5 is in the ones place"
    - "30 + 5 — zeros can be dropped from expanded form because they add nothing"
    - "300 + 5 — the zero is just a placeholder and doesn't affect other digits' values"
  answer: 1
  explanation: "305 = 300 + 0 + 5. The zero in the tens place is critical: it shows that there are no tens in this number. Without the zero, 305 and 35 would look the same in some notations — the zero holds the tens place so that the 3 stays in the hundreds position and the 5 stays in the ones position. Expanded form for 305 is written as 300 + 0 + 5, making explicit that the tens value is 0 × 10 = 0."

- question: "The digit 7 represents a different value in 70 than it does in 700."
  type: true-false
  answer: true
  explanation: "True. In 70, the 7 is in the tens place, so it is worth 7 × 10 = 70. In 700, the 7 is in the hundreds place, so it is worth 7 × 100 = 700. The same digit, placed in different positions, represents quantities ten times apart. This is the fundamental principle of the place value system: position determines value. Expanded form makes both values visible: 70 = 70 + 0, and 700 = 700 + 0 + 0."

- question: "In the number 234, the digit 2 has a value of 2."
  type: true-false
  answer: false
  explanation: "False. In 234, the digit 2 is in the hundreds place, so its value is 2 × 100 = 200. The digit 2 represents two hundred, not two. Students who say 'the 2 is worth 2' are reading the digit without considering its position. Expanded form — 234 = 200 + 30 + 4 — makes this explicit. The whole point of expanded form is to reveal what each digit is actually worth based on where it sits."

- question: "Explain why expanded form is more than just a notation exercise — how does understanding expanded form connect to doing addition with multi-digit numbers?"
  type: short-answer
  answer: "Expanded form reveals that multi-digit addition is really place-by-place addition. When you add 234 + 153, you are adding the hundreds (200 + 100 = 300), the tens (30 + 50 = 80), and the ones (4 + 3 = 7) separately, then combining: 300 + 80 + 7 = 387. Every column in the standard addition algorithm corresponds to one position in expanded form."
  explanation: "The column-by-column structure of the standard addition algorithm is directly an application of expanded form: you add the ones column, then the tens column, then the hundreds column — each column corresponds to one addend in the expanded representation. Understanding expanded form prevents students from treating multi-digit numbers as sequences of unrelated digits. It shows that 234 is not 'two, three, four' but 'two hundred plus thirty plus four' — a sum whose parts can be operated on independently and then recombined."
```

## Explainer

You already understand that three-digit numbers have a hundreds place, a tens place, and a ones place. **Expanded form** is simply a way of writing a number so that the full value of each digit is visible, rather than compressed into a single string. Writing 234 as 200 + 30 + 4 unpacks the number: the 2 is worth two hundred, the 3 is worth thirty, and the 4 is worth four.

The value of a digit depends entirely on its **position**. The same digit 5 means something completely different depending on where it sits: 5 in the ones place is just five, but 5 in the tens place is fifty, and 5 in the hundreds place is five hundred. Expanded form makes these hidden positional values explicit by writing them out as separate addends.

A useful way to build expanded form is to identify each digit and multiply it by its place value: 2 is in the hundreds place, so its value is 2 × 100 = 200. The 3 is in the tens place, so its value is 3 × 10 = 30. The 4 is in the ones place, so its value is 4 × 1 = 4. Writing all three gives the expanded form: 200 + 30 + 4. Going the other direction — collapsing expanded form back into a number — is simply addition: 200 + 30 + 4 = 234.

Expanded form is not just a notation exercise. It is the foundation of how multi-digit addition and subtraction work. When you add 234 + 153, you are really adding 200 + 100 = 300 in the hundreds, 30 + 50 = 80 in the tens, and 4 + 3 = 7 in the ones, then combining: 300 + 80 + 7 = 387. Every algorithm for adding or subtracting large numbers is secretly expanded form in action.
