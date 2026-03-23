---
id: fractions-on-number-line-comparison-3rd
title: Fractions on a Number Line and Comparison
domain: mathematics
course: 3rd-grade
prerequisites:
- id: fractions-on-number-line-3rd
  type: hard
- id: comparing-unit-fractions
  type: soft
builds-toward:
- equivalent-fractions
tags:
- fractions
- number-line
- comparing
stage: concrete-operations
status: validated
---

# Fractions on a Number Line and Comparison

## Core Idea
A number line shows fractions as distances from 0. Fractions to the right are greater. Number lines help students see that 1/2 = 2/4 and that fractions can be compared by position.

## Questions

```yaml
- question: "A student compares 1/8 and 1/3. Since 8 is greater than 3, the student concludes that 1/8 is greater than 1/3. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Fractions with 1 in the numerator cannot be compared directly"
    - "A larger denominator means the whole is divided into more pieces, making each piece smaller — so 1/8 is actually less than 1/3"
    - "Both fractions equal 1, so they are the same size"
    - "You need to find a common denominator before any comparison is possible"
  answer: 1
  explanation: "The denominator tells you how many equal pieces the whole is cut into — the more pieces, the smaller each one. Dividing a pizza into 8 slices gives you smaller slices than dividing it into 3. So 1/8 (one of eight small slices) is much less than 1/3 (one of three large slices). This is the key counterintuitive insight about unit fractions: larger denominator means smaller value, because the whole is being divided into more (therefore tinier) parts."

- question: "On a number line from 0 to 1, the fractions 1/2 and 2/4 land on the exact same point. What does this tell you?"
  type: multiple-choice
  options:
    - "The number line must be drawn incorrectly — two different fractions can't be at the same location"
    - "2/4 is slightly larger than 1/2 because it has a larger numerator"
    - "1/2 and 2/4 are equivalent fractions that represent the same amount"
    - "Fractions should only be compared on separate number lines to avoid confusion"
  answer: 2
  explanation: "Two fractions that land on the same point on the number line must represent the same distance from 0 — and therefore the same amount. This is the definition of equivalent fractions: different-looking symbols that name the same position. The number line makes equivalence visible in a way that symbols alone often don't: 1/2 and 2/4 really do occupy the same location because half of one whole is the same as two-fourths of one whole."

- question: "On a number line, a fraction that appears further to the right always represents a greater value than a fraction appearing to the left."
  type: true-false
  answer: true
  explanation: "True. This is the same rule that applies to whole numbers on a number line, extended to fractions. Position encodes magnitude: the further right, the closer to 1 (and beyond), the greater the value. This is why the number line is such a powerful tool for comparing fractions — you can read relative size directly from position without any additional calculation."

- question: "You can directly compare 2/3 and 3/4 by placing 2/3 on a number line divided into thirds and 3/4 on a separate number line divided into fourths, then comparing their positions."
  type: true-false
  answer: false
  explanation: "False. Fractions are only directly comparable when they are measured against the same whole and on the same number line. If one line shows thirds and another shows fourths, the two lines may be different lengths or their segments may not align — positions on different lines cannot be reliably compared. Both fractions must appear on the same number line (divided to show both thirds and fourths, or converted to a common denominator) to compare meaningfully."

- question: "Why does a fraction with a larger denominator (like 1/8) represent a smaller amount than a fraction with a smaller denominator (like 1/4), even though 8 > 4?"
  type: short-answer
  answer: "The denominator tells you how many equal parts the whole is divided into. More parts means smaller parts — just like cutting a pizza into 8 slices gives you smaller slices than cutting it into 4. When the numerator is 1, you get exactly one of those parts, so 1/8 (one small part) is less than 1/4 (one larger part)."
  explanation: "This is one of the most important counterintuitive insights in elementary fraction work. Students naturally apply whole-number logic ('bigger number = bigger value'), but denominators work inversely: the denominator counts divisions of the whole, and more divisions produce smaller pieces. On a number line, you can see this directly — the tick marks for eighths are packed more closely together than the tick marks for fourths, so each eighth-interval is physically shorter."
```

## Explainer

You already know how to place fractions on a number line: divide the segment from 0 to 1 into equal parts, then count parts from the left. A fraction like 3/4 sits three-quarters of the way from 0 to 1. The number line brings something powerful that fraction circles alone cannot provide: **position encodes size**. Whatever is further to the right is greater. This is the same rule you've used for whole numbers, and it works for fractions too.

To compare two fractions using a number line, you just need to see which fraction is further from 0. Because 3/4 sits to the right of 1/2, you can read directly that 3/4 > 1/2 — no additional reasoning required. The number line also makes visible something that can be hard to see from symbols alone: 1/2 and 2/4 land on exactly the same point. Two fractions that occupy the same position on the number line must be equal — that's the foundation of **equivalent fractions**.

The key to comparing fractions on a number line is that both fractions must be measured against the same-sized whole. You can only directly compare 3/4 and 2/4 on a number line whose segment from 0 to 1 is divided into fourths. If one line is divided into fourths and another into thirds, comparing positions across the two diagrams will give misleading results. This is why mathematicians insist that fractions are only comparable when they share the same whole.

Comparing unit fractions — fractions with numerator 1 — reveals a counterintuitive pattern: 1/4 is smaller than 1/2, even though 4 is bigger than 2. On a number line, dividing the same segment into more pieces makes each piece shorter, so 1/4 reaches only a quarter of the way to 1 while 1/2 reaches halfway. The bigger the denominator, the more the whole is sliced up, and the shorter each slice. Seeing this directly on the number line — the slices literally shrinking as you divide into more parts — is the clearest way to build lasting intuition for why larger denominators mean smaller pieces.
