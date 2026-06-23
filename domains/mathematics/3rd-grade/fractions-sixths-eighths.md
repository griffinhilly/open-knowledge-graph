---
id: fractions-sixths-eighths
title: 'Fractions: Sixths and Eighths'
domain: mathematics
course: 3rd-grade
prerequisites:
- id: fractions-equal-parts
  type: hard
- id: unit-fractions
  type: hard
- id: unit-fractions-halves-thirds-fourths-3rd
  type: hard
builds-toward:
- fractions-on-number-line
tags:
- fractions
- equal-parts
- sixths
- eighths
stage: concrete-operations
status: validated
---

# Fractions: Sixths and Eighths

## Core Idea
Sixths and eighths extend the fraction toolkit for thirds, fourths, and halves. Eighths are common in real-world measurement (ruler inches) and music. Students partition rectangles and circles into 6 and 8 equal parts, naming portions like ⅙, ⅛, ⅜.

## Questions

```yaml
- question: "A pizza is cut into 8 equal slices. A second identical pizza is cut into 6 equal slices. Maya eats one slice from each pizza. Did she eat the same amount from each?"
  type: multiple-choice
  options:
    - "Yes — she ate one slice from each, so she ate equal amounts from each pizza"
    - "No — she ate more from the pizza cut into 6 slices, because each of those slices is larger"
    - "No — she ate more from the pizza cut into 8 slices, because 8 is a larger number than 6"
    - "Yes — the pizzas are the same size, so one slice from each must be equal"
  answer: 1
  explanation: "When the same whole is cut into more pieces, each piece is smaller. ⅙ > ⅛ because the pizza cut into only 6 pieces has larger slices than the one cut into 8. Option C reveals the key misconception: a larger denominator does NOT mean a larger piece — it means more cuts, so each piece is smaller."

- question: "Which fraction represents the smallest amount?"
  type: multiple-choice
  options:
    - "½"
    - "⅙"
    - "⅛"
    - "⅓"
  answer: 2
  explanation: "When all numerators are 1, the fraction with the largest denominator is the smallest. ⅛ has denominator 8 — the whole is cut into the most pieces, so each piece is the smallest. The order from largest to smallest is: ½ > ⅓ > ⅙ > ⅛. This is counterintuitive because in regular counting, 8 > 6 > 3 > 2 — but as denominators, larger means smaller individual pieces."

- question: "One-eighth of a pizza is larger than one-sixth of the same pizza."
  type: true-false
  answer: false
  explanation: "⅛ < ⅙. When you cut the same whole into more pieces, each piece is smaller. Eight pieces are smaller than six pieces from the same pizza. Even though 8 > 6 as numbers, ⅛ < ⅙ as fractions — the denominator tells you how many equal pieces the whole was divided into, so more pieces means each piece is smaller."

- question: "The denominator of a fraction tells you how many equal pieces the whole is divided into."
  type: true-false
  answer: true
  explanation: "This is exactly what the denominator means. In ⅜, the denominator 8 tells you the whole was cut into 8 equal pieces. The numerator 3 tells you how many of those pieces you have. This is why comparing denominators — when numerators are the same — directly tells you which fraction is larger: a smaller denominator means fewer, bigger pieces."

- question: "Why does a larger denominator mean a smaller fraction when the numerators are equal? Explain using a real-world example."
  type: short-answer
  answer: "Because when you divide a whole into more pieces, each piece is smaller. If you cut a candy bar into 2 equal pieces, each piece is ½ — large. If you cut the same candy bar into 8 equal pieces, each piece is ⅛ — much smaller. More cuts means smaller pieces. So even though 8 > 2 as numbers, ⅛ < ½ as fractions."
  explanation: "This is the central counterintuitive insight about fractions with the same numerator. Students used to thinking 'bigger number = bigger amount' must learn that the denominator works in reverse: it counts divisions, not quantities. The more divisions, the smaller each share. This understanding is essential before comparing fractions, placing them on number lines, or working with equivalent fractions."
```

## Explainer

You already know what fractions mean from working with equal parts: a fraction names how many parts you have out of how many equal parts the whole is divided into. Sixths and eighths follow exactly the same idea — there are just more, smaller pieces. Imagine a pizza cut into 8 perfectly equal slices. Each slice is **one-eighth** of the pizza, written ⅛. If you take 3 slices, you have **three-eighths**, written ⅜. The bottom number (the **denominator**) tells you how many equal pieces the whole was cut into; the top number (the **numerator**) tells you how many of those pieces you have.

The most important pattern to notice is that a bigger denominator means smaller individual pieces. One-half (½) is a large piece — the whole cut in just two. One-sixth (⅙) is smaller, and one-eighth (⅛) is smaller still. This is counterintuitive at first because 8 > 6 > 2 as numbers, but as denominators they describe smaller and smaller shares. A useful picture: imagine cutting the same chocolate bar into 4 pieces vs. 8 pieces. The 8-piece version gives everyone smaller portions.

Eighths appear constantly in real-world measurement. A standard ruler divides each inch into 8 equal parts — those tiny marks between the inch numbers are eighths. A recipe might call for ⅜ cup of sugar. In music, an eighth note lasts half as long as a quarter note. Working with sixths and eighths now builds the fluency you'll need when fractions appear in geometry, measurement, and eventually on the number line — where understanding that ⅜ sits closer to ½ than to 0 requires exactly the kind of fraction sense you're developing here.
