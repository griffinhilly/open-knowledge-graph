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

## Explainer

You already know how to simplify radical expressions — for example, √12 = 2√3 — and you know how to combine like terms, such as 3x + 7x = 10x. Operations with radicals bring these two skills together. The central principle is that **like radicals** — radicals sharing the same radicand — behave exactly like like terms. Just as 3x and 7x combine to give 10x because they share the same "unit" x, the expressions 3√5 and 7√5 combine to give 10√5 because they share the same unit √5. The radical acts as the variable; the coefficient counts how many of it you have.

The important catch is that radicals often do not look alike until you simplify them. Consider √12 + √27. At first glance these seem unlike. But √12 = 2√3 and √27 = 3√3, so the sum becomes 2√3 + 3√3 = 5√3. The simplification step is what makes combining possible. The reliable procedure is: simplify each radical fully first, then look for matching radicands. If the radicands still differ after full simplification, the expression is already in simplest form — √2 + √3 cannot be simplified further, just as x + y cannot.

**Multiplication** follows the **product rule**: √a × √b = √(ab) for a, b ≥ 0. Unlike addition, you *can* multiply unlike radicals — √3 × √5 = √15. After multiplying, simplify the result: √6 × √10 = √60 = 2√15. For products involving binomials, use distribution: (2 + √3)(1 − √3) expands to 2 − 2√3 + √3 − 3 = −1 − √3. Notice that √3 × √3 = 3, eliminating the radical entirely — this is the key step in **rationalizing denominators**, where you multiply numerator and denominator by the radical that appears in the denominator to clear it away.

**Division** uses the **quotient rule**: √a / √b = √(a/b). Together, the product and quotient rules make radicals behave like a coherent algebraic system. When you later encounter the quadratic formula, the distance formula, and trigonometric identities, you will find radicals everywhere. Fluency with these operations — simplifying, combining, multiplying, and rationalizing — is what lets you work through those formulas without getting stuck on the radical arithmetic itself.
