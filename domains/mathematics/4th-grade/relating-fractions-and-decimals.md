---
id: relating-fractions-and-decimals
title: Relating Fractions and Decimals
domain: mathematics
course: 4th-grade
prerequisites:
  - id: intro-to-decimals
    type: hard
  - id: equivalent-fractions
    type: hard
builds-toward:
  - decimal-place-value
  - comparing-decimals
tags: [fractions, decimals, equivalence, number-sense]
stage: concrete-operations
status: validated
---

# Relating Fractions and Decimals

## Core Idea
Fractions and decimals are two notations for the same idea. Any fraction with a denominator of 10 or 100 converts directly to a decimal: 7/10 = 0.7 and 23/100 = 0.23. Other fractions can be converted by finding an equivalent fraction with a denominator of 10 or 100 (1/4 = 25/100 = 0.25) or by dividing the numerator by the denominator. Conversely, 0.6 = 6/10 = 3/5. Understanding this equivalence lets students move flexibly between representations, choosing whichever is more convenient for a given problem. Common benchmarks (1/2 = 0.5, 1/4 = 0.25, 3/4 = 0.75, 1/5 = 0.2) should become automatic.

## How It's Best Learned
Use 10x10 grids: shading 25 of 100 squares shows both 25/100 and 0.25 simultaneously. Practice converting fractions with denominators of 2, 4, 5, 10, 20, 25, and 100. Place both fractions and decimals on the same number line to reinforce that they name the same points.

## Common Misconceptions
- Writing 1/3 as 0.3 (confusing 1/3 with 3/10).
- Thinking fractions and decimals are fundamentally different kinds of numbers rather than different representations.
- Not recognizing that some fractions (like 1/3) produce repeating decimals, which is addressed more fully in later grades.

## Questions

```yaml
- question: "A student claims that 1/3 = 0.3 because 'there's a 3 in both.' What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — 1/3 and 0.3 are the same number and represent the same point on the number line"
    - "0.3 means 3/10, not 1/3 — the numbers look similar but represent very different quantities"
    - "1/3 should be written as 0.03, not 0.3"
    - "The student should divide 1 ÷ 3 to get the decimal, which equals 3.0"
  answer: 1
  explanation: "0.3 means 3 tenths, or 3/10 — not 1 third. 3/10 = 0.3 exactly, while 1/3 ≈ 0.333... (a repeating decimal that never ends). The confusion comes from surface similarity: both involve the digit 3. The actual conversion from fraction to decimal goes through the powers-of-ten structure. 1/3 cannot be written as a clean decimal because 3 does not divide evenly into 10 or 100."

- question: "To convert 3/4 to a decimal, a student finds that 4 × 25 = 100 and multiplies both numerator and denominator by 25, getting 75/100. What decimal does 75/100 equal?"
  type: multiple-choice
  options:
    - "0.075 — because 75 is placed three places after the decimal point"
    - "0.75 — because 75/100 means 75 hundredths"
    - "7.5 — because 75 divided by 10"
    - "0.34 — because the fraction converts digit by digit (3 and 4)"
  answer: 1
  explanation: "75/100 reads as '75 hundredths,' which is 0.75. The strategy works because the decimal system is built on powers of 10: hundredths place = /100. Since 4 × 25 = 100 and 3 × 25 = 75, we get 75/100 = 0.75. This is the benchmark ¾ = 0.75, which should become automatic."

- question: "The fraction 7/10 and the decimal 0.7 name exactly the same quantity."
  type: true-false
  answer: true
  explanation: "Decimals with one digit after the decimal point represent tenths. 0.7 literally means '7 tenths,' which is exactly what 7/10 means. They are two different notations for the same number — like writing 'a dozen' and '12.' Place them on a number line and they land on the exact same point."

- question: "Fractions represent parts of a whole, while decimals represent measurements — they are fundamentally different types of numbers that happen to look similar sometimes."
  type: true-false
  answer: false
  explanation: "Fractions and decimals are the same numbers expressed in different notations, not different types of numbers. 1/2 and 0.5 occupy exactly the same point on the number line. The decimal system is built on fractions with powers-of-ten denominators; 0.7 is simply shorthand for 7/10. Treating them as separate categories is the central misconception this topic is designed to correct."

- question: "Why can 1/4 be expressed as a clean decimal (0.25), but 1/3 cannot?"
  type: short-answer
  answer: "1/4 can be converted to an equivalent fraction with denominator 100 (since 4 × 25 = 100), giving 25/100 = 0.25. But 3 does not divide evenly into 10 or 100 — there is no whole number you can multiply 3 by to get 10 or 100 — so 1/3 produces a repeating decimal (0.333...) rather than a clean one."
  explanation: "Decimals are built on powers of 10. A fraction converts cleanly to a decimal only when its denominator can be made into 10 or 100 (or another power of 10) by multiplying by a whole number. 4 × 25 = 100, so 1/4 = 25/100 = 0.25. But 3 shares no factors with 10, so dividing 1 by 3 never terminates. This is why benchmark fractions like 1/4, 1/5, and 1/2 have clean decimal equivalents while 1/3, 1/6, and 1/7 do not."
```

## Explainer

You already know how to work with fractions, and you've been introduced to decimals like 0.7 and 0.25. The big idea here is that these are not two different kinds of numbers — they are two different **notations** for the same quantities. Just as "a dozen" and "12" name the same amount, ½ and 0.5 name the same point on the number line. Switching fluently between the two representations is a skill you'll use constantly.

The bridge between the notations is our decimal system, which is built on **powers of 10**. The first decimal place is tenths, the second is hundredths. So any fraction with denominator 10 converts directly: 7/10 = 0.7, 3/10 = 0.3. Any fraction with denominator 100 also converts directly: 47/100 = 0.47, 8/100 = 0.08. You can read the decimal aloud as the fraction: 0.47 says "47 hundredths," which writes as 47/100. The decimal notation is just a shorthand for fractions with powers-of-ten denominators.

Fractions with other denominators require a conversion step — and this is where your knowledge of **equivalent fractions** comes in. To convert ¼ to a decimal, ask: what can I multiply 4 by to get 10 or 100? Since 4 × 25 = 100, multiply both numerator and denominator by 25: 1/4 = 25/100 = 0.25. To convert ⅕, note 5 × 2 = 10, so 1/5 = 2/10 = 0.2. The strategy is always to find a multiplier that turns the denominator into 10 or 100, then read off the decimal. Not every fraction has a nice denominator — 1/3 cannot be written as a fraction with denominator 10 or 100 exactly, which is why it produces a repeating decimal (0.333...) rather than a clean one.

The benchmark conversions — ½ = 0.5, ¼ = 0.25, ¾ = 0.75, ⅕ = 0.2, 1/10 = 0.1 — appear so often in everyday contexts (prices, measurements, percentages) that they're worth making automatic. When a store advertises 25% off, that's ¼ off. When a recipe calls for ¾ cup, you can also measure 0.75 cups. The ability to move fluently between fractions and decimals is not just a school skill — it's the numerical literacy that underlies how quantities are communicated in the real world.
