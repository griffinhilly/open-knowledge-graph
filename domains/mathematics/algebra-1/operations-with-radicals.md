---
id: operations-with-radicals
title: Operations with Radicals
domain: mathematics
course: algebra-1
prerequisites:
- id: radical-expressions-simplifying
  type: hard
- id: combining-like-terms
  type: hard
builds-toward:
- rationalizing-denominators
- complex-numbers-intro
tags:
- radicals
- addition
- subtraction
- multiplication
- operations
stage: abstract-reasoning
status: validated
---
# Operations with Radicals

## Core Idea
Adding and subtracting radicals works like combining like terms: you can only combine radicals with the same radicand. 3sqrt(5) + 7sqrt(5) = 10sqrt(5), but 3sqrt(5) + 7sqrt(3) cannot be simplified. Sometimes simplification is needed first: sqrt(12) + sqrt(27) = 2sqrt(3) + 3sqrt(3) = 5sqrt(3). Multiplying radicals uses the product rule: sqrt(a) × sqrt(b) = sqrt(ab). Dividing radicals uses the quotient rule: sqrt(a)/sqrt(b) = sqrt(a/b). These operations are needed when working with the quadratic formula, distance formula, and trigonometry.

## How It's Best Learned
Draw the analogy to like terms explicitly: just as 3x + 7x = 10x, 3sqrt(5) + 7sqrt(5) = 10sqrt(5). Practice simplifying radicals first, then combining. For multiplication, practice the product rule and simplify the result. Include rationalizing the denominator (multiplying numerator and denominator by the radical to clear it from the denominator). Practice mixed operations.

## Common Misconceptions
- Adding radicands: sqrt(3) + sqrt(5) = sqrt(8) (this is incorrect — they are unlike radicals).
- Not simplifying before combining (missing that sqrt(12) + sqrt(27) can be combined after simplification).
- Thinking you cannot multiply unlike radicals (you can: sqrt(3) × sqrt(5) = sqrt(15)).

## Questions

