---
id: comparing-fractions
title: Comparing and Ordering Fractions
domain: mathematics
course: 4th-grade
prerequisites:
- id: intro-to-fractions
  type: hard
- id: equivalent-fractions
  type: hard
- id: fractions-halves-thirds-fourths
  type: soft
- id: comparing-unit-fractions
  type: soft
- id: fractions-on-number-line
  type: soft
- id: comparing-unit-fractions-3rd
  type: soft
builds-toward:
- adding-fractions-unlike-denominators
- comparing-decimals
tags:
- fractions
- comparison
- number-sense
stage: concrete-operations
status: validated
---
# Comparing and Ordering Fractions

## Core Idea
To compare fractions, students need strategies beyond "bigger number means bigger fraction." When denominators are the same, the fraction with the larger numerator is greater (3/5 > 2/5). When numerators are the same, the fraction with the smaller denominator is greater (1/3 > 1/5, because thirds are larger pieces). For fractions with different numerators and denominators, finding a common denominator or using benchmark fractions (0, 1/2, 1) are the standard approaches. Students should use <, >, and = symbols and be able to order sets of fractions.

## How It's Best Learned
Use fraction strips, area models, and number lines to make comparisons visual before introducing algorithmic methods. Benchmark reasoning is powerful: "Is this fraction more or less than 1/2?" Practice with carefully chosen pairs that target each strategy (same denominator, same numerator, neither). Avoid teaching cross-multiplication as the only method -- it works but builds no number sense.

## Common Misconceptions
- Thinking larger denominators mean larger fractions (believing 1/8 > 1/4 because 8 > 4).
- Comparing numerators and denominators separately (thinking 3/4 < 2/3 because 3 < 4 and 2 < 3).
- Only being able to compare when denominators are already the same.

## Questions

```yaml
- question: "A student claims that 1/8 is greater than 1/4 because 8 is greater than 4. What is wrong with this reasoning?"
  type: multiple-choice
  options:
    - "Nothing — larger denominators do mean larger fractions"
    - "The student confused the numerator and denominator positions"
    - "The denominator tells you how many equal pieces the whole is cut into, so more pieces means each piece is smaller — making 1/8 less than 1/4"
    - "You cannot compare fractions unless the numerators are the same"
  answer: 2
  explanation: "The denominator tells you the size of each piece, and the relationship is inverse: cutting a whole into 8 pieces gives smaller slices than cutting it into 4 pieces. So 1/8 is one small slice while 1/4 is one larger slice — 1/8 < 1/4. The student applied whole-number thinking (bigger number = bigger value) to a part that describes size, not count. This is the most common fraction comparison error."

- question: "Which of the following strategies correctly compares 3/4 and 5/6 without converting to decimals?"
  type: multiple-choice
  options:
    - "Compare numerators: 5 > 3, so 5/6 > 3/4"
    - "Compare denominators: 6 > 4, so 3/4 > 5/6"
    - "Find a common denominator of 12: rewrite as 9/12 and 10/12; since 10 > 9, then 5/6 > 3/4"
    - "Both fractions are close to 1, so they are equal"
  answer: 2
  explanation: "Finding a common denominator (12) rewrites both fractions with the same-sized pieces, making the comparison straightforward: 9 twelfths vs. 10 twelfths — 10/12 > 9/12, so 5/6 > 3/4. Option A fails because you cannot compare numerators when denominators differ. Option B applies inverted denominator logic incorrectly — larger denominator means smaller pieces, but you also need to account for how many pieces you have. Neither shortcut works here; the common denominator method does."

- question: "When two fractions have the same numerator, the fraction with the smaller denominator is the greater fraction."
  type: true-false
  answer: true
  explanation: "With equal numerators, you are comparing equal numbers of pieces, so piece size determines which is greater. Smaller denominator = larger pieces. For example, 2/3 vs. 2/5: both have 2 pieces, but thirds are larger than fifths, so 2/3 > 2/5. This is the 'same numerator' strategy — a reliable shortcut that depends on understanding what the denominator represents."

- question: "The most reliable way to compare any two fractions is to look at which fraction has the larger denominator."
  type: true-false
  answer: false
  explanation: "Larger denominators mean smaller pieces — so a larger denominator does NOT automatically mean a larger fraction. This strategy only works in a specific case (same numerator), and even then the logic is inverse: the larger denominator gives the *smaller* fraction. For fractions with different numerators and denominators, you need to find a common denominator, use benchmark fractions, or use another strategy that accounts for both parts of the fraction."

- question: "Why does a larger denominator produce smaller pieces, and how does this affect which fraction is greater when the numerators are the same?"
  type: short-answer
  answer: "The denominator tells you how many equal pieces the whole is divided into. More pieces means each piece is smaller — just as cutting a pizza into 8 slices gives smaller slices than cutting it into 4. When numerators are equal (same number of pieces), the fraction with smaller pieces is the smaller fraction. So 1/8 < 1/4 because eighths are smaller than fourths."
  explanation: "This inverse relationship — larger denominator, smaller piece — is the core insight of fraction comparison. It runs against whole-number intuition and is the source of the most persistent comparison errors. Understanding *why* the denominator is inverse (more cuts = smaller pieces) lets students reason through any same-numerator comparison correctly instead of guessing."
```

## Explainer

You already understand what a fraction means — a numerator counting how many pieces you have, a denominator telling you how many equal pieces make up the whole — and you can create equivalent fractions by multiplying or dividing numerator and denominator by the same number. Comparing fractions is where that understanding gets put to work in real comparisons.

When denominators are the same, comparison is straightforward: 3/7 > 2/7 because both fractions use the same size pieces (sevenths), and 3 of them is simply more than 2 of them. This is like comparing 3 cookies to 2 cookies — the unit is identical, so you just compare the counts. When numerators are the same, you compare denominators — but in reverse: 2/3 > 2/5 because thirds are larger pieces than fifths (cutting a whole into 3 gives bigger slices than cutting it into 5), so 2 large pieces is more than 2 small pieces. The key intuition: **smaller denominator = larger piece size = greater total amount** when the number of pieces is equal.

When neither numerators nor denominators match, you have two reliable strategies. The first is **common denominator**: use your equivalent-fractions skill to rewrite both fractions with the same denominator, then compare numerators. To compare 3/4 and 5/6, find a common denominator (12), rewrite as 9/12 and 10/12, and the comparison is immediate. The second is **benchmarking**: check whether each fraction is less than, equal to, or greater than 1/2. If 3/8 < 1/2 and 5/8 > 1/2, you can conclude 5/8 > 3/8 without any conversion at all.

The most persistent mistake is applying whole-number thinking directly: "1/8 is bigger than 1/4 because 8 > 4." This is wrong because the denominator describes piece size, not piece count — it's an inverse relationship. A fraction is a relationship between two numbers, not two independent numbers. Visualizing both fractions as pieces of the same-sized rectangle or as positions on a number line is the best antidote: when you can see that eighths are smaller slices than fourths, the comparison becomes obvious and the whole-number instinct loses its grip.
