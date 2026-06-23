---
id: factoring-gcf
title: Factoring Out the GCF
domain: mathematics
course: algebra-1
prerequisites:
- id: distributive-property
  type: hard
- id: polynomials-intro
  type: hard
- id: adding-subtracting-polynomials
  type: soft
- id: distributive-property-multiplication-3rd
  type: hard
builds-toward:
- factoring-trinomials
- factoring-completely
- solving-quadratics-by-factoring
tags:
- factoring
- GCF
- polynomials
- distributive-property
stage: abstract-reasoning
status: validated
---
# Factoring Out the GCF

## Core Idea
Factoring out the greatest common factor (GCF) is the reverse of the distributive property: instead of expanding a(b + c) into ab + ac, you start with ab + ac and write it as a(b + c). To factor 6x³ + 9x², find the GCF of the coefficients (3) and the lowest power of x (x²), giving 3x²(2x + 3). This is always the first step in any factoring problem — before trying other methods, always check for a GCF. Factoring is essential for solving polynomial equations, simplifying rational expressions, and finding roots.

## How It's Best Learned
Practice finding the GCF of monomials first (both numerical and variable parts). Then factor it out of two-term, three-term, and four-term polynomials. Verify by redistributing. Emphasize that factoring out the GCF should always be the first step, even when other factoring techniques will follow. Include negative leading coefficients (factor out −1 when helpful).

## Common Misconceptions
- Not finding the greatest common factor (factoring out 3 when 6 is common to all terms).
- Forgetting to factor the variable part (factoring out 3 from 6x² + 9x instead of 3x).
- Leaving 0 instead of 1 when the GCF equals one of the terms (e.g., factoring 5x + 5 as 5(x + 0) instead of 5(x + 1)).

## Questions

```yaml
- question: "A student factors 12x⁴ + 8x² and writes 4(3x⁴ + 2x²). Their teacher says this is not fully factored. Why?"
  type: multiple-choice
  options:
    - "The student should have factored out 2 instead of 4, since 2 divides both coefficients"
    - "The student only factored out the numerical GCF; the GCF is actually 4x² (including the variable part), giving 4x²(3x² + 2)"
    - "The student's answer is correct; 4 is the greatest common factor of 12 and 8"
    - "The student should have factored out x⁴ instead, since that is the highest power present"
  answer: 1
  explanation: "Finding the GCF has two parts: the numerical coefficient AND the variable part. The numerical GCF of 12 and 8 is 4 — the student got that right. But the variable GCF uses the lowest power present: both terms have at least x², so x² is also part of the GCF. The complete GCF is 4x², not just 4. Writing 4(3x⁴ + 2x²) is technically factored but not *completely* factored — the leftover expression still has a common factor of x². This is the most common GCF error: remembering the numbers but forgetting the variables."

- question: "What is the completely factored form of 5x³ + 5x²?"
  type: multiple-choice
  options:
    - "5(x³ + x²)"
    - "5x(x² + x)"
    - "5x²(x + 1)"
    - "x²(5x + 5)"
  answer: 2
  explanation: "The GCF of 5x³ and 5x² is 5x² — the numerical GCF is 5, and the variable GCF is x² (the lowest power). Dividing each term: 5x³ ÷ 5x² = x, and 5x² ÷ 5x² = 1. So the factored form is 5x²(x + 1). Options A and B factor out partial amounts (just 5, or just 5x), leaving the expression incompletely factored. Option D factors out only x², omitting the numerical GCF. The critical check: when one term's entire value equals the GCF, what remains inside the parentheses for that term is 1, not 0."

- question: "Factoring 6x + 6 as 6(x + 0) is a valid application of GCF factoring because 6 divides both terms."
  type: true-false
  answer: false
  explanation: "When the GCF equals one of the terms exactly, that term leaves a 1 inside the parentheses — not a 0. Here, 6x ÷ 6 = x, and 6 ÷ 6 = 1. The correct factored form is 6(x + 1). Writing 6(x + 0) would expand back to 6x + 0 = 6x, which is not the original expression. This error typically comes from confusing 'the term is gone after factoring' with 'the term becomes 0' — but factoring is the reverse of distribution, and distributing 6 back into 6(x + 1) gives you 6x + 6, confirming the correct answer."

- question: "You can always verify a GCF factoring by redistributing (expanding) the factored form and confirming it equals the original expression."
  type: true-false
  answer: true
  explanation: "Because GCF factoring is the reverse of the distributive property, expanding the result should always recover the original expression exactly. This check is reliable and fast: 3x²(2x + 3) → 6x³ + 9x² confirms the factoring is correct. If the expansion doesn't match, something went wrong — either the GCF was wrong, or a term inside the parentheses was computed incorrectly. Making this verification a habit catches almost every factoring error."

- question: "A classmate factors 8x³ + 12x² as 2(4x³ + 6x²). Explain why this is not fully factored, and show the correct completely factored form."
  type: short-answer
  answer: "The classmate factored out only 2, but the GCF of 8x³ and 12x² is 4x² — both the full numerical GCF (4, not 2) and the variable GCF (x²). To find the correct GCF: the GCF of 8 and 12 is 4; both terms contain at least x², so x² is the variable GCF. Dividing: 8x³ ÷ 4x² = 2x, and 12x² ÷ 4x² = 3. The correct factored form is 4x²(2x + 3). Verify: 4x²(2x + 3) = 8x³ + 12x² ✓"
  explanation: "The factoring 2(4x³ + 6x²) is not wrong — it does check out — but it is incomplete. 'Greatest' in GCF means you must factor out the *largest* possible common factor. The expression inside the parentheses, 4x³ + 6x², still has a common factor (2x²), so more factoring is possible. Fully factored means no further common factor remains. The word 'greatest' is doing real work here: any common factor won't do — it must be the greatest one."
```

## Explainer

Factoring out the GCF is the distributive property run in reverse. You already know how to expand: 3x²(2x + 3) gives you 6x³ + 9x² by multiplying the outside term into each term inside the parentheses. Factoring out the GCF asks the opposite question — given 6x³ + 9x², can you find what was "outside" and what was "inside"? The answer is found by identifying the largest factor that all terms share.

Finding the GCF has two parts: the numerical coefficient and the variable part. For 6x³ + 9x², the coefficients are 6 and 9; the greatest common factor of those numbers is 3. The variable parts are x³ and x²; the GCF uses the lowest exponent, which is x². Putting them together: the GCF is 3x². Now divide each term by 3x² to find what goes inside the parentheses: 6x³ ÷ 3x² = 2x, and 9x² ÷ 3x² = 3. So the factored form is 3x²(2x + 3). You can always verify by redistributing — expand 3x²(2x + 3) and confirm you get back the original expression.

The most common error is factoring out something smaller than the greatest common factor. If you only pull out 3 from 6x³ + 9x², you get 3(2x³ + 3x²), which is technically factored but not completely — there is still an x² hiding inside that could come out. The word "greatest" matters: you want the largest possible factor, not just any common factor. Similarly, don't forget the variable part: from 6x² + 9x, the GCF is 3x (not just 3), giving 3x(2x + 3).

Factoring out the GCF is always the first step in any factoring problem, before you try other techniques like factoring trinomials or difference of squares. Even when a polynomial needs several rounds of factoring, clearing the GCF first makes every subsequent step simpler. Think of it as tidying up before rearranging furniture — it makes everything else easier to see and handle. The factored form is also useful for solving equations: if you need to solve 6x³ + 9x² = 0, factoring to 3x²(2x + 3) = 0 immediately reveals the solutions x = 0 (from the 3x² factor) and x = −3/2 (from the 2x + 3 factor).
