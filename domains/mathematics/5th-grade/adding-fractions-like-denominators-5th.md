---
id: adding-fractions-like-denominators-5th
title: Adding and Subtracting Fractions with Like Denominators (5th Grade)
domain: mathematics
course: 5th-grade
prerequisites:
  - id: adding-fractions-like-denominators
    type: hard
  - id: subtracting-fractions-like-denominators
    type: hard
  - id: mixed-numbers-and-improper-fractions
    type: hard
builds-toward:
  - adding-fractions-unlike-denominators
  - subtracting-fractions-unlike-denominators
tags: [fractions, addition, subtraction, mixed-numbers]
stage: concrete-operations
status: validated
---

# Adding and Subtracting Fractions with Like Denominators (5th Grade)

## Core Idea
Fifth grade extends like-denominator fraction arithmetic to include mixed numbers and regrouping. Adding 3 2/5 + 2 4/5: add the whole numbers (3 + 2 = 5) and the fractions (2/5 + 4/5 = 6/5 = 1 1/5), then combine (5 + 1 1/5 = 6 1/5). Subtracting may require regrouping: 4 1/3 - 1 2/3 requires converting 4 1/3 to 3 4/3 before subtracting. This parallels whole-number borrowing but with fractional units. Fluency with like-denominator operations with mixed numbers is the foundation for unlike-denominator work.

## How It's Best Learned
Use visual models (fraction strips or number lines) to show the regrouping: converting a whole into fractional parts. Practice both converting to improper fractions first (simpler algorithm) and working with mixed numbers directly (stronger conceptual understanding). Compare both methods.

## Common Misconceptions
- Not regrouping when the fractional part being subtracted is larger than the fractional part being subtracted from.
- Subtracting whole numbers and fractions independently without accounting for borrowing (computing 4 1/3 - 1 2/3 as 3 -1/3).
- Adding or subtracting denominators along with numerators.

## Questions

```yaml
- question: "What is 4 1/3 − 1 2/3?"
  type: multiple-choice
  options:
    - "3 1/3, because 4 − 1 = 3 and 1 − 2 = 1 (keeping the smaller numerator)"
    - "2 2/3, by first regrouping 4 1/3 as 3 4/3, then subtracting (3−1) + (4/3−2/3)"
    - "3 −1/3, because you subtract the fractions and whole numbers separately without regrouping"
    - "5 3/3, by combining the fractional parts"
  answer: 1
  explanation: "The correct answer is 2 2/3. Since 1/3 < 2/3, you cannot subtract without regrouping. Convert 4 1/3 to 3 4/3 (borrow one whole from the 4 and add 3/3 to the 1/3). Then: (3 − 1) + (4/3 − 2/3) = 2 + 2/3 = 2 2/3. Option C (3 −1/3) reveals the missing step — getting a negative fraction signals that regrouping was required but skipped."

- question: "A student computes 5 1/4 − 2 3/4 by subtracting whole numbers (5 − 2 = 3) and fractions (1/4 − 3/4 = −2/4) and writes the answer as 3 −2/4. What should the student have done first?"
  type: multiple-choice
  options:
    - "Added the fractions instead of subtracting, then adjusted the sign"
    - "Subtracted the fractions before subtracting the whole numbers"
    - "Regrouped 5 1/4 as 4 5/4 before subtracting, because 1/4 < 3/4"
    - "Converted both numbers to decimals before subtracting"
  answer: 2
  explanation: "Because 1/4 < 3/4, you cannot subtract the fractional parts directly without going negative. The fix is to regroup first: borrow one whole from the 5, converting 5 1/4 to 4 5/4 (4 + 4/4 + 1/4 = 4 + 5/4). Now subtract: (4 − 2) + (5/4 − 3/4) = 2 + 2/4 = 2 1/2. This is identical in logic to borrowing in whole-number subtraction — the new unit borrowed is just expressed in fractional form."

- question: "When adding mixed numbers with like denominators results in an improper fraction, you must convert it and add the extra whole to the whole-number sum."
  type: true-false
  answer: true
  explanation: "True. For example, 3 2/5 + 2 4/5: the fraction sum is 2/5 + 4/5 = 6/5, which is improper (greater than one whole). Convert 6/5 = 1 1/5, then add the extra whole to the whole-number sum: 5 + 1 1/5 = 6 1/5. Skipping this step — writing the answer as 5 6/5 — leaves an improper fraction in the fractional part, which is not standard mixed-number form."

- question: "To subtract 3 1/5 − 1 4/5, you can compute 3 − 1 = 2 and 1/5 − 4/5 = −3/5, giving the answer 2 −3/5."
  type: true-false
  answer: false
  explanation: "False. Getting a negative fraction is a signal that regrouping was required but not done. The correct first step is to regroup 3 1/5 as 2 6/5 (borrow one whole: 3 = 2 + 5/5, then 5/5 + 1/5 = 6/5). Now subtract: (2 − 1) + (6/5 − 4/5) = 1 + 2/5 = 1 2/5. A mixed number with a negative fraction is not a valid answer — it is evidence of a missing step."

- question: "Explain why regrouping is necessary when subtracting 4 1/3 − 1 2/3, and describe what the regrouped form of 4 1/3 looks like."
  type: short-answer
  answer: "Regrouping is necessary because the fractional part being subtracted (2/3) is larger than the fractional part you have (1/3). You cannot subtract 2/3 from 1/3 without going negative. To regroup, borrow one whole from the 4: 4 1/3 becomes 3 + 1 1/3 = 3 + 3/3 + 1/3 = 3 4/3. Now you have enough thirds to subtract."
  explanation: "Regrouping in fraction subtraction mirrors whole-number borrowing: instead of converting 1 ten into 10 ones, you convert 1 whole into fractional parts matching the denominator. For thirds, 1 whole = 3/3. Adding that to the existing 1/3 gives 4/3 — now 4/3 − 2/3 = 2/3 is straightforward. The concept is identical to 42 − 17 requiring borrowing from the tens column; the only difference is that the borrowed unit is denominated in thirds, not tens."
```

