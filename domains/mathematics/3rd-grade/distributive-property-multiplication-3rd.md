---
id: distributive-property-multiplication-3rd
title: Distributive Property of Multiplication
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multiplication-arrays-3rd
  type: hard
builds-toward:
- mental-math-multiplication-3rd
- factoring-gcf
tags:
- properties
- multiplication
- distributive
stage: concrete-operations
status: validated
---

# Distributive Property of Multiplication

## Core Idea
Multiply a sum by breaking it apart: 3 × (4 + 2) = (3 × 4) + (3 × 2) = 12 + 6 = 18. Arrays split into sections show this clearly.

## How It's Best Learned
Draw arrays split into two parts. Compute each part separately, then add.

## Common Misconceptions
Not recognizing when to use the property; forgetting to add the products.

## Questions

```yaml
- question: "A student uses the distributive property to solve 6 × 7 by writing: 6 × (3 + 4) = (6 × 3) + (6 × 4) = 18 + 24 = 42. Why does splitting 7 into 3 + 4 not change the answer?"
  type: multiple-choice
  options:
    - "It works only because 3 and 4 happen to be easy numbers to multiply by 6"
    - "The 6 rows apply to every column in both parts — splitting the columns doesn't change the total number of dots in the array"
    - "Multiplication distributes only when the two parts add up to an even number"
    - "It works as a coincidence for small numbers but would fail for larger ones"
  answer: 1
  explanation: "The distributive property works because of what multiplication means in an array: 6 × 7 is 6 rows of 7 columns. Drawing a line after column 3 gives two rectangles — a 6×3 and a 6×4 — but all 6 rows still span both sections. The total dots don't change when you draw the dividing line, so (6×3) + (6×4) = 6×7 exactly. This works for any numbers and any split."

- question: "A student is unsure of 8 × 9 but knows 8 × 5 = 40 and 8 × 4 = 32. Which expression correctly applies the distributive property?"
  type: multiple-choice
  options:
    - "8 × 9 = (8 + 5) × (8 + 4)"
    - "8 × 9 = 8 × (5 + 4) = (8 × 5) + (8 × 4) = 40 + 32 = 72"
    - "8 × 9 = (8 × 5) × (8 × 4)"
    - "8 × 9 = 8 + (5 × 4)"
  answer: 1
  explanation: "The distributive property splits one factor into a sum: 9 = 5 + 4, so 8 × 9 = 8 × (5 + 4). Then 8 multiplies each part separately: (8 × 5) + (8 × 4) = 40 + 32 = 72. Option A incorrectly adds to both factors. Option C incorrectly multiplies the partial products together. Option D has no valid structure. The key move is always: outer factor × (part₁ + part₂) = (outer × part₁) + (outer × part₂)."

- question: "You can split a factor any way you like when using the distributive property, and you will always get the same final answer."
  type: true-false
  answer: true
  explanation: "This is one of the most powerful features of the property. To find 7 × 8, you can split 8 as (5+3), (4+4), (2+6), or (7+1) — all give 56. The choice of split affects which partial facts you use, but the answer is always the same. A flexible student chooses the split that uses facts they know best."

- question: "The distributive property is a special trick that only applies to multiplication in 3rd grade and doesn't connect to anything in later math."
  type: true-false
  answer: false
  explanation: "The distributive property is one of the most foundational ideas in all of mathematics. It reappears when multiplying two-digit numbers (24 × 3 = (20+4) × 3 = 60+12 = 72), in algebra when expanding expressions like (x+5)(x+2), and throughout higher mathematics. The rectangle-splitting model learned in 3rd grade is exactly the same geometric intuition that underlies multiplication at every level."

- question: "Describe a 4 × 7 array split into two rectangles to show why 4 × 7 = (4 × 3) + (4 × 4). What does the split make visible about why the property works?"
  type: short-answer
  answer: "Imagine a rectangle with 4 rows and 7 columns (28 dots). Draw a vertical line after the 3rd column, creating a 4×3 rectangle (12 dots) and a 4×4 rectangle (16 dots). Together: 12 + 16 = 28 = 4 × 7. The split makes visible that all 4 rows still span both sections — the '4' is not split, only the '7' is. The multiplier applies equally to every part."
  explanation: "The array model shows why the property is not a trick: the number of rows (the outer factor) remains constant across both halves. Splitting the columns never changes how many rows there are, so the total count stays the same. This is the geometric proof of the distributive property, and it works for any rectangular array."
```

## Explainer

You know from multiplication arrays that a product like 3 × 6 can be visualized as a rectangular arrangement — 3 rows and 6 columns, with 18 total dots. The **distributive property** is what happens when you split that rectangle into two smaller rectangles that together cover the same area. It gives you a way to break harder multiplications into easier ones by using facts you already know.

Here's the core idea: 3 × 6 = 3 × (4 + 2) = (3 × 4) + (3 × 2) = 12 + 6 = 18. Why does this work? Draw a 3-by-6 array, then draw a vertical line separating the first 4 columns from the last 2. You now have two separate rectangles: a 3×4 (which is 12) and a 3×2 (which is 6). Together they still cover 3×6 = 18 total dots. The "distribution" means that the 3 rows apply equally to both parts — each column in both sections still has 3 dots.

This strategy becomes most useful for products you don't yet have memorized. Suppose you're unsure of 7 × 8. Split 8 into 5 + 3: (7 × 5) + (7 × 3) = 35 + 21 = 56. Or split it as 4 + 4: (7 × 4) + (7 × 4) = 28 + 28 = 56. You choose the split that uses facts you know best. The property works no matter how you split the number, which is what makes it flexible.

The distributive property may look like a trick at this stage, but it is one of the most important ideas in all of mathematics. When you later multiply two-digit numbers (24 × 3 = (20 + 4) × 3 = 60 + 12 = 72), you'll use this exact idea. When you study algebra and expand expressions like (x + 5)(x + 2), that's the distributive property again. The rectangle model you learn now — splitting an array into two parts — is the same geometric intuition that underlies multiplication at every level.
