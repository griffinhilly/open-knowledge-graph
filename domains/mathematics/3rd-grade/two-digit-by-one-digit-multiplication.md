---
id: two-digit-by-one-digit-multiplication
title: Two-Digit by One-Digit Multiplication
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multiplication-facts-threes-through-nines
  type: hard
- id: distributive-property-3rd
  type: hard
- id: place-value-tens-and-ones
  type: soft
builds-toward:
- multi-digit-multiplication
tags:
- multiplication
- algorithms
- place-value
- two-digit
stage: concrete-operations
status: draft
---

# Two-Digit by One-Digit Multiplication

## Core Idea
To multiply 24 × 3, use the distributive property: break 24 into 20 + 4, then (20 × 3) + (4 × 3) = 60 + 12 = 72. Area models (rectangles divided into tens and ones) support this strategy before introducing the standard vertical algorithm.

## Questions

```yaml
- question: "A student computes 47 × 3 by thinking: '40 × 3 = 120, and 7 × 3 = 21, so 120 + 21 = 141.' Which property makes this approach valid?"
  type: multiple-choice
  options:
    - "Commutative property — swapping the order of 47 and 3"
    - "Distributive property — splitting 47 into (40 + 7) and multiplying each part by 3"
    - "Associative property — regrouping the factors in a different order"
    - "No property — this only works by coincidence for this particular problem"
  answer: 1
  explanation: "The distributive property states that a × (b + c) = (a × b) + (a × c). Here, 3 × 47 = 3 × (40 + 7) = (3 × 40) + (3 × 7) = 120 + 21 = 141. This property is what makes the decomposition-by-place-value strategy reliable — it guarantees that splitting the two-digit number and multiplying each part gives the same result as multiplying the whole number."

- question: "A student computes 25 × 4 as follows: '2 × 4 = 8, then 5 × 4 = 20, so the answer is 820.' What mistake did the student make?"
  type: multiple-choice
  options:
    - "They should have multiplied the ones digit before the tens digit"
    - "They treated the digit 2 as just 2, but it is in the tens place and represents 20 — so 20 × 4 = 80, not 8, giving (80 + 20) = 100"
    - "They cannot use this strategy unless they first draw an area model"
    - "The answer 820 is actually correct"
  answer: 1
  explanation: "This is the most common mistake when applying the distributive strategy: forgetting place value. In 25, the digit 2 is in the tens place, representing 20 — not 2. So 25 × 4 = (20 + 5) × 4 = (20 × 4) + (5 × 4) = 80 + 20 = 100. The area model makes this concrete: the left rectangle is 20 units wide, not 2 units wide."

- question: "To multiply 63 × 4, you can break it apart as (60 × 4) + (3 × 4) and then add the results."
  type: true-false
  answer: true
  explanation: "Yes — this is a direct application of the distributive property with place-value decomposition. 63 = 60 + 3, so 63 × 4 = (60 × 4) + (3 × 4) = 240 + 12 = 252. Breaking into tens and ones always works for any two-digit number because every two-digit number equals (tens value) + (ones value)."

- question: "In the area model for 34 × 5, the total area equals 34 + 5 = 39."
  type: true-false
  answer: false
  explanation: "Adding the two dimensions gives the sum, not the product. The area of a rectangle = length × width. The area model for 34 × 5 shows a rectangle divided into a 30 × 5 section (area = 150) and a 4 × 5 section (area = 20). Total area = 150 + 20 = 170. Area represents multiplication, not addition."

- question: "Explain in your own words why you split a two-digit number into tens and ones before multiplying, and what mathematical property makes this valid."
  type: short-answer
  answer: "You split a two-digit number into tens and ones because every two-digit number is a sum of its tens value and ones value (e.g., 37 = 30 + 7). The distributive property guarantees that you can multiply each part separately and add the results: 37 × 6 = (30 × 6) + (7 × 6) = 180 + 42 = 222. Each individual multiplication then involves a fact you already know (like 7 × 6) or a simple tens calculation (like 30 × 6 = 180)."
  explanation: "The distributive property is what makes all multi-digit multiplication possible — it is also the foundation of the standard algorithm. When you 'carry' in vertical multiplication, you are performing the same decomposition in a compressed form. Understanding the area-model method first makes the algorithm understandable rather than a memorized procedure."
```

## Explainer

You know your multiplication facts up through the nines table, and you've learned the **distributive property** — that a × (b + c) = (a × b) + (a × c). Two-digit by one-digit multiplication is what happens when you apply that property using place value. Since every two-digit number is built from tens and ones, you can always split it apart in a way that reduces the problem to single-digit facts you already know.

Take 24 × 3. The number 24 is 20 + 4 (two tens and four ones). Applying the distributive property: (20 + 4) × 3 = (20 × 3) + (4 × 3) = 60 + 12 = 72. Each multiplication in the second step is manageable: 4 × 3 = 12 is a basic fact, and 20 × 3 = 60 because 2 tens × 3 = 6 tens = 60. The **area model** makes this visual: draw a rectangle 24 units wide and 3 units tall, then draw a vertical line separating the 20-unit section from the 4-unit section. The total area equals the sum of the two smaller rectangles' areas.

Once the area model is solid, the standard vertical algorithm you'll use in higher grades is just a compact way to record the same process. When you write 24 × 3 vertically and compute 3 × 4 = 12 (write 2, carry 1), then 3 × 2 = 6 plus 1 carried = 7, you are doing exactly the same steps — just in a streamlined written form. The area model is the picture that makes the algorithm trustworthy; the algorithm is the area model compressed into notation.

The key habit to build is decomposing by place value before multiplying. Any two-digit number splits into tens and ones: 73 × 6 = (70 + 3) × 6 = 420 + 18 = 438. The tens digit always gets multiplied and scaled up by 10. This becomes automatic with practice, and it's exactly the mental process behind multi-digit multiplication of any size.
