---
id: multiplication-facts-0-through-10s
title: Basic Multiplication Facts Through 10
domain: mathematics
course: 2nd-grade
prerequisites:
- id: multiplication-introduction-equal-groups
  type: hard
- id: multiplication-introduction-arrays
  type: hard
builds-toward:
- multiplication-facts-within-100
tags:
- multiplication
- facts
- fluency
stage: concrete-operations
status: validated
---

# Basic Multiplication Facts Through 10

## Core Idea
Multiplication facts are products of two single-digit numbers. Memorizing facts through 10 (like 3 × 4 = 12, 5 × 6 = 30) allows faster problem-solving. These facts are built from understanding equal groups and arrays, not memorization alone.

## How It's Best Learned
Use skip counting, arrays, and repeated addition to derive facts. Practice with fact families (e.g., 2 × 5 = 10, 5 × 2 = 10) to see relationships. Use games and repeated practice to build automaticity.

## Common Misconceptions
- Memorizing facts without understanding the underlying model.
- Confusing the order of factors (thinking 3 × 4 is different from 4 × 3).
- Struggling with facts involving 0 or 1.

## Questions

```yaml
- question: "A student multiplies 0 × 9 and answers '9.' What error did she make, and what is the correct answer?"
  type: multiple-choice
  options:
    - "She confused multiplication with addition; 0 × 9 = 9 is actually correct"
    - "She confused 0 × 9 with 1 × 9 = 9; the correct answer is 0, because zero groups of nine contains nothing"
    - "She forgot to add the exponent; the answer is 90"
    - "She is correct for even numbers but not for 9, which is odd"
  answer: 1
  explanation: "0 × 9 means 'zero groups of nine' — no groups at all, so the total is 0. The common error is confusing 0 × 9 with 1 × 9 = 9. The equal-groups meaning resolves the confusion: one group of nine has something in it; zero groups have nothing."

- question: "You have memorized that 7 × 6 = 42. Which other multiplication fact do you automatically know because of this?"
  type: multiple-choice
  options:
    - "7 × 7 = 49, because multiplication grows by 7 each step"
    - "6 × 7 = 42, because multiplication is commutative — swapping factors gives the same product"
    - "7 + 6 = 13, because multiplication facts relate to addition"
    - "14 × 3 = 42, because you can always double one factor and halve the other"
  answer: 1
  explanation: "The commutative property means 7 × 6 = 6 × 7. Swapping the factors gives the same product — an array of 7 rows of 6 contains the same number of squares as 6 rows of 7. This single property cuts the work of learning the times table roughly in half: every fact you learn gives you a second fact for free."

- question: "The product of 3 × 4 is different from the product of 4 × 3."
  type: true-false
  answer: false
  explanation: "3 × 4 = 4 × 3 = 12. Multiplication is commutative — the order of the factors does not change the product. An array shows why: a 3-by-4 grid and a 4-by-3 grid contain the same number of squares, just oriented differently. This property halves the number of distinct facts that need to be learned."

- question: "Understanding why any number times zero equals zero is possible from the equal-groups meaning of multiplication."
  type: true-false
  answer: true
  explanation: "Multiplication means 'this many groups of this size.' Zero groups of any size means you have no groups at all — so the total is zero. Students who understand this don't need to memorize zero facts as a special rule; they can derive them from the meaning of multiplication. This is why understanding-based learning is more durable than rote memorization."

- question: "How can you use a 'near fact' strategy to figure out 7 × 8 if you don't remember it?"
  type: short-answer
  answer: "Use a fact you know — like 7 × 7 = 49 — and add one more group of 7: 49 + 7 = 56. Or use 8 × 8 = 64 and subtract one group of 8: 64 − 8 = 56. You build from a known fact to an unknown one by adding or subtracting exactly one group."
  explanation: "Near-fact strategies are more reliable than trying to recall an arbitrary memorized fact under pressure. They also reinforce the meaning of multiplication — each step up in one factor adds one more group. Students who use these strategies eventually internalize the fact through repeated derivation, which is more durable than rote memorization."
```

## Explainer

From your work with equal groups and arrays, you know what multiplication means: 4 × 6 is four groups of six, or a four-by-six rectangular arrangement. **Multiplication facts** are simply the memorized answers to all combinations of single-digit numbers — the 100 products that appear on a times table grid. Knowing them automatically frees up your thinking for harder problems, the same way knowing that 7 + 8 = 15 instantly lets you handle much bigger arithmetic.

Some facts follow patterns that make them easy to derive. The **zero facts** are all 0: any number times zero means "zero groups of that size," which gives nothing. The **ones facts** are the number itself: four groups of one is just four. The **twos facts** are doubles you already know from addition. The **fives facts** produce numbers ending in 0 or 5 — the same skip-counting you might do on a clock. The **tens facts** just append a zero. These patterns knock out nearly half the table right away.

The commutative property cuts the remaining work in half: 3 × 7 = 7 × 3. If you know one, you know the other. An array shows why: a three-by-seven grid has exactly as many squares as a seven-by-three grid, just rotated. So when you're learning the 6-times table, you can lean on whatever facts you already know from the other direction.

For facts without obvious patterns — like 6 × 7 or 7 × 8 — use a **near fact**: 6 × 7 = 6 × 6 + 6 = 36 + 6 = 42. Breaking an unknown fact into a known fact plus one more group is more reliable than pure memorization. Over time, facts that start as conscious strategies become automatic. Speed comes from repeated meaningful practice, not from drilling with no understanding of what you're computing.
