---
id: root-test
title: Root Test
domain: mathematics
course: calculus-2
prerequisites:
  - id: sequences-convergence
    type: hard
  - id: ratio-test
    type: soft
builds-toward:
  - radius-and-interval-of-convergence
tags: [series, convergence-tests, root-test]
stage: formal-systems
status: validated
---

# Root Test

## Core Idea
The Root Test examines L = lim(n->infinity) |a_n|^(1/n). If L < 1, the series converges absolutely. If L > 1, it diverges. If L = 1, inconclusive. The root test is most useful when a_n involves an nth power, such as (expression)^n, where the nth root simplifies cleanly. It is equivalent in power to the ratio test but sometimes easier to apply.

## How It's Best Learned
Apply to series of the form (f(n))^n. Compare with the ratio test on the same series to see which is more convenient. Practice computing nth roots using properties of limits and logarithms.

## Common Misconceptions
- Trying to use the root test on series with factorials (the ratio test is usually better for those).
- Confusing |a_n|^(1/n) with |a_n^(1/n)| (they are the same, but the computation can be confusing).
- Drawing a conclusion when L = 1.

## Explainer

The Root Test is a convergence test for infinite series that works by comparing a series to a geometric series — one of the few series types whose convergence you can determine completely. Recall that a geometric series Σrⁿ converges if and only if |r| < 1. The Root Test asks: does the n-th term of your series behave like rⁿ for some r, and if so, what is r? It answers this by looking at the n-th root of the n-th term.

The key quantity is L = lim_{n→∞} |aₙ|^{1/n}. If this limit exists and equals L, then for large n, |aₙ| behaves like Lⁿ. If L < 1, the terms shrink like a convergent geometric series, so the series converges absolutely. If L > 1, the terms grow, so the series diverges (the terms don't even go to zero). If L = 1, the test gives no information — both convergent and divergent series can have L = 1, so you need a different test.

The test shines on series where the n-th term is itself an n-th power, because the n-th root then simplifies cleanly. For example, consider Σ(2n/(3n+1))^n. Taking the n-th root gives |aₙ|^{1/n} = 2n/(3n+1) → 2/3 as n → ∞. Since 2/3 < 1, the series converges absolutely. By contrast, the Ratio Test on this series would require computing ratios of (2n/(3n+1))^n and (2(n+1)/(3(n+1)+1))^{n+1}, which is messier. Whenever you see an expression raised to the n-th power as the n-th term, the Root Test is usually your first choice.

Compare the Root Test to the Ratio Test, which you already know: both tests ultimately compare the series to a geometric series, and they are theoretically equivalent in power (if one gives L, the other gives the same L). However, the Root Test handles n-th powers more cleanly, while the Ratio Test handles factorials more cleanly (because factorial ratios simplify to single terms). When both are applicable, they give the same conclusion. The L = 1 inconclusive case is unavoidable — this is where series like Σ1/n (diverges) and Σ1/n² (converges) both land, and p-series or comparison tests are needed instead.
