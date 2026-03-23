---
id: multiplication-strategies-arrays-3rd
title: Multiplication Strategies Using Arrays
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multiplication-introduction-arrays
  type: hard
builds-toward:
- area-of-rectangles
tags:
- multiplication
- arrays
- visual-models
- strategies
stage: concrete-operations
status: validated
---

# Multiplication Strategies Using Arrays

## Core Idea
An array is a rectangular arrangement of objects in rows and columns. A 4-by-6 array has 4 rows and 6 objects in each row, representing 4 × 6 = 24. Arrays make multiplication concrete and visible, supporting mental strategies and understanding of commutativity.

## Questions

```yaml
- question: "A student doesn't know 7 × 6. She draws a 7-by-6 array, splits it into a 7-by-5 and a 7-by-1, and computes 35 + 7 = 42. How does this strategy work?"
  type: multiple-choice
  options:
    - "She guessed that the two parts would be close enough to the correct answer"
    - "She doubled the easier fact 7 × 3 = 21 to get 42"
    - "She used the break-apart strategy: the two smaller arrays contain all the same tiles as the original, so their products sum to the correct answer"
    - "She applied commutativity to rewrite 7 × 6 as 6 × 7 and then used a known fact"
  answer: 2
  explanation: "Splitting the array does not change the total number of tiles — the 42 tiles in the original 7×6 array are now in two groups: 35 and 7. Adding the partial products recovers the full total. The break-apart strategy works because the split is a partition of the same tiles, not a change to the problem. This is the concrete foundation of the distributive property."

- question: "What does rotating a 3-by-8 array 90 degrees to produce an 8-by-3 array demonstrate?"
  type: multiple-choice
  options:
    - "3 × 8 produces a different answer than 8 × 3, because the rows and columns switched"
    - "3 × 8 = 8 × 3, because rotation preserves the total number of tiles"
    - "Arrays can only be used for facts up to 5 × 5 before rotation causes errors"
    - "Rotating an array doubles its area"
  answer: 1
  explanation: "Rotating the array changes its orientation but not its tile count. The exact same tiles that were arranged in 3 rows of 8 are now in 8 rows of 3 — still 24 tiles. This is a visual proof of the commutative property of multiplication: the order of the factors doesn't change the product."

- question: "You can find 6 × 9 by splitting a 6-by-9 array into a 6-by-5 and a 6-by-4 array, then adding the two partial products."
  type: true-false
  answer: true
  explanation: "6 × 5 = 30 and 6 × 4 = 24; 30 + 24 = 54 = 6 × 9. The split is valid because 5 + 4 = 9 — the two parts account for all nine columns of the original array. Any split that adds back to the original factor produces the correct answer."

- question: "When you split an array into two smaller arrays to find a product, the total number of tiles changes — that is why you need to add the two partial products at the end."
  type: true-false
  answer: false
  explanation: "The total number of tiles does not change. Splitting the array partitions the existing tiles into two groups — no tiles are added or removed. You add the partial products because the same total has been divided into two parts, and adding the parts recovers the whole. The split is a reorganization, not a change in quantity."

- question: "Explain how splitting an array into two smaller arrays helps you find a multiplication fact you haven't memorized. Why does this strategy always give the correct answer?"
  type: short-answer
  answer: "When you don't know 4 × 7, you can split a 4-by-7 array at any column, say after column 5, creating a 4-by-5 (= 20) and a 4-by-2 (= 8). Adding 20 + 8 = 28 gives the correct answer. The strategy always works because the split partitions the original tiles into two groups without adding or removing any. The two partial products together account for every tile in the original array, so their sum equals the original product."
  explanation: "This strategy is the concrete, visual form of the distributive property: 4 × 7 = 4 × (5 + 2) = 4 × 5 + 4 × 2. Students who understand why this works — not just how to do it — are ready to apply the same reasoning to multi-digit multiplication and eventually to algebraic expressions."
```

## Explainer

You've worked with arrays before as a way to see what multiplication looks like. Now you're using them as a thinking tool — a way to break hard facts into easier ones. The key insight is that you can split any array into two smaller arrays whose answers you already know, add those answers, and get the fact you wanted. This is called the **break-apart strategy** (or decomposition), and arrays make it visible.

Suppose you want to figure out 4 × 7, and you're not sure of that fact yet. Draw a 4-by-7 array. Now draw a vertical line after the 5th column, splitting it into a 4×5 array and a 4×2 array. You know 4 × 5 = 20 (skip-count by 5s four times) and 4 × 2 = 8. Put them together: 20 + 8 = 28. So 4 × 7 = 28 — and you figured it out from facts you already knew. The array is the visual proof that this split is legal: the 28 tiles in the full array really do equal the 20 tiles plus the 8 tiles.

This strategy also explains why multiplication distributes over addition — the foundation of a rule you'll use throughout algebra. For now, think of arrays as your reasoning tool. Rotating an array 90° proves commutativity (4×6 and 6×4 have the same tiles). Splitting an array proves that you can break facts apart. Eventually, when you study area of rectangles, you'll see that an array of tiles and a rectangle in geometry are describing the same mathematical relationship — length times width. Arrays built that bridge from multiplication facts to geometry, and you're standing on it right now.
