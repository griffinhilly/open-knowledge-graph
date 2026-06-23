---
id: comparing-unit-fractions
title: Comparing Unit Fractions
domain: mathematics
course: 3rd-grade
prerequisites:
- id: unit-fractions
  type: hard
- id: fractions-on-number-line
  type: soft
- id: fractions-sixths-eighths
  type: soft
- id: fractions-halves-fourths-thirds-2nd
  type: hard
- id: unit-fractions-halves-thirds-fourths-3rd
  type: hard
- id: unit-fractions-sixths-eighths-3rd
  type: soft
builds-toward:
- comparing-fractions
- equivalent-fractions
tags:
- fractions
- comparing
- ordering
- unit-fractions
stage: concrete-operations
status: validated
---
# Comparing Unit Fractions

## Core Idea
When comparing unit fractions (fractions with numerator 1), the fraction with the larger denominator is actually smaller: 1/8 < 1/4 < 1/2. This is because dividing a whole into more parts makes each part smaller. Students compare using fraction strips, number lines, and reasoning about equal wholes.

## How It's Best Learned
Lay fraction strips for 1/2, 1/3, 1/4, 1/6, and 1/8 side by side. The visual directly shows the relative sizes. Emphasize that comparison only works when the wholes are the same size.

## Common Misconceptions
- The classic error: 1/8 > 1/4 because 8 > 4. Students need repeated concrete experience to overcome this.
- Students may correctly compare unit fractions but then revert to the larger-denominator = larger-fraction error when solving problems numerically.

## Questions

```yaml
- question: "Which fraction is larger: 1/6 or 1/3?"
  type: multiple-choice
  options:
    - "1/6, because 6 is greater than 3"
    - "1/3, because dividing a whole into fewer parts makes each part larger"
    - "They are equal because both fractions have 1 in the numerator"
    - "1/6, because more pieces means a greater total"
  answer: 1
  explanation: "1/3 is larger. When you divide a whole into 3 equal parts, each part is bigger than when you divide the same whole into 6 equal parts. The denominator tells you how many cuts were made — more cuts means smaller pieces. The tempting wrong answer (1/6, because 6 > 3) is the classic misconception: applying whole-number reasoning ('bigger number = bigger') to fractions, where the relationship is inverted for unit fractions."

- question: "One pizza is cut into 8 equal slices. An identical pizza is cut into 4 equal slices. If you take one slice from each pizza, which slice is larger?"
  type: multiple-choice
  options:
    - "The slice from the 8-piece pizza — there are more pieces, so each must be bigger"
    - "They are the same size because both are 'one slice'"
    - "The slice from the 4-piece pizza — fewer cuts means each piece is larger"
    - "The slice from the 8-piece pizza — 8 is greater than 4"
  answer: 2
  explanation: "1/4 of the pizza is a bigger piece than 1/8 of the same pizza. Cutting something into more pieces makes each piece smaller, not larger. Options A and D both fall for the misconception that a bigger denominator means a bigger fraction. Option B ignores that 'one slice' means different things depending on how many total slices there are."

- question: "1/8 is greater than 1/4 because 8 is a greater number than 4."
  type: true-false
  answer: false
  explanation: "This is the most common error with unit fractions. 8 > 4 as whole numbers, but 1/8 < 1/4 as fractions. The denominator tells you how many equal parts the whole was divided into — the more parts, the smaller each one. So 1/8 means one of eight tiny pieces, while 1/4 means one of four larger pieces. The fraction with the larger denominator is actually smaller."

- question: "As the denominator of a unit fraction increases, the value of the fraction decreases."
  type: true-false
  answer: true
  explanation: "This is the inverse relationship at the heart of comparing unit fractions. Going from 1/2 → 1/3 → 1/4 → 1/6 → 1/8, each fraction is smaller than the one before it, even though the denominators are getting larger. More equal parts means smaller pieces."

- question: "Why is 1/10 smaller than 1/2, even though 10 is a larger number than 2? Explain using the idea of dividing a whole into parts."
  type: short-answer
  answer: "When you divide a whole into 10 equal parts, each part is much smaller than when you divide the same whole into only 2 equal parts. 1/10 means one of ten tiny pieces; 1/2 means one of two large pieces. The bigger the denominator, the more pieces the whole was cut into, which means each individual piece is smaller. So even though 10 > 2, the fraction 1/10 is far smaller than 1/2."
  explanation: "The key insight is the inverse relationship: denominator and piece size move in opposite directions for unit fractions. This is counterintuitive because students are used to larger numbers meaning larger amounts. The physical model (pizza slices, fraction strips) makes this relationship concrete and visible."
```

## Explainer

A **unit fraction** is any fraction with a 1 in the numerator: 1/2, 1/3, 1/4, 1/8, and so on. You've already learned what these fractions mean — 1/4 is one equal part when a whole is cut into 4 equal pieces, and 1/8 is one equal part when a whole is cut into 8 equal pieces. Comparing unit fractions means asking: which of those single pieces is larger?

Here is the key insight: the more pieces you cut a whole into, the smaller each piece gets. Imagine one pizza cut into 4 slices versus the same pizza cut into 8 slices. If you take one slice from the 4-slice pizza, you get a bigger piece than if you take one slice from the 8-slice pizza. So 1/4 > 1/8, even though 4 < 8. The denominator tells you how many cuts were made — a bigger denominator means more cuts, which means smaller pieces.

This is the **inverse relationship** between denominator size and fraction size for unit fractions: as the denominator grows, the fraction shrinks. Put them in order from largest to smallest: 1/2 > 1/3 > 1/4 > 1/6 > 1/8. Each step introduces more equal parts, so each individual part is smaller. Fraction strips lay this out visually — line up a 1/2 strip next to a 1/8 strip and you can see directly that the 1/2 piece is four times as long.

One critical requirement that's easy to forget: comparisons only make sense when the **wholes are the same size**. One slice of a large pizza and one slice of a small pizza are both "1/4," but they're not the same amount of food. In math problems, assume the wholes are equal unless told otherwise — this is an assumption baked into every valid fraction comparison.