```yaml
- question: "A student wants to simplify √12 + √75. What must they do first, and what is the final simplified result?"
  type: multiple-choice
  options:
    - "Add the radicands: √12 + √75 = √87"
    - "Simplify each radical first: √12 = 2√3 and √75 = 5√3, then combine like radicals to get 7√3"
    - "Multiply using the product rule: √12 × √75 = √900 = 30"
    - "Recognize that 12 and 75 are different radicands, so the expression cannot be simplified"
  answer: 1
  explanation: "The critical first step is simplification: √12 = √(4×3) = 2√3, and √75 = √(25×3) = 5√3. Once simplified, both radicals share the radicand 3 — they are like radicals — and combine exactly like like terms: 2√3 + 5√3 = 7√3. Option A is the most dangerous misconception: adding radicands (√12 + √75 ≠ √87) violates the rule that you can only combine radicals with matching radicands. Option D is a common mistake when students skip the simplification step."

- question: "Which of the following is correct?"
  type: multiple-choice
  options:
    - "√3 + √5 = √8, because you add the radicands just as you add the numbers under the radical"
    - "√3 × √5 = √15, because the product rule allows multiplication of unlike radicals"
    - "√3 + √5 = √15, because you multiply the radicands when the radicals are unlike"
    - "√3 × √5 cannot be simplified because the radicands are different"
  answer: 1
  explanation: "The product rule states √a × √b = √(ab) for a,b ≥ 0 — unlike radicals CAN be multiplied. √3 × √5 = √15 (which cannot be further simplified). In contrast, √3 + √5 cannot be combined because addition of radicals requires identical radicands. Option A (√3 + √5 = √8) is the most common misconception — adding radicands as if they were ordinary numbers. The operations of multiplication and addition follow completely different rules for radicals: unlike radicals can be multiplied but not added."

- question: "3√5 + 7√5 = 10√5, for the same reason that 3x + 7x = 10x — in both cases, the coefficients count how many of the same 'unit' you have."
  type: true-false
  answer: true
  explanation: "This analogy is the key conceptual insight: the radical √5 acts exactly like a variable. The coefficients (3 and 7) count how many copies of that unit you have, and like any like-terms combination, you add the coefficients while keeping the shared unit unchanged. 3√5 + 7√5 = (3 + 7)√5 = 10√5, just as 3x + 7x = 10x. The rule only applies when the radicands are identical — you cannot combine 3√5 and 7√3 for the same reason you cannot combine 3x and 7y."

- question: "√2 + √8 cannot be simplified because 2 and 8 are different radicands."
  type: true-false
  answer: false
  explanation: "This is incorrect — simplification reveals hidden like radicals. √8 = √(4×2) = 2√2. After simplification, √2 + √8 = √2 + 2√2 = 3√2. The lesson: always simplify each radical fully before concluding that radicals are unlike. Two radicals may appear to have different radicands but become like radicals after simplification. The procedure is: simplify first, then check for matching radicands, then combine."

- question: "Explain why √12 + √27 can be simplified even though 12 and 27 are different numbers. What makes two radicals 'like radicals,' and why does simplification matter?"
  type: short-answer
  answer: "√12 = 2√3 (because 12 = 4 × 3, and √4 = 2) and √27 = 3√3 (because 27 = 9 × 3, and √9 = 3). After simplification, both radicals share the radicand 3, making them like radicals. Like radicals are those with identical radicands after full simplification — they function as the same unit. Since 2√3 + 3√3 = (2+3)√3 = 5√3, the sum simplifies. Without simplifying first, the different surface radicands (12 and 27) make the radicals appear unlike, leading to the wrong conclusion that they cannot be combined."
  explanation: "Simplification is the unlocking step. Different radicands do not necessarily mean unlike radicals — they may share a common simplified form. The reliable procedure is always: fully simplify each radical by extracting the largest perfect-square factor, then check whether the simplified radicands match. Only after this step can you correctly determine whether addition or subtraction is possible."
```

## Explainer

You already know how to simplify radical expressions — for example, √12 = 2√3 — and you know how to combine like terms, such as 3x + 7x = 10x. Operations with radicals bring these two skills together. The central principle is that **like radicals** — radicals sharing the same radicand — behave exactly like like terms. Just as 3x and 7x combine to give 10x because they share the same "unit" x, the expressions 3√5 and 7√5 combine to give 10√5 because they share the same unit √5. The radical acts as the variable; the coefficient counts how many of it you have.

The important catch is that radicals often do not look alike until you simplify them. Consider √12 + √27. At first glance these seem unlike. But √12 = 2√3 and √27 = 3√3, so the sum becomes 2√3 + 3√3 = 5√3. The simplification step is what makes combining possible. The reliable procedure is: simplify each radical fully first, then look for matching radicands. If the radicands still differ after full simplification, the expression is already in simplest form — √2 + √3 cannot be simplified further, just as x + y cannot.

**Multiplication** follows the **product rule**: √a × √b = √(ab) for a, b ≥ 0. Unlike addition, you *can* multiply unlike radicals — √3 × √5 = √15. After multiplying, simplify the result: √6 × √10 = √60 = 2√15. For products involving binomials, use distribution: (2 + √3)(1 − √3) expands to 2 − 2√3 + √3 − 3 = −1 − √3. Notice that √3 × √3 = 3, eliminating the radical entirely — this is the key step in **rationalizing denominators**, where you multiply numerator and denominator by the radical that appears in the denominator to clear it away.

**Division** uses the **quotient rule**: √a / √b = √(a/b). Together, the product and quotient rules make radicals behave like a coherent algebraic system. When you later encounter the quadratic formula, the distance formula, and trigonometric identities, you will find radicals everywhere. Fluency with these operations — simplifying, combining, multiplying, and rationalizing — is what lets you work through those formulas without getting stuck on the radical arithmetic itself.
