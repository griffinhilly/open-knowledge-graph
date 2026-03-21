---
id: two-digit-multiplication-one-digit-3rd
title: Multiplying Two-Digit by One-Digit Numbers
domain: mathematics
course: 3rd-grade
prerequisites:
- id: multiplication-facts-within-100
  type: hard
- id: place-value-three-digits-3rd
  type: soft
- id: area-as-multiplication-3rd
  type: soft
builds-toward:
- two-digit-by-one-digit-multiplication
tags:
- multiplication
- two-digit
- place-value
stage: concrete-operations
status: draft
---

# Multiplying Two-Digit by One-Digit Numbers

## Core Idea
Multiplying a two-digit number by a one-digit number can be done by decomposing the two-digit number into tens and ones, multiplying each part, and adding: 24 × 3 = (20 × 3) + (4 × 3) = 60 + 12 = 72. Arrays and area models support this understanding.

## Questions

```yaml
- question: "To compute 36 × 4, a student thinks: '30 × 4 = 120, and 6 × 4 = 24, so 36 × 4 = 144.' Why does this method always work?"
  type: multiple-choice
  options:
    - "It works because you can always split the second number in multiplication"
    - "It works because multiplying by 10 is easy"
    - "It works because 36 = 30 + 6, and multiplying each part by 4 then adding gives the same result as multiplying 36 × 4 directly — this is the distributive property"
    - "It works by coincidence for this particular problem"
  answer: 2
  explanation: "This is the distributive property: a × (b + c) = (a × b) + (a × c). Because 36 = 30 + 6, computing 4 × 30 and 4 × 6 separately then adding gives the correct total. This is not a trick — it works for any two-digit multiplication because any two-digit number can be decomposed into its tens and ones. Understanding why it works (not just how) is what makes it extendable to larger numbers."

- question: "A student computes 47 × 6 by thinking '40 × 6 = 240' but writes 240 as her final answer, forgetting to add anything else. What error did she make?"
  type: multiple-choice
  options:
    - "She multiplied by the wrong number"
    - "She forgot to also multiply the ones digit (7 × 6 = 42) and add it to the tens product"
    - "She should have multiplied 47 by 60 instead of 6"
    - "She rounded 47 incorrectly"
  answer: 1
  explanation: "When decomposing 47 into 40 + 7, you must multiply BOTH parts by 6: 40 × 6 = 240 AND 7 × 6 = 42. The final answer is 240 + 42 = 282. Computing only the tens partial product (240) and stopping is the most common error with this strategy — the ones partial product is always required."

- question: "24 × 3 = (20 × 3) + (4 × 3) because any two-digit number can be broken into its tens and ones, and each part can be multiplied independently."
  type: true-false
  answer: true
  explanation: "Correct. 24 = 20 + 4, so 24 × 3 = (20 + 4) × 3 = (20 × 3) + (4 × 3) = 60 + 12 = 72. This decomposition works because our number system is built on place value, and the distributive property guarantees that multiplying each part then adding equals multiplying the whole."

- question: "Decomposing a two-digit number into tens and ones before multiplying is only necessary when you cannot remember the answer."
  type: true-false
  answer: false
  explanation: "Decomposing is not a memory workaround — it is the fundamental strategy that scales to all larger multiplications. Understanding why it works (place value + distributive property) is more important than any specific answer, because the identical method extends to two-digit by two-digit, three-digit by two-digit, and beyond. The strategy IS the mathematical understanding."

- question: "Explain why multiplying 34 × 7 gives the same answer whether you compute it directly or by decomposing as (30 × 7) + (4 × 7)."
  type: short-answer
  answer: "34 = 30 + 4, and the distributive property states that a × (b + c) = (a × b) + (a × c). So 34 × 7 = (30 + 4) × 7 = (30 × 7) + (4 × 7) = 210 + 28 = 238. Both methods multiply the same total by 7 — the decomposition just breaks it into two simpler pieces using 34's place-value structure. Because the parts add up to the whole number, their products add up to the whole product."
  explanation: "The distributive property is the mathematical guarantee that this always works. You are not approximating — you are computing the exact same multiplication in two steps instead of one. This is why the decomposition strategy is not just a shortcut but a genuine method that produces exact results for any two-digit multiplication."
```

## Explainer

You know your multiplication facts up to 10 × 10. Now the question is: how do you multiply when one of the numbers is bigger than 10? The answer is to use **place value** to break the bigger number apart, multiply each piece using facts you already know, and add the results back together.

Take 24 × 3. You can think of 24 as 20 + 4. Multiplying each part by 3: 20 × 3 = 60, and 4 × 3 = 12. Then add: 60 + 12 = 72. This strategy is called **decomposing** the two-digit number into its tens and ones. You're not doing anything new — just applying your existing multiplication facts to smaller pieces.

The area model makes this visual. Draw a rectangle that is 24 units wide and 3 units tall. Split the width into two sections: 20 and 4. Now you have two smaller rectangles. The first is 20 × 3 = 60. The second is 4 × 3 = 12. The total area — the total product — is 60 + 12 = 72. This is the same calculation, just drawn as a picture. The area model works because area itself is multiplication (length × width), which is why your soft prerequisite connects here.

This decomposition strategy is the foundation of all multi-digit multiplication. In later grades, you'll use it to multiply two-digit numbers by two-digit numbers, or even larger. Every time, the idea is the same: break numbers into place-value parts, multiply each part, add up the partial products. Learning it well now — including understanding *why* it works, not just *how* to do it — will make all future multiplication much more approachable.
