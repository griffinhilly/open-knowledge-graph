---
id: multi-digit-multiplication
title: Multi-Digit Multiplication
domain: mathematics
course: 4th-grade
prerequisites:
- id: place-value-whole-numbers
  type: hard
- id: multiples-of-ten
  type: hard
- id: distributive-property-intro
  type: soft
- id: arrays
  type: soft
- id: equal-groups
  type: soft
- id: repeated-addition-to-multiplication
  type: soft
- id: associative-property-multiplication
  type: soft
- id: estimation-in-multiplication
  type: soft
- id: multiplication-facts-within-100
  type: soft
- id: two-digit-by-one-digit-multiplication
  type: soft
- id: area-of-rectangles
  type: soft
- id: arrays-2nd-grade
  type: soft
builds-toward:
- intro-to-long-division
- multiplying-decimals
- area-of-rectangles
tags:
- arithmetic
- multiplication
- place-value
- algorithms
stage: concrete-operations
status: validated
---
# Multi-Digit Multiplication

## Core Idea
Multiplying multi-digit numbers (e.g., 36 x 24) means finding the total when you have 24 groups of 36 (or equivalently, the area of a 36-by-24 rectangle). The standard algorithm breaks this into partial products using place value: 36 x 4 and 36 x 20, then adds the results. Each partial product is itself a multi-digit-by-single-digit multiplication with possible regrouping. Understanding that the algorithm is an organized application of the distributive property -- (30 + 6) x (20 + 4) -- gives students insight into why it works rather than just how.

## How It's Best Learned
Begin with area models (drawing a rectangle partitioned into place-value sections) to make partial products visible. Transition to the partial products written method, then to the compact standard algorithm. The area model and partial products should be used long enough that students see the standard algorithm as a shortcut for what they already understand, not a mysterious procedure.

## Common Misconceptions
- Forgetting to account for the place value of the tens digit (writing 36 x 2 instead of 36 x 20 in the second partial product).
- Regrouping errors within partial products.
- Omitting one of the four partial products in a 2-by-2 multiplication.

## Questions

```yaml
- question: "A student computes 36 × 24 and writes two partial products: 144 (from 36 × 4) and 72 (from 36 × 2). Their final answer is 216. What error did they make?"
  type: multiple-choice
  options:
    - "They computed 36 × 4 incorrectly"
    - "They forgot to account for the place value of the tens digit — 36 × 2 should be 36 × 20 = 720, not 72"
    - "They added the partial products incorrectly"
    - "They should have computed 36 × 24 as 24 × 36 instead"
  answer: 1
  explanation: "The 2 in 24 represents 20, not 2, so the partial product is 36 × 20 = 720. Writing 36 × 2 = 72 ignores the place value of the tens digit. The correct partial products are 144 + 720 = 864. This is the most common error in multi-digit multiplication: treating every digit as a ones digit regardless of its position."

- question: "The standard algorithm for multi-digit multiplication is built on the distributive property."
  type: true-false
  answer: true
  explanation: "36 × 24 is the same as (30 + 6) × (20 + 4), which distributes to four partial products: 30×20, 30×4, 6×20, and 6×4. The standard algorithm organizes these partial products efficiently. Understanding this connection is what makes the algorithm meaningful rather than arbitrary — every step corresponds to a real multiplication that the distributive property says must be included."

- question: "Why does the area model help students understand multi-digit multiplication better than jumping straight to the standard algorithm?"
  type: short-answer
  answer: "The area model makes each partial product visible as a physical region of a rectangle, so students can see why all four products must be included and why place value matters. The standard algorithm compresses these steps, which makes it faster but hides the reasoning — students who only learn the algorithm often can't explain why it works or catch their own errors."
  explanation: "The area model directly represents multiplication as the area of a rectangle partitioned by place value. Each sub-rectangle corresponds to one partial product. Students who build the algorithm from this visual foundation understand that the '720' in 36 × 24 is not magic — it is the area of the 36-by-20 region. This understanding is what lets them detect and correct errors like the place-value mistake in the multiple-choice question."
```

## Explainer

You have already learned that multiplication means equal groups or, equivalently, the area of a rectangle. You also know your single-digit multiplication facts and how multiples of ten work. Multi-digit multiplication combines these ideas: multiplying 36 × 24 is exactly the same kind of thing as multiplying 6 × 4, just with larger numbers. The question is how to organize the work so you do not lose track of anything.

The area model makes the structure visible. Draw a rectangle that is 36 wide and 24 tall. Now split the width into 30 and 6, and the height into 20 and 4. You have divided the big rectangle into four smaller ones. Their areas are: 30 × 20 = 600, 30 × 4 = 120, 6 × 20 = 120, and 6 × 4 = 24. Add all four: 600 + 120 + 120 + 24 = 864. This is the *partial products* method — you have computed the same thing the standard algorithm computes, just with every step written out explicitly.

The connection to the distributive property is worth pausing on: 36 × 24 = (30 + 6) × (20 + 4). The distributive property says you must multiply every piece of one factor by every piece of the other — four multiplications, not two. This is the precise reason you must treat the 2 in 24 as 20, not as 2. When you write the second partial product in the standard algorithm on its own indented line, the indentation is a shorthand for that multiplication by 10. Forgetting the indentation — or thinking 36 × 2 instead of 36 × 20 — is the most common error, and it comes from ignoring place value.

The standard algorithm compresses the area model into a more compact procedure. Instead of labeling four sub-rectangles, you write two rows of partial products and add. The first row is the bottom strip (× ones digit), the second row is the left strip (× tens digit), shifted one place left to honor place value. Once this compression makes sense to you — because you have seen the area model enough times — the algorithm is fast and reliable. If you can ever not remember why you are shifting left, draw the rectangle.

Estimation is your best check. Before computing 36 × 24, round to 40 × 25 = 1000. Your answer should be near 1000 — not 216 or 8640. If your answer is off by a factor of 10, you almost certainly made the place-value error on a partial product. If it is off by a smaller amount, check your regrouping. Building the habit of estimating first means that large errors announce themselves immediately.
