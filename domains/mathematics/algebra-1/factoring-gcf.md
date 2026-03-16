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

## Explainer

Factoring out the GCF is the distributive property run in reverse. You already know how to expand: 3x²(2x + 3) gives you 6x³ + 9x² by multiplying the outside term into each term inside the parentheses. Factoring out the GCF asks the opposite question — given 6x³ + 9x², can you find what was "outside" and what was "inside"? The answer is found by identifying the largest factor that all terms share.

Finding the GCF has two parts: the numerical coefficient and the variable part. For 6x³ + 9x², the coefficients are 6 and 9; the greatest common factor of those numbers is 3. The variable parts are x³ and x²; the GCF uses the lowest exponent, which is x². Putting them together: the GCF is 3x². Now divide each term by 3x² to find what goes inside the parentheses: 6x³ ÷ 3x² = 2x, and 9x² ÷ 3x² = 3. So the factored form is 3x²(2x + 3). You can always verify by redistributing — expand 3x²(2x + 3) and confirm you get back the original expression.

The most common error is factoring out something smaller than the greatest common factor. If you only pull out 3 from 6x³ + 9x², you get 3(2x³ + 3x²), which is technically factored but not completely — there is still an x² hiding inside that could come out. The word "greatest" matters: you want the largest possible factor, not just any common factor. Similarly, don't forget the variable part: from 6x² + 9x, the GCF is 3x (not just 3), giving 3x(2x + 3).

Factoring out the GCF is always the first step in any factoring problem, before you try other techniques like factoring trinomials or difference of squares. Even when a polynomial needs several rounds of factoring, clearing the GCF first makes every subsequent step simpler. Think of it as tidying up before rearranging furniture — it makes everything else easier to see and handle. The factored form is also useful for solving equations: if you need to solve 6x³ + 9x² = 0, factoring to 3x²(2x + 3) = 0 immediately reveals the solutions x = 0 (from the 3x² factor) and x = −3/2 (from the 2x + 3 factor).
