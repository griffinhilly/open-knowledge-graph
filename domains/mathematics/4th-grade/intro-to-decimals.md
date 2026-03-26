---
id: intro-to-decimals
title: Introduction to Decimals
domain: mathematics
course: 4th-grade
prerequisites:
- id: place-value-whole-numbers
  type: hard
- id: intro-to-fractions
  type: hard
- id: dollars-and-cents-notation
  type: soft
builds-toward:
- relating-fractions-and-decimals
- decimal-place-value
- comparing-decimals
tags:
- decimals
- place-value
- number-sense
stage: concrete-operations
status: validated
---
# Introduction to Decimals

## Core Idea
Decimals extend the place value system to represent quantities less than one. Just as moving left multiplies by 10, moving right of the ones place divides by 10: the tenths place is 1/10, the hundredths place is 1/100. The decimal point separates the whole-number part from the fractional part. So 3.47 means 3 ones + 4 tenths + 7 hundredths. Decimals are fractions written in place-value notation -- 0.25 is simply 25/100 or 1/4. Students encounter decimals primarily through money (dollars and cents) and measurement.

## How It's Best Learned
Start with money: $0.50 is 50 cents, half a dollar. Use base-ten blocks where the flat represents 1 whole, the rod represents 1 tenth, and the small cube represents 1 hundredth. Practice reading decimals aloud correctly ("three and forty-seven hundredths" not "three point four seven"), as proper reading reinforces place-value understanding.

## Common Misconceptions
- Reading 0.47 as "point forty-seven" and treating it like the whole number 47 (thinking 0.47 > 0.6 because 47 > 6).
- Thinking longer decimals are always larger (0.125 > 0.5 because 125 > 5).
- Not connecting decimals to fractions.

## Questions

```yaml
- question: "A student compares 0.47 and 0.6 and concludes that 0.47 is larger because 47 is greater than 6. What error is the student making?"
  type: multiple-choice
  options:
    - "The student should add a zero to get 0.60 first, then compare"
    - "The student is treating the decimal digits as whole numbers instead of reading them by place value (0.47 = 47/100; 0.6 = 60/100)"
    - "The student needs to convert both to percentages before comparing"
    - "The student forgot that numbers after the decimal point count in reverse order"
  answer: 1
  explanation: "0.47 means 47 hundredths (47/100), and 0.6 means 6 tenths (60/100). Written with a common denominator, 47/100 < 60/100, so 0.6 is greater. The student's error is treating '.47' and '.6' as bare whole numbers (47 vs 6) rather than reading them by their place values. Reading decimals correctly — 'forty-seven hundredths' vs 'six tenths' — immediately reveals that 60 hundredths beats 47 hundredths."

- question: "Which of the following correctly expresses the value of the decimal 0.3?"
  type: multiple-choice
  options:
    - "3 hundredths, or 3/100"
    - "30 tenths, or 30/10"
    - "3 tenths, or 3/10"
    - "0.3 is a unique type of number that cannot be written as a fraction"
  answer: 2
  explanation: "The first digit after the decimal point is the tenths place — it represents how many tenths you have. So 0.3 = 3/10, three tenths. Students who say '3 hundredths' are confusing the tenths place (first after the decimal) with the hundredths place (second after the decimal). Reading the decimal aloud correctly — 'three tenths' — forces you to say the denominator, which builds accurate place value understanding."

- question: "The decimal 0.25 and the fraction 1/4 represent exactly the same quantity."
  type: true-false
  answer: true
  explanation: "True. 0.25 = 25/100. Simplifying: 25/100 ÷ 25/25 = 1/4. Decimals and fractions are not two different types of numbers — they are two different notations for the same quantities. Every terminating decimal can be written as a fraction with a power-of-ten denominator. Recognizing this connection is essential for comparing, adding, and making sense of decimal arithmetic."

- question: "A decimal with more digits after the decimal point typically represents a larger number than one with fewer digits."
  type: true-false
  answer: false
  explanation: "False. 0.125 has three decimal places, but it equals 125/1000 = 1/8, which is less than 0.5 (= 1/2). More digits do not mean a larger value — place value determines size. This is exactly the misconception the Explainer warns about: treating 0.125 as 'bigger' because 125 > 5 ignores what those digits actually represent (125 thousandths vs 500 thousandths)."

- question: "Explain why reading '0.47' as 'forty-seven hundredths' rather than 'point four seven' helps you correctly compare it to 0.6."
  type: short-answer
  answer: "Reading '0.47' as 'forty-seven hundredths' tells you the denominator is 100, giving you 47/100. Reading '0.6' as 'six tenths' gives you 6/10 = 60/100. Now both fractions share the same denominator, and it's obvious that 47/100 < 60/100. The verbal reading forces you to name the place value, which is all the information you need to compare accurately."
  explanation: "This is the deepest practical implication of decimals-as-fractions. When you read decimals as bare digits ('point four seven'), you lose the denominator information. When you read them as fractions out loud, you immediately see that the comparison is 47 hundredths vs 60 hundredths — and 47 < 60 is obvious. The verbal habit encodes the mathematical relationship. This same habit prevents errors in ordering decimals, adding and subtracting them, and later in understanding decimal multiplication."
```

## Explainer

You already understand **place value** for whole numbers: each position in a number is worth ten times more than the position to its right. Ones, tens, hundreds, thousands — each step left multiplies by 10. The **decimal point** simply extends that pattern in the other direction. Each step right of the decimal point *divides* by 10: tenths (1/10), hundredths (1/100), thousandths (1/1000), and so on. The system is symmetric around the ones place. There is nothing new to memorize — the same base-ten logic you already know keeps on going past the point.

This means decimals are fractions in disguise — and you already know fractions too. The number 0.3 is not some mysterious new object; it is 3/10, three tenths. The number 0.47 is 47/100, forty-seven hundredths. Reading a decimal correctly forces you to say the denominator: "three tenths," "forty-seven hundredths." This is not just formality — it is exactly why 0.47 is *less* than 0.6. Written as fractions: 47/100 vs 6/10 = 60/100. Now it is obvious that 47/100 < 60/100. Students who read "point six" and "point forty-seven" as bare digits get confused; students who read "six tenths" and "forty-seven hundredths" almost never do.

Money gives you the most familiar example. You have been reading dollars and cents for years. $3.47 means 3 whole dollars, 4 dimes (tenths of a dollar), and 7 pennies (hundredths of a dollar). You already knew that 47 cents is less than 50 cents, which is half a dollar — you were reasoning about decimal place value without realizing it. Now you are just learning the formal notation that describes what you intuitively understand about coins.

The deepest idea here is that decimals and fractions are not two different kinds of numbers — they are two different notations for the same quantities. Every terminating decimal can be written as a fraction with a power-of-ten denominator, and vice versa. 0.25 = 25/100 = 1/4. This connection will be central when you start comparing, adding, and multiplying decimals. When in doubt about whether a decimal relationship makes sense, convert to a fraction and check your intuition against what you already know.

