---
id: three-digit-number-forms
title: Reading and Writing Three-Digit Numbers
domain: mathematics
course: 2nd-grade
prerequisites:
- id: place-value-hundreds
  type: hard
- id: skip-counting-by-100s
  type: soft
builds-toward:
- comparing-three-digit-numbers
- three-digit-addition
- number-line-to-1000
tags:
- three-digit
- place-value
- expanded-form
- word-form
- standard-form
stage: concrete-operations
status: validated
---
# Reading and Writing Three-Digit Numbers

## Core Idea
Three-digit numbers (100–999) can be expressed in three equivalent forms. Standard form is the usual notation: 583. Word form names the number in English: 'five hundred eighty-three.' Expanded form shows the value of each digit: 500 + 80 + 3. All three forms represent the same quantity; fluency moving between them deepens place-value understanding.

## How It's Best Learned
Use a place-value chart with columns labeled Hundreds, Tens, Ones. Practice translating a number from one form to another and back. Give students numbers with zeros in the middle (e.g., 405) to highlight the placeholder role of zero.

## Common Misconceptions
- Writing 'five hundred and eighty-three' — the word 'and' is reserved for the decimal point in formal usage.
- Writing 5083 for 583 (adding an extra zero).
- In expanded form, writing 5 + 8 + 3 instead of 500 + 80 + 3.

## Questions

```yaml
- question: "A student writes the expanded form of 583 as 5 + 8 + 3. What is wrong with this?"
  type: multiple-choice
  options:
    - "They used addition instead of multiplication"
    - "They failed to honor place value — the 5 represents 500, the 8 represents 80, and the 3 represents 3, so the correct expanded form is 500 + 80 + 3"
    - "They forgot to include a zero placeholder"
    - "They should have written the digits in reverse order"
  answer: 1
  explanation: "Expanded form exists to show the true value of each digit based on its position. The digit 5 in the hundreds place is worth 500, not 5. The digit 8 in the tens place is worth 80, not 8. Writing 5 + 8 + 3 = 16, while 583 is clearly not 16. This error shows the student knows the digit symbols but hasn't applied place value thinking — expanded form's entire purpose is to make that value explicit."

- question: "Which is the correct expanded form of 405?"
  type: multiple-choice
  options:
    - "4 + 0 + 5"
    - "400 + 05"
    - "400 + 5"
    - "40 + 5"
  answer: 2
  explanation: "In 405, the 4 is in the hundreds place (worth 400), the 0 is in the tens place (worth 0 tens = 0), and the 5 is in the ones place (worth 5). Expanded form is 400 + 0 + 5, which simplifies to 400 + 5 since adding 0 changes nothing. Option A (4+0+5) repeats the digit-not-value mistake. Option B (400+05) incorrectly writes 05, which isn't standard. Option D (40+5=45) omits the hundreds place entirely."

- question: "'Five hundred eighty-three' and 583 represent exactly the same quantity, expressed in different forms."
  type: true-false
  answer: true
  explanation: "True. Standard form (583), word form ('five hundred eighty-three'), and expanded form (500 + 80 + 3) are three different representations of the same number. They look different but denote the same point on the number line and the same quantity of objects. Fluency means being able to move between these forms and recognize they are equivalent."

- question: "The correct word form for 583 is 'five hundred and eighty-three' — the word 'and' connects the hundreds to the rest."
  type: true-false
  answer: false
  explanation: "False. In formal number naming, the word 'and' is reserved for the decimal point — it signals that a fractional part follows (as in 'five point three' becoming 'five and three tenths'). The correct word form for 583 is simply 'five hundred eighty-three.' Using 'and' in a whole number is a very common habit, but learning the convention now prepares students for decimals later."

- question: "Why does zero in the middle of a three-digit number (like 405) matter so much? What happens if you leave it out?"
  type: short-answer
  answer: "Zero is a placeholder that holds the tens position open. Without it, 405 would be written as 45, which is a completely different number (only 45, not 405). The zero communicates 'there are zero tens here' and ensures every digit sits in its correct place, preserving the hundreds value of the 4."
  explanation: "Place value works because each position has a fixed meaning. If you write 45 when you mean 405, you've collapsed two different positions into one, cutting the number's value by almost 90%. The placeholder zero is not 'nothing' — it's an active symbol that maintains the structural integrity of the number by keeping every digit in its rightful column."
```

## Explainer

You already understand place value with hundreds: each digit in a three-digit number occupies a position that determines its value — the hundreds place, the tens place, and the ones place. Reading and writing numbers in multiple forms is about making that hidden place-value structure *visible*. A number like 583 looks like three symbols side by side, but it is actually three separate quantities added together.

**Standard form** is the compact notation you use every day: 583. It is efficient but hides the structure. **Expanded form** tears the number apart to reveal what each digit is worth: 500 + 80 + 3. The 5 is not "five" — it is "five hundreds," which equals 500. The 8 is not "eight" — it is "eight tens," which equals 80. Expanded form makes this explicit. When you write 500 + 80 + 3 instead of 5 + 8 + 3, you are honoring the place-value rule your prerequisite covered.

**Word form** translates the number into English: "five hundred eighty-three." The structure of English number words mirrors place value almost perfectly. "Five hundred" names the hundreds digit. "Eighty" names the tens digit (eighty = eight tens). "Three" names the ones digit. One important rule: the word "and" belongs at the decimal point — it signals that a fraction is coming. So "five hundred eighty-three" has no "and" in it. You will see this convention again when you study decimals.

Zero in the middle of a number is the trickiest case and the most important one to get right. Consider 405. The standard form has a zero in the tens place — a **placeholder** that holds the position open even though there are no tens. In expanded form: 400 + 0 + 5, or simply 400 + 5. In word form: "four hundred five" (no mention of tens, because there are none). If you skip the placeholder zero in standard form and write 45, the number means something completely different. This is why the zero's job as a placeholder is so critical — it is the reason 405 ≠ 45.
