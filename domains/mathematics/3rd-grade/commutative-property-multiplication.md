---
id: commutative-property-multiplication
title: Commutative Property of Multiplication
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multiplication-facts-within-100
  type: hard
- id: arrays
  type: soft
builds-toward:
- associative-property-multiplication
tags:
- commutative
- properties
- multiplication
stage: concrete-operations
status: validated
---
# Commutative Property of Multiplication

## Core Idea
The commutative property of multiplication states that the order of factors does not change the product: 3×4 = 4×3 = 12. This is visually clear with arrays — a 3-row, 4-column array has the same number of tiles as a 4-row, 3-column array. Knowing this property cuts the number of facts to memorize roughly in half.

## How It's Best Learned
Have students build two arrays (e.g., 3×5 and 5×3) with tiles and count both. The visual rotation of the array makes commutativity concrete. Then connect it to the multiplication table — show that the table is symmetric across the diagonal.

## Common Misconceptions
- Students sometimes think 3×4 and 4×3 are different problems that happen to have the same answer, rather than the same fact.
- The property does NOT apply to subtraction or division, so students need explicit instruction not to overgeneralize.

## Questions

```yaml
- question: "A student says: '3 × 7 and 7 × 3 are different problems that happen to give the same answer, so I still need to memorize both separately.' Is this correct?"
  type: multiple-choice
  options:
    - "Correct — they are different problems with different processes, even if the answers match"
    - "Incorrect — they are the same fact; knowing one automatically gives you the other"
    - "Correct — the answers only match for small numbers, not larger ones"
    - "Incorrect — but only because multiplication facts are memorized as a set, not because of any property"
  answer: 1
  explanation: "The commutative property makes 3 × 7 and 7 × 3 the same fact, not two different facts that coincidentally match. A 3-row, 7-column array and a 7-row, 3-column array contain identical tiles — rotating the rectangle doesn't change its area. They express the same relationship from different directions. This means knowing one automatically gives the other, cutting the memorization burden roughly in half."

- question: "Which of the following equations is DEFINITELY true based on the commutative property?"
  type: multiple-choice
  options:
    - "15 ÷ 5 = 5 ÷ 15"
    - "10 − 3 = 3 − 10"
    - "6 × 9 = 9 × 6"
    - "12 ÷ 4 = 4 ÷ 12"
  answer: 2
  explanation: "The commutative property holds for multiplication (and addition), but NOT for subtraction or division. 6 × 9 = 9 × 6 = 54 is always guaranteed. But 15 ÷ 5 = 3 while 5 ÷ 15 = 1/3; and 10 − 3 = 7 while 3 − 10 = −7. Order matters for those operations. This is why commutativity is named as a special property of multiplication — it is not a universal rule that applies to all arithmetic."

- question: "Knowing that 8 × 6 = 48 automatically tells you that 6 × 8 = 48, without any additional calculation."
  type: true-false
  answer: true
  explanation: "The commutative property guarantees this. Once you know any multiplication fact a × b = c, you immediately know b × a = c. The two expressions are not separately derived facts that happen to match — they are the same mathematical relationship viewed from a different order. Geometrically: an 8-row, 6-column array and a 6-row, 8-column array contain exactly the same 48 tiles."

- question: "Because multiplication is commutative, division is also commutative — so 24 ÷ 6 must equal 6 ÷ 24."
  type: true-false
  answer: false
  explanation: "Commutativity is a special property of multiplication (and addition), not a universal arithmetic rule. 24 ÷ 6 = 4, but 6 ÷ 24 = 1/4 — very different values. In division, the divisor and dividend play distinct roles, so switching them fundamentally changes what you are computing. Students must learn explicitly that commutativity does not extend to subtraction or division, despite the temptation to apply it everywhere."

- question: "Why does the commutative property work for multiplication? Use the idea of an array to explain."
  type: short-answer
  answer: "A multiplication array with 4 rows and 6 columns has 24 tiles. Rotating it 90° gives 6 rows and 4 columns — still 24 tiles. The number of objects hasn't changed, only the orientation. This shows geometrically that 4 × 6 = 6 × 4. Order doesn't matter because you are counting the same collection of objects either way."
  explanation: "The array argument makes commutativity geometrically obvious and shows it is a consequence of what multiplication means, not an invented rule. A rectangle's area doesn't depend on which side you call 'length' and which you call 'width.' This physical grounding distinguishes the commutative property as a provable truth — and helps students see why it applies to multiplication and addition but not to subtraction and division."
```

## Explainer

You know your multiplication facts and you've worked with arrays — rectangular grids of rows and columns. Now think about what happens when you rotate an array. A 3-row, 4-column array has 12 tiles. Turn it on its side: now it's a 4-row, 3-column array. The tiles haven't changed — it's the same 12 objects, just rearranged. This is exactly why 3 × 4 = 4 × 3. The **commutative property of multiplication** says the order of the factors never changes the product.

This isn't just a coincidence or a rule someone decided. It's a geometric truth baked into the meaning of multiplication. A rectangle 3 units tall and 4 units wide has the same area as a rectangle 4 units tall and 3 units wide — you haven't added or removed any space. That's why the products must be equal. When you look at a multiplication table, you can see this symmetry directly: the table is a mirror image of itself across the main diagonal.

The practical power is enormous. If you know 7 × 8 = 56, you automatically know 8 × 7 = 56 — one fact for the price of one. This roughly cuts the number of distinct facts you need to memorize in half. But be careful about overgeneralizing: the commutative property works for addition too (3 + 4 = 4 + 3), but it does NOT work for subtraction (5 − 3 ≠ 3 − 5) or division (12 ÷ 3 ≠ 3 ÷ 12). The order matters in those operations, which is why multiplication's order-independence is worth recognizing as a special property.
