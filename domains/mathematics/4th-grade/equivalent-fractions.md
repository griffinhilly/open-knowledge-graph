---
id: equivalent-fractions
title: Equivalent Fractions
domain: mathematics
course: 4th-grade
prerequisites:
- id: intro-to-fractions
  type: hard
- id: factors-and-multiples
  type: soft
- id: comparing-unit-fractions
  type: soft
- id: fractions-sixths-eighths
  type: soft
- id: whole-number-fractions
  type: soft
- id: prime-and-composite-numbers
  type: soft
- id: intro-to-fractions-4th-grade
  type: soft
builds-toward:
- comparing-fractions
- adding-fractions-like-denominators
- adding-fractions-unlike-denominators
tags:
- fractions
- equivalence
- number-sense
stage: concrete-operations
status: validated
---
# Equivalent Fractions

## Core Idea
Equivalent fractions name the same amount using different-sized parts. 1/2 = 2/4 = 3/6 = 50/100. You generate equivalent fractions by multiplying (or dividing) both the numerator and denominator by the same nonzero number -- this is the same as multiplying by 1 in a different form (e.g., 2/2 or 3/3). Visually, equivalent fractions cover the same area or land on the same point on a number line. This concept is essential for comparing fractions, finding common denominators, and simplifying fractions.

## How It's Best Learned
Use fraction strips or fraction bars: physically overlay 2/4 on top of 1/2 to see they match. Draw area models partitioned different ways. On a number line, mark both 1/3 and 2/6 at the same point. Then formalize the multiplication/division rule, connecting it back to why it works (subdividing or combining equal parts does not change the total amount).

## Common Misconceptions
- Adding the same number to numerator and denominator instead of multiplying (thinking 1/3 = 2/4 because you "added 1 to each").
- Not recognizing that simplifying a fraction produces an equivalent fraction, not a different number.
- Believing equivalent fractions must look the same visually (different-shaped models can show the same fraction).

## Questions

```yaml
- question: "Which fraction is equivalent to 2/3?"
  type: multiple-choice
  options: ["3/4", "4/6", "4/5", "5/6"]
  answer: 1
  explanation: "Multiplying both the numerator and denominator of 2/3 by 2 gives 4/6. The fraction represents the same amount — the same portion of a whole — just cut into more pieces."

- question: "You can make an equivalent fraction by adding the same number to both the numerator and denominator. For example, 1/3 = 2/4 because you add 1 to both."
  type: true-false
  answer: false
  explanation: "Adding does not work — it changes the value of the fraction. 1/3 ≈ 0.333 but 2/4 = 0.5, which are different. You must multiply (or divide) both numerator and denominator by the same nonzero number to preserve the fraction's value."

- question: "Why does multiplying both the numerator and denominator by the same number produce an equivalent fraction?"
  type: short-answer
  answer: "Because multiplying by n/n is the same as multiplying by 1, which does not change the value of the fraction. You are splitting each existing piece into more equal parts, so the total amount represented stays the same."
  explanation: "For example, 2/3 × 4/4 = 8/12. Since 4/4 = 1, the value is unchanged. Visually: if you cut each third into 4 smaller pieces, you now have 12 pieces total and 8 of them — but the shaded region is exactly the same size."
```

## Explainer

You already know that a fraction like 1/2 means one out of two equal parts of a whole. Now imagine taking that same half and drawing a line down the middle of it — suddenly you have four equal parts instead of two, and your piece covers two of them. So 1/2 and 2/4 describe exactly the same amount. They are equivalent fractions.

The key to generating equivalent fractions is multiplying both the numerator and denominator by the same nonzero whole number. For example: 1/2 × 3/3 = 3/6. Because 3/3 = 1, you haven't changed the value — you've just renamed it. Visually, you divided each of the two original parts into 3 smaller pieces, giving 6 total pieces with 3 of them filled. Same shaded area, different label.

A very common mistake is adding the same number to top and bottom instead of multiplying. It feels symmetric, but it breaks the value. 1/3 is about 0.33, but 2/4 = 0.5 — they are not the same. Addition does not preserve the ratio between numerator and denominator; multiplication does.

You can also go in reverse: if both the numerator and denominator share a common factor, divide both by it to get a simpler equivalent fraction. 8/12 ÷ 4/4 = 2/3. This is called simplifying (or reducing). The result is still the same fraction — just with smaller numbers.

Equivalent fractions are the foundation for everything you will do with fractions next: comparing fractions with different denominators, adding them, and subtracting them all require rewriting fractions in equivalent forms first.
