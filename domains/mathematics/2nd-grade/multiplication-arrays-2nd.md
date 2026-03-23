---
id: multiplication-arrays-2nd
title: Multiplication and Arrays
domain: mathematics
course: 2nd-grade
prerequisites:
- id: arrays
  type: hard
- id: multiplication-equal-groups-2nd
  type: soft
builds-toward:
- multiplication-facts-basic-2nd
tags:
- multiplication
- arrays
- rows-columns
stage: concrete-operations
status: validated
---

# Multiplication and Arrays

## Core Idea
An array shows objects in rows and columns. 3 rows of 5 (or 5 columns of 3) represents 3×5=15. Arrays help visualize multiplication and show why 3×5 equals 5×3 (commutative property).

## Questions

```yaml
- question: "A student draws an array with 4 rows and 6 dots in each row. What multiplication fact does this array represent, and what is the total?"
  type: multiple-choice
  options:
    - "4 + 6 = 10, because there are 4 rows and 6 columns"
    - "4 × 6 = 24, because 4 rows of 6 means 4 groups of 6"
    - "6 × 4 = 10, because you add the number of rows to the number of columns"
    - "4 + 6 + 4 + 6 = 20, by adding rows and columns twice"
  answer: 1
  explanation: "An array of 4 rows with 6 in each row means you have 4 groups, each containing 6 — that is the definition of 4 × 6. Multiplying rows by items-per-row gives the total number of dots: 4 × 6 = 24. Addition (4 + 6) would only give 10, which doesn't match the total — addition combines the two numbers rather than finding the total objects in a repeated-group structure."

- question: "A student has an array showing 5 rows of 3. She rotates it 90 degrees. What does the new arrangement show, and what does this demonstrate?"
  type: multiple-choice
  options:
    - "It still shows 5 × 3 = 15; rotating doesn't change what the array represents"
    - "It now shows 3 × 5 = 15; demonstrating that changing the order of factors doesn't change the product"
    - "It shows 3 × 5 = 15, but this only works for these specific numbers, not in general"
    - "It shows a different total because rotating changes which numbers are rows versus columns"
  answer: 1
  explanation: "Rotating the array doesn't add or remove any dots — the total stays exactly 15. But the arrangement now shows 3 rows with 5 in each row, which represents 3 × 5. Since nothing was added or removed, 5 × 3 and 3 × 5 must both equal 15. This is a visual proof of the commutative property of multiplication: the order of the factors never changes the product. And it generalizes to all numbers — any a × b array rotated becomes b × a, with the same total."

- question: "A 2 × 8 array and an 8 × 2 array contain different numbers of objects."
  type: true-false
  answer: false
  explanation: "Both arrays contain 16 objects. A 2 × 8 array has 2 rows of 8 (8 + 8 = 16); an 8 × 2 array has 8 rows of 2 (2+2+2+2+2+2+2+2 = 16). The commutative property guarantees that swapping the order of factors never changes the product: 2 × 8 = 8 × 2 = 16. Arrays make this visible — rotating one gives you the other, and the dot count is unchanged. This is why knowing 2 × 8 also means you know 8 × 2."

- question: "In a multiplication array, the first number in the multiplication fact tells you how many rows, and the second number tells you how many items are in each row."
  type: true-false
  answer: true
  explanation: "By convention, a × b means 'a groups of b' — so in an array, the first factor (a) gives the number of rows, and the second factor (b) gives how many items fill each row. An array of 3 × 5 has 3 rows with 5 in each row. This convention connects arrays directly to the meaning of multiplication as repeated equal groups. The product — the total dots — equals rows times items-per-row."

- question: "How does looking at an array help you understand why 3 × 5 equals 5 × 3? Describe what you would do with the array to show this."
  type: short-answer
  answer: "Start with a 3 × 5 array: 3 rows with 5 dots in each row, totaling 15 dots. Now rotate the array 90 degrees — turn it on its side. The same 15 dots are now arranged as 5 rows with 3 in each row. You haven't added or removed any dots, so the total must still be 15. But now the array represents 5 × 3 = 15 instead of 3 × 5 = 15. The rotation proves visually that both facts equal the same total — the commutative property isn't just a rule to memorize, it's something you can see."
  explanation: "The array is a concrete proof, not just an illustration. It shows that two different multiplication expressions describe the same physical collection of objects viewed from different orientations. This understanding cuts the number of facts to memorize roughly in half — every fact you know automatically gives you its commutative partner."
```

## Explainer

You already know what an array looks like — it's objects arranged neatly in **rows** (going across) and **columns** (going up and down), the way eggs sit in a carton or seats are arranged in a movie theater. Now you're connecting that picture to multiplication. An array doesn't just show a collection of objects; it tells you a multiplication fact just by how it's organized.

When you see 3 rows of 5 dots, you could count all 15 one by one, or you could skip-count by 5s: 5, 10, 15. But the multiplication sentence 3 × 5 = 15 is the most efficient way to say it: 3 groups of 5. The first number in a multiplication fact tells you how many rows; the second number tells you how many in each row. Rows times items-per-row equals the total.

Arrays reveal something powerful that's hard to see with just numbers: why 3 × 5 = 5 × 3. Take your array of 3 rows with 5 in each row — it has 15 dots total. Now rotate it 90 degrees (turn it on its side). You now see 5 rows with 3 in each row. The dots haven't moved — there are still exactly 15 — but now the array represents 5 × 3. This visual proof shows the **commutative property** of multiplication: the order of the factors doesn't change the product. Knowing this cuts the number of facts you need to memorize roughly in half.

Once you can see a multiplication fact as an array, you can build any fact you need, even if you haven't memorized it yet. Don't know 4 × 6? Draw 4 rows of 6, or imagine it: four rows of six eggs. Count by 6s — 6, 12, 18, 24. The array gives your brain a concrete image to hold onto while you build fluency with the abstract number sentence.
