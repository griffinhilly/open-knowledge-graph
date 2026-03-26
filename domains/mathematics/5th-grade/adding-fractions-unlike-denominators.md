---
id: adding-fractions-unlike-denominators
title: Adding Fractions with Unlike Denominators
domain: mathematics
course: 5th-grade
prerequisites:
- id: equivalent-fractions
  type: hard
- id: adding-fractions-like-denominators-5th
  type: hard
- id: factors-and-multiples
  type: hard
- id: comparing-fractions
  type: soft
builds-toward:
- subtracting-fractions-unlike-denominators
- mixed-number-arithmetic
tags:
- fractions
- addition
- common-denominators
stage: concrete-operations
status: validated
---
# Adding Fractions with Unlike Denominators

## Core Idea
To add fractions with different denominators, you must first rewrite them as equivalent fractions with a common denominator. 1/3 + 1/4: the least common denominator of 3 and 4 is 12, so 1/3 = 4/12 and 1/4 = 3/12, giving 4/12 + 3/12 = 7/12. The key insight is that you cannot add fractions measured in different-sized units -- thirds and fourths are different units, just as you cannot add 3 feet and 4 inches without converting. Finding the least common multiple of the denominators gives the most efficient common denominator, though any common multiple works.

## How It's Best Learned
Use visual models first: overlay fraction strips of thirds and fourths to see that twelfths is the common subdivision. Practice finding least common multiples before applying to fraction addition. Work through many examples with different denominator pairs. Simplify results. Extend to mixed numbers once fluent with proper fractions.

## Common Misconceptions
- Adding numerators and denominators separately (1/3 + 1/4 = 2/7).
- Using a common denominator but forgetting to adjust the numerators.
- Always multiplying the two denominators instead of finding the least common multiple (works but produces larger numbers than necessary).

## Questions

```yaml
- question: "What is 1/2 + 1/3?"
  type: multiple-choice
  options: ["2/5", "2/6", "5/6", "1/6"]
  answer: 2
  explanation: "The least common denominator of 2 and 3 is 6. Rewrite: 1/2 = 3/6 and 1/3 = 2/6. Add: 3/6 + 2/6 = 5/6. The answer 2/5 is the classic 'add across' error — adding numerators (1+1=2) and denominators (2+3=5) separately, which is always wrong."

- question: "When finding a common denominator for 1/4 + 1/6, you is expected to use 24 as the denominator."
  type: true-false
  answer: false
  explanation: "Any common multiple of 4 and 6 works. The least common multiple is 12, not 24. Using 12 gives 3/12 + 2/12 = 5/12 directly. Using 24 also works (6/24 + 4/24 = 10/24 = 5/12), but requires simplifying afterward. The LCD is preferred for efficiency, not required for correctness."

- question: "A student adds 2/3 + 1/4 and writes 3/7. What mistake did they make, and what is the correct answer?"
  type: short-answer
  answer: "They added numerators and denominators separately (2+1=3, 3+4=7). The correct answer is 11/12: convert to twelfths (2/3 = 8/12, 1/4 = 3/12), then add numerators: 8/12 + 3/12 = 11/12."
  explanation: "Fractions can only be added when they represent same-sized pieces. The denominator names the size of the piece — thirds and fourths are different sizes. You must first rewrite both fractions with a common denominator before adding. The 3/7 error is the most common fraction mistake and always produces a wrong answer."
```

## Explainer

You already know how to add fractions with the same denominator: 3/8 + 2/8 = 5/8. The denominator names what kind of piece you have — eighths — and you simply count them. The challenge with unlike denominators is that you're combining pieces of different sizes. Trying to add thirds and fourths directly is like trying to add 3 feet and 4 inches: the units don't match, so you can't just count.

The fix is to rewrite both fractions so they use the same-sized pieces. For 1/3 + 1/4, you need a number that is both a multiple of 3 and a multiple of 4. List multiples of each: multiples of 3 are 3, 6, 9, **12**, 15...; multiples of 4 are 4, 8, **12**, 16... The least common multiple is 12, so use 12 as your common denominator.

Now apply equivalent fractions. To convert 1/3 to twelfths, ask: 3 × ? = 12? The answer is 4, so multiply numerator and denominator by 4: 1/3 = 4/12. For 1/4: 4 × ? = 12? Multiply by 3: 1/4 = 3/12. Now add: 4/12 + 3/12 = 7/12. The pieces are the same size, so the numerators can be added directly.

A shortcut that always works: multiply the two denominators to get a common denominator. For 1/3 + 1/4, use 3 × 4 = 12, which happens to be the LCD here. But for 1/4 + 1/6, the product is 24, while the LCD is only 12 — using 12 keeps numbers smaller and often avoids simplifying at the end. Either approach gives the correct answer; the LCD is more efficient.

The most important thing to avoid: **never add the denominators**. The answer to 1/3 + 1/4 is not 2/7. Imagine eating one slice from a 3-slice pizza and one slice from a 4-slice pizza. You now have 2 slices, but you don't have 2 slices of a 7-slice pizza — the pieces are different sizes. The denominator describes the size of each piece; it is not a number to be added.
