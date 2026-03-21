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

## Questions

```yaml
- question: "You want to determine whether the series Σ(3n/(4n+1))ⁿ converges. Which test is most natural, and what is the conclusion?"
  type: multiple-choice
  options:
    - "Ratio Test: compute the ratio of consecutive terms; it concludes divergence"
    - "Root Test: take the nth root to get L = 3/4 < 1, conclude absolute convergence"
    - "Comparison Test: compare to the harmonic series and conclude divergence"
    - "Integral Test: integrate (3x/(4x+1))^x and conclude convergence"
  answer: 1
  explanation: "The nth term is raised to the nth power — exactly the structure where the Root Test shines, because the nth root removes the exponent: |aₙ|^(1/n) = 3n/(4n+1) → 3/4 as n → ∞. Since L = 3/4 < 1, the series converges absolutely. The Ratio Test could work but requires computing the ratio of (3n/(4n+1))ⁿ and (3(n+1)/(4(n+1)+1))^(n+1), which is significantly messier. Whenever you see (expression)^n as the nth term, the Root Test is the natural first choice."

- question: "You apply the Root Test to a series and compute L = lim_{n→∞} |aₙ|^{1/n} = 1. What can you conclude?"
  type: multiple-choice
  options:
    - "The series converges absolutely, because L = 1 means the terms shrink at a geometric rate"
    - "The series diverges, because L = 1 means the terms do not go to zero"
    - "The series converges conditionally but not absolutely"
    - "The test is inconclusive — both convergent and divergent series can yield L = 1"
  answer: 3
  explanation: "L = 1 is the Root Test's inconclusive zone. The harmonic series Σ1/n diverges and gives L = 1; the p-series Σ1/n² converges and also gives L = 1. When L = 1, the Root Test provides no information about convergence. You must switch to a different test — Comparison, Limit Comparison, Integral Test, or p-series recognition. This is the most common error: treating L = 1 as a conclusion rather than a signal to switch tests."

- question: "The Root Test and Ratio Test are theoretically equivalent in power: when both are applicable and the limits exist, they yield the same value of L."
  type: true-false
  answer: true
  explanation: "Both tests ultimately compare the series to a geometric series. When both are applicable and the limits exist, they yield the same L and therefore the same conclusion (converge if L < 1, diverge if L > 1, inconclusive if L = 1). The difference is computational convenience: the Root Test handles nth-power expressions cleanly, while the Ratio Test handles factorials cleanly. Choosing the right test saves computation, but theoretically they are equivalent in what they can detect."

- question: "If the Root Test gives L = 1, the series converges conditionally."
  type: true-false
  answer: false
  explanation: "L = 1 is simply inconclusive — the Root Test gives no information whatsoever. Conditional convergence is a specific property (the series converges but not absolutely) that cannot be determined from L = 1 alone. The harmonic series Σ1/n (which diverges outright) and the alternating harmonic series Σ(−1)ⁿ/n (which converges conditionally) both produce L = 1. The test cannot distinguish among these cases."

- question: "Why is the Root Test particularly well-suited for series of the form Σ(f(n))ⁿ, and what happens algebraically when you apply it?"
  type: short-answer
  answer: "The Root Test computes L = lim_{n→∞} |aₙ|^{1/n}. When aₙ = (f(n))ⁿ, taking the nth root gives |aₙ|^{1/n} = |(f(n))ⁿ|^{1/n} = |f(n)|^{n·(1/n)} = |f(n)|. The exponent n cancels exactly with the 1/n from the root, leaving a simple limit of |f(n)| as n → ∞. This algebraic cancellation is precisely what makes the test powerful for these series: a seemingly complex nth-power expression collapses to a straightforward limit."
  explanation: "By contrast, applying the Ratio Test to (f(n))^n requires computing (f(n+1))^{n+1} / (f(n))^n, which involves both a changing ratio and a changing exponent — usually messier. The Root Test is the right tool not just because it works, but because it makes the computation almost trivial for this class of series. Recognizing the (expression)^n pattern is the key skill."
```

## Explainer

The Root Test is a convergence test for infinite series that works by comparing a series to a geometric series — one of the few series types whose convergence you can determine completely. Recall that a geometric series Σrⁿ converges if and only if |r| < 1. The Root Test asks: does the n-th term of your series behave like rⁿ for some r, and if so, what is r? It answers this by looking at the n-th root of the n-th term.

The key quantity is L = lim_{n→∞} |aₙ|^{1/n}. If this limit exists and equals L, then for large n, |aₙ| behaves like Lⁿ. If L < 1, the terms shrink like a convergent geometric series, so the series converges absolutely. If L > 1, the terms grow, so the series diverges (the terms don't even go to zero). If L = 1, the test gives no information — both convergent and divergent series can have L = 1, so you need a different test.

The test shines on series where the n-th term is itself an n-th power, because the n-th root then simplifies cleanly. For example, consider Σ(2n/(3n+1))^n. Taking the n-th root gives |aₙ|^{1/n} = 2n/(3n+1) → 2/3 as n → ∞. Since 2/3 < 1, the series converges absolutely. By contrast, the Ratio Test on this series would require computing ratios of (2n/(3n+1))^n and (2(n+1)/(3(n+1)+1))^{n+1}, which is messier. Whenever you see an expression raised to the n-th power as the n-th term, the Root Test is usually your first choice.

Compare the Root Test to the Ratio Test, which you already know: both tests ultimately compare the series to a geometric series, and they are theoretically equivalent in power (if one gives L, the other gives the same L). However, the Root Test handles n-th powers more cleanly, while the Ratio Test handles factorials more cleanly (because factorial ratios simplify to single terms). When both are applicable, they give the same conclusion. The L = 1 inconclusive case is unavoidable — this is where series like Σ1/n (diverges) and Σ1/n² (converges) both land, and p-series or comparison tests are needed instead.
