---
id: multiplying-fractions
title: Multiplying Fractions
domain: mathematics
course: 5th-grade
prerequisites:
- id: intro-to-fractions
  type: hard
- id: equivalent-fractions
  type: soft
- id: area-of-rectangles
  type: soft
- id: fractions-of-a-set
  type: soft
builds-toward:
- multiplying-mixed-numbers
- dividing-fractions
tags:
- fractions
- multiplication
- arithmetic
stage: concrete-operations
status: validated
---
# Multiplying Fractions

## Core Idea
Multiplying fractions answers the question "what is a fraction of a fraction?" 2/3 x 3/4 means "2/3 of 3/4," and the result is 6/12 = 1/2. The algorithm is straightforward: multiply numerators and multiply denominators. But the conceptual meaning is crucial -- multiplying by a proper fraction makes the result smaller, which is counterintuitive for students used to multiplication making things bigger. The area model (a rectangle with fractional side lengths) makes this visual: 2/3 x 3/4 is the doubly-shaded region in a unit square, covering 6 of the 12 equal parts.

## How It's Best Learned
Use area models extensively: draw a rectangle, shade 3/4 horizontally, then shade 2/3 vertically. The overlap region shows the product. Practice with unit fractions first (1/2 x 1/3), then with non-unit fractions. Discuss why the product is smaller than either factor. Introduce simplifying before multiplying (cross-cancellation) as an efficiency tool after conceptual understanding is solid.

## Common Misconceptions
- Finding common denominators before multiplying (confusing with addition/subtraction procedures).
- Expecting the product to be larger than both factors.
- Not simplifying the result.
- Multiplying numerator by numerator and denominator by denominator but then adding instead of keeping as a single fraction.

## Questions

```yaml
- question: "What is 3/4 × 2/5?"
  type: multiple-choice
  options: ["5/9", "6/20", "15/8", "6/9"]
  answer: 1
  explanation: "Multiply numerators: 3 × 2 = 6. Multiply denominators: 4 × 5 = 20. The result is 6/20, which simplifies to 3/10. Option A (5/9) is the error of adding numerators and denominators instead of multiplying. Option C (15/8) is the error of multiplying diagonally instead of straight across."

- question: "When multiplying 1/2 × 1/3, you need to find a common denominator before multiplying."
  type: true-false
  answer: false
  explanation: "Finding a common denominator is only necessary for adding and subtracting fractions, not multiplying. For multiplication, you simply multiply numerator × numerator and denominator × denominator: (1 × 1)/(2 × 3) = 1/6. Applying the addition procedure to multiplication is one of the most common fraction errors."

- question: "Why is the product of two proper fractions always smaller than either of the original fractions?"
  type: short-answer
  answer: "Multiplying by a fraction less than 1 takes a part of the other fraction, making the result smaller. For example, 1/2 × 3/4 means 'half of three-fourths,' which is only 3/8 — smaller than both 1/2 and 3/4. The denominator grows while the numerator grows proportionally less, so the resulting fraction is smaller."
  explanation: "This is the key conceptual insight of fraction multiplication. Whole-number multiplication scales things up; fraction multiplication scales things down. The area model makes this visible: the product is a smaller sub-region of a unit square, always contained within both original fractions."
```

## Explainer

When you learned to multiply whole numbers, multiplication always made things bigger: 3 × 4 = 12, bigger than both 3 and 4. Fraction multiplication breaks this rule, and understanding *why* is the most important thing about this topic. Multiplying by a proper fraction (a fraction less than 1) shrinks the result. That is not a bug — it is what fraction multiplication means.

The phrase "a fraction of a fraction" captures it perfectly. When you compute 2/3 × 3/4, you are asking: what is 2/3 *of* 3/4? You already know how to find a fraction of a whole number (1/2 of 10 is 5). This is the same idea, extended: 2/3 of 3/4 is a piece of a piece. The answer, 6/12 = 1/2, is smaller than either 2/3 or 3/4 — which makes sense, because you took only part of something that was already less than one.

The area model makes this concrete. Draw a unit square (a square with side length 1). Shade 3/4 of it horizontally with one color. Now shade 2/3 of it vertically with another color. The region covered by *both* shadings is the product. Count the doubly-shaded pieces: 6 out of a total of 12 equal parts — so the product is 6/12. The algorithm — multiply numerators, multiply denominators — is just a shortcut for what the area model counts. The denominator multiplies because you are dividing the square into finer pieces; the numerator multiplies because you are taking a portion of those finer pieces.

The algorithm itself is simpler than the one for adding fractions: no common denominators needed. Multiply straight across. 2/3 × 5/7 = (2 × 5)/(3 × 7) = 10/21. That is it. After you get the product, check whether it simplifies. One efficiency trick is to simplify *before* multiplying — if a numerator and any denominator share a factor, you can cancel it early (called cross-cancellation) to keep the numbers small.

Finally, do a sanity check on your answer. If you multiplied two proper fractions and got a result *larger* than one of the originals, something went wrong. The product of two proper fractions is always between 0 and the smaller of the two factors. Using this as a quick check will catch most errors before you commit to a wrong answer.
