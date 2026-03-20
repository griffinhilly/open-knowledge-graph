---
id: place-value-100-to-1000
title: 'Place Value: Hundreds, Tens, and Ones to 1000'
domain: mathematics
course: 2nd-grade
prerequisites:
- id: place-value-tens-and-ones
  type: hard
- id: place-value-hundreds
  type: hard
builds-toward:
- comparing-ordering-three-digit-numbers-2nd
- addition-three-digit-numbers-2nd
- subtraction-three-digit-numbers-2nd
tags:
- place-value
- 3-digit-numbers
- 100-to-1000
stage: concrete-operations
status: draft
---

# Place Value: Hundreds, Tens, and Ones to 1000

## Core Idea
Numbers to 1000 are built from hundreds, tens, and ones. 347 means 3 hundreds, 4 tens, and 7 ones. Understanding how digits represent different values is the foundation for larger calculations.

## How It's Best Learned
Use base-ten blocks or drawings to represent three-digit numbers. Start with numbers like 100, 200, 300, then add tens and ones. Show how changing a digit in different positions changes the number's value.

## Common Misconceptions
- Thinking 250 has 25 tens (it has 2 hundreds and 5 tens)
- Confusing the place of each digit
- Not understanding that 100 = 10 tens

## Questions

```yaml
- question: "What is the value of the digit 4 in the number 347?"
  type: multiple-choice
  options:
    - "4, because it is the digit 4"
    - "40, because it is in the tens place"
    - "400, because it is in the hundreds place"
    - "47, because it comes before the 7"
  answer: 1
  explanation: "In 347, the digit 4 is in the tens place, so its value is 4 × 10 = 40. The digit alone does not determine the value — its position does. The 3 is in the hundreds place (value 300), the 4 is in the tens place (value 40), and the 7 is in the ones place (value 7). This is the definition of place value: the same digit means something completely different depending on where it sits."

- question: "How many tens are in the number 250?"
  type: multiple-choice
  options:
    - "25 tens, because you can read '25' from the first two digits"
    - "5 tens, because the tens digit is 5"
    - "2 tens, because the hundreds digit is 2"
    - "0 tens, because 250 ends in 0"
  answer: 1
  explanation: "The tens digit in 250 is 5, so there are 5 tens (worth 50), in addition to 2 hundreds (worth 200) and 0 ones. The classic mistake is reading '25' from the first two digits and concluding '25 tens' — but that conflates the hundreds and tens digits into a single number. Each digit is read independently in its own place. 250 = 2 hundreds + 5 tens + 0 ones."

- question: "The digit 3 always represents the value 3, regardless of where it appears in a number."
  type: true-false
  answer: false
  explanation: "False. This is precisely what place value means. The digit 3 in 300 represents 3 × 100 = 300. The same digit 3 in 30 represents 3 × 10 = 30. In 3, it represents 3 × 1 = 3. The digit alone is not the value — the digit combined with its position is the value. This is the fundamental principle of our number system."

- question: "In the number 400, there are 4 hundreds but also 40 tens — both statements describe the same quantity."
  type: true-false
  answer: true
  explanation: "True. 400 = 4 hundreds = 40 tens, because 1 hundred = 10 tens. Both descriptions are correct representations of the same number. This flexibility — understanding that hundreds can be unpacked into tens — is important for addition and subtraction requiring regrouping. The bundling pattern (10 ones = 1 ten, 10 tens = 1 hundred) applies at every level."

- question: "Why is our number system called a 'place value' system? What does 'place' mean, and how does it change the value of a digit?"
  type: short-answer
  answer: "In a place value system, the value of a digit depends entirely on its position in the number, not just on the digit itself. Each position represents a different power of ten: the ones place, the tens place, the hundreds place. A digit is multiplied by the value of its place: 3 in the hundreds place equals 300; the same digit 3 in the ones place equals 3. 'Place' is the location; 'value' is what the digit is worth at that location."
  explanation: "This is why the zero in 307 matters: it holds the tens place empty (zero tens), ensuring the 3 stays in the hundreds place rather than sliding down. Without the placeholder zero, 307 would look like 37 — a completely different number. Place is meaning in our number system."
```

## Explainer

You already understand that a two-digit number like 47 means 4 tens and 7 ones. Now we extend exactly that logic one step further: we add a **hundreds place** to the left. Just as 10 ones bundle into 1 ten, 10 tens bundle into 1 hundred. That bundling pattern is the core rule of our number system.

So 347 means 3 hundreds, 4 tens, and 7 ones. You can picture this with base-ten blocks: three flat hundred-squares, four ten-rods, and seven individual cubes. The digit in each position tells you how many of that size block you have. Change the digit and you change the value — moving from 347 to 547 adds 2 more hundred-flats, making the number 200 larger.

The key insight is that **position carries meaning**. The same digit, 3, means something completely different depending on where it sits. In 300, the 3 means 300. In 30, the same 3 means only 30. In 3, it means 3. The digit alone is not the value — the digit combined with its place is the value. This is why the system is called **place value**.

The tricky case is numbers like 250 or 400. In 250, the 2 is in the hundreds place (worth 200), the 5 is in the tens place (worth 50), and the 0 in the ones place means zero ones. There are 2 hundreds and 5 tens — not 25 tens. When you see 100, remember it is just 10 tens compacted into a new level: 100 = 10 × 10. This understanding directly prepares you for adding and subtracting three-digit numbers, where you will regroup across all three place-value positions.

