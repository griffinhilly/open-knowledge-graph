---
id: sigma-notation
title: Sigma Notation
domain: mathematics
course: algebra-2
prerequisites:
- id: arithmetic-sequences-and-series
  type: hard
- id: geometric-sequences-and-series
  type: hard
builds-toward:
- binomial-theorem
- riemann-sums
tags:
- sequences
- series
- sigma-notation
- summation
stage: formal-systems
status: validated
---
# Sigma Notation

## Core Idea
Sigma notation (summation notation) uses the Greek letter sigma to compactly express sums. The expression sum from i=1 to n of a_i means a_1 + a_2 + ... + a_n. The variable i is the index, the lower and upper bounds define the range, and the expression after sigma defines each term. Sigma notation is essential for expressing series, statistical formulas, and integral approximations.

## How It's Best Learned
Practice expanding sigma notation into explicit sums and condensing explicit sums into sigma notation. Evaluate specific sums. Learn common summation formulas: sum of i = n(n+1)/2, sum of i^2 = n(n+1)(2n+1)/6. Apply to arithmetic and geometric series. Show that the index variable is a "dummy variable" (the choice of letter does not matter).

## Common Misconceptions
- Confusing the index of summation with a fixed value.
- Off-by-one errors in the bounds.
- Thinking the index must start at 1 (it can start at any integer).
- Not recognizing that changing the dummy variable does not change the sum.

## Explainer

You have worked with arithmetic series (sums of terms with constant differences) and geometric series (sums of terms with constant ratios). Both required writing out a pattern like 1 + 4 + 9 + 16 + 25 + ... and using a formula for the total. **Sigma notation** provides a compact, unambiguous way to express any such sum — or any sum at all — without relying on ellipses or asking the reader to guess what the pattern is. The symbol Σ (capital Greek sigma, standing for "sum") acts like a compact loop instruction.

The anatomy of a sigma expression: the subscript below Σ (like i = 1) names the **index variable** and its starting value; the superscript above (like n) is the stopping value; and the expression to the right of Σ (like i²) defines each term as a function of the index. To evaluate, substitute i = 1, then i = 2, and so on up to i = n, adding each result. So Σᵢ₌₁⁴ (2i + 1) = (2·1+1) + (2·2+1) + (2·3+1) + (2·4+1) = 3 + 5 + 7 + 9 = 24. Going in reverse — seeing 3 + 5 + 7 + 9 and writing sigma notation for it — requires identifying the general formula for the i-th term (here, 2i+1) and determining the correct bounds (i = 1 to 4).

The index variable is a **dummy variable**: its name carries no meaning outside the sum. Σᵢ₌₁ⁿ i², Σⱼ₌₁ⁿ j², and Σₖ₌₁ⁿ k² are identical — the letter chosen doesn't matter. This same idea will appear again with integration variables in calculus. The bounds, however, are not interchangeable: off-by-one errors are the most common mistake. Always check: does plugging in the lower bound give the first term you want? Does plugging in the upper bound give the last?

Three summation formulas appear constantly and are worth memorizing: Σᵢ₌₁ⁿ 1 = n (summing the constant 1 exactly n times gives n), Σᵢ₌₁ⁿ i = n(n+1)/2 (sum of the first n positive integers, derivable by the pairing trick from your arithmetic series work), and Σᵢ₌₁ⁿ i² = n(n+1)(2n+1)/6. Sigma notation is the language of Riemann sums — the rectangular approximations you will use to define the definite integral — and every statistical formula from variance to regression. Fluency with it now pays dividends throughout calculus and beyond.
