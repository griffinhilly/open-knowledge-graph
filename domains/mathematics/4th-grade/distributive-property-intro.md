---
id: distributive-property-intro
title: Introduction to the Distributive Property
domain: mathematics
course: 4th-grade
prerequisites:
  - id: multiples-of-ten
    type: soft
builds-toward:
  - multi-digit-multiplication
  - writing-numerical-expressions
tags: [arithmetic, multiplication, properties, algebra-readiness]
stage: concrete-operations
status: validated
---

# Introduction to the Distributive Property

## Core Idea
The distributive property says that multiplying a sum by a number gives the same result as multiplying each addend separately and then adding: a x (b + c) = a x b + a x c. For example, 7 x 14 = 7 x 10 + 7 x 4 = 70 + 28 = 98. This is not just an abstract rule -- it is the logical engine behind the multi-digit multiplication algorithm and area models. Students who internalize this property can break apart "hard" multiplication facts into easier ones, building both mental math power and algebraic readiness.

## How It's Best Learned
Use arrays and area models: a 7-by-14 array can be split into a 7-by-10 and a 7-by-4 array. Let students discover that the total stays the same. Practice breaking apart single-digit multiplication facts first (6 x 8 = 6 x 5 + 6 x 3), then extend to multi-digit numbers.

## Common Misconceptions
- Distributing only to the first addend (computing 4 x (10 + 3) as 4 x 10 + 3 = 43).
- Confusing distributive property with other properties (commutative, associative).

## Questions

```yaml
- question: "A student solves 6 × (10 + 4) by writing: 6 × 10 + 4 = 64. What error did she make?"
  type: multiple-choice
  options:
    - "She should have subtracted 4 instead of adding at the end"
    - "She correctly distributed 6 to 10, but forgot to also multiply 6 by 4"
    - "She should have added 10 + 4 first to get 14, then multiplied 6 × 14"
    - "She applied the wrong property; this requires the commutative property"
  answer: 1
  explanation: "The student distributed 6 to the first addend (10) but left the second addend (4) unchanged instead of multiplying it by 6. The correct application is 6 × 10 + 6 × 4 = 60 + 24 = 84. This is the most common distributive property error: the outside multiplier must reach every term inside the parentheses, not just the first one."

- question: "An area model for 8 × 15 splits the rectangle into an 8-by-10 and an 8-by-5 section. Which equation does this model represent?"
  type: multiple-choice
  options:
    - "8 × 15 = 8 × 10 + 5"
    - "8 × 15 = (8 + 10) × (8 + 5)"
    - "8 × 15 = 8 × 10 + 8 × 5"
    - "8 × 15 = 8 + 10 × 8 + 5"
  answer: 2
  explanation: "The area model splits the large rectangle (8 × 15) into two smaller rectangles: one with dimensions 8 × 10 and one with 8 × 5. The total area is the sum of the two parts: 80 + 40 = 120. This matches a × (b + c) = a × b + a × c, where a = 8, b = 10, c = 5. Option A shows the classic error of distributing only to the first term."

- question: "The distributive property allows you to break one multiplication problem into two easier ones, as long as the two parts you use add back up to the original number."
  type: true-false
  answer: true
  explanation: "This is precisely the property's power: you can decompose one factor into any sum (e.g., 14 = 10 + 4, or 14 = 7 + 7, or 14 = 12 + 2), multiply each part by the outside number, and add the results. The only requirement is that the parts sum to the original factor. Each valid decomposition produces the same correct answer."

- question: "In the expression 5 × (20 + 3), you mainly need to multiply 5 by 20, because 3 is just added at the end anyway."
  type: true-false
  answer: false
  explanation: "The 3 must also be multiplied by 5. The correct expansion is 5 × 20 + 5 × 3 = 100 + 15 = 115. Treating 5 × (20 + 3) as 5 × 20 + 3 = 103 is a common error that undercounts by 12. Every term inside the parentheses must receive the outside multiplier — think of it as 5 groups of (20 + 3): every group contains both a 20 and a 3."

- question: "Use an equal-groups story to explain why the distributive property requires multiplying the outside number by every term inside the parentheses, not just the first one."
  type: short-answer
  answer: "Imagine 4 bags, and each bag contains 10 apples and 3 oranges. The total fruit is 4 × (10 + 3). To count all the fruit, you need 4 groups of apples (4 × 10 = 40) AND 4 groups of oranges (4 × 3 = 12). If you only multiplied 4 by the apples and just added 3 for the oranges, you'd have 43 instead of 52 — missing 9 oranges. Every group has all the parts, so every part must be multiplied by the number of groups: 40 + 12 = 52."
  explanation: "The equal-groups story makes the necessity of full distribution concrete. Each of the 4 groups contains both a 10-piece and a 3-piece; the outside multiplier (4) belongs to every element in every group. Partial distribution is like counting only some of the items in each group."
```

## Explainer

You know how to multiply by multiples of ten — 7 × 10 = 70, 7 × 20 = 140. But what about 7 × 14? That is not a multiple of ten, and it might not be a fact you have memorized. The **distributive property** is the strategy that makes unfamiliar multiplication problems solvable by splitting them into easier ones you already know.

The idea: you can break one of the numbers into a sum, multiply each part separately, and add the results. 7 × 14 becomes 7 × (10 + 4). The distributive property says this equals 7 × 10 + 7 × 4 — you multiply 7 by each addend inside the parentheses, then add. Since 7 × 10 = 70 and 7 × 4 = 28, the answer is 70 + 28 = 98. One unfamiliar problem became two easy ones. In symbols: **a × (b + c) = a × b + a × c**.

The **area model** makes this visible. Draw a rectangle that is 7 units tall and 14 units wide. Draw a vertical line at the 10-unit mark, splitting it into two smaller rectangles: one that is 7 by 10 and one that is 7 by 4. The big rectangle's area equals the combined areas of the two smaller ones: 70 + 28 = 98. Splitting the rectangle does not change its total size — that is exactly what the distributive property says. Area models are especially useful because they make the structure impossible to forget: every part of the rectangle must be counted.

The most common mistake is **distributing to only the first addend**. A student might compute 7 × (10 + 4) as 7 × 10 + 4 = 74 — multiplying 7 by 10 but just carrying the 4 along unchanged. The rule is that the outside multiplier must reach every term inside the parentheses. Think of it as 7 groups of (10 + 4): every group of 10 needs a 7, and every group of 4 needs a 7. Leaving any part without its multiplier means undercounting. Once you have internalized this, multi-digit multiplication and later algebraic simplification (like expanding 3(x + 5) = 3x + 15) are natural extensions of the same idea.
