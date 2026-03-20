---
id: distributive-property-3rd
title: 'Distributive Property: Breaking Apart to Multiply'
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multiplication-facts-threes-through-nines
  type: hard
- id: associative-property-multiplication-3rd
  type: soft
builds-toward:
- two-digit-by-one-digit-multiplication
tags:
- multiplication
- properties
- area-models
stage: concrete-operations
status: draft
---

# Distributive Property: Breaking Apart to Multiply

## Core Idea
The distributive property states that 3 × 7 = 3 × (5 + 2) = (3 × 5) + (3 × 2). Breaking a number into parts and multiplying each part separately mirrors dividing a rectangle into smaller rectangles. This supports mental math and prepares for multi-digit algorithms.

## Questions

```yaml
- question: "A student needs to calculate 6 × 7 but is more confident with 6 × 5. Which approach correctly uses the distributive property?"
  type: multiple-choice
  options:
    - "6 × 7 = 6 × 5 + 7 (add the second factor to the first product)"
    - "6 × 7 = (6 × 5) + (6 × 2), because 7 = 5 + 2"
    - "6 × 7 = (6 × 5) × (6 × 2), because you multiply each part"
    - "6 × 7 = 6 × 5 + 5, because you just add another 5"
  answer: 1
  explanation: "The distributive property says you can break one factor into parts and multiply each part by the other factor, then add the products: 6 × 7 = 6 × (5 + 2) = (6 × 5) + (6 × 2) = 30 + 12 = 42. Option A adds 7 to the product instead of multiplying — a common error. Option C multiplies the partial products together instead of adding them. Option D arbitrarily adds 5 without mathematical justification."

- question: "To check the distributive property for 4 × 8, a student draws a rectangle that is 4 units tall and 8 units wide, then splits it into a 4 × 3 section and a 4 × 5 section. What is the total area?"
  type: multiple-choice
  options:
    - "(4 × 3) + (4 × 5) = 12 + 20 = 32, which equals 4 × 8"
    - "(4 + 3) × (4 + 5) = 7 × 9 = 63, because splitting changes the area"
    - "(4 × 3) × (4 × 5) = 12 × 20 = 240, because you multiply the parts"
    - "The total area cannot be determined without measuring the split"
  answer: 0
  explanation: "The area of the full rectangle is 4 × 8 = 32. Splitting it with a vertical line creates two smaller rectangles: 4 × 3 = 12 and 4 × 5 = 20. Adding them: 12 + 20 = 32. The split does not change the total area — it just reorganizes it. The key is that you ADD the partial products, not multiply them. This is why the distributive property works: you're counting the same space in a different way."

- question: "The distributive property only works when you break apart the second factor, not the first."
  type: true-false
  answer: false
  explanation: "The distributive property works symmetrically — you can break apart either factor. For 6 × 8, you could split the 6: (4 + 2) × 8 = (4 × 8) + (2 × 8) = 32 + 16 = 48. Or split the 8: 6 × (5 + 3) = (6 × 5) + (6 × 3) = 30 + 18 = 48. Both give the same answer. You choose which factor to split based on what makes the mental calculation easiest."

- question: "3 × (5 + 2) = (3 × 5) + (3 × 2) = 21 is a correct application of the distributive property."
  type: true-false
  answer: true
  explanation: "Yes — this is the distributive property applied correctly. 5 + 2 = 7, so 3 × 7 = 3 × (5 + 2). Distributing the 3 to each part gives (3 × 5) + (3 × 2) = 15 + 6 = 21. And 3 × 7 = 21 directly confirms the result. Each part of the sum gets multiplied by the same factor, then the partial products are added."

- question: "Why doesn't drawing a vertical line inside a rectangle change its total area, and how does this explain why the distributive property works?"
  type: short-answer
  answer: "The line reorganizes the rectangle into two smaller pieces but doesn't remove or add any space. The total area stays the same — you're just counting it in two parts instead of one. This shows that (a × b) + (a × c) = a × (b + c): splitting the width into b and c and multiplying each piece by the height a gives the same total as multiplying a by the full width."
  explanation: "The area model makes the distributive property feel inevitable rather than arbitrary. Students who can explain this connection understand multiplication as area — a deep geometric insight — rather than treating the property as a rule to apply by rote."
```

## Explainer

You already know your multiplication facts from 3s through 9s. The distributive property is a strategy that lets you use facts you know to compute facts you haven't memorized — or to make hard facts easier. The key idea is that multiplication distributes across addition: if you break a number into smaller pieces, you can multiply each piece separately and add the results. The total is exactly what you would have gotten by multiplying the original number.

The best way to see why this works is through an **area model**. Draw a rectangle that is 3 units tall and 7 units wide. Its area is 3 × 7 = 21. Now draw a vertical line that divides the rectangle into a 3 × 5 piece and a 3 × 2 piece. The total area is still 21, but now it is (3 × 5) + (3 × 2) = 15 + 6 = 21. The dividing line did not change the total — it just reorganized it. This visual proof is what makes the distributive property feel true rather than arbitrary.

Why would you ever want to split a number up? Because some splits are much easier to compute mentally. Suppose you need 6 × 8 and you are more confident with 6 × 5. Break 8 into 5 + 3: then 6 × 8 = (6 × 5) + (6 × 3) = 30 + 18 = 48. The property lets you use a comfortable foothold — a fact you know — to reach a fact that feels shakier. You can break either factor. For 7 × 8, you might split 7 into 5 + 2: (5 × 8) + (2 × 8) = 40 + 16 = 56.

This is not just a trick for 3rd grade — it is the same logic that powers long multiplication for larger numbers. When you multiply 34 × 6, you are actually computing (30 + 4) × 6 = (30 × 6) + (4 × 6) = 180 + 24 = 204. The algorithm you will learn for **two-digit by one-digit multiplication** is a structured way of applying the distributive property step by step. Understanding the property now means you will see the algorithm as a system that makes sense, not a set of steps to memorize.