## Explainer

You already know how to add and subtract fractions with like denominators: keep the denominator, add or subtract the numerators. You also know how to convert between mixed numbers and improper fractions. Fifth grade brings these two skills together because the new challenge — mixed numbers with regrouping — requires both. The denominator rule hasn't changed; what is new is how you handle the whole-number parts and what to do when the fractional pieces don't cooperate.

Adding mixed numbers with like denominators starts simply. For 3 2/5 + 2 4/5, add the whole numbers (3 + 2 = 5) and the fractions (2/5 + 4/5 = 6/5) separately, then deal with the result. The fraction sum 6/5 is an **improper fraction** — the numerator exceeds the denominator, which means it is bigger than one whole. Convert it: 6/5 = 1 1/5. Now add the extra whole to your whole-number sum: 5 + 1 1/5 = 6 1/5. This is called **carrying** from the fraction part into the whole number, exactly like carrying in whole-number addition.

Subtraction is trickier because sometimes the fractional part you are subtracting is larger than the fractional part you have. Consider 4 1/3 − 1 2/3. You cannot subtract 2/3 from 1/3 without going negative. This is where **regrouping** (borrowing) comes in — the same concept you used in whole-number subtraction, now applied to fractions. Convert one whole into thirds: 4 1/3 becomes 3 + 1 1/3, and 1 1/3 = 4/3. So 4 1/3 = 3 4/3. Now subtract: (3 − 1) + (4/3 − 2/3) = 2 + 2/3 = 2 2/3. If you forget to regroup, you might compute 4 − 1 = 3 and 1/3 − 2/3 = −1/3, producing the nonsensical answer 3 − 1/3, which reveals the missing step.

An alternative that some students find cleaner: convert both mixed numbers to improper fractions first, then subtract, then convert back. 4 1/3 = 13/3 and 1 2/3 = 5/3, so 13/3 − 5/3 = 8/3 = 2 2/3. Same answer, different path. Both methods are valid; the regrouping method builds deeper understanding of the structure of mixed numbers, while the improper-fraction method is a reliable algorithm. Mastering both — and knowing when each is convenient — is the goal before you move on to unlike denominators, where finding a common denominator adds a new layer of complexity.
